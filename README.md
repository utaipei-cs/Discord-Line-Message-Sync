### 如何使用Docker運行

1. 將原始碼最新的版本下載到本地
2. 遵照內文完成填寫 `config.yml`，請參考 [這裡](#關於-configyml)
3. 將 `config.yml` 移動到 `run` 資料夾底下
4. 運行 `docker-compose up -d --build`
5. 確認你已經邀請Line bot/Line Notify/Discord bot至你的伺服器及聊天室
6. 在 Line 群組中，發送 `!綁定` 開始整個綁定流程，點擊機器人發送給你的 URL 並依照指示操作
7. 當你完成 Line Notify 的綁定後，你將收到一個綁定代碼，請將 `/link <binding_code>` 發送到你想要同步的 Discord 頻道
8. 完成！盡情享受 | Discord<>Line | 訊息同步服務吧！