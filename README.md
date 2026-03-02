# 臺灣地震 Discord Bot

一個基於交通部中央氣象局舊版 API 的 Discord 地震通知機器人。

## ⚠️ 重要說明

本專案使用的是**交通部中央氣象局舊版 API**。如您想使用此專案，**請自行修改以適應目前可用的 API 版本**。

中央氣象局已更新其 API，原有的 API 端點可能已停用或有所變更。建議查詢[中央氣象局開放資料平台](https://opendata.cwa.gov.tw/)獲取最新的 API 文檔和端點。

## 功能特色

- 🌍 實時地震報告通知
- 📊 自動抓取中央氣象局地震資料
- 🎨 美化的 Discord Embed 訊息
- 📍 詳細的震度分布信息

## 前置需求

- Python 3.8+
- Discord Bot Token
- 中央氣象局 API Token（需自行申請）

## 安裝

1. Clone 此專案

```bash
git clone https://github.com/Kevin28576/cwa-earthquake-discord-bot.git
cd cwa-earthquake-discord-bot
```

2. 建立虛擬環境（可選但建議）

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. 安裝依賴

```bash
pip install -r requirements.txt
```

4. 設置環境變數

建立 `.env` 檔案在根目錄，並填入以下內容：

```
token=YOUR_DISCORD_BOT_TOKEN
APIToken=YOUR_CWA_API_TOKEN
channels=YOUR_CHANNEL_ID_1 YOUR_CHANNEL_ID_2
```

5. 運行機器人

```bash
python main.py
```

## 配置說明

### Discord Bot 設置

1. 前往 [Discord Developer Portal](https://discord.com/developers/applications)
2. 新建應用程式並取得 Bot Token
3. 在 `Intents` 中啟用必要權限
4. 將 Bot 邀請到您的 Server

### 中央氣象局 API

需要自行修改以下部分以適應最新 API：

- API 端點 URL（目前使用已停用的舊版端點）
- 回應資料格式解析
- 地震資訊字段映射

建議參考[中央氣象局開放資料文檔](https://opendata.cwa.gov.tw/devManual/insure)進行更新。

## 專案結構

```
earthquake-discord-bot/
├── main.py           # 主程式進入點
├── earthquake.py     # 地震資料處理邏輯
├── .env             # 環境變數（需自行建立）
├── check.json       # 地震紀錄檔（自動生成）
├── requirements.txt # 依賴套件列表
└── README.md        # 此檔案
```

## 依賴套件

- `discord.py` - Discord Bot 框架
- `requests` - HTTP 請求
- `python-dotenv` - 環境變數管理

詳見 `requirements.txt`

## 已知問題

- ⚠️ 原有 API 端點已停用，需自行修改以適應新 API
- 某些地震數據字段可能需要重新映射

## 貢獻

歡迎提交 Pull Request 或 Issue！

如果您：

- 找到了 Bug
- 有改進建議
- 更新了 API 適配代碼
- 新增了功能

請直接提交 PR，感謝您的貢獻！

## 許可證

MIT License - 詳見 LICENSE 文件

## 注意事項

1. **API 使用條款**：使用中央氣象局 API 時，請遵守其使用條款和限制
2. **Bot Permissions**：確保 Bot 有足夠的權限在指定頻道發送訊息
3. **Rate Limiting**：注意 API 的請求頻率限制

## 聯絡方式

如有任何問題或建議，歡迎通過 Issue 或 PR 與我們聯繫。

---

**最後更新**：2026年3月

此為舊版 API 設置參考專案，使用前請確認 API 的可用性。
