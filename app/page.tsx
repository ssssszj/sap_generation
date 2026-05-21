"use client";

import { useState, useCallback, useEffect, useRef } from "react";
import { SAP_SPEC, type SapSection } from "@/lib/sap-spec";
import styles from "./page.module.css";

interface CoverMeta {
  studyTitle?: string;
  studyTitleEn?: string;
  protocolNo?: string;
  version?: string;
  date?: string;
  sponsor?: string;
  leadStatistician?: string;
}

interface CoreContentItem {
  id: string;
  title: string;
  content: string;
  confirmed?: boolean;
}

type Step = "core" | "outline" | "generate";

const cloneDefaultOutline = (): SapSection[] =>
  SAP_SPEC.map((section) => ({
    ...section,
    subsections: [...section.subsections],
  }));

export default function SapGeneratePage() {
  const protocolInputRef = useRef<HTMLInputElement | null>(null);
  const crfInputRef = useRef<HTMLInputElement | null>(null);
  const [protocolFile, setProtocolFile] = useState<File | null>(null);
  const [crfFile, setCrfFile] = useState<File | null>(null);
  const [meta, setMeta] = useState<CoverMeta>({
    version: "1.0",
    date: new Date().toISOString().slice(0, 10),
  });
  const [step, setStep] = useState<Step>("core");
  const [coreItems, setCoreItems] = useState<CoreContentItem[]>([]);
  const [coreLoading, setCoreLoading] = useState(false);
  const [revisingId, setRevisingId] = useState<string | null>(null);
  const [feedbackById, setFeedbackById] = useState<Record<string, string>>({});
  const [outline, setOutline] = useState<SapSection[]>(cloneDefaultOutline);
  const [outlineConfirmed, setOutlineConfirmed] = useState(false);
  const [newOutlineTitle, setNewOutlineTitle] = useState("");
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState<{ current: number; total: number; sectionTitle: string } | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [fullDocument, setFullDocument] = useState<string | null>(null);
  const [coverMeta, setCoverMeta] = useState<CoverMeta | null>(null);
  const [tflLoading, setTflLoading] = useState(false);
  const [tflProgress, setTflProgress] = useState<{
    step: "table" | "figure" | "listing";
    status: "generating" | "done";
    label: string;
  } | null>(null);
  const [tflDocument, setTflDocument] = useState<string | null>(null);
  const [toast, setToast] = useState<string | null>(null);

  const allCoreConfirmed =
    coreItems.length > 0 && coreItems.every((item) => item.confirmed && item.content.trim());

  useEffect(() => {
    if (!toast) return;
    const timer = setTimeout(() => setToast(null), 3000);
    return () => clearTimeout(timer);
  }, [toast]);

  const resetGeneratedOutputs = useCallback(() => {
    setFullDocument(null);
    setCoverMeta(null);
    setTflDocument(null);
    setProgress(null);
    setTflProgress(null);
  }, []);

  const handleProtocolChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    setProtocolFile(e.target.files?.[0] ?? null);
    setError(null);
    setCoreItems([]);
    setStep("core");
    setOutlineConfirmed(false);
    resetGeneratedOutputs();
  }, [resetGeneratedOutputs]);

  const handleCrfChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    setCrfFile(e.target.files?.[0] ?? null);
    setError(null);
    setCoreItems([]);
    setStep("core");
    setOutlineConfirmed(false);
    resetGeneratedOutputs();
  }, [resetGeneratedOutputs]);

  const handleMetaChange = useCallback((field: keyof CoverMeta, value: string) => {
    setMeta((prev) => ({ ...prev, [field]: value }));
  }, []);

  const buildFileFormData = useCallback(() => {
    const currentProtocolFile = protocolFile ?? protocolInputRef.current?.files?.[0] ?? null;
    const currentCrfFile = crfFile ?? crfInputRef.current?.files?.[0] ?? null;
    if (!currentProtocolFile || !currentCrfFile) {
      throw new Error("请同时上传 Protocol 和 CRF 文件");
    }
    const formData = new FormData();
    formData.append("protocol", currentProtocolFile);
    formData.append("crf", currentCrfFile);
    return formData;
  }, [protocolFile, crfFile]);

  const handleGenerateCore = useCallback(async () => {
    setCoreLoading(true);
    setError(null);
    resetGeneratedOutputs();
    try {
      const formData = buildFileFormData();
      const res = await fetch("/api/generate-core-content", {
        method: "POST",
        body: formData,
      });
      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        throw new Error(data.error || "生成核心内容失败");
      }
      const data = (await res.json()) as { items: CoreContentItem[] };
      setCoreItems(data.items ?? []);
      setOutline(cloneDefaultOutline());
      setOutlineConfirmed(false);
      setStep("core");
    } catch (err) {
      setError(err instanceof Error ? err.message : "生成核心内容时发生错误");
    } finally {
      setCoreLoading(false);
    }
  }, [buildFileFormData, resetGeneratedOutputs]);

  const handleConfirmCoreItem = useCallback((id: string) => {
    setCoreItems((items) =>
      items.map((item) => (item.id === id ? { ...item, confirmed: true } : item))
    );
    setFeedbackById((prev) => ({ ...prev, [id]: "" }));
  }, []);

  const handleReviseCoreItem = useCallback(
    async (item: CoreContentItem) => {
      const feedback = feedbackById[item.id]?.trim();
      if (!feedback) {
        setError("请先填写反馈，再重新生成该项核心内容");
        return;
      }
      setRevisingId(item.id);
      setError(null);
      try {
        const formData = buildFileFormData();
        formData.append("item", JSON.stringify(item));
        formData.append("allItems", JSON.stringify(coreItems));
        formData.append("feedback", feedback);
        const res = await fetch("/api/revise-core-content", {
          method: "POST",
          body: formData,
        });
        if (!res.ok) {
          const data = await res.json().catch(() => ({}));
          throw new Error(data.error || "重新生成核心内容失败");
        }
        const data = (await res.json()) as { item: CoreContentItem };
        setCoreItems((items) =>
          items.map((current) => (current.id === item.id ? data.item : current))
        );
        setFeedbackById((prev) => ({ ...prev, [item.id]: "" }));
      } catch (err) {
        setError(err instanceof Error ? err.message : "修订核心内容时发生错误");
      } finally {
        setRevisingId(null);
      }
    },
    [buildFileFormData, coreItems, feedbackById]
  );

  const handleCoreTextChange = useCallback((id: string, content: string) => {
    setCoreItems((items) =>
      items.map((item) =>
        item.id === id ? { ...item, content, confirmed: false } : item
      )
    );
  }, []);

  const proceedToOutline = useCallback(() => {
    if (!allCoreConfirmed) {
      setError("请先确认每一项核心内容，再进入大纲编辑");
      return;
    }
    setError(null);
    setStep("outline");
  }, [allCoreConfirmed]);

  const removeOutlineSection = useCallback((index: number) => {
    setOutlineConfirmed(false);
    setOutline((sections) => sections.filter((_, i) => i !== index));
  }, []);

  const addOutlineSection = useCallback(() => {
    const title = newOutlineTitle.trim();
    if (!title) {
      setError("请输入要新增的一级目录标题");
      return;
    }
    setOutlineConfirmed(false);
    setOutline((sections) => {
      const numericIds = sections
        .map((section) => Number(section.id.replace(/\D/g, "")))
        .filter((id) => Number.isFinite(id));
      const nextId = `${numericIds.length ? Math.max(...numericIds) + 1 : sections.length}`;
      return [
        ...sections,
        {
          id: nextId,
          title,
          titleEn: "",
          description: "用户新增章节，由大模型根据核心内容与上下文自主生成",
          subsections: [],
        },
      ];
    });
    setNewOutlineTitle("");
    setError(null);
  }, [newOutlineTitle]);

  const confirmOutline = useCallback(() => {
    const cleaned = outline
      .map((section) => ({
        ...section,
        id: section.id.trim(),
        title: section.title.trim(),
        titleEn: section.titleEn?.trim(),
        description: section.description.trim() || "用户确认的大纲章节",
        subsections: section.subsections.map((s) => s.trim()).filter(Boolean),
      }))
      .filter((section) => section.id && section.title);
    if (!cleaned.length) {
      setError("大纲至少需要保留一个章节");
      return;
    }
    setOutline(cleaned);
    setOutlineConfirmed(true);
    setStep("generate");
    setError(null);
    resetGeneratedOutputs();
  }, [outline, resetGeneratedOutputs]);

  const handleGenerateSap = useCallback(async () => {
    if (!allCoreConfirmed || !outlineConfirmed) {
      setError("请先确认核心内容和大纲，再生成 SAP");
      return;
    }
    setLoading(true);
    setError(null);
    resetGeneratedOutputs();
    try {
      const formData = buildFileFormData();
      formData.append("meta", JSON.stringify(meta));
      formData.append("coreContent", JSON.stringify(coreItems));
      formData.append("outline", JSON.stringify(outline));
      const res = await fetch("/api/generate-sap", {
        method: "POST",
        body: formData,
      });
      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        throw new Error(data.error || "生成失败");
      }
      const reader = res.body?.getReader();
      const decoder = new TextDecoder();
      if (!reader) throw new Error("无法读取响应流");
      let buffer = "";
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n");
        buffer = lines.pop() ?? "";
        for (const line of lines) {
          const trimmed = line.trim();
          if (!trimmed) continue;
          const msg = JSON.parse(trimmed) as {
            type: string;
            current?: number;
            total?: number;
            section?: { id: string; title: string; titleEn?: string };
            result?: { fullDocument: string; coverMeta: CoverMeta };
            error?: string;
          };
          if (msg.type === "progress" && msg.current != null && msg.total != null && msg.section) {
            setProgress({
              current: msg.current,
              total: msg.total,
              sectionTitle: `${msg.section.id} ${msg.section.title}${msg.section.titleEn ? ` / ${msg.section.titleEn}` : ""}`,
            });
          } else if (msg.type === "done" && msg.result) {
            setFullDocument(msg.result.fullDocument);
            setCoverMeta(msg.result.coverMeta ?? null);
            setProgress(null);
          } else if (msg.type === "error" && msg.error) {
            setError(msg.error);
            setProgress(null);
          }
        }
      }
      if (buffer.trim()) {
        const msg = JSON.parse(buffer.trim());
        if (msg.type === "done" && msg.result) {
          setFullDocument(msg.result.fullDocument);
          setCoverMeta(msg.result.coverMeta ?? null);
        } else if (msg.type === "error" && msg.error) setError(msg.error);
      }
      setProgress(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : "生成 SAP 时发生错误");
      setProgress(null);
    } finally {
      setLoading(false);
    }
  }, [
    allCoreConfirmed,
    buildFileFormData,
    coreItems,
    meta,
    outline,
    outlineConfirmed,
    resetGeneratedOutputs,
  ]);

  const TFL_STEP_LABELS: Record<"table" | "figure" | "listing", string> = {
    table: "Table shells",
    figure: "Figure and graph shells",
    listing: "Listing shells",
  };
  const TFL_STEP_ORDER = { table: 1, figure: 2, listing: 3 };

  const handleGenerateTfl = useCallback(async () => {
    if (!protocolFile || !crfFile || !fullDocument) {
      setError("请先完成 SAP 生成后再生成 TFL Shells");
      return;
    }
    setTflLoading(true);
    setError(null);
    setTflDocument(null);
    setTflProgress(null);
    try {
      const formData = new FormData();
      formData.append("protocol", protocolFile);
      formData.append("crf", crfFile);
      formData.append("sapText", fullDocument);
      const res = await fetch("/api/generate-tfl-shells", {
        method: "POST",
        body: formData,
      });
      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        throw new Error(data.error || "生成 TFL Shells 失败");
      }
      const reader = res.body?.getReader();
      const decoder = new TextDecoder();
      if (!reader) throw new Error("无法读取响应流");
      let buffer = "";
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n");
        buffer = lines.pop() ?? "";
        for (const line of lines) {
          const trimmed = line.trim();
          if (!trimmed) continue;
          const msg = JSON.parse(trimmed) as {
            type: string;
            step?: "table" | "figure" | "listing";
            status?: "generating" | "done";
            result?: { fullDocument: string };
            error?: string;
          };
          if (msg.type === "progress" && msg.step && msg.status) {
            setTflProgress({
              step: msg.step,
              status: msg.status,
              label: TFL_STEP_LABELS[msg.step],
            });
          } else if (msg.type === "done" && msg.result) {
            setTflDocument(msg.result.fullDocument);
            setTflProgress(null);
          } else if (msg.type === "error" && msg.error) {
            setError(msg.error);
            setTflProgress(null);
          }
        }
      }
      if (buffer.trim()) {
        const msg = JSON.parse(buffer.trim());
        if (msg.type === "done" && msg.result) setTflDocument(msg.result.fullDocument);
        else if (msg.type === "error" && msg.error) setError(msg.error);
      }
      setTflProgress(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : "生成 TFL Shells 时发生错误");
      setTflProgress(null);
    } finally {
      setTflLoading(false);
    }
  }, [crfFile, fullDocument, protocolFile]);

  const tflProgressPercent =
    tflProgress == null
      ? 0
      : tflProgress.status === "done"
        ? (TFL_STEP_ORDER[tflProgress.step] / 3) * 100
        : ((TFL_STEP_ORDER[tflProgress.step] - 1) / 3) * 100;

  return (
    <main className={styles.main}>
      <header className={styles.header}>
        <h1>统计分析计划（SAP）生成</h1>
        <p>先确认核心内容，再编辑大纲，最后按章节生成完整 SAP 文档</p>
      </header>

      <section className={styles.section}>
        <div className={styles.stepHeader}>
          <span className={styles.stepBadge}>准备</span>
          <h2>上传文件与封面信息</h2>
        </div>
        <div className={styles.form}>
          <div className={styles.field}>
            <label>Protocol（研究方案）</label>
            <input ref={protocolInputRef} type="file" accept=".pdf,.docx,.txt,.md" onChange={handleProtocolChange} disabled={loading || coreLoading} />
            {protocolFile && <span className={styles.hint}>{protocolFile.name}</span>}
          </div>
          <div className={styles.field}>
            <label>CRF（病例报告表）</label>
            <input ref={crfInputRef} type="file" accept=".pdf,.docx,.txt,.md" onChange={handleCrfChange} disabled={loading || coreLoading} />
            {crfFile && <span className={styles.hint}>{crfFile.name}</span>}
          </div>
          <p className={styles.note}>支持 .pdf、.docx、.txt、.md。系统会先解析文件，再进入三步生成流程。</p>

          <h3>封面信息（可选）</h3>
          <div className={styles.grid}>
            {[
              ["studyTitle", "研究题目", "中文"],
              ["studyTitleEn", "Study Title", "English"],
              ["protocolNo", "方案号", ""],
              ["version", "版本号", ""],
              ["date", "日期", ""],
              ["sponsor", "申办方", ""],
              ["leadStatistician", "统计负责人", ""],
            ].map(([field, label, placeholder]) => (
              <div className={styles.field} key={field}>
                <label>{label}</label>
                <input
                  type={field === "date" ? "date" : "text"}
                  value={meta[field as keyof CoverMeta] ?? ""}
                  onChange={(e) => handleMetaChange(field as keyof CoverMeta, e.target.value)}
                  placeholder={placeholder}
                  disabled={loading}
                />
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className={`${styles.section} ${step === "core" ? styles.activeSection : ""}`}>
        <div className={styles.stepHeader}>
          <span className={styles.stepBadge}>1</span>
          <h2>生成并确认核心内容</h2>
        </div>
        <p className={styles.note}>核心内容列表由系统固定维护，用于完整 SAP 生成前确认 Synopsis 统计口径，不生成 SAP 正文或 TFL shells。</p>
        <button type="button" className={styles.submit} onClick={handleGenerateCore} disabled={coreLoading || loading}>
          {coreLoading ? "正在生成核心内容..." : "生成核心内容"}
        </button>

        {coreItems.length > 0 && (
          <div className={styles.coreList}>
            {coreItems.map((item, index) => (
              <article className={styles.coreItem} key={item.id}>
                <div className={styles.coreTitleRow}>
                  <h3>{index + 1}. {item.title}</h3>
                  <span className={item.confirmed ? styles.statusOk : styles.statusPending}>
                    {item.confirmed ? "已确认" : "待确认"}
                  </span>
                </div>
                <textarea
                  className={styles.reviewTextarea}
                  value={item.content}
                  onChange={(e) => handleCoreTextChange(item.id, e.target.value)}
                  disabled={loading || revisingId === item.id}
                />
                <div className={styles.feedbackRow}>
                  <textarea
                    className={styles.feedback}
                    value={feedbackById[item.id] ?? ""}
                    onChange={(e) => setFeedbackById((prev) => ({ ...prev, [item.id]: e.target.value }))}
                    placeholder="如需修改，请在这里写反馈，然后点击重新生成该项。"
                    disabled={loading || revisingId === item.id}
                  />
                  <div className={styles.verticalActions}>
                    <button type="button" className={styles.download} onClick={() => handleConfirmCoreItem(item.id)} disabled={loading || revisingId === item.id || !item.content.trim()}>
                      确认
                    </button>
                    <button type="button" className={styles.secondaryButton} onClick={() => handleReviseCoreItem(item)} disabled={loading || revisingId === item.id}>
                      {revisingId === item.id ? "重新生成中..." : "按反馈重新生成"}
                    </button>
                  </div>
                </div>
              </article>
            ))}
            <button type="button" className={styles.submit} onClick={proceedToOutline} disabled={!allCoreConfirmed || loading}>
              进入大纲编辑
            </button>
          </div>
        )}
      </section>

      <section className={`${styles.section} ${step === "outline" ? styles.activeSection : ""}`}>
        <div className={styles.stepHeader}>
          <span className={styles.stepBadge}>2</span>
          <h2>确认一二级目录</h2>
        </div>
        <p className={styles.note}>这里展示当前生成用大纲。删除的一级目录不会在第三步生成；新增目录没有预置指导，会由模型结合核心内容和上下文自主生成。</p>
        <div className={styles.outlineList}>
          {outline.map((section, index) => (
            <article className={styles.outlineItem} key={`${section.id}-${index}`}>
              <div className={styles.outlineRow}>
                <div className={styles.outlineTitle}>
                  <span className={styles.outlineNo}>{section.id}</span>
                  <span>{section.title}{section.titleEn ? ` / ${section.titleEn}` : ""}</span>
                </div>
                <button type="button" className={styles.dangerButton} onClick={() => removeOutlineSection(index)} disabled={loading || !allCoreConfirmed}>
                  删除
                </button>
              </div>
              {section.subsections.length > 0 && (
                <ol className={styles.subOutlineList}>
                  {section.subsections.map((subsection) => (
                    <li key={subsection}>{subsection}</li>
                  ))}
                </ol>
              )}
            </article>
          ))}
        </div>
        <div className={styles.addOutlineRow}>
          <input
            value={newOutlineTitle}
            onChange={(e) => setNewOutlineTitle(e.target.value)}
            placeholder="输入新增一级目录标题"
            disabled={loading || !allCoreConfirmed}
          />
          <button type="button" className={styles.secondaryButton} onClick={addOutlineSection} disabled={loading || !allCoreConfirmed}>
            新增一级目录
          </button>
        </div>
        <div className={styles.actions}>
          <button type="button" className={styles.submit} onClick={confirmOutline} disabled={!allCoreConfirmed || loading}>
            确认大纲，进入生成
          </button>
        </div>
        {outlineConfirmed && <p className={styles.note}>大纲已确认，共 {outline.length} 个章节。</p>}
      </section>

      <section className={`${styles.section} ${step === "generate" ? styles.activeSection : ""}`}>
        <div className={styles.stepHeader}>
          <span className={styles.stepBadge}>3</span>
          <h2>按章节生成 SAP</h2>
        </div>
        {error && <div className={styles.error}>{error}</div>}
        {loading && progress && (
          <div className={styles.progressWrap}>
            <div className={styles.progressText}>
              正在生成 SAP：第 {progress.current} / {progress.total} 章 - {progress.sectionTitle}
            </div>
            <div className={styles.progressBar}>
              <div className={styles.progressFill} style={{ width: `${(100 * progress.current) / progress.total}%` }} />
            </div>
          </div>
        )}
        <button type="button" className={styles.submit} onClick={handleGenerateSap} disabled={loading || !allCoreConfirmed || !outlineConfirmed}>
          {loading ? "正在生成 SAP..." : "生成 SAP"}
        </button>
      </section>

      {fullDocument && (
        <section className={styles.section}>
          <h2>生成的 SAP 文档</h2>
          <div className={styles.actions}>
            <button type="button" onClick={handleGenerateTfl} className={styles.tflButton} disabled={tflLoading}>
              {tflLoading ? "正在生成 TFL Shells..." : "生成 TFL Shells"}
            </button>
          </div>
          {tflLoading && tflProgress && (
            <div className={styles.progressWrap}>
              <div className={styles.progressText}>
                正在生成 TFL Shells：{tflProgress.label}
                {tflProgress.status === "done" ? " 已完成" : " 生成中..."}
              </div>
              <div className={styles.progressBar}>
                <div className={styles.progressFill} style={{ width: `${tflProgressPercent}%` }} />
              </div>
            </div>
          )}
          <div className={styles.preview}>
            <div className={styles.document}>{fullDocument.split(/\r?\n/).map((line, i) => (
              <p key={i} className={styles.para}>{line || "\u00A0"}</p>
            ))}</div>
          </div>
        </section>
      )}

      {tflDocument && (
        <section className={styles.section}>
          <h2>生成的 TFL Shells</h2>
          <p className={styles.note}>TFL shells 为 Table / Figure / Listing 输出模板，用于明确展示结构与统计口径，不包含真实结果。</p>
          <div className={styles.preview}>
            <div className={styles.document}>{tflDocument.split(/\r?\n/).map((line, i) => (
              <p key={i} className={styles.para}>{line || "\u00A0"}</p>
            ))}</div>
          </div>
        </section>
      )}

      <footer className={styles.footer}>
        <p>SAP 生成依据用户确认的核心内容与大纲，各章节由独立 Agent 生成后合并</p>
      </footer>

      {toast && <div className={styles.toast}>{toast}</div>}
    </main>
  );
}
