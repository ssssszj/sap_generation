import { NextRequest, NextResponse } from "next/server";
import {
  reviseCoreContentItem,
  type CoreContentItem,
} from "@/lib/sap-generator";

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
      item?: CoreContentItem;
      feedback?: string;
      allCoreContents?: CoreContentItem[];
    };

    if (!body.protocolText?.trim() || !body.crfText?.trim()) {
      return fail("protocolText 和 crfText 不能为空");
    }
    if (!body.item?.id || !body.item.title || !body.item.content) {
      return fail("item 必须包含 id、title、content");
    }
    if (!body.feedback?.trim()) {
      return fail("feedback 不能为空");
    }

    const item = await reviseCoreContentItem({
      protocolText: body.protocolText,
      crfText: body.crfText,
      item: body.item,
      feedback: body.feedback,
      allCoreContent: body.allCoreContents,
    });

    return ok({ coreContent: item });
  } catch (err) {
    console.error("AI SAP core content regeneration error:", err);
    return fail(err instanceof Error ? err.message : "重新生成核心内容失败", 500);
  }
}
