import { NextResponse } from "next/server";
import { SAP_SPEC } from "@/lib/sap-spec";

export const maxDuration = 30;

export async function GET() {
  return NextResponse.json({
    code: 0,
    data: {
      outline: SAP_SPEC.map((section) => ({
        id: section.id,
        title: section.title,
        titleEn: section.titleEn,
        level: 1,
      })),
    },
  });
}
