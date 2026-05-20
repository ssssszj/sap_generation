# 修复 Windows npm 权限问题

## 问题
npm install 时出现 `EPERM: operation not permitted` 错误，无法在 `D:\nodejs\node_cache` 创建目录。

## 解决方案

### 方案 1：更改 npm 缓存目录到用户目录（推荐）

在 PowerShell 中运行以下命令：

```powershell
# 将 npm 缓存目录改到用户目录（有权限的地方）
npm config set cache "C:\Users\$env:USERNAME\AppData\Local\npm-cache" --global

# 验证配置
npm config get cache

# 清理旧缓存（可选）
npm cache clean --force

# 重新安装依赖
npm install
```

### 方案 2：以管理员身份运行

1. 右键点击 PowerShell 或 CMD
2. 选择"以管理员身份运行"
3. 导航到项目目录：`cd D:\Lab\clinical_web`
4. 运行：`npm install`

### 方案 3：清理缓存后重试

```powershell
# 清理 npm 缓存
npm cache clean --force

# 删除 node_modules 和 package-lock.json（如果存在）
Remove-Item -Recurse -Force node_modules -ErrorAction SilentlyContinue
Remove-Item -Force package-lock.json -ErrorAction SilentlyContinue

# 重新安装
npm install
```

### 方案 4：使用本地缓存目录（项目级别）

```powershell
# 在项目目录下设置本地缓存
npm config set cache "./.npm-cache"

# 重新安装
npm install
```

## 推荐操作步骤

1. **首先尝试方案 1**（更改全局缓存目录）
2. 如果方案 1 不行，尝试**方案 2**（管理员权限）
3. 如果还是不行，尝试**方案 3**（清理缓存）

## 验证安装

安装成功后，运行以下命令验证：

```powershell
npm list pdf-parse mammoth
```

应该能看到这两个包已安装。
