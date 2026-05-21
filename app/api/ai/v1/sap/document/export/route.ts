import { NextRequest, NextResponse } from "next/server";
import { markdownToDocx, markdownToPdf } from "@/lib/document-exporter";

export const runtime = "nodejs";
export const maxDuration = 60;

type ExportFormat = "docx" | "pdf";

function fail(message: string, status = 400) {
  return NextResponse.json({ code: 1, message }, { status });
}

function sanitizeFilename(value: string | undefined, format: ExportFormat): string {
  const base = (value?.trim() || "sap-document")
    .replace(/\.(docx|pdf)$/i, "")
    .replace(/[\\/:*?"<>|]+/g, "-")
    .slice(0, 120);
  return `${base || "sap-document"}.${format}`;
}

function contentDisposition(filename: string): string {
  return `attachment; filename="${encodeURIComponent(filename)}"; filename*=UTF-8''${encodeURIComponent(filename)}`;
}

export async function POST(request: NextRequest) {
  try {
    const contentType = request.headers.get("content-type")?.toLowerCase() ?? "";
    if (!contentType.includes("application/json")) {
      return fail("Content-Type 必须是 application/json", 415);
    }

    const body = (await request.json()) as {
      markdown?: string;
      documentContent?: string;
      format?: ExportFormat;
      filename?: string;
    };

    const markdown = body.markdown?.trim() || body.documentContent?.trim() || "";
    if (!markdown) return fail("markdown 或 documentContent 不能为空");
    if (body.format !== "docx" && body.format !== "pdf") {
      return fail("format 必须是 docx 或 pdf");
    }

    const format: ExportFormat = body.format;
    const buffer =
      format === "docx" ? await markdownToDocx(markdown) : markdownToPdf(markdown);
    const filename = sanitizeFilename(body.filename, format);
    const responseContentType =
      format === "docx"
        ? "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        : "application/pdf";

    return new NextResponse(new Uint8Array(buffer), {
      headers: {
        "Content-Type": responseContentType,
        "Content-Length": String(buffer.byteLength),
        "Content-Disposition": contentDisposition(filename),
      },
    });
  } catch (err) {
    console.error("AI SAP document export error:", err);
    return fail(err instanceof Error ? err.message : "导出文档失败", 500);
  }
}
