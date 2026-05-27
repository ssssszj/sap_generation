import { generateSapWithRevisions } from "@/lib/sap-generator";
import { createSapDocumentGenerateHandler } from "../generate-handler";

export const maxDuration = 300;

export const POST = createSapDocumentGenerateHandler(
  generateSapWithRevisions,
  "AI SAP document generation with revision error:"
);
