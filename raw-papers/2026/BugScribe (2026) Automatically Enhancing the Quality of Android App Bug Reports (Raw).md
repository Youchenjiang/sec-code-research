---
title: "Automatically Enhancing the Quality of Android App Bug Reports"
author: "Antu Saha; Atish Kumar Dipongkor; Sam Bennett; Kevin Moran; Andrian Marcus; Oscar Chaparro"
creator: "arXiv GenPDF (tex2pdf:a6404ea)"
pages: 12
---

# Automatically Enhancing the Quality of Android App Bug Reports

> **作者**：Antu Saha; Atish Kumar Dipongkor; Sam Bennett; Kevin Moran; Andrian Marcus; Oscar Chaparro
> **總頁數**：12 頁

---

## Page 1

Automatically Enhancing the Quality of Android

App Bug Reports

| Antu Saha | Atish Kumar Dipongkor | Sam Bennett |
| --- | --- | --- |
| William & Mary | University of Central Florida | William & Mary |
| Williamsburg, Virginia, USA | Orlando, Florida, USA | Williamsburg, Virginia, USA |
| asaha02@wm.edu | atish.kumardipongkor@ucf.edu | srbennett01@wm.edu |
| Kevin Moran | Andrian Marcus | Oscar Chaparro |
| University of Central Florida | George Mason University | William & Mary |
| Orlando, Florida, USA | Fairfax, Virginia, USA | Williamsburg, Virginia, USA |
| kpmoran@ucf.edu | amarcus7@gmu.edu | oscarch@wm.edu |
| Abstract | —Most defects in mobile applications are visually | Unfortunately, bug reports are often incomplete, ambiguous, |

observable on the device screen. Since automated mechanisms or inaccurate, sometimes omitting the EB or S2Rs entirely [5].

for detecting and reporting such defects are often unavailable, Low-quality reports hinder developers’ understanding of

users, testers, and developers must manually submit bug reports.

However, these reports are frequently incomplete, ambiguous, or defects [6], delay resolution [7], [8], and may lead to reopened

inaccurate, often lacking the information needed to understand, or unresolvable issues [8], [7]. This problem is particularly

reproduce, and diagnose defects. This challenge is particularly challenging for mobile apps because defects are often

prominent for UI-centric defects, where the relevant application GUI-centric and involve multiple GUI screens, interactions,

behavior is difficult for end users to describe precisely. and execution states that can be difficult for end users to

We formulate automatic bug report enhancement as the

describe precisely. This is because such users are typically

problem of connecting user-written bug reports with application

execution. We present B UG S CRIBE , an LLM-powered approach unfamiliar with app internals and the report information that

that links bug report information with app-specific UI execution is important for developers ( e.g. , the OB, EB, and S2Rs). As

information to infer and generate accurate, complete, and correct a result, reports frequently lack the detailed, complete, and

Observed Behavior (OB), Expected Behavior (EB), and Steps to correct information needed for developers (or automated tools)

Reproduce (S2Rs). B UG S CRIBE employs a component-specific

to accurately understand, reproduce, and diagnose the defect.

grounding strategy that provides the most relevant context to

an LLM for generating each bug report component. To support The core challenge in enhancing these reports is therefore

B UG S CRIBE ’s design and evaluation, we develop a bug report not merely improving the bug description, but recovering the

quality model and use it to identify the most effective context missing connections between the reported bug information and

for each component. We evaluate B UG S CRIBE on 48 bug reports the application’s underlying UI execution needed to produce

from 26 Android applications with manually constructed ground

a complete and accurate description of the defect.

truth. Our results show that B UG S CRIBE generates higher-quality

bug report components than the original reports and three LLM- Prior work has proposed techniques to assess bug report

based baselines, improving S2R quality by 44.1%–82.3% and quality [9], [6], identify missing information [10], [11], provide

OB/EB quality by 3.8%–35.2%. feedback to reporters [9], [6], support interactive report con-

struction [2], [12], [13], [14], and restructure bug reports [15].

I. I NTRODUCTION While these approaches help identify quality problems or

arXiv:2604.01148v2 [cs.SE] 2 Jul 2026 rewrite existing reports, they either leave users responsible

Most defects in mobile applications are visually observable for correcting the report or generate content primarily from

on the device screen [1]. Since automated mechanisms for the original report text. Consequently, they cannot ensure that

detecting and reporting such bugs are often unavailable— the generated information accurately reflects the application’s

especially when they do not produce explicit signals such behavior, potentially producing plausible but incorrect or

as crashes—users, testers, and developers must manually incomplete bug descriptions, such as reproduction steps that

submit bug reports (BRs) during app use or testing [2]. These do not correspond to valid GUI interactions.

reports help developers understand, diagnose, reproduce, and Our key insight is that high-quality bug report generation

ultimately fix the defects [3]. A high-quality bug report should should be formulated as a problem of connecting bug

describe at least three essential components [4], [3]: the descriptions with the application’s UI execution information .

Observed Behavior (OB) , which describes the faulty behavior; The original bug report contains information useful to identify

the Expected Behavior (EB) , which describes the intended the relevant screens, GUI interactions, execution paths, and

behavior; and the Steps to Reproduce (S2Rs) , which describe buggy screen, but these relationships are implicit rather than

the sequence of actions needed to reproduce the defect. explicitly described. By leveraging LLM reasoning together

---

## Page 2

| with app-specific execution information, these connections can | • | An empirical evaluation showing that B | UG | S | CRIBE | improves |
| --- | --- | --- | --- | --- | --- | --- |
| be inferred and translated into detailed, complete, and accurate | original bug reports, outperforming LLM-based baselines |  |  |  |  |  |
| OB/EB/S2R | descriptions. | However, | effective | reasoning | that do not use app-specific information. |  |
| requires more than simply providing app context to an LLM. | • | A replication package with a manually curated dataset of |  |  |  |  |
| We pose that different bug report components require different | 58 bug reports, ground truth OB/EB/S2Rs, code, prompts, |  |  |  |  |  |
| execution | information, | motivating | a | component-specific | documentation, and experimental infrastructure [16]. |  |

grounding strategy that leverages the most relevant context

for bug report generation. II. B UG R EPORT Q UALITY M ODEL

In this paper, we present B UG S CRIBE , an LLM-powered

approach that automatically enhances user-written Android Our quality model defines quality categories for the three

bug reports. B UG S CRIBE augments existing reports with main bug report components: the OB, EB, and S2Rs. A high-

accurate, correct, and complete OB, EB, and S2R descriptions quality bug report must contain complete, detailed, and accurate

through a pipeline that connects bug report content with descriptions of these components. The model targets reports

app-specific execution information. Specifically, B UG S CRIBE of GUI-based applications, in particular Android apps.

constructs a graph-based execution model of app screens S2R Quality Model. The S2Rs in a high-quality bug report

and GUI interactions enriched with UI metadata; identifies are an enumerated list of GUI interactions that a user performs

OB, EB, and S2R sentences in the original report; links this on the app sequentially to reproduce the bug. Each step should

information to relevant app execution elements; and generates be atomic: it should represent a single GUI action ( e.g. , a tap,

high-quality bug report components using component-specific type, or swipe) on a particular GUI component ( e.g. , button or

prompts. B UG S CRIBE ’s novel contribution is an LLM-guided text field). An example of high-quality S2R is “Tap the ‘More

reasoning strategy that selectively combines bug report text options’ button”. We adapt the S2R quality model from prior

with app execution information according to the needs of each work [6] and define the following categories:

| bug report component. | • | Correct Step (CS): | the step corresponds to a specific GUI |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| To design B | UG | S | CRIBE | , we used a data-driven methodology | interaction in the application. |  |  |  |  |
| to identify which combinations of app-specific information are | • | Ambiguous Step (AS): | the step corresponds to multiple |  |  |  |  |  |  |
| most effective for generating OB, EB, and S2Rs. To support | interactions on GUI components. |  |  |  |  |  |  |  |  |
| this analysis, we developed a bug report quality model that | • | Extra Step (ES): | step is not required to reproduce the bug. |  |  |  |  |  |  |
| extends an existing S2R quality model [6] to systematically | • | Missing | Step | (MS): | a | GUI | interaction | required | to |
| evaluate the quality of OB, EB, and S2R descriptions and their | reproduce the bug is missing from the report. |  |  |  |  |  |  |  |  |

constituent information elements. Using this quality model Compared to the original quality model [6], we include the

and manually curated ground truth for 10 bug reports from 9 Extra Step (ES) category because automated approaches may

Android apps, we evaluated eight context configurations for generate steps that are unnecessary to reproduce a bug, and we

S2R and OB/EB generation. Our results show that different discarded the Vocabulary Mismatch (VM) category [6] because

components benefit from different app-specific information: we expect LLMs to always generate well-written steps that map

S2R generation depends primarily on GUI interactions and the to GUI interactions—we also did not observe this quality issue

buggy screen, whereas OB and EB generation benefit from in our experiments. An example of an Ambiguous S2R would be

generated S2Rs, buggy screen descriptions, and screen-level “Restore from backup” (see fig. 1) because multiple individual

context. These findings guided the final design of B UG S CRIBE . steps are required to complete the data restoration in the app.

We further evaluated B UG S CRIBE on 48 bug reports from OB Quality Model. The OB in a high-quality report should

26 Android apps. For these bug reports, we manually con- be a clear, detailed, and self-contained description of the

structed ground truth OB, EB, and S2Rs following our quality bug and should specify three main information elements:

model. We compare B UG S CRIBE against the original bug 1) the buggy app behavior (the observed app misbehavior),

reports and three LLM-based baselines that do not use app- (2) a buggy screen reference (the screen where the user

specific information. Our results show that B UG S CRIBE gener- observed the bug), and (3) the triggering GUI interaction (the

ates more complete, detailed, and accurate S2Rs than the base- interaction that triggers the buggy behavior). An example of

lines and the original reports, with 44.1% to 82.3% relative im- a high-quality OB is “The app crashes if I tap the ‘Restore

provement, and improves OB and EB quality by 3.8% to 35.2%. from backup’ option on the pop-up menu of the Main Task

In summary, this paper makes the following contributions: screen”. Our model defines four quality attributes for each

• B UG S CRIBE , an LLM-powered bug report enhancement of the OB elements. A quality OB element can be:

| approach that links report information to app-specific | • | Correct: | the element corresponds to plausible buggy app |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| execution information to generate accurate, complete, and | behaviors, screens, or GUI interactions. |  |  |  |  |  |  |
| correct OB, EB, and S2Rs descriptions. | • | Incomplete: | the element lacks information to fully map it to |  |  |  |  |
| • | A data-driven methodology that identifies the specific app | plausible buggy app behavior, screens, or GUI interactions. |  |  |  |  |  |
| information elements needed by B | UG | S | CRIBE | ’s LLM-based | • | Ambiguous: | the element contains ambiguous or generic |
| reasoning strategy to link report and app execution data | information for mapping it specifically to plausible buggy |  |  |  |  |  |  |
| and generate high-quality OB, EB, and S2R descriptions. | app behavior, app screens, or GUI interactions. |  |  |  |  |  |  |

---

## Page 3

• Incorrect: the element describes information that does not

map the buggy app behavior, screen, or GUI interaction.

tap the ‘Restore from backup’ option”, it would also contain

also contain an Incomplete triggering GUI interaction .

EB Quality Model. The EB in a high-quality report should

For example, for the OB “The app crashes if I tap the ‘Restore

from backup’ option on the pop-up menu...”, the EB should be

ambiguous S2R ( “after selecting the menu item” ).

with...” ), the triggering app screen ( “On the extended options

We introduce B UG S CRIBE , an LLM-based automated ap-

proach that receives an existing bug report and produces a high-

quality report that more effectively describes the equivalent

BugScribe Bug Report

Title: App crashes when selecting 'Restore

Original

| Bug Report | extended options popup menu over the |
| --- | --- |
| crash on restore | backup”, the app crashes with an |
| when trying to | stopped.” message. |

restore a backup,

with successfully restore the backup and display

Time Tracker has

| stopped." this | Steps to Reproduce (S2R): |  |  |
| --- | --- | --- | --- |
| happens directly | 1. Launch the application. |  |  |
| a |  | er selecting | 2. On the initial help/about dialog, tap OK. |

“More options” overflow bu  on.

“Restore from backup”.

This popup menu

such as… backing

appears as a dialog

indicating that "A

stopped." The

the message by

use [19]. In B UG S CRIBE ’s evaluation, described in Section V,

another state-of-the-art LLM, to assess whether using different

frontier models impacts the effectiveness of B UG S CRIBE .

B UG S CRIBE performs three main phases (see Figure 2):

| • | Missing: | the element is not provided in the OB description. | from backup' |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| For example, in the OB “The app crashes if I tap the | Observed Behavior (OB): | On the |  |  |  |  |  |  |  |  |  |
| ‘Restore from backup’ option”, the | buggy screen reference | is | main task list, if the user taps “Restore from |  |  |  |  |  |  |  |  |
| Missing | , and if it is written as “The app does not work if I | “Unfortunately, A Time Tracker has |  |  |  |  |  |  |  |  |  |
| an | Ambiguous buggy app behavior | , and if it was written as | the app crashes | Expected Behavior (EB): | The app should |  |  |  |  |  |  |
| “The app does not work if I ‘Restore from backup”’, it would | "Unfortunately, A | the confirmation dialog instead of crashing. |  |  |  |  |  |  |  |  |  |
| be a clear, detailed, and self-contained description of the | the menu item. | 3. On the main screen, tap the |  |  |  |  |  |  |  |  |  |
| intended app behavior | , and it is tied to the OB as it describes | 4. In the first popup menu, tap “More…”. |  |  |  |  |  |  |  |  |  |
| the opposite (or an alternative) to the OB’s buggy behavior. | 5. In the extended options dialog, tap |  |  |  |  |  |  |  |  |  |  |
| “The app should successfully restore the backup and display a | UI-anchored App Information |  |  |  |  |  |  |  |  |  |  |
| confirmation dialog”. We define the same five quality attributes | a | GUI Interactions | b | LLM-generated |  |  |  |  |  |  |  |
| as for the OB elements ( | i.e. | , correct, incomplete, ambiguous, | Screen Descriptions |  |  |  |  |  |  |  |  |
| missing, and incorrect). For instance, an EB with an | Ambiguous | provides options |  |  |  |  |  |  |  |  |  |
| intended behavior | would be “The app should work”. | up, restoring… It |  |  |  |  |  |  |  |  |  |
| Motivating | Example. | Figure 1 shows bug report #35 | over the main task |  |  |  |  |  |  |  |  |
| submitted | for | the | ATimeTracker | app | [17], | which | allows | list. |  |  |  |
| users to track the time of their daily activities. This report is | c | LLM-generated |  |  |  |  |  |  |  |  |  |
| unstructured and contains an OB with | missing EB | ( | i.e. | , the | Buggy Screen Description |  |  |  |  |  |  |
| intended behavior is missing) and is missing S2Rs. The OB | An error dialog |  |  |  |  |  |  |  |  |  |  |
| describes a correct buggy behavior ( | “the app crashes with...” | ) | Time Tracker has |  |  |  |  |  |  |  |  |
| but contains an | incomplete | triggering | GUI | interaction | user can dismiss |  |  |  |  |  |  |
| ( | “trying | to | restore | a | backup” | ). | The | report | contains | an | tapping "OK". |

Figure 1 also shows the bug report that our approach, Fig. 1: Bug report #35 of the Time Tracker app [17], and

B UG S CRIBE , generates. Unlike the original bug report, this the corresponding B UG S CRIBE report. Pieces of the report

report is structured and provides complete, correct, and detailed are linked to: (i) GUI interaction data (orange), (ii) LLM-

OB, EB, and S2R descriptions. For example, the OB includes generated descriptions of bug-related screens (green), and (iii)

correct descriptions of the buggy behavior ( “...the app crashes LLM-generated description(s) of the buggy screen(s) (red).

popup menu...” ), and the triggering GUI interaction ( “... the (1) it offers reasoning of multi-modal information, as our prob-

user taps ‘Restore from backup’...” ). The S2Rs describe lem involves reasoning about app execution information, app

a complete reproduction scenario with atomic steps that screen data, and natural language and (2) it is a frontier model

| correspond to specific GUI interactions (see fig. 1.a). | with state-of-the-art performance in reasoning, coding, and tool |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| III. B | UG | S | CRIBE | : G | ENERATING | E | NHANCED | B | UG | R | EPORTS | we instantiate | B | UG | S | CRIBE | with | C | LAUDE | O | PUS | -4.6 | [20], |
| defect from the original report. B | UG | S | CRIBE | leverages dynamic | 1) | App Execution Model Generation | : it constructs a graph- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| app analysis, LLM-based language reasoning/generation, and | based execution model of the app using both automated |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| uses app-related information as context for the LLM to generate | and manual app exploration (Section III-A). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

bug reports with clear, detailed, and accurate OB, EB, and S2Rs. 2) Contextual Information Extraction : it extracts and for-

| Based on these components, B | UG | S | CRIBE | also generates a one- | mats app-related information ( | e.g. | , GUI interactions) used |
| --- | --- | --- | --- | --- | --- | --- | --- |
| line bug summary as bug report title and adds environment | as context for the LLM (Section III-B). |  |  |  |  |  |  |
| details described in the original bug report, | including mobile | 3) | Bug Report Generation | : it generates high-quality bug |  |  |  |
| device information and Android version. | reports, including a title, OB, EB, and S2Rs, leveraging |  |  |  |  |  |  |
| In its current version, B | UG | S | CRIBE | uses GPT-5.4 [18], a | the app-specific information and LLM-based reasoning via |  |  |
| state-of-the-art reasoning LLM. We selected this model because: | zero-shot, task-decomposition prompting (Section III-C). |  |  |  |  |  |  |

---

## Page 4

App +BR

Information

b Bug Report Labeled Bug

Report

Sentence Annotation

S2R

Sentence OB EB

Execution

Classifier

a App Screen

Model

Descriptions

Generation

c GUI Interaction +

Screen Extraction

Exploration Analysis Model Interac-

tions

Buggy Screen

d

Localization

Database GPT-5.4

Fig. 2: B UG S CRIBE

In the first phase, B UG S CRIBE constructs a graph-based

B UG S CRIBE represents the execution model as a directed

graph, where nodes represent unique GUI screens and edges rep-

resent user interactions ( e.g. , taps). Screens are distinguished by

their UI component hierarchies. Each interaction is represented

as ( v x , v y , e, c ) , where c is the interacted GUI component ( e.g. ,

a button) on screen v x , e is the performed action, and v y is

the resulting screen. Each edge also stores metadata such as

the component type, ID, label, and description.

execution model can be built from GUI interaction traces col-

B. Contextual Information Extraction

into individual sentences and uses GPT-5.4 with zero-shot,

e S2R Generation Reproduction Steps:

Labeled - Launch the app

- Tap on “More Options”

GUI

| Buggy | - … |
| --- | --- |
| Screen | Interac- |
| tions | + |

Observed Behavior:

| Screen | } | On the extended |
| --- | --- | --- |
| Descriptions | GPT-5.4 | options popup menu |

over the main task

| f | OB & EB Generation | list, if the user taps |
| --- | --- | --- |
| Bug Report | Expected Behavior: |  |
| BugScribe | The app should |  |

Buggy

| S2Rs | Screen | successfully restore |
| --- | --- | --- |
| + | the backup and |  |
| Screen Descriptions | GPT-5.4 | instead of crashing. |

’s architecture

or other. The labeled report is then passed to the next phase.

sentences in the bug report.

2) App Screen Description Generation: B UG S CRIBE uses

app screen descriptions generated by the LLM as additional

app context. These descriptions summarize each screen’s

functionality, layout, GUI components, and available actions.

B UG S CRIBE generates one description for every identified

screen in the execution model using zero-shot prompting

on textual screen metadata ( e.g. , layout and UI component

interaction sequence in the execution model that leads to the

buggy behavior (Figure 2.b). To achieve this, B UG S CRIBE

extracts all GUI interactions from the execution and provides

and the execution model.

| Inputs | App Info Extraction | Bug Report Generation | Output Bug Report |  |  |
| --- | --- | --- | --- | --- | --- |
| APK | Bug Report | Bug Report | - Tap OK on the dialog |  |  |
| Automated App | UI-flow | Execution | GUI | Labeled | “Restore … |
| Manual App | App | Buggy | display the |  |  |
| Exploration | Execution | Screen | S2R-Involved | } | confirmation dialog |
| A. App Execution Model Generation | rule-based prompting to classify each sentence as OB, EB, S2R, |  |  |  |  |
| execution model that captures GUI interactions and screen meta- | Based on prior work’s data-driven methodology [9], we |  |  |  |  |

data, including UI hierarchies and events (Figure 2.a). It then designed a prompt to classify OB, EB, and S2R sentences. The

extracts and formats this information as context for the LLM template (found in our replication package [16]) includes the

to generate high-quality bug reports (Sections III-B and III-C). OB/EB/S2R definitions with detailed guidelines to classify all

B UG S CRIBE constructs the execution model from GUI information). An example of an app screen description is: “This

interaction traces collected through automated exploration and popup menu provides options such as changing the date range,

manual app usage. For automated exploration, it uses a modified exporting to CSV, ... It appears as a dialog over the main task

version of C RASH S COPE [21], [22]; manual traces complement list.” This context can help the LLM identify the interactions

workflows that automated exploration cannot cover. mapped to a reproduction scenario, generate atomic S2Rs,

Execution model generation is a one-time activity for a given and localize the suspected buggy screen (Section III-B4). The

app and is independent of the data collection strategy. The prompt template is available in our replication package [16].

lected through app usage or in-house testing and maintenance 3) GUI Interaction Extraction: GUI interactions are the

workflows, including automated exploration, developer testing, building blocks for B UG S CRIBE to generate atomic S2Rs

crowd-sourced testing, record-and-replay systems, and user because the interactions required to reproduce a bug are a

interaction logs [23]. As new traces become available, they subset of all possible app interactions. B UG S CRIBE uses the

can be incrementally incorporated into the execution model. LLM to map the S2Rs in the original bug report to a navigable

B UG S CRIBE annotates the user-submitted bug report to them to the LLM as context. Each interaction is represented

specify three components (OB, EB, and S2Rs) and extracts as a tuple containing (1) the action ( e.g. , tap), (2) the target

three app information elements (app screen information, GUI GUI element ( e.g. , “OK” button), (3) the source screen ID,

interactions, and buggy screen) as context for the LLM. and (4) the target screen ID. The LLM then synthesizes these

1) OB/EB/S2R Sentence Annotation: B UG S CRIBE identifies interactions into atomic S2Rs. When S2Rs are missing ( i.e. ,

the sentences that express the OB, EB, and S2Rs in the input there are gaps in paths in the execution model), it infers

bug report (Figure 2.b). B UG S CRIBE decomposes the report plausible steps from the OB, EB, other bug report information,

---

## Page 5

4) Buggy Screen Localization: The buggy screen is the IV. A PP - SPECIFIC I NFORMATION FOR B UG S CRIBE

screen where the faulty behavior occurs. It serves as the “stop-

ping” point for S2R generation ( i.e. , the final screen in the repro-

duction scenario) and provides context for OB/EB generation.

B UG S CRIBE identifies the buggy screen by reasoning

over the reported bug and the generated screen descriptions

(Figure 2.c). We formulate this task as a screen retrieval

problem [24], where the LLM ranks all screens in the ex-

ecution model using zero-shot prompting. B UG S CRIBE selects

the top-ranked screen as the buggy screen for subsequent

C. Bug Report Generation

We used a data-driven approach to identify the most effective

combinations of app-specific information ( e.g. , GUI interactions

and buggy screen) for B UG S CRIBE ’s S2R and OB/EB genera-

tion. Using a development set, we evaluated reports generated

by B UG S CRIBE against ground truth OB, EB, and S2Rs that

we manually created based on our bug report quality model.

A. Development Dataset Construction

and 80.5 GUI interactions (ranging from 19 to 159) on average.

The dataset includes OB/EB/S2R sentences, videos that show

how to reproduce the bugs, and screenshots of the exercised app

bug component generation. To this end, we use LLM-based 1) Bug Report Collection: We collected the 10 bug reports

reasoning with carefully designed prompts. We evaluated two from the development set from prior work on S2R quality

prompting strategies: (1) using the labeled bug report and assessment [9]. The bug reports span diverse bug types and apps:

screen descriptions, and (2) additionally providing all GUI nine Android apps from various domains (finance tracking, file

interactions. Including GUI interactions improved localization management, multimedia, etc. ) and report various bug types:

accuracy, ranking the correct buggy screen first in 80% of cases crashes (3), cosmetic issues (3), output problems (3), and a

compared to 60%. The prompt templates and experimental navigation bug (1). The app execution models associated with

results are available in our replication package [16]. the 10 reports contain 37.2 UI screens (ranging from 12 to 74)

1) S2R Generation: To generate an improved bug report, screen during automated/manual app exploration and execution.

B UG S CRIBE first generates atomic S2R descriptions for the However, it does not include data required to validate report

input bug report with GPT-5.4 (Figure 2.d). This step uses quality ( e.g. , ground truth OB, EB, and S2R descriptions).

a zero-shot, task-decomposition prompt to guide the LLM to 2) Ground Truth Creation: To create ground truth S2Rs, we

map the labeled S2R sentences to GUI interaction sequences first identified a minimal reproduction scenario (a path of GUI

and infer plausible reproduction scenarios that lead to the interactions) in the app execution model that maps to the S2Rs

buggy screen. The prompt instructs the LLM to identify the in the reports. Once identified, we created natural language

most likely reproduction scenario given the described bug and descriptions of the GUI interactions using GUI interaction

context and generate a detailed, enumerated list of reproduction metadata ( i.e. , the action and the interacted GUI component).

steps. The prompt starts with the task description, followed by a For each of the 10 reports, an author read the reported bug,

description of the input ( i.e. , app-related and report information watched the reproduction video, and manually inspected the

used as context), the output format, the inputs (structured into graph nodes and edges to identify a minimal reproduction

well-defined sections), and detailed instructions to complete scenario. This author created the natural language description

the task. To determine the combination of context information of each S2R following the format: [action] [GUI component]

elements that lead to the highest-quality generated S2Rs, we ( e.g. , “tap the OK button”). A second author validated the

employed a data-driven methodology described in Section IV. identified path and S2R descriptions, noting potential mistakes

2) OB/EB Generation: The last step in B UG S CRIBE ’s and disagreements. The two authors engaged in a discussion

pipeline generates the OB and EB for the input report session to resolve any issues and reach a consensus to finalize

using GPT-5.4 (Figure 2.e). This step uses a zero-shot, task the S2R ground truth. The agreement rate was high, 91.7%,

decomposition prompt to guide the LLM to map the identified with the most common reason for the disagreement being the

OB and EB from the original bug report to the contextual app misinterpretation of execution model metadata.

information, including the suspected buggy screen, the S2Rs During the ground truth creation process, the authors also

generated in the previous pipeline step, and the source and identified the buggy screen in the execution model: the resulting

target screen descriptions for each generated S2R. This step screen of the last GUI interaction in the reproduction scenario.

also generates a bug report title and additional environmental Based on this screen and the OB/EB in the original reports, one

information, such as the Android version and device. author wrote ground truth OB and EB. For OBs, the format

The prompt specifies the task description, the inputs (struc- used was: “On [buggy screen reference], if the user [triggering

tured into well-defined sections) with their descriptions, detailed GUI interaction], [buggy app behavior]” ( e.g. , “On the

instructions to complete the task, and the output format. To confirmation dialog, if the user clicks the OK button, the app

determine the combination of contextual information elements crashes”). The EB format used was: “[subject] should/shouldn’t

that lead to the highest-quality OB and EB, we employed the [intended app behavior]” ( e.g. , “the app should take me to

data-driven methodology described in Section IV. the previous screen without crashing”). These templates were

Finally, B UG S CRIBE assembles the complete bug report by designed based on the OB/EB discourse patterns identified in

appending the generated output into labeled sections in the fol- prior work [5], which were derived from manual analysis of

lowing order: title, OB, EB, S2Rs, and additional information. hundreds of real-life bug reports. A second author validated

---

## Page 6

the ground truth OBs/EBs, and both authors agreed on the final and complete path in the transition graph, starting from the

ground truth if changes were needed ( e.g. , due to mistakes). initial screen and ending at the screen where the bug occurs.”

3) Development Dataset Summary: Across the 10 bug For each task, one author designed a zero-shot, task-

reports, ground truth S2Rs include 103 atomic steps (10.3 decomposition prompt [25], [26] following the OpenAI guide-

per bug on average), each corresponding to one specific GUI lines [27] and prompt engineering best practices [28], [29], [30].

interaction. For each bug report, we created one OB and EB The prompts were iteratively refined using three development

description with the correct OB/EB information elements. bugs and meta-prompting with ChatGPT [31]. A second author

independently reviewed the prompt templates, evaluated them

B. Configurations of App Information Used as LLM Context on the same bugs, and suggested improvements. Both authors

1) Configurations for S2R generation: We designed four discussed the suggestions and finalized the prompt templates.

configurations that combine three app information elements:

GUI interactions, screen descriptions, and the buggy screen. D. Prompt Execution, Metrics, and Evaluation

1) No Info. uses the original report and no app-related We executed the eight prompt configurations (four prompts

information, allowing us to understand the LLM’s ability per generation task) using the OpenAI API [32] with the

to generate high-quality S2Rs without any context. GPT-5.4 model. Note that the latest GPT models do not have

2) Interac. adds GUI interactions to generate S2Rs, assuming temperature control, so we used the model as is. We assessed

that access to all app interactions enables the LLM to the consistency of LLM generation across three prompt

identify the required steps based on the original report. executions and reported the average bug report component

3) Interac.+Scrn. adds the screen descriptions. Screen quality using the evaluation metrics described next.

descriptions can help the LLM map interaction sequences 1) Evaluation Metrics: We evaluated the quality of the

to the original bug report when generating S2Rs. generated S2Rs, OBs, and EBs using the bug report quality

4) Interac.+Scrn.+BuggyScrn. adds the suspected buggy model described in Section II, by manually comparing them

screen. The buggy screen can inform the LLM about the against ground truth. For S2Rs, we assigned three quality labels:

stopping point in the reproduction scenario because it is 1) Correct Step (CS): the generated step is found in the ground

the final app screen where the bug manifests. truth S2Rs ( True Positive or TP) , 2) Extra Step (ES): the

2) Configurations for OB/EB generation: We designed four generated step is not found in the ground truth S2Rs ( False

configurations combining three app-specific contexts: the buggy Positive or FP , and 3) Missing Step (MS): a ground truth S2R

screen, B UG S CRIBE -generated S2Rs, and screen descriptions. is not found in the generated steps ( False Negative or FN) .

1) No Info. does not use any app context, serving as a bare- Using the quality labels assigned to the S2Rs, we computed

minimum baseline for OB/EB generation. precision , recall , and F1 score to measure S2R quality.

2) Buggy Scrn. adds the buggy screen description to generate For OB/EB evaluation, we assessed each OB/EB information

the OB/EB. As the bug manifests on this screen, it can element ( e.g. , buggy behavior or triggering GUI interaction)

provide key information, e.g. , OB’s buggy screen reference. using four quality labels (see Section II): Correct , Incomplete ,

3) S2Rs+BuggyScrn. adds atomic S2Rs generated in the S2R Ambiguous , Incorrect , and Missing . We counted the number

phase to the buggy screen description, helping the LLM of cases within each quality category for each component ele-

identify the triggering GUI interaction. ment ( e.g. , the OB’s buggy behavior) to measure OB/EB quality.

4) S2Rs+BuggyScrn.+Scrns. adds screen descriptions of the 2) Methodology for Quality Assessment: We conducted a

S2Rs, helping the LLM reason about the steps and identify multi-coder qualitative evaluation to mitigate potential bias.

the triggering GUI interaction. Two authors independently compared the generated S2Rs, OB,

and EB against the corresponding ground truth and assigned

C. Prompt Development Methodology quality labels using the quality model. To ensure consistent

To evaluate the app-related information configurations, we evaluation, they followed detailed criteria and annotation

designed two core prompt templates for the S2Rs and OB/EB guidelines (see our replication package [16]). Disagreements

generation tasks (described in Section III-C). We adapted the were resolved through discussion, and unresolved cases were

templates with specific instructions for handling the different evaluated by a third annotator to reach consensus.

app-related information elements, thus creating different in- We assessed inter-annotator reliability using observed

stances of the prompts, corresponding to the configurations. agreement, Cohen’s κ [33] and Krippendorff’s α [34],

The wording and structure of all the prompts are nearly the obtaining overall high agreement: 99.5% agreement for S2Rs

same. The main difference lies in the inputs ( i.e. , combinations ( κ = 0 . 98 , almost perfect agreement [35]; α = 0 . 99 , reliable

of app information elements) and specific instructions to handle agreement [36]) and 87.5% agreement for OBs/EBs ( κ = 0 . 6 ,

them. For example, one S2R generation instruction to handle moderate agreement [35]; α = 0 . 94 , reliable agreement [36]).

the buggy screen is: “Starting from the initial transition [GUI

interaction], i.e. , the “open app” transition, your goal is to reach E. Results and Analysis

the buggy screen by identifying the most relevant transitions 1) Quality of Generated S2Rs: To assess LLM consistency

for the user-reported S2Rs.” An example instruction to handle (producing the same outputs), we compared the evaluation met-

GUI interactions is: “The generated S2Rs must form a valid rics of the configurations across three runs. All configurations

---

## Page 7

| No Info | 80.7 | 34.3 | 28.3 | 70.2 | 74.0 | 72.0 | No Info | 30.3 | 5.3 | 1.7 | 0 | 2.7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Interac. | 95.3 | 14.0 | 13.7 | 87.2 | 87.5 | 87.3 | Buggy Scrn. | 32.3 | 5.3 | 0 | 0 | 2.3 |
| Interac.+Scrn. | 97.7 | 15.0 | 12.3 | 86.7 | 88.8 | 87.7 | S2Rs+Buggy Scrn. | 33.3 | 5.3 | 0.3 | 0 | 1.0 |
| Interac.+Scrn. | S2Rs+Buggy Scrn. |  |  |  |  |  |  |  |  |  |  |  |

+Buggy Scrn. 97.3 13.0 12.3 88.2 88.8 88.5

(MS) in the development bug reports (avg. over three runs)

All three context-aware configurations substantially outperform

( No Info. ) to 87.33–88.49 across the other setups. Notably,

compared to No Info. , using GUI interactions yields a large gain

(F1 87.33 vs 72.02), indicating that this context is essential for

accurately identifying an associated reproduction path. Adding

screen descriptions and/or the buggy screen to GUI interactions

performance achieved by Interac.+Scrn.+BuggyScrn. (F1 88.49,

configurations produce a similar number of correct steps

(95.3–97.7), the best configuration reduces both extra steps

(13.0 vs. 14.0–15.0) and missing steps (12.3 vs. 13.7).

+ Scrns. 34.3 4.3 0 0 1.3

reports (avg. over three runs)

The primary goal of B UG S CRIBE ’s evaluation is to assess

the quality of the generated S2Rs, OBs, and EBs compared to

baseline approaches on a larger dataset of 48 bug reports. Given

this goal, we answer the following research questions (RQs):

• RQ

to baseline and original reports?

• RQ

compared to baseline and original reports?

A. Test Dataset

CS (TP) ES (FP) MS (FN) Precision Recall F1 Score Correct Incomplete Ambiguous Missing Incorrect

Fig. 3: Total # of correct (CS), extra (ES), and missing S2Rs Fig. 4: Total # of OB/EB elements in the development bug

achieved consistent performance across the runs. For instance, (34.3) and fewer incomplete ones (4.3). Across all configura-

the F1 score’s std. deviation in Interac.+Scrn.+BuggyScrn. tions, no OB/EB elements are missing, and results for each

is 0.01, indicating high consistency. Our replication package OB/EB element (not shown in the table, but found in our

provides complete consistency results [16]. replication package [16]) follow the same trends, confirming

Figure 3 shows the S2R quality results of the four configura- that B UG S CRIBE effectively leverages contextual information

tions for S2R generation, averaged across the three executions. to generate high-quality OB and EB descriptions.

| the no-information configuration, with F1 increasing from 72.02 | V. B | UG | S | CRIBE | ’ | S | E | VALUATION |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| leads to small but consistent improvements, with the best | 1 | : | What is the quality of B | UG | S | CRIBE | ’s S2Rs compared |  |
| Precision 88.22, Recall 88.75). While all three context-aware | 2 | : | What is the quality of B | UG | S | CRIBE | ’s OBs/EBs |  |
| Qualitative data analysis shows that including the buggy | We evaluated B | UG | S | CRIBE | with a dataset of 48 bug reports |  |  |  |

screen informs the LLM about the final screen where the bug ( i.e. , a test set , different from the development set), which

manifests, constraining the reproduction path. Since each inter- enables comparison with baseline techniques (Section V-B).

action has source/target screens (see Section III-B3), the target We collected these bug reports via stratified random sampling

screen of the final step should correspond to the buggy screen. across various bug types from 96 reports used in prior

Leveraging this allows the LLM to more accurately align the re- work [24], [6]. These 48 reports span 26 Android applications

ported steps from the original bug report with the actual interac- of various domains (web browsing, WiFi diagnosis, finance

tions, resulting in fewer extra steps, compared to Interac.+Scrn. tracking, etc. ) and cover different bug types: output issues (18),

2) Quality of Generated OBs/EBs: Figure 4 presents the cosmetic problems (12), crashes (12), and navigation bugs (6).

total number of OB/EB elements in the generated 10 bug Corresponding app execution models have an average of 43.4

reports, across the quality categories from our OB/EB quality GUI screens (ranging from 5 to 105; median: 27.5) and 117.5

model, and the four OB/EB generation configurations. All the GUI interactions (ranging from 10 to 282; median: 92.5).

configurations consistently generated OBs/EBs with similar As the bug reports lack the high-quality bug report ground

elements across all three runs (see our replication package for truth needed to evaluate B UG S CRIBE , we manually constructed

the results of all executions [16]). the high-quality OB/EB/S2R ground truth for each bug report

Out of 40 OB/EB elements ( 4 OB/EB elements types following the methodology in Section IV-A2 and Section IV-B2.

× 10 bug reports), we found that all configurations yield We also extracted and assessed the OB/EB information elements

similar results across the quality categories, with correct and S2Rs in the original reports using our quality model to

OB/EB elements ranging from 30.3 ( No Info. ) to 34.3 measure the improvements achieved by B UG S CRIBE . Following

( S2Rs+BuggyScrn.+Scrns. ), and consistently low numbers of in- the same rigorous process used for the development set, two

complete (5.3–4.3), ambiguous (1.7–0), and incorrect elements authors achieved agreement rates of 89.6% for OB/EB and

(2.7–1.3). However, incorporating context (particularly the 93.5% for S2R. In total, this data construction process required

buggy screen, shared across all context-aware configurations) substantial effort: ≈ 204 human hours.

improves element correctness ( e.g. , 32.3–34.3 vs. 30.3). The In summary, the 48 bug reports include 599 atomic S2Rs

best performance is achieved by S2Rs+BuggyScrn.+Scrns. , (12.5 steps per bug), each representing one specific app interac-

which includes buggy screens, generated S2Rs, and screen tion, e.g. , taps, long-taps, etc. They also include the high-quality

descriptions, yielding the highest number of correct elements OB/EB ground truth with the correct information elements.

---

## Page 8

B. Baseline techniques we adopted the following strategies. If there are m atomic steps

We implemented B UG S CRIBE using two state-of-the-art in the generated bug report, and among them n are present in

LLMs, i.e. , GPT-5.4 [18] and C LAUDE O PUS -4.6 [20], result- the ground truth as individual steps, we counted n correct steps.

ing in two variants: BS GPT and BS CLAUDE . Both variants use Moreover, we considered generated steps with different wording

the best context configurations identified during B UG S CRIBE ’s or presentation but similar meaning to the ground truth step as

development: Interac.+Scrn.+BuggyScrn. for S2R generation correct . If multiple steps are implicitly mentioned, we counted

and S2Rs+BuggyScrn.+Scrns. for OB/EB generation. them individually. We also used these strategies to compare

We evaluated both variants against a recent bug report im- the S2R quality of the original bug reports against the ground

provement technique, U2S BR [15]. We also implemented two truth, which is required to compare the reports generated by

baselines (GPT NO - INFO and CLAUDE NO - INFO ) which lever- B UG S CRIBE and the baselines with the original reports using

age the same LLMs without using any app-specific information. our evaluation metrics. A complete comparison protocol to en-

1) GPT NO - INFO and CLAUDE NO - INFO : These baselines sure a fair comparison is found in our replication package [16].

generate bug reports following a similar generation pipeline as

D. Results and Analysis

B UG S CRIBE , including the same prompt templates for S2R and

OB/EB generation. However, these prompt templates do not 1) RQ1 – Quality of S2R Generation: Figure 5 presents the

include the placeholders for app-specific information and the quality results of the S2Rs in the original bug reports and the

specific instructions to handle it, i.e. , the No Info. configuration S2Rs generated by BS GPT , BS CLAUDE , and the baselines.

(see section IV-B for details). We designed this baseline to B UG S CRIBE vs. Baselines and Original Reports. The

understand how GPT-5.4 and C LAUDE O PUS -4.6 perform for table shows that B UG S CRIBE (both BS GPT and BS CLAUDE )

bug report generation without app-specific information. clearly outperforms all baselines and the original bug reports

2) U2S BR : it is an LLM-based approach to transform across all metrics. In particular, it generates substantially

unstructured bug reports into structured bug reports with more correct steps (532, 538 vs. 196, 243, 345, 312) while

explicit OB, EB, and S2Rs [15]. (We refer to this approach as significantly reducing both extra and missing steps ( e.g. , 57, 67

U2S BR .) The original approach uses GPT-4o with three-shot vs. 75, 356 by U2S BR ). This results in large gains in F1 (89.56,

prompting to generate structured bug reports for the given 88.27 vs. 49.12–59.66), demonstrating that B UG S CRIBE

unstructured bug report. To enable a fair comparison, we produces higher-quality S2Rs than all alternatives.

| replaced its GPT-4o model with GPT-5.4. We implemented | These improvements highlight the importance of app context, |
| --- | --- |
| this baseline using the companion replication package [37]. | which enables the LLM to better map S2Rs to reproduction |

paths from the app execution model. While baselines without

C. Methodology and Metrics such context (GPT NO - INFO , CLAUDE NO - INFO , and U2S BR )

We ran B UG S CRIBE and all baseline techniques on the still improve over the original bug reports ( e.g. , F1 61.22, 59.66,

48 bug reports in the test set and generated high-quality bug 53.00 vs. 49.12), they remain far behind B UG S CRIBE . Across

reports for the given original bug reports. Given that our LLMs, BS GPT and BS CLAUDE achieve similar overall perfor-

development experiments found near-perfect consistency in mance, with a slight trade-off: BS CLAUDE achieves slightly

LLM responses under the same inputs across three executions, higher recall (89.82) and more correct steps (538), while BS GPT

we executed all the approaches only once in this evaluation. achieves substantially higher precision (90.32) and fewer extra

To address RQ 1 , we manually compared the generated S2Rs steps (57), indicating more precise S2R generation.

to the ground truth S2Rs following the methodology discussed The lower performance of the baselines stems from the

in Section IV-D2 and computed precision, recall, and F1 lack of context for S2R generation, as they solely rely on

score (Section IV-D1). To answer RQ 2 , we extracted the four user-submitted reports to generate a possible reproduction

information elements from the B UG S CRIBE -generated OBs path. This leads to either missing steps (356 for U2S BR ) or

and EBs and compared them with the ground truth annotations over-generation (183 and 135 extra steps for GPT NO - INFO

manually (Section IV-D2). We counted the bug reports and CLAUDE NO - INFO ). For instance, in bug report #84 [38]

with different quality labels (see Section IV-D1) for each of the Ultrasonic app, the baselines correctly generate “enter

OB/EB element. Overall, the agreement rates between the two the server URL” but introduce unnecessary steps ( e.g. , “enter

evaluators for S2Rs is 97.3% ( κ = 0 . 92 , i.e. , almost perfect the username” and “enter the password” ) and miss required

agreement [35]; α = 0 . 99 , i.e. , reliable agreement [36]), and interactions ( e.g. , “Click OK” and Swipe up” before “Click

for OB/EB is 92.9% ( κ = 0 . 81 , i.e. , moderate agreement [35]; Test Connection” ), whereas BS GPT and BS CLAUDE avoid

α = 0 . 97 , i.e. , reliable agreement [36]). Our replication such errors by leveraging app-specific information.

package includes the agreement results for each approach [16]. B UG S CRIBE ’s superior performance stems from combining

Comparison Protocol. As GPT NO - INFO , CLAUDE NO - multiple app information types: GUI interactions, screen

INFO , and U2S BR do not use application information and descriptions, and the buggy screen. GUI interactions constrain

are not designed to generate atomic S2Rs, they can produce the LLM to valid user actions, screen descriptions provide

compound S2Rs ( i.e. , multiple steps in one S2R sentence), source and target context for each interaction, and the buggy

contain different wording than the application vocabulary, or screen anchors the final state of the reproduction scenario.

implicitly mention multiple steps. To ensure a fair comparison, Together, these signals enable the LLM to identify valid

---

## Page 9

| Original BR | 80.7 | 3 | 80.7 | 403 | 98.5 | 32.7 | 49.1 | Original BR | 46 | 1 | 1 | 1 | 1 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| U2S | BR | 243 | 75 | 356 | 76.4 | 40.6 | 53.0 | Buggy | U2S | BR | 45 | 3 | 0 | 0 | 0 |
| GPT | No-Info | 345 | 183 | 254 | 65.3 | 57.6 | 61.2 | Behavior | GPT | No-Info | 43 | 3 | 0 | 0 | 2 |
| CLAUDE | No-Info | 312 | 135 | 287 | 69.8 | 52.1 | 59.7 | (OB) | CLAUDE | No-Info | 46 | 1 | 0 | 0 | 1 |
| BS | GPT | 532 | 57 | 67 | 90.3 | 88.8 | 89.6 | BS | GPT | 46 | 0 | 0 | 0 | 2 |  |
| BS | CLAUDE | 538 | 82 | 61 | 86.9 | 89.8 | 88.3 | BS | CLAUDE | 46 | 1 | 0 | 0 | 1 |  |
| CS (TP) | ES (FP) | MS (FN) | Precision | Recall | F1 Score | Original BR | 28 | 3 | 1 | 16 | 0 |  |  |  |  |
| Fig. 5: Total # of correct (CS), extra (ES), and missing S2Rs | Triggering | U2S | BR | 21 | 10 | 2 | 11 | 4 |  |  |  |  |  |  |  |

and generate accurate S2Rs aligned with the reported bug.

Analysis of Failed Cases. Despite substantial improvements,

produce 57 and 82 extra steps, respectively. Our qualitative

user reports with incomplete or ambiguous steps, and (3)

ground truth steps). With insufficient information, B UG S CRIBE

tends to produce a shorter but suboptimal path. Addressing this

2) RQ2: Quality of OB/EB Generation.: Figure 6 shows the

number of OB/EB information elements in the original bug

The table shows results for each individual OB/EB element

type, with elements categorized by their quality category.

GUI

Action

| CLAUDE | 36 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| (OB) | No-Info | 10 | 1 | 0 | 1 |  |
| BS | GPT | 43 | 2 | 0 | 0 | 3 |
| Original BR | 12 | 3 | 1 | 32 | 0 |  |

Buggy

U2S 10

GPT

| Screen | No-Info | 22 | 4 | 2 | 12 | 7 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (OB) | CLAUDE | No-Info | 30 | 0 | 5 | 6 | 7 |
| Original BR | 36 | 1 | 1 | 10 | 0 |  |  |

(EB)

| BS | CLAUDE | 47 | 1 | 0 | 0 | 0 |
| --- | --- | --- | --- | --- | --- | --- |
| Original BR | 122 | 8 | 3 | 59 | 0 |  |
| U2S | BR | 123 | 14 | 8 | 34 | 13 |
| BS | CLAUDE | 165 | 11 | 4 | 3 | 9 |
| Correct | Incomplete | Ambiguous | Missing | Incorrect |  |  |

| (MS) in the test set bug reports | GPT | No-Info | 36 | 7 | 0 | 0 | 5 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| execution paths from the initial screen to the buggy screen | BS | CLAUDE | 37 | 9 | 0 | 1 | 1 |  |  |  |  |
| BS | GPT | and | BS | CLAUDE | still miss 67 and 61 steps and | Reference | BR | 1 | 5 | 23 | 9 |
| analysis of these cases reveals three main causes: (1) multiple | BS | GPT | 29 | 5 | 1 | 0 | 11 |  |  |  |  |
| feasible paths in the app execution model, (2) very low-quality | BS | CLAUDE | 35 | 0 | 4 | 2 | 7 |  |  |  |  |
| inaccuracies in buggy screen localization. For example, bug | Intended | U2S | BR | 47 | 0 | 1 | 0 | 0 |  |  |  |
| report #1402 [39] (Phimp.me app) contains only one vague step | Behavior | GPT | No-Info | 41 | 5 | 0 | 0 | 2 |  |  |  |
| ( | “Try with different images in share activity” | ), leading BS | GPT | CLAUDE | No-Info | 47 | 1 | 0 | 0 | 0 |  |
| and BS | CLAUDE | to generate only 6 and 8 correct steps (vs. 13 | BS | GPT | 41 | 5 | 0 | 0 | 2 |  |  |
| limitation may require combining LLM reasoning with path- | Total | GPT | No-Info | 142 | 19 | 2 | 12 | 16 |  |  |  |
| finding techniques and human-in-the-loop approaches [2] to | CLAUDE | No-Info | 159 | 12 | 6 | 6 | 9 |  |  |  |  |
| better identify correct interaction paths associated with the bug. | BS | GPT | 158 | 12 | 1 | 0 | 19 |  |  |  |  |
| reports and the reports generated using different approaches. | Fig. 6: Total # of OB/EB elements in the 48 test set reports |  |  |  |  |  |  |  |  |  |  |

B UG S CRIBE vs. Baselines and Original Reports. The bug reports, increasing the number of correct elements ( e.g. ,

results vary depending across the individual OB/EB elements. 158–165 vs. 122) and reducing the number of missing ones (0–3

(As U2S BR was not designed to include triggering GUI vs. 59), though with slight increases in incomplete and incorrect

interaction and buggy screen reference, we abstain from cases. Compared to the baselines, BS CLAUDE achieves the

comparing B UG S CRIBE with U2S BR for these two elements.) best overall balance (165 correct, 3 missing), outperforming all

For Buggy Behavior (OB) , all approaches perform similarly approaches across most metrics, while BS GPT also performs

( e.g. , 46 correct elements, out of 48), indicating limited impact strongly but with slightly more incorrect elements. Notably,

of app-specific context on generating this element. This can be CLAUDE NO - INFO performs comparatively (with 159 correct

explained by the fact that the buggy behavior is typically present elements), approaching BS GPT , suggesting that while context

in original reports. In contrast, for the OB’s Triggering GUI is beneficial, the choice of LLM also influences performance.

Interaction , B UG S CRIBE performs better, especially BS GPT , Analysis of Failed Cases. Manual inspection of the incom-

generating more correct elements (43 by BS GPT ) than the plete and incorrect triggering GUI interactions generated by BS-

baselines and reducing missing or incomplete cases. For GPT /BS CLAUDE reveals that extra or unnecessary reproduction

the OB’s Buggy Screen Reference , results are mixed, but steps in the original bug report can misguide B UG S CRIBE . For

BS CLAUDE achieves the highest performance (35 correct, 2 example, bug report #1066 [40] (Focus-android app) contains

missing elements), while BS GPT still improves over original the line: “Repeat moving cursor and clicking system status

reports (29 vs. 12). For Intended Behavior (EB) , B UG S CRIBE bar...” , where the user attempted to circumvent the bug. This

performs comparably to the baselines, suggesting that context is operation is not a part of the reproduction steps; however,

less important, as intended behavior can often be inferred from B UG S CRIBE considers this as the triggering GUI interaction,

the buggy behavior, which appears in 46 of the original reports. resulting in an incomplete/incorrect element.

Overall, B UG S CRIBE improves substantially over original We analyzed the ambiguous buggy screen references gen-

---

## Page 10

erated by B UG S CRIBE and found that, although imprecise, reasoning on the provided bug report and app-specific execution

they refer to the correct buggy screens. These ambiguities information, rather than on knowledge acquired during training.

arise because B UG S CRIBE often uses generic, functionality- External Validity. The results may or may not generalize to

based names rather than the exact UI wording. For instance, in bug reports and apps outside from our datasets. However, these

bug report #154 for the Camfahrplan app [41], the correct datasets contain bug reports of various bug types ( e.g. , crashes,

buggy screen is “schedule screen” , whereas BS CLAUDE UI issues, navigation problems, etc. ) and 26 Android apps

refers to it as “event details screen” . This discrepancy stems of various kinds ( e.g. , web browsing, WiFi diagnosis, finance

from limitations in the app metadata used to build the app tracking, etc. ) and sizes. B UG S CRIBE is developed using

execution model, which may omit or differ from the user- a distinct dataset, i.e. , a development set of 10 bug reports

visible screen names, prompting B UG S CRIBE to infer names from nine apps of various domains ( e.g. , file management,

from the UI screen descriptions used as context. To address multimedia, etc. ) and different bug types. B UG S CRIBE ’s

this, our future work will incorporate visual information from evaluation using a different data set (the test set) and the fact

UI screenshots via multimodal models to improve screen that the quality results between both datasets are similar gives

naming. Besides ambiguous cases, incorrect buggy screens confidence in the generalizability of the results.

were primarily generated because the buggy screen localization

VII. R ELATED W ORK

phase failed to identify the correct buggy screen. Our future

work will experiment with the inclusion of multiple buggy Bug reports have been studied for various purposes,

screen suggestions, i.e. , not only leverage the most suspicious such as understanding bug resolution process [42],

screen detected by the localization phase as context. bug management [43], [24], [44], [45], [46], detecting

3) Computational Cost: We measured the end-to-end cost duplicates [47], [48], [49], [50], [51], [52], predicting priority

of B UG S CRIBE . On average, BS GPT processes 121.8K input and severity [53], [54], [55], localizing faulty code [56], [57],

and 9.0K output tokens, costing $0.44 and taking 135 seconds [58], [59], identifying solution discussions [60], classifying bug

( < 2.3 mins) per bug report. BS CLAUDE processes 154.8K input types [61], [62], reproducing bugs [63], [64], [65], and more.

and 5.6K output tokens, costing $0.92 and taking 128 seconds. Bug Report Quality Assessment and Interactive Bug

Detailed cost data is found in our replication package [16]. Reporting. Past research has proposed methods to assess bug

report quality from multiple angles, including lexical analysis

VI. T HREATS TO V ALIDITY ( e.g. , readability) [66], [67], [4] and presence of bug information

( e.g. , patches and screenshots) [4], [6]. The most related to

Construct Validity. The manual construction of high-quality work is by Chaparro et al. [6], who proposed E ULER to evaluate

ground truth OB, EB, and S2Rs and the manual evaluation of S2R quality via heuristics that map keywords in reports to app

generated bug reports may introduce subjectivity. To mitigate UI information. More recently, Mahmud et al. [9] introduced

this, two authors performed these tasks using well-defined, A STRO BR, which uses LLMs to assess S2R quality. Imran et

replicable procedures. In-depth discussion sessions were al. [68] aimed to enhance incomplete reports by generating

conducted to resolve the misunderstandings and disagreements. follow-up clarification questions to developers.

We further quantified the consistency of their work by Other work has investigated interactive bug reporting

computing inter-rater agreement, which was consistently methods. Song et al. introduced the chatbot B URT [2], [12] to

very high across all cases, reinforcing the reliability of guide reporters during submission, verifying bug information

B UG S CRIBE ’s development and evaluation. quality in real time and providing improvement suggestions.

Internal Validity. The performance of B UG S CRIBE can Moran et al. presented F USION [14], which enabled reporters

vary depending on the wording and structure of the prompt to construct structured reports by selecting actions and GUI

templates. To mitigate this, we systematically designed the components from drop-down lists. Fazzini et al. proposed

templates following the best practices [28], [29], [30] and EB UG [13], which extends F USION [14] by suggesting S2Rs

evaluated the prompts with different configurations on the to reporters in addition to dropdown-based selections.

development dataset. LLM non-determinism may cause results These methods provide feedback on problematic bug

to fluctuate across executions. We addressed this by running report content but leave corrections to end-users, rather

our development experiments three times, reporting consistent than automatically improving reports via LLM-provided app

results across runs. While the baselines were not designed to context as B UG S CRIBE does.

produce atomic S2Rs, we applied consistent and transparent Bug Report Quality Improvement. Prior research on

rules to ensure a fair comparison with B UG S CRIBE , document- enhancing the bug report quality has primarily focused on de-

ing our procedure to ensure reproducibility. tecting missing components ( e.g. , OB/EB/S2R) and generating

B UG S CRIBE ’s development and evaluation use public structured reports by leveraging LLMs. For instance, Acharya

bug reports and Android projects, so LLMs may have seen et al. [15] proposed an LLM-based technique to transform

related content during training. While this threat cannot be unstructured bug summaries into structured reports with explicit

eliminated, all evaluated approaches use the same LLMs on the OB, EB, and S2Rs. Bo et al. [11] introduced ChatBR, which

same benchmark, making bias toward B UG S CRIBE unlikely. first identifies components completely missing in the report

Moreover, B UG S CRIBE is designed to guide the LLM to base its using a fine-tuned BERT classifier and then employs an

---

## Page 11

LLM to generate the missing content. Compared to these [11] L. Bo, W. Ji, X. Sun, T. Zhang, X. Wu, and Y. Wei, “Chatbr: Automated

approaches, B UG S CRIBE formulates bug report enhancement assessment and improvement of bug report quality using chatgpt,”

in Proceedings of the 39th IEEE/ACM International Conference on

as the problem of connecting user-written bug reports with Automated Software Engineering , 2024, p. 1472–1483.

application execution. It links report information to relevant [12] Y. Song, J. Mahmud, N. De Silva, Y. Zhou, O. Chaparro, K. Moran,

app execution elements and leverages a component-specific A. Marcus, and D. Poshyvanyk, “Burt: A chatbot for interactive

bug reporting,” in Proceedings of the 45th IEEE/ACM International

grounding strategy that supplies the most appropriate execution Conference on Software Engineering (ICSE’23) , 2023, pp. 170–174.

context for LLM reasoning. As a result, B UG S CRIBE generates [13] M. Fazzini, K. Moran, C. Bernal-C´ ardenas, T. Wendland, A. Orso, and

more accurate, complete, and correct OB, EB, and S2Rs than D. Poshyvanyk, “Enhancing mobile app bug reporting via real-time

understanding of reproduction steps,” IEEE Transactions on Software

approaches that rely primarily on the bug report text. Other Engineering , vol. 49, no. 3, p. 1246–1272, Mar. 2023.

work has used LLMs to analyze bug reports and recommend [14] K. Moran, M. Linares-V´ asquez, C. Bernal-C´ ardenas, and D. Poshyvanyk,

relevant screenshots [69] and user reviews [70], generate bug “Auto-completing Bug Reports for Android Applications,” in Proceedings

of the Joint Meeting on Foundations of Software Engineering (FSE’15) ,

reports based on chat conversions [71], classify report sentences 2015, pp. 673–686.

into templates [72], and generate issue report templates [73]. [15] J. Acharya and G. Ginde, “Can we enhance bug report quality using

llms?: An empirical study of llm-based bug report generation,” arXiv

VIII. C ONCLUSIONS preprint arXiv:2504.18804 , 2025.

[16] “Online replication package,” https://zenodo.org/records/21089393, 2026.

We showed that automatic bug report enhancement can [17] “Atimetracker bug report 35 - https://github.com/netmackan/

be formulated as the problem of connecting user-written ATimeTracker/issues/35,” 2025.

bug reports with application execution. By linking report [18] OpenAI, “Introducing GPT-5.4,” https://openai.com/index/

introducing-gpt-5-4/, March 2026, accessed: 2026-03-26.

information to relevant app execution elements through a [19] “Introducing gpt-5.4 - https://openai.com/index/introducing-gpt-5-4/

component-specific grounding strategy, B UG S CRIBE enables ?utm source=chatgpt.com,” 2026.

LLMs to generate accurate, complete, and correct OB, EB, and [20] Anthropic, “Claude opus 4.6,” https://platform.claude.com/docs/en/

about-claude/models/overview, 2025, accessed: 2026-03-26.

S2Rs. Our results show that B UG S CRIBE consistently produces [21] K. Moran, M. Linares-V´ asquez, C. Bernal-C´ ardenas, C. Vendome, and

higher-quality bug reports than the original reports and existing D. Poshyvanyk, “Automatically discovering, reporting and reproducing

LLM-based approaches that rely primarily on bug report text. android application crashes,” in Proceedings of the IEEE International

Conference on Software Testing, Verification and Validation (ICST) , 2016,

pp. 33–44.

R EFERENCES

[22] K. Moran, M. Linares-Vasquez, C. Bernal-Cardenas, C. Vendome, and

| [1] | J. Johnson, J. Mahmud, T. Wendland, K. Moran, J. Rubin, and M. Fazzini, | D. Poshyvanyk, “Crashscope: A practical tool for automated testing of |  |
| --- | --- | --- | --- |
| “An empirical investigation into the reproduction of bug reports for android | android applications,” in | Proceedings of the 39th IEEE/ACM International |  |
| apps,” in | 2022 IEEE International Conference on Software Analysis, | Conference on Software Engineering Companion (ICSE-C) | , 2017, pp. |
| Evolution and Reengineering (SANER) | . | IEEE, 2022, pp. 321–322. | 15–18. |

[2] Y. Song, J. Mahmud, Y. Zhou, O. Chaparro, K. Moran, A. Marcus, [23] M. Du, S. Yu, C. Fang, T. Li, H. Zhang, and Z. Chen, “Semcluster: a

| and D. Poshyvanyk, “Toward interactive bug reporting for (android app) | semi-supervised clustering tool for crowdsourced test reports with deep |  |  |
| --- | --- | --- | --- |
| end-users,” in | Proceedings of the 30th ACM Joint European Software | image understanding,” in | Proceedings of the 30th ACM Joint European |
| Engineering Conference and Symposium on the Foundations of Software | Software Engineering Conference and Symposium on the Foundations of |  |  |
| Engineering | , 2022, pp. 344–356. | Software Engineering | , 2022, pp. 1756–1759. |

[3] N. Bettenburg, S. Just, A. Schr¨ oter, C. Weiss, R. Premraj, and T. Zim- [24] A. Saha, Y. Song, J. Mahmud, Y. Zhou, K. Moran, and O. Chaparro,

| mermann, “What makes a good bug report?” in | Proceedings of the 16th | “Toward the automated localization of buggy mobile app uis from bug |  |
| --- | --- | --- | --- |
| ACM SIGSOFT International Symposium on Foundations of Software | descriptions,” in | Proceedings of the 33rd ACM SIGSOFT International |  |
| Engineering | , 2008, p. 308–318. | Symposium on Software Testing and Analysis | , 2024, pp. 1249–1261. |

[4] T. Zimmermann, R. Premraj, N. Bettenburg, S. Just, A. Schroter, and [25] T. Khot, H. Trivedi, M. Finlayson, Y. Fu, K. Richardson, P. Clark, and

C. Weiss, “What makes a good bug report?” IEEE Transactions on A. Sabharwal, “Decomposed prompting: A modular approach for solving

Software Engineering , vol. 36, no. 5, pp. 618–643, 2010. complex tasks,” arXiv preprint arXiv:2210.02406 , 2022.

[5] O. Chaparro, J. Lu, F. Zampetti, L. Moreno, M. Di Penta, A. Marcus, [26] D. Dua, S. Gupta, S. Singh, and M. Gardner, “Successive prompting

| G. Bavota, and V. Ng, “Detecting missing information in bug descriptions,” | for decomposing complex questions,” | arXiv preprint arXiv:2212.04092 | , |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| in | Proceedings of the 11th Joint Meeting on the Foundations of Software | 2022. |  |  |  |  |  |  |  |  |  |  |
| Engineering (ESEC/FSE’17) | , 2017, pp. 396–407. | [27] | “Prompt | engineering | - | https://platform.openai.com/docs/guides/ |  |  |  |  |  |  |
| [6] | O. | Chaparro, | C. | Bernal-C´ | ardenas, | J. | Lu, | K. | Moran, | A. | Marcus, | prompt-engineering,” 2025. |

M. Di Penta, D. Poshyvanyk, and V. Ng, “Assessing the quality of the [28] J. White, S. Hays, Q. Fu, J. Spencer-Smith, and D. C. Schmidt, “Chatgpt

| steps to reproduce in bug reports,” in | Proceedings of the 27th ACM Joint | prompt patterns for improving code quality, refactoring, requirements |  |  |
| --- | --- | --- | --- | --- |
| Meeting on European Software Engineering Conference and Symposium | elicitation, and software design,” in | Generative AI for Effective Software |  |  |
| on the Foundations of Software Engineering | , 2019, p. 86–96. | Development | . | Springer, 2024, pp. 71–108. |

[7] P. J. Guo, T. Zimmermann, N. Nagappan, and B. Murphy, “Characterizing [29] E. Santana Jr, G. Benjamin, M. Araujo, H. Santos, D. Freitas, E. Almeida,

| and predicting which bugs get fixed: an empirical study of microsoft | P. A. d. Neto, J. Li, J. Chun, and I. Ahmed, “Which prompting technique |  |  |  |
| --- | --- | --- | --- | --- |
| windows,” in | Proceedings of the 32nd International Conference on | should i use? an empirical investigation of prompting techniques for |  |  |
| Software Engineering | , 2010, pp. 495–504. | software engineering tasks,” | arXiv preprint arXiv:2506.05614 | , 2025. |

[8] T. Zimmermann, N. Nagappan, P. J. Guo, and B. Murphy, “Characterizing [30] S. Schulhoff, M. Ilie, N. Balepur, K. Kahadze, A. Liu, C. Si, Y. Li,

| and | predicting | which | bugs | get | reopened,” | in | Proceedings | of | the | A. Gupta, H. Han, S. Schulhoff | et al. | , “The prompt report: a sys- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| International Conference on Software Engineering (ICSE’12) | , 2012, | tematic | survey | of | prompt | engineering | techniques,” | arXiv | preprint |  |  |  |
| pp. 1074–1083. | arXiv:2406.06608 | , 2024. |  |  |  |  |  |  |  |  |  |  |

[9] J. Mahmud, A. Saha, O. Chaparro, K. Moran, and A. Marcus, “Combining [31] Y. Zhang, Y. Yuan, and A. C.-C. Yao, “Meta prompting for ai systems,”

language and app ui analysis for the automated assessment of bug arXiv preprint arXiv:2311.11482 , 2023.

reproduction steps,” arXiv preprint arXiv:2502.04251 , 2025. [32] “Openai api - https://openai.com/api/,” 2025.

[10] Y. Song and O. Chaparro, “Bee: A tool for structuring and analyzing bug [33] J. Cohen, “A coefficient of agreement for nominal scales,” Educational

reports,” in Proceedings of the 28th ACM Joint Meeting on European and Psychological Measurement , vol. 20, no. 1, pp. 37–46, 1960.

Software Engineering Conference and Symposium on the Foundations of [34] K. Krippendorff, Content analysis: An introduction to its methodology .

Software Engineering , 2020, pp. 1551–1555. Sage publications, 2018.

---

## Page 12

[35] A. J. Viera, J. M. Garrett et al. , “Understanding interobserver agreement: [56] J. M. Florez, O. Chaparro, C. Treude, and A. Marcus, “Combining query

| the kappa statistic,” | Fam med | , vol. 37, no. 5, pp. 360–363, 2005. | reduction and expansion for text-retrieval-based bug localization,” in |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [36] | G. | Marzi, | M. | Balzano, | and | D. | Marchiori, | “K-alpha | calculator– | 2021 IEEE International Conference on Software Analysis, Evolution |
| krippendorff’s alpha calculator: a user-friendly tool for computing | and Reengineering (SANER) | . | IEEE, 2021, pp. 166–176. |  |  |  |  |  |  |  |

krippendorff’s alpha inter-rater reliability coefficient,” MethodsX , vol. 12, [57] O. Chaparro, J. M. Florez, and A. Marcus, “Using bug descriptions

| p. 102545, 2024. | to reformulate queries during text-retrieval-based bug localization,” |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [37] | “U2s-br replication package,” https://github.com/GindeLab/Ease 2025 | Empirical Software Engineering | , vol. 24, pp. 2947–3007, 2019. |  |  |  |  |
| AI model, 2025. | [58] | ——, “Using observed behavior to reformulate queries during text |  |  |  |  |  |
| [38] | “Ultrasonic bug report 84 - https://github.com/ultrasonic/ultrasonic/issues/ | retrieval-based bug localization,” in | 2017 IEEE International Conference |  |  |  |  |
| 187,” 2026. | on Software Maintenance and Evolution (ICSME) | . | IEEE, 2017, pp. |  |  |  |  |
| [39] | “Phimp.me | bug | report | 1402 | - | https://github.com/fossasia/ | 376–387. |
| phimpme-android/issues/1039,” 2026. | [59] | O. Chaparro and A. Marcus, “On the reduction of verbose queries in |  |  |  |  |  |
| [40] | “Focus-android bug report 1066 - https://github.com/mozilla-mobile/ | text retrieval based software maintenance,” in | Proceedings of the 38th |  |  |  |  |
| focus-android/issues/3152,” 2026. | International Conference on Software Engineering Companion | , 2016, pp. |  |  |  |  |  |
| [41] | “Camfahrplan | bug | report | 154 | - | https://github.com/tuxmobil/ | 716–718. |
| CampFahrplan/issues/154,” 2026. | [60] | A. Saha, M. Sun, and O. Chaparro, “Automatically identifying solution- |  |  |  |  |  |
| [42] | A. Saha and O. Chaparro, “Decoding the issue resolution process in | related content in issue report discussions with language models,” | arXiv |  |  |  |  |
| practice via issue report analysis: A case study of firefox,” in | Proceedings | preprint arXiv:2511.06501 | , 2025. |  |  |  |  |

of the IEEE/ACM 47th International Conference on Software Engineering [61] K. Somasundaram and G. C. Murphy, “Automatic categorization of bug

| (ICSE’25) | , 2025. | reports using latent dirichlet allocation,” in | Proceedings of the 5th India |
| --- | --- | --- | --- |
| [43] | A. Saha, “Studying and automating issue resolution for software quality,” | software engineering conference | , 2012, pp. 125–130. |
| arXiv preprint arXiv:2512.10238 | , 2025. | [62] | G. Catolino, F. Palomba, A. Zaidman, and F. Ferrucci, “Not all bugs |
| [44] | A. Adnan, A. Saha, and O. Chaparro, “Sprint: An assistant for issue | are the same: Understanding, characterizing, and classifying bug types,” |  |
| report management,” | Proceedings of the 22nd IEEE/ACM International | Journal of Systems and Software | , vol. 152, pp. 165–181, 2019. |
| Conference on Mining Software Repositories (MSR’25) | , 2025. | [63] | S. Feng and C. Chen, “Prompting is all you need: Automated android |
| [45] | W. Zou, D. Lo, Z. Chen, X. Xia, Y. Feng, and B. Xu, “How practi- | bug replay with large language models,” in | Proceedings of the 46th |
| tioners perceive automated bug report management techniques,” | IEEE | IEEE/ACM International Conference on Software Engineering | , 2024. |

Transactions on Software Engineering , vol. 46, no. 8, pp. 836–862, 2018. [64] D. Wang, Y. Zhao, S. Feng, Z. Zhang, W. G. J. Halfond, C. Chen,

| [46] | J. Mahmud, N. De Silva, S. A. Khan, S. H. Mostafavi, S. M. H. Mansur, | X. Sun, J. Shi, and T. Yu, “Feedback-driven automated whole bug |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| O. Chaparro, A. A. Marcus, and K. Moran, “On using gui interaction | report reproduction for android apps,” in | Proceedings of the 33rd ACM |  |  |  |  |  |  |  |  |
| data to improve text retrieval-based bug localization,” in | Proceedings of | SIGSOFT International Symposium on Software Testing and Analysis | , |  |  |  |  |  |  |  |
| the 46th IEEE/ACM International Conference on Software Engineering | , | 2024, p. 1048–1060. |  |  |  |  |  |  |  |  |
| 2024. | [65] | M. Fazzini, M. Prammer, M. d’Amorim, and A. Orso, “Automatically |  |  |  |  |  |  |  |  |
| [47] | Y. Yan, N. Cooper, O. Chaparro, K. Moran, and D. Poshyvanyk, | translating bug reports into test cases for mobile apps,” in | Proceedings |  |  |  |  |  |  |  |
| “Semantic gui scene learning and video alignment for detecting duplicate | of the 27th International Symposium on Software Testing and Analysis |  |  |  |  |  |  |  |  |  |
| video-based | bug | reports,” | in | Proceedings | of | the | IEEE/ACM | 46th | (ISSTA’18) | , 2018, pp. 141–152. |
| International Conference on Software Engineering | , 2024, pp. 1–13. | [66] | B. Dit and A. Marcus, “Improving the readability of defect reports,” in |  |  |  |  |  |  |  |
| [48] | J. Zhou and H. Zhang, “Learning to rank duplicate bug reports,” in | Proceedings of the 2008 International Workshop on Recommendation |  |  |  |  |  |  |  |  |
| CIKM’12 | , 2012, pp. 852–861. | Systems for Software Engineering (RSSE) | , pp. 47–49. |  |  |  |  |  |  |  |

[49] J. He, L. Xu, M. Yan, X. Xia, and Y. Lei, “Duplicate bug report detection [67] E. Linstead and P. Baldi, “Mining the coherence of gnome bug

| using dual-channel convolutional neural networks,” in | Proceedings of | reports with statistical topic models,” in | Proceedings of the 6th IEEE |
| --- | --- | --- | --- |
| the 28th International Conference on Program Comprehension | , 2020, | International Working Conference on Mining Software Repositories | , 2009, |
| pp. 117–127. | pp. 99–102. |  |  |

[50] N. Cooper, C. Bernal-C´ ardenas, O. Chaparro, K. Moran, and D. Poshy- [68] M. M. Imran, A. Ciborowska, and K. Damevski, “Automatically selecting

| vanyk, “It takes two to tango: Combining visual and textual information | follow-up questions for deficient bug reports,” in | 2021 IEEE/ACM 18th |  |  |
| --- | --- | --- | --- | --- |
| for detecting duplicate video-based bug reports,” in | 2021 IEEE/ACM | International Conference on Mining Software Repositories (MSR) | , 2021, |  |
| 43rd International Conference on Software Engineering (ICSE) | . | IEEE, | pp. 167–178. |  |
| 2021, pp. 957–969. | [69] | X. Tan, D. Yadav, F. Ahmed, and M. Nayebi, “Imager: Enhancing bug |  |  |
| [51] | O. Chaparro, J. M. Florez, U. Singh, and A. Marcus, “Reformulating | report clarity by screenshots,” | arXiv preprint arXiv:2505.01925 | , 2025. |

queries for duplicate bug report detection,” in 2019 IEEE 26th inter- [70] A. Pilone, M. Raglianti, M. Lanza, F. Kon, and P. Meirelles, “Auto-

national conference on software analysis, evolution and reengineering matically augmenting github issues with informative user reviews,” in

(SANER) . IEEE, 2019, pp. 218–229. Proceedings , no. accepted paper preprint ju 2025, 2025, pp. 1–12.

[52] O. Chaparro, J. M. Florez, and A. Marcus, “On the vocabulary agreement [71] L. Shi, F. Mu, Y. Zhang, Y. Yang, J. Chen, X. Chen, H. Jiang, Z. Jiang,

| in software issue descriptions,” in | Proceedings of the IEEE International | and Q. Wang, “Buglistener: identifying and synthesizing bug reports |  |  |
| --- | --- | --- | --- | --- |
| Conference on Software Maintenance and Evolution | . | IEEE, 2016, pp. | from collaborative live chats,” in | Proceedings of the 44th international |
| 448–452. | conference on software engineering | , 2022, pp. 299–311. |  |  |

[53] Q. Umer, H. Liu, and I. Illahi, “Cnn-based automatic prioritization of bug [72] J. Zhang, M. Peng, and Y. Zhang, “An empirical study of transformer

| reports,” | IEEE Transactions on Reliability | , vol. 69, no. 4, pp. 1341–1354, | models on automatically templating github issue reports,” in | 2025 |
| --- | --- | --- | --- | --- |
| 2019. | IEEE International Conference on Software Analysis, Evolution and |  |  |  |
| [54] | Y. Tian, D. Lo, X. Xia, and C. Sun, “Automated prediction of bug report | Reengineering (SANER) | . | IEEE, 2025, pp. 615–626. |

priority using multi-factor analysis,” Empirical Software Engineering , [73] N. Nikeghbal, A. H. Kargaran, and A. Heydarnoori, “Girt-model:

| vol. 20, pp. 1354–1383, 2015. | Automated generation of issue report templates,” in | Proceedings of the |  |
| --- | --- | --- | --- |
| [55] | Z. Huang, Z. Shao, G. Fan, H. Yu, K. Yang, and Z. Zhou, “Bug report | 21st International Conference on Mining Software Repositories | , 2024, |
| priority prediction using developer-oriented socio-technical features,” in | pp. 407–418. |  |  |

Proceedings of the 13th Asia-Pacific symposium on internetware , 2022,

pp. 202–211.
