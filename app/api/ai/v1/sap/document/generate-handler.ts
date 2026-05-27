import { NextRequest, NextResponse } from "next/server";
import type {
  CoreContentItem,
  SapCoverMeta,
  SapGenerateInput,
  SapGenerateResult,
} from "@/lib/sap-generator";
import { normalizeSapOutline, type SapOutlineInput } from "@/lib/sap-guides";

type SapDocumentGenerator = (input: SapGenerateInput) => Promise<SapGenerateResult>;

function ok(data: unknown) {
  return NextResponse.json({ code: 0, data });
}

function fail(message: string, status = 400) {
  return NextResponse.json({ code: 1, message }, { status });
}

export function createSapDocumentGenerateHandler(
  generateDocument: SapDocumentGenerator,
  errorLabel: string
) {
  return async function POST(request: NextRequest) {
    try {
      const body = (await request.json()) as {
        protocolText?: string;
        crfText?: string;
        coreContents?: CoreContentItem[];
        outline?: SapOutlineInput[];
        meta?: SapCoverMeta;
      };

      if (!body.protocolText?.trim() || !body.crfText?.trim()) {
        return fail("protocolText 和 crfText 不能为空");
      }
      if (!Array.isArray(body.coreContents) || body.coreContents.length === 0) {
        return fail("coreContents 必须是已确认的核心内容列表");
      }
      if (body.coreContents.some((item) => item.confirmed === false)) {
        return fail("coreContents 中存在未确认项");
      }
      if (!Array.isArray(body.outline) || body.outline.length === 0) {
        return fail("outline 必须是已确认的大纲列表");
      }

      const outline = normalizeSapOutline(body.outline);
      if (!outline.length) {
        return fail("outline 规范化后不能为空");
      }

      const result = await generateDocument({
        protocolText: body.protocolText,
        crfText: body.crfText,
        meta: body.meta,
        coreContent: body.coreContents,
        sections: outline,
      });

      return ok({
        documentContent: result.fullDocument,
        contentType: "text/markdown",
        coverMeta: result.coverMeta,
        sections: result.sections.map(({ section, content }) => ({
          id: section.id,
          title: section.title,
          titleEn: section.titleEn,
          content,
        })),
      });
    } catch (err) {
      console.error(errorLabel, err);
      return fail(err instanceof Error ? err.message : "生成 SAP Markdown 文档失败", 500);
    }
  };
}
