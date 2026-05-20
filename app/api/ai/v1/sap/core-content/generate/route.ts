import { NextRequest, NextResponse } from "next/server";
import { generateCoreContent } from "@/lib/sap-generator";

export const maxDuration = 120;

function ok(data: unknown) {
  return NextResponse.json({ code: 0, data });
}

function fail(message: string, status = 400) {
  return NextResponse.json({ code: 1, message }, { status });
}

export async function POST(request: NextRequest) {
  try {
    const body = (await request.json()) as {
      protocolText?: string;
      crfText?: string;
    };

    if (!body.protocolText?.trim() || !body.crfText?.trim()) {
      return fail("protocolText 和 crfText 不能为空");
    }

    const items = await generateCoreContent(
      body.protocolText,
      body.crfText
    );

    return ok({ coreContents: items });
  } catch (err) {
    console.error("AI SAP core content generation error:", err);
    return fail(err instanceof Error ? err.message : "生成核心内容失败", 500);
  }
}
