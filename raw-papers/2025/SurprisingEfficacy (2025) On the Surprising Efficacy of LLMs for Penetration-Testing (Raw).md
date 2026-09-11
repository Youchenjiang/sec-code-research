---
title: "On the Surprising Efficacy of LLMs for Penetration-Testing"
author: "Andreas Happe; Jürgen Cito"
creator: "arXiv GenPDF (tex2pdf:)"
pages: 12
---

# On the Surprising Efficacy of LLMs for Penetration-Testing

> **作者**：Andreas Happe; Jürgen Cito
> **總頁數**：12 頁

---

## Page 1

On the Surprising Efficacy of LLMs for Penetration-Testing

| Andreas Happe | Jürgen Cito |
| --- | --- |
| andreas.happe@tuwien.ac.at | juergen.cito@tuwien.ac.at |
| TU Wien | TU Wien |
| Vienna, Austria | Vienna, Austria |
| ABSTRACT | A common way of preventing security incidents is to test one’s |
| This paper presents a critical examination of the surprising efficacy | own defenses through penetration-testing. The capability of per- |
| of Large Language Models (LLMs) in penetration testing. The pa- | forming sufficient penetration-testing is severely limited by the |
| per thoroughly reviews the evolution of LLMs and their rapidly | amount of available offensive personnel, i.e. ISC2 estimates that |
| expanding capabilities which render them increasingly suitable for | currently 4.7 million cybersecurity experts are missing from the |
| complex penetration testing operations. It systematically details the | workforce. The year-over-year change indicates that this gap is |
| historical adoption of LLMs in both academic research and industry, | still increasing, e.g., by 19.1% [46] in 2025, this indicates a massive |
| showcasing their application across various offensive security tasks | need to make existing security penetration-testers more effective, |
| and covering broader phases of the cyber kill chain. Crucially, the | or even to automate time-consuming parts of penetration-testing, |
| analysis also extends to the observed adoption of LLMs by mali- | reducing the need for manual work by human specialists. As will |
| cious actors, underscoring the inherent dual-use challenge of this | be shown in Section 3, Large Language Models (LLMs) have been |
| technology within the security landscape. | increasingly investigated by both industry and academia to fulfill |
| The unexpected effectiveness of LLMs in this context is eluci- | this need. |
| dated by several key factors: the strong alignment between pen- | In this paper, we reflect on the first two years (2023–2025) of |
| etration testing’s reliance on pattern-matching and LLMs’ core | LLM-aided penetration-testing. We use the Background Section |
| strengths, their inherent capacity to manage uncertainty in dynamic | (Section 2) to create a common understanding of penetration-testing |
| environments, and cost-effective access to competent pre-trained | and highlight important milestones within the evolution of LLMs. |
| models through LLM providers. | In Section 3, we give a short history of how LLMs were used for |
| The current landscape of LLM-aided penetration testing is cate- | penetration-testing, separated into academic research and adoption |
| gorized into interactive ’vibe-hacking’ and the emergence of fully | by industry. After we have shown their clear and present interest in |
| autonomous systems. The paper identifies and discusses significant | LLMs, we discuss why LLMs are a good fit for penetration-testing |
| obstacles impeding wider adoption and safe deployment. These | and summarize the current status-quo (Sections 4 and 5). Subse- |
| include critical issues concerning model reliability and stability, | quently, we highlight obstacles that prevent further adoption of |
| paramount safety and security concerns, substantial monetary and | LLMs before we conclude with a final section highlighting potential |
| ecological costs, implications for privacy and digital sovereignty, | remediation means, also known as research opportunities, for the |
| complex questions of accountability, and profound ethical dilem- | mentioned obstacles. |

mas. This comprehensive review and analysis provides a foundation

for discussion on future research directions and the development 2 BACKGROUND

of robust safeguards at the intersection of AI and security. We introduce penetration-testing, show how pre-LLM AI systems

were used by adversaries, and conclude with a high-level overview

CCS CONCEPTS of the evolution of LLMs.

• Security and privacy → Systems security ; Network security ;

• Computing methodologies → Artificial intelligence . 2.1 Penetration-Testing

During penetration-testing highly-skilled professionals try to break

KEYWORDS systems to uncover vulnerabilities so that those can be mitigated

arXiv:2507.00829v1 [cs.CR] 1 Jul 2025

| Penetration-Testing, Security Testing, Large Language Models, LLM, | by defensive personnel before malicious actors can exploit them. |
| --- | --- |
| Offensive Security | We focus on the practitioners’ daily work [34], not on security |

researchers that seek to find new vulnerabilities and attack vectors

that practitioners will subsequently exploit.

| 1 | INTRODUCTION | Enterprise networks are typically comprised of Microsoft Active |
| --- | --- | --- |
| Upholding an organization’s IT security has been problematic since | Directory, with industry studies indicating that over 90% of Global |  |
| the rise of enterprise networks in the early 2000s. One of the most | Fortune 1000 companies are using it as their primary means of |  |
| publicly visible type of security incidents are ransomware attacks. | authenticating and authorizing users [55]. Having this common |  |
| Current estimates indicate that 72% of business were affected by | technology stack, or mono-culture, for enterprise network architec- |  |
| ransomware between 2018–2023 [81]. Related losses are estimated | tures allows penetration-testers to apply knowledge learned during |  |
| to reach $57 billion for 2025 or $6.5 million per hour [73]. The | prior penetration-tests to new assignments by matching common |  |
| trend indicates a worsening of this situation with estimates of | problems and insecure configurations. Practitioners also describe |  |
| ransomware incidents happening every 2 seconds in 2031, up from | that they can apply knowledge learned during educational attack- |  |
| 11 seconds in 2021 [73]. | ing of simulated systems (CTFs) to real-world systems [34], further |  |

---

## Page 2

Interest into applying machine-learning techniques to offensive

security tasks precedes the rise of LLMs. Mirsky et al. [72] per-

formed a literature review and surveyed experts from academia,

industry, and government on the potential threat of offensive AI

to organizations. The initial version of the paper was released to

arXiv in July 2021, a revised version was published in January 2023.

As ChatGPT went public in late November 2022, this publication

describes the state-of-the-art pre-LLM.

The authors identify 33 AI offensive capabilities and group them

into Automation , Campaign Resilience , Credential Theft , Exploit De-

velopment , Information Gathering , and Stealth . Of these categories,

the top 3 identified capabilities were Exploit Development , Social

Engineering , and Information Gathering . Their survey indicated

that, overall, academia and industry felt that impersonation (and

thus social engineering) was the biggest threat, mirroring another

user study of professional penetration-testers [34] that highlighted

the potential of machine-learning for phishing, a subtask of social

engineering.

They conclude that offensive AI primarily impacts the initial

steps of the cyber kill chain, focusing on reconnaissance, resource

development, and initial access as “ AI technologies are not ma-

ture enough to create agents able to carry on attacks that

proceed without human supervision and aid ”. In 2021, their

outlook on the near future was that “ we aren’t likely to see bot-

nets that can autonomously and dynamically interact with a

diverse set of complex systems (like an organization’s net-

work) in the near future ”.

We will show in this paper that the rise of LLMs has acceler-

escalation and lateral movement. Dwelling deeper on their list of

tion capabilities well-covered by research: Attack Adaption , Attack

Coordination , Next Hop Targeting , Point of Entry Detection . Of Cam-

Password Guessing .

2.3 Evolution of LLMs

and thus sparkled public interest into LLMs. Their API allowed

Andreas Happe and Jürgen Cito

supplied functions, typically used to interact with their environ-

ment. Structured output allows easier integration of LLM’s out-

systems in which agents issue commands to interact with their

environment to solve their given tasks, often autonomously. Re-

trieval Augmented Generation (RAG) and using the ever-increasing

LLM context size for In-Context Learning allowed LLMs to integrate

additional background knowledge [59] without having to expen-

sively retrain models. It became feasible to operate smaller models

on commodity hardware on-edge [97]. Prompt-Engineering used

techniques such as Chain-of-Thought [103] (CoT) to improve the

efficacy of LLMs in complex tasks.

Another big step forward was the introduction of reasoning

LLMs, e.g., by OpenAI introducing the o1 model in 2024 [79]. Rea-

soning models are pre-trained to incorporate CoT during inference,

reducing the dependence on prior prompt-engineering techniques

for solving complex tasks. Recent contested research [82, 90] in-

dicates that reasoning models do not perform reasoning similar

to humans, but that LLMs are “merely” getting even better at

pattern-matching than they were before. Concurrent research

indicates that reasoning LLMs can introduce problems with tool-

calling and instruction-following [61].

Latest advancements further improve the ability of LLMs to inter-

act with their environment or with each other. The Model Context

Protocol (MCP), originally proposed by Anthropic in 2024 [4], stan-

dardized integration of tools into LLMs, leading to an explosion of

available tool-integrations. Recent interest into Multi-Agent Sys-

tems , e.g. Google’s A2A [93], uses multiple collaborating LLMs to

solve complex tasks [51].

3 A SHORT HISTORY OF USING LLMS FOR

LLMs is based on articles posted on security-specific news-sites 1

by LLM providers.

upload to arXiv.

3.1.1 Initial Forays (2023). Given our described methodology, the

first paper that used LLMs for penetration-testing was Getting pwn’d

by AI by Happe et al. [33] in July 2023. They differentiated between

| enforcing the idea that | penetration-testing is often based on | Over time, LLMs gained advanced capabilities [50] such as | tool- |  |  |
| --- | --- | --- | --- | --- | --- |
| pattern-matching | . | calling | or | structured-output | . The former allows LLMs to call user- |
| 2.2 | Pre-LLM Usage of AI for Offensive Security | put into the caller’s system. Both of them have lead to | agentic AI | , |  |
| ated the adoption of machine-learning for offensive security and | PENETRATION-TESTING |  |  |  |  |
| has fulfilled some of the paper’s predictions. While we focus upon | Give the rapid evolution for LLMs, we want to highlight their impact |  |  |  |  |
| penetration-testing (roughly comprising the | automation | and | cam- | on security with a focus on penetration-testing. We differentiate |  |
| paign resilience | categories of their study), our section on malicious | between academic research and industry adoption. |  |  |  |
| industrial use of LLMs (Section 3.2.2) will show that their predic- | For academic research, we used Google Scholar to identify survey |  |  |  |  |
| tions about social engineering, exploit development, and informa- | papers on offensive use of LLMs [7, 20, 39, 48, 69, 74, 87, 107, 113– |  |  |  |  |
| tion gathering became reality. Furthermore, while not employed | 115]. We included papers from these surveys if they were using |  |  |  |  |
| by industry yet, LLMs enabled academic prototypes (Section 3.1) | LLMs to perform penetration-testing, and analyzed them in chrono- |  |  |  |  |
| to cover more phases of the cyber kill chain, including privilege | logical order for their novelty. The analysis of industrial use of |  |  |  |  |
| identified offensive AI capabilities, we see the following | Automa- | mentioning the use of LLMs, as well as on abuse reports provided |  |  |  |
| paign Resilience | ’s capabilities, we see | Campaign Planning | covered; | 3.1 | Academic Research |
| of the other techniques some are implicitly covered by the proto- | We group academic research based on the initial publication year |  |  |  |  |
| types highlighted in Section 3.1, e.g., | Virtualization Detection | and | of the respective publication, typically using the date of their initial |  |  |
| In November 2022, OpenAI made ChatGPT publicly available [78] | two use-cases. On a strategic level, they used chatGPT to devise an |  |  |  |  |
| integration of LLMs into existing tools and workflows. | 1 | https://www.bleepingcomputer.com/ and https://www.darkreading.com/ |  |  |  |

---

## Page 3

On the Surprising Efficacy of LLMs for Penetration-Testing

LLMs have sufficient inherent capabilities for hacking but have

While still focusing on Linux privilege-escalation attacks, they ex-

3.1.2 Broadening Domains and Embracing Newer LLM Capabilities

(2024). In 2024, LLM-capabilities improved through the introduction

of function-calling and structured-output. Supported context sizes

increased from typical 4–16 kTokens in 2023 to typically 64–128

kTokens, with some models allowing for even larger context sizes,

e.g., Google’s Gemini-1.5 model allowed for a context size of up to

one million tokens in February 2024.

In February 2024, Fang et al. [24] published LLM Agents can

Autonomously Hack Websites , extending targets to web sites and

showing that LLMs were able to autonomously find vulnerabilities

within them. They incorporated both in-context learning and were

the first to use function-calling in their prototype. Also in February,

Shao et al. [88] published An Empirical Evaluation of LLMs for Solv-

ing Offensive Security Challenges . They analyze the capacity of LLMs

for solving CTF challenges in interactive and autonomous settings.

Similar to Fang et al., their prototype incorporated function-calling.

They conclude that LLM-driven prototypes produced similar results

They are also the only paper within our analysis that explicitly men-

tioned the need for jailbreaks, i.e., being caught by LLM provider’s

safety filters and needed to bypass these filters by utilizing roleplay

and zero-day vulnerabilities [25]. In their initial paper, they used a

A zero-day vulnerability is unknown to the vendor, and thus there is no patch, miti-

performance.

LLMs to successfully perform penetration-testing, while improving

the hacking results of larger models.

In February 2025, Happe et al. [37] published Can LLMs Hack En-

terprise Networks? , replacing single targets with a real-life Microsoft

Active Directory enterprise network. Their prototype consists of a

high-level strategy component using a penetration task tree, and a

low-level ReAct-based task execution agent. They use tool-calling

and structured-output and analyze the capabilities offered by rea-

soning LLMs. Their results indicate that modern models contain

enough penetration-testing knowledge to perform autonomous

hacking without providing background-knowledge through RAG.

Their results indicate that LLMs have sufficient hacking capabilities

but that results lack consistency, i.e., vary between testruns. They

highlight models’ auto-repair capabilities and conclude that the

costs of using LLMs for penetration-testing compares favorable to

human penetration-testers.

the reviewed publications.

3.2.1 Benign White-Hats. There has been interest in using LLMs

| attack plan and gather information about a target organization. On | GPT-4 based ReAct-agent and highlighted the need for better plan- |  |  |
| --- | --- | --- | --- |
| an operational level, they introduced an autonomous penetration- | ning and improved exploration capabilities. In their latter paper, |  |  |
| testing prototype capable of performing privilege-escalation attacks | they implemented a hierarchical planning system using multiple |  |  |
| against a vulnerable Linux virtual machine. | task-specific agents that were provided background knowledge |  |  |
| Deng et al. [16] published | pentestGPT | in August 2023. Their pro- | through in-context learning. Their results indicate that hierarchi- |
| totype integrates human operators with an LLM to interactively | cal planning improved penetration-testing results by a factor of 6, |  |  |
| hack CTF boxes. They were the first paper to explicitly state that | while task-specific agents and in-context learning both doubled the |  |  |
| problems with context-management, manifesting in missing long- | Finally, in October 2024, Gioacchini et al. [28] introduced | Au- |  |
| term memory, recency bias, and hallucinations. They propose the | toPenBench | . They use function-calling and structured-output to |  |
| Pentest-Task-Tree, a hierarchical todo list, to alleviate these prob- | autonomously solve CTF challenges. Their results indicate that |  |  |
| lems. | LLMs were able to solve challenges if similar tasks were well docu- |  |  |
| In October 2023, Happe et al. [38] published | LLM as Hackers | . | mented publicly through blog posts and walk-throughs. |
| changed the single vulnerable VM with a benchmark comprised of | 3.1.3 | Breaching Out (2025). | In January 2025, Kong et al. [52] in- |
| different privilege-escalation vulnerability classes to further ana- | troduced | VulnBot | , a multi-agent autonomous prototype using a |
| lyze the capabilities of LLMs. They focus on context-management, | penetration-testing task graph as internal storage mechanism for |  |  |
| summarization capabilities, in-context learning for providing back- | creating high-level strategies. They also incorporated RAG for pro- |  |  |
| ground knowledge, the impact of high-level guidance, and included | viding background knowledge to the agent. Also in February, Singer |  |  |
| small language models in their evaluation. Their results indicate | et al. [91] published | On the Feasibility of Using LLMs to Execute Mul- |  |
| that small language models were not feasible for penetration-testing, | tistage Network Attacks | , switching from the single-host attacks |  |
| highlight LLMs’ problems with complex multi-step attacks, and | performed by previous papers to attacking complex multi-stage |  |  |
| the importance of high-level strategy/guidance mechanisms for the | networks. They introduce a tool abstraction layer that simplifies |  |  |
| overall performance of LLMs. | tool usage for LLMs, indicating that this abstraction enables smaller |  |  |
| compared to human penetration-testers. | 3.1.4 | Specialized LLMs for Security Tasks. | In parallel, LLMs were |
| In March, Xu et al. [108] introduced | AutoAttacker | focusing on | fine-tuned for security-tasks [83, 104]. As their makers typically |
| post-breach attacks using the Metasploit attack framework. They ex- | do not publish these models, or, if published, they lack capabilities |  |  |
| plicitly mention the use of RAG for background knowledge storage. | such as tool-calling, these specialized models were not used within |  |  |
| prompting [49]. | 3.2 | Industry Adoption |  |
| Fang et al. analyzed the capability of LLMs for exploit develop- | We differentiate between white-hats trying to improve security, and |  |  |
| ment, i.e., their capability to create exploits for both one-day | 2 | [23] | black-hats trying to use LLMs to exploit security vulnerabilities. |
| 2 | to either accelerate tedious tasks during vulnerability research, to |  |  |
| gation, or fix available to address it. One-day vulnerabilities are known vulnerabilities | increase test coverage within analyzed projects, and to cover more |  |  |
| for which a patch or mitigation is available but hasn’t yet been applied. | projects with vulnerability research. |  |  |

---

## Page 4

hypotheses through independent trajectories. In November 2024,

commonly used network file-system). They provided only a subset

for use-after-free vulnerabilities [110], gave a high-level overview

of the SMB module, and provided a threat model. They then ran

the resulting prompt 100 times, resulting in 8 trajectories correctly

identifying the vulnerability, indicating that LLMs have sufficient

capabilities for finding zero-days, but lack reliability.

LLMs are also used for non-exploitation purposes. Matt Adams

, a LLM-powered automated threat-modeling

tool. Daniel Miessler, a well-known security professional, provides

, an open-source framework for augmenting humans with

AI. In his opinion, “ AI doesn’t have a capabilities problem—it has an

integration problem ”.

professionals using LLMs instead of dedicated search systems for

3.2.2 Malicious Black-Hats. Academic research indicated early up-

publish abuse reports. We analyze malicious tasks included in

3 https://github.com/google/oss-fuzz

Andreas Happe and Jürgen Cito

image generators.

In this section we speculate why LLMs have become a part of the

vanguard for automated penetration-testing.

There are few empirical studies on the work practices of penetration-

testers and their decision making processes [34]. Thus, we include

our own experiences (one of the authors has been a professional

in academic and industrial settings). We encourage further empiri-

support our hypotheses.

Pattern-Matching

bilities in enterprise networks and web-applications.

exploited before.

| Google operates OSS-Fuzz | 3 | which provides continuous fuzzing | the reports provided by OpenAI [75–77, 80], Anthropic [5], and |
| --- | --- | --- | --- |
| for open-source projects. In order to fuzz a project, complex fuzzing | Google [30]. Overall, they show a similar theme: threat actors use |  |  |
| harnesses have to be created. OSS-Fuzz started to use AI for creating | LLMs to accelerate and optimize their work, but they do not use |  |  |
| and testing these fuzz harnesses using AI [63] in August 2023, and | them to create novel methods of attack. Threat actors use LLMs for |  |  |
| reported 26 vulnerabilities detected with help of AI in November | information gathering similar to using search engines, employ them |  |  |
| 2024 [11]. Their blog post highlights how LLMs were used to create | for developing and debugging malicious software, and use them to |  |  |
| and debug fuzz harnesses, leading to increased fuzzing coverage. | generate content for social engineering and phishing attacks. |  |  |
| In addition, LLMs were used to analyze the traces gathered by the | Presumed state-level actors use LLMs for covert | Influence Opera- |  |
| fuzzing process. | tions | (IO) trying to perform election tinkering, sway public opinion |  |
| We will use the cooperation between Google’s Project Zero, a | especially in and around conflict zones, discredit political activists |  |  |
| team of security-analysts tasked with finding zero days, and Google | and parties, attack independent media, sow discontent within pop- |  |  |
| DeepMind as an example study for using LLM agents in security | ulations, and polarize existing population sub-groups. They use |  |  |
| research. In June 2024, Project Zero detailed | Project Naptime | [29], | LLMs to rewrite articles from genuine news sources with a particu- |
| a LLM-powered vulnerability research framework. They utilized | lar political perspective or tone. Anthropic highlighted an | Influence- |  |
| Chain-of-Thought, an interactive environment, specialized tools | as-a-Service | operation in their March 2025 report [5, 58], detailing |  |
| for debugging, and provide an external verification environment | a semi-autonomous LLM-driven system that used approximately |  |  |
| to validate found vulnerabilities. To explore multiple vulnerabil- | 100 fake social-media puppet accounts to influence opinion. AI was |  |  |
| ity hypotheses, instead of implementing a high-level strategizing | used to make both strategic and tactical decisions when and how |  |  |
| loop, they advocate for a sampling strategy that explores multiple | to employ these social accounts and incorporated LLM-powered |  |  |
| they were able to disclose the first real-world vulnerability found | Advanced Persistent Threats (APTs) use LLMs to aid develop- |  |  |
| through their agent, now called | Big Sleep | : an exploitable stack buffer | ment of malware and backdoors, analyze defensive capabilities and |
| underflow in SQLite [95]. | perform deceptive employment schemes. | 6 | As Anthropic states [5], |
| LLM-use is not limited to large-scale companies such as Google. | LLMs “ | flatten the learning curve for malicious actors | ”. OpenAI’ high- |
| Sean Heelan used OpenAI’s o3 model to find CVE-2025-37899 [41], | lighted in its June 2025 report [76] that threat actors start to research |  |  |
| a remote zero-day in the Linux kernel’s SMB implementation (a | into LLM-driven penetration-testing. |  |  |
| of the SMB code to o3 as including the full kernel code would exceed | 4 | ON THE SURPRISING EFFICACY OF LLMS |  |
| o3’s context size. They instructed the LLM to specifically search | FOR PENETRATION-TESTING |  |  |
| released | StrideGPT | 4 | penetration-tester for 13 years and taught penetration-testing both |
| fabric | 5 | cal research into hackers’ work and expect that future findings will |  |
| This list does not include indirect industry use, i.e., security | 4.1 | Penetration-Testing Resembles |  |
| security-specific information-retrieval. Anecdotally, LLM systems | We focus on security practitioners within this work: they are the |  |  |
| are also used during reporting. | professionals that perform daily penetration-tests to find vulnera- |  |  |
| take of LLMs by malicious actors, often facilitated within the Dark- | 4.1.1 | Pattern-Matching is a Substantial Part of Penetration-Testing. |  |
| net [26, 62]. Specialized LLMs employing neither ethical guardrails | Empirical studies with security professionals [34] list examples |  |  |
| nor safety filters were offered to help with exploit development, | of practitioners applying pattern-matching, e.g., identifying vul- |  |  |
| social engineering, and information gathering. Monitoring this ma- | nerable areas or operations through knowledge gained from CTF |  |  |
| licious use of LLMs is complicated by their provider’s inherent | exercises, applying knowledge learned as software developer, using |  |  |
| covert and illegal operation. | knowledge from prior interactions with the customer and their |  |  |
| Public cloud-backed LLM providers have started to periodically | systems, and using vulnerabilities that the penetration-tester has |  |  |
| 4 | https://github.com/mrwadams/stride-gpt | 6 | These are a form of social engineering attack in which the attacker applies for a job |
| 5 | https://github.com/danielmiessler/fabric | interview to gain access to the target organization. |  |

---

## Page 5

On the Surprising Efficacy of LLMs for Penetration-Testing

catalog, matching the right configuration options, and matching

overall target network matches security bad-practices from 10 years

4.1.2 The Target System Landscape is Homogeneous. Pattern-matching

is only feasible if penetration-testing targets exhibit similarities—

otherwise there would be insufficient features to base the pattern-

matching on. Fortunately, when looking at enterprise networks,

over 90% of Global Fortune 1000 companies use the same under-

lying technology stack (Section 2.1). Security practitioners note

that they encounter the same security vulnerabilities and inse-

cure configurations during assignments [34]. When looking at web

penetration-testing, the landscape is more diverse. Applications

utilizing the same technology stack, e.g., the same web framework,

are similar implementation-wise and often exhibit similar vulner-

abilities. Architectures between different technology stacks also

show similarity through common architecture design patterns.

testing background knowledge available from technical blog posts,

When adopting machine learning, there’s always the question of

costs for creating and operating the system, as well as for creating

a training data-set and utilizing it for training.

4.3.1 LLM-Makers are Front-Loading Creation Costs. As shown

through-out our review of academic research (Section 3.1), off-the-

shelf LLMs already contain sufficient background knowledge to

perform penetration-testing, alleviating the need to costly train

new security-specific LLMs. Even if specific additional knowledge

is needed, In-Context Learning and RAG (Section 2.3) offer cost-

effective alternatives to training a model from scratch.

A model alone does not make a penetration-testing prototype—

integration with its environment is also required. The LLM ecosys-

tem provides easy access to development libraries/frameworks.

Technologies, such as function-calling or MCP, make integration

efficient from a development perspective.

| One example of pattern-matching in penetration testing are | Vul- | 4.2 | LLMs Inherently Cope With Uncertainty |  |  |
| --- | --- | --- | --- | --- | --- |
| nerability Assessments | . During those, software version numbers, | 4.2.1 | Uncertainty During Penetration-Testing. | Security practition- |  |
| detected from service banners or application errors messages, are | ers routinely deal with uncertainty [34, 43]. Examples given for |  |  |  |  |
| compared against well-known vulnerabilities. If a match occurred, | sources of uncertainty include interpreting misleading tool out- |  |  |  |  |
| a potentially available exploit is prepared, i.e., its options are filled | puts and target system responses, negative side-effects like target |  |  |  |  |
| with data gathered from the target environment, and execute to ex- | systems becoming unresponsive due to exploits, incomplete infor- |  |  |  |  |
| ploit the expected vulnerability. Pattern matching occurs at multiple | mation about the target environment, and invalid but not falsified |  |  |  |  |
| levels: detecting error messages, matching them to the vulnerability | assumptions about the target system’s behavior and security. |  |  |  |  |
| the exploit’s output to the expected behavior. | 4.2.2 | LLMs’ Pattern-Matching Copes with Uncertainty. | Pattern- |  |  |
| Another low-level occurrence of pattern-matching happens dur- | matching is inherently capable of dealing with uncertainty. During |  |  |  |  |
| ing analyzing of web-application responses containing error mes- | a penetration-test, a LLM-driven hacking prototype will sample the |  |  |  |  |
| sages. For example, LLMs can match error messages that indicate | target environment and create a representation of its view of the |  |  |  |  |
| database issues (SQL injection attacks) to knowledge in their train- | target world, typically as a text-based representation. This world |  |  |  |  |
| ing data, and subsequently successfully exploit these vulnerabili- | view is typically included in subsequent LLM invocations. Com- |  |  |  |  |
| ties [24]. | pared to deterministic rule-based systems, LLMs are able to ignore |  |  |  |  |
| On a higher level, creating an attack-strategy is also grounded in | parts of their world-view through the pattern-matching process. |  |  |  |  |
| patterns seen during security testing. Interviews with professional | This is beneficial during penetration-testing in realistic network |  |  |  |  |
| penetration-testers indicate that they encounter similar insecure | scenarios where actions influence the state of the network, e.g., |  |  |  |  |
| configurations during assignments, create a hypothesis about the | where a failed attack might lead to locked accounts or crashed net- |  |  |  |  |
| network’s security, and select attacks based upon that [34]. For ex- | work servers, changing the ground truth. While traditional systems |  |  |  |  |
| ample, if penetration-testers encounter unsigned NTLMv2-Hashes | need to manually invalidate their world view, LLMs implicitly do |  |  |  |  |
| during an enterprise network security test, they assume that the | this through their pattern-matching approach. |  |  |  |  |
| ago and attempt matching attacks such as pass-the-hash attacks. | 4.3 | The Costs of Using LLMs |  |  |  |
| 4.1.3 | LLMs exceed in Pattern-Matching. | One side-effect of the on- | 4.3.2 | LLM-Providers Enable Cost-Effective Inference. | Running LLMs |
| going discussion about LLMs’ reasoning capabilities is that re- | using cloud-based LLM-providers is cost efficient, e.g., Happe et |  |  |  |  |
| searchers agree that LLMs exceed at pattern-matching [71, 86, 90]. | al. [37] listed operational costs for their penetration-testing proto- |  |  |  |  |
| Given the previous section, this implies that they are well-suited | type running from $0.10 to $11.64 depending on the used LLM. |  |  |  |  |
| for penetration-testing. | Given the sensitive nature of using LLMs for hacking, LLM |  |  |  |  |
| Research implies that LLMs are able to solve tasks if examples in | providers imposing stricter safety guards would negate this benefit. |  |  |  |  |
| their training data resemble those tasks [28]. Given the described | Of the reviewed academic publications, a single paper mentioned |  |  |  |  |
| semi-monocultures, target IT environments should resemble each | problems with safe-guards [108]—and those were easily bypassed |  |  |  |  |
| other. Furthermore, there is ample publicly available penetration- | by simple techniques such as roleplay-prompting [49, 108]. |  |  |  |  |
| incident reports, and CTF walk-throughs and thus included in com- | 4.3.3 | Costs of Running to Stand Still. | In evolutionary biology, the |  |  |
| mon training data sets. We further note that common walkthrough | Red Queen’s hypothesis proposes that species must continuously |  |  |  |  |
| formats, i.e., providing step-by-step instructions including reason- | adopt and evolve to survive while pitted against ever-evolving |  |  |  |  |
| ing steps and tool usage examples, structurally resembles trajecto- | opposing species [98]. In penetration-testing, we have active adver- |  |  |  |  |
| ries used to train LLMs and thus are well-suited to train LLMs. | saries (defensive blue teams) that adapt to our attacks and evolve |  |  |  |  |

---

## Page 6

to be adopted to new vulnerabilities, current trends, and evolved

niques, is thus tempting to time-poor penetration-testers.

ple, if a LLM detects a web-server during an enterprise network

penetration-testers [34].

software-engineering use-cases.

testing. We structure this into interactive use of LLMs ( vibe-hacking )

As Section 3.2 has shown, industrial interactive uptake of LLMs

is already occurring. Borrowing from vibe-coding , this interactive

delegating of tedious tasks has become known as vibe-hacking . Lev-

els of autonomy are diverse, ranging from chat-based LLMs for

information-retrieval and exploit-code generation, over co-pilot

inspired augmenting agents, to systems influenced by pentest-

Andreas Happe and Jürgen Cito

paramount [84].

industrial adoption (Section 3.2).

used autonomous LLM agents [33]. In addition, with increasing

x”, both approaches converge.

runs (Section 3.1).

Autonomous systems often try to minimize the amount of keep-

6 OBSTACLES TO OVERCOME

6.1.1 Impact of Feature Selection. Agentic AI (Section 2) is highly

output, limiting model selection to LLMs supporting these features.

Empirical research [61] has shown that model support for these

features is not homogeneous and, even if features are supported,

using these features can impact the overall quality of LLM responses.

During our research using LLMs-as-Judges, we saw that switching

to structured-output changed the LLM judge’s result.

| their defenses based on our activities, e.g., develop new intrusion- | The former highlights the potential for developer burnout, cat- |  |  |
| --- | --- | --- | --- |
| detection (IDS/IPS) or endpoint detection and response (EDR) capa- | astrophic failures, ethical problems, and increased maintenance |  |  |
| bilities. | costs [60]; while the latter highlight developer efficiency gains and |  |  |
| Security tooling, esp. in case of covert C2 frameworks or vul- | reduction of tedious work. While our use-case, penetration-testing, |  |  |
| nerability scanners, impose a high maintenance cost as they have | does not include high-maintenance overheads, safety concerns are |  |  |
| adversary measures. Penetration-testers also have to continuously | We foresee that, over time, more and more complex tasks will |  |  |
| improve, e.g., learn new attack vectors or how to circumvent novel | be delegated to LLM agents, culminating in LLMs autonomously |  |  |
| counter-measures. Delegating parts of these costs to the LLM-maker, | performing complex multi-step tasks. This is already established |  |  |
| as newer training data will inherently incorporate these new tech- | in academic research (Section 3.1) and first forays can be seen in |  |  |
| 4.4 | Additional Beneficial Capabilities | 5.2 | Towards Autonomous Hacking |
| We want to high-light additional LLM capabilities that, while not | We see two research directions leading towards autonomous hack- |  |  |
| required for successful penetration-testing, are beneficial. | ing. The first paper using LLMs for penetration-testing already |  |  |
| 4.4.1 | Inter-Context Attacks. | Compared to traditional tooling, LLMs | delegated task complexity, interactive LLM-systems resemble au- |
| provide multi-modal or inter-context capabilities [37]. For exam- | tonomous hacking systems. When the task becomes “hack system |  |  |
| penetration-test, it will switch to a web-testing context and perform | Capability evaluations show that LLMs contain sufficient penetration- |  |  |
| a web penetration-test. They are able to detect passwords in text | testing capabilities to successfully exploit systems, but their reli- |  |  |
| files [37] and utilize them during subsequent penetration-testing | ability is lacking, i.e., the same LLM-driven prototype will find |  |  |
| steps. This is a time-consuming task, typically performed by human | different attack chains within the same testbed during multiple |  |  |
| 4.4.2 | Hallucinations often not deemed catastrophic. | LLMs are prone | ing humans in the loop for efficiency reasons, increasing safety |
| to hallucinations, e.g., they invent untrue facts. In small amounts, | concerns (Section 6.2) when deploying autonomous prototypes. |  |  |
| this can be beneficial during penetration-tests as it is similar to | We find it concerning that malicious actors already have started |  |  |
| human penetration-testers trying out hypotheses about the security | to investigate using LLMs for autonomous penetration-testing and |  |  |
| of their target systems. Thus, limited hallucinations are not as | influence-operations (Section 3.2.2), increasing the need for security |  |  |
| problematic for the penetration-testing use-case compared to other | tooling with which defenders can test and improve their defenses. |  |  |
| 5 | STATUS-QUO: VIBE-HACKING AND | We highlight obstacles that prevent further adaption of LLMs for |  |
| AUTONOMOUS AGENTS | penetration-testing. We focus on autonomous use as this includes |  |  |

We want to highlight the current status-quo of LLM-driven penetration- obstacles relevant to vibe-hacking too.

| and in prototypes that use LLMs to autonomously hack systems. | 6.1 | Model Features and Stability |  |  |
| --- | --- | --- | --- | --- |
| 5.1 | Vibe-Hacking | dependent on LLM features such as function-calling and structured- |  |  |
| GPT [16] where humans are responsible for oversight. CTF chal- | 6.1.2 | Minuscule Changes Impact Outcomes. | LLMs can be unstable |  |
| lenges are often created by the same authors, exhibiting patterns | and exhibit chaotic behavior: minimal changes to prompts or switch- |  |  |  |
| in their structure. Anecdotally, CTF players use OpenAI’s custom | ing model versions can substantially impact created trajectories. |  |  |  |
| GPTs support to create LLMs trained with previous challenges cre- | Capability differences between model families are expected, but |  |  |  |
| ated by well-known authors and use that knowledge for future | there can be unexpected differences between versions of the same |  |  |  |
| challenges. Compared to other automation approaches, currently | model family, e.g., there is an ongoing discussion if OpenAI’s o1- |  |  |  |
| vibe-hacking keeps the human in the loop and thus incorporating | preview model’s capabilities were significantly reduced compared |  |  |  |
| an important safety feature. | to the final o1 model [2, 3]. Obviously, prompt engineering has a |  |  |  |
| While | vibe-hacking | is not often discussed online, | vibe-coding | large impact upon the LLM’s results and their consistency [101]. |
| is, current opinions range from AI Angst to AI enthusiasm [8]. | Unobvious, formatting changes orthogonal to the prompt’s content |  |  |  |

---

## Page 7

On the Surprising Efficacy of LLMs for Penetration-Testing

nondeterministic [6].

These instabilities are problematic as seemingly unrelated prompt

adaptions occurring during empirical experiments can potentially

impact and taint the experiment’s measurements.

6.2 Safety and Security Concerns

allowed to attack. If LLMs do not heed those safety instructions,

outcomes can be catastrophic. Concurrent research investigates

rity Applications [10] or CBRN [109] domains. 7 Safety instructions

are also employed during penetration-testing. Happe et al. [37] de-

scribe while they instructed LLMs to only target their lab network

6.2.2 Alignment Concerns. Happe et al. [37] highlight another case

in which the LLM diverged from the user’s original intent by dis-

carding the assigned task and starting to solve an unrelated security

task, thus breaking the model’s alignment with the user’s goals.

Similar problems can occur unintentionally, e.g., through changes

in the model’s deployment infrastructure [27], or can be maliciously

precipitated [66].

6.2.3 Security. Safety and security are intertwined. While we are

investigating the offensive use of LLMs, offensive prototypes can

also become the target of adversaries, e.g., became victims to active

or forward defenses. Offensive AI agents are high-value targets for

attackers as they sit at the intersection of private data, untrusted

content, powerful actions, and external communication [106]. An

adversary, that is able to take over an offensive AI agent, e.g.,

through using a prompt injection, gains powerful means of attack-

ing the agent’s owner or an unrelated third-party system, further

complicating attribution.

6.3 Costs and Efficiency Concerns

6.3.1 Monetary Costs. Running a LLM depends upon a costly run-

6.3.3 Effectiveness of Using LLMs. Given the mentioned monetary

and ecological costs, usage of LLMs should show cost-effectiveness.

The common internet saying of “ go away or I will replace you

with a small shell script ” encapsulates the difference between the

two extremes: writing a shell script can be tedious and resource-

intensive, but operating it is light on resources. Creating a LLM-

space.

LLMs do not exist in emptiness but within the real-world with its

geo-political tensions.

gesting sensitive data. If using cloud-provided LLMs, this sensitive

data is transported to the cloud of the respective LLM provider—a

potential violation of digital sovereignty. If an LLM-driven proto-

type is able to detect and exploit a vulnerability, knowledge of this

vulnerability is also transported to the LLM cloud; this means that

knowledge of an exploitable vulnerability is thus stored outside of

the security perimeter and control of the affected company—both a

security and privacy risk.

6.4.2 Digital Sovereignty. LLMs are currently only provided by a

limited amount of countries, making LLM users dependent upon

those countries.

Another problem is the opaque nature of LLMs. Due to their

missing explainability, both closed- and open-weight models can

contain backdoors that can result in adversary-planted behavior

when triggered by a predefined interaction with the environment.

Kutosov et al. [56] tasked frontier LLMs to compete a main task

while they should also covertly execute a side-task, emulating in-

dustrial espionage, sabotage, and insider threats. Complex models

such as Claude 3.7 Sonnet and Gemini 2.5 Pro performed “best”,

resulting in 27% and 15% successful covert task execution.

disrupted due to a LLM-operated penetration-test that executed

| impact results: He et al. [40] investigated the impact of using dif- | Analysis of the energy and water usage of different model families |  |  |
| --- | --- | --- | --- |
| ferent formats (such as plain text, Markdown, JSON, and YAML) | indicates that reasoning models, such as OpenAI o3 or DeepSeek- |  |  |
| for providing context information and detected a variance of 40% | R1, consume 70 times the energy compared to a small LLM such |  |  |
| when using OpenAI GPT-3.5-turbo. Another problem is that even | as OpenAI GPT-4.1-nano, making conscious model selection an |  |  |
| when using deterministic settings, an LLM’s output can still be | important goal for sustainability [47]. |  |  |
| 6.2.1 | Safety. | As LLMs are autonomously interacting with their | driven hacking prototype is comparatively cheap, but running it |
| environment in potentially destructive ways, safety is of the high- | is resource-intensive. Coming back to Sommer and Paxson [92], |  |  |
| est concern. Typically, prototypes embed safety instructions into | machine-learning might not be an end in itself, but rather an under- |  |  |
| their prompts, e.g., limit valid targets that the LLM prototype is | appreciated means to an end, used to illuminating the problem |  |  |
| potential catastrophic fallout when LLMs are used in National Secu- | 6.4 | Privacy and Digital Sovereignty Concerns |  |
| range, some of their evaluated LLMs ignored those instructions and | 6.4.1 | Privacy. | When LLM-driven penetration-testing prototypes |
| attacked systems explicitly forbidden form being targeted. | interact with enterprise networks, there’s a high chance of them in- |  |  |
| time environment: either they run on expensive local AI accelera- | 6.5 | Accountability Concerns |  |
| tors or are hosted within on-demand clouds occurring a per-minute | 6.5.1 | Who is accountable if a LLM makes a faulty decision? | A fa- |
| cost. Especially newer reasoning models can incur unexpected costs | mous quote from a 1970’s IBM manual has become surprisingly |  |  |
| when using their maker’s cloud offerings: spending thousands of | relevant again: “ | A computer can never be accountable therefore a |  |
| US$ for running a single prototype for few hours is not unheard of; | computer must never make a management decision | ” [45]. There has |  |
| using a non-reasoning LLM with the same prototype can cost 1–2 | been legal precedent of a company being made liable for advice |  |  |
| orders of magnitude less. | given by a LLM-powered chat bot [111]. |  |  |
| 6.3.2 | Ecological Costs. | Concerns about non-monetary cost are | Given the potential catastrophic impact of a security LLM-prototype |
| becoming more prominent [96]. Energy-usage of LLMs imposes | interacting with their target environment, who is liable for direct |  |  |
| a ecological burden that needs to be answered for by their utility. | and collateral damages? Imagine, that a company’s operation is |  |  |
| 7 | Chemical, Biological, Radiological and Nuclear (CBRN) | a destructive command unrelated to the penetration-testing task |  |

---

## Page 8

“normal” company but to a power plant?

6.5.2 Overlap with Explainability. Regulatory and legal require-

ments often imply explainability. The European Union’s AI Act

mandates that organizations operating high-risk AI systems must

provide meaningful explanations of AI decisions to individuals. In

the United States of America, the FDA’s proposed framework for med-

ical devices empathizes the importance of explainable AI for patient

safety and clinical decision making [18].

6.6 Capability vs. Reliability

6.6.1 Missing Reliability. As mentioned in Sections 3.1.3 and 3.2.2,

experiments indicate that LLMs exhibit capabilities for penetration-

testing but lack reliability, i.e., multiple runs of the same prototype

against the same testbed yield different vulnerabilities. The obvious

solution of repeatedly calling the prototype is problematic due to

the higher time- and resource usage (Section 6.3). In addition, if

a security-test should be covert, repeatedly calling the prototype

might trigger detection. Better approaches to raise consistency and

reliability are needed.

curity testing, i.e., providing access to security testing to parties that

currently lack means of testing to improve their security posture.

(SMEs), non-governmental, and non-profit organizations (NGOs

and NPOs). As shown in our review of blackhat activities (Sec-

tion 3.2.2), malicious actors also see the potential of AI, although

with less benign intentions. This problematic situation results from

the inherent dual-purpose nature of security tooling [65]. Recent

research into how security researcher express their ethical consid-

erations indicates that they are aware of this ethical dilemma [36].

Andreas Happe and Jürgen Cito

and lower-skill workers [9].

Experience indicates that successful use of autonomous LLM-

agents depends on oversight by highly-skilled human workers with

domain knowledge [105]. Recent research shows that (premature)

use of LLMs during education, e.g., through delegating information-

retrieval tasks, has negative impact on brain neural connectivity,

leading to measurable negative impact on learning skills [53]. Do

we bite the hand that feeds us?

7 THE WAY FORWARD?

Academic (Section 3.1) and industrial (Section 3.2) uptake of LLMs

suggest that they will play an increasing role for cybersecurity in

the near future. As Section 5 showed, vibe-hacking is already here,

and real-world use of LLMs for autonomous hacking is currently

investigated by both white- and blackhats. Based on the issues

mentioned in Section 6, we now turn to potential remediations and

research opportunities to enable and ease adaption of LLMs for

offensive security tasks.

7.1 Costs and Features

soning models seem to struggle with function calling [112]. While

image- and video-creation [68], is used by blackhats for influence

at large, to decide (Section 7.4).

LLMs become further integrated into security workflows and thus

gain more potential to interact with their environment, making

their security and safety parameter (Section 6.2). If security or safety

incidents occur, Accountability (Section 6.5) becomes important.

Google identified multiple features needed for operating secure

LLM-based systems [21]. Prominent features were, e.g., protection

from malicious inputs, limitation of agents’ interaction capabilities,

| at hand. Who is liable for damages? What if this happens not to a | with the hopeful expectation that LLMs will be beneficial for novice |  |  |  |
| --- | --- | --- | --- | --- |
| 6.6.2 | The Problem with Capability Evaluations. | Capability Evalua- | While LLM-based experiments can impose substantial costs (Sec- |  |
| tions are used to measure LLM’s abilities throughout diverse fields, | tion 6.3), the overall trajectory indicates continuously decreasing |  |  |  |
| typically using testbeds and benchmarks. Benchmark test-cases | costs per token. For example, during January 2025, one million |  |  |  |
| have multiple desired properties, e.g., atomicity of test-cases and re- | output/reasoning tokens using OpenAI’s o1 model would cost $60. |  |  |  |
| producibility, that can conflict with real-world use-cases which are | Five months later, using the new o3 model, the costs would have |  |  |  |
| often “messy” and not reproducible [35]. There are concerns [64, 92] | been reduced from $60 to $8 per million output/reasoning tokens. |  |  |  |
| that synthetic test-beds often do not measure real-world impact | Newer model releases typically also improve their feature sup- |  |  |  |
| and thus not provide meaningful guidance for LLM development. | port, e.g., function-calling and structured-output. Currently, rea- |  |  |  |
| 6.7 | Concerns About Ethics | this problem is something that researchers should be aware of, this |  |  |
| While usage of LLMs might be technically feasible, the question | situation should resolve itself quickly. |  |  |  |
| arises if it is ethical, or wise, to advance this research. Machine- | While costs per token decreases, overall volume of token con- |  |  |  |
| learning ethics is a diverse field; we only cover the subset of using | sumption is rising and thus impacts global energy use and ecology. |  |  |  |
| LLMs for penetration-testing purposes and refer to existing publi- | To reduce this impact, careful selection of models is essential, e.g., |  |  |  |
| cations for areas not covered in this publication, such as bias [14, | only using reasoning models if their capabilities are needed. Unfor- |  |  |  |
| 94, 100] or potential problems with training data [13, 19, 67]. | tunately, one of the most resource-intensive areas of using LLMs, |  |  |  |
| 6.7.1 | Democratizing Access to Penetration-Testing. | Mirsky et al. [72] | operations (Section 3.2.2)—we assume that these malicious opera- |  |
| noted that | AI is a Double-Edged Sword | . Security researchers with | tors are not that ecology-conscious. Ultimately, the decision about |  |
| noble intentions see the potential of AI democratizing access to se- | the ecological impact of LLMs if for each individual, and societies |  |  |  |
| Examples typically given include small- and medium businesses | 7.2 | The Need for Better Safeguards |  |  |
| 6.7.2 | Impact Upon Workforce. | In economics, Schumpeter’s | Cre- | and clear human oversight being enforced. |
| ative Destruction | describes a process in which new innovations re- | Prototypes can use LlamaGuard [44] to analyze user input for |  |  |
| place and make obsolete older innovations [17]. The impact of LLMs, | unsafe content, e.g., if a user might follow criminal intentions. The |  |  |  |
| especially their potential for automating tasks, on the workforce is | similarly named Llama PromptGuard [70] can be used to detect |  |  |  |
| currently subject of academic discussions [22, 42, 54, 85, 89, 102] | malicious inputs used for prompt-injection or jailbreak attacks. |  |  |  |

---

## Page 9

On the Surprising Efficacy of LLMs for Penetration-Testing

| Google CaMeL [15] applies | Control Flow Integrity | [1], a traditional | often have to ultimately decide if they value, e.g., privacy, over |
| --- | --- | --- | --- |
| defensive mechanism, to LLM prompting and uses it to separate | LLM-provided features. |  |  |
| data from control flow. Meta’s CodeShield [12] uses source-code | Andy Masley compared resource-consumption of using LLMs |  |  |
| analysis to prevent malicious program generation through agentic | with other lifestyle-decisions [96] and calculated the equivalent of |  |  |
| AI. Agent AlignmentChecks [12] continuously compares a LLM’s | “going vegan” with 400 | . | 000 chatGPT text queries a year, concluding |
| reasoning trace with the user’s stated goal to detect misalignment. | with that his becoming vegan will offset his chatGPT use. When |  |  |
| Still, using agentic AI for penetration-testing imposes the prob- | measuring the average query counts of the two best-performing |  |  |
| lem that we cannot differentiate ethical hacking (whitehats) from | LLMs for hacking enterprise networks [37], we arrive at 165 | . | 75 |
| unethical hacking (blackhats) as the utilized mechanisms and tech- | queries per hours, or | . | 145 million queries a year if the autonomous |
| niques are identical. In the case of red-teaming, there is not even a | penetration-testing prototype is running 24/7. Given their prelimi- |  |  |
| difference in the target’s awareness of being attacked. Ultimately, | nary results, this could prevent dozens or hundreds of ransomware |  |  |
| the only difference is the potential impact of a penetration-testing | incidents saving resource-intesive recovery costs. How would this |  |  |
| campaign on the target, but as this is orthogonal to the penetration- | balance out? |  |  |

testing operations that were performed before, this cannot be used

| to differentiate ethical from unethical behavior. | 8 | CONCLUSION |
| --- | --- | --- |
| Please note that concerns for safety and security should not | Using LLMs for offensive security is evolving at a fast pace. Vibe- |  |
| be abused as reason to put ethical penetration-testing prototypes | hacking has already been established; autonomous penetration- |  |
| inside walled-gardens to prepare later commercialization. | testing is currently investigated within Academia while both black- |  |

and whitehat hackers are deploying first systems in production.

Given the scarcity of professional penetration-testers, a reduction

7.3 Capabilities and Reliability

in interest is hard to believe in.

| As seen in Section 6.6.1, there is currently a lack of reliability and | Due to the high-risk environment, keeping humans in the loop |
| --- | --- |
| reproducibility when using LLMs for penetration-testing. Improve- | is essential for production environments’ safety. We hope that the |
| ments can be categorized in single-agent and multi-agent solutions. | proliferation of using LLMs during in or during education will |
| The former try to improve reliability within a single agent’s trajec- | not reduce human capabilities [53] needed for performing this |
| tory, while the latter combine multiple agents to increase reliability | oversight. |
| while typically imposing higher token costs due to more agents | Security tooling always had an dual-edged nature, especially |
| being run. | if it is deployable in an autonomous manner as this reduces the |
| Single-LLM solutions currently explore the impact of self-discussion | skills needed to perform security audits. We have reports of initial |
| or self-challenging [116], investigate better state management [57], | adversarial use (Section 3.2.2), we are already within a weapons |
| or implement auto-correction mechanisms [37]. Multi-LLM solu- | race. Fittingly, Vernor Vinge [99] used the Red Queen’s paradox |
| tions typically combine output of multiple agents using techniques | to illustrate the struggle between encouraging technological ad- |
| such as LLM-as-judge [31] to integrate the results of singular agents. | vancement and protecting the world if technology is abused. While |
| As Anthropic notes [32], multi-agent systems improve the actin- | originally this was written as part of a science fiction story-line, we |
| space search breadth but incur substantial higher token costs (they | are living it out right now. |

note that their multi-agent system consumes 3 . 75 times the to-

| kens of a similar single-agent system) introducing an overlap with | REFERENCES |  |
| --- | --- | --- |
| monetary and economic cost concerns (Section 6.3). | [1] | Martín Abadi, Mihai Budiu, Ulfar Erlingsson, and Jay Ligatti. Control-flow |
| If a multi-agent system uses multiple different LLMs, concerns | integrity principles, implementations, and applications. | ACM Transactions on |

Information and System Security (TISSEC) , 13(1):1–40, 2009.

| about LLM stability in face of minuscule changes altering the tra- | [2] | Anonymous. O1 is less powerful than o1-preview due to the less time it spends |
| --- | --- | --- |
| jectory substantially (Section 6.1.2 should be alleviated as each | on thinking (compute time). | https://www.reddit.com/r/OpenAI/comments/ |
| individual model should have a reduced overall impact on the sys- | 1h7qtaf/o1_is_less_powerful_than_o1preview_due_to_the/, December 2024. |  |

Accessed: 2025-06-29.

| tem’s result. | [3] | Anonymous. Performance of o1 vs. o1-preview. https://community.openai. |
| --- | --- | --- |
| Regardless of the chosen approach, more empirical data about | com/t/performance-o1-vs-o1-preview/1046831/1, December 2024. Accessed: |  |
| model behavior is needed. Improving the explainability of models | 2025-06-29. |  |

[4] Anthropic. Introducing the model context protocol. https://www.anthropic.

would make analysis of models’ decisions more impactful and also com/news/model-context-protocol, November 2024. Accessed: 2025-06-02.

more efficient. [5] Anthropic. Detecting and countering malicious uses of claude: March

2025. https://www.anthropic.com/news/detecting-and-countering-malicious-

uses-of-claude-march-2025, April 2025. Accessed: 2025-06-19.

[6] Berk Atil, Sarp Aykent, Alexa Chittams, Lisheng Fu, Rebecca J. Passonneau,

7.4 Decision Time for Individuals and Society Evan Radcliffe, Guru Rajan Rajagopal, Adam Sloan, Tomasz Tudrej, Ferhan Ture,

Zhe Wu, Lixinyu Xu, and Breck Baldwin. Non-determinism of "deterministic"

| While we try to propose technological improvements, some of the | llm settings, 2025. URL https://arxiv.org/abs/2408.04667. |  |
| --- | --- | --- |
| imposed problems of LLMs are for society to decide, i.e., are a | [7] | Mohamed Boukhlif, Nassim Kharmoum, and Mohamed Hanine. Llms for in- |
| socio-economical problem, not a technological one. We need con- | telligent software testing: A comparative study. In | Proceedings of the 7th In- |

ternational Conference on Networking, Intelligent Systems and Security , NISS

| sensus on how to handle privacy, ecological impact, ethical issues, | ’24, New York, NY, USA, 2024. Association for Computing Machinery. ISBN |
| --- | --- |
| accountability, and digital sovereignty concerns (Section 6.7). While | 9798400709296. doi: 10.1145/3659677.3659749. URL https://doi.org/10.1145/ |

3659677.3659749.

technology solutions for parts of the problems exists, e.g., running [8] Tim Bray. Ai angst. https://www.tbray.org/ongoing/When/202x/2025/06/06/

small language models locally to keep data private, individuals will My-AI-Angst, June 2025. Accessed: 2025-06-29.

---

## Page 10

Andreas Happe and Jürgen Cito

| [9] | Erik Brynjolfsson, Danielle Li, and Lindsey Raymond. Generative ai at work. | [34] | Andreas Happe and Jürgen Cito. Understanding hackers’ work: An empirical |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The Quarterly Journal of Economics | , page qjae044, 2025. | study of offensive security practitioners. In | Proceedings of the 31st ACM Joint |  |  |  |  |  |  |  |  |  |  |  |
| [10] | William N Caballero and Phillip R Jenkins. On large language models in national | European Software Engineering Conference and Symposium on the Foundations |  |  |  |  |  |  |  |  |  |  |  |  |
| security applications. | Stat | , 14(2):e70057, 2025. | of Software Engineering | , ESEC/FSE ’23, page 1669–1680. ACM, November 2023. |  |  |  |  |  |  |  |  |  |  |
| [11] | Oliver Chang, Dongge Liu, and Jonathan Metzman. Leveling up fuzzing: Finding | doi: 10.1145/3611643.3613900. URL http://dx.doi.org/10.1145/3611643.3613900. |  |  |  |  |  |  |  |  |  |  |  |  |
| more vulnerabilities with ai. https://security.googleblog.com/2024/11/leveling- | [35] | Andreas Happe and Jürgen Cito. Benchmarking practices in llm-driven offensive |  |  |  |  |  |  |  |  |  |  |  |  |
| up-fuzzing-finding-more.html, November 2024. Accessed: 2025-06-19. | security: Testbeds, metrics, and experiment design, 2025. URL https://arxiv.org/ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [12] | Sahana Chennabasappa, Cyrus Nikolaidis, Daniel Song, David Molnar, | abs/2504.10112. |  |  |  |  |  |  |  |  |  |  |  |  |
| Stephanie Ding, Shengye Wan, Spencer Whitman, Lauren Deason, Nicholas | [36] | Andreas Happe and Jürgen Cito. | On the ethics of using llms for offensive |  |  |  |  |  |  |  |  |  |  |  |
| Doucette, Abraham Montilla, et al. Llamafirewall: An open source guardrail | security, 2025. URL https://arxiv.org/abs/2506.08693. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| system for building secure ai agents. | arXiv preprint arXiv:2505.03574 | , 2025. | [37] | Andreas Happe and Jürgen Cito. | Can llms hack enterprise networks? au- |  |  |  |  |  |  |  |  |  |
| [13] | A. Feder Cooper, Aaron Gokaslan, Amy B. Cyphert, Christopher De Sa, Mark A. | tonomous assumed breach penetration-testing active directory networks, 2025. |  |  |  |  |  |  |  |  |  |  |  |  |
| Lemley, Daniel E. Ho, and Percy Liang. | Extracting memorized pieces of | URL https://arxiv.org/abs/2502.04227. |  |  |  |  |  |  |  |  |  |  |  |  |
| (copyrighted) books from open-weight language models, 2025. | URL https: | [38] | Andreas Happe, Aaron Kaplan, and Juergen Cito. Llms as hackers: Autonomous |  |  |  |  |  |  |  |  |  |  |  |
| //arxiv.org/abs/2505.12546. | linux privilege escalation attacks. | arXiv preprint arXiv:2310.11409 | , 2024. |  |  |  |  |  |  |  |  |  |  |  |
| [14] | Sunhao Dai, Chen Xu, Shicheng Xu, Liang Pang, Zhenhua Dong, and Jun Xu. | [39] | Mohammed Hassanin and Nour Moustafa. A comprehensive overview of large |  |  |  |  |  |  |  |  |  |  |  |
| Bias and unfairness in information retrieval systems: New challenges in the llm | language models (llms) for cyber defences: Opportunities and directions, 2024. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| era. In | Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery | URL https://arxiv.org/abs/2405.14487. |  |  |  |  |  |  |  |  |  |  |  |  |
| and Data Mining | , pages 6437–6447, 2024. | [40] | Jia He, Mukund Rungta, David Koleczek, Arshdeep Sekhon, Franklin X Wang, |  |  |  |  |  |  |  |  |  |  |  |
| [15] | Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes, Nicholas Carlini, | and Sadid Hasan. Does prompt formatting have any impact on llm performance?, |  |  |  |  |  |  |  |  |  |  |  |  |
| Daniel Fabian, Christoph Kern, Chongyang Shi, Andreas Terzis, and Florian | 2024. URL https://arxiv.org/abs/2411.10541. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tramèr. Defeating prompt injections by design. | arXiv preprint arXiv:2503.18813 | , | [41] | Sean | Heelan. | How | i | used | o3 | to | find | cve-2025-37899, | a | remote |
| 2025. | zeroday | vulnerability | in | the | linux | kernel’s | smb | implementation. |  |  |  |  |  |  |
| [16] | Gelei Deng, Yi Liu, Víctor Mayoral-Vilches, Peng Liu, Yuekang Li, Yuan Xu, | https://sean.heelan.io/2025/05/22/how-i-used-o3-to-find-cve-2025-37899-a- |  |  |  |  |  |  |  |  |  |  |  |  |
| Tianwei Zhang, Yang Liu, Martin Pinzger, and Stefan Rass. | { | PentestGPT | } | : | remote-zeroday-vulnerability-in-the-linux-kernels-smb-implementation/, |  |  |  |  |  |  |  |  |  |
| Evaluating and harnessing large language models for automated penetration | May 2025. Accessed: 2025-06-19. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| testing. In | 33rd USENIX Security Symposium (USENIX Security 24) | , pages 847– | [42] | Oliver Azuara Herrera, Laura Ripani, and Eric Torres Ramirez. | Ai and the |  |  |  |  |  |  |  |  |  |
| 864, 2024. | increase of productivity and labor inequality in latin america: Potential impact |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [17] | Arthur M Diamond Jr. | Schumpeter’s creative destruction: A review of the | of large language models on latin american workforce. 2024. |  |  |  |  |  |  |  |  |  |  |  |
| evidence. | Journal of Private Enterprise | , 22(1):120, 2006. | [43] | Zhiyuan Hu, Chumin Liu, Xidong Feng, Yilun Zhao, See-Kiong Ng, Anh Tuan |  |  |  |  |  |  |  |  |  |  |
| [18] | Lee Dittmar. The explainability challenge of generative ai and llms. https://www. | Luu, Junxian He, Pang Wei W Koh, and Bryan Hooi. Uncertainty of thoughts: |  |  |  |  |  |  |  |  |  |  |  |  |
| oceg.org/the-explainability-challenge-of-generative-ai-and-llms/, November | Uncertainty-aware planning enhances information seeking in llms. | Advances |  |  |  |  |  |  |  |  |  |  |  |  |
| 2024. Accessed: 2025-06-21. | in Neural Information Processing Systems | , 37:24181–24215, 2024. |  |  |  |  |  |  |  |  |  |  |  |  |
| [19] | Chris Draper and Nicky Gillibrand. The potential for jurisdictional challenges | [44] | Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi Rungta, Krithika Iyer, |  |  |  |  |  |  |  |  |  |  |  |
| to ai or llm training datasets. In | AI4AJ@ ICAIL | , 2023. | Yuning Mao, Michael Tontchev, Qing Hu, Brian Fuller, Davide Testuggine, et al. |  |  |  |  |  |  |  |  |  |  |  |
| [20] | Rohit Dube. Large language models in information security research: A january | Llama guard: Llm-based input-output safeguard for human-ai conversations. |  |  |  |  |  |  |  |  |  |  |  |  |
| 2024 survey. | ResearchGate preprint RG | , 2(20107.26404), 2024. | arXiv preprint arXiv:2312.06674 | , 2023. |  |  |  |  |  |  |  |  |  |  |
| [21] | Santiago (Sal) Díaz, Christoph Kern, and Kara Olive. Google’s approach for | [45] | Civic Innovations. Ethics and algorithms. https://civic.io/2022/12/14/ethics- |  |  |  |  |  |  |  |  |  |  |  |
| secure ai agents. Technical report, 2025. | and-algorithms/, December 2022. Accessed: 2025-06-02. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [22] | Tyna Eloundou, Sam Manning, Pamela Mishkin, and Daniel Rock. Gpts are | [46] | ISC2. 2024 isc2 cybersecurity workforce study. https://www.isc2.org/Insights/ |  |  |  |  |  |  |  |  |  |  |  |
| gpts: Labor market impact potential of llms. | Science | , 384(6702):1306–1308, 2024. | 2024/10/ISC2-2024-Cybersecurity-Workforce-Study, October 2024. Accessed: |  |  |  |  |  |  |  |  |  |  |  |
| [23] | Richard Fang, Rohan Bindu, Akul Gupta, and Daniel Kang. Llm agents can | 2025-06-13. |  |  |  |  |  |  |  |  |  |  |  |  |
| autonomously exploit one-day vulnerabilities, 2024. URL https://arxiv.org/abs/ | [47] | Nidhal Jegham, Marwen Abdelatti, Lassad Elmoubarki, and Abdeltawab Hen- |  |  |  |  |  |  |  |  |  |  |  |  |
| 2404.08144. | dawi. How hungry is ai? benchmarking energy, water, and carbon footprint of |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [24] | Richard Fang, Rohan Bindu, Akul Gupta, Qiusi Zhan, and Daniel Kang. Llm | llm inference, 2025. URL https://arxiv.org/abs/2505.09598. |  |  |  |  |  |  |  |  |  |  |  |  |
| agents can autonomously hack websites, 2024. URL https://arxiv.org/abs/2402. | [48] | Haolin Jin, Linghan Huang, Haipeng Cai, Jun Yan, Bo Li, and Huaming Chen. |  |  |  |  |  |  |  |  |  |  |  |  |
| 06664. | From llms to llm-based agents for software engineering: A survey of current, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [25] | Richard Fang, Rohan Bindu, Akul Gupta, Qiusi Zhan, and Daniel Kang. Teams | challenges and future, 2024. URL https://arxiv.org/abs/2408.02479. |  |  |  |  |  |  |  |  |  |  |  |  |
| of llm agents can exploit zero-day vulnerabilities, 2024. URL https://arxiv.org/ | [49] | Zachary D Johnson. | Generation, Detection, and Evaluation of Role-play based |  |  |  |  |  |  |  |  |  |  |  |
| abs/2406.01637. | Jailbreak attacks in Large Language Models | . PhD thesis, Massachusetts Institute |  |  |  |  |  |  |  |  |  |  |  |  |
| [26] | Mohamed Fazil Mohamed Firdhous, Walid Elbreiki, Ibrahim Abdullahi, BH Su- | of Technology, 2024. |  |  |  |  |  |  |  |  |  |  |  |  |
| dantha, and Rahmat Budiarto. Wormgpt: a large language model chatbot for | [50] | Muhammad Zaeem Khan, Saleha Jamshed, Sadia Ahmad, Aleesha Zainab, Kay- |  |  |  |  |  |  |  |  |  |  |  |  |
| criminals. In | 2023 24th International Arab Conference on Information Technology | nat Khatib, Faria Bibi, Abdul Rehman, et al. Advances in llms with focus on |  |  |  |  |  |  |  |  |  |  |  |  |
| (ACIT) | , pages 1–6. IEEE, 2023. | reasoning, adaptability, efficiency and ethics. | arXiv preprint arXiv:2506.12365 | , |  |  |  |  |  |  |  |  |  |  |
| [27] | Asma Ghandeharioun, Ann Yuan, Marius Guerard, Emily Reif, Michael Lepori, | 2025. |  |  |  |  |  |  |  |  |  |  |  |  |
| and Lucas Dixon. Who’s asking? user personas and the mechanics of latent | [51] | Dezhang Kong, Shi Lin, Zhenhua Xu, Zhebo Wang, Minghao Li, Yufeng Li, |  |  |  |  |  |  |  |  |  |  |  |  |
| misalignment. | Advances in Neural Information Processing Systems | , 37:125967– | Yilun Zhang, Zeyang Sha, Yuyuan Li, Changting Lin, Xun Wang, Xuan Liu, |  |  |  |  |  |  |  |  |  |  |  |
| 126003, 2024. | Muhammad Khurram Khan, Ningyu Zhang, Chaochao Chen, and Meng Han. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [28] | Luca Gioacchini, Marco Mellia, Idilio Drago, Alexander Delsanto, Giuseppe | A survey of llm-driven ai agent communication: Protocols, security risks, and |  |  |  |  |  |  |  |  |  |  |  |  |
| Siracusano, and Roberto Bifulco. Autopenbench: Benchmarking generative | defense countermeasures, 2025. URL https://arxiv.org/abs/2506.19676. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| agents for penetration testing, 2024. URL https://arxiv.org/abs/2410.03225. | [52] | He Kong, Die Hu, Jingguo Ge, Liangxiong Li, Tong Li, and Bingzhen Wu. |  |  |  |  |  |  |  |  |  |  |  |  |
| [29] | Sergei Glazunov and Mark Brand. Project naptime: Evaluating offensive security | Vulnbot: Autonomous penetration testing for a multi-agent collaborative frame- |  |  |  |  |  |  |  |  |  |  |  |  |
| capabilities of large language models. https://googleprojectzero.blogspot.com/ | work. | arXiv preprint arXiv:2501.13411 | , 2025. |  |  |  |  |  |  |  |  |  |  |  |
| 2024/06/project-naptime.html, June 2024. Accessed: 2025-06-19. | [53] | Nataliya Kosmyna, Eugene Hauptmann, Ye Tong Yuan, Jessica Situ, Xian-Hao |  |  |  |  |  |  |  |  |  |  |  |  |
| [30] | Google Threat Intelligence Group. | Adversarial misuse of generative | Liao, Ashly Vivian Beresnitzky, Iris Braunstein, and Pattie Maes. Your brain on |  |  |  |  |  |  |  |  |  |  |  |
| ai. https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse- | chatgpt: Accumulation of cognitive debt when using an ai assistant for essay |  |  |  |  |  |  |  |  |  |  |  |  |  |
| generative-ai, January 2025. Accessed: 2025-06-19. | writing task, 2025. URL https://arxiv.org/abs/2506.08872. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [31] | Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin | [54] | Elizabeth Koumpan | 1 | and Lynda McOwen. Revolutionizing talent: the path in |  |  |  |  |  |  |  |  |  |
| Xu, Wei Li, Yinghan Shen, Shengjie Ma, Honghao Liu, et al. | A survey on | 21st century workforce transformation. | Human Factors, Business Management |  |  |  |  |  |  |  |  |  |  |  |
| llm-as-a-judge. | arXiv preprint arXiv:2411.15594 | , 2024. | and Society | , 33(16):74, 2024. |  |  |  |  |  |  |  |  |  |  |
| [32] | Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jerem Fox, and | [55] | Swetha Krishnamoorthi and Jarad Carleton. Active directory holds the keys to |  |  |  |  |  |  |  |  |  |  |  |
| Daniel Ford. How we built our multi-agent research system. https://www. | your kingdom, but is it secure? https://www.frost.com/growth-opportunity- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| anthropic.com/engineering/built-multi-agent-research-system, June 2025. Ac- | news/active-directory-holds-the-keys-to-your-kingdom-but-is-it-secure, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cessed: 2025-06-21. | March 2020. Accessed: 2025-06-02. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [33] | Andreas Happe and Jürgen Cito. | Getting pwn’d by ai: Penetration testing | [56] | Jonathan Kutasov, Yuqi Sun, Paul Colognese, Teun van der Weij, Linda Petrini, |  |  |  |  |  |  |  |  |  |  |
| with large language models. In | Proceedings of the 31st ACM Joint European | Chen Bo Calvin Zhang, AI Scale, John Hughes, Xiang Deng, Henry Sleight, et al. |  |  |  |  |  |  |  |  |  |  |  |  |
| Software Engineering Conference and Symposium on the Foundations of Software | Shade-arena: Evaluating sabotage and monitoring in llm agents. |  |  |  |  |  |  |  |  |  |  |  |  |  |

Engineering , pages 2082–2086, 2023.

---

## Page 11

On the Surprising Efficacy of LLMs for Penetration-Testing

| [57] | Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, and Jennifer Neville. Llms get | [81] | Ani Petrosyan. | Annual share of organizations affected by ransomware at- |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lost in multi-turn conversation. | arXiv preprint arXiv:2505.06120 | , 2025. | tacks worldwide from 2018 to 2023. https://www.statista.com/statistics/204457/ |  |  |  |  |  |  |  |
| [58] | Ken Lebedev, Alex Moix, and Jacob Klein. | Operating multi-client influ- | businesses-ransomware-attack-rate/, November 2024. Accessed: 2025-06-13. |  |  |  |  |  |  |  |
| ence networks across platforms. https://cdn.sanity.io/files/4zrzovbb/website/ | [82] | Ivo Petrov, Jasper Dekoninck, Lyuben Baltadzhiev, Maria Drencheva, Kristian |  |  |  |  |  |  |  |  |
| 45bc6adf039848841ed9e47051fb1209d6bb2b26.pdf, April 2025. Accessed: 2025- | Minchev, Mislav Balunović, Nikola Jovanović, and Martin Vechev. Proof or bluff? |  |  |  |  |  |  |  |  |  |
| 06-19. | evaluating llms on 2025 usa math olympiad. | arXiv preprint arXiv:2503.21934 | , |  |  |  |  |  |  |  |
| [59] | Jinhyuk Lee, Anthony Chen, Zhuyun Dai, Dheeru Dua, Devendra Singh Sachan, | 2025. |  |  |  |  |  |  |  |  |
| Michael Boratko, Yi Luan, Sébastien M. R. Arnold, Vincent Perot, Siddharth | [83] | Derry Pratama, Naufal Suryanto, Andro Aprila Adiputra, Thi-Thu-Huong Le, |  |  |  |  |  |  |  |  |
| Dalmia, Hexiang Hu, Xudong Lin, Panupong Pasupat, Aida Amini, Jeremy R. | Ahmada Yusril Kadiptya, Muhammad Iqbal, and Howon Kim. Cipher: Cyberse- |  |  |  |  |  |  |  |  |  |
| Cole, Sebastian Riedel, Iftekhar Naim, Ming-Wei Chang, and Kelvin Guu. Can | curity intelligent penetration-testing helper for ethical researcher. | Sensors | , 24 |  |  |  |  |  |  |  |
| long-context language models subsume retrieval, rag, sql, and more?, 2024. URL | (21):6878, 2024. |  |  |  |  |  |  |  |  |  |
| https://arxiv.org/abs/2406.13121. | [84] | Thomas Ptacek. My ai skeptic friends are all nuts. https://fly.io/blog/youre-all- |  |  |  |  |  |  |  |  |
| [60] | Glyph Lefkowitz. I think i’m done thinking about genai for now. https://blog. | nuts/, June 2025. Accessed: 2025-06-29. |  |  |  |  |  |  |  |  |
| glyph.im/2025/06/i-think-im-done-thinking-about-genai-for-now.html, June | [85] | William G. Resh, Yi Ming, Xinyao Xia, Michael Overton, Gul Nisa Gürbüz, and |  |  |  |  |  |  |  |  |
| 2025. Accessed: 2025-06-29. | Brandon De Breuhl. Complementarity, augmentation, or substitutivity? the |  |  |  |  |  |  |  |  |  |
| [61] | Xiaomin Li, Zhou Yu, Zhiwei Zhang, Xupeng Chen, Ziji Zhang, Yingying | impact of generative artificial intelligence on the u.s. federal workforce, 2025. |  |  |  |  |  |  |  |  |
| Zhuang, Narayanan Sadagopan, and Anurag Beniwal. When thinking fails: | URL https://arxiv.org/abs/2503.09637. |  |  |  |  |  |  |  |  |  |
| The pitfalls of reasoning for instruction-following in llms. | arXiv preprint | [86] | Christian Schindler and Andreas Rausch. Llm-based design pattern detection, |  |  |  |  |  |  |  |
| arXiv:2505.11423 | , 2025. | 2025. URL https://arxiv.org/abs/2502.18458. |  |  |  |  |  |  |  |  |
| [62] | Zilong Lin, Jian Cui, Xiaojing Liao, and XiaoFeng Wang. Malla: Demystifying | [87] | Saskia Laura Schröer, Giovanni Apruzzese, Soheil Human, Pavel Laskov, |  |  |  |  |  |  |  |
| real-world large language model integrated malicious services. In | 33rd USENIX | Hyrum S. Anderson, Edward W. N. Bernroider, Aurore Fass, Ben Nassi, Vera Rim- |  |  |  |  |  |  |  |  |
| Security Symposium (USENIX Security 24) | , pages 4693–4710, 2024. | mer, Fabio Roli, Samer Salam, Chi En Ashley Shen, Ali Sunyaev, Tim Wadhwa- |  |  |  |  |  |  |  |  |
| [63] | Dongge Liu, Jonathan Metzman, and Oliver Chang. | Ai-powered fuzzing: | Brown, Isabel Wagner, and Gang Wang. Sok: On the offensive potential of ai. |  |  |  |  |  |  |  |
| Breaking the bug hunting barrier. https://security.googleblog.com/2023/08/ai- | In | 2025 IEEE Conference on Secure and Trustworthy Machine Learning (SaTML) | , |  |  |  |  |  |  |  |
| powered-fuzzing-breaking-bug-hunting.html, August 2023. Accessed: 2025-06- | pages 247–280, 2025. doi: 10.1109/SaTML64287.2025.00021. |  |  |  |  |  |  |  |  |  |
| 19. | [88] | Minghao Shao, Boyuan Chen, Sofija Jancheska, Brendan Dolan-Gavitt, Sid- |  |  |  |  |  |  |  |  |
| [64] | Kamil˙ | e Lukoši¯ | ut˙ | e and Adam Swanda. Llm cyber evaluations don’t capture | dharth Garg, Ramesh Karri, and Muhammad Shafique. | An empirical eval- |  |  |  |  |
| real-world risk, 2025. URL https://arxiv.org/abs/2502.00072. | uation of llms for solving offensive security challenges, 2024. | URL https: |  |  |  |  |  |  |  |  |
| [65] | Amir Lupovici. The dual-use security dilemma and the social construction of | //arxiv.org/abs/2402.11814. |  |  |  |  |  |  |  |  |
| insecurity. | Contemporary Security Policy | , 42(3):257–285, 2021. | [89] | Yijia Shao, Humishka Zope, Yucheng Jiang, Jiaxin Pei, David Nguyen, Erik |  |  |  |  |  |  |
| [66] | Aengus Lynch, Benjamin Wright, Caleb Larson, Kevin K. Troy, Stuart J. | Brynjolfsson, and Diyi Yang. Future of work with ai agents: Auditing automation |  |  |  |  |  |  |  |  |
| Ritchie, Sören Mindermann, Ethan Perez, and Evan Hubinger. Agentic mis- | and augmentation potential across the u.s. workforce, 2025. URL https://arxiv. |  |  |  |  |  |  |  |  |  |
| alignment: How llms could be an insider threat. | Anthropic Research | , 2025. | org/abs/2506.06576. |  |  |  |  |  |  |  |
| https://www.anthropic.com/research/agentic-misalignment. | [90] | Parshin Shojaee, Iman Mirzadeh, Keivan Alizadeh, Maxwell Horton, Samy |  |  |  |  |  |  |  |  |
| [67] | Pratyush Maini, Hengrui Jia, Nicolas Papernot, and Adam Dziedzic. Llm dataset | Bengio, and Mehrdad Farajtabar. The illusion of thinking: Understanding the |  |  |  |  |  |  |  |  |
| inference: Did you train on my dataset? | Advances in Neural Information Pro- | strengths and limitations of reasoning models via the lens of problem complexity. |  |  |  |  |  |  |  |  |
| cessing Systems | , 37:124069–124092, 2024. | arXiv preprint arXiv:2506.06941 | , 2025. |  |  |  |  |  |  |  |
| [68] | Andy Masley. Why using chatgpt is not bad for the environment - a cheat | [91] | Brian Singer, Keane Lucas, Lakshmi Adiga, Meghna Jain, Lujo Bauer, and Vyas |  |  |  |  |  |  |  |
| sheet. https://andymasley.substack.com/p/a-cheat-sheet-for-conversations- | Sekar. On the feasibility of using llms to execute multistage network attacks. |  |  |  |  |  |  |  |  |  |
| about, April 2025. Accessed: 2025-06-23. | arXiv preprint arXiv:2501.16466 | , 2025. |  |  |  |  |  |  |  |  |
| [69] | Harindra S. Mavikumbure, Victor Cobilean, Chathurika S. Wickramasinghe, | [92] | Robin Sommer and Vern Paxson. Outside the closed world: On using machine |  |  |  |  |  |  |  |
| Devin Drake, and Milos Manic. Generative ai in cyber security of cyber physical | learning for network intrusion detection. In | 2010 IEEE symposium on security |  |  |  |  |  |  |  |  |
| systems: Benefits and threats. In | 2024 16th International Conference on Human | and privacy | , pages 305–316. IEEE, 2010. |  |  |  |  |  |  |  |
| System Interaction (HSI) | , pages 1–8, 2024. doi: 10.1109/HSI61632.2024.10613562. | [93] | Rao Surapaneni, Miku Jha, Michael Vakoc, and Todd Segal. Announcing the |  |  |  |  |  |  |  |
| [70] | Meta. Llama prompt guard 2. https://www.llama.com/docs/model-cards-and- | agent2agent protocol (a2a). https://developers.googleblog.com/en/a2a-a-new- |  |  |  |  |  |  |  |  |
| prompt-formats/prompt-guard/, January 2025. Accessed: 2025-06-21. | era-of-agent-interoperability/, April 2025. Accessed: 2025-06-02. |  |  |  |  |  |  |  |  |  |
| [71] | Suvir Mirchandani, Fei Xia, Pete Florence, Brian Ichter, Danny Driess, Montser- | [94] | Amir Taubenfeld, Yaniv Dover, Roi Reichart, and Ariel Goldstein. Systematic |  |  |  |  |  |  |  |
| rat Gonzalez Arenas, Kanishka Rao, Dorsa Sadigh, and Andy Zeng. | Large | biases in llm simulations of debates. | arXiv preprint arXiv:2402.04049 | , 2024. |  |  |  |  |  |  |
| language models as general pattern machines, 2023. URL https://arxiv.org/abs/ | [95] | Big Sleep Team. From naptime to big sleep: Using large language models to catch |  |  |  |  |  |  |  |  |
| 2307.04721. | vulnerabilities in real-world code. https://googleprojectzero.blogspot.com/2024/ |  |  |  |  |  |  |  |  |  |
| [72] | Yisroel Mirsky, Ambra Demontis, Jaidip Kotak, Ram Shankar, Deng Gelei, Liu | 10/from-naptime-to-big-sleep.html, November 2024. Accessed: 2025-06-19. |  |  |  |  |  |  |  |  |
| Yang, Xiangyu Zhang, Maura Pintor, Wenke Lee, Yuval Elovici, et al. The threat | [96] | The New York Times. Can you choose an a.i. model that harms the planet |  |  |  |  |  |  |  |  |
| of offensive ai to organizations. | Computers & Security | , 124:103006, 2023. | less? | https://www.nytimes.com/2025/06/19/climate/ai-emissions-chatbot- |  |  |  |  |  |  |
| [73] | Steve Morgan. Global ransomware damage costs predicted to exceed $275 billion | accuracy.html, June 2025. Accessed: 2025-06-21. |  |  |  |  |  |  |  |  |
| by 2031. https://cybersecurityventures.com/global-ransomware-damage-costs- | [97] | Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne |  |  |  |  |  |  |  |  |
| predicted-to-reach-250-billion-usd-by-2031/, April 2025. Accessed: 2025-06-02. | Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal |  |  |  |  |  |  |  |  |  |
| [74] | Farzad Nourmohammadzadeh Motlagh, Mehrdad Hajizadeh, Mehryar Majd, | Azhar, et al. Llama: Open and efficient foundation language models. | arXiv |  |  |  |  |  |  |  |
| Pejman Najafi, Feng Cheng, and Christoph Meinel. Large language models in | preprint arXiv:2302.13971 | , 2023. |  |  |  |  |  |  |  |  |
| cybersecurity: State-of-the-art, 2024. URL https://arxiv.org/abs/2402.00891. | [98] | Valen Van. A new evolutionary law. | Evolutionary theory | , 1:1, 1973. |  |  |  |  |  |  |
| [75] | Ben Nimmo and Michael Flossman. Influence and cyber operations: an up- | [99] | Vernor Vinge. | Rainbows End: A Novel With One Foot In The Future | . Tor Books, |  |  |  |  |  |
| date. https://cdn.openai.com/threat-intelligence-reports/influence-and-cyber- | 2007. |  |  |  |  |  |  |  |  |  |
| operations-an-update_October-2024.pdf, October 2024. Accessed: 2025-06-13. | [100] | Yixin Wan, George Pu, Jiao Sun, Aparna Garimella, Kai-Wei Chang, and Nanyun |  |  |  |  |  |  |  |  |
| [76] | Ben Nimmo, Albert Zhang, Sophia Farquhar, and Kimo Murphy, Max Bu- | Peng. " kelly is a warm person, joseph is a role model": Gender biases in llm- |  |  |  |  |  |  |  |  |
| manglag. Disrupting malicious uses of ai: June 2025. https://openai.com/global- | generated reference letters. | arXiv preprint arXiv:2310.09219 | , 2023. |  |  |  |  |  |  |  |
| affairs/disrupting-malicious-uses-of-ai-june-2025/, June 2025. Accessed: 2025- | [101] | Li Wang, Xi Chen, XiangWen Deng, Hao Wen, MingKe You, WeiZhi Liu, Qi Li, |  |  |  |  |  |  |  |  |
| 06-13. | and Jian Li. Prompt engineering in consistency and reliability with the evidence- |  |  |  |  |  |  |  |  |  |
| [77] | Ben Nimmo, Albert Zhang, Matthew Richard, and Nathaniel Hartley. Disrupting | based guideline for llms. | NPJ digital medicine | , 7(1):41, 2024. |  |  |  |  |  |  |
| malicious uses of ai: February 2025. https://cdn.openai.com/threat-intelligence- | [102] | Yifei Wang. The large language model (llm) paradox: Job creation and loss in |  |  |  |  |  |  |  |  |
| reports/disrupting-malicious-uses-of-our-models-february-2025-update.pdf, | the age of advanced ai. | Authorea Preprints | , 2023. |  |  |  |  |  |  |  |
| February 2025. Accessed: 2025-06-18. | [103] | Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, |  |  |  |  |  |  |  |  |
| [78] | OpenAI. Introducting chatgpt. https://openai.com/index/chatgpt/, November | Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning |  |  |  |  |  |  |  |  |
| 2022. Accessed: 2025-06-02. | in large language models. | Advances in neural information processing systems | , |  |  |  |  |  |  |  |
| [79] | OpenAI. Introducing openai o1. https://openai.com/o1/, September 2024. Ac- | 35:24824–24837, 2022. |  |  |  |  |  |  |  |  |
| cessed: 2025-06-02. | [104] | WhiteRabbitNeo. Whiterabbitneo. https://huggingface.co/WhiteRabbitNeo, |  |  |  |  |  |  |  |  |
| [80] | OpenAI. | Disrupting | malicious | uses | of | ai | by | state-affiliated | threat | February 2024. Accessed: 2025-06-02. |
| actors. | https://openai.com/index/disrupting-malicious-uses-of-ai-by-state- | [105] | Simon Willison. Coding agents. https://simonwillison.net/2025/Jun/18/coding- |  |  |  |  |  |  |  |
| affiliated-threat-actors/, February 2024. Accessed: 2025-06-19. | agents/, June 2025. Accessed: 2025-06-21. |  |  |  |  |  |  |  |  |  |

---

## Page 12

Andreas Happe and Jürgen Cito

| [106] | Simon Willison. The lethal trifecta for ai agents: private data, untrusted content, | air-canada-chatbot-misinformation-what-travellers-should-know, February |  |  |
| --- | --- | --- | --- | --- |
| and external communication. https://simonwillison.net/2025/Jun/16/the-lethal- | 2024. Accessed: 2025-06-21. |  |  |  |
| trifecta/, June 2025. Accessed: 2025-06-21. | [112] | Fanjia Yan, Huanzhi Mao, Charlie Cheng-Jie Ji, Tianjun Zhang, Shishir G. |  |  |
| [107] | Hanxiang Xu, Shenao Wang, Ningke Li, Kailong Wang, Yanjie Zhao, Kai Chen, | Patil, Ion Stoica, and Joseph E. Gonzalez. | Berkeley function calling |  |
| Ting Yu, Yang Liu, and Haoyu Wang. Large language models for cyber security: | leaderboard. https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_ |  |  |  |
| A systematic literature review, 2024. URL https://arxiv.org/abs/2405.04760. | leaderboard.html, 2024. |  |  |  |
| [108] | Jiacen Xu, Jack W Stokes, Geoff McDonald, Xuesong Bai, David Marshall, Siyue | [113] | Yifan Yao, Jinhao Duan, Kaidi Xu, Yuanfang Cai, Zhibo Sun, and Yue Zhang. A |  |
| Wang, Adith Swaminathan, and Zhou Li. | Autoattacker: A large language | survey on large language model (llm) security and privacy: The good, the bad, |  |  |
| model guided system to implement automatic cyber-attacks. | arXiv preprint | and the ugly. | High-Confidence Computing | , 4(2):100211, 2024. ISSN 2667-2952. |
| arXiv:2403.01038 | , 2024. | doi: https://doi.org/10.1016/j.hcc.2024.100211. URL https://www.sciencedirect. |  |  |
| [109] | Rongwu Xu, Xiaojian Li, Shuo Chen, and Wei Xu. Nuclear deployed: Analyzing | com/science/article/pii/S266729522400014X. |  |  |
| catastrophic risks in decision-making of autonomous llm agents, 2025. URL | [114] | Yagmur Yigit, William J Buchanan, Madjid G Tehrani, and Leandros Maglaras. |  |  |
| https://arxiv.org/abs/2502.11355. | Review of generative ai methods in cybersecurity, 2024. URL https://arxiv.org/ |  |  |  |
| [110] | Wen Xu, Juanru Li, Junliang Shu, Wenbo Yang, Tianyi Xie, Yuanyuan Zhang, | abs/2403.08701. |  |  |
| and Dawu Gu. From collision to exploitation: Unleashing use-after-free vulner- | [115] | Jie Zhang, Haoyu Bu, Hui Wen, Yu Chen, Lun Li, and Hongsong Zhu. When |  |  |
| abilities in linux kernel. In | Proceedings of the 22nd ACM SIGSAC Conference on | llms meet cybersecurity: A systematic literature review, 2024. | URL https: |  |
| Computer and Communications Security | , pages 414–425, 2015. | //arxiv.org/abs/2405.03644. |  |  |
| [111] | Maria Yagoda. Airline held liable for its chatbot giving passenger bad advice - | [116] | Yifei Zhou, Sergey Levine, Jason Weston, Xian Li, and Sainbayar Sukhbaatar. |  |
| what this means for travellers. https://www.bbc.com/travel/article/20240222- | Self-challenging language model agents. | arXiv preprint arXiv:2506.01716 | , 2025. |  |
