# **Android DAST 現有工具極限與前沿學術研究突破分析 (Research Gaps & Tooling Limitations)**

---

**文檔用途**：系統性記錄《Android DAST 核心矩陣 (v14.0)》中 8 大架構域在「現有工具能力極限（表層 30%）」與「當前亟需突破之深層技術瓶頸（深層 70%）」的對照分析，並深度對標 2020–2026 年國際資安頂會（USENIX Security, ACM CCS, NDSS, IEEE S&P, ICSE, ISSTA, FSE）之最新解決方案。
**撰寫時間**：2026-08-27 | **關聯專案**：Android DevSecOps-SAFE / SecVerify / SecBrain

## **📌 核心論點：為什麼現有工具無法應付現代 Android 攻防？**

1. **工具代差與環境失效**：10 年前的開源工具（如 TaintDroid, Drozer, 傳統 Monkey）依賴 Dalvik 虛擬機與舊版架構，在現代 64-bit ART、SELinux、Scoped Storage 與 Android 14–17 環境下已完全死亡。
2. **靜態工具的「知識幻覺與誤報」**：MobSF、QARK 或常規 SAST 僅能比對字串與配置，無法理解執行期資料流、多線程競爭與商業邏輯。
3. **動態探索的「UI 盲區」**：傳統 DroidBot / Stoat 碰上 Flutter/React Native 自繪 Canvas、Jetpack Compose 虛擬節點、簡訊 OTP 與雙因素認證牆時原地卡死。
4. **底層穿透的「Hook 失效」**：現代加固模組與惡意代碼普遍採用 Direct Syscall（內聯 SVC 指令）繞過 libc，使基於 PLT/Inline 的 Frida / Objection 動態檢測工具全盲。

## **📊 8 大架構域：現有工具能力 vs. 亟需強化之深層盲區對照表**

| # | 架構分類名稱 | 現有工具能做的 (30% 表層/模板化) | ❌ 現有工具無法應付的巨大盲區 (70% 亟需強化) | 對應學術頂會研究突破點 |
| :---: | :--- | :--- | :--- | :--- |
| **一** | **傳輸與近場通訊安全**<br>*(Network & Peripheral)* | • Burp / mitmproxy 攔截 HTTPS<br>• Objection 一鍵 Hook 繞過標準憑證固定 (Pinning) | • **BLE GATT 狀態機失步與特徵值亂序重放**<br>• **自訂二進位私有通訊協議逆向**<br>• **QUIC / gRPC Protobuf 語意混淆**<br>• **偽造 Beacon 廣播與 Rogue 週邊劫持** | #71 AsiaCCS 2022 (BLE Vulns)<br>#17 Sensors 2024 (Companion IoT) |
| **二** | **四大組件與 IPC 通訊**<br>*(Components & IPC)* | • 靜態掃描 Manifest exported=true<br>• db am/pm 發送基本型別字串 Intent | • **跨多 SDK 嵌套呼叫鏈的 PendingIntent 來源混淆 (Provenance Confusion)**<br>• **複雜 Parcelable 跨版本序列化長度差異**<br>• **跨 Binder 共享記憶體 (Ashmem/Gralloc) 並行競爭損毀**<br>• **OEM 客製 ROM 殘留私有 API 越權提權** | #23 USENIX Security 2020 (FANS)<br>#49 arXiv 2026 (PendingIntent)<br>#78 ACM CCS 2021 (Residual APIs)<br>#22 IEEE ISSRE 2017 (Chizpurfle) |
| **三** | **UI、Deep Link 與 WebView**<br>*(UI, DeepLink & WebView)* | • 檢查 setJavaScriptEnabled(true)<br>• 發送單一 Deep Link URI Scheme 測試跳轉 | • **Flutter 自繪 Canvas 與 Compose 節點深度探索**<br>• **登入牆、簡訊 OTP、人機驗證碼自動化穿透**<br>• **多步驟商業流程導航與上下文感知探索**<br>• **異常 Unicode (BiDi/RTL/零寬) 導致排版引擎崩潰與 ReDoS** | #35 ICSE 2024 (GPTDroid)<br>#36 ICSE 2024 (InputBlaster)<br>#07 arXiv 2025 (A2 Agent)<br>#38 IET 2026 (GPT-Monkey) |
| **四** | **本地儲存、記憶體與資料流**<br>*(Storage, Memory & Data)* | • db run-as 讀取沙箱明文 XML / SQLite<br>• 監聽一般 Logcat 輸出 | • **動態污點分析跨 JNI / 跨進程資料流追蹤 (進入 C/C++ 即斷鏈)**<br>• **剪貼簿時序側信道與文字長度/元數據特徵推測**<br>• **Direct Boot 首次解鎖前狀態切換資料殘留**<br>• **Heap 記憶體中金鑰生命週期動態追蹤與殘留** | #42 ACM FSE 2023 (ViaLin)<br>#63 ACM IMC 2023 (Clipboard Study)<br>#43 ACM ISSTA 2024 (Call Graph Soundness) |
| **五** | **密碼學、金鑰與生物辨識**<br>*(Crypto, Keystore & Biometrics)* | • Frida Hook Cipher.getInstance() 檢查 AES-ECB<br>• 攔截 Random 偽隨機數 | • **硬體 TEE / Keymaster 內部實作缺陷、IV 重用與協議降級**<br>• **BiometricPrompt 假解鎖防護 (驗證 CryptoObject 簽章密鑰綁定)**<br>• **密碼金鑰生成參數與時序側信道推測** | #66 USENIX Security 2022 (TrustZone)<br>#65 arXiv 2025 (KeyDroid) |
| **六** | **反逆向、執行期保護與加固**<br>*(Anti-RE & Runtime Resilience)* | • 執行通用 Frida 腳本或 Magisk 模組隱藏 Root / 偵錯狀態 | • **Direct Syscall 繞過使用者空間 Hook (Frida/Xposed 完全抓不到)**<br>• **VMP / OLLVM 控制流平坦化與動態脫殼 (Unpacking)**<br>• **純記憶體 MemFD / 匿名 mmap 動態代碼執行檢測** | #18 ACNS 2020 (DaVinci)<br>#20 USENIX Security 2018 (TIRO)<br>#58 ACM 2023 (Stealthy Framework)<br>#57 JSS 2025 (Anti-Analysis) |
| **七** | **身分認證、Session 與商業邏輯**<br>*(Auth, Session & Business Logic)* | • 幾乎「完全全盲」！現有工具無法理解 App 業務語意與計費邏輯 | • **並行多線程競態條件 (Race Condition 雙花/重複領獎)**<br>• **負數金額 / 優惠券疊加套利 / 狀態機跳步**<br>• **Google Play Billing 購買憑證 (Purchase Token) 異步重放**<br>• **長生命週期 Session 跨設備非法復活** | **需要 LLM 智慧推理代理 (SecBrain) + Headless 微執行 (SecVerify) 之核心領域** |
| **八** | **現代 Android 平台與系統相容**<br>*(Modern OS Compliance)* | • 靜態讀取 uild.gradle 的 	argetSdkVersion 數字 | • **Android 14–17 在多品牌 OEM (小米/三星/OPPO) 上的碎片化行為**<br>• **16 KB Memory Page 對齊崩潰與 ELF segment 相容性**<br>• **ARM MTE (記憶體標籤擴展) 在原生庫的動態驗證**<br>• **私密空間 (Private Space) 跨 Profile 呼叫者身分隔離** | #59 NDSS 2021 (Android Framework)<br>Android 16/17 Platform Specs (API 36/37) |

## **💡 對研究計畫（SecVerify / SecBrain）與論文撰寫之關鍵啟示**

1. **有效反駁審查意見**：當審查委員質疑「現有開源工具是否已足夠」時，本分析提供了扎實的學術論據（如 FANS、DaVinci、GPTDroid、ViaLin），證明現有工具在 **Native IPC、Direct Syscall、LLM 業務探索、硬體 TEE** 存在巨大盲區。
2. **微執行與 DAST 結合點**：計畫中所提之 Robolectric 微執行驗證，應進一步結合 **Native JNI 橋接 (JNI Stubbing)** 與 **Syscall 攔截機制**，以克服 JVM 模擬環境對底層 C/C++ 盲區的限制。
3. **自動化修復 (SecRepair) 的 Oracle 依據**：本分析定義的 8 大領域深層漏洞，為後續利用 GRPO 強化學習與 AI Agent 生成「可驗證修復補丁」提供了精確的動態驗證標準（Validation Oracles）。
