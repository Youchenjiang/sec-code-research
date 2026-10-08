# 綜合研究報告與專題綜述索引（Research Vault Reports MOC）

本目錄收錄 **軟體安全研究庫（Code Security Research Vault）** 之跨領域專題綜述、技術全景報告與知識庫分類元數據。

> 📌 **計畫提案文件分流說明**：
> 國科會計畫申請、三年度架構設計與審查意見回覆等提案性質文件，已獨立歸檔至專門的 **[proposals/](../../proposals/)** 目錄：
> * 舊計畫封存：[proposals/archive-secverify/](../../proposals/archive-secverify/)
> * 新三年計畫：[proposals/logic-vuln-lifecycle/](../../proposals/logic-vuln-lifecycle/)

---

## 🔬 1. 專題學術綜述與技術報告（Thematic Surveys & Syntheses）

針對 Android 安全、動態測試框架、安全測試工具鏈與測試預言生成（Security Oracle）的系統化文獻綜述：

| 報告名稱 | 核心主題 | 涵蓋重點 |
| :--- | :--- | :--- |
| **[自動生成安全斷言（Security_Oracle_Generation）五合一文獻綜述大滿貫.md](./自動生成安全斷言（Security_Oracle_Generation）五合一文獻綜述大滿貫.md)** | 測試預言與安全斷言合成 | 經典語法判定（SOFIA, Athena）、LLM 斷言生成（TOGA, TOGLL, ChatAssert）、CWE 導向合成與動態 Mock 攔截（SecMutBench）。 |
| **[Android_DAST_工具極限與前沿突破分析.md](./Android_DAST_工具極限與前沿突破分析.md)** | 移動端 DAST 工具深度評測 | 分析主流 Android 動態分析工具的瓶頸、反調試防護繞過、與前沿突破技術。 |
| **[Android動態測試框架完整研究報告.md](./Android動態測試框架完整研究報告.md)** | 動態測試架構評估 | 比較 Robolectric、Headless AVD、Cuttlefish 與真實設備在動態測試中的保真度與效能平衡。 |
| **[Android安全測試完整工具清單.md](./Android安全測試完整工具清單.md)** | 工具鏈全景指南 | 整理靜態、動態、互動式（IAST）與二進位檢測工具之完整矩陣與適用情境。 |
| **[Android動態測試學術論文與研究資源.md](./Android動態測試學術論文與研究資源.md)** | 學術資源清單 | 匯整頂會（ICSE/ISSTA/Security）中關於 Android GUI 探索、微執行與動態污點分析論文。 |
| **[Android安全相關論文-非DAST.md](./Android安全相關論文-非DAST.md)** | 靜態與形式化文獻補充 | 涵蓋靜態污點追蹤、型別系統、權限模型與二進位重用攻擊之文獻精選。 |

---

## 🗂️ 2. 文獻庫分類法與元數據管理（Vault Taxonomy & Metadata）

本知識庫的結構化標籤體系、資料表與維護腳本手冊：

| 文件名稱 | 類型 | 說明 |
| :--- | :--- | :--- |
| **[TAXONOMY.md](./TAXONOMY.md)** | 分類體系規範 | 定義全庫 4 大維度與子領域的多面向分類法（Faceted Taxonomy）。 |
| **[PAPERS_METADATA_TABLE.md](./PAPERS_METADATA_TABLE.md)** | 元數據總表 | 收錄全庫論文之發表年份、頂會別、研究流派與關鍵詞對照表。 |
| **[ALL_PAPERS_APP_SETUP_GUIDE.md](./ALL_PAPERS_APP_SETUP_GUIDE.md)** | 應用設定手冊 | 知識庫可視化工具與本地 Paper App 的安裝與配置流程指南。 |
| **[genre relations review.md](./genre%20relations%20review.md)** | 流派關聯審查 | 跨領域研究流派（如 APR、Symbolic Execution、Fuzzing）的交互引用與演進關係。 |
| **[引用鏈.md](./引用鏈.md)** | 論文引用圖譜 | 記錄經典論文與現代 LLM 安全修復論文之間的引用繼承脈絡。 |
| **[論文待重抓清單.md](./論文待重抓清單.md)** | 維護清單 | 標記需補充實體 PDF 或重新提取 Raw Markdown 的待辦文獻清單。 |
