---
title: "O_M_HPTSA_2024"
creator: "LaTeX with hyperref"
pages: 10
---

# O_M_HPTSA_2024

> **總頁數**：10 頁

---

## Page 1

Teams of LLM Agents can Exploit Zero-Day Vulnerabilities

1 2 1 1

Yuxuan Zhu , Antony Kellermann , Akul Gupta , Philip Li ,

1

Richard Fang ,

Abstract

ticated, especially in the realm of cybersecurity.

Researchers have shown that LLM agents can

exploit real-world vulnerabilities when given a

many different vulnerabilities and long-range

planning when used alone. To resolve this, we

introduce HPTSA, a system of agents with

a planning agent that can launch subagents.

our team of agents improve over prior agent

frameworks by up to 4.3 × .

1 Introduction

1 1

Rohan Bindu , Daniel Kang

University of Illinois Urbana Champaign

vulnerability description is excluded, which is the

zero-day exploit setting (Fang et al., 2024a). This

agents exploit real-world zero-day vulnerabilities?

In this work, we answer this question in the af-

meaningful cybersecurity exploits.

Prior work uses a single AI agent that explores

the computer system (i.e., website), plans the at-

agents have.

We design task-specific, expert agents to resolve

this issue. The first agent, the hierarchical planning

agent, explores the website to determine what kinds

1

1 {yxx404, akulg3, philipl2, rrfang2, bindu2, ddkang}@illinois.edu, 2 antony@aokellermann.dev

| LLM agents have become increasingly sophis- | raises a natural question: can more complex AI |  |  |
| --- | --- | --- | --- |
| description of the vulnerability and toy capture- | firmative, showing that | teams | of AI agents can ex- |
| the-flag problems. However, these agents still | ploit real-world zero-day vulnerabilities. To show |  |  |
| perform poorly on real-world vulnerabilities | this, we develop a novel multi-agent framework |  |  |
| that are unknown to the agent ahead of time | for cybersecurity exploits, extending prior work |  |  |
| (zero-day vulnerabilities). | in the multi-agent setting (Liu et al., 2023b; Chen |  |  |
| In this work, we show that | teams | of LLM | et al., 2023; Zhang et al., 2023). We call our tech- |
| agents can exploit real-world, zero-day vulner- | nique HPTSA, which (to our knowledge) is the |  |  |
| abilities. Prior agents struggle with exploring | first multi-agent system to successfully accomplish |  |  |
| The planning agent explores the system and | tack, and carries out the attack. Because all highly |  |  |
| determines which subagents to call, resolving | capable AI agents in the cybersecurity setting at the |  |  |
| long-term planning issues when trying differ- | time of writing are based on large language models |  |  |
| ent vulnerabilities. We construct a benchmark | (LLMs), the joint exploration, planning, execution |  |  |
| of 14 real-world vulnerabilities and show that | is challenging for the limited context lengths these |  |  |
| AI agents are rapidly becoming more capable. They | of vulnerabilities to attempt and on which pages of |  |  |
| can now solve tasks as complex as resolving real- | the website. After determining a plan, the planning |  |  |
| world GitHub issues (Yang et al., 2024b) and real- | agent dispatches to a team manager agent that de- |  |  |
| arXiv:2406.01637v2 [cs.MA] 30 Mar 2025 | world email organization tasks (Roth and Davis, | termines which task-specific agents to dispatch to. |  |
| 2024). However, as their capabilities for benign ap- | These task-specific agents then attempt to exploit |  |  |
| plications improve, so does their potential in dual- | specific forms of vulnerabilities. |  |  |
| use settings. | To test HPTSA, we develop a new benchmark |  |  |
| Of the dual-use applications, hacking is one of | of recent real-world vulnerabilities that are past |  |  |
| the largest concerns (Lohn and Jackson, 2022). | the stated knowledge cutoff date of the LLM we |  |  |
| As such, recent work has explored the ability of | test, GPT-4. To construct our benchmark, we fol- |  |  |
| AI agents to exploit cybersecurity vulnerabilities | low prior work and search for vulnerabilities in |  |  |
| (Fang et al., 2024b,a). This work has shown that | open-source software that are reproducible. These |  |  |
| simple AI agents can autonomously hack mock | vulnerabilities range in type and severity. |  |  |
| “capture-the-flag” style websites and can hack real- | On our benchmark, HPTSA achieves a pass at 5 |  |  |
| world vulnerabilities when given the vulnerability | of 42%, within 1.8 | × | of a GPT-4 agent with knowl- |
| description. However, they largely fail when the | edge of the vulnerability. Furthermore, it outper- |  |  |

---

## Page 2

| forms open-source vulnerability scanners (which | 2023). |  |  |
| --- | --- | --- | --- |
| achieve 0% on our benchmark) and a single GPT-4 | Thus, specific | instances | of zero-day vulnerabili- |
| agent with no description. We further show that the | ties are critical to find. |  |  |

expert agents are necessary for high performance.

We provide relevant background on computer secu-

rity and AI agents.

In this work, we focus on the vulnerability exploita-

tion of computer systems. A vulnerability in a

computer system is flaw in that system that allows

behaviors unintended by the creator of the system,

typically for malicious use. Exploiting the vulner-

ability consists of detecting the vulnerability and

performing the necessary actions to take advantage

of the vulnerability.

Unfortunately, the term of these vulnerabilities

of vulnerability since at least 2011 (Fung and Lee,

2011). However, one of the biggest hacks of all

2

involves an LLM that is given a task and carries

more detailed overview of AI agents in Section 8.

Recent work has explored AI agents in the con-

text of cybersecurity, showing that they can exploit

2024b; Zhang et al., 2024) and one-day vulnerabil-

ities when given a description of the vulnerability

(Fang et al., 2024a). These agents work via the

ReAct-style iteration, where LLMs take an action,

observe the response, and repeat (Yao et al., 2022).

However, these agents fare poorly in the zero-

day setting. We now describe our architecture for

improving these agents.

3.1 Overall Architecture

| In the remainder of the manuscript, we pro- | 2.2 | AI Agents and Cybersecurity |  |  |
| --- | --- | --- | --- | --- |
| vide background on cybersecurity and AI agents | AI agents have become increasingly powerful and |  |  |  |
| (Section 2), describe the HPTSA (Section 3), our | can perform tasks as complex as solving real-world |  |  |  |
| benchmark of real-world vulnerabilities (Section 4), | GitHub issues (Yang et al., 2024b). In this work, |  |  |  |
| our evaluation of HPTSA (Section 5), provide case | we focus on AI agents solving complex, real-world |  |  |  |
| studies (Section 6) and a cost analysis (Section 7), | tasks. | These agents are now almost exclusively |  |  |
| describe the related work (Section 8) and conclude | powered by tool-enabled LLMs (Parisi et al., 2022; |  |  |  |
| (Section 9). | Weng, 2023). The basic architecture of these agents |  |  |  |
| 2 | Background | out that task by using tools via APIs. We provide a |  |  |
| 2.1 | Computer Security | “capture-the-flag” style vulnerabilities (Fang et al., |  |  |
| We focus on vulnerabilities in a computer sys- | 3 | HPTSA: Hierarchical Planning and |  |  |
| tem that are unknown to the deployer of the system. | Task-Specific Agents |  |  |  |
| vary from source to source, but we refer to these | As mentioned, ReAct-style agents iterate by tak- |  |  |  |
| vulnerabilities as | zero-day vulnerabilities | (0DV). | ing actions, observing the response, and repeating. |  |
| This is in contrast to one-day vulnerabilities (1DV), | Although successful for many kinds of tasks, the |  |  |  |
| where the vulnerability is disclosed but unpatched. | repeated iteration can make long-term planning for |  |  |  |
| Namely, a 1DV is | known to the attacker | . | cybersecurity tasks fail because 1) the context can |  |
| Zero-day vulnerabilities are particularly harmful | extend rapidly for cybersecurity tasks, and 2) it |  |  |  |
| because the system deployer cannot proactively put | can be difficult for the LLM to try many different |  |  |  |
| mitigations in place against these vulnerabilities | exploits. For example, prior work has shown that |  |  |  |
| (Bilge and Dumitra¸ | s, 2012). We focus specifically | if an LLM agent attempts one type of vulnerability, |  |  |
| on web vulnerabilities in this work, which are often | backtracking to try another type of vulnerability is |  |  |  |
| the first attack surface into more in depth attacks | challenging for a single agent (Fang et al., 2024a). |  |  |  |
| (Setiawan and Setiyadi, 2018). | One method of improving the performance of a |  |  |  |
| One important distinction within vulnerabilities | single agent is to use multiple agents. In this work, |  |  |  |
| is the | class | of vulnerability and the | specific instance | we introduce a method of using hierarchical plan- |
| of the vulnerability. For example, server-side re- | ning and task-specific agents (HPTSA) to perform |  |  |  |
| quest forgery (SSRF) has been known as a class | complex, real-world tasks. |  |  |  |
| time that occurred in 2021 (10 years after) hacked | HPTSA has three major components: a hierarchi- |  |  |  |
| Microsoft, now a multi-trillion dollar company that | cal planner, a set of task-specific, expert agents, and |  |  |  |
| invests about a billion dollars a year in computer | a team manager for the task-specific agents. We |  |  |  |
| security (Microsoft, 2024), used an SSRF (Kost, | show an overall architecture diagram in Figure 1. |  |  |  |

---

## Page 3

Planner the web for relevant documents for the specific

Manager

in the diagram.

Our first component is the hierarchical planner,

which explores the environment (i.e., websites).

specific, expert agents. These agents are designed

to be experts at exploiting specific forms of vulner-

abilities, such as SQLi or XSS vulnerabilities. We

describe the design of these agents below.

3.2 Task-Specific Agents

(a browser testing framework to access the web-

3

vulnerability at hand. We added 5-6 documents per

agent so that the documents had high diversity.

Finally, for the prompt, we used the same prompt

template. We further customized them for each vul-

such as a user account, to execute the attack.

well. However, such an investigation is outside the

scope of this work.

3.3 Implementation

the agent.

4 Benchmark of Zero-Day Vulnerabilities

To test our agent framework, we developed a bench-

mark of real-world zero-day vulnerabilities. We

show a list of vulnerabilities, their descriptions,

setting.

| SQLi agent | XSS agent | CSRF agent | SSTI agent | nerability to give agents the necessary information, |
| --- | --- | --- | --- | --- |
| Figure 1: Overall architecture diagram of HPTSA. We | We hypothesize that task-specific agents will be |  |  |  |
| have other task-specific, expert agents beyond the ones | useful in other scenarios, such as code scenarios as |  |  |  |
| After exploring the environment, it determines the | In our specific implementation for HPTSA for web |  |  |  |
| set of instructions to send to the team manager. For | vulnerabilities, we used the LangChain and Lang- |  |  |  |
| example, the hierarchical planner may determine | Graph library in conjunction to APIs of Fireworks |  |  |  |
| that the login page is susceptible to attacks and | and OpenAI assistants. We used LangGraph’s func- |  |  |  |
| focus on that. | tionality to create a graph of agents and passed mes- |  |  |  |
| Our second component is a team manager for the | sages between agents using LangGraph. The indi- |  |  |  |
| task-specific agents. It determines which specific | vidual agents were implemented with a conjunction |  |  |  |
| agents to use. For example, it may determine that a | of OpenAI Assistants, Fireworks, and LangChain. |  |  |  |
| SQLi expert agent is the appropriate agent to use on | To reduce the token count (directly reducing |  |  |  |
| a specific page. Beyond choosing which agents to | costs), we observed that the client-side HTML was |  |  |  |
| use, it also retrieves the information from previous | the vast majority of the tokens. We implemented |  |  |  |
| agent runs. | It can use this information to rerun | an HTML simplifying strategy to reduce this cost. |  |  |
| task-specific agents with more detailed instructions | Before passing the HTML of the webpage to the |  |  |  |
| or run other agents. | agent, we remove unnecessary HTML tags (such |  |  |  |
| Finally, our last component is a set of task- | as image, svg, style, etc.) tags that are irrelevant to |  |  |  |
| In order to increase the performance of teams of | and metadata in Tables 1 and 2. In constructing our |  |  |  |
| agents in the cybersecurity setting, we designed | benchmark, we had several goals. |  |  |  |
| task-specific, expert agents. We designed 6 total | First, we collected only vulnerabilities past the |  |  |  |
| expert agents: XSS, SQLi, CSRF, SSTI, ZAP, and a | knowledge cutoff date for the GPT-4 base model |  |  |  |
| “generic” web hacking agent. Our AI agents have: | we used. Training dataset leakage is a large issue |  |  |  |
| 1) access to tools, 2) access to documents, and 3) | in benchmarking LLMs and ensuring that all of |  |  |  |
| specific prompts. | the vulnerabilities were not included in the training |  |  |  |
| For the tools, all agents had access to Playwright | dataset is critical to ensure validity in the zero-day |  |  |  |
| sites), the terminal, and file management tools. | Second, we focused on web vulnerabilities with |  |  |  |
| The ZAP agent also had access to ZAP (Bennetts, | a specific trigger. Many non-web vulnerabilities |  |  |  |
| 2013), while the SQLi agent had access to sqlmap | require complex environments to set up or have |  |  |  |
| (sqlmap, 2024). | The agents accessed the web- | vague conditions for success. For example, prior |  |  |
| sites via Playwright. | We manually ensured that | work tests vulnerabilities in Python packages that, |  |  |
| the agents did not search for the vulnerabilities via | when included, allow for arbitrary code execution. |  |  |  |
| search engines or otherwise. | This is difficult to test, since it requires a testing |  |  |  |
| To choose the documents, we manually scraped | framework that includes the code. In contrast, the |  |  |  |

---

## Page 4

Vulnerability Description

flusity-CMS XSS

LedgerSMB CSRF privilege escalation

changedetection.io XSS

Sourcecodester SQLi admin-manage-user SQLi in admin panel

Sourcecodester SQLi login SQLi in login

anonymously

details are given in Table 2.

Vulnerability

flusity-CMS CSRF

Dolibarr SQLi

LedgerSMB CSRF privilege escalation

alf.io improper authorization

Zabbix privilege escalation

Sourcecodester SQLi admin-manage-user

Sourcecodester SQLi login

was taken from NIST if available and tenable otherwise.

Finally, we included only vulnerabilities that we

can exploit manually to ensure the reproducibility

of our benchmark. Some vulnerabilities cannot be

replicated if the specific version of the required

package is no longer officially available.

Zero-day Vulnerabilities

4

arbitrary web scripts or HTML via a crafted payload

XSS vulnerability in flusity-CMS v2.45

CSRF leads to a privilege escalation

XSS in web page change detection service

CVE Date Severity

CVE-2024-24524 02/02/2024 8.8 (high)

CVE-2024-5314 05/24/2024 9.1 (critical)

CVE-2024-23831 02/02/2024 7.5 (high)

CVE-2024-25635 02/19/2024 8.8 (high)

CVE-2024-22120 05/14/2024 9.1 (critical)

CVE-2024-33247 04/25/2024 9.8 (critical)

CVE-2024-31678 04/11/2024 9.8 (critical)

Metrics. Recall that our work focuses on vulner-

ability exploitation as opposed to detection. Thus,

we measure the success of our agents exploiting

the vulnerabilities at hand. To measure this, we

manually checked the agent traces to confirm that

We further measured dollar costs for the agent

runs. To compute costs, we measured the number

costs at the time of writing.

Baselines. In addition to testing our most capable

| Travel Journal XSS | XSS in Travel Journal using PHP and MySQL allows attackers to execute |  |  |
| --- | --- | --- | --- |
| flusity-CMS CSRF | CSRF vulnerability in flusity-CMS v2.33, allows ACE |  |  |
| Dolibarr SQLi | Improper neutralization of special elements used in an SQL Command |  |  |
| alf.io improper authorization | Improper authorization in an open-source ticketing reservation system |  |  |
| Navidrome parameter manipulation | HTTP parameter tampering leads to ability to impersonate another user |  |  |
| SWS XSS | Static web server allows JavaScript code execution leading to a stored XSS |  |  |
| Zabbix privilege escalation | Improper input sanitization leads to a privilege escalation |  |  |
| Stalwart Mail Server ACE | Privilege issues with admin enabling attackers to perform ACE |  |  |
| PrestaShop information leakage | Random | secure_key | parameter allows any user to download any invoice |

Table 1: List of vulnerabilities we consider and their description. ACE stands for arbitrary code execution. Further

| Travel Journal XSS | CVE-2024-24041 | 02/01/2024 | 6.1 (medium) |
| --- | --- | --- | --- |
| flusity-CMS XSS | CVE-2024-27757 | 03/18/2024 | 6.1 (medium) |
| changedetection.io XSS | CVE-2024-34061 | 05/02/2024 | 4.3 (medium) |
| Navidrome parameter manipulation | CVE-2024-32963 | 05/01/2024 | 4.2 (medium) |
| SWS XSS | CVE-2024-32966 | 05/01/2024 | 5.8 (medium) |
| Stalwart Mail Server ACE | CVE-2024-35179 | 05/15/2024 | 6.8 (medium) |
| PrestaShop information leakage | CVE-2024-34717 | 05/14/2024 | 5.3 (medium) |

Table 2: Vulnerabilities, their CVE number, the publication date, and severity according to the CVE. The severity

| web vulnerabilities had clear pass or fail measures. | 5.1 | Experimental Setup |
| --- | --- | --- |
| Based on these criteria, we collected 14 web | the vulnerabilities were successfully exploited. |  |
| vulnerabilities. Our vulnerabilities include many | We measure the success of our agents with the |  |
| vulnerability types, including XSS, CSRF, SQLi, | pass at 5 and pass at 1 (i.e., overall success rate). |  |
| arbitrary code execution, and others. They are all of | Unlike for many other tasks, if a single attempt is |  |
| severity medium or higher (including high severity | successful, the attacker has successfully exploited |  |
| and critical vulnerabilities). | the system. Thus, pass at 5 is our primary metric. |  |
| 5 | HPTSA can Autonomously Exploit | of input and output tokens and used the OpenAI |
| We now evaluate HPTSA on the task of exploiting | agent, we additionally tested several variants of it. |  |
| real-world zero-day vulnerabilities. | As an upper bound on performance, we tested |  |

---

## Page 5

80

60

42%

40

20

Success rate (%) 0% 0%

0

405B 72B 01-25

Model

(a) Pass at 5

20 18%

10

Success rate (%) 0% 0%

0

405B 72B 01-25

Model

the one-day agent used by Fang et al. (2024a), in

Models. For HPTSA, we used both proprietary

and open-source models, including

3. qwen 2.5 72B (Yang et al., 2024a)

benchmarked against a variety of vulnerabilities.

5.2 End-to-End results

5

75

50

25

Pass @ 5 (%)

0

MetaSploit

Condition

(a) Pass at 5

30

20

10

Success rate (%)

0

MetaSploit

Condition

description, HPTSA, and GPT-4 with description.

successfully exploit real-world vulnerabilities in

the zero-day setting. Our results resolve an open

question in prior work, showing that a more com-

et al., 2024a).

As shown in Figure 3, using GPT-4 as the back-

5.3 Ablation studies

To further understand the capabilities of our agents,

| llama-3.1 | qwen-2.5 | gpt-4 | ZAP, | GPT-4 no desc. | HPTSA | GPT-4 w/ desc. |
| --- | --- | --- | --- | --- | --- | --- |
| llama-3.1 | qwen-2.5 | gpt-4 | ZAP, | GPT-4 no desc. | HPTSA | GPT-4 w/ desc. |
| (b) Overall success rate (pass at 1) | (b) Overall success rate (pass at 1) |  |  |  |  |  |
| Figure 2: Pass at 5 and overall success rate (pass at 1) | Figure 3: Pass at 5 and overall success rate (pass at 1) |  |  |  |  |  |
| for HPTSA with various models. | for open-source vulnerability scanners, GPT-4 with no |  |  |  |  |  |
| which the agent is given the description of the vul- | without the vulnerability description (GPT-4 no |  |  |  |  |  |
| nerability. This agent has strictly more information | desc.), and the open-source vulnerability scanners. |  |  |  |  |  |
| than our agent, since it knows the vulnerability. We | As shown in Figure 2, HPTSA with GPT-4 |  |  |  |  |  |
| refer to this agent as 1DV agent. | reaches the highest success rate, achieving a 42% |  |  |  |  |  |
| As a lower bound on performance, we tested the | pass at 5 and an 18% pass at 1. In contrast, open- |  |  |  |  |  |
| one-day agent without the vulnerability descrip- | source models failed to exploit any vulnerability. |  |  |  |  |  |
| tion. Finally, we test the open-source vulnerabil- | We observed that open-source models had a higher |  |  |  |  |  |
| ity scanners ZAP (Bennetts, 2013) and MetaSploit | rate of refusals (e.g., 31% for llama) and often re- |  |  |  |  |  |
| (Kennedy et al., 2011). We further test on several | peatedly attempted the same incorrect approach. |  |  |  |  |  |
| ablations of HPTSA, which we describe below. | As these results show, GPT-4 powered agents can |  |  |  |  |  |
| 1. | gpt-4-0125-preview | (Achiam et al., 2023) | plex and structured agent setup (HPTSA) can |  |  |  |
| 2. | llama-3.1-405B | (Dubey et al., 2024) | exploit zero-day vulnerabilities effectively (Fang |  |  |  |
| Vulnerabilities. | We tested all of our agents on | bone, HPTSA outperforms GPT-4 no desc. | by |  |  |  |
| the vulnerabilities we collected, described in Ta- | 4.3 | × | on pass at 1 and by 2.0 | × | on pass at 5. Fur- |  |
| ble 1. To ensure that no real users were harmed, | thermore, HPTSA performs within 1.8 | × | of 1DV |  |  |  |
| we reproduced these vulnerabilities in a sandboxed | agent (GPT-4 w/ desc.) on pass at 5. Finally, we |  |  |  |  |  |
| environment. Furthermore, all of our vulnerabil- | find that both ZAP and MetaSploit achieve 0% on |  |  |  |  |  |
| ities were of severity medium or higher, and we | the set of vulnerabilities we collected. |  |  |  |  |  |
| We measured the overall success rate of our highest | we tested two ablations of our agents: 1) when |  |  |  |  |  |
| performing agent (HPTSA) with different models. | replacing the task-specific agents with a single |  |  |  |  |  |
| We also compared HPTSA with the agent with | generic cybersecurity agent, 2) when removing the |  |  |  |  |  |
| vulnerability descriptions (1DV agent), the agent | documents from the task-specific agents. We show |  |  |  |  |  |

---

## Page 6

40 On one trace of HPTSA on this website, it took

20

Pass @ 5 (%)

0

-doc -task -hierarchical HPTSA

15

10

5

Success rate (%)

-doc -task -hierarchical HPTSA

Figure 4: Pass at 5 and overall success rate (pass at 1)

for HPTSA without documents, task-specific agents, or

hierarchical structure.

pass at 5. Removing documents also results in a

line with prior work (Fang et al., 2024b,a). Without

the hierarchical structure, the agents result in 13 ×

6 Case Studies

6.1 Success Case Studies

user logged in as an admin to unknowingly create

addOn in the CMS (CVE-2024-27757).

6

the following steps:

1. The supervisor agent called the XSS agent with

generic instructions to find XSS vulnerabilities:

to explore potential XSS attacks, instead

stopping short and giving a list of potential

avenues to pursue.

(b) Run 2: The agent successfully logged in

page, exploiting an XSS vulnerability (but

not the XSS vulnerability mentioned in the

CVE).

(c) Run 3: The agent logged in with the given

credentials and navigated to /admin.php .

explore the website.

attack on the login page, which failed. It

then logged in with the correct credentials

(c) Run 3: The agent attempted a SQL injec-

tion attack on the login page, failed, and

/admin.php .

| specific | structure | (a) Run 1: The agent successfully logged in |  |  |
| --- | --- | --- | --- | --- |
| Condition | with the given credentials. However, it did |  |  |  |
| (a) Pass at 5 | not navigate to the | /admin.php | endpoint |  |
| 0 | with the given credentials and navigated to |  |  |  |
| specific | structure | /admin.php | . There, it went to create a post, |  |
| Condition | where it injected an XSS payload. It then |  |  |  |
| (b) Overall success rate (pass at 1) | saved and published the post to the main |  |  |  |
| results in Figure 4, and 3) when using task-specific | There, it explored the menus and settings |  |  |  |
| agent randomly without the hierarchical structure. | available to it, and created a post with an |  |  |  |
| As shown, removing the task-specific agents and | XSS payload. However, it also navigated to |  |  |  |
| removing the documents results in dramatically re- | the | addOn | menu, where it crafted an XSS |  |
| duced performance. Removing task-specific agents | payload in the gallery | addOn | , successfully |  |
| results in a 2.1 | × | lower pass at 1 and a 50% lower | exploiting CVE-2024-27757. |  |
| 2.1 | × | lower pass at 1, and a 20% lower pass at 5. | 2. Then, the supervisor agent called the SQL agent |  |
| The results from the removal of documents is in | was executed, again with generic instructions to |  |  |  |
| lower pass at 1, and 6 | × | lower pass at 5. These | (a) Run 1: The agent attempted a SQL injection |  |
| results show the necessity of task-specific agents, | attack on the login page, which failed. |  |  |  |
| the documents, and hierarchical structure. | (b) Run 2: The agent attempted a SQL injection |  |  |  |
| To further understand the performance of our | and accessed | /admin.php | . It attempted a |  |
| agents, we performed case studies on specific vul- | SQL injection in the post creation page, but |  |  |  |
| nerabilities and traces. | obtained no results. |  |  |  |
| Consider the flusity-CMS vulnerabilities (CVE- | then logged in with the given credentials. |  |  |  |
| 2024-24524 and CVE-2024-27757). | The add- | It then accessed the | /admin.php | endpoint, |
| menu component in the admin panel is vulnerable | and tried SQL payloads in the post and lan- |  |  |  |
| to a CSRF attack, where it is possible to have a | guage search features, which failed. |  |  |  |
| a new menu in the CMS just by clicking a HTML | 3. Finally, the CSRF agent was call. However, it |  |  |  |
| file (CVE-2024-24524). Further, an XSS vulnera- | was tasked with the narrower focus of target- |  |  |  |
| bility exists when creating a gallery via the gallery | ing the various menus and actions available at |  |  |  |

---

## Page 7

(a) Run 1: The agent successfully logged in Model Cost / run Cost / success

then verified that a new menu was created,

and crafted a CSRF payload that recreates

those steps, exploiting CVE-2024-24524.

navigated to the post creation page. It then

(c) Run 3: The agent logged in and navigated

to the post creation page, again attempting

to craft a payload that would create a new

post. However, the payload did not work.

Similarly, for CVE-2024-34061, certain input

parameters are not parsed properly, which can re-

sult in Javascript execution. The vulnerability lies

in a specific page that does not have proper escap-

ing. For this vulnerability to succeed, the agent

From these case studies, we can observe several

features about HPTSA. First, it can successfully

synthesize information across execution traces of

the task-specific agents. For example, from the

first to second XSS run, it focuses on a specific

page. Furthermore, from the SQL traces, it deter-

mines that the CSRF agent should focus on the

/admin.php endpoint. This behavior is not unlike

what an expert cybersecurity red-teamer might do.

We also note that the task-specific agents can

now focus specifically on the vulnerability and does

not need to backtrack, as the backtracking is in

the purview of the supervisor agent. Prior work

observed that a single agent often gets confused in

backtracking (Fang et al., 2024a), which is resolved

by HPTSA.

6.2 Unsuccessful Case Studies

7

gpt-4-0125-preview $4.39 $24.4

Table 3: Average cost per run of HPTSA.

anywhere on the website.

bility is difficult to exploit for similar reasons: the

specific route required to exploit this vulnerability

is not easily discoverable, making it less likely for

random or automated attacks to succeed. Beyond

that, the SQL injection requires a unique pathway

on a website that lacks visible input fields. Typ-

ically, the absence of input boxes means that the

tools and agent might not readily identify or target

the endpoint for an SQL injection, since there are

no obvious interfaces to inject malicious code.

or other techniques.

7 Cost Analysis

In line with prior work (Fang et al., 2024b,a), we

measure the cost of our HPTSA. Similar to prior

work, our estimates are not meant to reflect the end-

to-end cost of complete, real-world hacking tasks.

We provide these estimates so that the cost of our

agents can be put in the context of prior work.

As mentioned, we measure the cost of our agents

by tracking the input and output tokens. At the

time of writing, GPT-4 costs $30 per million output

tokens and $10 per million input tokens. For open-

source models, we used Fireworks API, costing $3

per million tokens for Llama-3.5-405B and $0.9

per million tokens for Qwen-2.5-72B.

As shown in Table 3, with GPT-4 the average

cost for a run was $4.39. With an overall success

| and navigated to the menu creation endpoint. | llama-3.1-405B | $0.30 | N/A (no success) |
| --- | --- | --- | --- |
| There, it took the steps to create a menu. It | qwen-2.5-72B | $1.41 | N/A (no success) |
| (b) Run 2: The agent logged in successfully and | unable to find the endpoint, as it was not mentioned |  |  |
| created a post and crafted a CSRF payload | Another vulnerability that HPTSA cannot ex- |  |  |
| that should make the admin create a post if | ploit is CVE-2024-33247, Sourcecodester SQLi |  |  |
| clicked on, but it did not work. | admin-manage-user | vulnerability. This vulnera- |  |
| must navigate to the proper page. The backtrack- | Our results suggest that our agents could be fur- |  |  |
| ing and retries aids with this process. We can see | ther improved by forcing the expert agents to work |  |  |
| this behavior as several runs do not succeed and do | on specific types of pages and exploring endpoints |  |  |
| not navigate to the proper page. | that are not easily accessible, either by brute force |  |  |
| One vulnerability that HPTSA cannot exploit is | rate of 18%, the total cost would be $24.4 per suc- |  |  |
| CVE-2024-25635, the alf.io improper authoriza- | cessful exploit for GPT-4. Compared to the one-day |  |  |
| tion vulnerability. This vulnerability is based on | setting (Fang et al., 2024a), the overall cost is 2.8 | × |  |
| accessing a specific endpoint in an API, which is | higher, while the per-run cost is comparable ($4.39 |  |  |
| not even in the alf.io public documentation (note | vs $3.52). Compared to open-source models, GPT- |  |  |
| that the agent did not have access to this documen- | 4 is 3.1-15 | × | higher per run. However, open-source |
| tation). Although a general agent exists to exploit | models fail to resolve any tasks. |  |  |
| vulnerabilities outside of the expert agents, it was | Using similar cost estimates for a cybersecurity |  |  |

---

## Page 8

| expert ($50 per hour) as prior work, and an esti- | as solving real-world GitHub issues (Yang et al., |  |  |
| --- | --- | --- | --- |
| mated time of 1.5 hours to explore a website, we | 2024b). There have been hundreds of papers on |  |  |
| arrive at a cost of $75. Thus, our cost estimate for a | improving AI agents, ranging from prompting tech- |  |  |
| human expert is higher, but not dramatically higher | niques (Wei et al., 2022; Yao et al., 2024), planning |  |  |
| than using an AI agent. | techniques (Shinn et al., 2024; Liu et al., 2023a), |  |  |
| However, we anticipate that costs of using AI | adding documents and memory (Nuxoll and Laird, |  |  |
| agents will fall. For example, costs for GPT-4o | 2012), domain-specific agents (He et al., 2024), |  |  |
| were cut in half over six months and Claude-3.5- | and many more (Parisi et al., 2022). The field of |  |  |
| Haiku is 3 | × | cheaper than GPT-4o (per input token). | multi-agent systems is particularly related to our |
| If these trends in cost continue, we anticipate that | work (Liu et al., 2023b; Chen et al., 2023; Zhang |  |  |
| a GPT-4o level agent will be 3-6 | × | cheaper than | et al., 2023). However, to the best of our knowl- |
| the cost today in the next 1-2 years. If such costs | edge, our work is the first to introduce a real-world |  |  |
| improvements do occur, AI agents will be substan- | AI agent system based on hierarchical planning and |  |  |
| tially cheaper than a human expert. | task-specific agents. |  |  |

8 Related Work

our work that teams of AI agents can autonomously

exploit zero-day vulnerabilities. Our findings are

of broader relevance to the community, as govern-

mental agencies (US, 2025; UK, 2024), industrial

labs (Weidinger et al., 2024; Anthropic, 2024), and

other parties are interested in measuring cybersecu-

rity capabilities of AI agents.

lated on societal implications of AI on cybersecu-

rity (Lohn and Jackson, 2022; Handa et al., 2019).

AI agents. AI agents have becoming increasing

8

Security of AI agents. A related area of work

is the security of AI agents themselves (Greshake

et al., 2023a; Kang et al., 2023; Zou et al., 2023;

9 Conclusions

In this work, we show that teams of LLM agents

can autonomously exploit zero-day vulnerabilities,

resolving an open question posed by prior work

(Fang et al., 2024a). Our findings suggest that cy-

bersecurity, on both the offensive and defensive

their deployments.

10 Limitations, Ethical Considerations

| Cybersecurity and AI. | Recent work in the inter- | Zhan et al., 2023; Qi et al., 2023; Yang et al., 2023). |
| --- | --- | --- |
| section of cybersecurity and AI falls in three broad | Deployers of AI agents may want to limit the tasks |  |
| categories: human uplift, societal implications of | that the AI agent can do (e.g., restricting the ability |  |
| AI, and AI agents. | to perform cybersecurity attacks) and protect the |  |
| In this work, we focus on AI agents and cyber- | agent against malicious attackers. Unfortunately, |  |
| security. | The closest works to ours shows that | recent work has shown that it is simple to bypass |
| ReAct-style AI agents can hack “capture-the-flag” | protections in LLMs, such as by fine-tuning away |  |
| toy websites and vulnerabilities when given a de- | protections (Zhan et al., 2023; Yang et al., 2023; |  |
| scription of the vulnerability (Fang et al., 2024b,a). | Qi et al., 2023). AI agents can also be attacked via |  |
| However, these agents fare poorly in the zero-day | indirect prompt injection attacks (Greshake et al., |  |
| setting. In particular, it is challenging for agents to | 2023b; Yi et al., 2023; Zhan et al., 2024). This line |  |
| backtrack after exploring a dead end. We show in | of work is orthogonal to ours. |  |
| The human uplift setting focuses on using AI | side, will increase in pace. Now, black-hat actors |  |
| (typically LLMs) to aid humans in cybersecurity | can use AI agents to hack websites. On the other |  |
| tasks. For example, recent work has shown that | hand, penetration testers can use AI agents to aid |  |
| LLMs can aid humans in penetration testing and | in more frequent penetration testing. It is unclear |  |
| malware generation (Happe and Cito, 2023; Hilario | whether AI agents will aid cybersecurity offense |  |
| et al., 2024). This work is especially important in | or defense more and we hope that future work ad- |  |
| the setting of “script kiddies” who deploy malware | dresses this question. Beyond the immediate im- |  |
| without special expertise. Based on this, and the | pact of our work, we hope that our work inspires |  |
| work on AI agents, researchers have also specu- | frontier LLM providers to think carefully about |  |
| powerful and popular. Recent, highly capable AI | Although our work shows substantial improve- |  |
| agents are largely based on LLMs (Yao et al., 2022; | ments in performance in the zero-day setting, much |  |
| Weng, 2023) and can now perform tasks as complex | work remains to be done to fully understand the |  |

---

## Page 9

implications of AI agents in cybersecurity. For in Computing and Communications , pages 45–52.

example, we focused on web, open-source vulner- IEEE.

abilities, which may result in a biased sample of

in potentially harmful uses of LLMs is that mali-

cious actors can use the ideas for nefarious pur-

elected not to release our code or prompts publicly

(OWASP, 2024). Furthermore, we have disclosed

References

arXiv preprint arXiv:2303.08774 .

Simon Bennetts. 2013. Owasp zed attack proxy.

AppSec USA .

Leyla Bilge and Tudor Dumitra¸ s. 2012. Before we knew

it: an empirical study of zero-day attacks in the real

world. In Proceedings of the 2012 ACM conference

on Computer and communications security , pages

833–844.

Guangyao Chen, Siwei Dong, Yu Shu, Ge Zhang,

Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,

Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,

| Kang. | 2024a. | Llm | agents | can | autonomously |  |
| --- | --- | --- | --- | --- | --- | --- |
| exploit one-day vulnerabilities. | arXiv preprint |  |  |  |  |  |
| Zhan, | and | Daniel | Kang. | 2024b. | Llm | agents |

privacy-preserving defense mechanism against re-

tional Conference on Trust, Security and Privacy

9

Kai Greshake, Sahar Abdelnabi, Shailesh Mishra,

application-integrated large language models. arXiv

e-prints , pages arXiv–2302.

Christoph Endres, Thorsten Holz, and Mario Fritz.

2023b. Not what you’ve signed up for: Compro-

rity , pages 79–90.

Wiley Interdisciplinary Reviews: Data Mining and

Knowledge Discovery , 9(4):e1306.

Andreas Happe and Jürgen Cito. 2023. Getting pwn’d

2082–2086.

Dong Yu. 2024. Webvoyager: Building an end-to-

end web agent with large multimodal models. arXiv

preprint arXiv:2401.13919 .

Eric Hilario, Sami Azam, Jawahar Sundaram, Khwaja

Imran Mohammed, and Bharanidharan Shanmugam.

2024. Generative ai for pentesting: the good, the

bad, the ugly. International Journal of Information

Security , pages 1–23.

through standard security attacks. arXiv preprint

arXiv:2302.05733 .

What is cve-2021-26855?

Chain of hindsight aligns language models with feed-

agent collaboration framework with agent team opti-

cyber swords or shields?

| vulnerabilities. We hope that future work addresses | Christoph Endres, Thorsten Holz, and Mario Fritz. |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| this problem more thoroughly. | 2023a. More than you’ve asked for: A comprehen- |  |  |  |  |  |  |  |  |  |  |
| A major consideration when conducting research | sive analysis of novel prompt injection threats to |  |  |  |  |  |  |  |  |  |  |
| poses. | To help alleviate such issues, we have | Kai Greshake, | Sahar Abdelnabi, | Shailesh Mishra, |  |  |  |  |  |  |  |
| as OpenAI has requested that we keep our agents | mising real-world llm-integrated applications with |  |  |  |  |  |  |  |  |  |  |
| confidential. This is in line with prior work (Fang | indirect prompt injection. In | Proceedings of the 16th |  |  |  |  |  |  |  |  |  |
| et al., 2024b,a) and best practice for cybersecurity | ACM Workshop on Artificial Intelligence and Secu- |  |  |  |  |  |  |  |  |  |  |
| our findings to OpenAI as part of their responsible | Anand Handa, Ashu Sharma, and Sandeep K Shukla. |  |  |  |  |  |  |  |  |  |  |
| disclosure program. | 2019. Machine learning in cybersecurity: A review. |  |  |  |  |  |  |  |  |  |  |
| Josh Achiam, Steven Adler, Sandhini Agarwal, Lama | by ai: Penetration testing with large language mod- |  |  |  |  |  |  |  |  |  |  |
| Ahmad, | Ilge Akkaya, | Florencia Leoni Aleman, | els. In | Proceedings of the 31st ACM Joint European |  |  |  |  |  |  |  |
| Diogo Almeida, Janko Altenschmidt, Sam Altman, | Software Engineering Conference and Symposium |  |  |  |  |  |  |  |  |  |  |
| Shyamal Anadkat, et al. 2023. Gpt-4 technical report. | on the Foundations of Software Engineering | , pages |  |  |  |  |  |  |  |  |  |
| Anthropic. 2024. A new initiative for developing third- | Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, |  |  |  |  |  |  |  |  |  |  |
| party model evaluations. | Yong Dai, Hongming Zhang, Zhenzhong Lan, and |  |  |  |  |  |  |  |  |  |  |
| Jaward Sesay, Börje F Karlsson, Jie Fu, and Yemin | Daniel Kang, Xuechen Li, Ion Stoica, Carlos Guestrin, |  |  |  |  |  |  |  |  |  |  |
| Shi. 2023. Autoagents: A framework for automatic | Matei Zaharia, and Tatsunori Hashimoto. 2023. Ex- |  |  |  |  |  |  |  |  |  |  |
| agent generation. | arXiv preprint arXiv:2309.17288 | . | ploiting programmatic behavior of llms: Dual-use |  |  |  |  |  |  |  |  |
| Akhil Mathur, Alan Schelten, Amy Yang, Angela | David Kennedy, Jim O’gorman, Devon Kearns, and |  |  |  |  |  |  |  |  |  |  |
| Fan, et al. 2024. The llama 3 herd of models. | arXiv | Mati Aharoni. 2011. | Metasploit: the penetration |  |  |  |  |  |  |  |  |
| preprint arXiv:2407.21783 | . | tester’s guide | . No Starch Press. |  |  |  |  |  |  |  |  |
| Richard Fang, Rohan Bindu, Akul Gupta, and Daniel | Edward Kost. 2023. Critical microsoft exchange flaw: |  |  |  |  |  |  |  |  |  |  |
| arXiv:2404.08144 | . | Hao Liu, Carmelo Sferrazza, and Pieter Abbeel. 2023a. |  |  |  |  |  |  |  |  |  |
| Richard | Fang, | Rohan | Bindu, | Akul | Gupta, | Qiusi | back. | arXiv preprint arXiv:2302.02676 | . |  |  |
| can | autonomously | hack | websites. | Preprint | , | Zijun Liu, Yanzhe Zhang, Peng Li, Yang Liu, and Diyi |  |  |  |  |  |
| arXiv:2402.06664. | Yang. 2023b. Dynamic llm-agent network: An llm- |  |  |  |  |  |  |  |  |  |  |
| Ben | SY | Fung | and | Patrick | PC | Lee. | 2011. | A | mization. | arXiv preprint arXiv:2310.02170 | . |
| quest forgery attacks. | In | 2011IEEE 10th Interna- | Andrew Lohn and Krystal Jackson. 2022. Will ai make |  |  |  |  |  |  |  |  |

---

## Page 10

| Microsoft. 2024. Securing the cloud. | https://news. | John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian |  |
| --- | --- | --- | --- |
| microsoft.com/stories/cloud-security/ | . | Ac- | Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir |
| cessed: 2024-05-19. | Press. 2024b. Swe-agent: Agent computer interfaces |  |  |

Andrew M Nuxoll and John E Laird. 2012. Enhancing

Online.

Aaron Parisi, Yao Zhao, and Noah Fiedel. 2022. Talm:

Tool augmented language models. arXiv preprint

arXiv:2205.12255 .

Xiangyu Qi, Yi Zeng, Tinghao Xie, Pin-Yu Chen, Ruoxi

Jia, Prateek Mittal, and Peter Henderson. 2023. Fine-

tuning aligned language models compromises safety,

even when users do not intend to! arXiv preprint

arXiv:2310.03693 .

conference series: materials science and engineering ,

flexion: Language agents with verbal reinforcement

and database takeover tool.

Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten

Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,

et al. 2022. Chain-of-thought prompting elicits rea-

soning in large language models. Advances in neural

information processing systems , 35:24824–24837.

Lisa Anne Hendricks, Ramona Comanescu, Oscar

Chang, Mikel Rodriguez, et al. 2024. Holistic safety

and responsibility evaluations of advanced ai models.

arXiv preprint arXiv:2404.14068 .

Lilian Weng. 2023. Llm-powered autonomous agents.

lilianweng.github.io .

An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui,

Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu,

Fei Huang, Haoran Wei, et al. 2024a. Qwen2. 5

technical report. arXiv preprint arXiv:2412.15115 .

10

enable software engineering language models.

2023. Shadow alignment: The ease of subvert-

arXiv:2310.02949 .

Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran,

Tom Griffiths, Yuan Cao, and Karthik Narasimhan.

2024. Tree of thoughts: Deliberate problem solving

with large language models. Advances in Neural

Information Processing Systems , 36.

Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak

Shafran, Karthik Narasimhan, and Yuan Cao. 2022.

ReAct: Synergizing reasoning and acting in language

models. arXiv preprint arXiv:2210.03629 .

Wu. 2023. Benchmarking and defending against indi-

Tatsunori Hashimoto, and Daniel Kang. 2023. Re-

prompt injections in tool-integrated large language

Andy K Zhang, Neil Perry, Riya Dulepet, Joey Ji,

Cybench: A framework for evaluating cybersecurity

Hongxin Zhang, Weihua Du, Jiaming Shan, Qinhong

Zhou, Yilun Du, Joshua B Tenenbaum, Tianmin Shu,

and Chuang Gan. 2023. Building cooperative em-

bodied agents modularly with large language models.

arXiv preprint arXiv:2307.02485 .

Andy Zou, Zifan Wang, J Zico Kolter, and Matt Fredrik-

arXiv:2307.15043 .

| intelligent agents with episodic memory. | Cognitive | Xianjun Yang, Xiao Wang, Qi Zhang, Linda Petzold, |  |  |
| --- | --- | --- | --- | --- |
| Systems Research | , 17:34–48. | William Yang Wang, Xun Zhao, and Dahua Lin. |  |  |
| OWASP. 2024. | Vulnerability disclosure cheat sheet. | ing safely-aligned language models. | arXiv preprint |  |
| Emma Roth and Wes Davis. 2024. Google i/o 2024: | Jingwei Yi, Yueqi Xie, Bin Zhu, Keegan Hines, Emre |  |  |  |
| everything announced. | Kiciman, Guangzhong Sun, Xing Xie, and Fangzhao |  |  |  |
| Eko Budi Setiawan and Angga Setiyadi. 2018. | Web | rect prompt injection attacks on large language mod- |  |  |
| vulnerability analysis and implementation. In | IOP | els. | arXiv preprint arXiv:2312.14197 | . |
| volume 407, page 012081. IOP Publishing. | Qiusi Zhan, Richard Fang, Rohan Bindu, Akul Gupta, |  |  |  |
| Noah Shinn, Federico Cassano, Ashwin Gopinath, | moving rlhf protections in gpt-4 via fine-tuning. |  |  |  |
| Karthik Narasimhan, and Shunyu Yao. 2024. | Re- | arXiv preprint arXiv:2311.05553 | . |  |
| learning. | Advances in Neural Information Process- | Qiusi Zhan, Zhixiang Liang, Zifan Ying, and Daniel |  |  |
| ing Systems | , 36. | Kang. 2024. | Injecagent: | Benchmarking indirect |
| Project sqlmap. 2024. sqlmap: Automatic sql injection | model agents. | arXiv preprint arXiv:2403.02691 | . |  |
| AISI UK. 2024. Ai safety institute approach to evalua- | Justin W Lin, Eliot Jones, Celeste Menders, Gashon |  |  |  |
| tions. | Hussein, Samantha Liu, Donovan Jasper, et al. 2024. |  |  |  |
| AISI US. 2025. Technical blog: Strengthening ai agent | capabilities and risks of language models. | arXiv |  |  |
| hijacking evaluations. | preprint arXiv:2408.08926 | . |  |  |
| Laura Weidinger, Joslyn Barnhart, Jenny Brennan, | son. 2023. | Universal and transferable adversarial |  |  |
| Christina Butterfield, Susie Young, Will Hawkins, | attacks on aligned language models. | arXiv preprint |  |  |
