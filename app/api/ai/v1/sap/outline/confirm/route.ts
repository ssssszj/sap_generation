import { NextRequest, NextResponse } from "next/server";
import { SAP_SPEC, type SapSection } from "@/lib/sap-spec";

export const maxDuration = 30;

type OutlineInput = {
  id?: string;
  title: string;
  titleEn?: string;
};

function ok(data: unknown) {
  return NextResponse.json({ code: 0, data });
}

function fail(message: string, status = 400) {
  return NextResponse.json({ code: 1, message }, { status });
}

function normalizeOutline(outline: OutlineInput[]): SapSection[] {
  return outline
    .map((item, index) => {
      const id = item.id?.trim() || `${index + 1}`;
      const title = item.title.trim();
      const builtIn = SAP_SPEC.find((section) => section.id === id && section.title === title);
      if (builtIn) return builtIn;
      return {
        id,
        title,
        titleEn: item.titleEn?.trim() || "",
        description: "用户新增一级目录，由大模型根据核心内容与上下文自主生成",
        subsections: [],
      };
    })
    .filter((section) => section.title);
}

export async function POST(request: NextRequest) {
  try {
    const body = (await request.json()) as { outline?: OutlineInput[] };
    if (!Array.isArray(body.outline) || body.outline.length === 0) {
      return fail("outline 必须是非空一级目录列表");
    }

    const confirmedOutline = normalizeOutline(body.outline);
    if (!confirmedOutline.length) {
      return fail("确认后的大纲不能为空");
    }

    return ok({ outline: confirmedOutline });
  } catch (err) {
    console.error("AI SAP outline confirmation error:", err);
    return fail(err instanceof Error ? err.message : "确认大纲失败", 500);
  }
}
