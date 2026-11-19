import { execFile } from 'node:child_process'
import path from 'node:path'
import { promisify } from 'node:util'
import { defineTool } from '@deepseek-ai/dsh-tools'

const execFileAsync = promisify(execFile)

export const name = 'sapgen-tools'
export const inject = ['tools']

function workspaceRoot() {
  const value = process.env.SAPGEN_WORKSPACE_ROOT
  if (!value) throw new Error('SAPGEN_WORKSPACE_ROOT is required')
  return path.resolve(value)
}

function safePath(value) {
  const root = workspaceRoot()
  const resolved = path.resolve(root, value)
  const relative = path.relative(root, resolved)
  if (relative.startsWith('..') || path.isAbsolute(relative)) {
    throw new Error(`path is outside SAPGEN_WORKSPACE_ROOT: ${value}`)
  }
  return resolved
}

async function bridge(args) {
  const python = process.env.SAPGEN_PYTHON
  if (!python) throw new Error('SAPGEN_PYTHON must point to the project Python executable')
  const env = { ...process.env }
  const { stdout, stderr } = await execFileAsync(python, ['-m', 'sapgen.tool_bridge', ...args], {
    cwd: workspaceRoot(), env, windowsHide: true, maxBuffer: 8 * 1024 * 1024,
  })
  if (stderr.trim()) process.stderr.write(`[sapgen] ${stderr}`)
  return stdout.trim()
}

function textOutput() {
  return {
    schema: { type: 'string' },
    render: (_args, value) => [{ type: 'text', text: value }],
  }
}

export function apply(ctx) {
  ctx.tools.register(defineTool({
    name: 'sap_validate_ir',
    description: 'Run deterministic cross-reference, estimand, missing-data, safety, provenance, and TFL checks against a SAP-IR JSON file.',
    parameters: {
      ir_path: { type: 'string', required: true, description: 'Path to SAP-IR JSON inside the configured workspace.' },
    },
    output: textOutput(),
    async execute(args) {
      return bridge(['validate', '--ir', safePath(args.ir_path)])
    },
  }))

  ctx.tools.register(defineTool({
    name: 'sap_enrich_ir',
    description: 'Apply the four SAP-specific modules to a SAP-IR file and write a reviewable enriched SAP-IR. Proposed choices remain inferred or unresolved.',
    parameters: {
      ir_path: { type: 'string', required: true },
      output_path: { type: 'string', required: true },
    },
    output: textOutput(),
    async execute(args) {
      return bridge(['enrich', '--ir', safePath(args.ir_path), '--output', safePath(args.output_path)])
    },
  }))

  ctx.tools.register(defineTool({
    name: 'sap_export_docx',
    description: 'Export a reviewed SAP-IR as an editable Word SAP draft.',
    parameters: {
      ir_path: { type: 'string', required: true },
      output_path: { type: 'string', required: true },
    },
    output: textOutput(),
    async execute(args) {
      return bridge(['export', '--ir', safePath(args.ir_path), '--output', safePath(args.output_path)])
    },
  }))

  ctx.tools.register(defineTool({
    name: 'sap_export_tfl',
    description: 'Render the TFLSpec records in SAP-IR as editable Word table shells.',
    parameters: {
      ir_path: { type: 'string', required: true },
      output_path: { type: 'string', required: true },
    },
    output: textOutput(),
    async execute(args) {
      return bridge(['export-tfl', '--ir', safePath(args.ir_path), '--output', safePath(args.output_path)])
    },
  }))
}

