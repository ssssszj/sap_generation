/**
 * LLM 客户端抽象接口
 * 支持七牛云 OpenAI 兼容 API
 */
export interface LLMMessage {
  role: "system" | "user" | "assistant";
  content: string;
}

export interface LLMCallOptions {
  model?: string;
  temperature?: number;
  maxTokens?: number;
  retryMaxTokens?: number;
  timeoutMs?: number;
  maxAttempts?: number;
  rejectTruncated?: boolean;
}

export interface LLMClient {
  /**
   * 调用 LLM 生成内容
   * @param messages 对话消息列表
   * @param options 可选参数
   * @returns 生成的文本
   */
  chat(messages: LLMMessage[], options?: LLMCallOptions): Promise<string>;
}

const DEFAULT_QNY_API_BASE_URL = "https://api.qnaigc.com";
const DEFAULT_QNY_MODEL = "deepseek/deepseek-v4.1-flash";
const DEFAULT_MAX_TOKENS = 65536;

function getChatCompletionsUrl(baseUrl: string): string {
  const normalized = baseUrl.trim().replace(/\/+$/, "");
  if (normalized.endsWith("/v1/chat/completions")) return normalized;
  if (normalized.endsWith("/v1")) return `${normalized}/chat/completions`;
  return `${normalized}/v1/chat/completions`;
}

type HttpResponse = { status: number; text: string };

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function shorten(s: string, max = 300): string {
  if (s.length <= max) return s;
  return `${s.slice(0, max)}...`;
}

async function postJson(
  url: string,
  payload: unknown,
  headers: Record<string, string>,
  proxy?: string,
  timeoutMs: number = 600000
): Promise<HttpResponse> {
  const { request } = await import("node:https");
  const { URL } = await import("node:url");
  const u = new URL(url);

  const body = JSON.stringify(payload);
  const finalHeaders: Record<string, string> = {
    ...headers,
    "Content-Length": Buffer.byteLength(body).toString(),
  };

  const agent = proxy
    ? // 使用 https-proxy-agent，避免在 Next 打包环境里引入 undici 的 WebIDL 依赖
      new (await import("https-proxy-agent")).HttpsProxyAgent(proxy)
    : undefined;

  return await new Promise<HttpResponse>((resolve, reject) => {
    const req = request(
      {
        protocol: u.protocol,
        hostname: u.hostname,
        port: u.port || 443,
        path: `${u.pathname}${u.search}`,
        method: "POST",
        headers: finalHeaders,
        agent,
      },
      (res) => {
        const chunks: Buffer[] = [];
        res.on("data", (c) => chunks.push(Buffer.isBuffer(c) ? c : Buffer.from(c)));
        res.on("end", () => {
          resolve({
            status: res.statusCode || 0,
            text: Buffer.concat(chunks).toString("utf-8"),
          });
        });
      }
    );
    req.setTimeout(timeoutMs, () => {
      req.destroy(new Error(`Request timeout after ${timeoutMs}ms`));
    });
    req.on("error", reject);
    req.write(body);
    req.end();
  });
}

/**
 * 七牛云 OpenAI 兼容 API 客户端
 * 需配置环境变量 QNY_API_KEY
 * 可选环境变量 QNY_MODEL 设置默认模型
 * 可选环境变量 QNY_API_BASE_URL 切换请求域名
 * 可选环境变量 HTTPS_PROXY 或 HTTP_PROXY：服务端请求走代理
 */
export class QiniuLLMClient implements LLMClient {
  constructor(
    private apiKey: string,
    private defaultModel: string = DEFAULT_QNY_MODEL,
    private apiBaseUrl: string = DEFAULT_QNY_API_BASE_URL
  ) {}

  async chat(messages: LLMMessage[], options?: LLMCallOptions): Promise<string> {
    const model = options?.model ?? this.defaultModel;
    const experimentMaxTokens = Number.parseInt(
      process.env.SAP_EXPERIMENT_MAX_TOKENS?.trim() || "",
      10
    );
    const hasExperimentMaxTokens =
      Number.isFinite(experimentMaxTokens) && experimentMaxTokens > 0;
    const maxTokens = hasExperimentMaxTokens
      ? experimentMaxTokens
      : options?.maxTokens ?? DEFAULT_MAX_TOKENS;
    const useProviderDefaultTemperature =
      process.env.SAP_EXPERIMENT_PROVIDER_DEFAULT_TEMPERATURE?.trim() === "1";
    const temperature = options?.temperature ?? 0.3;
    // Benchmark runs must keep the same token ceiling even after a transient retry.
    const retryMaxTokens = hasExperimentMaxTokens
      ? maxTokens
      : Math.max(maxTokens, options?.retryMaxTokens ?? maxTokens);
    const timeoutMs = options?.timeoutMs ?? 600000;
    const maxAttempts = options?.maxAttempts ?? 2;
    const inputChars = messages.reduce((sum, message) => sum + message.content.length, 0);

    // 默认不使用代理，避免环境中残留的 HTTPS_PROXY/HTTP_PROXY 影响国内接口。
    // 如需启用代理：在 .env.local 设置 QNY_PROXY_MODE=on。
    const proxyMode = process.env.QNY_PROXY_MODE?.trim().toLowerCase();
    const proxyEnabled =
      proxyMode === "on" || proxyMode === "true" || proxyMode === "1";

    const proxy = proxyEnabled
      ? process.env.HTTPS_PROXY?.trim() || process.env.HTTP_PROXY?.trim() || ""
      : "";

    let lastErr: unknown = null;
    for (let attempt = 1; attempt <= maxAttempts; attempt++) {
      const attemptStartedAt = Date.now();
      const attemptMaxTokens = attempt === 1 ? maxTokens : retryMaxTokens;
      try {
        const { status, text } = await postJson(
          getChatCompletionsUrl(this.apiBaseUrl),
          {
            model,
            messages: messages.map((m) => ({ role: m.role, content: m.content })),
            ...(useProviderDefaultTemperature ? {} : { temperature }),
            max_tokens: attemptMaxTokens,
          },
          {
            "Content-Type": "application/json",
            Authorization: `Bearer ${this.apiKey}`,
          },
          proxy || undefined,
          timeoutMs
        );

        if (status < 200 || status >= 300) {
          throw new Error(`七牛云 API 错误 (${status}): ${text}`);
        }

        const raw = (text ?? "").trim();
        if (!raw) {
          throw new Error("七牛云 API 返回空响应体");
        }

        let data: {
          model?: string;
          choices?: Array<{
            finish_reason?: string | null;
            message?: {
              content?: string | null;
              reasoning_content?: string | null;
            };
          }>;
          usage?: {
            prompt_tokens?: number;
            completion_tokens?: number;
            total_tokens?: number;
          };
        };
        try {
          data = JSON.parse(raw) as typeof data;
        } catch (e) {
          const parseErr = e instanceof Error ? e.message : String(e);
          throw new Error(
            `七牛云 API 响应 JSON 解析失败: ${parseErr}; body=${shorten(raw)}`
          );
        }

        const choice = data.choices?.[0];
        const content = choice?.message?.content;
        const reasoningContent = choice?.message?.reasoning_content;
        const metadata = {
          model: data.model ?? model,
          attempt,
          maxTokens: attemptMaxTokens,
          inputChars,
          elapsedMs: Date.now() - attemptStartedAt,
          finishReason: choice?.finish_reason ?? null,
          promptTokens: data.usage?.prompt_tokens ?? null,
          completionTokens: data.usage?.completion_tokens ?? null,
          totalTokens: data.usage?.total_tokens ?? null,
          contentLength: typeof content === "string" ? content.length : 0,
          hasReasoningContent:
            typeof reasoningContent === "string" && reasoningContent.trim().length > 0,
        };

        if (
          typeof content === "string" &&
          content.trim() &&
          options?.rejectTruncated &&
          choice?.finish_reason === "length"
        ) {
          console.warn("Qiniu LLM returned truncated content", metadata);
          throw new Error(
            `七牛云 API 输出达到 token 上限 (finish_reason=length, content_length=${content.length})`
          );
        }

        if (typeof content === "string" && content.trim()) {
          console.info("Qiniu LLM response completed", metadata);
          return content;
        }

        console.warn("Qiniu LLM returned empty content", metadata);
        throw new Error(
          `七牛云 API 返回空内容 (finish_reason=${choice?.finish_reason ?? "unknown"}, reasoning_content=${metadata.hasReasoningContent ? "present" : "absent"})`
        );
      } catch (err) {
        lastErr = err;
        const errObj =
          typeof err === "object" && err ? (err as { code?: string; message?: string }) : {};
        const code = errObj.code;
        const message = errObj.message ?? String(err);

        // 网络抖动/重置时重试；其它错误直接抛出
        const retryableCodes = new Set([
          "ECONNRESET",
          "ECONNREFUSED",
          "ETIMEDOUT",
          "EAI_AGAIN",
          "ECONNABORTED",
          "ENOTFOUND",
        ]);

        const tokenLimitReached =
          /finish_reason=length|输出达到 token 上限/i.test(message);
        const canIncreaseTokenBudget = retryMaxTokens > attemptMaxTokens;
        const retryableByMessage =
          /Unexpected end of JSON input|JSON 解析失败|返回空响应体|Request timeout|七牛云 API 错误 \((429|5\d\d)\)/i.test(
            message
          ) ||
          (/返回空内容/i.test(message) &&
            (!tokenLimitReached || canIncreaseTokenBudget)) ||
          (tokenLimitReached && canIncreaseTokenBudget);

        if (!retryableCodes.has(code ?? "") && !retryableByMessage) {
          throw err;
        }
        if (attempt === maxAttempts) throw err;

        console.warn("Qiniu LLM request will retry", {
          model,
          attempt,
          maxAttempts,
          maxTokens: attemptMaxTokens,
          retryMaxTokens,
          elapsedMs: Date.now() - attemptStartedAt,
          errorCode: code ?? null,
          error: shorten(message, 240),
        });

        // 指数退避 + 小抖动
        const backoff = 450 * Math.pow(2, attempt - 1);
        const jitter = Math.floor(Math.random() * 150);
        await sleep(backoff + jitter);
      }
    }

    // 理论上不会到这里
    throw lastErr ?? new Error("七牛云 API 请求失败");
  }
}

/**
 * 占位实现：当未配置 QNY_API_KEY 时使用
 */
export class PlaceholderLLMClient implements LLMClient {
  async chat(messages: LLMMessage[], _options?: LLMCallOptions): Promise<string> {
    const lastUser = messages.filter((m) => m.role === "user").pop();
    const prompt = lastUser?.content ?? "";
    const sectionMatch = prompt.match(/章节\s*[：:]\s*(\d+)[\s\S]*?标题[：:]\s*([^\n]+)/);
    const id = sectionMatch?.[1] ?? "?";
    const title = sectionMatch?.[2]?.trim() ?? "未识别";
    return `【本节为占位内容，请配置 QNY_API_KEY 环境变量以使用真实 LLM】\n\n本章节（${id} ${title}）应根据用户提供的 Protocol 与 CRF 内容，由 LLM 生成完整的统计分析计划正文。`;
  }
}

/**
 * 工厂：优先使用七牛云，未配置 API Key 时回退到占位实现
 */
export function createLLMClient(): LLMClient {
  const apiKey = process.env.QNY_API_KEY?.trim();
  if (apiKey) {
    const model = process.env.QNY_MODEL?.trim() || DEFAULT_QNY_MODEL;
    const apiBaseUrl =
      process.env.QNY_API_BASE_URL?.trim() || DEFAULT_QNY_API_BASE_URL;
    return new QiniuLLMClient(apiKey, model, apiBaseUrl);
  }
  return new PlaceholderLLMClient();
}
