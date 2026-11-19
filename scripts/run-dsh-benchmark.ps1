<#
.SYNOPSIS
Runs the 20-study DSH SAP benchmark as a new batch or resumes the current batch.

.PARAMETER RunMode
New creates a new batch timestamp so all selected studies run again. Resume reuses the existing
batch and skips generation/evaluation already completed in that batch.

.EXAMPLE
.\scripts\run-dsh-benchmark.ps1 -Phase all -RunMode New

.EXAMPLE
.\scripts\run-dsh-benchmark.ps1 -Phase generate -RunMode New
.\scripts\run-dsh-benchmark.ps1 -Phase judge -RunMode Resume
#>
[CmdletBinding()]
param(
    [ValidateSet("all", "generate", "judge", "summarize")]
    [string]$Phase = "all",
    [ValidateSet("New", "Resume")]
    [string]$RunMode = "Resume",
    # Backward-compatible alias for -RunMode New.
    [switch]$NewRun,
    [switch]$ForceJudge,
    [ValidateRange(1, 20)]
    [int]$StartAt = 1,
    [ValidateRange(0, 20)]
    [int]$Limit = 0
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

if (
    $NewRun -and
    $PSBoundParameters.ContainsKey("RunMode") -and
    $RunMode -ne "New"
) {
    throw "-NewRun conflicts with -RunMode Resume. Use -RunMode New or omit -NewRun."
}
$effectiveRunMode = if ($NewRun) { "New" } else { $RunMode }

$projectRoot = Split-Path -Parent $PSScriptRoot
$experimentRoot = Join-Path $projectRoot "benchmark\experiment"
$python = Join-Path $projectRoot ".venv\Scripts\python.exe"
$samplePath = Join-Path $experimentRoot "sample.json"
$statePath = Join-Path $experimentRoot "dsh-only-state.json"
$batchesRoot = Join-Path $experimentRoot "batches"

if (-not (Test-Path -LiteralPath $python)) {
    throw "Python environment does not exist: $python"
}
if (-not (Test-Path -LiteralPath $samplePath)) {
    throw "Benchmark sample does not exist: $samplePath"
}

function Read-JsonFile {
    param([Parameter(Mandatory)][string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        return $null
    }
    try {
        return Get-Content -LiteralPath $Path -Raw -Encoding UTF8 | ConvertFrom-Json
    }
    catch {
        Write-Warning "Ignoring unreadable JSON file: $Path; $($_.Exception.Message)"
        return $null
    }
}

function Write-JsonFile {
    param(
        [Parameter(Mandatory)]$Value,
        [Parameter(Mandatory)][string]$Path
    )

    $Value | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $Path -Encoding UTF8
}

function Write-MethodScoreComparison {
    param(
        [Parameter(Mandatory)][string]$SummaryPath,
        [Parameter(Mandatory)][string]$BatchReportPath
    )

    $summary = Read-JsonFile -Path $SummaryPath
    if ($null -eq $summary) {
        Write-Warning "Cannot print method scores; summary is unavailable: $SummaryPath"
        return
    }

    $batchReport = Read-JsonFile -Path $BatchReportPath
    if ($null -eq $batchReport) {
        Write-Warning "Cannot print current-batch scores; report is unavailable: $BatchReportPath"
        return
    }

    $nativeMatches = @($summary.methods | Where-Object method -eq "direct_llm_native")
    if ($nativeMatches.Count -eq 0) {
        Write-Warning "Cannot compare methods; direct_llm_native is absent from summary.json"
        return
    }

    $native = $nativeMatches[0]
    $freshDshRows = @(
        $batchReport.rows |
            Where-Object { $_.evaluation_status -eq "complete" -and $null -ne $_.weighted_score }
    )
    if ($freshDshRows.Count -eq 0) {
        Write-Warning "The current DSH batch has no successful evaluations to compare."
        return
    }
    $freshDshMean = (
        ($freshDshRows | Measure-Object -Property weighted_score -Average).Average
    )

    Write-Host ""
    Write-Host "Native LLM vs current-batch DSH SAP scores"
    Write-Host ("direct_llm_native (all available): {0:N2} (n={1})" -f `
        [double]$native.mean_weighted_score, [int]$native.completed_studies)
    Write-Host ("dsh_sap (batch $($batchReport.run_id)): {0:N2} (n={1})" -f `
        [double]$freshDshMean, $freshDshRows.Count)

    $nativeByStudy = @{}
    foreach ($row in @($summary.study_method_scores | Where-Object method -eq "direct_llm_native")) {
        $nativeByStudy[[string]$row.study_id] = [double]$row.weighted_score
    }

    $pairedNativeTotal = 0.0
    $pairedDshTotal = 0.0
    $pairedCount = 0
    foreach ($row in $freshDshRows) {
        $studyId = [string]$row.study_id
        if ($nativeByStudy.ContainsKey($studyId)) {
            $pairedNativeTotal += [double]$nativeByStudy[$studyId]
            $pairedDshTotal += [double]$row.weighted_score
            $pairedCount += 1
        }
    }

    if ($pairedCount -gt 0) {
        $pairedNativeMean = $pairedNativeTotal / $pairedCount
        $pairedDshMean = $pairedDshTotal / $pairedCount
        $pairedDelta = $pairedDshMean - $pairedNativeMean
        Write-Host ("Paired comparison (n={0}): native={1:N2}, dsh={2:N2}, delta={3:+0.00;-0.00;0.00} points" -f `
            $pairedCount, $pairedNativeMean, $pairedDshMean, $pairedDelta)
    }

    if ([int]$native.completed_studies -ne $freshDshRows.Count) {
        Write-Warning "Method coverage differs; the DSH score above uses only successful evaluations from this batch. Use the paired comparison for a fair comparison."
    }
}

function Invoke-ExperimentCli {
    param([Parameter(Mandatory)][string[]]$CliArguments)

    & $script:python -m sapgen.experiment.cli --root $script:projectRoot @CliArguments
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "sapgen.experiment.cli failed (exit $LASTEXITCODE): $($CliArguments -join ' ')"
        return $false
    }
    return $true
}

function Test-FreshGeneration {
    param(
        $Run,
        [double]$BatchStartedAt
    )

    if ($null -eq $Run) {
        return $false
    }
    if ($Run.status -ne "complete") {
        return $false
    }
    if ($null -eq $Run.started_at_epoch) {
        return $false
    }
    return [double]$Run.started_at_epoch -ge $BatchStartedAt
}

function Test-RunBelongsToBatch {
    param(
        $Run,
        [double]$BatchStartedAt
    )

    if ($null -eq $Run -or $null -eq $Run.started_at_epoch) {
        return $false
    }
    return [double]$Run.started_at_epoch -ge $BatchStartedAt
}

function Get-BatchRoot {
    param($BatchState)

    if ($null -eq $BatchState -or [string]::IsNullOrWhiteSpace([string]$BatchState.run_id)) {
        throw "Batch state does not contain run_id."
    }
    return Join-Path $script:batchesRoot ([string]$BatchState.run_id)
}

function Copy-FileToBatch {
    param(
        [Parameter(Mandatory)][string]$Source,
        [Parameter(Mandatory)][string]$Destination
    )

    if (-not (Test-Path -LiteralPath $Source)) {
        return $false
    }
    $destinationParent = Split-Path -Parent $Destination
    New-Item -ItemType Directory -Force -Path $destinationParent | Out-Null
    Copy-Item -LiteralPath $Source -Destination $Destination -Force
    return $true
}

function Initialize-BatchStorage {
    param($BatchState)

    $batchRoot = Get-BatchRoot -BatchState $BatchState
    $batchStatePath = Join-Path $batchRoot "batch.json"
    $newBatchStorage = -not (Test-Path -LiteralPath $batchStatePath)
    if ($newBatchStorage) {
        New-Item -ItemType Directory -Force -Path $batchRoot | Out-Null
        Write-JsonFile -Value $BatchState -Path $batchStatePath
    }

    # One-time migration for batches created before isolated storage was introduced.
    $batchSample = Read-JsonFile -Path $script:samplePath
    if ($newBatchStorage) {
        foreach ($question in @($batchSample.questions)) {
            $studyId = [string]$question.study_id
            $workingRoot = Join-Path $script:experimentRoot "runs\$studyId\dsh_sap"
            $workingRunPath = Join-Path $workingRoot "run.json"
            $workingRun = Read-JsonFile -Path $workingRunPath
            if (-not (Test-RunBelongsToBatch `
                -Run $workingRun `
                -BatchStartedAt ([double]$BatchState.started_at_epoch))) {
                continue
            }

            $batchMethodRoot = Join-Path $batchRoot "runs\$studyId\dsh_sap"
            $null = Copy-FileToBatch `
                -Source $workingRunPath `
                -Destination (Join-Path $batchMethodRoot "run.json")

            $workingCandidate = Join-Path $workingRoot "candidate.md"
            $batchCandidate = Join-Path $batchMethodRoot "candidate.md"
            if ($workingRun.status -eq "complete") {
                $null = Copy-FileToBatch -Source $workingCandidate -Destination $batchCandidate
            }

            $workingEvaluation = Join-Path $workingRoot "evaluation.json"
            if (
                $workingRun.status -eq "complete" -and
                (Test-Path -LiteralPath $workingCandidate) -and
                (Test-Path -LiteralPath $workingEvaluation) -and
                (Get-Item -LiteralPath $workingEvaluation).LastWriteTimeUtc -ge
                    (Get-Item -LiteralPath $workingCandidate).LastWriteTimeUtc
            ) {
                $null = Copy-FileToBatch `
                    -Source $workingEvaluation `
                    -Destination (Join-Path $batchMethodRoot "evaluation.json")
            }
        }

        $legacyReport = Join-Path $script:experimentRoot "$($BatchState.run_id)-report.json"
        $legacyScores = Join-Path $script:experimentRoot "$($BatchState.run_id)-scores.csv"
        $null = Copy-FileToBatch -Source $legacyReport -Destination (Join-Path $batchRoot "report.json")
        $null = Copy-FileToBatch -Source $legacyScores -Destination (Join-Path $batchRoot "scores.csv")
    }

    # Snapshot the exact model-visible inputs so every batch remains reproducible.
    foreach ($question in @($batchSample.questions)) {
        $studyId = [string]$question.study_id
        $workingInputRoot = Join-Path $script:experimentRoot "runs\$studyId\input"
        $batchInputRoot = Join-Path $batchRoot "runs\$studyId\input"
        foreach ($fileName in @("protocol_input.txt", "crf_not_provided.txt", "manifest.json")) {
            $batchInputPath = Join-Path $batchInputRoot $fileName
            if (-not (Test-Path -LiteralPath $batchInputPath)) {
                $null = Copy-FileToBatch `
                    -Source (Join-Path $workingInputRoot $fileName) `
                    -Destination $batchInputPath
            }
        }
    }
    return $batchRoot
}

function Save-GenerationToBatch {
    param(
        [Parameter(Mandatory)][string]$StudyId,
        $BatchState
    )

    $workingRoot = Join-Path $script:experimentRoot "runs\$StudyId\dsh_sap"
    $workingRunPath = Join-Path $workingRoot "run.json"
    $run = Read-JsonFile -Path $workingRunPath
    if (-not (Test-RunBelongsToBatch `
        -Run $run `
        -BatchStartedAt ([double]$BatchState.started_at_epoch))) {
        return $null
    }

    $batchMethodRoot = Join-Path (Get-BatchRoot -BatchState $BatchState) "runs\$StudyId\dsh_sap"
    $null = Copy-FileToBatch `
        -Source $workingRunPath `
        -Destination (Join-Path $batchMethodRoot "run.json")
    if ($run.status -eq "complete") {
        $null = Copy-FileToBatch `
            -Source (Join-Path $workingRoot "candidate.md") `
            -Destination (Join-Path $batchMethodRoot "candidate.md")
    }
    return $run
}

function Restore-GenerationFromBatch {
    param(
        [Parameter(Mandatory)][string]$StudyId,
        $BatchState
    )

    $batchMethodRoot = Join-Path (Get-BatchRoot -BatchState $BatchState) "runs\$StudyId\dsh_sap"
    $workingRoot = Join-Path $script:experimentRoot "runs\$StudyId\dsh_sap"
    $null = Copy-FileToBatch `
        -Source (Join-Path $batchMethodRoot "run.json") `
        -Destination (Join-Path $workingRoot "run.json")
    $null = Copy-FileToBatch `
        -Source (Join-Path $batchMethodRoot "candidate.md") `
        -Destination (Join-Path $workingRoot "candidate.md")
}

function Save-EvaluationToBatch {
    param(
        [Parameter(Mandatory)][string]$StudyId,
        $BatchState
    )

    $batchMethodRoot = Join-Path (Get-BatchRoot -BatchState $BatchState) "runs\$StudyId\dsh_sap"
    $workingEvaluation = Join-Path $script:experimentRoot "runs\$StudyId\dsh_sap\evaluation.json"
    $null = Copy-FileToBatch `
        -Source $workingEvaluation `
        -Destination (Join-Path $batchMethodRoot "evaluation.json")
    return Read-JsonFile -Path (Join-Path $batchMethodRoot "evaluation.json")
}

function Reset-DshWorkingResults {
    $batchSample = Read-JsonFile -Path $script:samplePath
    foreach ($question in @($batchSample.questions)) {
        $studyId = [string]$question.study_id
        $workingRoot = Join-Path $script:experimentRoot "runs\$studyId\dsh_sap"
        foreach ($fileName in @("candidate.md", "run.json", "evaluation.json")) {
            $path = Join-Path $workingRoot $fileName
            if (Test-Path -LiteralPath $path) {
                Remove-Item -LiteralPath $path -Force
            }
        }
    }
}

$needsState = $Phase -in @("all", "generate", "judge")
if ($needsState) {
    if ($effectiveRunMode -eq "New" -or -not (Test-Path -LiteralPath $statePath)) {
        $previousState = Read-JsonFile -Path $statePath
        if ($null -ne $previousState) {
            $previousBatchRoot = Initialize-BatchStorage -BatchState $previousState
            Write-Host "Preserved previous batch: $previousBatchRoot"
        }
        if (-not (Invoke-ExperimentCli -CliArguments @("prepare-inputs"))) {
            throw "Failed to refresh domain-balanced benchmark inputs for the new batch."
        }
        Reset-DshWorkingResults
        $now = [DateTimeOffset]::UtcNow
        $state = [ordered]@{
            run_id = "dsh-only-$($now.ToString('yyyyMMdd-HHmmss'))"
            started_at_epoch = $now.ToUnixTimeMilliseconds() / 1000.0
            created_at = $now.ToString("o")
            method = "dsh_sap"
        }
        Write-JsonFile -Value $state -Path $statePath
        $batchRoot = Initialize-BatchStorage -BatchState $state
        Write-Host "Run mode: New"
        Write-Host "Started new DSH-only batch: $($state.run_id)"
        Write-Host "Batch directory: $batchRoot"
    }
    else {
        $state = Read-JsonFile -Path $statePath
        $batchRoot = Initialize-BatchStorage -BatchState $state
        Write-Host "Run mode: Resume"
        Write-Host "Resuming DSH-only batch: $($state.run_id)"
        Write-Host "Batch directory: $batchRoot"
    }
}
else {
    $state = Read-JsonFile -Path $statePath
    $batchRoot = if ($null -ne $state) {
        Initialize-BatchStorage -BatchState $state
    }
    else {
        $null
    }
}

$sample = Read-JsonFile -Path $samplePath
$questions = @($sample.questions)
$offset = $StartAt - 1
if ($offset -ge $questions.Count) {
    throw "StartAt $StartAt exceeds sample size $($questions.Count)."
}
$questions = @($questions | Select-Object -Skip $offset)
if ($Limit -gt 0) {
    $questions = @($questions | Select-Object -First $Limit)
}

$runGeneration = $Phase -in @("all", "generate")
$runJudge = $Phase -in @("all", "judge")

if ($runGeneration) {
    $index = 0
    foreach ($question in $questions) {
        $index += 1
        $studyId = [string]$question.study_id
        $methodRoot = Join-Path $batchRoot "runs\$studyId\dsh_sap"
        $runPath = Join-Path $methodRoot "run.json"
        $run = Read-JsonFile -Path $runPath
        if (Test-FreshGeneration -Run $run -BatchStartedAt ([double]$state.started_at_epoch)) {
            Write-Host "[$index/$($questions.Count)] SKIP generated: $studyId"
            continue
        }

        Write-Host "[$index/$($questions.Count)] GENERATE: $studyId"
        $null = Invoke-ExperimentCli -CliArguments @(
            "run", "--method", "dsh_sap", "--study-id", $studyId, "--force"
        )
        $run = Save-GenerationToBatch -StudyId $studyId -BatchState $state
        if ($null -eq $run) {
            Write-Warning "No current-batch run.json was written for $studyId"
        }
        elseif ($run.status -eq "complete") {
            Write-Host "[$index/$($questions.Count)] COMPLETE: $studyId; calls=$($run.calls); elapsed_ms=$($run.elapsed_ms)"
        }
        else {
            Write-Warning "[$index/$($questions.Count)] FAILED: $studyId; $($run.error)"
        }
    }
}

if ($runJudge) {
    $index = 0
    foreach ($question in $questions) {
        $index += 1
        $studyId = [string]$question.study_id
        $methodRoot = Join-Path $batchRoot "runs\$studyId\dsh_sap"
        $runPath = Join-Path $methodRoot "run.json"
        $candidatePath = Join-Path $methodRoot "candidate.md"
        $evaluationPath = Join-Path $methodRoot "evaluation.json"
        $run = Read-JsonFile -Path $runPath

        if (-not (Test-FreshGeneration -Run $run -BatchStartedAt ([double]$state.started_at_epoch))) {
            Write-Warning "[$index/$($questions.Count)] SKIP judge; no successful candidate from this batch: $studyId"
            continue
        }
        if (-not (Test-Path -LiteralPath $candidatePath)) {
            Write-Warning "[$index/$($questions.Count)] SKIP judge; candidate missing: $studyId"
            continue
        }

        $evaluation = Read-JsonFile -Path $evaluationPath
        $evaluationIsFresh = $false
        if ($null -ne $evaluation -and $evaluation.status -eq "complete") {
            $evaluationTime = (Get-Item -LiteralPath $evaluationPath).LastWriteTimeUtc
            $candidateTime = (Get-Item -LiteralPath $candidatePath).LastWriteTimeUtc
            $evaluationIsFresh = $evaluationTime -ge $candidateTime
        }
        if ($evaluationIsFresh -and -not $ForceJudge) {
            Write-Host "[$index/$($questions.Count)] SKIP evaluated: $studyId"
            continue
        }

        Write-Host "[$index/$($questions.Count)] JUDGE: $studyId"
        Restore-GenerationFromBatch -StudyId $studyId -BatchState $state
        $null = Invoke-ExperimentCli -CliArguments @(
            "judge", "--method", "dsh_sap", "--study-id", $studyId, "--force"
        )
        $evaluation = Save-EvaluationToBatch -StudyId $studyId -BatchState $state
        if ($null -ne $evaluation -and $evaluation.status -eq "complete") {
            Write-Host "[$index/$($questions.Count)] SCORED: $studyId; score=$($evaluation.summary.weighted_score)"
        }
        else {
            $errorText = if ($null -ne $evaluation) { $evaluation.error } else { "evaluation.json missing" }
            Write-Warning "[$index/$($questions.Count)] JUDGE FAILED: $studyId; $errorText"
        }
    }
}

if ($Phase -in @("all", "judge", "summarize")) {
    $null = Invoke-ExperimentCli -CliArguments @("summarize")
}

$rows = @()
foreach ($question in $questions) {
    $studyId = [string]$question.study_id
    $methodRoot = Join-Path $batchRoot "runs\$studyId\dsh_sap"
    $run = Read-JsonFile -Path (Join-Path $methodRoot "run.json")
    $evaluation = Read-JsonFile -Path (Join-Path $methodRoot "evaluation.json")
    $fresh = $false
    if ($null -ne $state) {
        $fresh = Test-FreshGeneration -Run $run -BatchStartedAt ([double]$state.started_at_epoch)
    }
    $rows += [ordered]@{
        study_id = $studyId
        generation_status = if ($fresh) { "complete" } elseif ($null -ne $run) { $run.status } else { "missing" }
        generation_error = if ($null -ne $run -and $run.status -eq "failed") { $run.error } else { $null }
        calls = if ($fresh) { $run.calls } else { $null }
        elapsed_ms = if ($fresh) { $run.elapsed_ms } else { $null }
        evaluation_status = if ($fresh -and $null -ne $evaluation) { $evaluation.status } else { "missing" }
        weighted_score = if ($fresh -and $null -ne $evaluation -and $evaluation.status -eq "complete") { $evaluation.summary.weighted_score } else { $null }
        critical_pass = if ($fresh -and $null -ne $evaluation -and $evaluation.status -eq "complete") { $evaluation.summary.critical_pass } else { $null }
    }
}

$completeGeneration = @($rows | Where-Object generation_status -eq "complete").Count
$failedGeneration = @($rows | Where-Object generation_status -eq "failed").Count
$completeEvaluation = @($rows | Where-Object evaluation_status -eq "complete").Count
$failedEvaluation = @($rows | Where-Object evaluation_status -eq "failed").Count
$report = [ordered]@{
    run_id = if ($null -ne $state) { $state.run_id } else { "summary-only" }
    method = "dsh_sap"
    studies_selected = $rows.Count
    generation_complete = $completeGeneration
    generation_failed = $failedGeneration
    evaluation_complete = $completeEvaluation
    evaluation_failed = $failedEvaluation
    rows = $rows
}
$reportName = "$($report.run_id)-report.json"
$reportPath = Join-Path $batchRoot "report.json"
Write-JsonFile -Value $report -Path $reportPath
$scoreCsvPath = Join-Path $batchRoot "scores.csv"
$rows |
    Select-Object study_id, generation_status, evaluation_status, weighted_score, critical_pass, calls, elapsed_ms |
    Export-Csv -LiteralPath $scoreCsvPath -NoTypeInformation -Encoding UTF8

# Keep the historical top-level filenames for existing downstream consumers.
Copy-Item -LiteralPath $reportPath -Destination (Join-Path $experimentRoot $reportName) -Force
Copy-Item `
    -LiteralPath $scoreCsvPath `
    -Destination (Join-Path $experimentRoot "$($report.run_id)-scores.csv") `
    -Force

Write-Host ""
Write-Host "DSH-only batch summary"
Write-Host "Generation: $completeGeneration complete, $failedGeneration failed"
Write-Host "Evaluation: $completeEvaluation complete, $failedEvaluation failed"
Write-Host "Batch directory: $batchRoot"
Write-Host "Report: $reportPath"
Write-Host "DSH-only scores: $scoreCsvPath"
Write-Host "Scores: $(Join-Path $experimentRoot 'scores.csv')"
Write-Host "Summary: $(Join-Path $experimentRoot 'summary.json')"
Write-MethodScoreComparison `
    -SummaryPath (Join-Path $experimentRoot "summary.json") `
    -BatchReportPath $reportPath

