# 修复 npm 权限问题的 PowerShell 脚本
# 使用方法：在 PowerShell 中运行：.\fix-npm-permissions.ps1

Write-Host "正在修复 npm 权限问题..." -ForegroundColor Cyan

# 方案 1: 更改 npm 缓存目录到用户目录
$userCache = "$env:USERPROFILE\AppData\Local\npm-cache"
Write-Host "`n1. 设置 npm 缓存目录为: $userCache" -ForegroundColor Yellow
npm config set cache $userCache --global

# 验证配置
$currentCache = npm config get cache
Write-Host "   当前缓存目录: $currentCache" -ForegroundColor Green

# 清理旧缓存
Write-Host "`n2. 清理 npm 缓存..." -ForegroundColor Yellow
npm cache clean --force

# 删除项目中的 node_modules（如果存在）
if (Test-Path "node_modules") {
    Write-Host "`n3. 删除旧的 node_modules..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force node_modules -ErrorAction SilentlyContinue
}

# 删除 package-lock.json（如果存在）
if (Test-Path "package-lock.json") {
    Write-Host "   删除旧的 package-lock.json..." -ForegroundColor Yellow
    Remove-Item -Force package-lock.json -ErrorAction SilentlyContinue
}

# 重新安装依赖
Write-Host "`n4. 重新安装依赖..." -ForegroundColor Yellow
npm install

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✓ 安装成功！" -ForegroundColor Green
    Write-Host "`n验证安装的包:" -ForegroundColor Cyan
    npm list pdf-parse mammoth --depth=0
} else {
    Write-Host "`n✗ 安装失败，请尝试以管理员身份运行此脚本" -ForegroundColor Red
    Write-Host "   或者手动运行以下命令:" -ForegroundColor Yellow
    Write-Host "   npm config set cache `"$userCache`" --global" -ForegroundColor Gray
    Write-Host "   npm cache clean --force" -ForegroundColor Gray
    Write-Host "   npm install" -ForegroundColor Gray
}
