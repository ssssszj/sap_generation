/**
 * LLM 客户端抽象接口
 * 支持 OpenRouter API（https://openrouter.ai）
 */
export interface LLMMessage {
  role: "system" | "user" | "assistant";
  content: string;
}

export interface LLMCallOptions {
  model?: string;
  temperature?: number;
  maxTokens?: number;
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

const OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions";

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
  timeoutMs: number = 60000
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
 * OpenRouter API 客户端
 * 需配置环境变量 OPENROUTER_API_KEY
 * 可选环境变量 OPENROUTER_MODEL 设置默认模型（如 openai/gpt-4o、anthropic/claude-3-haiku）
 * 可选环境变量 HTTPS_PROXY 或 HTTP_PROXY：服务端请求走代理（解决地区限制）
 */
export class OpenRouterLLMClient implements LLMClient {
  constructor(
    private apiKey: string,
    private defaultModel: string = "openai/gpt-4o"
  ) {}

  async chat(messages: LLMMessage[], options?: LLMCallOptions): Promise<string> {
    const model = options?.model ?? this.defaultModel;
    const temperature = options?.temperature ?? 0.3;
    const max_tokens = options?.maxTokens ?? 4096;

    // 默认不使用代理，避免你环境里残留的 HTTPS_PROXY/HTTP_PROXY 导致请求抖动/失败。
    // 如需启用代理：在 .env.local 设置 OPENROUTER_PROXY_MODE=on
    const proxyMode = process.env.OPENROUTER_PROXY_MODE?.trim().toLowerCase();
    const proxyEnabled =
      proxyMode === "on" || proxyMode === "true" || proxyMode === "1";

    const proxy = proxyEnabled
      ? process.env.HTTPS_PROXY?.trim() || process.env.HTTP_PROXY?.trim() || ""
      : "";

    const maxAttempts = 5;
    let lastErr: unknown = null;
    for (let attempt = 1; attempt <= maxAttempts; attempt++) {
      try {
        const { status, text } = await postJson(
          OPENROUTER_URL,
          {
            model,
            messages: messages.map((m) => ({ role: m.role, content: m.content })),
            temperature,
            max_tokens,
          },
          {
            "Content-Type": "application/json",
            Authorization: `Bearer ${this.apiKey}`,
          },
          proxy || undefined,
          35000
        );

        if (status < 200 || status >= 300) {
          throw new Error(`OpenRouter API 错误 (${status}): ${text}`);
        }

        const raw = (text ?? "").trim();
        if (!raw) {
          throw new Error("OpenRouter 返回空响应体");
        }

        let data: {
          choices?: Array<{ message?: { content?: string } }>;
        };
        try {
          data = JSON.parse(raw) as {
            choices?: Array<{ message?: { content?: string } }>;
          };
        } catch (e) {
          const parseErr = e instanceof Error ? e.message : String(e);
          throw new Error(
            `OpenRouter 响应 JSON 解析失败: ${parseErr}; body=${shorten(raw)}`
          );
        }

        const content = data.choices?.[0]?.message?.content;
        return typeof content === "string" ? content : "";
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

        const retryableByMessage =
          /Unexpected end of JSON input|JSON 解析失败|返回空响应体|Request timeout/i.test(
            message
          );

        if (!retryableCodes.has(code ?? "") && !retryableByMessage) {
          throw err;
        }
        if (attempt === maxAttempts) throw err;

        // 指数退避 + 小抖动
        const backoff = 450 * Math.pow(2, attempt - 1);
        const jitter = Math.floor(Math.random() * 150);
        await sleep(backoff + jitter);
      }
    }

    // 理论上不会到这里
    throw lastErr ?? new Error("OpenRouter 请求失败");
  }
}

/**
 * 占位实现：当未配置 OPENROUTER_API_KEY 时使用
 */
export class PlaceholderLLMClient implements LLMClient {
  async chat(messages: LLMMessage[], _options?: LLMCallOptions): Promise<string> {
    const lastUser = messages.filter((m) => m.role === "user").pop();
    const prompt = lastUser?.content ?? "";
    const sectionMatch = prompt.match(/章节\s*[：:]\s*(\d+)[\s\S]*?标题[：:]\s*([^\n]+)/);
    const id = sectionMatch?.[1] ?? "?";
    const title = sectionMatch?.[2]?.trim() ?? "未识别";
    return `【本节为占位内容，请配置 OPENROUTER_API_KEY 环境变量以使用真实 LLM】\n\n本章节（${id} ${title}）应根据用户提供的 Protocol 与 CRF 内容，由 LLM 生成完整的统计分析计划正文。`;
  }
}

/**
 * 工厂：优先使用 OpenRouter，未配置 API Key 时回退到占位实现
 */
export function createLLMClient(): LLMClient {
  const apiKey = process.env.OPENROUTER_API_KEY?.trim();
  if (apiKey) {
    const model = process.env.OPENROUTER_MODEL?.trim() || "openai/gpt-4o";
    return new OpenRouterLLMClient(apiKey, model);
  }
  return new PlaceholderLLMClient();
}
