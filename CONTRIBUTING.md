# 簡約指南

感謝您有興趣為本專案貢獻！無論您是修正 Bug、提出改進建議，還是更新 API 適配代碼，我們都熱烈歡迎您的參與。

## 🤝 貢獻方式

### 報告 Bug

如果您發現了 Bug，請建立一個 Issue 並包含以下信息：

- **清楚的標題** - 簡潔描述問題
- **詳細的步驟** - 如何重現該問題
- **預期結果** - 應該發生什麼
- **實際結果** - 實際發生了什麼
- **環境信息** - Python 版本、Discord.py 版本、OS 等

### 提出功能建議

有新想法嗎？

1. 先檢查 Issues 中是否已有類似建議
2. 建立新 Issue，用 `[功能]` 標籤
3. 詳細說明您的想法和用途

### 更新 API 適配

**重要提醒**：本專案使用的是舊版 API，非常需要有人更新到新版本！

如果您要更新 API 適配：

1. Fork 本專案
2. 建立新分支：`git checkout -b api/update-to-new-version`
3. 測試您的更改
4. 提交 Pull Request，並詳細說明 API 變更

## 📝 貢獻步驟

### 1. Fork 專案

```bash
# 點擊 GitHub 上的 Fork 按鈕
```

### 2. Clone 您的 Fork

```bash
git clone https://github.com/Kevin28576/cwa-earthquake-discord-bot.git
cd earthquake-discord-bot
```

### 3. 建立功能分支

```bash
git checkout -b feature/your-feature-name
```

分支命名建議：

- `feature/` - 新功能
- `fix/` - Bug 修復
- `api/` - API 相關更新
- `docs/` - 文檔更新
- `refactor/` - 代碼重構

### 4. 進行更改

- 確保代碼符合項目風格
- 添加或更新必要的注釋
- 測試您的更改

### 5. Commit 您的更改

```bash
git add .
git commit -m "feat: 簡潔的變更說明"
```

Commit 信息建議使用 Conventional Commits 格式：

- `feat:` - 新功能
- `fix:` - 修復
- `docs:` - 文檔
- `refactor:` - 重構
- `test:` - 測試

### 6. Push 到您的 Fork

```bash
git push origin feature/your-feature-name
```

### 7. 提交 Pull Request

1. 在 GitHub 上開啟 Pull Request
2. 清楚描述您的更改
3. 連結相關的 Issue（如果有的話）
4. 等待審核

## ✅ Pull Request 檢查清單

提交 PR 前，請確保：

- [ ]  代碼已測試
- [ ]  添加了必要的注釋
- [ ]  更新了相關文檔（如適用）
- [ ]  沒有違反 `.gitignore` 規則
- [ ]  Commit 信息清楚明確
- [ ]  沒有發生合併衝突

## 📋 代碼風格

### Python 代碼

- 遵循 PEP 8 規範
- 使用有意義的變數名
- 添加函數文檔字符串
- 保持行長在 100 字元以內（如可能）

### 注釋

```python
# 好的注釋示例
def get_earthquake_data(api_token):
    """
    從中央氣象局 API 獲取最新地震數據。
  
    Args:
        api_token: CWB API 的授權令牌
      
    Returns:
        dict: 包含地震信息的字典
    """
    pass
```

## 🔍 測試

在提交 PR 前：

1. 測試您的代碼改動
2. 確保不會破壞現有功能
3. 如果新增功能，建議提供測試代碼

## 📚 文檔

如果您對文檔或 README 進行了更改：

1. 確保信息準確
2. 檢查繁體中文語法
3. 保持風格一致

## 🐛 已知問題

- 原有 API 端點已停用，需要更新整個 API 層
- 某些地震數據字段可能在新 API 中有所改變

## ❓ 有疑問？

- 查看現有 Issues 和 Discussions
- 提交新 Issue 提出問題
- 檢查 README 中的說明

## 📄 許可證

通過貢獻本專案，您同意您的貢獻將遵循 MIT License。

---

**感謝您的貢獻！** 💪

讓我們一起讓這個專案變得更好！
