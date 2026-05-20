import { NextRequest, NextResponse } from "next/server";
import { generateCoreContent } from "@/lib/sap-generator";
import { parseFileToText } from "@/lib/file-parser";

export const maxDuration = 120;

export async function POST(request: NextRequest) {
  try {
    const formData = await request.formData();
    const protocolFile = formData.get("protocol") as File | null;
    const crfFile = formData.get("crf") as File | null;

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

    const items = await generateCoreContent(
      protocolResult.text,
      crfResult.text
    );

    return NextResponse.json({ items });
  } catch (err) {
    console.error("Core content generation error:", err);
    return NextResponse.json(
      { error: err instanceof Error ? err.message : "生成核心内容时发生错误" },
      { status: 500 }
    );
  }
}
