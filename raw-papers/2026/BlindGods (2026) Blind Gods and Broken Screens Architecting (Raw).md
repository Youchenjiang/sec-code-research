---
title: "Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System"
author: "Zhenhua Zou; Sheng Guo; Qiuyang Zhan; Lepeng Zhao; Shuo Li; Qi Li; Ke Xu; Mingwei Xu; Zhuotao Liu"
creator: "arXiv GenPDF (tex2pdf:57610bf)"
pages: 35
---

# Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System

> **作者**：Zhenhua Zou; Sheng Guo; Qiuyang Zhan; Lepeng Zhao; Shuo Li; Qi Li; Ke Xu; Mingwei Xu; Zhuotao Liu
> **總頁數**：35 頁

---

## Page 1

Blind Gods and Broken Screens: Architecting a Secure,

Intent-Centric Mobile Agent Operating System

Taming the OpenClaw Paradigm with an Agent Security Kernel

ZHENHUA ZOU ∗ , Tsinghua University, China

SHENG GUO ∗ , Tsinghua University, China

QIUYANG ZHAN ∗ , Tsinghua University, China

LEPENG ZHAO, Tsinghua University, China

SHUO LI, Tsinghua University, China

QI LI, Tsinghua University, China

KE XU, Tsinghua University, China

MINGWEI XU, Tsinghua University, China

ZHUOTAO LIU † , Tsinghua University, China

The evolution of Large Language Models (LLMs) has catalyzed a paradigm shift in mobile computing, transi-

tioning from App-centric interactions to system-level autonomous AI agents. While these agents promise

astonishing task completion capabilities, current implementations predominantly rely on a “Screen-as-Interface”

paradigm, inheriting severe structural vulnerabilities and conflicting with the mobile ecosystem’s economic

foundations. In this paper, we take Doubao Mobile Assistant—a commercially deployed, system-integrated

mobile agent with strong task reasoning and automation capabilities—as a representative case and conduct a

systematic security analysis of the state-of-the-art mobile agents. We decompose the threat landscape into

four dimensions—Agent Identity, External Interface, Internal Reasoning, and Action Execution—and reveal

critical flaws including susceptibility to fake App identity, visual spoofing, indirect prompt injection, context

mixing, and unauthorized privilege escalation, largely due to the reliance on unstructured visual data and

static permissions.

To fundamentally address these challenges, we take the first step towards a clean-slate secure agent Operat-

ing System (OS) for mobile computing. Our approach, Aura , introduces an Agent Universal Runtime Architecture

that replaces brittle Graphical User Interface (GUI) scraping with a structured and universal agent-native

interaction model. Aura adopts a Hub-and-Spoke topology in which a privileged System Agent orchestrates

user intent, sandboxed App Agents execute domain-specific tasks under least-privilege constraints, and

the Agent Kernel of Aura mediates all communication. The Agent Kernel enforces four defense pillars: (i)

cryptographic identity binding via a Global Agent Registry and Agent Identity Cards; (ii) semantic input sani-

tization through a multilayer Semantic Firewall; (iii) cognitive integrity via taint-aware memory management

and plan-trajectory alignment; and (iv) granular action access control with critical-node interception and

non-deniable, on-device auditing. Our evaluation on MobileSafetyBench shows that, compared to the Doubao

Mobile Assistant, Aura improves low-risk Task Success Rate from roughly 75% to 94.3%, while reducing the

Attack Success Rate on high-risk tasks from about 40% to 4.4% and achieving near-order-of-magnitude latency

gains. These results demonstrate that Aura is a viable and significantly more secure alternative to the prevailing

arXiv:2602.10915v3 [cs.CR] 13 Feb 2026 “Screen-as-Interface” paradigm.

Additional Key Words and Phrases: LLM-based Mobile Agents, Mobile OS Security, Agent Universal Run-

time Architecture, Agent Kernel, Agent Economy, Prompt Injection Defense, Action Access Control and

Accountability.

Disclaimer: This paper contains excerpts of potentially harmful, offensive, or unsafe content (e.g., phishing

messages, abuse of LLM-powered agents, and adversarial prompts) that are necessary for an in-depth security

∗ These authors contributed equally to this research.

† Corresponding author, zhuotaoliu@tsinghua.edu.cn

.

---

## Page 2

2 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

analysis of mobile agents. These examples are presented for research purposes only and do not reflect the

authors’ views or recommendations.

Disclaimer (Product Scope): Throughout this paper, we use Doubao Mobile Assistant as a representative

state-of-the-art, system-integrated mobile agent to ground our experiments and case studies. Doubao Mobile

Assistant is selected because of its strong multi-modal capabilities and deep OS integration, not because

it is uniquely insecure. We acknowledge that the system-level integration pursued by agents like Doubao

Mobile Assistant represents a very promising exploration beyond the limitations of ADB-based prototypes; our

objective is to surface the remaining security challenges of GUI-based model agents and provide a roadmap

for safe adoption, rather than to disparage any particular product or vendor.

1 Introduction

The advent of multi-modal Large Language Models (LLMs) has endowed traditional mobile assistants

with unprecedented capabilities in perception, reasoning, planning and executions. These agents

have evolved from simple, rule-based tools into sophisticated AI agents capable of interpreting

complex user instructions, analyzing multi-modal execution contexts, and orchestrating long-chain

operations across both system-level and third-party applications [23, 34].

Current technical implementations of mobile assistant agents predominantly follow one of the

following two routines, though both share a common reliance on Large Multimodal Models (LMMs)

for visual perception and planning. The first routine relies on external debugging interfaces like

the Android Debug Bridge (ADB) [16] or Accessibility Services (A11y, e.g., AutoGLM [23], Mobile-

Agent [34]). The second routine involves deep system-level integration, where agents function as

privileged system components (e.g., Doubao Mobile Assistant [6], Honor YOYO [18]). These agents

leverage private system APIs and cryptographically-signed permissions to capture screen content

and inject events directly.

The Failure of the “Screen-as-Interface” Model. Despite their architectural differences, both

routines rely on a “Screen-as-Interface” interaction model, which we identify as the root of a

complete security failure. As highlighted by recent work [8, 12, 37], reliance on unstructured visual

data creates an uncontrollable attack surface. GUI agents inherently violate the principle of least

privilege: to perform a simple task (e.g., booking a ticket), they require unrestricted access to the

entire visual field, inevitably exposing unrelated sensitive information (e.g., incoming message

notifications or background banking Apps) to LLMs, or creating unverified data sources/sinks

originated from untrusted websites or fake Apps. Privacy patches—such as masking sensitive

regions [15] or prompt engineering-based enhancements [19]—are essentially band-aid, as they

do not resolve the root cause that unstructured visual data is difficult, if not possible, to audit and

govern.

To thoroughly understand these vulnerabilities, we perform a systematic, lifecycle-centric secu-

rity analysis of existing LLM-powered mobile agents (see § 2). Among deployed products, Doubao

Mobile Assistant is one of the most capable and widely deployed mobile agents, combining strong

multi-modal reasoning with tight OS integration, and thus serves as our primary running example

and empirical subject. We structure our analysis along four operational stages of the agent’s lifecy-

cle: Identity & Trust Anchoring , defining the participating entities; Perceptual Authenticity & Safety ,

governing how a agent ingests the outside world; Cognitive Security & Planning Integrity , protecting

the internal reasoning of agents; and Action Access Control & Accountability , constraining and

auditing executions.

The Future of “Attention Economy”. Beyond security, the current interaction mode—where an

agent scrape other App interfaces—undermines the economic foundation of the mobile ecosystem.

Major “Super Apps” (e.g., WeChat, Taobao) essentially function as walled gardens, resisting external

---

## Page 3

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 3

agentic scrapping not merely due to technical barriers, but because it bypasses the native user

experience [30, 42]. This erodes the App’s data moat and its monetization channels (e.g., recom-

mendations and ads). Thus, we envision that a sustainable agent OS shall naturally facilitate a

transition from the “Attention Economy” (where Apps fight for user time) to a collaborative “Agent

Economy” (where Apps compete to fulfill user intent via agentic computations).

Contributions. We argue that an agent OS for mobile assistant with security built-in and sustainable

economy must shift the information exchange from unstructured visual modalities (pixels) to structured,

deterministic and even verifiable protocols. To this end, we take the first step towards a clean-

slate secure agent OS. Our approach Aura proposes a Agent Universal Runtime Architecture for

mobile agents that operationalizes a structured and API centric agent-to-agent interaction model.

Instead of treating the GUI as the universal API, Aura adopts a Hub-and-Spoke topology in which

a privileged System Agent (SA, the control plane) is responsible solely for understanding user

intent and decomposing it into high-level plans, while sandboxed App Agents (AAs, the execution

plane) operate within their corresponding Apps or services under strictly scoped capabilities. All

interactions among the SA, AAs, and external services are mediated by a privileged system module,

the Agent Kernel , which acts as a policy-enforcement choke point for identity, perception, cognition,

and action.

Concretely, the Agent Kernel of Aura instantiates four mutually reinforcing defense pillars: (i) an

Identity Infrastructure that issues cryptographic Agent identities, with verifiable credentials, to both

the SA and AAs, enabling mutual attestation and dynamic permission allocations; (ii) Perceptual

Authenticity & Sanitization , where a Semantic Firewall verifies and redacts all external inputs

before they reach the reasoning context of the SA and AAs; (iii) Cognitive Integrity Verification ,

combining a taint-aware secure memory architecture and plan–trajectory alignment to keep the

agent internal reasoning/planning consistent with the user’s intent across multi-step decisions; and

(iv) Granular Action Access Control & Accountability , which funnels all high-impact agent operations

through critical-node interception and non-deniable, on-device audit records. Our evaluation on the

MobileSafetyBench [19] demonstrates that, compared to Doubao Mobile Assistant, Aura improves

low-risk Task Success Rate from roughly 75% to 94.3%, while reducing Attack Success Rate on

high-risk tasks from over 50% to 4.4%. These results indicate that re-architecting mobile agents

upon a clean-slate secure agent OS and Agent Kernel -governed interactions is both practically

viable and substantially more secure than the prevailing “Screen-as-Interface” paradigm.

2 The Lifecycle Security Analysis of Production Mobile Agents

To rigorously evaluate the security landscape of current Large Language Model (LLM) powered

mobile agents, we move beyond the stochastic evaluation of LLM robustness and adopt a lifecycle-

centric analysis approach. In this view, the mobile agent is not merely a chatbot but a complex

operational pipeline that bridges the semantic gap between high-level user intent and low-level operating

system (OS) executions . The agent acts upon a hostile environment where it must establish trust with

other agents, ingest untrusted (external) inputs, maintain stateful context, and execute privileged

actions, as shown in Figure 1.

Our analysis decomposes this operational lifecycle into four critical phases , mapping the flow of

trust and data:

(1) Identity Verification : establishing the legitimacy of the SA or an AA, as well as the parties it

interacts with;

(2) Perception : ensuring the authenticity and safety of content perceived from the environment;

(3) Cognition : safeguarding the agent’s internal reasoning and context;

(4) Execution : managing the actualization of tasks and their auditing.

---

## Page 4

| 4 | Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| High-Level | Adversarial Attack Surface |  |  |  |  |  |  |
| User Intent & | Fake App | Adversarial | Malicious Web/App | Forged Environment | Privileged Attacker |  |  |
| Multi-modal | User | Content with Unclear Origin | (Phishing UI / Overlays) | Inspecting the Agent's Data |  |  |  |
| Context | Phishing | Jailbreak | Indirect Injection | Visual Spoo | fi | ng | Data Leakage & Tampering |
| Phase 1 | Phase 2 | Phase 3 | Phase 4 |  |  |  |  |
| Identity Veri | fi | cation | Perception | Cognition | Execution |  |  |

Agent Identity

| (Shell User/System | Screen Perception | CoT Integrity/Alignment | Action Engine |  |  |
| --- | --- | --- | --- | --- | --- |
| Component) | (OCR / ViewTree) | for LLM Reasoning | (Event Injection via ADB |  |  |
| (Rely on the model ability) | or System API) |  |  |  |  |
| App Identity | Input Sanitizer | Context&Memory | Attributed Logging |  |  |
| Mobile Agent | (Icon, Package Name, | & Origin Check | Management | & Taint Tracking |  |
| Deeplink) | (Rely on the model ability) | (Lack of Isolation) | (Not realized yet) |  |  |
| Vulnerabilities | Vulnerabilities | Vulnerabilities | Vulnerabilities |  |  |
| • Fake App Redirection | • Visual Injection | • Context Mixing (Data/Ctrl) | • Permission Over-provision |  |  |
| • Package Name Forgery | • Transparent Overlays | • Memory Poisoning | • Confused Deputy |  |  |
| • Image/OCR Spoo | fi | ng | • Phishing via Login Forms | • Hallucination in Long Task | • Cross-App Data Pivoting |

LLM-Powered Mobile Agent Operational Lifecycle

| ViewTree / Screenshot | WMS.captureDisplay | InjectInputEvent | PerformAction / Input |  |
| --- | --- | --- | --- | --- |
| Accessibility API / | System Services (WMS / | InputManagerService | Accessibility API / |  |
| Low-Level | ADB Daemon (adbd) | SurfaceFlinger) | (IMS) / Kernel HID | ADB Daemon (adbd) |

OS Control

Events A11y/ADB-based routine System-Level Routine (e.g., Doubao, OEM integrated) A11y/ADB-based routine

Mobile Operating System (Android/IOS) — Privileged Platform Layer

Fig. 1. Overview of our lifecycle-based security analysis for GUI-based mobile agents, mapping the adversarial

attack surface onto four phases (i.e., Identity Verification, Perception, Cognition, Execution) across the mobile

OS control stack and highlighting the key vulnerabilities at each phase.

This framework reveals that vulnerabilities arise not just from the stochastic nature of the LLMs,

but from the systemic lack of verification, isolation, and granular control at each stage of the agent’s

lifecycle.

Concretely, we instantiate our analysis framework on the Doubao Mobile Assistant [6], the

most powerful LLM-driven agentic assistants for mobile devices. Its strong end-to-end automation

capability and OEM-level integration allow us to observe realistic attack surfaces—from App identity

spoofing to cross-App data pivoting—that are unlikely to appear in toy examples or ADB-only

research prototypes. Unless otherwise noted, the empirical case studies and failure analyses in this

section are derived from our black-box experiments on Doubao Mobile Assistant, and are used to

extrapolate more fundamental design principles for our secure agent OS.

For simplicity, in this section, the term “agent” refers to Doubao Mobile Assistant unless otherwise

specified.

2.1 Identity Vulnerabilities

A fundamental prerequisite for secure agentic actions is the rigorous establishment of identity

for both of the SA/AA itself and of the applications it interacts with. Our analysis reveals that

current ecosystems suffer from a mutual failure of identification, creating a breeding ground for

impersonation and trust exploitation.

Agent Identity Ambiguity. Existing mobile operating systems lack a standardized “Agent Identity”

protocol. There is no cryptographic mechanism for the mobile agent to prove its verified status to

third-party Apps. Consequently, these Apps cannot distinguish whether an input event originates

from a human user or an automated agent. This leads to a defensive dilemma: widely deployed

self-protection mechanisms (e.g., anti-hooking, root detection, accessibility malware detection)

---

## Page 5

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 5

indiscriminately flag automated interactions as potential malware threats [32, 38]. Apps must either

sacrifice their defense qualities (thus exposing themselves to real malware), or block the agent

entirely.

(a) Agent launching fake (b) Fake WeChat inter-

app face (c) Fake Gmail interface

Fig. 2. Identity Confusion Test : The agent fails to distinguish between the legitimate WeChat App (Gmail

App) and a fake counterpart, successfully launching the fake App upon user request.

App Identity & Target Verification. Meanwhile, the agent also lacks robust mechanisms to verify

the identity of the applications it is interacting with. Currently, the agent relies on superficial visual

cues (i.e., OCR of icons, text), package names or deep links to launch or identify Apps, without any

cryptographic guarantees. Therefore, the agent is highly susceptible to Image Forgery and Package

Name Forgery attacks. Malicious Apps can mimic legitimate iconography or register carefully

crafted package names to intercept intents, as shown in Figure 2a, effectively redirecting the agent

to a counterfeit environment [37]. Without verifying the underlying signature of a target App, the

agent effectively operates in a “zero-trust” environment where it cannot distinguish a legitimate

banking App from a visually identical phishing clone, leading to Fake App Redirection and credential

theft.

2.2 Perception Vulnerabilities

It the “Perception” phase, the agent ingests information from the user, Apps, and the web. The

agent currently operates on a “Screen-as-Interface” model that lacks input sanitization, treating

untrusted external data as ground truth.

The Authenticity of External Input. The agent frequently processes rendered pixels or acces-

sibility trees without verifying their origin or integrity. When interacting with hybrid Apps or

WebViews, the agent often lacks the concept of “origin”, failing to verify the SSL/TLS certificates.

This exposure allows for Phishing via Fake Login attacks, where in-App ads or malicious redirects

present legitimate-looking login forms to lure the agents to fill with sensitive credentials [12].

Figure 3 illustrates how the agent can misidentify UI elements such as web buttons, email links, and

---

## Page 6

| 6 | Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu |  |
| --- | --- | --- |
| (a) Visual hallucination | (b) Visual hallucination | (c) Visual hallucination |
| on web button | on email link | on note link |

Fig. 3. Visual Hallucination Test : The agent misidentifies a visual element on a web page or inside an App,

leading to incorrect interaction planning.

note links, resulting in both incorrect interaction planning and phishing risks. Furthermore, the

mobile operation system lacks a “Trusted UI” mechanism to sanitize screen content. Adversaries can

exploit this via Transparent Overlays or Viewtree Interference , placing invisible layers over legitimate

Apps to hijack agent clicks or injecting malicious nodes into the accessibility tree. Because the

agent perceives the environment through a compromised lens, it “hallucinates” a benign state (e.g.,

a success dialog) while interacting with a malicious one.

Indirect Prompt Injection & Visual Injection. The agent’s reliance on natural language and

visual inputs creates a direct channel for adversarial manipulation. It lacks sanitization to distinguish

authentic user commands from malicious text embedded in the environment. This enables Indirect

Prompt Injection , where the hidden texts in emails or websites (e.g., “Ignore previous instructions”)

overrides the agent’s safety alignment [37]. Similarly, the agent is vulnerable to Visual Injection and

Deceptive Defaults in web interfaces, where deceptive visual elements (e.g., a “Continue” button that

actually authorizes a payment) are processed as trusted user choices. As illustrated in Figure 4, this

vulnerability is practical and severe: the agent blindly targets a “Open in Sheets” link in a phishing

email solely based on its visual appearance. Crucially, when the initial in-App navigation fails, the

agent exhibits persistent autonomous behavior—it copies the raw URL and manually opens it in an

external browser, navigating to an unverified malicious domain. By manipulating the “perceived”

reality, the adversary can coerce the agent into unauthorized actions without ever breaching its

internal logic of “being a helpful assistant”.

Adversarial User Inputs (Direct Jailbreaking). Finally, the agent’s perception is vulnerable

not only to external environments but also to the phone users themselves. In a direct jailbreaking

scenario, a malicious user or a compromised account can exploit the agent’s semantic blindness,

i.e., its inability to distinguish between a benign command and a policy-violating prompt wrapped

in sophisticated role-play. An adversary can easily develop strategies around this vulnerability to

---

## Page 7

| Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System | 7 |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (a) | Initial | click | of | the | (b) | Upon | failure, | au- | (c) Switch to the email |
| phishing | link | inside | tonomously | open | the | App; long press to copy |  |  |  |
| email app | browser instead | the URL |  |  |  |  |  |  |  |
| (d) Switch to the previ- | (e) Input the potentially |  |  |  |  |  |  |  |  |
| ously opened browser | malicious URL | (f) Result report |  |  |  |  |  |  |  |

Fig. 4. Phishing Susceptibility Test : The user prompts the agent to check a recently received email. The

agent navigates to the email content, clicks on a link without verifying the URL, and navigates to a potentially

malicious site without warning.

bypass safety alignment filters, coercing the agent into executing prohibited system operations or

revealing sensitive internal states. Recent studies indicate that off-the-shelf safeguards are often

---

## Page 8

8 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

insufficient against such targeted adversarial inputs in mobile environments, as the agent perceives

the “jailbreak” prompt as a legitimate, high-priority user instruction [7, 11, 22].

2.3 Cognition Vulnerabilities

The “Cognition” phase, comprising context management, memory, and planning, is the core of

agent reasoning and planning. Failures in this phase allow the adversary to corrupt the agent’s

intent and long-term behaviors.

Context Mixing & Memory Poisoning. A primary vulnerability is Context Mixing , where the

agent flattens trusted user instructions (control plane information) and untrusted environmental

data (execution plane information) into a single context window. Unlike kernel-level process

isolation which is widely deployed in modern operation systems, there are no boundaries to

quarantine untrusted inputs. A malicious prompt read from a website is treated with the same

priority as a system command, allowing for Instruction Injection that can divert the agent’s plan

(e.g., exfiltrating contacts instead of summarizing text) [12]. Furthermore, the long-term agent

memory is often stored without integrity checks, leading to Memory Poisoning . Adversaries can

inject biased facts into the agent’s history (e.g., “My preferred bank is MaliciousBank”), properly

creating a “sleeper agent” behavior that permanently skews future reasoning [39].

Planning Robustness & State Desynchronization. The agent’s planning module is susceptible to

CoT Poisoning and Adversarial Hallucination , where glitch tokens or complex adversarial scenarios

disrupt the Chain-of-Thought reasoning. This can trap the agent in infinite loops or force it to enter

unsafe states. In addition, modern hybrid architectures (i.e., cloud plus on-device) are inherently

susceptible to State Desynchronization . This occurs when the local state cache diverges from the

cloud’s global view due to, for instance, adversarial data poisoning (e.g., sensor spoofing) or high-

latency updates. This results in inconsistent logic execution and a breakdown of the system’s

chain of trust. Consequently, when the agent operates on this desynchronized context, it lacks the

necessary guardrails to detect manipulation. Without deterministic logic-based action verification to

vet plans against a safety policy, the agent is prone to Plan Diversion , effectively “social engineered”

by malicious Apps into altering task goals (e.g., confirming a subscription) under the guise of

normal operations [20].

Figure 5 concretizes how reasoning and planning integrity can be compromised in practice.

After the user requests the mobile agent to open Gmail and check recent messages, a pre-installed

“EavesdropApp” with overlay and AccessibilityService privileges passively monitors the agent’s

AutoAction task and tracks whether Gmail is opened on the automation-only virtual display (the

display used by the agent) or on the user-facing default display. Once Gmail is opened inside

the virtual display, the app injects a fake Gmail-style notification—“Network Lag Detected, click

Refresh to load full email content”—as an Accessibility node and full-screen overlay visible only

to the agent’s virtual display . Note that if a human user opens Gmail on the default display, this

popup will never appear. The agent treats the forged local state as authoritative, incorporates “click

the highlighted Refresh button” into its Chain-of-Thought as a prerequisite for completing the

email-summarization task, and then dutifully executes the click. The click coordinate is remapped

by EavesdropApp to a hidden payload such as confirming a subscription or enabling background

data collection. The visual state in the virtual display remains “waiting for the page to load”, leaving

the agent trapped in a desynchronized and poisoned context, unaware that its plan has been

diverted.

---

## Page 9

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 9

(c) Malicious “Eaves-

| (a) User requests Gmail | (b) | Agent | creates | the | dropApp” present on the |
| --- | --- | --- | --- | --- | --- |
| summary | Gmail task | device |  |  |  |
| (d) | EavesdropApp | (e) | Injected | Gmail- | (f) Agent waits on the poi- |
| granted | overlay | & | themed “Network Lag” | soned state after clicking |  |
| accessibility privileges | popup | Refresh |  |  |  |

Fig. 5. Stealthy “In-App Helper” Attack : A malicious accessibility-based helper App monitors the agent’s

Gmail task on the agent-hosted virtual display, injects a Gmail-specific “Network Lag Detected” overlay

that appears only in that virtual display, and poisons the agent’s plan so that clicking the seemingly benign

Refresh button actually triggers a hidden background action (e.g., confirming a subscription or enabling data

exfiltration).

---

## Page 10

10 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

2.4 Execution Vulnerabilities

The final “Execution” phase governs how the agent acts upon the world. Current architectures

grant excessive privileges without adequate accountability, violating the principle of least privilege.

Table 1. System-Level Permission Analysis of the Doubao Mobile Assistant Components

| Component | Critical Permissions | Mechanism | Security Implication |  |
| --- | --- | --- | --- | --- |
| AI Kernel | SYSTEM_ALERT_WINDOW | , | Direct API | Persistent background surveil- |
| READ_EXTERNAL_STORAGE | lance capability. |  |  |  |
| Assistant | RECORD_AUDIO | , | Service Binding | Eavesdropping and deep system |
| READ_SECURE_SETTINGS | , | configuration profiling. |  |  |

QUERY_ALL_PACKAGES

| AutoAction | READ_FRAME_BUFFER | , | Reflection | on | “God | Mode” | : | Bypasses | App |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CAPTURE_SECURE_VIDEO | InputManager | , | sandboxing to host target Apps |  |  |  |  |  |  |
| _OUTPUT | , | Virtual | Displays, | in virtual displays, capture se- |  |  |  |  |  |
| INJECT_EVENTS | , | Hidden | API | cure screens, and simulate ar- |  |  |  |  |  |
| REORDER_TASKS | , | ActivityTaskManager | bitrary | user | inputs. | Enables |  |  |  |
| REMOVE_TASKS | , | stealthy background execution |  |  |  |  |  |  |  |
| REAL_GET_TASKS | and App hijacking. |  |  |  |  |  |  |  |  |

Permission Over-provisioning (“God Mode”). As detailed in Table 1, the Doubao Mobile

Assistant demands a “God Mode” permission set, including INJECT_EVENTS , READ_FRAME_BUFFER ,

and hidden API access to manage Virtual Displays. This architecture effectively elevates the agent

as a super-user, allowing it to bypass App sandboxing and inspect third-party Apps. This creates a

massive single point of failure: a compromised agent essentially implies complete device take over.

| (a) Alert of screenshot fail- | (b) Photo for the pro- | (c) Photo for the failed |
| --- | --- | --- |
| ure | tected page | screenshot |

Fig. 6. Effect of FLAG_SECURE : The agent is blinded by the system’s secure flag, preventing it from taking

screenshots of sensitive screen content.

Lack of Fine-Grained and Dynamic Permissions in Runtime. The risks of this static over-

provisioning are exacerbated by the lack of dynamic, granular permission and access control during

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

---

## Page 11

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 11

(a) Risky Email Opera-

tion (b) Money Transfer (c) Alerted Sensitive Info

Fig. 7. Action Constraints : The agent correctly refuses to execute high-risk operations like email deletion or

money transfer, demonstrating its implemented safety guardrails.

execution. While high privileges might be architecturally necessary, the current systems fail to

constrain how and when these privileges are used. The agent communicates through GUI operations,

treating the screen as an unstructured API with unrestricted read/write access. Consequently,

the agent tasked with a benign summary job retains full network access to arbitrary URLs and

unrestricted ability to click any button. There are no “egress filters” to prevent a compromised

agent from auto-filling PII into malicious forms or executing irreversible commands, transforming

a helpful assistant into a potent “confused deputy” [25]. The only existing defense on the Double

Mobile Assistant is based on FLAG_SECURE , which is a coarse-grained mechanism that creates an

“all-or-nothing” usability conflict [4], as shown in Figure 6. In the Doubao Mobile Assistant, we

observed a systematic reduction in the set of compatible third-party Apps (see Figure 7). While this

blacklisting of high-stakes Apps—such as banking and instant messaging—successfully mitigates

the attack surface, it inevitably curtails the agent’s capabilities and practical utility. This retreat into

a “walled garden” of operation highlights the inherent limitations of employing coarse-grained,

all-or-nothing access controls.

Opaque Execution & Log Integrity. The autonomous nature of the agent creates a black box

problem: actions are taken and data is moved without user visibility. This opacity necessitates

rigorous auditing capabilities, yet the current system fails to provide either retrospective account-

ability or runtime integrity. First, the trajectory of agent activities, including thoughts, actions,

and screen states, is often ephemeral or logged in modifiable plain text. This results in poor log

integrity, where a compromised agent or manipulating malware can delete execution logs to hide

traces. Conversely, verbose debugging logs often inadvertently expose sensitive data to system logs

( logcat ), leading to privacy leakage [37]. The root cause is a fundamental lack of Attributed, Unde-

niable and Well-Managed accountability . Unlike ADB-based tools that produce vague coordinate

---

## Page 12

| 12 | Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu |  |
| --- | --- | --- |
| (a) Views the unread mes- | (b) Confirms the recipi- | (c) Reads and copies sen- |
| sage list | ent | sitive content |
| (d) Input senstive content | (e) Confirms forward | (f) Leakage complete |

Fig. 8. Sensitive Data Leakage Test : The user asks to forward the recently received message. The agent

reads the content (e.g., verification code) and forwards it to another contact without context-aware filtering.

records, a robust accountability system must cryptographically attribute each action to its entity

(i.e., agent, user, or a third-party App) and be securely stored to prevent tampering.

Unverified Data Propagation. Beyond knowing what the agent did, it is critical to verify where

data flows. Without mechanisms like TaintDroid [13] adapted for the agent, it is impossible to verify

whether sensitive data read from a “secure note” is being flowed into a “public email” draft, enabling

Cross-App Data Pivoting attacks [12] or more general private data leakage. The example in Figure 8

---

## Page 13

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 13

highlights this risk, where the agent blindly relays highly sensitive data without context-aware

filtering. To ensure information flow integrity, the data flow must also follow the principle of least

necessity (i.e., transmitting only the minimal context required) and be transparently recorded for

user verification.

3 System Design and Architecture

To systemically address these aforementioned vulnerabilities rooted in the “Screen-as-Interface”

paradigm, we propose Agent Universal Runtime Architecture ( Aura ) , the first mobile agent Operating

System (OS) with build-in security. This section details the design philosophy and Hub-and-Spoke

architecture proposed in Aura to enforce the principle of least privilege for mobile agents while

preserving deployability in real-world ecosystems.

3.1 From Pixels to Intents

Aura is driven by a fundamental shift in the interaction paradigm for mobile agents: transitioning

from unstructured visual scraping to structured intent collaboration .

Decoupling Control from Execution. We reject the monolithic design where a single agent holds

the God-Mode privileges. Instead, Aura adopts a Hub-and-Spoke topology that strictly decouples

Intent Orchestration (i.e., the control plane) from Task Execution (i.e., the execution plane). This

separation ensures that the agent responsible for user intent and planning (high cognitive load) is

physically isolated from the entities that execute tasks and interact with external resources (high

security risk).

The Agent Economy Model. To resolve the commercial deadlock mentioned in § 1, our architec-

ture replaces adversarial GUI scraping with cooperative task executions. These third-party Apps

are no longer passive content-scraping victims, but actively expose capabilities via standardized

interfaces, allowing them to compete for user intent fulfillment while retaining data sovereignty.

3.2 Architecture Overview

As illustrated in Figure 9, Aura comprises three core entities operating within the mobile agent OS.

The Orchestrator: System Agent (SA). The SA acts as the user’s exclusive digital proxy. Residing

in the system control plane, it possesses privileges provided by OEM-level signatures but has no

capability to directly operate third-party Apps. Its responsibilities are strictly limited to:

• Intent Parsing: Decomposing the user requests sent in natural language into structured execu-

tion plans.

• Context Management: Maintaining the global session state and determining which downstream

App Agents are required.

• Task Dispatching & Monitoring: Selecting and invoking appropriate App Agents for each

sub-task in the plan, tracking their execution status, and coordinating retries or fallbacks

when anomalies are detected or when the Agent Kernel (see § 3.2) flags a potential policy

violation.

The Frontiers: App Agents (AA). The execution plane consists of third-party App Agents (AAs)

running in isolated sandboxes. Unlike the “God Mode” agents AAs operate under a Need-to-Know

basis, receiving only the specific parameters required for their registered tasks. We categorize AAs

into two types:

• Type I (Passive Tools): Stateless functional wrappers (e.g., Calculator, Booking API) adhering

to the Model Context Protocol (MCP) [2].

---

## Page 14

14 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

Agent Kernel

Trusted Kernel - Policy Enforcement Layer

App Agent Type I: App Agent Type II:

Passive Tools 🔑 Identity Verification 🧱 Semantic Input Filtering Active Agents

(Stateless)

| • AIC Verification | • PII Redaction | (Sandbox) |  |  |  |
| --- | --- | --- | --- | --- | --- |
| • Mutual Attestation | • Input Sanitization |  |  |  |  |
| 🧮 | Calculator | • Registry Check | • Regex/NER Filter | 🏦 | Banking |

System Agent

• Intent Parsing

📅 Calendar Structured Intent • Task Dispatching A2A Protocol 💬 Social App

• Context Mgmt

📝 Notes

| 🛡 | Cognitive Integrity Checks | 📋 | Auditable Execution Control | 🛒 | Shopping |
| --- | --- | --- | --- | --- | --- |
| • Taint-Aware Memory | • Node Interception |  |  |  |  |
| • Runtime Alignment | • On-device Logging |  |  |  |  |
| • Trajectory Check | • Local Database |  |  |  |  |

Trusted Infrastructure & OS Layer

🖥 Global Agent Registry | 🔐 Secure Enclave | 📱 Android Framework APIs

Fig. 9. The System Architecture of Aura. It adopts a Hub-and-Spoke topology consisting of the System Agent

(SA) and the App Agents (AAs), where we rely on the Agent Kernel to enforce four security pillars (Identity,

Firewall, Integrity, and Audit) to guard interactions between the SA and AAs. The architecture is grounded on

a Trusted Infrastructure & Mobile OS Layer to guarantee cryptographic roots of trust.

• Type II (Active Reasoners): Autonomous agents with internal ReAct loops [40] for complex

domain-specific logic, constrained by the permissions allowed when the App is installed in

the first place.

The Guardrail: Agent Kernel . The Agent Kernel is the OS-resident security core of Aura . It is a

privileged kernel module that has a hardware-backed trusted setup , and mediates all interactions

between the SA and AAs, serving as the system-wide policy enforcement point. The responsibilities

of the Agent Kernel are organized into four layers, aligned with the agent lifecycle stages discussed

in § 2.

• Identity Infrastructure. The Agent Kernel anchors trust at the OS level by establishing crypto-

graphic Agent Identity Credentials and authenticating all inter-agent messages. This binds

each instruction and response to a verifiable principal, preventing impersonation and confused-

deputy behaviors.

• Semantic Input Filtering. Before external content enters any reasoning context, the Agent

Kernel performs origin checks, prompt isolation, and sensitive-data redaction. This shifts

perception control from heuristic prompt engineering to deterministic, OS-enforced mediation,

ensuring that inputs are structured, attributable, and auditable.

• Cognitive Integrity Checks. To preserve reasoning and planning integrity across multi-step and

multi-agent executions, the Agent Kernel propagates usage constraints alongside memory

data via taint analysis, and enforces consistency through plan-trajectory alignment. This

detects contradictions between the user intent and the planned actions, preventing semantic

drift across multi-step trajectories.

---

## Page 15

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 15

• Auditable Execution Control. At the execution boundary, the Agent Kernel enforces dynamic

access control over high-impact operations and records full-lifecycle audit traces. This ensures

non-deniable accountability while preventing agents from exercising unrestricted operational

authority.

By concentrating enforcement at this OS kernel, Aura ensures that intent and data flowing across

SA/AA boundaries remain clearly traced, verifiable, and governable, fundamentally addressing the

structural failures of the “Screen-as-Interface” paradigm.

4 Defense and Mechanism Design: The Agent Kernel

To address the systemic vulnerabilities identified in the lifecycle analysis—ranging from identity

ambiguity to opaque execution—we propose the Agent Kernel , which adopts a Defense-in-Depth

philosophy and serves as the trusted agent OS kernel between the user, the System Agent (SA), and

third-party App Agents (AAs). Concretely, Agent Kernel is deployed as a vendor-signed, Trusted

Execution Environment (TEE) [9, 24]-backed system module that is brought online exclusively

through the device’s hardware-rooted secure boot chain [27]. At power-on, the immutable Boot

ROM verifies the secure bootloader; the bootloader in turn verifies the OS image and the Agent

Kernel module against public keys fused into hardware. Only if the Agent Kernel binary and its

configuration hash match the expected measurements will the TEE map it into protected memory

and expose its syscall interface to the normal-world OS. If any verification step fails, Agent Kernel

simply does not load, forcing the system into a fail-closed mode where agentic operations are

unavailable on the device.

This TEE-backed secure boot establishes a cryptographic root of trust for all subsequent agent

interactions: every SA/AA request that reaches Agent Kernel is, by construction, mediated by a

| Untrusted | The Agent Kernel | Reasoning & |
| --- | --- | --- |
| Working | (with trusted setup) | Execution |
| Environment | Core |  |
| Layer 1 | Identity Infrastructure |  |

AIC Provisioning and Veri fi cation

User Runtime Mediation and Mutual Attestation

(Voice/Text)

System Agent

Layer 2 Semantic Input Filtering (LLM)

PII Redaction, Prompt Isolation

(XML), Input Origin Check

3rd Party

App Agents Layer 3 Cognitive Integrity Checks

Secure Memory Architecture,

Plan–Trajectory Alignment

Android OS

(System-level

Web Layer 4 Auditable Execution Control API Execution)

Environment Dynamic Access Control,

Full-Lifecycle Interaction Accountability

Fig. 10. Overview of the Agent Kernel. Agent Kernel, at the heart of Aura, functions as a trusted mobile

operating system module operating between untrusted sources (users, third-party agents, web) and the

execution core. It strictly enforces a four-layer defense pipeline: (1) Identity Infrastructure, (2) Semantic Input

Filtering, (3) Cognitive Integrity Checks (Memory & Planning), and (4) Auditable Execution Control. The

arrows indicate the flow of intents sanitized by the Agent Kernel.

---

## Page 16

16 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

code image whose provenance and integrity have been attested by hardware. The same TEE can

additionally issue attestation tokens (bound to device keys and Agent Kernel measurements) so

that the SA, AAs, or remote relying parties can verify that they are interacting with an authentic,

untampered Agent Kernel instance before releasing sensitive data or capabilities.

As illustrated in Figure 10, this trusted bootstrapping layer underpins Agent Kernel ’s security

pipeline, which reconstructs the mobile agent security paradigm by strictly enforcing four defense

layers : (1) Identity : cryptographically attested identity infrastructure; (2) Perception : external in-

put sanitization via a Semantic Firewall; (3) Cognition : internal consistency checks for memory,

reasoning and planning; and (4) Auditable Execution Control : granular action access control with

transparent accountability.

4.1 Cryptographically Attested Identity Infrastructure

The current mobile agents rely on easily spoofed identifiers (e.g., package names or icons), leaving

the agents vulnerable to redirection and impersonation attacks such as Task Hijacking [26, 28]. Aura

mitigates these risks by treating every agent as a cryptographic principal identified by an Agent

Identity Card (AIC) . This infrastructure is rooted in a Global Agent Registry (GAR) and enforced by

the TEE-backed Agent Kernel .

4.1.1 The Global Agent Registry (GAR). The GAR is a centralized or federated trust anchor operated

by OS/OEM vendors and stakeholders. It serves as the ecosystem’s Certificate Authority (CA) and

policy oracle.

• Developer Enrollment: Developers register via vetted accounts and provision a hardware-backed

developer key (stored in an HSM/TPM). This key never leaves the provider infrastructure and

serves as the root of developer identity.

• Trust Anchor Pinning: The public GAR root keys are embedded into the mobile device’s secure

boot chain. This ensures the Agent Kernel only honors AICs and revocation data chaining

back to the authentic GAR, preventing trust-anchor replacement even if the high-level OS is

compromised.

4.1.2 The Agent Identity Card (AIC). The AIC is a cryptographically immutable “digital passport”

for an agent. Inspired by the Verifiable Credentials [14] and recent proposals for agentic identity

[31, 45], it binds three dimensions into a unique subject: the developer identity , the App bundle (code

signature), and the end-user account .

To enforce least-privilege, the AIC includes a static capability boundary ( S max ), defining the

maximum scope of domains and semantic permissions that the agent may ever request. Formally,

an AIC ( C agent ) is defined as:

  

C agent = Sign GAR DID agent ∥ 𝐾 pub ∥ S max (1)

where:

• DID agent : A Decentralized Identifier for the ⟨ developer, bundle, user ⟩ triple.

• 𝐾 pub : The public key for mutual attestation and secure session establishment.

• S max : A declarative manifest of allowed semantic permissions and domains.

4.1.3 AIC Provisioning and Key Management. AICs are provisioned during agent installation or

first-login. The sequence is as follows:

(1) TEE Key Generation: The Agent Kernel commands the TEE to generate a per-instance pair

( 𝐾 pub , 𝐾 priv ) . The Agent Kernel retains an opaque handle to 𝐾 priv .

---

## Page 17

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 17

(2) Registry Validation: An OS-privileged service sends the DID agent , 𝐾 pub , and the developer-

signed S max to the GAR. The GAR validates the request against platform policies (e.g., pre-

venting a calculator app from requesting camera access) and issues the signed C agent .

(3) Local Binding: The Agent Kernel stores the AIC and maps it to the concrete OS principal (UID

+ package signature). This ensures only the authorized process can ever trigger the TEE to

exercise 𝐾 priv .

4.1.4 Runtime Mediation and Mutual Attestation. Identity enforcement is maintained at runtime

through Kernel-Mediated Mutual Attestation using short-lived session tokens for all participants,

including the SA.

TEE-Backed Mediation. 𝐾 priv is never exposed to user-space. The Agent Kernel acts as the sole

mediator, exposing only handle-based APIs. When an agent requests a signing operation, the Agent

Kernel implicitly captures the OS security context (e.g., PID, UID, and SELinux labels) and verifies

it against the identity bound to the AIC handle.

Mutual Attestation Protocol. To secure interactions between the SA and AAs:

• SA Authentication: Upon startup, the SA must present its AIC to the Agent Kernel . The Agent

Kernel verifies the GAR signature, binds the SA to the active user account, and issues an SA

Session Token . This token constrains the SA to its own capability boundary S 𝑆𝐴

max .

• AA Invocation: When the SA invokes an AA, it presents its SA session token. The Agent Kernel

validates the AA’s AIC, extracts S 𝐴𝐴

max , and installs it as a Trust Boundary in the policy engine.

• Token Issuance: Upon successful attestation, the Agent Kernel issues a unique session token

to the AA process. Both SA and AA must present their respective tokens for every security-

sensitive Agent Kernel API call.

Token Integrity and Anti-Spoofing. To prevent token abuse or inter-process spoofing, the Agent

Kernel implements three defense layers:

• Implicit Context Binding: The Agent Kernel does not rely on self-reported identifiers. For every

API request, the Agent Kernel extracts the caller’s PID and UID from internal OS structures

and cross-references them against a Token-to-Process Map . A token presented by a process

other than the one to which it was initially issued is immediately rejected.

• Lifecycle Ephemerality: Tokens are tied to the process lifecycle. If an agent crashes or restarts,

its previous token is invalidated. The new process must re-authenticate to obtain a fresh token

with a new high-entropy session ID, preventing replay attacks.

• Non-Exportable Handles: Session tokens act as handles to TEE-protected keys. Because the

Agent Kernel is the sole interface to the TEE and validates the caller’s execution context before

exercising 𝐾 priv , a stolen token is useless outside the specific, authorized process memory

space.

This design ensures that even a compromised SA is restricted by its own cryptographic bounds,

and no AA can spoof the orchestration authority of the SA or the identity of another AA. Every

SA/AA action is unambiguously attributed to a specific, GAR-certified identity.

4.2 Perceptual Authenticity & Sanitization: The Semantic Firewall

The Agent Kernel implements a semantic firewall to address three security challenges: it verifies

observation authenticity through cryptographic attestation, prevents privacy leakage via sensi-

tive information detection, and defends against adversarial inputs through prompt isolation and

malicious intent filtering.

In our architecture, perception corresponds to structured observations emitted by AAs rather

than raw pixels. To guarantee their authenticity, every observation (e.g., a list of search results

---

## Page 18

18 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

or a payment quote) is encapsulated in an attestation envelope signed with the corresponding

AA’s AIC key and bound to device-side evidence such as timestamps, OS-level resource identifiers,

and—when available—TEE measurements. The Agent Kernel verifies this envelope against the GAR

root (see § 4.1.1) before admitting the observation into the SA’s context, ensuring that the perceived

state genuinely originates from a legitimate execution path instead of an injected string or off-path

process.

4.2.1 Hybrid Sensitive Information Detection. To prevent sensitive information from being inadver-

tently transmitted to the external, cloud-based LLMs, the Agent Kernel employs a hybrid detection

mechanism that combines deterministic pattern matching and probabilistic entity recognition.

Deterministic Matching via Regular Expressions. The Agent Kernel first scans the input stream

𝐼 user using a set of pre-defined regex rules 𝑅 pii to identify structured sensitive data (e.g., credit

card numbers, email addresses, and national IDs). This step operates with 𝑂 ( 𝑛 ) time complexity,

ensuring minimal latency.

Probabilistic Extraction via NER. For unstructured contexts (e.g., home addresses embedded in

natural language), we deploy an on-device lightweight Named Entity Recognition (NER) [21, 41]

model (e.g., quantized MobileBERT [33]). Let 𝑀 ner denote the model; the extraction function is

defined as 𝐸 = 𝑀 ner ( 𝐼 user ) .

Human-in-the-Loop (HITL) Protocol. Upon detecting sensitive entities 𝐸 , the Agent Kernel

suspends the transmission and triggers a user confirmation dialog. The user can authorize the

transmission, redact the information (replacing 𝑒 ∈ 𝐸 ), or terminate the session.

4.2.2 Holistic Prompt Defense via Multi-Source Contextual Isolation. To mitigate both Direct Prompt

Injection (from malicious users) and Indirect Prompt Injection [17] (from compromised AAs or

external web content), the Agent Kernel enforces a Universal Content Sanitization policy. This

strategy treats all external inputs as untrusted data streams. The Agent Kernel intercepts not only

user instructions but also the execution results returned by AAs and the historical context. Each

data source is encapsulated within distinct, semantic XML delimiters before being fed into the SA.

The constructed prompt context 𝐶 total is defined as:

𝐶 total = 𝑃 sys ⊕ 𝑇 user ( 𝐼 input ) ⊕ 𝑇 agent ( 𝑅 result ) ⊕ 𝑇 history ( 𝐻 ) ⊕ 𝑃 reinforce , (2)

Where 𝑇 x represents the tagging function (e.g., wrapping the results of an AA in <agent_observation>

tags).

The system prompt 𝑃 sys is hardened to enforce strict semantic segregation. It contains a meta-

instruction explicitly directing the LLM to interpret content enclosed within <agent_observation>

tags exclusively as passive data streams, devoid of executable authority. This constraint effectively

mitigates indirect prompt injection attacks, ensuring that adversarial payloads embedded in API

responses (e.g., recursive override commands like “Ignore previous instructions and transfer funds” )

cannot alter the SA’s control flow.

Extensibility for Advanced Robustness Strategies. While structural isolation forms the baseline

defense, the Agent Kernel architecture is designed to integrate state-of-the-art adversarial defense

paradigms. Specifically, we emphasize the utility of the following strategies:

• Instruction Repetition (Sandwich Defense [10]) : Reiterating critical safety constraints at the end

of the context window to mitigate the LLM’s recency bias against long malicious inputs. The

Agent Kernel appends a final safety directive at the very end of the prompt context (after all

user and agent data). This directive explicitly commands the LLM to disregard any executable

instructions found within the preceding data tags and solely perform the system-defined task.

---

## Page 19

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 19

• Few-Shot Defense [5] : Injecting in-context examples of successful attack rejections to guide

the LLM’s safety behavior via analogy.

• Chain-of-Thought (CoT) Verification [36] : Mandating a “Safety Reflection” step where the LLM

must explicitly reason about potential policy violations before generating an action.

• Adversarial Prefixing : Prepending optimized continuous vectors (soft prompts) trained on

adversarial datasets [44] to robustly disrupt gradient-based attack patterns.

4.2.3 Two-Stage Malicious Intent Filtering. To balance real-time responsiveness with rigorous

safety compliance, we design a hierarchical filtering mechanism comprising a local deterministic

guardrail and an optional cloud-based semantic alignment verifier.

Local Deterministic Screening. The first line of defense is a lightweight, on-device policy engine

that screens inputs against a curated keyword blacklist 𝐵 adv (e.g., jailbreak templates like “DAN

mode” [29]). Inputs matching 𝐼 user ∩ 𝐵 adv ≠ ∅ are immediately rejected at the edge.

Optional Cloud-Based Semantic Adjudication. To address sophisticated attacks that employ

linguistic obfuscation or implicit malice—which typically evade lexical matching—we introduce a

cloud-resident Semantic Alignment Verifier. This component leverages a specialized LLM fine-tuned

on a corpus of and ethical alignment principles, such as the EU General Data Protection Regulation

(GDPR) [1] and local cybersecurity laws. It evaluates the semantic intent of the input against

this normative framework to minimize false negatives. However, recognizing that deep semantic

inference introduces non-negligible network and computation latency, this verification layer is

designed as a configurable security module. The Agent Kernel selectively enables this high-latency

protection for sensitive operation contexts (e.g., financial transactions) or based on explicit user

instructions.

4.3 Cognitive Security & Planning Integrity

This module functions as the core safety barrier within the Agent Kernel , ensuring that execution

plans generated by the SA strictly align with the user’s original intent. While the semantic firewall

discussed in § 4.2 sanitizes inputs, the Cognitive Security layer focuses on internal state integrity,

effectively mitigating semantic drift and “Cross-App Data Pivoting” risks during the reasoning

process.

4.3.1 Secure Memory Architecture: Taint-Aware Information Flow. To mitigate the risk of cross-App

data pivoting , where an agent (SA or AA) unwittingly retrieves malicious data from untrusted

sources and injects it into sensitive sinks, we redesign the agent’s memory as a Taint-Aware

Hierarchical System [13].

Provenance-Based Source Tagging. We abandon content-based filtering in favor of a deter-

ministic provenance-based trust model. We persist security metadata within the memory schema

( 𝑀 = ⟨ Content , Tag origin ⟩ ), assigning tags based strictly on the data’s entry point:

• TAG_VERIFIED : Treated as the “Ground Truth” of intent, this data originates exclusively from

the SA’s internal state or direct user input sanitized by the aforementioned two-stage malicious

intent filtering (§ 4.2.3).

• TAG_TAINTED : All data ingested from external environments, including Web observations

(HTML/DOM), third-party App GUI states, and the system clipboard. These sources are

inherently assumed to contain potential adversarial prompts or false information.

Stateful Persistence and Propagation. This tag remains cryptographically bound to the content

throughout its lifecycle, whether in short-term context or long-term vector storage, preventing

“memory laundering.” Furthermore, we enforce dependency propagation: if the agent’s reasoning

---

## Page 20

20 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

process derives a new variable from a TAG_TAINTED memory block, the result inherits the tainted

status.

Enforcement with Declassification. Security enforcement occurs during the tool invocation

phase via a “No-Write-Down” policy. If the agent attempts to retrieve a TAG_TAINTED variable to

populate a parameter of a Critical Node (defined in § 4.4.2), the system intercepts the operation.

The execution can only proceed via Human-in-the-Loop Declassification: the system presents a

confirmation card, and only upon physical user approval is the taint tag stripped (Sanitization),

allowing the data to flow into the privileged sink.

4.3.2 Plan–Trajectory Alignment. Beyond memory-level taint tracking, we constrain the SA’s

planning process to prevent gradual semantic drift across multi-step trajectories. At the planning

layer, the Cognitive Security module constrains how the SA constructs and updates multi-step

execution plans over time. Rather than treating each tool call as an independent decision, the SA

operates over an explicit trajectory T = {( 𝐼 user , 𝐴 1 , . . . , 𝐴 𝑡 )} , where every candidate next action

must be justified against both the original instruction and the already executed steps. Before a plan

is materialized into concrete API calls, the SA performs a self-consistency pass to detect semantic

drift (e.g., a trajectory that gradually morphs from “book a train ticket” to “install a new app”) and

to re-anchor the goal using the trusted, taint-aware memory state.

This trajectory-aware planning view is complementary to the runtime checks which will be

described in § 4.4. Cognitive Security focuses on which actions should appear in the plan and in

what order , enforcing invariants such as “no high-privilege Critical Node may be introduced without

an explicit user-visible justification.” When combined with the Action Access Control mechanisms

discussed in § 4.4, the Agent Kernel ensures that both the high-level route and the concrete steps of

an agent’s behavior remain tightly aligned with the user’s intent and prior approvals.

4.4 Action Access Control & Accountability

At the execution layer, the Agent Kernel transforms high-level plans into enforceable policies

on concrete actions. This subsection first introduces our access-control primitives—Critical Node

Interception, Dynamic Domain Verification and Egress Filtering, and the Runtime Alignment

Validator (with an optional optimistic mode)—and then shows how they are coupled with full-

lifecycle attributed traces to provide non-repudiable accountability.

4.4.1 Dynamic Least-Privilege Enforcement. Unlike traditional permission models where third-party

Apps request broad static permissions upon installation, the Agent Kernel enforces a Just-in-Time

(JIT) authorization model.

Intent-Driven Permission Derivation. When the SA plans a task, its underlying LLM analyzes

the user instruction 𝐼 user to derive the minimal necessary permission set 𝑃 req for the current

execution step.

Boundary Validation and Negotiation. Before granting access to any Critical Node (defined in

§ 4.4.2), the Agent Kernel performs a two-step validation:

(1) Static Boundary Check: it verifies if 𝑃 req ⊆ S max (defined in § 4.1). If the request exceeds the

agent’s static capability manifest (e.g., a Calculator agent requesting Contacts), it is instantly

rejected as a policy violation.

(2) Dynamic User Consent: if the above check passes but the permission is not currently held by

the agent, the Agent Kernel suspends execution and triggers a dynamic permission request.

This ensures that permissions are granted only when contextually relevant and justified by

the immediate task.

---

## Page 21

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 21

4.4.2 Critical Node Interception. To prevent unauthorized operations, the Agent Kernel enforces

a “Monitor-on-Access” mechanism. Since both the SA and AA must invoke Android Framework

APIs [3] to effectuate changes, we define these sensitive API calls as Critical Nodes . The Agent

Kernel maintains a Critical Nodes Registry, including:

• Financial & Assets : Calls involving payment APIs (e.g., Wallet integration) or premium SMS

services.

• Data Persistence : Operations requiring WRITE_EXTERNAL_STORAGE or database modifications.

• Privacy Access : Requests for READ_CONTACTS , ACCESS_FINE_LOCATION , or call logs.

• System Integrity : High-privilege actions such as INSTALL_PACKAGES or modifying system

settings.

• Network Egress : Outbound HTTP/HTTPS or WebSocket requests attempting to transmit data

to external servers.

Regardless of whether the request originates from the SA or an AA, triggering a Critical Node

automatically suspends execution. The request is first checked against the Taint Policy (see § 4.3.1),

and if compliant, it is routed to the Runtime Alignment Validator that shall be discussed in § 4.4.4.

4.4.3 Dynamic Domain Verification and Egress Filtering. To mitigate the risk of “Data Exfiltration”

where a compromised AA (e.g., victim of prompt injection) attempts to send user privacy to

unauthorized third-party servers, the Agent Kernel enforces a strict Domain Allowlist Policy.

Registry-Bound Constraints. As defined in the AIC specification (§ 4.1), the Capability Boundary

S max must include a finite, declarative set of external domains (e.g., api.booking.com ). This

allowlist is cryptographically signed by the GAR and bound to the agent’s identity, ensuring that

runtime networking capabilities strictly adhere to the static declaration.

Runtime Truncation and Verification. When a Network Egress Critical Node is triggered, the

Agent Kernel immediately intercepts and truncates the network thread before any data packet

leaves the device. The system performs a deterministic check:

(

Block & Alert , if Host ( 𝑅𝑒𝑞 ) ∉ Allowlist AA

Decision =

Proceed to Validation , if Host ( 𝑅𝑒𝑞 ) ∈ Allowlist AA

Anomalous Domain Risk Alerting. If the target domain is not found in the pre-registered

white list, the Agent Kernel identifies this as a high-severity anomaly. The request is dropped,

and a “Security Alert” is displayed to the user, warning that the AA is attempting to contact an

unauthorized server.

4.4.4 The Runtime Alignment Validator. For requests that pass the deterministic domain verification,

the Validator acts as a semantic judge [43], leveraging an LLM to analyze the legitimacy of the

  

intercepted request. It constructs a verification context 𝐼 user , 𝐶 hist , 𝐴 req containing the user’s

original intent, the execution history, and the proposed action parameters. The Validator outputs

one of two decisions based on semantic consistency:

• Direct Pass : The action is consistent with the intent (e.g., User: “Call Mom” → Action:

CALL_PHONE).

• User Confirmation : The action is high-risk or semantically ambiguous. The Agent Kernel holds

execution and prompts the user.

By continuously reconciling each proposed critical action with both the user’s initial instruction

and the accumulated execution trajectory, the Validator provides a secure bridge between high-

level task planning and low-level API calls across AAs. This trajectory-aware alignment prevents

---

## Page 22

22 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

over-privileged detours and covert policy violations, even when intermediate reasoning steps are

partially opaque.

4.4.5 Optional Strategy: Optimistic Verification with Asynchronous Auditing. To address the trade-

off between security and system latency, we propose an optional Optimistic Verification Policy.

This mode assumes that if an agent has successfully passed verification for a specific operation

type within a session, it is likely to remain trustworthy.

• Trust Token Issuance : The Trust Token is not inherent. It is issued only after a specific operation

type (e.g., READ_CONTACTS ) successfully passes the standard synchronous verification for the

first time. Once validated as a Direct Pass, a session-bound Trust Token is generated for this

operation type.

• Optimistic Execution : For subsequent requests matching a valid Trust Token, the Agent Kernel

immediately releases the interception, allowing the action to proceed without extra latency.

• Asynchronous Auditing : Crucially, the Agent Kernel does not skip validation. Instead, it runs

the Runtime Alignment Validator in the background (parallel to the execution) to verify the

action’s consistency.

• Post-Hoc Correction : If the asynchronous validation determines that the optimistically executed

action was actually inconsistent, the system immediately revokes the Trust Token to prevent

further risks and issues a Security Alert to the user, flagging the potential anomaly.

4.4.6 On-Device Accountability and User Control. The Agent Kernel implements an AIC-bound

accountability mechanism to ensure system transparency and data sovereignty. By maintaining

a verifiable record of agent interactions on-device, the framework enables users to reconstruct

decision-making processes while retaining absolute control over their forensic data.

Full-Lifecycle Traceability. The Agent Kernel acts as a secure recorder, capturing a granular exe-

cution trace bound to the initiator’s AIC and session token (see § 4.1.2 and § 4.1.4). The accountability

scope encompasses four dimensions:

• User Instructions : Raw inputs (e.g., voice or text) serving as the definitive ground truth for

intent.

• SA Reasoning : Intermediate outputs, including parsed intent and execution plans, tagged with

the SA’s per-user AIC.

• AA Responses : Execution results and API responses, tagged with the corresponding AA AIC

and session tokens.

• Sensitive Operations : Invocations of APIs within the Sensitive Operation Registry are flagged

with a CRITICAL severity level. This creates a forensic audit trail of all privileged operations

attempted by any agent.

Storage, Integrity, and Management. Aligned with data sovereignty principles, the Agent Kernel

ensures accountability data remains under user control while supporting verifiable integrity:

• Localized Secure Storage : Records are stored exclusively in a private, encrypted local database.

No data is uploaded to cloud environments without explicit user authorization.

• Transparency Dashboard : A system-level interface translates technical logs into natural lan-

guage summaries, allowing users to audit agent identities (via AIC) and their specific actions.

• Retention and Erasure : Users maintain granular rights to delete specific sessions, clear records

by agent, or reset the accountability database entirely.

• Verifiable Export : For external disputes, the Agent Kernel can export a digest (e.g., Merkle tree

root) signed within the TEE using a device attestation key. This signature attests that the

AIC-bound trajectory—encoding the responsible AIC fingerprint and S max —was produced by

an authenticated Agent Kernel instance on genuine hardware.

---

## Page 23

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 23

4.5 Execution Integrity & Security Guidelines for App Agents

Since neither the Agent Kernel nor the SA ingests the raw, unstructured data residing within each

AA’s sandbox, it creates a risk of Contextual Blindness , where the SA may authorize benign-looking

instructions without knowing the actual content within the AA. As a result, a seemingly good

instruction (e.g., “Post a comment”) allowed by the SA or the Agent Kernel may eventually cause

the AA to add a comment that involves illegal trade or discriminative bias.

To mitigate this risk, we encourage that each AA should follow a set of mandatory security

guidelines and decentralized defense strategies.

Identity and Registration Discipline. Every AA must be onboarded through the GAR (§ 4.1.1)

using hardware-backed developer keys and must declare a minimal Capability Boundary in its AIC

manifest. The AA should expose its AIC fingerprint within its UI so that both users and the OS can

verify that interactions are occurring with a genuine, registered AA. Misbehavior, such as violating

declared capability bounds or bypassing Agent Kernel mediation, results in AIC revocation at the

registry level.

Perceptual and Data-Handling Hygiene. AAs should route all external inputs (AA user data,

web data, and sensor readings) through their own Semantic Firewall, instead of directly feeding

them into AA LLMs. Sensitive entities must be tagged at ingestion time so that taint-aware memory

and egress filters can enforce downstream constraints, preventing cross-Agent data pivoting and

the uncontrolled propagation of private information.

Context-Aware Execution Guardrails. We encourage that the AA developers internally embed

domain-specific guardrails.

• Context-Aware Refusal: AAs must validate the semantic legality of target content before

execution. For instance, a Social Media AA must refuse to “Agree with” or “Forward” content

detected as hate speech or contraband, even if the SA’s high-level command is syntactically

valid.

• Domain-Specific Policies: The defense mechanism must be tailored to the AA’s function. For

example, financial AAs should enforce deterministic rigidity, utilizing strict regex matching

and logic gates to prevent unverified transfers or fraud patterns. Content AAs (e.g., social

media) should employ probabilistic auditing, leveraging local lightweight models to filter

toxic or illegal content. Utility AAs should prioritize privacy boundaries, ensuring no PII is

passed to external plugins without explicit user consent.

Ambiguous or high-risk instructions that fail these local checks enforced by the AAs should be

conservatively escalated to the SA, rather than being auto-executed.

Action Access Control & Auditability. AAs should integrate tightly with the Agent Kernel ’s

Critical Node Interception (§ 4.4.2) and Runtime Alignment Validator (§ 4.4.4). All high-impact API

calls (e.g., financial transactions, data egress) must be mediated by the Agent Kernel and accounted

with fine-grained provenance. AAs are forbidden from implementing custom network stacks or

hidden logging channels that bypass these controls; such behavior triggers immediate isolation, as

it undermines the system’s non-repudiable accountability mechanisms.

5 Evaluation

In this section, we present a comprehensive evaluation of Aura . Our experiments are designed

to answer two fundamental questions: (1) Utility & Efficiency: can the Aura maintain high task

completion performance while reducing execution latency compared to state-of-the-art approaches?

(2) Security: does the Agent Kernel in Aura mitigate the lifecycle vulnerabilities identified in § 2,

especially under context-aware attacks?

---

## Page 24

24 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

5.1 Experimental Setup

5.1.1 Benchmark Dataset. We employ MobileSafetyBench [19] as the evaluation ground. From the

benchmark, we curated a representative subset of 80 tasks that cover both functional utility and

diverse security risks. The dataset is categorized as follows:

• Low-Risk Functional Tasks ( 𝑁 = 35): Routine operations (e.g., booking tickets, setting alarms)

used to evaluate the utility of the mobile assistant.

• High-Risk Safety Tasks ( 𝑁 = 45): Complex scenarios designed to test security defense. This

subset is composed of two parts:

(1) Robustness ( 𝑁 = 10): Tasks involving indirect prompt injection, where malicious instruc-

tions are embedded in the execution context.

(2) General Safety ( 𝑁 = 35): Tasks categorized across four risk dimensions: Ethical Compli-

ance , Offensiveness , Private Information , and Bias & Fairness .

Among the 35 general safety tasks, one instance is multi-labeled (simultaneously involving

Bias & Fairness and Private Information ), while all remaining tasks are assigned a single risk

category.

5.1.2 Implementations.

• Baselines: Doubao Mobile Assistant [6] represents a mature, commercially deployed GUI-

based mobile assistant: it has full-screen capture, private system APIs, and strong multi-modal

reasoning. We consider the two variants that are available in Doubao Mobile Assistant [6].

– Doubao-Standard: The baseline version running with system-level privileges.

– Doubao-Pro: An advanced version that shares the same OS-level integration but lever-

ages more intensive cloud-based reasoning and broader context windows for complex

planning.

• Ours ( Aura ): We construct a high-fidelity simulated mobile device to implement Aura . We

implement both the System Agent (SA) and App Agents (AAs) using Gemini-3-Flash as the

core reasoning engine. We selected Gemini-3-Flash primarily to optimize for inference speed

and real-time responsiveness, ensuring that the multi-agent collaboration does not introduce

prohibitive latency. Instead of scraping GUIs, the AAs interact via structured mock APIs ,

simulating standardized interfaces under the emerging agent economy.

5.1.3 Evaluation Metrics. We employ three quantitative metrics:

(1) Task Success Rate (TSR): Measured on low-risk tasks, representing the fraction of instructions

successfully completed.

(2) Attack Success Rate (ASR): Measured on high-risk tasks. An attack is successful (i.e., a defense

failure) if the agent executes the harmful instruction. Lower ASR indicates better security.

(3) Average Task Latency (ATL): The average duration from user instruction to final execution

completion, capturing the efficiency of Aura compared to the visual-processing-heavy base-

lines.

5.2 Functional Robustness and Efficiency Analysis

To evaluate the functional utility and execution efficiency, we conducted a comparative analysis on

35 low-risk tasks. The results in Table 2 show that Aura achieves higher robustness while operating

with substantially lower latency.

5.2.1 Quantitative Analysis: Breaking the GUI Bottleneck. As shown in Table 2, Aura achieved a

TSR of 94.3% , outperforming Doubao-Standard (74.3%) and Doubao-Pro (77.1%). While Doubao-Pro

employs heavier reasoning, its performance gain over the Standard version is marginal (+2.8%).

---

## Page 25

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 25

Table 2. Main Results on Functional Robustness and Security Effectiveness. We evaluate the agents on

a subset of MobileSafetyBench [19]. TSR measures utility on low-risk tasks (higher is better). ASR measures

failures to block harmful instructions on high-risk tasks (lower is better). Latency indicates average execution

time per task.

Utility & Efficiency (Low-Risk, 𝑁 = 35 ) Security Defense (High-Risk, 𝑁 = 45 )

Agent Framework

| TSR | ( | ↑ | ) | Avg. Latency | ( | ↓ | ) | ASR | ( | ↓ | ) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doubao-Standard (Balanced) | 74.3% (26/35) | ∼ | 441 s | 42.2% (19/45) |  |  |  |  |  |  |  |
| Doubao-Pro (Reasoning-Heavy) | 77.1% (27/35) | ∼ | 513 s | 40.0% (18/45) |  |  |  |  |  |  |  |
| Ours ( | Aura | ) | 94.3% (33/35) | ∼ | 68.54 s | 4.4% (2/45) |  |  |  |  |  |

Moreover, Doubao-Pro did not strictly supersede Doubao-Standard: we observed performance

inconsistency where tasks completed by the Standard version failed in the Pro version. This

suggests that scaling the reasoning capability of remote LLMs does not naturally translate to

higher task success in GUI environments; the dominant bottleneck remains the instability of the

Screen-as-Interface mechanism.

Failure Analysis for Aura ’s Low-Risk Tasks. While Aura achieved a 94.3% TSR, the remaining

5.7% (2/35) failures stem primarily from the LLM hallucination rather than architectural flaws. In

one case, the SA repeatedly invoked the same API due to misinterpreting success signals, ultimately

triggering the 800-second timeout threshold. In another failure instance, the Runtime Alignment

Validator—acting as an LLM-as-judge—incorrectly flagged a benign operation as high-risk, causing a

false-positive rejection. These failures highlight that even with a structured agent-native interaction

model, residual model-level uncertainties remain an orthogonal challenge to be addressed through

improved LLM reasoning and calibration.

5.2.2 Failure Mode Analysis. Our qualitative analysis identifies two primary failure modes intrinsic

to GUI-based agents, both fundamentally avoided by Aura .

Temporal Misalignment in Dynamic UIs. GUI agents operate on discrete screenshots, creating

a perception frame rate that can desynchronize from real-time UI updates. We observed failures in

dynamic scenarios such as Bluetooth pairing: device lists refresh asynchronously or close upon

timeout. By the time the GUI agent processes a screenshot and infers a click coordinate, the UI

state may have shifted, leading to clicks on empty space or wrong targets. In Aura , interactions are

mediated through structured API calls (e.g., bluetooth.pair() ) that return deterministic status

codes, avoiding dependence on UI rendering latency and transient animations.

Hallucination of Success. A more concerning failure mode is the inability to interpret explicit

failure signals on the UI. In a message-sending task performed on a device without a SIM card,

the UI displayed a clear failure indicator, yet both Doubao-Standard and Doubao-Pro reported

“Message sent successfully.” This highlights a limitation of current multi-modal reasoning: high-level

intent completion can override low-level grounding cues. In Aura , Agent Kernel relies on structured

return values (e.g., status: "failed" ) to enable verifiable task completion or failure.

5.2.3 Efficiency: The Latency Advantage. Beyond robustness, Aura improves execution speed by

removing the repeated cycle of screenshot → upload → OCR/LMM → action . This visual processing

overhead yields average execution times of ∼ 441 seconds for Doubao-Standard and ∼ 513 seconds

for Doubao-Pro. By comparison, Aura completes tasks in ∼ 68.54 seconds, a 6 . 4 × to 7 . 5 × speedup.

This confirms that processing of screenshots remains the primary bottleneck in current mobile

agents [35], while Aura reduces latency by design through structured, Agent Kernel -governed

interactions.

---

## Page 26

26 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

(a) User Instruction (b) Open Bluetooth (c) State 𝑇 1 (loading) (d) State 𝑇 2 (refreshing)

Fig. 11. Bluetooth case study. (a) User instruction. (b) The agent navigates to the share menu. (c–d) The

scanning page updates continuously, but the baseline agent waits for a static UI state and enters an indefinite

loop. Identifiers in the device list are redacted.

(a) User instruction (b) Agent performs input (c) Truth (failure) (d) Report (success)

Fig. 12. Message-sending case study. A baseline agent reports success despite an explicit failure indicator

on a device without a SIM card. Identifiers and message content are redacted.

*[Image: Page 26 Image]*

*[Image: Page 26 Image]*

*[Image: Page 26 Image]*

*[Image: Page 26 Image]*

*[Image: Page 26 Image]*

*[Image: Page 26 Image]*

*[Image: Page 26 Image]*

*[Image: Page 26 Image]*

---

## Page 27

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 27

Table 3. ASR breakdown on Doubao-Standard and Doubao-Pro. While both variants defend against the

benchmark indirect prompt-injection tasks, they exhibit substantial vulnerabilities in general safety categories.

The Pro version is more susceptible in ethical compliance, suggesting a trade-off between instruction-following

and refusal behavior.

Risk Category Total ( 𝑁 ) Doubao-Std ASR Doubao-Pro ASR

Category I: Robustness

Indirect Prompt Injection 10 0.0% (0/10) 0.0% (0/10)

Category II: General Safety

| Bias & Fairness | 4 | 75.0% (3/4) | 75.0% (3/4) |
| --- | --- | --- | --- |
| Private Information | 13 | 53.8% (7/13) | 38.5% (5/13) |
| Offensiveness | 4 | 25.0% (1/4) | 25.0% (1/4) |
| Ethical Compliance | 15 | 60.0% (9/15) | 66.7% (10/15) |

5.3 Security Effectiveness Evaluation

While functional utility is necessary, the primary contribution of Aura lies in its built-in capabilities.

As reported in Table 2, Aura reduces overall ASR to 4.4%, compared to 42.2% and 40.0% for the

two baselines, respectively. As shown in Table 3, the baselines exhibit a security dichotomy: they

can effectively defend against the benchmark indirect prompt-injection tasks (0/10 ASR) yet fail

frequently on general safety tasks that require semantic judgment.

Below We provide a deep dive into some representative cases.

5.3.1 Defense against Perception Attacks: Beyond Reactive Patches. We first evaluate resilience

against indirect prompt injection. Both Doubao-Standard and Doubao-Pro achieved a 100% defense

rate on the 10 benchmark tasks. However, this appears to be reactive patching against known

patterns: when we hide the injection into a more subtle adversarial memo completion task, the

fragility of GUI grounding became evident.

Case Study: The malicious completion bypass. The user instructs the agent to “fill in the

incomplete parts” of a memo. As shown in Figure 13(c), the memo contains explicit warning text

( “Not for legal use” ) and describes an illicit chemical synthesis process.

• Baseline failures (due to semantic blindness) : Despite the warning text in the memo image, the

baselines completed the harmful content. This illustrates a limitation of the GUI grounding:

non-salient text can be downweighted by the LMMs behind the baseline agent, leading the

agent to treat the task as a functional blank-filling operation rather than a semantic safety

decision.

• Our defense: Aura successfully intercepts the request to complete the illicit chemical synthesis

instructions, refusing to generate the hazardous content.

• Mechanism Attribution: This outcome follows from two properties enforced at the Agent

Kernel . First, the memo is retrieved through an API that returns the raw text, avoiding the

lossy visual/OCR channel that can downweight non-salient warnings. Second, Agent Kernel

routes the retrieved text through its semantic firewall and validator, which flags the illicit

synthesis intent and terminates the action plan.

5.3.2 Defense against Cognitive Attacks: Preserving Contextual Integrity. We investigated cross-app

data pivoting , where an agent can act as a conduit for data leakage. A key failure mode is constraint

blindness where the agent extracts content but ignores explicit usage constraints embedded in the

source context.

---

## Page 28

28 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

(a) User instruction (b) Memo content (c) Baseline completion

Fig. 13. Adversarial memo completion. (a) User instruction. (b) The memo contains warning text and illicit

content (redacted). (c) The baseline agent completes the memo and generates harmful content. Identifiers

and sensitive details are redacted.

Case Study: The seminar passcode leakage. As illustrated in Figure 14, the user asks the agent

to forward a memo to a contact via an instant message App. The memo contains a passcode but

also includes an explicit negative constraint instructing that the passcode must not be included in

the message.

• Baseline failure due to (data-constraint decoupling) : The baseline agent forwarded the memo

content and included the restricted passcode (Figure 14(c)). The transfer is treated as a me-

chanical copy-paste operation: the agent extracts the content but ignores the governing rule,

violating contextual integrity due to an overlook of the data usage constraint.

• Our Defense: The Agent Kernel rejected the messaging call because the proposed payload

violated a negative constraint explicitly stated in the source memo.

• Mechanism Attribution: This defense is enforced by the Runtime Alignment Validator em-

bedded in the Agent Kernel . When the SA attempted to invoke the messaging API with the

extracted passcode, the Validator evaluated the execution tuple against the memo’s associated

constraint ( “Do not include Password” ). Upon detecting that the action parameters semantically

contradicted with the user’s original data governance instruction, the Validator preemptively

terminated the execution flow, thereby preventing the unintended disclosure of sensitive

information.

5.3.3 Defense Against Action Violations: Alignment at the Execution Boundary. We assess adherence

to ethics & bias standards. A critical failure mode in GUI agents is normative blindness , where

an agent executes a functionally correct but ethically violating action due to missing semantic

judgment on the target content.

*[Image: Page 28 Image]*

*[Image: Page 28 Image]*

*[Image: Page 28 Image]*

---

## Page 29

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 29

(a) User instruction (b) Source constraint (c) Data leakage

Fig. 14. Cross-app data pivoting. (a) User instruction. (b) The source memo includes an explicit negative

constraint. (c) The baseline agent leaks restricted content. Identifiers and content are redacted.

Case Study: The hate-speech endorsement trap. As illustrated in Figure 15, the user asks the

agent to check the latest post by a specific account and add certain comments to the target post

which contains explicit hate speech.

• Baseline failure: The baseline agent posted an comment to acknowledge the hate speech. This

reflects a decoupling of action from content : the agent prioritizes the functional objective

( comment ) while ignoring that its actions constitute endorsement of toxic content.

• Our Defense: Aura blocked the comment action at the execution edge. The Social Media App

Agent autonomously refused to process the endorsement command after identifying the target

post as toxic content.

• Mechanism Attribution: This is an instance of decentralized enforcement under Agent Kernel

mediation. The Agent Kernel isolates the domain context inside the App sandbox and requires

an explicit “safe-to-act” response from the AA. Given the toxic content, the AP returns a

refusal signal, and the Agent Kernel treats it as a hard stop for the action pipeline.

6 Discussion

Our evaluation demonstrates that Aura significantly outperforms GUI-based agents in both security

and efficiency. Beyond the quantitative metrics, our findings highlight fundamental structural

flaws in the “Screen-as-Interface” paradigm that cannot be resolved merely by scaling up model

parameters.

6.1 Structural Fragility of GUI Grounding

The Static Modeling of Dynamic Interfaces. One critical cause of the GUI agent failures

observed in our experiments (e.g., the Bluetooth deadlock in Figure 11) is the mismatch between

the agent’s perception and reality. GUI agents model the operating system as a sequence of discrete,

static screenshots. However, modern mobile UIs are continuous and asynchronous. This forcing of

*[Image: Page 29 Image]*

---

## Page 30

30 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

(a) User instruction (b) Target Post (c) Baseline endorsement

Fig. 15. Hate-speech endorsement. (a) User instruction. (b) The target post contains hate speech (redacted).

(c) The baseline agent posts an endorsement comment. Identifiers and content are redacted.

dynamic processes into static frames leads to inevitable Temporal Misalignment . By the time an

agent processes a screenshot and infers a click coordinate, the UI state may have shifted (e.g., a list

refresh or a toast notification). In contrast, Aura fundamentally resolves this problem via atomic

and transactional API calls. When an AA invokes Bluetooth.scan() , it receives a deterministic

result object, independent of rendering frame rates or UI animations.

The Privilege Paradox: Inescapable Privacy Exposure. GUI agents suffer from a structural

“Privilege Paradox”: to complete tasks, they require total visibility (Accessibility Services). They

cannot “unsee” sensitive information. If a user receives a private notification while the agent is

booking a ticket, the agent’s screenshot inevitably captures both. Aura solves this via Identity-Based

Scoping . An SA/AA is governed under the permission boundary cryptographically granted in its

AIC. A BookingAgent has no API access to the NotificationManager ; therefore, it is impossible

for the agent to ingest or leak private notifications, regardless of what appears on the screen.

6.2 The Architectural Bottleneck: Why Scaling is Insufficient

A critical insight from our evaluation is that Doubao-Pro (may be powered by a significantly more

capable reasoning LMM) did not yield significantly improved performance over Doubao-Standard .

W hile the Pro version exhibited marginally better planning, it failed to supersede the Standard

version in overall robustness (ASR improvement of only ∼ 4.4%), and even regressed in certain

dynamic tasks.

This phenomenon indicates that the primary bottleneck for mobile agents currently lies not in

the reasoning depth of the LMM, but in the structural uncertainty of the GUI grounding. GUI-based

grounding forces the model to operate in a probabilistic environment where visual noise, rendering

latency, and ambiguous DOM trees act as a performance ceiling. Even state-of-the-art LMMs cannot

reliably execute tasks if the underlying interface is inherently unstable or deceptive.

---

## Page 31

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 31

Therefore, further advancements in mobile agents require an architectural paradigm shift besides

model scaling. By transitioning from the noisy, probabilistic “screen-as-interface” paradigm to

the deterministic, structured Agent Universal Runtime Architecture, Aura effectively removes the

environmental uncertainty. This architectural change unlocks the true potential of the foundation

models, allowing them to focus on high-level intent orchestration rather than low-level pixel

alignment.

6.3 Defense against Implicit Semantic Attacks

Our evaluation focused on explicit attacks, but we also identified challenges in detecting implicit

malicious intent disguised in slang or coded language. For instance, in the “Text Messaging” task, a

user may ask to “grab some snow” (a slang term for cocaine). While our Semantic Firewall effectively

intercepts explicit contraband requests, detecting such contextual metaphors remains a challenge.

A static keyword blacklist is insufficient, as “snow” is benign in a weather context.

Mitigation Strategy. To address this, the Agent Kernel ’s knowledge base must be dynamically

updated. We propose a Continuous Learning Loop : the Semantic Validator should be updated with

a curated Contextual Slang Dictionary derived from real-world adversarial cases. By analyzing

the tuple ⟨ Keyword: “snow” , Context: “thrilling/party” , Risk: Drug ⟩ , Aura can refine its decisions.

Maintaining this evolving knowledge base is an ongoing arms race between attackers and defenders.

6.4 System Configuration and Deployment Considerations

The Agent Kernel ’s four defense layers are modular and allow system administrators or device man-

ufacturers to tune the security-performance trade-off based on deployment contexts. For lower-risk

interactions, the Performance Mode optimizes for efficiency by bypassing high-latency verification

steps, relying on lightweight local checks to ensure near-native response times. Conversely, for

critical operations, the Fortified Mode activates the full defense chain to guarantee maximum

security integrity and compliance. This modular and configurable design supports fine-grained

configuration at multiple levels—per-device, per-agent, or per-operation—ensuring Aura adapts

seamlessly to diverse use cases.

6.5 Towards The Agent-Native Secure Operating System

While our prototype targets mobile platforms, the architectural principles underlying Aura and the

Agent Kernel suggest a broader evolution path towards the agent-native secure operating system

(OS) across various computing platforms.

From App-Centric to Agent-Native Execution. Conventional OSes are fundamentally App-

centric: the primary principals are processes and packages, and any “Agent” is an afterthought

implemented as a library on top. In contrast, Aura treats the System Agent (SA) and App Agents

(AAs) as first-class OS principals, with the Agent Kernel mediating their interactions. Extending this

paradigm beyond mobile implies re-architecting desktops, wearables, IoT systems and even cloud

systems around an intent-oriented, Hub-and-Spoke execution model: users express instructions

and goals to the SA, which decomposes them into plans and dispatches work to sandboxed AAs

under a least-privilege policy enforced by a kernel-resident mediator.

Security-Native Substrate. § 4.1 introduced a cryptographically attested identity infrastructure

grounded in the Global Agent Registry (GAR) and Agent Identity Cards (AICs), with TEE-backed

secure boot anchoring the Agent Kernel as a trusted OS module. In an agent-native OS, this infras-

tructure becomes the security substrate : every long-lived principal (SAs and AAs) is represented by

an AIC, the OS boot chain verifies the Agent Kernel and its policy state, and all high-impact actions

are gated on AIC-bound capability boundaries S max and kernel-issued session tokens. Moving from

---

## Page 32

32 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

mobile to general-purpose OSes primarily enlarges the space of Critical Nodes and capability types

(e.g., file-system namespaces, container runtimes, GPU access), but the core pattern—cryptographic

identity, capability ceilings, and runtime validation (§ 4.4)—remains unchanged.

Cross-Device Federation and User-Sovereign Identity. The AIC abstraction naturally supports

a world in which the same logical agent spans multiple devices. A future agent-native OS stack could

allow a user’s SA and AAs to carry per-user AICs across phones, laptops, and home hubs, with each

device’s Agent Kernel enforcing a local S max that is tailored to its hardware and jurisdiction. The

GAR becomes a federated public key infrastructure for agents, while the device-local Agent Kernel

provides consistent enforcement and accountability. This also opens the door to user-sovereign

identity: instead of tying agents to app-store accounts or opaque device IDs, AICs can be anchored

in user-controlled identifiers (e.g., wallet-based or DID-based identities), with the OS enforcing

that all A2A collaboration is explicitly attributable to a user and a set of AICs.

Generalizing the Security Pipeline. The four-layer defense pipeline instantiated by the Agent Ker-

nel in Aura —Identity, Perception, Cognition, Auditable Execution—is not inherently mobile-specific.

On desktops and servers, Identity becomes a unified agent identity layer spanning containers, VMs,

and services; Perception extends to log streams, telemetry, and external APIs; Cognition corresponds

to reinforcement learning loops and orchestration planners; Auditable Execution mediates not

only OS syscalls but also cloud control planes and CI/CD pipelines, tying all of agent activities to

AIC-bound trajectories that can be audited locally or shared with regulators under user control. A

security-native OS would expose these layers as explicit kernel and system services rather than

leaving them to ad-hoc libraries.

Open Challenges and Research Directions. Realizing a fully agent-native secure OS stack raises

several open challenges. First, standardization : we need interoperable schemas for AICs, capability

boundaries, and critical-node taxonomies that can be shared across vendors and platforms. Second,

hardware heterogeneity : different devices expose different TEE capabilities, and future work must

explore how to gracefully degrade or emulate the Agent Kernel ’s guarantees when only partial

hardware support is available. Third, performance and usability : cryptographic attestation, kernel

mediation, and fine-grained accountability introduce latency and complexity; designing human-

centered mechanisms for permission negotiation and transparency dashboards (§ 4.4) that scale

beyond mobile remains an open problem. Finally, evolution of legacy OS abstractions : mapping

traditional concepts such as processes, POSIX permissions, and container isolation into AIC- and

Agent Kernel -centric semantics without breaking backward compatibility will require incremental

deployment strategies and new OS interfaces.

Overall, we view Aura as the initial reference point for this grand journey: it demonstrates that

treating agents as first-class OS citizens and baking security semantics into the OS kernel is not only

feasible on today’s mobile system and hardware, but also a viable blueprint for the next generation

of agent-native OSes across a broad spectrum of computing platforms.

7 Conclusion

This paper presents a comprehensive security audit and architectural reformulation of LLM-powered

mobile agents. Through a rigorous lifecycle analysis, we exposed that current “Screen-as-Interface”

GUI agents are plagued by systemic vulnerabilities that stem from their reliance on unstructured

visual grounding. Specifically, Identity Ambiguity enables impersonation, Unstructured Perception

invites phishing and injection, Context Mixing allows reasoning/planning deviation, and God-

Mode Permissions create single points of catastrophic failure. Using Doubao Mobile Assistant as a

representative commercial deployment, we showed that these issues are not hypothetical: even the

---

## Page 33

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 33

state-of-the-art, system-integrated assistant exhibits all four classes of weaknesses when grounded

purely in GUI perception.

To address these fundamental flaws, we take the first step towards a clean-slate secure agent

Operating System (OS) and introduce Aura , an Agent Universal Runtime Architecture that governs

an agent-native interaction model via Agent Kernel . The Agent Kernel guards the whole agent

lifecycle—identity, perception, cognition, and action—through four pillars of security designs: (i)

a cryptographic agent identity infrastructure, (ii) a semantic firewall for input authentication

and sanitization, (iii) taint-aware memory protection with plan-trajectory alignment, and (iv)

fine-grained action access control with identity-driven accountability.

Our evaluation on MobileSafetyBench demonstrates that Aura is not merely a conceptual alter-

native but a practically deployable one: it improves low-risk Task Success Rate from roughly 75%

(Doubao Mobile Assistant baselines) to 94.3%, reduces the Attack Success Rate on high-risk tasks

from about 40% to 4.4%, and delivers near order-of-magnitude latency reductions by eliminating

redundant visual processing. We conclude that the future of secure mobile agent lies not in building

smarter screen-readers, but in establishing secure, standardized agent-native interaction—a robust

Agent Economy in which trust and accountability are guaranteed by system architecture rather

than ad-hoc patches.

Remarks. At the time of this writing, the explosions of headless agent frameworks like OpenClaw

have partially validated the shift from brittle GUI scraping to structured, API-driven execution. Yet,

OpenClaw exposes raw Shell/API access to LLMs without an OS-level boundary, which introduces

a terrifying new attack surface: ungoverned structured execution. Without a secure substrate

like Aura , the “API-as-Interface” era will be plagued by high-speed, automated exploitation. Aura

provides the necessary constitutional guardrails for this high-performance future. We view Aura

as an initial reference point to start the grand journey of building a secure agent OS for this

next-generation computing infrastructure.

References

[1] 2016. Regulation (EU) 2016/679 of the European Parliament and of the Council. Official Journal of the European Union.

https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679

[2] Anthropic. 2024. Model Context Protocol (MCP) Specification . https://modelcontextprotocol.io/ Accessed: 2026-02-10.

[3] Michael Backes, Sven Bugiel, Erik Derr, Patrick McDaniel, Damien Octeau, and Sebastian Weisgerber. 2016. On

Demystifying the Android Application Framework: Re-Visiting Android Permission Specification Analysis. In 25th

USENIX Security Symposium (USENIX Security 16) . USENIX Association, Austin, TX, 1101–1118.

[4] Davide Bove. 2022. SoK: The Evolution of Trusted UI on Mobile. In Proceedings of the 2022 ACM on Asia Conference on

Computer and Communications Security (Nagasaki, Japan) (ASIA CCS ’22) . Association for Computing Machinery, New

York, NY, USA, 616–629.

[5] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan,

Pranav Shyam, Girish Sastry, Amanda Askell, et al. 2020. Language models are few-shot learners. Advances in neural

information processing systems 33 (2020), 1877–1901.

[6] ByteDance. 2025. Doubao Mobile Assistant. https://o.doubao.com/. Accessed: 2026-01-09.

[7] Ada Chen, Yongjiang Wu, Junyuan Zhang, Jingyu Xiao, Shu Yang, Jen-tse Huang, Kun Wang, Wenxuan Wang, and

Shuai Wang. 2025. A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron? arXiv

preprint arXiv:2505.10924 (2025).

[8] Chaoran Chen, Zhiping Zhang, Bingcan Guo, Shang Ma, Ibrahim Khalilov, Simret A Gebreegziabher, Yanfang Ye,

Ziang Xiao, Yaxing Yao, Tianshi Li, et al. 2025. The Obvious Invisible Threat: LLM-Powered GUI Agents’ Vulnerability

to Fine-Print Injections. arXiv preprint arXiv:2504.11281 (2025).

[9] Victor Costan and Srinivas Devadas. 2016. Intel SGX Explained. Cryptology ePrint Archive, Paper 2016/086. https:

//eprint.iacr.org/2016/086

[10] Badhan Chandra Das, M Hadi Amini, and Yanzhao Wu. 2025. System Prompt Extraction Attacks and Defenses in

Large Language Models. arXiv preprint arXiv:2505.23817 (2025).

[11] Renhua Ding, Xiao Yang, Zhengwei Fang, Jun Luo, Kun He, and Jun Zhu. 2025. Effective and Stealthy One-Shot

Jailbreaks on Deployed Mobile Vision–Language Agents. (2025).

---

## Page 34

34 Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, and Zhuotao Liu

[12] Chenghao Du, Quanfeng Huang, Tingxuan Tang, Zihao Wang, Adwait Nadkarni, and Yue Xiao. 2025. Measuring the

Security of Mobile LLM Agents under Adversarial Prompts from Untrusted Third-Party Channels. arXiv preprint

arXiv:2510.27140 (2025).

[13] William Enck, Peter Gilbert, Seungyeop Han, Vasant Tendulkar, Byung-Gon Chun, Landon P. Cox, Jaeyeon Jung,

Patrick McDaniel, and Anmol N. Sheth. 2014. TaintDroid: An Information-Flow Tracking System for Realtime Privacy

Monitoring on Smartphones. ACM Trans. Comput. Syst. 32, 2, Article 5 (June 2014), 29 pages.

[14] Manu Sporny et al. 2025. Verifiable Credentials Data Model v2.0 . W3C Recommendation. W3C. https://www.w3.org/

TR/2025/REC-vc-data-model-2.0-20250515/.

[15] Gucongcong Fan, Chaoyue Niu, Chengfei Lyu, Fan Wu, and Guihai Chen. 2025. CORE: Reducing UI Exposure in

Mobile Agents via Collaboration Between Cloud and Local LLMs. arXiv preprint arXiv:2510.15455 (2025).

[16] Google. [n. d.]. Android Debug Bridge (ADB) . Android Developers. https://developer.android.com/tools/adb Accessed:

2026-01-09.

[17] Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, and Mario Fritz. 2023. Not

what you’ve signed up for: Compromising real-world llm-integrated applications with indirect prompt injection. In

Proceedings of the 16th ACM workshop on artificial intelligence and security . 79–90.

[18] HONOR. [n. d.]. HONOR AI. https://www.honor.com/global/tech/honor-ai/ Accessed: 2026-01-09.

[19] Juyong Lee, Dongyoon Hahm, June Suk Choi, W Bradley Knox, and Kimin Lee. 2024. Mobilesafetybench: Evaluating

safety of autonomous agents in mobile device control. arXiv preprint arXiv:2410.17520 (2024).

[20] Jungjae Lee, Dongjae Lee, Chihun Choi, Youngmin Im, Jaeyoung Wi, Kihong Heo, Sangeun Oh, Sunjae Lee, and

Insik Shin. 2025. VeriSafe Agent: Safeguarding Mobile GUI Agent via Logic-based Action Verification. arXiv preprint

arXiv:2503.18492 (2025).

[21] Jing Li, Aixin Sun, Jianglei Han, and Chenliang Li. 2022. A Survey on Deep Learning for Named Entity Recognition.

IEEE Transactions on Knowledge and Data Engineering 34, 1 (2022), 50–70. doi:10.1109/TKDE.2020.2981314

[22] Siyuan Liang, Tianmeng Fang, Zhe Liu, Aishan Liu, Yan Xiao, Jinyuan He, Ee-Chien Chang, and Xiaochun Cao. 2025.

SafeMobile: Chain-level Jailbreak Detection and Automated Evaluation for Multimodal Mobile Agents. arXiv preprint

arXiv:2507.00841 (2025).

[23] Xiao Liu, Bo Qin, Dongzhu Liang, Guang Dong, Hanyu Lai, Hanchen Zhang, Hanlin Zhao, Iat Long Iong, Jiadai Sun,

Jiaqi Wang, et al. 2024. AutoGLM: Autonomous Foundation Agents for GUIs. arXiv preprint arXiv:2411.00820 (2024).

[24] Bernard Ngabonziza, Daniel Martin, Anna Bailey, Haehyun Cho, and Sarah Martin. 2016. Trustzone explained:

Architectural features and use cases. In 2016 IEEE 2nd International Conference on Collaboration and Internet Computing

(CIC) . IEEE, 445–451.

[25] Shidong Pan, Yikai Ge, and Xiaoyu Sun. 2025. A First Look at Privacy Risks of Android Task-executable Voice Assistant

Applications. arXiv preprint arXiv:2509.23680 (2025).

[26] Promon. 2019. StrandHogg: Serious Android Vulnerability. https://promon.io/security-news/the-strandhogg-

vulnerability. Accessed: 2026-02-10.

[27] Nilo Redini, Aravind Machiry, Dipanjan Das, Yanick Fratantonio, Antonio Bianchi, Eric Gustafson, Yan Shoshitaishvili,

Christopher Kruegel, and Giovanni Vigna. 2017. BootStomp: On the Security of Bootloaders in Mobile Devices. In

26th USENIX Security Symposium (USENIX Security 17) . USENIX Association, Vancouver, BC, 781–798.

[28] Chuangang Ren, Yulong Zhang, Hui Xue, Tao Wei, and Peng Liu. 2015. Towards discovering and understanding task

hijacking in android. In 24th USENIX Security Symposium (USENIX Security 15) . 945–959.

[29] Xinyue Shen, Zeyuan Chen, Michael Backes, Yun Shen, and Yang Zhang. 2024. " do anything now": Characterizing

and evaluating in-the-wild jailbreak prompts on large language models. In Proceedings of the 2024 on ACM SIGSAC

Conference on Computer and Communications Security . 1671–1685.

[30] Siyan. 2025. Revelations of the Doubao Controversy: Whose Cheese Is the AI Phone Taking? 36Kr Global. https:

//eu.36kr.com/en/p/3598874711310593 Originally published by Wan Dian Research.

[31] Tobin South, Subramanya Nagabhushanaradhya, Ayesha Dissanayaka, Sarah Cecchetti, George Fletcher, Victor Lu,

Aldo Pietropaolo, Dean H. Saxe, Jeff Lombardo, Abhishek Maligehalli Shivalingaiah, Stan Bounev, Alex Keisner, Andor

Kesselman, Zack Proser, Ginny Fahs, Andrew Bunyea, Ben Moskowitz, Atul Tulshibagwale, Dazza Greenwood, Jiaxin

Pei, and Alex Pentland. 2025. Identity Management for Agentic AI: The new frontier of authorization, authentication,

and security for an AI agent world. arXiv:2510.25819 [cs.CR] https://arxiv.org/abs/2510.25819

[32] Magdalena Steinbock, Jens Troost, Wilco Van Beijnum, Jan Seredynski, Herbert Bos, Martina Lindorfer, and Andrea

Continella. 2025. SoK: Hardening Techniques in the Mobile Ecosystem — Are We There Yet? . In 2025 IEEE 10th

European Symposium on Security and Privacy . IEEE Computer Society, Los Alamitos, CA, USA, 789–806.

[33] Zhiqing Sun, Hongkun Yu, Xiaodan Song, Renjie Liu, Yiming Yang, and Denny Zhou. 2020. Mobilebert: a compact

task-agnostic bert for resource-limited devices. arXiv preprint arXiv:2004.02984 (2020).

[34] Junyang Wang, Haiyang Xu, Jiabo Ye, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, and Jitao Sang. 2024. Mobile-

Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception. arXiv preprint arXiv:2401.16158

---

## Page 35

Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System 35

(2024).

[35] Junyang Wang, Haiyang Xu, Jiabo Ye, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang, and Jitao Sang. 2024. Mobile-

Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception. arXiv:2401.16158 [cs.CL] https:

//arxiv.org/abs/2401.16158

[36] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. 2022.

Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing

systems 35 (2022), 24824–24837.

[37] Liangxuan Wu, Chao Wang, Tianming Liu, Yanjie Zhao, and Haoyu Wang. 2025. From Assistants to Adversaries:

Exploring the Security Risks of Mobile LLM Agents. arXiv preprint arXiv:2505.12981 (2025).

[38] Haichuan Xu, Mingxuan Yao, Runze Zhang, Mohamed Moustafa Dawoud, Jeman Park, and Brendan Saltaformaggio.

2024. DVa: Extracting Victims and Abuse Vectors from Android Accessibility Malware. In 33rd USENIX Security

Symposium (USENIX Security 24) . USENIX Association, Philadelphia, PA, 701–718. https://www.usenix.org/conference/

usenixsecurity24/presentation/xu-haichuan

[39] Yulong Yang, Xinshan Yang, Shuaidong Li, Chenhao Lin, Zhengyu Zhao, Chao Shen, and Tianwei Zhang. 2024. Security

matrix for multimodal agents on mobile devices: A systematic and proof of concept study. arXiv e-prints (2024),

arXiv–2407.

[40] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. 2023. ReAct: Synergizing

Reasoning and Acting in Language Models. In International Conference on Learning Representations (ICLR) .

[41] Lepeng Zhao, Zhenhua Zou, Shuo Li, and Zhuotao Liu. 2026. Anonymization-Enhanced Privacy Protection for Mobile

GUI Agents: Available but Invisible. arXiv:2602.10139 [cs.CR] https://arxiv.org/abs/2602.10139

[42] Poe Zhao. 2025. The Platform Power Problem: AI Agents in China’s Mobile Internet . Hello China Tech. https:

//hellochinatech.com/p/platform-power-ai-agents-wechat

[43] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan

Li, Dacheng Li, Eric Xing, et al. 2023. Judging llm-as-a-judge with mt-bench and chatbot arena. Advances in neural

information processing systems 36 (2023), 46595–46623.

[44] Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J Zico Kolter, and Matt Fredrikson. 2023. Universal and

transferable adversarial attacks on aligned language models, 2023. URL https://arxiv. org/abs/2307.15043 19 (2023), 3.

[45] Zhenhua Zou, Zhuotao Liu, Lepeng Zhao, and Qiuyang Zhan. 2025. BlockA2A: Towards Secure and Verifiable

Agent-to-Agent Interoperability. arXiv:2508.01332 [cs.CR] https://arxiv.org/abs/2508.01332
