import { NextRequest, NextResponse } from "next/server";
import { generateSap, type CoreContentItem, SapCoverMeta } from "@/lib/sap-generator";
import type { SapSection } from "@/lib/sap-spec";
import { parseFileToText } from "@/lib/file-parser";

export const maxDuration = 120;

function streamLine(controller: ReadableStreamDefaultController<Uint8Array>, obj: object) {
  const encoder = new TextEncoder();
  controller.enqueue(encoder.encode(JSON.stringify(obj) + "\n"));
}

export async function POST(request: NextRequest) {
  try {
    const formData = await request.formData();
    const protocolFile = formData.get("protocol") as File | null;
    const crfFile = formData.get("crf") as File | null;
    const metaJson = formData.get("meta") as string | null;
    const coreContentJson = formData.get("coreContent") as string | null;
    const outlineJson = formData.get("outline") as string | null;

    if (!protocolFile || !crfFile) {
      return NextResponse.json(
        { error: "请同时上传 Protocol 和 CRF/aCRF 文件" },
        { status: 400 }
      );
    }

    const protocolResult = await parseFileToText(protocolFile);
    if (protocolResult.error || !protocolResult.text) {
      return NextResponse.json(
        { error: `Protocol 文件解析失败: ${protocolResult.error || "文件内容为空"}` },
        { status: 400 }
      );
    }

    const crfResult = await parseFileToText(crfFile);
    if (crfResult.error || !crfResult.text) {
      return NextResponse.json(
        { error: `CRF/aCRF 文件解析失败: ${crfResult.error || "文件内容为空"}` },
        { status: 400 }
      );
    }

    const protocolText = protocolResult.text;
    const crfText = crfResult.text;

    let meta: SapCoverMeta | undefined;
    if (metaJson) {
      try {
        meta = JSON.parse(metaJson) as SapCoverMeta;
      } catch {
        meta = undefined;
      }
    }

    let coreContent: CoreContentItem[] | undefined;
    if (coreContentJson) {
      try {
        coreContent = JSON.parse(coreContentJson) as CoreContentItem[];
      } catch {
        coreContent = undefined;
      }
    }

    let sections: SapSection[] | undefined;
    if (outlineJson) {
      try {
        const parsed = JSON.parse(outlineJson) as SapSection[];
        sections = parsed.filter((section) => section.id?.trim() && section.title?.trim());
      } catch {
        sections = undefined;
      }
    }

    const stream = new ReadableStream<Uint8Array>({
      async start(controller) {
        try {
          const result = await generateSap({
            protocolText,
            crfText,
            meta,
            coreContent,
            sections,
            onProgress(current, total, section) {
              streamLine(controller, {
                type: "progress",
                current,
                total,
                section: {
                  id: section.id,
                  title: section.title,
                  titleEn: section.titleEn,
                },
              });
            },
          });
          streamLine(controller, {
            type: "done",
            result: {
              success: true,
              coverMeta: result.coverMeta,
              fullDocument: result.fullDocument,
              sectionsCount: result.sections.length,
            },
          });
        } catch (err) {
          console.error("SAP generation error:", err);
          streamLine(controller, {
            type: "error",
            error: err instanceof Error ? err.message : "生成 SAP 时发生错误",
          });
        } finally {
          controller.close();
        }
      },
    });

    return new Response(stream, {
      headers: { "Content-Type": "application/x-ndjson" },
    });
  } catch (err) {
    console.error("SAP generation error:", err);
    return NextResponse.json(
      { error: err instanceof Error ? err.message : "生成 SAP 时发生错误" },
      { status: 500 }
    );
  }
}
