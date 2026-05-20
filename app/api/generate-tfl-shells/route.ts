import { NextRequest, NextResponse } from "next/server";
import { generateTflShells } from "@/lib/tfl-generator";
import { parseFileToText } from "@/lib/file-parser";
import type { TflStep } from "@/lib/tfl-spec";

export const maxDuration = 180;

function streamLine(controller: ReadableStreamDefaultController<Uint8Array>, obj: object) {
  const encoder = new TextEncoder();
  controller.enqueue(encoder.encode(JSON.stringify(obj) + "\n"));
}

export async function POST(request: NextRequest) {
  try {
    const formData = await request.formData();
    const protocolFile = formData.get("protocol") as File | null;
    const crfFile = formData.get("crf") as File | null;
    const sapText = formData.get("sapText") as string | null;

    if (!protocolFile || !crfFile) {
      return NextResponse.json(
        { error: "请同时上传 Protocol 和 CRF 文件" },
        { status: 400 }
      );
    }
    if (!sapText || !sapText.trim()) {
      return NextResponse.json(
        { error: "请先生成 SAP 后再生成 TFL Shells，或传入 SAP 全文（sapText）" },
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
        { error: `CRF 文件解析失败: ${crfResult.error || "文件内容为空"}` },
        { status: 400 }
      );
    }

    const protocolText = protocolResult.text;
    const crfText = crfResult.text;

    const stream = new ReadableStream<Uint8Array>({
      async start(controller) {
        try {
          const result = await generateTflShells({
            protocolText,
            crfText,
            sapText: sapText.trim(),
            onProgress(step: TflStep, status: "generating" | "done") {
              streamLine(controller, { type: "progress", step, status });
            },
          });
          streamLine(controller, {
            type: "done",
            result: {
              tableShells: result.tableShells,
              figureShells: result.figureShells,
              listingShells: result.listingShells,
              fullDocument: result.fullDocument,
            },
          });
        } catch (err) {
          console.error("TFL shells generation error:", err);
          streamLine(controller, {
            type: "error",
            error: err instanceof Error ? err.message : "生成 TFL Shells 时发生错误",
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
    console.error("TFL shells generation error:", err);
    return NextResponse.json(
      { error: err instanceof Error ? err.message : "生成 TFL Shells 时发生错误" },
      { status: 500 }
    );
  }
}
