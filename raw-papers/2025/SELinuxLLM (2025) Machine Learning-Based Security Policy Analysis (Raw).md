---
title: "V_M_SELinux_LLM_2025"
creator: "PDFium"
pages: 9
---

# V_M_SELinux_LLM_2025

> **總頁數**：9 頁

---

## Page 1

Machine Learning-Based Security Policy Analysis

| Krish Jain | Joann Sum | Pranav Kapoor | Dr. Amir Eaman |
| --- | --- | --- | --- |
| Department of Computer Science | Department of Computer Science | Department of Computer Science | Department of Computer Science |
| University of Rochester | California State University, | Acadia University | Acadia University |
| Rochester, USA | Fullerton | Wolfville, CA | Wolfville, CA |
| kjain7@u.rochester.edu | Fullerton, USA | 157998k@acadiau.ca | amir.eaman@acadiau.ca |

Josum@csu.fullerton.edu

capture the complex relationships inherent in SELinux policies.

Here we present a novel approach combining graph-based policy

representation with neural networks to automate SELinux policy

analysis. Our method transforms policies into graph structures

where nodes represent security contexts and edges capture access

production systems, we show that our method effectively captures

Neo4j, LSMs, anomaly detection

I. I NTRODUCTION

Security-Enhanced Linux (SELinux) implements mandatory

©2024 IEEE

practitioners to interpret and apply effectively. The SETools

suite [6] forms the foundation of basic analysis, providing

several key utilities: apol[] offers a graphical interface for

exploring and analyzing SELinux policies, allowing users to

granularity of policy specifications. Formal models like SELAC

widespread use. This research addresses these gaps by offering a

graph-based technique that simplifies the analysis process while

maintaining precision.

promise in identifying anomalous patterns in complex policies.

| Abstract | — | Analysis of Security-Enhanced Linux (SELinux) | Current SELinux policy analysis tools span a range of |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| policies requires extensive manual effort to identify violations and | approaches. | Mathematical | proof-based | analysis | tools | often |  |  |  |  |  |  |
| security misconfigurations. Current tools employ mathematical | introduce additional layers of abstraction, translating policies |  |  |  |  |  |  |  |  |  |  |  |
| abstractions that, while theoretically sound, produce outputs that | first into mathematical logic and then into mathematical models |  |  |  |  |  |  |  |  |  |  |  |
| practitioners | struggle | to | interpret | effectively. | Automated | before generating results [3]. This multi-step process, while |  |  |  |  |  |  |
| approaches using machine learning have shown promise but fail to | theoretically sound, produces outputs that are difficult for |  |  |  |  |  |  |  |  |  |  |  |
| relationships, then applies Node2vec to learn continuous feature | examine policy components like types, classes, and rules; |  |  |  |  |  |  |  |  |  |  |  |
| representations that preserve policy neighborhoods and violation | seinfo[] | provides | command-line | access | to | statistics | and |  |  |  |  |  |
| patterns. We develop a flexible policy analysis framework that | summaries of policy components; and SEsearch enables detailed |  |  |  |  |  |  |  |  |  |  |  |
| processes these representations through Random Forest, Support | searching of policy rules with flexible criteria [3]. For policy |  |  |  |  |  |  |  |  |  |  |  |
| Vector | Machine | (SVM), | and | Multi-Layer | Perceptron | (MLP) | management, | tools | like | audit2allow, | which | automatically |
| models to detect violations. Our experimental results demonstrate | generates policy rules from denied operations in audit logs, and |  |  |  |  |  |  |  |  |  |  |  |
| that this approach achieves 95% accuracy in identifying security | Semanage, which facilitates the creation and modification of |  |  |  |  |  |  |  |  |  |  |  |
| violations while maintaining balanced precision and recall metrics, | SELinux policy modules without requiring detailed policy |  |  |  |  |  |  |  |  |  |  |  |
| significantly outperforming existing analysis techniques. Through | language knowledge, enable iterative policy refinement based |  |  |  |  |  |  |  |  |  |  |  |
| extensive evaluation on synthetic policy datasets derived from | on system behavior and modular policy administration [3]. |  |  |  |  |  |  |  |  |  |  |  |
| diverse violation patterns including separation of duty violations, | Previous efforts, such as Efremov and Shchepetkov’s work |  |  |  |  |  |  |  |  |  |  |  |
| domain | transition | issues, | and | unauthorized | access | paths. | on runtime verification [12], underscore the need for tools that |  |  |  |  |  |
| Together, our work presents an efficient approach for automated, | can map high-level security goals onto lower-level system |  |  |  |  |  |  |  |  |  |  |  |
| interpretable | SELinux | policy | analysis | that | bridges | the | gap | operations. Likewise, SPLinux | [13] demonstrated the value of |  |  |  |
| between | theoretical | security | models | and | practical | policy | enforcing information flow policies, but its approach, like |  |  |  |  |  |
| management. | others, remains challenging to deploy at scale due to the |  |  |  |  |  |  |  |  |  |  |  |
| Keywords—SELinux policy, machine learning, graph databases, | [14] provide theoretical frameworks but are not practical for |  |  |  |  |  |  |  |  |  |  |  |
| access controls (MAC) to enhance the traditional discretionary | Recent advancements include formal verification methods |  |  |  |  |  |  |  |  |  |  |  |
| access control (DAC) model. While DAC bases access decisions | using Satisfiability Modulo Theories (SMT) [7], which aim to |  |  |  |  |  |  |  |  |  |  |  |
| solely | on | user | ownership, | SELinux | requires | all | subjects | automatically detect inconsistencies and policy violations. The |  |  |  |  |
| (processes) and objects (files, sockets) to satisfy additional | emergence of machine learning techniques, particularly graph- |  |  |  |  |  |  |  |  |  |  |  |
| policy rules based on their security contexts [1]. | based approaches using algorithms like node2vec [8], shows |  |  |  |  |  |  |  |  |  |  |  |
| Despite SELinux's robust security model, its policy-language | This evolution in analysis methods has led to diverse approaches |  |  |  |  |  |  |  |  |  |  |  |
| complexity creates significant challenges for policy analysis and | for | policy | verification | and | optimization. | SPRT | [15] | uses |  |  |  |  |
| management. The core problem lies in the disconnect between | prototype | networks | to | classify | vulnerabilities | and | adjust |  |  |  |  |  |
| SELinux's intricate policy framework and the tools available to | SELinux policies based on vulnerability descriptions, while our |  |  |  |  |  |  |  |  |  |  |  |
| analyze them. Additionally, the fine-grained nature of SELinux | research | leverages | emerging | graph-based | techniques | by |  |  |  |  |  |  |
| access control necessitates numerous rules, often resulting in | employing Neo4j [10] to model policy structures and applying |  |  |  |  |  |  |  |  |  |  |  |
| policies with thousands of statements that are time-consuming to | machine learning algorithms to the resulting graph data. Where |  |  |  |  |  |  |  |  |  |  |  |
| create and risky to modify [4]. | SPRT [15] focuses on categorizing vulnerabilities to guide |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 2

policy modifications, our work emphasizes detecting anomalous ensuring each process operates with the minimum necessary

patterns in policy relationships through graph-based permissions for its current task.

representations and anomaly detection models. These modern

approaches attempt to bridge the gap between theoretical rigor

and practical usability, though challenges remain in making

these solutions accessible to system administrators.

evaluate whether machine learning techniques can effectively

automate SELinux policy analysis, and 2) compare the

system security. This section introduces SELinux's core

At the core of SELinux's security model is Type

Enforcement (TE), which serves as the primary mechanism for

(process) and object (file, socket, etc.) receives a security context

label containing user, role, type, and optionally, a level for

Multi-Level Security (MLS) implementations [5]. Among these

attributes, the type is most crucial for access control decisions,

with subjects (typically processes) assigned domain types and

objects given resource types. So, our research focuses on

allow SourceDType TargetType : class1 {perm1 perm2};

Listing 1: Basic Syntax of a SELinux security policy

The rule in Listing 1 represents the fundamental building

Beyond simple allow rules, the policy language includes type

definitions, attributes for grouping related types, and macros for

reusable policy blocks [3].

all interactions between types by default unless explicitly

permitted through allow rules. A key feature is domain

transitions, where processes can securely change their security

context when executing certain programs. Consider Listing 2:

Listing 2: Example of domain transition rule in SELinux

At the application layer, SELinux's type enforcement can be

integrated through type-aware interfaces. Applications can use

type labels to categorize data and resources, enforcing

information flow controls that complement system-level MAC

B. SELinux Security Goals and Policy

goals through constraints and access rules. However, policy

maintaining system security.

allow audit_log_t financial_data_t:file { write };

This configuration violates SoD by allowing a single process

type (financial_process_t) to both modify financial data and

write audit logs, potentially enabling fraud through manipulation

of both transaction and audit records. A secure configuration

would separate these duties as shown in Listing 4:

write };

allow audit_process_t audit_log_t:file { write };

Listing 4: Example of SoD enforcement in SELinux Policy

misconfigured transition rules can prevent legitimate operations

or create security vulnerabilities. Policy inconsistencies also

manifest through contradictory rules, where conflicting

permissions create unpredictable behavior, and through

assigned to resources.

Network-related violations, particularly unauthorized

network access, represent a distinct threat category where

processes may gain unintended network capabilities.

security vulnerabilities and system functionality issues, while

missing necessary file access rules for system processes can

inspection [3].

| This research aims to develop an automated approach to | policies. This integration allows applications to enforce their |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SELinux | policy | analysis | that | is | both | comprehensive | and | own security rules based on data types while maintaining |  |
| accessible to security administrators. Our objectives are to: 1) | compatibility with system-wide policies [5]. |  |  |  |  |  |  |  |  |
| effectiveness | of | different | anomaly | detection | models | in | Violations |  |  |
| identifying policy violations and misconfigurations. | SELinux policies are designed to enforce specific security |  |  |  |  |  |  |  |  |
| II. | SEL | INUX | B | ACKGROUND | misconfigurations can lead to violations of these security goals. |  |  |  |  |
| SELinux represents a significant advancement in operating | Understanding | common | violation | types | is | crucial | for |  |  |
| architecture, explains its security goals and common policy | Separation of Duty (SoD) represents a fundamental security |  |  |  |  |  |  |  |  |
| violations, and reviews existing analysis approaches. | goal where critical operations should be divided among multiple |  |  |  |  |  |  |  |  |
| A. | SELinux Policy Architecture and Type | entities. Consider the misconfigured policy in Listing 3: |  |  |  |  |  |  |  |
| Enforcement | allow financial_data_t audit_log_t:file { read write }; |  |  |  |  |  |  |  |  |
| implementing | mandatory | access | controls. | Every | subject | Listing 3: Example of SoD violation in SELinux policy |  |  |  |
| SELinux Policy Type Enforcement. | allow | financial_process_t | financial_data_t:file | { | read |  |  |  |  |
| block of SELinux policy. This allow rule syntax permits the | Another violation we focus on is domain transition issues. |  |  |  |  |  |  |  |  |
| process with domain SourceDType to have actions perm1 or | Domain transition issues arise from incomplete or incorrect |  |  |  |  |  |  |  |  |
| perm2 on the object of type TargetType and object class of | transition rules between security contexts. For proper operation, |  |  |  |  |  |  |  |  |
| class1. An object class specifies the type of resource (such as | domain transitions require specific combinations of entrypoint |  |  |  |  |  |  |  |  |
| files, sockets, and directories). | access, execute permissions, and transition rights. Missing or |  |  |  |  |  |  |  |  |
| SELinux operates on the principle of least privilege, denying | incorrect type usage where security contexts are inappropriately |  |  |  |  |  |  |  |  |
| type_transition httpd_t httpd_exec_t:process httpd_child_t; | Additionally, mislabeled files and processes can lead to both |  |  |  |  |  |  |  |  |
| The rule in Listing 2 indicates that when a process of type | disrupt essential operations. These violations often interact in |  |  |  |  |  |  |  |  |
| 'httpd_t' executes a file labeled 'httpd_exec_t', it transitions to | complex ways - for example, a combination of mislabeled files |  |  |  |  |  |  |  |  |
| type 'httpd_child_t'. Such transitions enable fine-grained control | and improper privilege assignment could create unauthorized |  |  |  |  |  |  |  |  |
| over process privileges as they execute different programs, | access | paths | that | are | difficult | to | detect | through | manual |

---

## Page 3

The complexity of SELinux policies means violations can optimized for such traversals, allowing for more efficient and

manifest in various ways, from simple permission scalable analysis of large policies [9].

misconfigurations to subtle interactions between multiple rules.

These violations often require sophisticated analysis techniques

for detection, as manual inspection becomes impractical with the

thousands of rules present in typical SELinux deployments [3].

A comprehensive categorization and analysis of specific

violation classes and their detection through our machine

learning approach is presented in Section 4.1.

III. G RAPH - BASED A NALYSIS

Graph-based analysis has emerged as a powerful approach

for analyzing complex security policies and access control

systems. Recent work by Wu et al. demonstrates its effectiveness

in analyzing large-scale security policies [2], while research in

cloud computing security has shown graphs to be particularly

effective at representing and analyzing complex permission

relationships [7]. This methodology has gained traction in

security policy analysis due to its ability to represent and process

complex relationships efficiently, making it particularly well-

suited for analyzing SELinux's intricate policy structures. The

effectiveness of graph-based approaches has been further

security policy analysis [9].

Fundamentally, SELinux policies lend themselves naturally

to graph representations. In this graph model, types—the core

elements of SELinux's Type Enforcement mechanism—can be

conceptualized as nodes in a graph. The allow rules that define

permitted interactions between these types form the edges

connecting these nodes. This mapping provides an intuitive and

mathematically rigorous foundation for policy analysis [2].

One of the primary strengths of graph-based analysis lies in

its focus on relationships. SELinux policies are, at their core,

about defining and constraining relationships between different

entities in a system. Graph structures excel at capturing and

representing these relationships, allowing for efficient analysis

of access paths and potential information flows. This relational

focus aligns closely with the fundamental security questions that

policy analysts need to address, such as determining what

resources a given process type can access or identifying all

potential paths between two types [9,11].

The visual nature of graphs provides another significant

advantage. Complex policies that might be difficult to

comprehend when expressed as long lists of rules can become

much more accessible when visualized as graphs. This visual

intuition can help administrators quickly identify patterns,

anomalies, or potential security issues that might not be apparent

from textual representations alone. Visualization tools based on

graph representations have shown promise in enhancing policy

comprehension and analysis efficiency [2].

From a computational perspective, graph databases and

algorithms offer efficient mechanisms for querying and

analyzing complex relationship structures. Traditional relational

databases can struggle with the types of recursive queries often

needed in security policy analysis, such as finding all possible

paths between two types. Graph databases, in contrast, are

B. Graph Model for SELinux Policies

Our graph representation of SELinux policies in Figure 1

builds on the model proposed by Eaman et al. [9], which defines

three fundamental node types to capture policy relationships.

The model represents processes and domains as Subject nodes

containing name and type properties, resources as Object nodes

with name, type, and class properties, and permission categories

as Class nodes storing name and associated permissions. This

structure effectively captures the hierarchical nature of SELinux

(resources) according to defined class permissions. The

relationships between these nodes directly represent the allow

rules in the SELinux policy, with edges from Subject to Object

nodes indicating permitted operations under specific class

constraints [5]. This graph structure provides a natural

representation of SELinux's Type Enforcement mechanism,

enabling efficient analysis of permission relationships and

policy patterns.

validated by recent studies applying graph neural networks to Fig 1: Example of SELinux Type Enforcement Graph Model

A. Benefits of Using Graph For Analysis policies, where subjects (processes) interact with objects

---

## Page 4

Expanding on the model in Figure 1, allows for a

comprehensive representation of SELinux policies within a

graph database, such as in Figure 2. Subject nodes represent

The relationships between these nodes represent the allow

rules in the SELinux policy. For instance, an edge from a Subject

node to an Object node would indicate that the subject has

certain permissions on that object, as defined by the policy [5].

While this graph representation provides an intuitive way to

visualize policy relationships, analyzing complex policy patterns

requires transforming these graph structures into a format

suitable for machine learning algorithms. This transformation

process involves several steps: first, converting the policy rules

into a graph structure that captures all relevant security

relationships; then, encoding this graph structure into numerical

features that preserve both local and global policy patterns; and

finally, preparing these features for input into machine learning

models.

During our initial analysis, we observed that traditional

of four violation classes.

Our approach combines graph-based structural analysis with

machine learning techniques to automate SELinux policy

violation detection. This hybrid approach begins with

graph database, creating the foundation for our machine learning

pipeline [3]. We leverage Node2vec, a deep learning algorithm

that generates continuous feature representations for nodes in

networks [8], to transform our graph structures into vector

embeddings that capture both structural and semantic policy

relationships. This vectorization step is crucial for enabling our

subsequent machine learning analysis.

The training data for our models is constructed from three

distinct policy aspects: SELinux Transition Graphs capturing

entity interactions and transitions, attribute graphs representing

entity relationships, and Object Class Graphs encoding

permission hierarchies. These graph representations are then

processed through our machine learning pipeline, employing

Random Forest, Support Vector Machine (SVM), and Multi-

Layer Perceptron (MLP) Neural Network models to detect

policy violations. This combination of graph-based

representation and modern machine learning techniques

provides a robust framework for automated policy analysis,

capable of handling the scale and complexity of real-world

SELinux deployments [3], [8].

A. Defining Violation Classes

policies. These goals are expressed through security constraints

which, along with access rules, specify access decisions, i.e., to

grant or deny an access request.

model such as contradictions, which arise when conflicting rules

create unpredictable behavior, such as when one rule allows

access while another denies it. Also, missing rule violations,

exemplified by cases where the absence of network access

restrictions creates security gaps, can leave systems vulnerable

[3]. And incorrect Type Usage violations occur when

inappropriate types are assigned to resources, such as labeling

system binaries with user data types. Another important concept

is overly permissive rules which create unnecessary attack

surfaces by granting excessive permissions beyond operational

requirements. Domain transition issues arise when any of three

required conditions fail: entrypoint access to exec file type,

execute access to entry point file type, and transition access to

new domain type. Finally, Mislabeled Files and Processes,

where incorrect context assignments lead to unintended access

functionality [3].

0: No anomalies

1: Separation of Duty (SoD) violation - single subject with

read and write access to sensitive data

3: Critical system file modification

4: Incorrect type usage

| Fig. | 2: Graph of Synthetic Policies using Neo4j and Three.js | Security administrators can apply security goals through |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| processes or domains that can initiate actions. Object nodes | Common policy violations manifest in several ways in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| represent resources that can be acted upon, such as files or | SELinux systems. For example, there are Separation of Duty |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| sockets. Class nodes define the types of objects and their | Violations as outlined previously in Section 2.2. Additionally, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| associated permissions. | there are other violation classes we classify while training our |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| IV. | M | ACHINE | M | ODEL | D | EVELOPMENT | AND | T | RAINING | restrictions | or | permissions, | can | severely | impact | system |
| query generation often resulted in very specific queries, which | By | carefully | analyzing | for | these | potential | anomalies, |  |  |  |  |  |  |  |  |  |
| may not encompass all potential errors or violations. In contrast, | administrators can identify and rectify policy misconfigurations, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| our violation detection model offers more opportunities to detect | ensuring that SELinux policies are correctly implemented and |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| new | and | potentially | unforeseen | violations. | The | model | we | aligned with the intended security goals. In our models we define |  |  |  |  |  |  |  |  |
| developed is intended to read the policy data and populate a | violation classes to address these common policy violations, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| "violation class" column, categorizing each policy rule into one | finetuning them to be more specific. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| developing scripts to extract, parse, and import policy data into a | 2: Improper privilege assignment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 5

5: Domain transition issues This synthetic approach, while not utilizing complete

6: Mislabeled files or processes

8: Separation of Duty (SoD) violation - single subject with

access to multiple mutually exclusive roles

10: Missing necessary file access for system processes

Listing 5: Specific Violation Classes Used when Training

Models

critical system file modification access (Type 3), domain

transition issues that could enable privilege escalation (Type 5),

and missing necessary file access for system processes (Type

10). Type 0 serves as our baseline case, representing properly

configured policies with no detected anomalies. Each violation

class corresponds to specific patterns in the policy graph

structure that our detection models are trained to identify. These

examples were specifically chosen to represent realistic

misconfigurations that security administrators might encounter

in production environments.

B. Dataset Construction and Preparation

of our detection capabilities. The examples follow the syntax

shown in Listing 1 while incorporating violations like the SoD

verify that each synthetic example correctly represented its

intended security properties. This approach allowed us to

confirm that our synthetic policies exhibited the structural

characteristics of real SELinux policies while containing well-

production policies, provided several advantages for our

research. It allowed us to create a balanced dataset with well-

associated with using production policies, and enabled us to

systematically evaluate our models' detection capabilities across

different violation types. The controlled nature of the synthetic

performance characteristics and generalization capabilities.

C. Results

Employing our dataset preparation method from Section 4.2,

we then selected and evaluated three distinct machine learning

For model training, when tested on our largest dataset of 455

policy rules, Node2vec-based models achieved consistently

higher performance, with the MLP model reaching 95%

accuracy. Node2vec's superior performance stems from its

ability to preserve both local and global graph structures through

its flexible random walk strategy, which proved crucial for

capturing the complex relationships in SELinux policies [8].

This approach generates rich feature representations that encode

both structural and semantic aspects of policy relationships,

enabling our models to better identify policy violations across

varying contexts and scales.

class column.

| Macro Avg | Weighted Avg |
| --- | --- |
| Model | Accuracy |
| (P/R/F1) | (P/R/F1) |
| 0.79 | 0.83/0.79/0.79 |

| 7: Unauthorized network access | understood | properties, | avoided | potential | security | concerns |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9: Contradictory type transitions for the same process | data also facilitated more precise evaluation of our models' |  |  |  |  |  |  |  |
| The anomalies we aim to detect can be categorized into ten | models for policy violation detection: Random Forest, SVM, |  |  |  |  |  |  |  |
| distinct violation classes, as shown in Listing 5. These range | and MLP models. Random Forest was chosen for its ability to |  |  |  |  |  |  |  |
| from access control violations to type assignment issues and | handle | high-dimensional | data | and | capture | complex | rule |  |
| system integrity concerns. In terms of access control, we detect | interactions | through | ensemble | learning | of | decision | trees, |  |
| Separation of Duty (SoD) violations where a single subject has | achieving 93% accuracy with balanced precision and recall |  |  |  |  |  |  |  |
| both read and write access to sensitive data (Type 1), or access to | (0.93/0.93/0.93) in violation detection. SVM was selected for its |  |  |  |  |  |  |  |
| multiple mutually exclusive roles (Type 8). We also identify | effectiveness in handling binary and multi-class classification |  |  |  |  |  |  |  |
| unauthorized | network | access | patterns | (Type | 7) | that | could | problems with clear decision boundaries, demonstrating 92% |
| indicate security bypasses. For type assignment issues, our | accuracy with strong performance metrics (0.93/0.92/0.92). The |  |  |  |  |  |  |  |
| models detect incorrect type usage (Type 4), mislabeled files or | MLP Neural Network was included for its capacity to learn |  |  |  |  |  |  |  |
| processes (Type 6), and contradictory type transitions that create | complex non-linear relationships in the policy data, ultimately |  |  |  |  |  |  |  |
| ambiguous process contexts (Type 9). System integrity concerns | providing the best performance with 95% accuracy and highest |  |  |  |  |  |  |  |
| include improper privilege assignments (Type 2), unauthorized | precision/recall scores (0.95/0.97/0.95). |  |  |  |  |  |  |  |
| We constructed a synthetic dataset to enable controlled | To evaluate the effectiveness of our approach, we conducted |  |  |  |  |  |  |  |
| evaluation of our violation detection models. Initial analysis of | a series of experiments with increasing complexity. Starting with |  |  |  |  |  |  |  |
| Fedora | 39 | and | Ubuntu | Server | SELinux | policies | provided | a basic set of violation classes, we progressively refined our |
| templates for policy structure and common patterns. Using these | classification schema based on model performance and real- |  |  |  |  |  |  |  |
| patterns, we generated synthetic examples representing each | world | policy | patterns. | This | iterative | process | helped | us |
| violation class described in Section 2.2. | understand both the capabilities and limitations of different |  |  |  |  |  |  |  |
| The dataset focuses on server security contexts, including | model architectures while working with SELinux policy data. |  |  |  |  |  |  |  |
| web servers and database systems, where policy violations | We initially tested our models on 5 violation classes and with |  |  |  |  |  |  |  |
| present significant risks. We developed examples covering all | a smaller dataset of 125 policy rules, including the control class |  |  |  |  |  |  |  |
| ten violation categories from Listing 5. Each synthetic policy | ‘0’ representing policies without a violation. The model we |  |  |  |  |  |  |  |
| isolates specific security properties to enable precise evaluation | developed is intended to read the data and populate the violation |  |  |  |  |  |  |  |
| issues demonstrated in Listings 3 and 4. | Here are some key results for a dataset of 125 policy rules: |  |  |  |  |  |  |  |
| Our validation process employed graph-based modeling to | Table 1: Results for 125 Policy Rules |  |  |  |  |  |  |  |
| defined violations suitable for training our machine learning | Random | 0.85/0.77/0.7 |  |  |  |  |  |  |
| models. | Forest | 9 |  |  |  |  |  |  |

---

## Page 6

0.80/0.65/0.6

SVM 0.68 0.78/0.68/0.65

3

0.89/0.85/0.8

MLP 0.86 0.88/0.86/0.85

6

Our initial approach with 5 violation classes proved too

broad, leading to high false positives particularly in classes like

"Separation of Duty Violations" and "Domain Transition

Issues". For example, the general SoD violation class

encompassed both file access violations and role-based

violations, which exhibited different structural patterns in the

policy graphs. This led us to split SoD into two distinct classes:

"SoD violation - single subject with read and write access to

sensitive data" and "SoD violation - single subject with access to

multiple mutually exclusive roles".

So, we then split up the violation classes into more specific

examples with patterns we believed the models would pick up

more accurately. Our next test used 10 violation classes: No

anomalies, Separation of Duty (SoD) violation, Overly

permissive access, Improper privilege assignment, Critical

system file modification, Contradictory rules, Missing necessary

Table 2: Results for Initial 10 Violation Classes

| Macro Avg | Weighted Avg |
| --- | --- |
| Model | Accuracy |
| (P/R/F1) | (P/R/F1) |
| 0.85 | 0.87/0.85/0.85 |
| Forest | 7 |

0.43/0.47/0.4

SVM 0.73 0.68/0.73/0.69

5

0.78/0.74/0.7

MLP 0.83 0.86/0.83/0.83

3

| 0.83 | 0.85/0.83/0.84 |
| --- | --- |
| Ensemble | 7 |

Fig. 3: Bar Graph of Initial 10 Violation Class’ Results

With these classes, our Random Forest model achieved an

accuracy of 0.85, with a macro average precision/recall/F1 of

0.80/0.77/0.77 and a weighted average of 0.87/0.85/0.85. The

SVM model had an accuracy of 0.73, while the MLP achieved

0.83. We also implemented a Stacking Ensemble model, which

achieved an accuracy of 0.83.

detailed categories. And the dataset included 455 different

example policies.

Table 3: Results for 16 Violation Classes

| Macro Avg | Weighted Avg |
| --- | --- |
| Model | Accuracy |
| Random | 0.85/0.83/0.8 |
| 0.87 | 0.88/0.87/0.86 |
| Forest | 2 |

0.84/0.78/0.7

SVM 0.82 0.85/0.82/0.80

7

0.84/0.82/0.8

MLP 0.86 0.87/0.86/0.85

| rules, | Incorrect | type | usage, | Domain | transition | issues, | Due to poor results from classes related to Separation of |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Unauthorized network access. | And we expanded the dataset to | Duty, Contradictory Rules, and Missing Rules, we decided to |  |  |  |  |  |
| include 401 different types of rules with a balanced amount of | expand our classification to 16 more specific violation classes. |  |  |  |  |  |  |
| each violatioin class. | This included separating the problematic classes into more |  |  |  |  |  |  |
| Random | 0.80/0.77/0.7 | (P/R/F1) | (P/R/F1) |  |  |  |  |
| Stacking | 0.77/0.77/0.7 | 2 |  |  |  |  |  |

---

## Page 7

0.85/0.83/0.82 and a weighted average of 0.88/0.87/0.86. The

reached 0.86.

These results demonstrate the importance of specific and

well-defined violation classes in improving the accuracy of our

models. Initial expansion to 16 classes allowed us to distinguish

allow and deny rules for same subject-object-permission

policy misconfigurations. However, we found that this fine-

matches of contradictory rules, they often failed to detect

conceptually similar contradictions that differed slightly in

structure. This observation led us to first consolidate these into a

single "Contradictory rules" class in our 15-class model, while

maintaining the same dataset, improving the model's ability to

detect contradictions in various forms. Additionally, all models

struggle with class 14 (Missing necessary file access for system

processes), showing particularly low recall as shown in Table 6:

Table 4: Recall Score for violation class 14 (Missing necessary

file access for system processes)

| Model | Recall Score |
| --- | --- |
| Random Forest | 0.25 |
| SVM | 0.06 |

performance on these classes was notably lower, indicating a

need for further refinement.

Our refinement from 16 to 10 classes involved strategic

consolidation of related violation types. The overly permissive

access class (originally class 2) was merged into improper

privilege assignment, as our models showed significant overlap

in detecting these patterns. Similarly, we consolidated all

contradictory rule violations (original classes 5, 12, and 13) into

a single "Contradictory type transitions" class, as these

violations shared common structural patterns in the policy

graphs.

A significant consolidation occurred with system access

violations. The original separate classes for missing port access

(class 6), file access (class 14), directory access (class 15), and

necessary file access" class. This consolidation was driven by

| Macro Avg | Weighted Avg |  |
| --- | --- | --- |
| Model | Accuracy |  |
| (P/R/F1) | (P/R/F1) |  |
| Random | 0.93/0.93/0.9 |  |
| SVM | 0.92 | 0.92/0.92/0.92 |

5

The consolidated 10 classes in Figure 5 showed improved

| Fig. 4: Bar Graph of 16 Violation Class’ Results | network access (class 16) were combined into a single "Missing |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| With this refined classification, our model performance | our observation that the models struggled with overly specific |  |  |  |  |  |  |  |
| improved. The Random Forest model now achieved an accuracy | access violations, showing particularly low recall scores for |  |  |  |  |  |  |  |
| of | 0.87, | with | a | macro | average | precision/recall/F1 | of | these classes (around 0.25 for both Random Forest and MLP). |
| SVM model improved to an accuracy of 0.82, and the MLP | Table 5: Results for 10 Refined Violation Classes |  |  |  |  |  |  |  |
| between subtle variations in policy violations. For example, we | 0.93 | 0.94/0.93/0.93 |  |  |  |  |  |  |
| split contradictory rules into two distinct classes: "Contradictory | Forest | 3 |  |  |  |  |  |  |
| combination" and "Contradictory type transitions for the same | 0.93/0.92/0.9 |  |  |  |  |  |  |  |
| process". This separation helped identify specific patterns in | 2 |  |  |  |  |  |  |  |
| grained separation sometimes caused the models to miss broader | 0.95/0.97/0.9 |  |  |  |  |  |  |  |
| patterns of contradiction. While the models could identify exact | MLP | 0.95 | 0.96/0.95/0.95 |  |  |  |  |  |
| MLP | 0.25 | Fig. 5: Bar Graph of Final Refined 10 Violation Class’ Results |  |  |  |  |  |  |
| Despite achieving higher overall accuracies in the datasets | detection rates while maintaining the ability to identify critical |  |  |  |  |  |  |  |
| using 16 violation classes, as shown in Table 4 and 5, the models | access violations. By combining related violations into broader |  |  |  |  |  |  |  |
| exhibited difficulty in detecting certain types of violations, | but | still | meaningful | categories, | we | achieved | better |  |
| particularly those that are rare or complex, such as "Missing | generalization while maintaining the ability to detect specific |  |  |  |  |  |  |  |
| necessary | file | access | for | system | processes." | The | models' | types of policy misconfigurations. The final 10-class model |

---

## Page 8

| showed more balanced performance across all categories, with | A particularly promising direction is better integration of |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| improved precision and recall metrics compared to the more | type-based enforcement at both system and application levels. |  |  |  |  |  |  |  |
| granular 16-class model. Thus, we went with refined 10 classes | This approach could enable applications to enforce fine-grained |  |  |  |  |  |  |  |
| as our final model. | security | decisions | internally | based | on | type | labels | while |

According to Table 5, all three models perform very well,

with accuracies ranging from 0.92 to 0.95. The MLP model

achieves the highest accuracy (0.95), followed by Random

Forest (0.93) and SVM (0.92). The MLP model shows strong

of SELinux policies. By representing policies as graphs and

applying models like Random Forests, SVM, and MLP Neural

While our research demonstrates the effectiveness of

machine learning models in detecting SELinux policy

violations, further work is needed to evaluate real-world

performance implications. System administrators could

potentially integrate this approach into their workflows through

automated policy analysis, but actual deployment would require

careful performance testing and optimization. The

of rules. This performance analysis would help determine

whether the approach is better suited for periodic policy audits or

Additionally, reinforcement learning could enable more

violations through interaction with policy environments. Unlike

(LLMs) with Retrieval Augmented Generation (RAG) could

between high-level security requirements and low-level policy

maintaining compatibility with system-wide policies. By

allowing applications to dynamically interact with SELinux's

security contexts, this model could provide more flexible and

granular security enforcement [5].

analysis in complex Linux environments. The ultimate goal is to

security.

policy verification and property checking. His guidance helped

shape our methodology for ensuring policy correctness. We also

thank the engineers at Google and Red Hat for their constructive

feedback and look forward to future collaborations as we

continue developing this work.

155–171, 2013.

[3] Red Hat, Inc., "What is SELinux?," Red Hat Customer Portal. [Online].

Ch 1-13. Available:

[Accessed: Sept. 3, 2024]

[4] "Security-Enhanced Linux for mortals," YouTube. [Online]. Available:

28, 2024]

Verification Using SMT," arXiv preprint arXiv:2312.04586, 2023.

Networks," in Proc. 22nd ACM SIGKDD Int. Conf. Knowledge

10.1145/2939672.2939754.

Refining of SELinux Security Policies," unpublished, 2024.

| performance across all metrics, with macro-averaged precision, | Our results suggest that machine learning-based policy |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| recall, and F1-scores of 0.95, 0.97, and 0.95 respectively, and | analysis can effectively bridge the gap between SELinux's |  |  |  |  |  |  |  |  |  |  |  |  |  |
| weighted averages of 0.96, 0.95, and 0.95. The Random Forest | powerful security features and administrators' practical needs. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| model demonstrates consistent performance with both macro | The combination of graph-based representation, sophisticated |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and weighted averages around 0.93, while the SVM model | machine learning models, and automated analysis tools provides |  |  |  |  |  |  |  |  |  |  |  |  |  |
| shows similar consistency with metrics around 0.92. This | a | promising | framework | for | enhancing | SELinux | policy |  |  |  |  |  |  |  |
| indicates that all models maintain good balance across different | management. While challenges remain in areas such as model |  |  |  |  |  |  |  |  |  |  |  |  |  |
| violation classes, though the MLP model appears to have a slight | interpretability | and | computational | resources, | our | approach |  |  |  |  |  |  |  |  |
| edge in overall performance. | demonstrates significant potential for improving security policy |  |  |  |  |  |  |  |  |  |  |  |  |  |
| V. | C | ONCLUSION | AND | F | UTURE | D | IRECTION | develop | a | comprehensive, | automated | system | that | makes |
| The findings from our research underscore the efficacy of | SELinux policy analysis more accessible while maintaining the |  |  |  |  |  |  |  |  |  |  |  |  |  |
| graph-based machine learning models in automating the analysis | security guarantees that make SELinux valuable for system |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Networks, | we | achieved | high | accuracy | in | detecting | policy | A | CKNOWLEDGMENT |  |  |  |  |  |
| violations. Notably, the MLP model consistently demonstrated | We express our gratitude to Prof. Daniel Jackson (MIT |  |  |  |  |  |  |  |  |  |  |  |  |  |
| robust | performance | across | varying | dataset | sizes | and | CSAIL) for his valuable insights on applying formal verification |  |  |  |  |  |  |  |
| classification schemes, achieving accuracies up to 96%. | approaches, particularly his suggestions around using Alloy for |  |  |  |  |  |  |  |  |  |  |  |  |  |
| computational | overhead | of | graph | construction, | embedding | R | EFERENCES |  |  |  |  |  |  |  |
| generation, and model inference in production environments | [1] | Red Hat, Inc., "Quick start to write a custom SELinux policy," Red Hat |  |  |  |  |  |  |  |  |  |  |  |  |
| with large policy sets remains to be thoroughly benchmarked. | Customer | Portal. | [Online]. | Available: |  |  |  |  |  |  |  |  |  |  |
| Future research should focus on measuring these performance | https://access.redhat.com/articles/6999267. [Accessed: Aug. 15, 2024] |  |  |  |  |  |  |  |  |  |  |  |  |  |
| characteristics across different scales of deployment, from small | [2] | W. Xu, M. Shehab, and G. J. Ahn, "Visualization-based policy analysis for |  |  |  |  |  |  |  |  |  |  |  |  |
| systems to enterprise environments with hundreds of thousands | SELinux: Framework and user study," Int. J. Inf. Secur., vol. 12, no. 3, pp. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| if it could be feasibly implemented as part of real-time policy | https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| validation. | 8/html/using_selinux/getting-started-with-selinux_using-selinux. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| dynamic | policy | analysis, | with | agents | learning | to | identify | https://www.youtube.com/watch?v=_WOKRaM-HI4. | [Accessed: | Aug. |  |  |  |  |
| our current supervised learning approach, RL agents could | [5] | F. Mayer, K. MacMillan, and D. Caplan, SELinux by Example: Using |  |  |  |  |  |  |  |  |  |  |  |  |
| potentially discover novel attack vectors and policy weaknesses | Security Enhanced Linux. Pearson Education, 2006. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| by simulating various security scenarios. The integration of | [6] | SELinux Project, "SETools," SELinux Project Wiki. [Online]. Available: |  |  |  |  |  |  |  |  |  |  |  |  |
| machine | learning | techniques | with | advanced | methodologies | https://github.com/SELinuxProject/setools. [Accessed: Sept. 12, 2024] |  |  |  |  |  |  |  |  |
| presents | exciting | opportunities. | Large | Language | Models | [7] | S. Dashevskyi, D. Nisi, Y. Oren, "Automated SELinux RBAC Policy |  |  |  |  |  |  |  |
| assist | in | policy | interpretation, | generate | human-readable | [8] | A. Grover and J. Leskovec, "node2vec: Scalable Feature Learning for |  |  |  |  |  |  |  |
| explanations of violations, and potentially help bridge the gap | Discovery | Data | Mining, | 2016, | pp. | 855-864, | doi: |  |  |  |  |  |  |  |
| specifications [2]. | [9] | A. Eaman, P. Jadczyk, and H. Chipman, "Graph-Powered Mining and |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 9

[10] Neo4j, Inc., "Neo4j Graph Database Platform," Neo4j Graph Database

Platform. [Online]. Available: https://neo4j.com/

[11] T. Jaeger, "Operating System Security," Synthesis Lectures on

Information Security, Privacy, and Trust, vol. 4, no. 1, pp. 1–218, 2008.

[12] D. Efremov and I. Shchepetkov, "Runtime verification of Linux Security

Modules policies," arXiv preprint, arXiv:2001.01442, 2020. [Online].

Available: https://arxiv.org/abs/2001.01442.

[13] P. Vyas, R. Shyamasundar, B. Patil, S. Borse and S. Sen, "SPLinux: An

Information Flow Secure Linux," 2021 IEEE Intl Conf on Parallel &

Distributed Processing with Applications, Big Data & Cloud Computing,

Sustainable Computing & Communications, Social Computing &

Networking (ISPA/BDCloud/SocialCom/SustainCom), New York City,

NY, USA, 2021, pp. 1603-1612, doi: 10.1109/ISPA-BDCloud-

SocialCom-SustainCom52081.2021.00214.

[14] G. Zanin and L. V. Mancini, "Towards a formal model for security

policies specification and validation in the selinux system," in Proc. 9th

ACM Symp. Access Control Models and Technologies (SACMAT '04),

2004, pp. 136-145, doi: 10.1145/990036.990059.

[15] H. Wang, A. Yu, L. Xiao, J. Li, and X. Cao, "SPRT: Automatically

Adjusting SELinux Policy for Vulnerability Mitigation," in Proceedings

of the 29th ACM Symposium on Access Control Models and

Technologies (SACMAT), Jun. 2024, pp. 71-82, doi:

10.1145/3649158.3657306.
