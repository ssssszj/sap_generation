# SAPGen DeepSeek Harness Plugin

This installable bundle exposes deterministic SAP tools to a DeepSeek Harness profile. The model can validate and enrich SAP-IR, then export the reviewed result and TFL shells.

Required environment variables:

- `SAPGEN_WORKSPACE_ROOT`: absolute path of this project or another allowed workspace.
- `SAPGEN_PYTHON`: absolute path of the Python executable where `sapgen-system` is installed.

Install into a dedicated profile after the SDK/runtime is installed:

```powershell
$node = $env:SAPGEN_DSH_NODE
$dsh = (Resolve-Path 'node_modules/@deepseek-ai/dsh/lib/bin.js').Path
$env:DSH_HOME = (Resolve-Path '.runtime/dsh-home').Path
& $node $dsh --profile sapgen --from-default-profile sdk --dump-default-config | Out-Null
& $node $dsh plugin --profile sapgen add file:./deepseek-plugin
```

Set `SAPGEN_DSH_PROFILE=sapgen` before launching the application. Restart the Harness profile after adding or updating the bundle.

