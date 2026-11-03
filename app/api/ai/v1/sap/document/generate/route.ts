import { generateSap } from "@/lib/sap-generator";
import { createSapDocumentGenerateHandler } from "../generate-handler";

export const maxDuration = 7200;

export const POST = createSapDocumentGenerateHandler(
  generateSap,
  "AI SAP document generation error:"
);
