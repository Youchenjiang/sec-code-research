# **Android 安全檢核——非 Android DAST 項目彙整（後端 API、靜態 SAST、法規治理與實體安全）**

---

**用途**：從原《Android App 滲透測試矩陣 v13.3》中抽離之非 Android 客戶端動態安全測試（DAST）範疇項目，專門用於伺服器端審計、純靜態掃描（SAST/SCA）、法規合規與實體安全檢核。
**總收錄項目**：99 項
**分類維度**：
1. **純後端 API、雲端架構與服務端安全**（69 項）：GraphQL、gRPC、RESTful、Firebase IAM、Webhook、伺服器端注入與阻斷攻擊等
2. **隱私權益、資料治理與法規合規**（18 項）：MASVS-PRIVACY 條款、個資保存與刪除期限、隱私聲明一致性等
3. **純靜態原始碼審計、SCA 與建置配置**（9 項）：硬編碼密鑰、ProGuard 保留規則、minSdkVersion、SBOM 與 CI/CD 密鑰等
4. **物理安全與社會工程**（3 項）：肩窺防護、實體設備遺失與假冒客服等

## **📌 矩陣圖例說明 (Legend)**

---

| 標籤 | 屬性定義 | 實務處理建議 |
| :---- | :---- | :---- |
| **🔴 漏洞** | **可被攻擊者直接利用的安全漏洞** (Exploitable Vulnerability) | **必須修補**：直接導致資料外洩、越權、金流篡改或提權 |
| **🟡 加固** | **縱深防禦與防逆向機制缺失** (Defense-in-Depth / Resilience) | **建議防護**：不直接致危，但大幅降低逆向與破解門檻 |
| **🔵 相容** | **系統規範、相容性與崩潰缺陷** (OS Compliance / Stability / Crash) | **品質修復**：非惡意提權，但會導致特定 Android 版本閃退或功能失效 |
| **🟣 隱私／合規** | **可驗證的資料治理、透明度或法規控制缺口** (Privacy / Compliance) | **依情境修復**：確認適用法域、資料流、同意與政策義務；不預設等同可利用漏洞 |

## **1、純後端 API、雲端架構與服務端安全 (Backend / Cloud / Server-Side) (69 項)**

---

| 原 # | 檢測項目名稱 | 屬性分類 | 適用版本 | OWASP / 規範對應 | 說明與利用情境 |
| :---: | :---- | :---: | :---: | :---- | :---- |
| **22** | **NoSQL 注入** | **🔴 漏洞** | **通用** | MASVS-CODE / M4 | Firestore / MongoDB 查詢條件遭運算子注入（如 $ne, $gt）繞過驗證 |
| **23** | **伺服器端請求偽造 (SSRF)** | **🔴 漏洞** | **通用** | MASVS-CODE / M4 / OWASP API7 | 後端 Functions 盲目請求客戶端傳入的 URL，導致內網或雲端 Metadata 洩漏 |
| **25** | **XML 外部實體注入 (XXE)** | **🔴 漏洞** | **通用** | MASVS-CODE / M4 | XML 解析器未禁用 DTD 與外部實體，導致伺服器本地檔案讀取或內網探測 |
| **27** | **LDAP 注入** | **🔴 漏洞** | **通用** | MASVS-CODE / M4 | LDAP 目錄查詢語句未對特殊字元轉義，導致目錄結構洩漏或鑑權繞過 |
| **28** | **模板注入 (SSTI)** | **🔴 漏洞** | **通用** | MASVS-CODE / M4 | 後端模板引擎直接渲染使用者輸入，導致遠端程式碼執行 (RCE) |
| **202** | **回應欄位過度暴露／物件屬性層級授權缺失** | **🔴 漏洞** | **通用** | OWASP API3 / CWE-200 | API 回傳呼叫者不應取得的 PII、雜湊密碼、內部旗標或其他物件屬性，僅由前端隱藏；應以明確回應 DTO 與欄位層級授權控制輸出 |
| **203** | **Mass Assignment／請求屬性層級授權缺失** | **🔴 漏洞** | **通用** | OWASP API3 / CWE-915 | 自動綁定客戶端 Payload 至內部模型，未允許清單與逐欄位授權，使攻擊者注入 is\_admin、ownerId、tenantId、balance 或狀態欄位 |
| **204** | **API 速率限制繞過與門檻配置不當** | **🔴 漏洞** | **通用** | MASVS-AUTH / M3 / OWASP API4 | 透過多 IP、修改 X-Forwarded-For、並行請求或付費端點梯度繞過速率限制（合併 \#202 與 \#213） |
| **205** | **詳細錯誤訊息與 Stack Trace 洩漏** | **🟡 加固** | **通用** | OWASP API8 / M8 / CWE-209 | 500 Internal Server Error 回傳詳細 Stack Trace、資料庫表結構與伺服器路徑 |
| **206** | **HTTP Header 技術棧精確版本洩漏** | **🟡 加固** | **通用** | OWASP API8 / CWE-200 | Server、X-Powered-By 等回應標頭暴露後端產品與精確版本，可協助漏洞比對；僅有通用框架名稱通常是低風險資訊，不應誤套 Mobile M10 |
| **207** | **瀏覽器可達 API 的 CORS 配置錯誤** | **🔴 漏洞** | **通用** | OWASP API8 / CWE-942 | 對受 Cookie 或瀏覽器憑證保護的 API 反射任意 Origin、錯誤允許 credentials，或把不可信 Origin 加入白名單，使惡意網站可讀取回應；單純 ACAO:* 不可搭配 credentials，且純原生 App 不受瀏覽器 CORS 強制機制保護 |
| **208** | **API 版本控制平行部署與未修補影子端點殘留** | **🔴 漏洞** | **通用** | OWASP API9 / M8 | 舊版本 API 端點（如 /v1/）未廢棄且存在已知漏洞，攻擊者可繞過新版防護降級調用舊端點 |
| **209** | **伺服器端祕密或未受限可計費 API Key 洩漏** | **🔴 漏洞** | **通用** | MASVS-CODE / M1 | 伺服器端 Secret、管理金鑰或可直接授權／計費且未綁定套件、簽章、來源與配額的 Key 出現在 URL、客戶端或公開日誌，攻擊者可冒用；設計上必須發布給客戶端的公開識別 Key 應檢查限制與可造成的實際影響，不能只因可在 APK 找到便定案 |
| **210** | **JWT 簽署算法混淆與金鑰混淆攻擊** | **🔴 漏洞** | **通用** | MASVS-AUTH / M3 | 接受 alg: none 演算法或將 RS256 公鑰當作 HMAC 密鑰進行簽名驗證繞過 |
| **211** | **日誌注入 (Log Injection / CRLF Injection)** | **🔴 漏洞** | **通用** | MASVS-CODE / M4 | 使用者輸入包含 \\r\\n 等換行控制字元，污染伺服器日誌或偽造日誌紀錄 |
| **212** | **伺服器端快取投毒 (Cache Poisoning)** | **🔴 漏洞** | **通用** | MASVS-NETWORK / M5 / OWASP API8 | 篡改 HTTP 請求 Header 污染 CDN/快取層，使其他用戶獲取惡意內容 |
| **213** | **HTTP 請求走私 (Request Smuggling)** | **🔴 漏洞** | **通用** | MASVS-NETWORK / M5 / OWASP API8 | 前端代理與後端伺服器對 Content-Length 與 Transfer-Encoding 解析不一致 |
| **214** | **HTTP 參數污染 (HPP \- Parameter Pollution)** | **🔴 漏洞** | **通用** | MASVS-CODE / M4 | 傳遞多個同名參數（?id=1\&id=2），繞過 WAF 或業務邏輯校驗 |
| **215** | **不安全的反序列化 (Insecure Deserialization)** | **🔴 漏洞** | **通用** | MASVS-CODE / M4 | 伺服器端反序列化不可信的 Java/Python/PHP 物件，導致遠端代碼執行 (RCE) |
| **216** | **多餘管理與除錯介面暴露 (Extraneous Functionality Exposure)** | **🔴 漏洞** | **通用** | OWASP API8 / M8 | 除錯端點（如 /debug/vars, /actuator/heapdump）或管理員 Panel 在生產環境仍可公開存取 |
| **217** | **伺服器端快取參數污染** | **🔴 漏洞** | **通用** | MASVS-NETWORK / M5 / OWASP API8 | 利用快取鍵 (Cache Key) 衝突覆寫其他合法用戶的回應資料 |
| **218** | **HTTP 方法混淆與動詞篡改 (Verb Tampering)** | **🔴 漏洞** | **通用** | MASVS-AUTH / M3 / OWASP API8 | 同一 API 路徑對 GET/POST 設有限制，但使用 HEAD/PUT 可繞過權限檢查 |
| **219** | **可達且具實際影響的第三方依賴／供應鏈弱點** | **🔴 漏洞** | **通用** | MASVS-CODE / M2 / MASWE-0044 | 打包版本落在受影響範圍，弱點程式碼確實可由 App 輸入或執行流程到達並造成可證明影響，或依賴／建置流程已遭投毒；只有套件名稱命中 CVE、但版本、配置或程式路徑不受影響時，不應直接列為已證實漏洞 |
| **220** | **GraphQL Schema／Playground／錯誤建議過度暴露** | **🟡 加固** | **通用** | OWASP API8 / CWE-200 | 生產環境不必要地公開 Introspection、GraphiQL／Playground、詳細 Resolver 錯誤或欄位拼字建議，降低攻擊者枚舉成本；Schema 可從客戶端或流量推導，故不能把關閉 Introspection 當作授權控制。GraphQL 授權與資源耗用另由 #345–#348 檢查 |
| **221** | **gRPC Reflection／Proto／服務中繼資料過度暴露** | **🟡 加固** | **通用** | OWASP API8 / CWE-200 | 不需公開探索的生產服務啟用 Reflection，或錯誤訊息、健康檢查暴露內部方法、欄位與版本，會降低枚舉成本；Reflection 本身不等同未授權。gRPC 傳輸、RPC 授權與串流控制另由 #349–#353 檢查 |
| **222** | **Webhook 來源真實性驗證缺失** | **🔴 漏洞** | **通用** | OWASP API2 / CWE-345 | 後端處理金流、帳務或通知 Webhook 時，未依供應商規格對原始請求內容驗證 MAC／數位簽章或受信任 mTLS 身分，攻擊者可偽造事件；時間窗、重放與冪等另由 #354 檢查 |
| **223** | **雲端儲存預簽名 URL 權限範圍過寬** | **🔴 漏洞** | **通用** | OWASP API1 / API3 / CWE-862 | 簽發前未逐物件／租戶授權，URL 的 Object Key、HTTP Method、期限或可用操作過寬，且在供應商／簽章格式支援時未約束必要的大小、Content-Type、校驗和或條件 Header，導致跨租戶存取、覆寫或資源濫用；需按實際雲端服務能簽入的條件驗證，不假設每種 URL 都支援相同綁定 |
| **276** | **Payload 大小與分頁限制缺失** | **🔴 漏洞** | **通用** | OWASP API4 | API 端點未設 Body 大小上限或分頁限制，攻擊者上傳超大 Payload 觸發 OOM |
| **277** | **可被低成本觸發的 CPU／記憶體／頻寬耗盡** | **🔴 漏洞** | **通用** | OWASP API4 | 攻擊者能以少量或低成本請求觸發昂貴查詢、模型推論、轉檔、匯出或高放大回應，服務又缺少逾時、併發、配額、工作佇列與取消控制，造成可重現的拒絕服務或顯著成本衝擊；單純沒有某一固定門檻但無可利用影響時不定案 |
| **278** | **付費服務成本限制缺失（SMS／語音／郵件／儲存）** | **🔴 漏洞** | **通用** | OWASP API4 / MASVS-AUTH | SMS／語音 OTP、郵件、轉檔、第三方查詢或儲存等按量計費端點未設每帳號、裝置、目的地與全域預算限制，可被大量觸發造成帳單耗盡；是否包含推播應依實際供應商計價，不預設 FCM 訊息本身按次收費 |
| **279** | **自動化濫用敏感業務流程** | **🔴 漏洞** | **通用** | OWASP API6 / API4 / MASVS-AUTH | 註冊、登入、搶購、邀請、密碼重設或內容提交可被腳本大量執行並造成可證明的帳號、安全、稀缺資源或成本影響，且缺少適當速率、行為風險、挑戰、配額與人工處置；不一律要求單一 CAPTCHA／Bot 產品 |
| **280** | **不安全消費第三方 API 回應** | **🔴 漏洞** | **通用** | OWASP API10 / CWE-20 | 後端把第三方回應視為可信內部資料，未做 TLS 身分驗證、Schema／型別／範圍驗證、重新導向與錯誤處理，並直接用於查詢、模板、金流或授權；只有供應商提供且業務需要時才驗數位簽章／Webhook MAC，其他情境採獨立業務確認與最小權限 |
| **281** | **上傳檔案宣告型別、實際格式與下游處理器不一致** | **🔴 漏洞** | **通用** | MASVS-CODE / M4 | 僅信副檔名／Content-Type，未以允許格式解析、Magic／結構驗證與安全重新命名，讓 Polyglot、HTML／SVG、腳本或畸形檔進入會 inline 呈現、解析或執行的下游流程；單純允許保存任意位元組但使用隔離下載網域且不執行，不會只因「可執行檔偽裝成圖片」自動成立高風險漏洞 |
| **282** | **壓縮炸彈 (Zip Bomb)** | **🔴 漏洞** | **通用** | MASVS-CODE / M4 | App 或後端處理 ZIP、GZIP、Tar、Office 等壓縮／容器格式時，未限制累計解壓大小、壓縮比、檔案數、巢狀層級、CPU 時間與磁碟配額，攻擊者可用小型輸入耗盡記憶體、儲存或運算資源 |
| **283** | **可達的圖片／PDF／影音解析器漏洞** | **🔴 漏洞** | **通用** | MASVS-CODE / M4 | 不可信檔案會進入實際打包且版本受影響的 ImageMagick、PDF、libjpeg、FFmpeg 或 OEM 解析路徑，並可重現記憶體破壞、檔案讀取、SSRF 或程式碼執行；只命中套件 CVE、但格式、版本、配置或呼叫路徑不可達時不直接定案 |
| **284** | **惡意檔案掃描、隔離與安全呈現機制缺失** | **🟡 加固** | **通用** | OWASP ASVS / CWE-434 | 上傳內容未先隔離，且缺少符合資料敏感度的私有惡意程式掃描、內容消毒／轉檔與安全下載策略便提供他人；機密檔案不應任意提交公有多引擎掃描服務，掃描也不能取代型別、大小與授權檢查 |
| **285** | **檔案上傳路徑遍歷與名稱注入** | **🔴 漏洞** | **通用** | MASVS-CODE / M4 | 後端把使用者檔名直接拼入儲存路徑、命令、Header 或日誌，未以伺服器產生的物件鍵、正規化後目錄邊界與安全顯示名稱隔離，攻擊者可穿越目錄、覆蓋檔案或注入下游語意；只移除字面 ../ 不足以涵蓋編碼、分隔符與平台差異 |
| **286** | **登入／MFA／金流關鍵事件未記錄** | **🟡 加固** | **通用** | OWASP ASVS / CWE-778 | 登入成功／失敗、MFA 觸發、權限變更與金流交易等關鍵事件未寫入集中式且受保護的稽核日誌，事後無法還原事件脈絡 |
| **287** | **異常偵測與告警機制缺失** | **🟡 加固** | **通用** | OWASP ASVS / CWE-778 | 短時間大量登入失敗、異常地理位置、裝置更換或高風險交易等模式未觸發告警與風險處置 |
| **288** | **稽核日誌防竄改機制缺失** | **🟡 加固** | **通用** | OWASP ASVS / CWE-223 | 稽核日誌存放於可被應用程式或一般管理者任意覆寫的路徑，且無集中收集、完整性驗證或不可變儲存，攻擊者可刪除入侵痕跡 |
| **289** | **稽核日誌存取控制與保存期限不當** | **🟡 加固** | **通用** | OWASP ASVS / CWE-532 | 過多帳號可查閱安全日誌，或日誌保存時間過短而無法調查、過長而增加個資暴露；應依事件類型實施最小權限與保存政策 |
| **290** | **日誌時間同步與事件關聯資訊缺失** | **🟡 加固** | **通用** | OWASP ASVS / CWE-778 | 多個服務的時鐘、Request ID、Session ID 與裝置事件無法關聯，導致跨系統事件排序不一致；關聯識別碼不得直接使用敏感 Token |
| **311** | **Cookie 型 API CSRF** | **🔴 漏洞** | **通用** | OWASP ASVS / CWE-352 | 敏感操作僅依賴瀏覽器或 WebView 自動攜帶的 Session Cookie，卻缺少 CSRF Token、Origin／Referer 驗證及適當的 SameSite 策略，惡意網頁可誘使已登入使用者執行未授權操作 |
| **312** | **CSRF Token 產生與驗證缺陷** | **🔴 漏洞** | **通用** | OWASP ASVS / CWE-352 | CSRF Token 可預測、固定、跨 Session 共用、未由伺服器驗證或洩漏於 URL／日誌；Token 應具足夠熵值並綁定正確的使用者 Session，是否每次操作更新則依風險設計 |
| **313** | **JWT Claims 驗證缺失** | **🔴 漏洞** | **通用** | OWASP ASVS / CWE-345 | 後端未依實際 Token Profile 驗證必要且已出現的時間、Issuer、Audience、Subject、Token Type 與其他 Claims，或接受 Profile 不允許的演算法；不是所有 JWT 都一律要求 exp／nbf／jti，但若 Profile、業務時效或防重放設計要求，缺漏或未驗證即可造成過期、跨受眾或重放 Token 被接受 |
| **314** | **JWT kid／jku／x5u 遠端金鑰注入** | **🔴 漏洞** | **通用** | OWASP ASVS / CWE-345 | 驗證端盲信 Token Header 指定的 kid、jku 或 x5u，允許路徑穿越、SQL 注入或載入攻擊者控制的 JWK／憑證，進而接受偽造 JWT |
| **315** | **Open Redirect** | **🔴 漏洞** | **通用** | OWASP ASVS / CWE-601 | 登入、密碼重設、OAuth 或 Deep Link 流程直接採用使用者控制的 redirect／continueUrl，未使用精確白名單與正規化驗證，可能將使用者與一次性憑證導向惡意網域 |
| **316** | **Host Header Injection** | **🔴 漏洞** | **通用** | OWASP ASVS / CWE-346 | 後端直接使用 Host、X-Forwarded-Host 或 Forwarded 產生密碼重設連結、快取鍵或重新導向 URL，且未由可信反向代理覆寫並以伺服器端設定驗證，導致連結被投毒 |
| **330** | **Callable／HTTP Functions 信任客戶端 UID、角色或租戶欄位** | **🔴 漏洞** | **通用** | OWASP API1 / API5 / CWE-602 | Cloud Functions／Cloud Run 從 Payload、Query 或可偽造 Header 讀取 uid、role、tenantId 並據以授權，而未使用平台已驗證的 Auth Context／JWT Claims 且未逐資源授權，攻擊者可冒用他人或管理者身分 |
| **331** | **Cloud Functions／Cloud Run 原始端點繞過 Gateway 與可信 Header 偽造** | **🔴 漏洞** | **通用** | OWASP API5 / API8 / CWE-441 | API Gateway、WAF 或反向代理後方服務仍可由公開原始 URL 直連，或後端接受客戶端自送的 X-Forwarded-*、內部角色／租戶 Header，導致路由層認證、限流與來源限制被繞過 |
| **332** | **Admin SDK／Server Client 繞過 Security Rules 後缺少後端授權** | **🔴 漏洞** | **通用** | OWASP API1 / API5 / CWE-862 | Firestore Server Client Libraries 與 Admin SDK 依 IAM／服務帳戶執行而不受行動端 Security Rules 保護；若 Function 只因客戶端規則存在便省略物件與欄位授權，任何可達後端路徑都可能跨使用者讀寫 |
| **333** | **Firestore／Realtime Database 欄位與狀態轉移規則不完整** | **🔴 漏洞** | **通用** | OWASP API3 / CWE-915 | 規則只驗證登入或 ownerId，卻未限制 create／update／delete、不可變 owner／role／balance、允許欄位、型別、狀態轉移與查詢條件；Firestore Rules 不是事後過濾器，查詢本身須能證明所有可能結果皆獲授權 |
| **334** | **Cloud Storage Rules 未限制物件路徑、操作與 Metadata** | **🔴 漏洞** | **通用** | OWASP API1 / API3 / CWE-434 | 只驗證已登入而未綁定 Object Path 與 owner／tenant，或未分離 create、overwrite、read、delete，且未限制 size、contentType、自訂 Metadata 與不可變欄位，導致跨租戶讀寫、覆蓋或惡意內容上傳 |
| **335** | **Firebase／Google Cloud 服務帳戶與 IAM 權限過度** | **🟡 加固** | **通用** | OWASP API8 / CWE-250 | Function、CI/CD 或維運服務帳戶持有 Owner、Editor 或跨專案廣域角色，缺少最小權限、工作負載身分、金鑰禁用／輪替與環境隔離；憑證或工作負載遭入侵時會把單點事件放大成全專案控制 |
| **342** | **Tenant／Organization／Project 隔離缺失** | **🔴 漏洞** | **通用** | OWASP API1 / API5 / CWE-862 | 後端只檢查資源 ID 或使用者已登入，卻未把每次查詢、快取鍵、背景工作、檔案路徑與搜尋索引綁定當前 tenant／org／project，導致跨租戶讀寫、搜尋結果或通知外洩 |
| **343** | **業務狀態機跳步與非法轉移** | **🔴 漏洞** | **通用** | OWASP ASVS / CWE-841 | 客戶端可直接呼叫「完成、退款、取消、核准、出貨」端點，跳過前置付款／審批，重複或逆向轉移狀態；後端須以允許轉移表、角色、前置條件與原子更新驗證每一步 |
| **344** | **分散式交易、帳本與補償流程不一致** | **🔴 漏洞** | **通用** | OWASP ASVS / CWE-367 | 支付、庫存、獎勵與退款跨服務更新缺少冪等鍵、唯一約束、Outbox／Saga 或對帳，逾時重試、亂序回呼與部分失敗可造成重複入帳、免費出貨或餘額漂移 |
| **345** | **GraphQL Resolver／欄位／型別授權缺失** | **🔴 漏洞** | **通用** | OWASP API1 / API3 / API5 | 只在頂層 Query 或 UI 檢查權限，攻擊者經 Nested Resolver、Node／Global ID、Alias、Mutation Input 或敏感欄位讀寫他人物件與受限屬性；授權應在業務／資料層對每個物件與欄位一致執行 |
| **346** | **GraphQL Subscription／WebSocket 認證生命週期缺陷** | **🔴 漏洞** | **通用** | OWASP API1 / API2 / CWE-613 | 只在 WebSocket 建連時驗證 Token，之後 Token 過期、撤銷或租戶／角色變更仍持續收訊；Topic／Filter 未逐事件授權，或 Cookie 型連線未驗證 Origin，造成跨站 WebSocket 劫持與跨租戶事件外洩 |
| **347** | **GraphQL Demand Control 可被 Alias、Fragment 與 Batch 繞過** | **🔴 漏洞** | **通用** | OWASP API4 / CWE-770 | 只限制 Depth，未計算 Breadth、Alias、重複 Fragment、List Pagination、Batch／Array Query 與高成本 Resolver，攻擊者以淺層高扇出查詢耗盡資料庫；應採 Cost Analysis、分頁上限、速率／併發限制與可選 Trusted Documents |
| **348** | **GraphQL Multipart Upload 的 CSRF 與內容驗證缺失** | **🔴 漏洞** | **通用** | OWASP API4 / CWE-352 / CWE-434 | 接受 multipart/form-data 上傳卻只依 Cookie 認證、未驗證 CSRF／Origin，且未限制檔案數量、大小、Map 重複引用、MIME／Magic Bytes 與未使用檔案串流，造成跨站操作、記憶體耗盡或惡意檔案進入後端 |
| **349** | **gRPC TLS／mTLS／Server Identity 或 h2c 信任配置錯誤** | **🔴 漏洞** | **通用** | OWASP API2 / CWE-295 | 行動端或服務間 gRPC 使用明文 h2c、盲信憑證、未驗 Hostname／Authority，或宣稱 mTLS 卻未驗客戶端憑證鏈與工作負載身分，導致攔截、冒用或跨環境連線 |
| **350** | **gRPC Per-RPC／Method 授權與 Metadata 信任缺失** | **🔴 漏洞** | **通用** | OWASP API1 / API5 / CWE-862 | Auth Interceptor 未覆蓋所有 Service／Method、只驗已登入不驗物件與角色，或信任客戶端傳入的 user／tenant／internal Metadata；攻擊者可直接呼叫管理 RPC 或冒用身分 |
| **351** | **長生命週期 gRPC Stream 未處理 Token 過期與撤銷** | **🔴 漏洞** | **通用** | OWASP API2 / CWE-613 | Server／Bidi Stream 只在建立時驗證，Token 過期、登出、停權或權限／租戶改變後仍可持續收發；應定義最長 Stream 壽命、週期重驗、每訊息／資源授權與安全重連策略 |
| **352** | **gRPC 資源耗盡與流量控制缺失** | **🔴 漏洞** | **通用** | OWASP API4 / CWE-770 | 未限制單訊息與 Metadata 大小、壓縮後膨脹、並行 Stream、未讀訊息佇列、Keepalive／連線數；Client 呼叫未設合理 Deadline，Server 未停止已取消工作或下游呼叫未傳播 Deadline，造成 CPU、記憶體、FD 與執行緒池耗盡。另檢查手動 Flow Control／應用佇列是否破壞預設背壓 |
| **353** | **Protobuf 語意／解析差異造成驗證繞過** | **🔴 漏洞** | **通用** | OWASP API8 / CWE-20 | Gateway、WAF、JSON Transcoding 與後端對 unknown／duplicate fields、oneof、預設值、enum、整數範圍或欄位合併語意不一致，攻擊者可讓驗證層與執行層看到不同資料；須固定解析規則並在最終語意物件上驗證 |
| **354** | **Webhook 重放、亂序與冪等處理缺失** | **🔴 漏洞** | **通用** | OWASP API2 / CWE-294 | Webhook 真實性已通過驗證，但接收端未檢查 Timestamp 容許窗、Event ID 去重、事件版本／順序與業務冪等，或金鑰輪替期間無界接受新舊祕密，使有效事件可被重放或亂序提交並造成重複入帳、狀態回滾或撤銷失效；原始 Body 的簽章驗證由 #222 檢查 |
| **355** | **上傳後檔案物件 BOLA 與 Signed URL 受眾失控** | **🔴 漏洞** | **通用** | OWASP API1 / CWE-862 | 上傳階段已限制路徑，但列舉、預覽、下載、分享、取代與刪除 API 未逐物件／租戶授權，或 Signed URL 可被不當轉交、期限過長、未綁定用途，使攻擊者存取他人檔案 |
| **356** | **使用者檔案被同源主動內容執行** | **🔴 漏洞** | **通用** | OWASP ASVS / CWE-79 / CWE-434 | SVG、HTML、XML、PDF 或 Polyglot 上傳後由主站同 Origin inline 顯示，Content-Type 可嗅探且缺少安全 Content-Disposition／獨立下載網域／CSP，導致 Stored XSS、憑證動作或惡意下載 |

## **2、純靜態原始碼審計、SCA 與建置配置 (Pure SAST / SCA / Build Config) (9 項)**

---

| 原 # | 檢測項目名稱 | 屬性分類 | 適用版本 | OWASP / 規範對應 | 說明與利用情境 |
| :---: | :---- | :---: | :---: | :---- | :---- |
| **63** | **硬編碼密鑰與 API Secret** | **🔴 漏洞** | **通用** | MASVS-CODE / M1 / MASWE-0004 | AES 加密金鑰、JWT Secret 或第三方 Private Key 直接寫死於 Java/Kotlin 程式碼 |
| **64** | **硬編碼憑證與私鑰檔案** | **🔴 漏洞** | **通用** | MASVS-CODE / M1 | 伺服器私鑰、測試帳號或管理者憑證打包於 APK assets 或 res 目錄中 |
| **78** | **ProGuard / R8 \-keep 規則過寬** | **🟡 加固** | **通用** | MASVS-RESILIENCE / M7 | 混淆規則過度保留內部工具類與反射介面，逆向後可直接調用底層私有邏輯 |
| **297** | **SBOM (Software Bill of Materials) 缺失** | **🟡 加固** | **通用** | MASVS-CODE / M2 | App 未維護完整的第三方套件/SDK 版本清單，已知漏洞套件無法被及時發現與替換 |
| **298** | **依賴來源、完整性與投毒防護不足** | **🟡 加固** | **通用** | MASVS-CODE / M2 | 建置未鎖定版本與受信 Repository、未啟用可用的 checksum／簽章／dependency verification、來源允許清單與異常審查，增加 Dependency Confusion 或遭竄改套件進入 Release 的機率；若已證明惡意依賴實際打包執行，應另升級為紅色供應鏈事件 |
| **299** | **CI/CD Secret 洩漏** | **🔴 漏洞** | **通用** | MASVS-CODE / M2 | 建構流程中的 API Key、Keystore 密碼或 Service Account 洩漏至公開 CI log |
| **300** | **可重現建置與發布產物可驗證性不足** | **🟡 加固** | **通用** | MASVS-CODE / M2 / MASWE-0075 | 固定原始碼、依賴、工具鏈與建置參數後，仍無法產生可比對的未簽署／已簽署產物，或無法說明簽章、時間戳、ZIP Metadata 等預期差異，使審查者難以確認商店版本來自已審核原始碼；應定義可重現邊界與差異證據，不籠統要求所有發行管道逐位元完全相同 |
| **319** | **minSdkVersion 過舊導致平台防護缺失** | **🟡 加固** | **通用** | MASVS-CODE / MASWE-0041 | 即使 targetSdkVersion 很新，過低的 minSdkVersion 仍允許 App 執行於已停止安全更新、缺少現代權限與平台防護的舊系統；最低版本應依資料敏感度與裝置風險評估設定 |
| **320** | **已棄用 Keystore／非標準安全 API 使用** | **🟡 加固** | **通用** | MASVS-CODE / MASWE-0046 / MASWE-0047 | 安全關鍵功能使用已棄用 Android Keystore 實作／Provider、舊 API、自訂加密協定或自行管理金鑰，容易遺漏驗證與生命週期控制；應先確認目標版本與供應商棄用狀態，再遷移至平台 JCA／Android Keystore 與持續維護、適合需求的標準函式庫 |

## **3、物理安全與社會工程 (Physical & Social Engineering) (3 項)**

---

| 原 # | 檢測項目名稱 | 屬性分類 | 適用版本 | OWASP / 規範對應 | 說明與利用情境 |
| :---: | :---- | :---: | :---: | :---- | :---- |
| **239** | **BiometricPrompt 回呼可被 Hook 的韌性驗證** | **🟡 加固** | **通用** | MASVS-AUTH / M3 | 以 Hook 偽造 onAuthenticationSucceeded() 是測試客戶端信任邊界的方法；若 App 只信回呼布林值，可能解鎖本地 UI，但綁定 CryptoObject 的 Keystore 操作不會因此自動取得可用密碼原語。須證明敏感資料或後端操作確實可完成，否則僅列韌性觀察；架構缺陷另由 #142 檢查 |
| **240** | **敏感 UI 明文顯示與旁路觀看（Shoulder Surfing）** | **🟡 加固** | **通用** | MASVS-PRIVACY / MASWE-0036 | 密碼、PIN、OTP、卡號、復原碼或健康／金融資料未適度遮罩，或按鍵動畫與最近任務預覽暴露輸入；須同時考慮可用性、無障礙與使用者主動顯示需求，而非一律永久遮蔽 |
| **241** | **偽造 QR Code / Deep Link 導向釣魚** | **🔴 漏洞** | **通用** | MASVS-PLATFORM / M3 | 掃描 QR Code 或解析 Deep Link 時未過濾目標網域，自動跳轉至釣魚頁面 |

## **4、隱私權益、資料治理與法規合規 (Privacy Governance & Legal Compliance) (18 項)**

---

| 原 # | 檢測項目名稱 | 屬性分類 | 適用版本 | OWASP / 規範對應 | 說明與利用情境 |
| :---: | :---- | :---: | :---: | :---- | :---- |
| **242** | **危險／特殊權限最小化原則違反** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY / MASWE-0066 | App 聲明或實際使用的危險／特殊權限超出核心功能與已告知目的；若過度權限另形成可利用越權路徑，應再獨立列為紅色漏洞 |
| **243** | **隱私相關動作的範圍、對象與後果未即時說明** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY / MASWE-0070 | 分享、匯出、發布、同步、備份、改變可見性或回應第三方資料請求前，介面未清楚顯示資料範圍、Metadata、目的地、接收者、公開程度與持久性，也沒有與風險相稱的預覽、確認或復原，使使用者無法理解即將形成的隱私狀態 |
| **244** | **權限拒絕／撤銷後降級處理缺失** | **🔵 相容** | **通用** | MASVS-PRIVACY | 使用者拒絕、選擇「僅這次／概略」、自動重設或在設定中撤銷權限後，App 閃退、卡在循環彈窗、沿用過期授權假設或破壞非相關功能；應提供最小可用替代流程與必要時的設定說明，不以強迫反覆請求取代尊重拒絕 |
| **245** | **背景定位超出必要目的** | **🟣 隱私／合規** | **Android 10+** | MASVS-PRIVACY | 宣告或使用 ACCESS\_BACKGROUND\_LOCATION，但核心功能不需持續背景追蹤，或實際頻率、保存與分享超出已告知用途；若位置 API 另有未授權讀取，應獨立列紅色漏洞 |
| **246** | **精確／概略位置用途未區分** | **🟣 隱私／合規** | **Android 12+** | MASVS-PRIVACY | 僅需城市或鄰近級功能卻要求 ACCESS\_FINE\_LOCATION，未尊重 approximate location 與資料最小化；同時驗證選擇概略位置後功能能否合理降級 |
| **247** | **第三方 SDK 權限聲明與實際存取未審計** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY | Manifest 合併引入非必要權限，或 SDK 在宿主已授權後存取超出預期資料；需檢查 merged manifest、SDK 初始化條件、執行期資料流與可移除的權限 |
| **248** | **隱私資料存取來源與用途追溯不足** | **🟣 隱私／合規** | **Android 11+** | MASVS-PRIVACY | 未以 Data Access Auditing、Attribution Tags 或適當伺服器稽核辨識哪段程式與第三方 SDK 存取敏感資料，導致無法驗證目的限制；稽核本身不得記錄敏感值 |
| **249** | **Privacy Policy／Data Safety 與實際行為不一致** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY / MASWE-0072 / MASWE-0073 | 政策或商店揭露聲稱不蒐集、分享某類資料，但動態流量、SDK 行為或保存實況相反；應依實際資料流與當期平台申報規則確認，不直接推定特定法規違反 |
| **250** | **資料蒐集目的未明確標示** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY | 每類資料未對應清楚、具體且可驗證的用途，介面、政策與後端資料流也無法互相對照；依適用法域確認目的限制義務 |
| **251** | **資料保存期限未設定或超出必要** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY | 對話、位置、行為與安全日誌沒有分級保存政策、到期清理或合理例外，實際留存超出業務與法定需要 |
| **252** | **適用的資料管理、刪除／匯出權利無法行使** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY / MASWE-0076 | 在適用政策或法域要求下，使用者無法提出、驗證並完成資料刪除、匯出、修改或退出特定蒐集，或只做軟刪除而未說明備份與法定保留例外；不是所有 App 在所有法域都一律有相同介面義務 |
| **253** | **撤回同意後依該同意進行的處理未停止** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY | 使用者撤回特定目的同意後，相關 SDK、排程、上傳與後續分享仍繼續；需區分以其他合法基礎或必要安全目的保留的處理 |
| **254** | **去識別化／假名化聲稱與重識別風險不符** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY / MASWE-0067 | 對外聲稱匿名化，但仍保留可連結識別碼、細粒度時間位置或可與其他資料集拼接的欄位；不是所有資料都必須匿名化，應依目的與風險選擇控制 |
| **255** | **帳號刪除後非必要資料或公開內容持續殘留** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY | 完成帳號刪除後，超出已告知備份／法定例外的關聯資料仍留存，或原應移除的內容仍可由其他使用者、公開 URL 或搜尋引擎存取 |
| **256** | **個資可見性與分享對象缺少細粒度控制** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY / MASWE-0077 | 使用者無法控制生日、Email、上線狀態、已讀回條、可被搜尋性、貼文或位置等資料對哪些其他使用者、群組或第三方可見，或設定粒度與實際分享行為不一致；另依適用目的與法域驗證揭露、退出與退出後停止分享 |
| **257** | **兒童／未成年人資料保護控制缺失** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY | 服務面向或實際知悉有兒童／未成年使用者，卻未依適用法域與商店政策實施年齡適切設計、必要的家長同意、資料最小化與廣告限制；門檻與義務須按地區確認 |
| **326** | **隱私動作預設過度揭露或同意機制不明確** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY / MASWE-0071 / MASWE-0078 | 分享、匯出、發布、同步或可見性預設勾選較廣受眾、更多資料、額外接收者或更長保存；同意介面又使用模糊／綁定文字、預先勾選、不對稱按鈕、重複干擾或難以撤回，使選擇可能不具自由、具體與知情性。須依適用政策、法域與非同意的合法處理基礎分別判定 |
| **327** | **Tracking Domain 與第三方資料接收者揭露不足** | **🟣 隱私／合規** | **通用** | MASVS-PRIVACY / MASWE-0074 | 實際流量中的追蹤網域、SDK、資料類型與接收者無法和 Privacy Policy、Data Safety 或適用平台揭露對上；應以動態資料流驗證，網域名稱本身不一定能完整代表法律角色 |

## **📊 統計分佈**

---

| 類別 | 項數 | 🔴 漏洞 | 🟡 加固 | 🔵 相容 | 🟣 隱私/合規 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **純後端 API、雲端架構與服務端安全 (Backend / Cloud / Server-Side)** | 69 | 58 | 11 | 0 | 0 |
| **純靜態原始碼審計、SCA 與建置配置 (Pure SAST / SCA / Build Config)** | 9 | 3 | 6 | 0 | 0 |
| **物理安全與社會工程 (Physical & Social Engineering)** | 3 | 1 | 2 | 0 | 0 |
| **隱私權益、資料治理與法規合規 (Privacy Governance & Legal Compliance)** | 18 | 0 | 0 | 1 | 17 |
| **總計** | **99** | **62** | **19** | **1** | **17** |
