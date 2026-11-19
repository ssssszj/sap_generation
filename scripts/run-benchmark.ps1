[CmdletBinding()]
param(
    [ValidateSet("all", "generate", "judge", "collect")]
    [string]$Phase = "all",
    [switch]$ForceGeneration,
    [switch]$ForceJudge,
    [switch]$Reprepare,
    [switch]$UseExistingLegacyServer
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$projectRoot = Split-Path -Parent $PSScriptRoot
$experimentRoot = Join-Path $projectRoot "benchmark\experiment"
$configPath = Join-Path $experimentRoot "config.json"
$cli = Join-Path $projectRoot ".venv\Scripts\sapgen-experiment.exe"
$legacyProcess = $null
$startedLegacyServer = $false

function Invoke-ExperimentCli {
    param([Parameter(Mandatory)][string[]]$Arguments)

    & $script:cli --root $script:projectRoot @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "sapgen-experiment failed (exit $LASTEXITCODE): $($Arguments -join ' ')"
    }
}

function Test-HttpReady {
    param([Parameter(Mandatory)][string]$Url)

    try {
        $null = Invoke-WebRequest -Uri $Url -Method Get -TimeoutSec 5 -UseBasicParsing
        return $true
    }
    catch {
        return $false
    }
}

function Start-LegacyServer {
    param([Parameter(Mandatory)]$Config)

    $baseUri = [Uri]$Config.legacy_base_url
    if (Test-HttpReady -Url $baseUri.AbsoluteUri) {
        if (-not $UseExistingLegacyServer) {
            throw "Legacy URL is already serving. Stop it or rerun with -UseExistingLegacyServer: $($baseUri.AbsoluteUri)"
        }
        Write-Host "Using existing legacy server at $($baseUri.AbsoluteUri)"
        return
    }

    $legacyRoot = [string]$Config.legacy_project
    if (-not (Test-Path -LiteralPath $legacyRoot)) {
        throw "Legacy project does not exist: $legacyRoot"
    }

    $logRoot = Join-Path $experimentRoot "logs"
    New-Item -ItemType Directory -Force -Path $logRoot | Out-Null
    $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $stdoutPath = Join-Path $logRoot "sap-ver1-$stamp.stdout.log"
    $stderrPath = Join-Path $logRoot "sap-ver1-$stamp.stderr.log"

    $previousMaxTokens = $env:SAP_EXPERIMENT_MAX_TOKENS
    $previousTemperature = $env:SAP_EXPERIMENT_PROVIDER_DEFAULT_TEMPERATURE
    try {
        $env:SAP_EXPERIMENT_MAX_TOKENS = [string]$Config.max_output_tokens
        $env:SAP_EXPERIMENT_PROVIDER_DEFAULT_TEMPERATURE = "1"
        $script:legacyProcess = Start-Process `
            -FilePath "npm.cmd" `
            -ArgumentList @("run", "dev", "--", "--port", [string]$baseUri.Port) `
            -WorkingDirectory $legacyRoot `
            -WindowStyle Hidden `
            -RedirectStandardOutput $stdoutPath `
            -RedirectStandardError $stderrPath `
            -PassThru
        $script:startedLegacyServer = $true
    }
    finally {
        $env:SAP_EXPERIMENT_MAX_TOKENS = $previousMaxTokens
        $env:SAP_EXPERIMENT_PROVIDER_DEFAULT_TEMPERATURE = $previousTemperature
    }

    $deadline = (Get-Date).AddMinutes(2)
    while ((Get-Date) -lt $deadline) {
        if ($legacyProcess.HasExited) {
            throw "Legacy server exited early. See $stderrPath"
        }
        if (Test-HttpReady -Url $baseUri.AbsoluteUri) {
            Write-Host "Started legacy server at $($baseUri.AbsoluteUri)"
            return
        }
        Start-Sleep -Seconds 2
    }
    throw "Legacy server did not become ready within two minutes. See $stderrPath"
}

function Stop-LegacyServer {
    if ($startedLegacyServer -and $null -ne $legacyProcess -and -not $legacyProcess.HasExited) {
        Stop-Process -Id $legacyProcess.Id -Force
        $legacyProcess.WaitForExit()
        Write-Host "Stopped legacy server PID $($legacyProcess.Id)"
    }
}

function Export-ExperimentResults {
    $resultsRoot = Join-Path $projectRoot "benchmark\results"
    New-Item -ItemType Directory -Force -Path $resultsRoot | Out-Null
    $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $bundleRoot = Join-Path $resultsRoot "sap-three-arm-$stamp"
    New-Item -ItemType Directory -Force -Path $bundleRoot | Out-Null

    $files = @(
        "config.json",
        "sample.json",
        "fetch-report.json",
        "input-report.json",
        "generation-report.json",
        "evaluation-report.json",
        "summary.json",
        "scores.csv",
        "score-report.md"
    )
    foreach ($name in $files) {
        $source = Join-Path $experimentRoot $name
        if (Test-Path -LiteralPath $source) {
            Copy-Item -LiteralPath $source -Destination $bundleRoot
        }
    }

    foreach ($name in @("requirements", "rubrics", "runs", "logs")) {
        $source = Join-Path $experimentRoot $name
        if (Test-Path -LiteralPath $source) {
            Copy-Item -LiteralPath $source -Destination $bundleRoot -Recurse
        }
    }

    $zipPath = "$bundleRoot.zip"
    Compress-Archive -Path (Join-Path $bundleRoot "*") -DestinationPath $zipPath -CompressionLevel Optimal
    Write-Host "Result directory: $bundleRoot"
    Write-Host "Result archive:   $zipPath"
    return $zipPath
}

if (-not (Test-Path -LiteralPath $cli)) {
    throw "Experiment CLI does not exist. Install the project first: $cli"
}
if (-not (Test-Path -LiteralPath $configPath)) {
    throw "Experiment config does not exist: $configPath"
}

$config = Get-Content -LiteralPath $configPath -Raw | ConvertFrom-Json
$runGeneration = $Phase -in @("all", "generate")
$runJudge = $Phase -in @("all", "judge")

try {
    if ($runGeneration) {
        if ($Reprepare -or -not (Test-Path -LiteralPath (Join-Path $experimentRoot "sample.json"))) {
            Invoke-ExperimentCli -Arguments @("prepare", "--sample-size", "20", "--seed", "20261108")
        }
        Invoke-ExperimentCli -Arguments @("fetch")
        Invoke-ExperimentCli -Arguments @("prepare-inputs")

        $forceArgs = if ($ForceGeneration) { @("--force") } else { @() }
        Invoke-ExperimentCli -Arguments (@("run", "--method", "direct_llm_native") + $forceArgs)
        Invoke-ExperimentCli -Arguments (@("run", "--method", "dsh_sap") + $forceArgs)

        Start-LegacyServer -Config $config
        Invoke-ExperimentCli -Arguments (@("run", "--method", "sap_ver1") + $forceArgs)
        Stop-LegacyServer
    }

    if ($runJudge) {
        $forceArgs = if ($ForceJudge) { @("--force") } else { @() }
        Invoke-ExperimentCli -Arguments (@("judge") + $forceArgs)
        Invoke-ExperimentCli -Arguments @("summarize")
    }
}
finally {
    Stop-LegacyServer
    $archive = Export-ExperimentResults
}

Write-Host "Experiment phase '$Phase' completed. Archive: $archive"
