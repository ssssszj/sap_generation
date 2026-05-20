import mammoth from "mammoth";

/**
 * 文件解析结果
 */
export interface ParseResult {
  text: string;
  error?: string;
}

/**
 * 根据文件类型解析文件内容为文本
 * 支持：.txt, .md, .pdf, .docx
 */
export async function parseFileToText(file: File): Promise<ParseResult> {
  const fileName = file.name.toLowerCase();
  const extension = fileName.split(".").pop()?.toLowerCase();

  try {
    if (extension === "pdf") {
      return await parsePdf(file);
    } else if (extension === "docx") {
      return await parseDocx(file);
    } else if (extension === "txt" || extension === "md") {
      return await parseText(file);
    } else {
      return {
        text: "",
        error: `不支持的文件格式: .${extension}。支持格式: .pdf, .docx, .txt, .md`,
      };
    }
  } catch (err) {
    return {
      text: "",
      error: `解析文件失败: ${err instanceof Error ? err.message : String(err)}`,
    };
  }
}

/**
 * 解析 PDF 文件
 */
async function parsePdf(file: File): Promise<ParseResult> {
  try {
    // 在 Node.js 环境中使用 require 导入 CommonJS 模块
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    const pdfParse = require("pdf-parse");
    const arrayBuffer = await file.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);
    const data = await pdfParse(buffer);
    return { text: data.text };
  } catch (err) {
    return {
      text: "",
      error: `PDF 解析失败: ${err instanceof Error ? err.message : String(err)}`,
    };
  }
}

/**
 * 解析 Word (.docx) 文件
 */
async function parseDocx(file: File): Promise<ParseResult> {
  try {
    const arrayBuffer = await file.arrayBuffer();
    // mammoth 在 Node.js 环境下使用 Buffer 作为输入
    const buffer = Buffer.from(arrayBuffer);
    const result = await mammoth.extractRawText({ buffer });
    return { text: result.value };
  } catch (err) {
    return {
      text: "",
      error: `Word 文档解析失败: ${err instanceof Error ? err.message : String(err)}`,
    };
  }
}

/**
 * 解析文本文件 (.txt, .md)
 */
async function parseText(file: File): Promise<ParseResult> {
  try {
    const text = await file.text();
    return { text };
  } catch (err) {
    return {
      text: "",
      error: `文本文件读取失败: ${err instanceof Error ? err.message : String(err)}`,
    };
  }
}
