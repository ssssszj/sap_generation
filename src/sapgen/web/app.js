const state = { projectId: "", latestRunId: "" };

async function api(path, options = {}) {
  const response = await fetch(path, options);
  if (!response.ok) {
    let detail = response.statusText;
    try { detail = (await response.json()).detail || detail; } catch (_) {}
    throw new Error(detail);
  }
  return response.json();
}

function status(message, isError = false) {
  const node = document.querySelector("#run-status");
  node.textContent = message;
  node.style.borderLeftColor = isError ? "#a93030" : "#2674a9";
  node.classList.remove("hidden");
}

async function refreshProjects(selectId = "") {
  const projects = await api("/api/projects");
  const select = document.querySelector("#project-select");
  select.innerHTML = '<option value="">请选择项目</option>';
  for (const project of projects) {
    const option = document.createElement("option");
    option.value = project.id;
    option.textContent = `${project.name} (${project.id})`;
    select.append(option);
  }
  if (selectId) select.value = selectId;
}

async function refreshProject() {
  const list = document.querySelector("#file-list");
  list.innerHTML = "";
  if (!state.projectId) return;
  const project = await api(`/api/projects/${state.projectId}`);
  for (const filename of project.inputs) {
    const item = document.createElement("li");
    item.textContent = filename;
    list.append(item);
  }
  document.querySelector("#use-working-ir").disabled = !project.has_working_ir;
}

document.querySelector("#project-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  try {
    const name = document.querySelector("#project-name").value.trim();
    const project = await api("/api/projects", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name }),
    });
    state.projectId = project.id;
    await refreshProjects(project.id);
    await refreshProject();
    status(`已创建项目 ${project.id}`);
  } catch (error) { status(error.message, true); }
});

document.querySelector("#project-select").addEventListener("change", async (event) => {
  state.projectId = event.target.value;
  await refreshProject();
});

document.querySelector("#upload-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!state.projectId) return status("请先选择项目。", true);
  const files = document.querySelector("#files").files;
  if (!files.length) return status("请选择至少一个文件。", true);
  const body = new FormData();
  for (const file of files) body.append("files", file);
  try {
    await api(`/api/projects/${state.projectId}/inputs`, { method: "POST", body });
    await refreshProject();
    status(`已上传 ${files.length} 个文件。`);
  } catch (error) { status(error.message, true); }
});

document.querySelector("#run-button").addEventListener("click", async () => {
  if (!state.projectId) return status("请先选择项目。", true);
  const body = new FormData();
  body.append("use_working_ir", document.querySelector("#use-working-ir").checked);
  body.append("allow_harness_fallback", document.querySelector("#allow-fallback").checked);
  status("正在执行证据提取、专项模块与规则检查，请稍候……");
  document.querySelector("#run-button").disabled = true;
  try {
    const result = await api(`/api/projects/${state.projectId}/runs`, { method: "POST", body });
    state.latestRunId = result.run_id;
    renderResult(result);
    status(`运行 ${result.run_id} 已完成。`);
  } catch (error) { status(error.message, true); }
  finally { document.querySelector("#run-button").disabled = false; }
});

function renderResult(result) {
  const results = document.querySelector("#results");
  const counts = result.report.issues.reduce((acc, item) => {
    acc[item.severity] = (acc[item.severity] || 0) + 1;
    return acc;
  }, { error: 0, warning: 0, info: 0 });
  document.querySelector("#issue-counts").innerHTML = ["error", "warning", "info"]
    .map((key) => `<span class="count ${key}">${key}: ${counts[key]}</span>`).join("");
  const artifacts = [
    ["SAP 草稿 Word", "sap-draft.docx"],
    ["TFL 表壳 Word", "tfl-shells.docx"],
    ["SAP-IR", "sap-ir.json"],
    ["检查报告", "validation-report.json"],
    ["Markdown 草稿", "sap-draft.md"],
  ];
  document.querySelector("#artifacts").innerHTML = artifacts.map(([label, file]) =>
    `<a href="/api/runs/${result.run_id}/artifacts/${file}">${label}</a>`).join("");
  const table = document.querySelector("#issue-table");
  table.innerHTML = "";
  for (const issue of result.report.issues) {
    const row = document.createElement("tr");
    row.innerHTML = `<td class="severity-${issue.severity}">${issue.severity}</td>`
      + `<td>${issue.module}</td><td>${issue.message}</td><td><code>${issue.path}</code></td>`;
    table.append(row);
  }
  results.classList.remove("hidden");
}

async function boot() {
  try {
    const health = await api("/api/health");
    document.querySelector("#health").textContent = health.harness_configured
      ? "DeepSeek Harness 已接入" : "规则模式，Harness 未启用";
    await refreshProjects();
  } catch (error) {
    document.querySelector("#health").textContent = "服务不可用";
    status(error.message, true);
  }
}

boot();

