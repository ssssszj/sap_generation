import fs from "fs";
import path from "path";
import type { SapSection } from "./sap-spec";

export type SapOutlineInput = {
  id?: string;
  title?: string;
  titleEn?: string;
  level?: number;
  description?: string;
  subsections?: Array<string | SapOutlineInput>;
  children?: SapOutlineInput[];
};

export type SapGuideSubsection = {
  id: string;
  title: string;
  guide: string;
};

export type SapGuideSection = {
  id: string;
  title: string;
  guide: string;
  subsections: SapGuideSubsection[];
};

let GUIDE_CACHE: SapGuideSection[] | null = null;

function readSapGuides(): string {
  const filePath = path.join(process.cwd(), "knowledge_bank", "sap_guides.md");
  return fs.readFileSync(filePath, "utf8");
}

function stripHeadingNumber(value: string): { id?: string; title: string } {
  const text = value.trim();
  const matched = text.match(/^(\d+(?:\.\d+)*)\s+(.+)$/);
  if (!matched) return { title: text };
  return { id: matched[1], title: matched[2].trim() };
}

function normalizeTitle(value: string | undefined): string {
  if (!value) return "";
  return stripHeadingNumber(value)
    .title.replace(/[（(].*?[）)]/g, "")
    .replace(/\s*\/\s*.*$/g, "")
    .replace(/[：:，,。.;；\s]/g, "")
    .toLowerCase();
}

function parseSapGuides(text: string): SapGuideSection[] {
  const lines = text.split(/\r?\n/);
  const sections: SapGuideSection[] = [];
  let current: SapGuideSection | null = null;
  let currentBuffer: string[] = [];
  let currentSub: SapGuideSubsection | null = null;
  let currentSubBuffer: string[] = [];

  const flushSubsection = () => {
    if (!currentSub) return;
    currentSub.guide = currentSubBuffer.join("\n").trim();
    current?.subsections.push(currentSub);
    currentSub = null;
    currentSubBuffer = [];
  };

  const flushSection = () => {
    flushSubsection();
    if (!current) return;
    current.guide = currentBuffer.join("\n").trim();
    sections.push(current);
    current = null;
    currentBuffer = [];
  };

  for (const line of lines) {
    const top = line.match(/^(\d+)\s+(.+)$/);
    const sub = line.match(/^(\d+\.\d+)\s+(.+)$/);

    if (top && !sub) {
      flushSection();
      current = { id: top[1], title: top[2].trim(), guide: "", subsections: [] };
      currentBuffer = [line];
      continue;
    }

    if (sub && current) {
      flushSubsection();
      currentSub = { id: sub[1], title: sub[2].trim(), guide: "" };
      currentSubBuffer = [line];
      currentBuffer.push(line);
      continue;
    }

    if (current) currentBuffer.push(line);
    if (currentSub) currentSubBuffer.push(line);
  }

  flushSection();
  return sections;
}

export function loadSapGuideSections(): SapGuideSection[] {
  if (GUIDE_CACHE) return GUIDE_CACHE;
  try {
    GUIDE_CACHE = parseSapGuides(readSapGuides());
  } catch {
    GUIDE_CACHE = [];
  }
  return GUIDE_CACHE;
}

export function getSapGuideOutline(): SapSection[] {
  return loadSapGuideSections().map((section) => ({
    id: section.id,
    title: section.title,
    titleEn: "",
    description: `来自 knowledge_bank/sap_guides.md 的固定章节：${section.title}`,
    subsections: section.subsections.map((sub) => `${sub.id} ${sub.title}`),
  }));
}

export function getSapGuideOutlineTree() {
  return loadSapGuideSections().map((section) => ({
    id: section.id,
    title: section.title,
    titleEn: "",
    level: 1,
    children: section.subsections.map((sub) => ({
      id: sub.id,
      title: sub.title,
      level: 2,
    })),
  }));
}

function findGuideByTitle(title: string | undefined): SapGuideSection | undefined {
  const normalized = normalizeTitle(title);
  if (!normalized) return undefined;
  return loadSapGuideSections().find((section) => normalizeTitle(section.title) === normalized);
}

function findSubGuideByTitle(title: string | undefined): SapGuideSubsection | undefined {
  const normalized = normalizeTitle(title);
  if (!normalized) return undefined;
  for (const section of loadSapGuideSections()) {
    const matched = section.subsections.find((sub) => normalizeTitle(sub.title) === normalized);
    if (matched) return matched;
  }
  return undefined;
}

function normalizeSubsectionInput(value: string | SapOutlineInput): string | null {
  if (typeof value === "string") {
    const text = value.trim();
    if (!text) return null;
    const parsed = stripHeadingNumber(text);
    return parsed.id ? `${parsed.id} ${parsed.title}` : parsed.title;
  }
  const title = value.title?.trim();
  if (!title) return null;
  const parsed = stripHeadingNumber(title);
  const id = value.id?.trim() || parsed.id;
  const cleanTitle = parsed.title;
  return id ? `${id} ${cleanTitle}` : cleanTitle;
}

function buildTreeFromPossiblyFlatOutline(outline: SapOutlineInput[]): SapOutlineInput[] {
  if (!outline.some((item) => item.level === 2)) return outline;

  const roots: SapOutlineInput[] = [];
  let currentRoot: SapOutlineInput | null = null;

  for (const item of outline) {
    if (item.level === 2) {
      if (!currentRoot) continue;
      currentRoot.children = [...(currentRoot.children ?? []), item];
      continue;
    }

    currentRoot = { ...item, children: [...(item.children ?? [])] };
    roots.push(currentRoot);
  }

  return roots;
}

export function normalizeSapOutline(outline: SapOutlineInput[]): SapSection[] {
  const roots = buildTreeFromPossiblyFlatOutline(outline);

  return roots
    .map((item, index) => {
      const parsedTitle = stripHeadingNumber(item.title ?? "");
      const matchedGuide = findGuideByTitle(parsedTitle.title || item.title);
      const id = item.id?.trim() || parsedTitle.id || matchedGuide?.id || `${index + 1}`;
      const title = (parsedTitle.title || item.title || "").trim();
      const childInputs = [
        ...(item.children ?? []),
        ...((item.subsections ?? []).map((sub) =>
          typeof sub === "string" ? sub : { ...sub, level: 2 }
        ) as Array<string | SapOutlineInput>),
      ];
      const subsections = childInputs
        .map(normalizeSubsectionInput)
        .filter((sub): sub is string => Boolean(sub));

      return {
        id,
        title,
        titleEn: item.titleEn?.trim() || "",
        description:
          item.description?.trim() ||
          (matchedGuide
            ? `来自 knowledge_bank/sap_guides.md 的章节指导：${matchedGuide.title}`
            : "后端编辑大纲中的新增章节，未在 sap_guides.md 中匹配到同名指导，由模型根据上下文自主生成"),
        subsections: subsections.length
          ? subsections
          : matchedGuide?.subsections.map((sub) => `${sub.id} ${sub.title}`) ?? [],
      };
    })
    .filter((section) => section.title);
}

export function findSapGuidesForSubsections(subsections: string[]): {
  guide: string;
  unmatchedSubsections: string[];
} {
  const matchedGuides: string[] = [];
  const unmatchedSubsections: string[] = [];

  for (const subsection of subsections) {
    const matchedGuide = findSubGuideByTitle(subsection);
    if (!matchedGuide?.guide) {
      unmatchedSubsections.push(subsection);
      continue;
    }
    matchedGuides.push(`【${subsection} 对应指导】\n${matchedGuide.guide}`);
  }

  return {
    guide: matchedGuides.join("\n\n"),
    unmatchedSubsections,
  };
}
