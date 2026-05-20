# Clinical Web SAP Service

Next.js service for generating Statistical Analysis Plan (SAP) content from Protocol and CRF text. The project is intended to be deployed as an AI backend service and called by another website backend.

## Main Capabilities

- Generate pre-SAP Synopsis confirmation items.
- Confirm a first-level SAP outline.
- Generate the final SAP document as Markdown.
- Optional local demo page at `/` for manual testing.

The formal backend integration APIs are documented in [API_INTERFACE.md](./API_INTERFACE.md).

## Tech Stack

- Next.js 14 App Router
- TypeScript
- OpenRouter-compatible LLM client
- PDF/DOCX text parsing support for the local demo endpoints

## Requirements

- Node.js `>=18.17.0` (Node 20 is recommended; see `.nvmrc`)
- npm
- OpenRouter API key for real model calls

Install:

```bash
npm ci
```

Configure environment:

```bash
cp .env.example .env.local
```

Then edit `.env.local` and set:

```bash
OPENROUTER_API_KEY=your_key_here
```

## Development

```bash
npm run dev
```

Default local URL:

```text
http://localhost:3000
```

If port 3000 is already occupied:

```bash
npm run dev -- --port 3001
```

## Production

```bash
npm run build
npm run start
```

## Formal API Endpoints

The production integration endpoints use JSON and do not require file upload. The calling backend should parse uploaded files into text and pass `protocolText` and `crfText`.

- `POST /ai/v1/sap/core-content/generate`
- `POST /ai/v1/sap/core-content/regenerate`
- `GET /ai/v1/sap/outline/default`
- `POST /ai/v1/sap/outline/confirm`
- `POST /ai/v1/sap/document/generate`

See [API_INTERFACE.md](./API_INTERFACE.md) for request/response examples.

## Local Demo Endpoints

The `/api/*` routes are retained for local manual testing with uploaded files. They are not the preferred backend integration surface.

## Environment Variables

| Name | Required | Description |
| --- | --- | --- |
| `OPENROUTER_API_KEY` | Yes | API key used for real LLM calls |
| `OPENROUTER_MODEL` | No | Defaults to `openai/gpt-4o` |
| `OPENROUTER_PROXY_MODE` | No | Set to `on`, `true`, or `1` to enable proxy use |
| `HTTPS_PROXY` | No | Proxy URL when proxy mode is enabled |
| `HTTP_PROXY` | No | Proxy URL when proxy mode is enabled |
| `SAP_RUBRIC_MAX_CHARS` | No | Optional prompt-size cap for rubric injection; `0` or unset means full rubric |

## Repository Notes

- Do not commit `.env.local`, `.next`, `node_modules`, `input`, or `output`.
- `requirements.txt` is included only as a handoff checklist for teams expecting one; this is not a Python project.
- Sample/private study files should stay outside Git or be shared through approved internal storage.
