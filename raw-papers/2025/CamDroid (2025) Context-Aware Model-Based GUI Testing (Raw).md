---
title: "19_CamDroid_Context-Aware_Model-Based_GUI_Testing"
author: "SoWise"
creator: "SoWise"
pages: 13
---

# 19_CamDroid_Context-Aware_Model-Based_GUI_Testing

> **作者**：SoWise
> **總頁數**：13 頁

---

## Page 1

TSINGHUA SCIENCE AND TECHNOLOGY

ISSN 1007-0214 04/31 pp55−67

DOI: 1 0 . 2 6 5 9 9 / T S T . 2 0 2 4 . 9 0 1 0 0 3 8

Volume 30, Number 1, February 2025

Hongyi Wang, Yang Li *

outperforms non-trivial baselines in activity coverage, crash detection, and test efficiency.

generation

With the widespread popularity of mobile phones,

mobile applications (apps) have been an indispensable

part of our daily life and have increased dramatically in

number over recent years [1] . To maintain commercial

competitiveness and keep user loyalty, it is crucial to

adequately test these apps to guarantee their

robustness. In practice, Graphical User Interface (GUI)

testing for apps heavily involves human efforts.

However, due to the rapid releasing cycle and limited

Daqiang Hu and Zhi Liao are with Hangzhou Uusense

Technology Inc., Hangzhou 310012, China. E-mail: hudaqiang@

uusense.com; liaozhi@uusense.com.

©

Testing for Android Apps

, Jing Yang, Daqiang Hu, and Zhi Liao

limited test time. App stores also rely on automated

testing to detect malicious apps before they are

officially released [2–5] . Therefore, automated GUI

testing for Android apps has been studied extensively

in both academia and industry.

A variety of automated GUI testing approaches have

been proposed, including model-based [6] , probability-

based [7] , and deep learning based methods [8] to

dynamically explore app activities by injecting actions

(like clicking and scrolling) according to the detection

continuous testing. This is because they rerun each

version from scratch without learning from the context

The author(s) 2025. The articles published in this open access journal are distributed under the terms of the

Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/).

CamDroid: Context-Aware Model-Based Automated GUI

Abstract: Recent years have witnessed the widespread adoption of mobile applications (apps for short). For

quality-of-service and commercial competitiveness, sufficient Graphical User Interface (GUI) testing is required

to verify the robustness of the apps. Given that testing with manual efforts is time-consuming and error-prone,

automated GUI testing has been widely studied. However, existing approaches mostly focus on GUI

exploration while lacking attention to complex interactions with apps, especially generating appropriate text

inputs like real users. In this paper, we introduce CamDroid, a lightweight context-aware automated GUI testing

tool, which can efficiently explore app activities through (1) a model-based UI-guided testing strategy informed

by the context of previous event-activity transitions and (2) a data-driven text input generation approach

regarding the GUI context. We evaluate CamDroid on 20 widely-used apps. The results show that CamDroid

Key words: Android app; automated Graphical User Interface (GUI) testing; state transition model; text input

| 1 | Introduction | resource-consuming with poor activity coverages in |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| human resources, manual GUI testing is time- and | and | analysis | of | the | current | GUI | components | [9] | . |
| Hongyi Wang, Yang Li, and Jing Yang are with School of | However, since quick feedback on the quality of new |  |  |  |  |  |  |  |  |
| Software, Tsinghua University, Beijing 100084, China. E-mail: | app | features | is | required | whenever | a | new | internal |  |
| hongyi-w21@mails.tsinghua.edu.cn; | liyang14thu@gmail.com; | version of the app is built | [8] | , these approaches are |  |  |  |  |  |
| yangj23@mails.tsinghua.edu.cn. | mostly | inefficient | and | ineffective | in | terms | of |  |  |
| * | To whom correspondence should be addressed. | knowledge of previous testing runs to accelerate the |  |  |  |  |  |  |  |
| Manuscript | received: | 2023-10-25; | revised: | 2024-02-09; | current test. Moreover, inside one testing run, most of |  |  |  |  |
| accepted: 2024-02-15 | them | focus | on | the | GUI | exploration | algorithm |  |  |

---

## Page 2

| 56 | Tsinghua Science and Technology, February | 2025, 30(1): 55−67 |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| improvement | while | lacking | attention | to | complex | score. In this way, CamDroid can generate suitable text |  |  |
| interactions | with | apps, | especially | generating | inputs like real users, and certain sequential activities |  |  |  |
| appropriate | text | inputs | like | real | users, | leading | to | requiring specific text inputs to reach can be effectively |
| unsatisfactory app activity coverages. | explored. The architectural overview of CamDroid is |  |  |  |  |  |  |  |
| To fill the above gaps, we propose CamDroid, a | depicted in Fig. 1. |  |  |  |  |  |  |  |
| context-aware | model-based | automated | GUI | testing | We implement the prototype of CamDroid based on |  |  |  |
| approach for Android apps. To effectively store the | the | source | of | Android | Monkey. | To | evaluate | the |
| context knowledge of previous testing runs, CamDroid | effectiveness of CamDroid, we compare CamDroid |  |  |  |  |  |  |  |
| abstracts the key identities of feasible widgets with the | with | state-of-the-art | testing | tools | (i.e., | Monkey | [22] | , |
| allowed actions on the GUI page as events, and builds | APE | [6] | , and Fastbot2 | [7] | ) on 20 large, widely-used apps |  |  |  |
| a state transition model to memorize the historical | from | Google | Play. | Experiment | results | show | that |  |
| probabilities of the event-activity transitions (each of | CamDroid | achieves | 1.25× | (1.27×) | higher | average |  |  |
| which represents the probability of an event to reach an | (median) | activity | coverage | than | the | best | baseline |  |
| app | activity). | To | further | leverage | the | context | within one hour. Though the apps have been well |  |
| knowledge, CamDroid combines the one-step guidance | tested, CamDroid manages to find 34 unique crashes in |  |  |  |  |  |  |  |
| of | the | state | transition | model | with | the | multi-step | one hour, while the best baseline Fastbot2 finds 18. We |
| guidance of reinforcement learning, aiming to reach | also conduct ablation study to further demonstrate the |  |  |  |  |  |  |  |
| deep activities requiring sequential event executions. | effectiveness of our text input generation technique and |  |  |  |  |  |  |  |
| Furthermore, CamDroid learns the correlation of user | its adaptability to other testing tools. Results show that |  |  |  |  |  |  |  |
| characteristics and app metadata (collected from public | the | proposed | text | input | generation | technique | can |  |
| datasets | [10–20] | ) with a Generative Adversarial Network | improve the activity coverages of Monkey, APE, and |  |  |  |  |  |
| (GAN) | and | generates | text | inputs | for | diverse | user | Fastbot2 by 1.13×, 1.19×, and 1.15×, respectively. |
| profiles and app scenarios (each pair of profile and | Roadmap. | The remainder of the paper is organized |  |  |  |  |  |  |
| scenario information is encoded as a vector named | as follows. In Section 2, we illustrate the problem and |  |  |  |  |  |  |  |
| “input context vector”, which is corresponding to one | challenges. In Section 3, we present our algorithm |  |  |  |  |  |  |  |
| generated | text | input) | in | advance. | When | an | event | CamDroid. In Section 4, we introduce the prototype |
| requiring text inputs is selected by the aforementioned | setting | and | the | evaluation | results. | We | survey | the |
| state transition model, CamDroid encodes the contexts | related works in Section 5 and conclude this paper in |  |  |  |  |  |  |  |
| of current GUI widget identities as a feature vector, | Section 6. |  |  |  |  |  |  |  |

and calculates BERTScores [21] of this vector with each

of the input context vectors corresponding to the text

Event execution

Update

GUI

knowledge

Build

Install Multi-step

rewards

Event abstractor

Android

application Valid-identity Events

labels

Fig. 1

2 Background and Motivation

CamDroid

Event selection Text input generation

BERTScore ranking

One-step state

with GUI coverage

contexts context

High-score text

Generate

Reinforcement

GAN

learning

Learn correlations datasets

Architectural overview of CamDroid.

| inputs generated by GAN. Then CamDroid ranks the | In | this | section, | we | introduce | the | problem | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| input context vectors by BERTScores and selects the | challenges of the automated GUI testing for Android |  |  |  |  |  |  |  |
| text input corresponding to the one with the highest | apps, especially issues related to text input generation. |  |  |  |  |  |  |  |
| info | Context | transition model | Text inputs | Current | Activity |  |  |  |
| package | Static widget | pool | Public | Crashes |  |  |  |  |

---

## Page 3

| Hongyi Wang et al.: | CamDroid: Context-Aware Model-Based Automated GUI Testing for Android Apps | 57 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Furthermore, | we | uncover | why | existing | methods | example, a variety of pages cannot be accessed without |
| struggle to address these challenges. | the login operation. On the other hand, some activities |  |  |  |  |  |

2.1 Problem

wide range of scenarios. These characteristics make

comprehensive testing of mobile apps challenging.

Traditional manual testing is not only time-consuming

and labor-intensive but also prone to overlooking

corner cases. As a result, there is a growing demand for

effective and efficient automated testing tools that can

streamline the testing process, improve the testing

coverage, and enhance the quality of Android apps.

(1) Vast and dynamically changing search space

Considering that a mobile app has hundreds of

activities and potentially thousands of widgets, the

search space for app testing is very extensive. Random

, suffer from getting stuck

in loops early and no longer making progress.

Additionally, since GUI pages often update

dynamically, sometimes even a simple backward action

Toutiao) and less effective for others. Therefore,

can only be reached when the app is not logged in.

However, existing tools fail to handle them properly.

version update for an app rarely undergoes heavy-

weight changes, which means that the model built in

previous testing can be somehow reusable. However,

most model-based tools fail to leverage this

characteristic and instead rebuild the model from

scratch after each version update, which is ineffective

and inefficient.

(2) Text input generation

while lacking attention to complex interaction with

apps like text input generation. They just perform

completely random inputs or input a few fixed

words [25, 26] . However, most apps contain pages that

proceed. As shown in Fig. 2, the test will be hindered if

the tool can not enter meaningful content in the search

box of X (former name Twitter). Therefore, testing

input generation of app testing [27]

text inputs is difficult.

| With the rapid growth of the Android app market, | Additionally, a model-based tool needs to initialize |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ensuring the quality and reliability of Android apps | its model at the beginning of the testing. Considering |  |  |  |  |  |  |  |  |  |
| becomes a critical concern for developers. However, | the vast search space, the initialization can be time- |  |  |  |  |  |  |  |  |  |
| mobile apps have short update cycles and encompass a | consuming. For industrial app development, a single |  |  |  |  |  |  |  |  |  |
| 2.2 | Challenges | Most existing tools only focus on GUI exploration, |  |  |  |  |  |  |  |  |
| testing tools, like Monkey | [22] | require meaningful text inputs in the preceding page to |  |  |  |  |  |  |  |  |
| fails | to | return | to | the | exact | previous | GUI | page. | tools failing to generate valid text inputs struggle to |  |
| Consequently, the effectiveness of search-based tools | access | these | pages, | resulting | in | limited | activity |  |  |  |
| based on graph traversal algorithms | [23, 24] | is not ideal. | coverages and difficulties in surpassing the bottleneck. |  |  |  |  |  |  |  |
| Model-based | tools | [6, 7, 25] | abstract | GUI | trees | into | Automated text input generation is challenging. The |  |  |  |
| different states and regard the page changes caused by | algorithm needs to generate text that conforms to the |  |  |  |  |  |  |  |  |  |
| events as transitions between states. They adapt to the | GUI context and satisfies constraints, requiring strong |  |  |  |  |  |  |  |  |  |
| dynamic search space by adjusting state abstractions or | Natural | Language | Processing | (NLP) | capabilities. |  |  |  |  |  |
| transition | relationships. | However, | simply | defining | Although | the | Large | Language | Model | (LLM) |
| different GUI pages as different states leads to a large | demonstrates remarkable performance in the field of |  |  |  |  |  |  |  |  |  |
| state space, thus reducing the testing efficiency. | NLP, applying the inference of such a model for the |  |  |  |  |  |  |  |  |  |
| Some | model-based | tools | leverage | coarse-grained | would entail several |  |  |  |  |  |
| abstractions to tackle the problem. Unfortunately, they | seconds on generating and encoding the prompt for |  |  |  |  |  |  |  |  |  |
| face low accuracy in modeling app behaviors. Take | each | text | input. | Consequently, | the | whole | testing |  |  |  |
| Fastbot2 | [7] | for example, it may consider two events | process | would | be | slowed | down | by | the | inference |
| with different functionalities as the same one, which | overhead of the LLM, resulting in unsatisfactory test |  |  |  |  |  |  |  |  |  |
| may mislead event selections. This limitation makes it | efficiency. | As | a | result, | maintaining | test | efficiency |  |  |  |
| only | suitable | for | specific | apps | (i.e., | Douyin | and | without significantly reducing the quality of generated |  |  |
| balancing the trade-off between the size and precision | Additionally, correlations may exist among a real |  |  |  |  |  |  |  |  |  |
| of states is untrivial for model-based tools. | user’s multiple text inputs while interacting with an |  |  |  |  |  |  |  |  |  |
| Worse still, some actions lead to irreversible changes | app. For example, when a user purchases a flight ticket |  |  |  |  |  |  |  |  |  |
| in GUI pages and result in great differences between | and then proceeds to book accommodation in a travel |  |  |  |  |  |  |  |  |  |
| the search space before and after performing them. For | app, the destination of the ticket and the city of the |  |  |  |  |  |  |  |  |  |

---

## Page 4

58 Tsinghua Science and Technology, February 2025, 30(1): 55−67

Random text input

Fig. 2

scale study on interrelationships among text input

scenarios within the same app. Second, further utilizing

previous text inputs and user information for real-time

3 Approach

metadata.

The workflow of CamDroid is illustrated in Fig. 1,

which mainly consists of two components: event

selection and text input generation. CamDroid first

Meaningful text input

(e.g., a person’s name)

Example of text input in Android app.

context vector to fill in.

3.2 Model-based testing tool

as a state, and the transitions between states represent

the switchings between activities. The key identities of

the app activity a .

event, e.g., e i , is executed. The value of every p ( e i , a j )

that associates with e i is updated according to the

following rule:

n ( e

p ( e i , a j ) = (1)

| accommodation typically are the same. | inputs for various possible scenarios (each is encoded |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| However, realizing the above insight in practice is | as an input context vector) before the test. During the |  |  |  |  |  |  |  |  |  |  |  |  |
| challenging. First, there is no public dataset of real user | test, it encodes the current GUI context into a feature |  |  |  |  |  |  |  |  |  |  |  |  |
| text inputs while using apps, while collecting data | vector and calculates BERTScores | [21] | of this vector |  |  |  |  |  |  |  |  |  |  |
| manually is time-consuming, labor-intensive, and lacks | with each of the input context vectors. It then selects |  |  |  |  |  |  |  |  |  |  |  |  |
| diversity. Therefore, it is difficult to conduct a large- | the | text | corresponding | to | the | highest-scoring | input |  |  |  |  |  |  |
| text | generation | can | lead | to | even | longer | prompt | 3.2.1 | Model abstraction |  |  |  |  |
| processing time and lower efficiency. | In our model-based testing tool, we regard each activity |  |  |  |  |  |  |  |  |  |  |  |  |
| In this section, we present CamDroid, a context-aware | interactive widgets on each page are extracted and |  |  |  |  |  |  |  |  |  |  |  |  |
| model-based automated GUI testing tool that tackles | considered | as | events. | In | this | way, | we | construct | a |  |  |  |  |
| the above challenges. Our efforts lie in two folds. First, | probability | model | M | to | represent | the | relationships |  |  |  |  |  |  |
| we | propose | a | model-based | testing | tool | where | we | between activities and widgets in an app. Specifically, |  |  |  |  |  |
| carefully design its state abstraction and enable it to | M | stores event-activity transition probabilities, each |  |  |  |  |  |  |  |  |  |  |  |
| leverage historical context knowledge from previous | one of which is denoted as | p | ( | e | , | a | ) | , where |  |  |  |  |  |
| testing | runs. | Second, | we | introduce | a | lightweight | ● | e | represents for an event, |  |  |  |  |
| approach to generate text inputs by incorporating GUI | ● | a | represents for an app activity, and |  |  |  |  |  |  |  |  |  |  |
| widget | identities, | user | characteristics, | and | app | ● | p | represents the probability of the event | e | to reach |  |  |  |
| 3.1 | Overview of CamDroid | During the test, the model | M | is updated whenever an |  |  |  |  |  |  |  |  |  |
| utilizes the GUI info to extract feasible events. The | i | , | a | j | ) |  |  |  |  |  |  |  |  |
| event selection component then combines the one-step | n | ( | e | i | ) |  |  |  |  |  |  |  |  |
| guidance of the state transition model with the multi- | where | n | ( | e | i | , | a | j | ) | represents the number of times reaching |  |  |  |
| step guidance of reinforcement learning to choose the | a | j | after executing | e | i | , and | n | ( | e | i | ) | represents the total |  |
| best event. The text input generation component is | execution times of | e | i | . In order to reuse the context |  |  |  |  |  |  |  |  |  |
| activated | when | an | event | requiring | text | inputs | is | information | from | previous | testing | runs, | CamDroid |
| selected. This component utilizes a trained GAN to text | stores the model | M | as well as total execution times of |  |  |  |  |  |  |  |  |  |  |

---

## Page 5

| Hongyi Wang et al.: | CamDroid: Context-Aware Model-Based Automated GUI Testing for Android Apps | 59 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| each | event. | M | will | be | reconstructed | from | the | events | based | on | the | transition | probabilities | in | M | , |
| aforementioned values before the next testing run. | aiming to cover activities that have not been covered in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Additionally, | if | each | widget | is | considered | as | an | the current testing. |  |  |  |  |  |  |  |  |
| individual event, the scale of | M | would be rather large. | For each event | e | i | of all events | E | on the page, we |  |  |  |  |  |  |  |  |
| Therefore, | we | carefully | design | abstract | rules | for | calculate | the | probability | that | it | can | reach | a | new |  |
| widgets to prevent redundant records of widgets with | activity, | and | select | the | event | according | to | the |  |  |  |  |  |  |  |  |
| the same functionalities. In detail, we classify widgets | probability distribution. The probability (represented as |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| into | the | same | event | if | they | share | the | following | p | r | ) can be calculated according to | M | , |  |  |  |
| 6 properties: | the | activity | to | which | the | widget | ∑ |  |  |  |  |  |  |  |  |  |
| p | r | ( | e | i | ) | = | p | ( | e | i | , | a | j | ) | (2) |  |

belongs, content - description , text , resource - id ,

a j < A t

class - name , and allowed actions (i.e., click ,

where A

long click , scroll , and text input ). According to t is the set of activities tested in the current

testing run. The probability that event e

sampling observations, there are tens of widget i is selected

(represented as p

attributes that contain meaningful representatives of s ( e i ) ) is calculated through applying

the softmax function to p

| functionalities. | Furthermore, | based | on | statistical | r | ( | e | i | ) | , |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| calculation results, the heterogeneity is most prominent | exp ( | α | 1 | × | p | r | ( | e | i | )) |  |  |  |  |  |  |  |  |  |  |
| p | s | ( | e | i | ) | = | ∑ | (3) |  |  |  |  |  |  |  |  |  |  |  |  |
| among the aforementioned 6 properties, resulting in an | exp ( | α | 1 | × | p | r | ( | e | j | )) |  |  |  |  |  |  |  |  |  |  |
| effective abstraction. | e | j | ∈ | E |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The contents of the widget’s | text | , | resource | - | ID | , | where | α | 1 | is a float larger than 1 and is set as 1.25 in |  |  |  |  |  |  |  |  |  |  |
| and | content | - | description | sometimes overlap, as they | CamDroid. | Here | we | use | the | scaled | probability |  |  |  |  |  |  |  |  |  |
| often | provide | a | brief | summary | of | the | widget’s | α | 1 | × | p | r | ( | e | i | ) | instead of | p | r | to magnify the gaps among the |
| functionality, such as search or location. The reason for | probabilities assigned to different events. In this way, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| recording all three properties is that some widgets may | events with higher | p | r | values are further preferred, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| have empty values for some of them (this is also why | leading to faster exploration of uncovered activities. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| there is still significant heterogeneity among them). | Furthermore, we have detailed settings towards the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Imagine a scenario that a widget only has one non- | selection of events and actions for improving the test |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| empty property of these three, e.g., | text | with the | efficiency | in | CamDroid | from | the | following | three |  |  |  |  |  |  |  |  |  |  |  |
| content “search”, while another widget only has one | aspects. | First, | if | an | event | corresponds | to | multiple |  |  |  |  |  |  |  |  |  |  |  |  |
| non-empty | resource | - | ID | with the content “location”. | widgets, | CamDroid | will | randomly | select | one | for |  |  |  |  |  |  |  |  |  |
| If, unfortunately, they are on the same GUI page and | execution. Second, if the selected event has multiple |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| we | only | record | content | - | description | , | then | they | executable | actions | (e.g., | click | and | scroll | ), |  |  |  |  |  |
| would be mistakenly classified as the same event. By | CamDroid will prioritize actions that have not been |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| simultaneously recording these properties, we ensure | executed or have been executed only a few times. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| an accurate abstraction of the GUI event. With the size | Third, if an event on the current page has been selected |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| of | M | slightly increased, this approach guarantees a | twice under the one-step guidance, it will not be chosen |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| high precision for classifying the widgets into events. | for a time. This continues until all other events on the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3.2.2 | One-step guidance for event selection | page have been executed twice. Then their counters of |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| During | testing, | model | M | is | used | to | guide | event | execution times in this stage will be reset to 0. |  |  |  |  |  |  |  |  |  |  |  |
| selection. However, in the early stages of the test, | M | 3.2.3 | Multi-step guidance for event selection |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| only | has | limited | information. | Therefore, | event | Some activities may require sequential events to reach, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| selection at this stage is relatively random, aiming at | and for these activities, the aforementioned one-step |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| rapidly initializing model | M | . Specifically, when there | guidance | may | not | be | sufficient. | Reinforcement |  |  |  |  |  |  |  |  |  |  |  |  |
| are still unexecuted events on a page, that is, events not | learning, | on | the | other | hand, | enables | multi-step |  |  |  |  |  |  |  |  |  |  |  |  |  |
| recorded in | M | , CamDroid randomly selects one and | decision-making. Therefore, we have incorporated a |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| updates | M | based on the execution result. Once the | typical reinforcement learning algorithm, Q-learning, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| information in | M | is sufficient, it can be utilized to | into CamDroid to provide multi-step guidance. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| further explore unreached activities. When all events | The core of Q-learning is to utilize a Q-table to store |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| on a GUI page are included in | M | , CamDroid selects | the Q-values of actions (events in CamDroid), where |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 6

| 60 | Tsinghua Science and Technology, February | 2025, 30(1): 55−67 |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the Q-value represents the benefits that an action can | where | r | t | and | r | t | − | 1 | represent | instant | rewards | after |
| bring. In our tool, the Q-value suggests the probability | executing | e | t | and | e | t | − | 1 | , respectively. CamDroid gets an |  |  |  |
| of reaching new activities in the future. Then, at each | additional reward if it performs better at | t | than | t | − | 1 | . |  |  |  |  |  |
| time | t | CamDroid selects an event | e | t | (no matter whether | Similar to the one-step guidance, multi-step guidance |  |  |  |  |  |  |
| e | t | is selected under one-step guidance or multi-step | is | used | only | after | the | Q-table | contains | enough |  |  |
| guidance), observes a reward | r | t | , enters the activity | information,i.e., when all the events on the page have |  |  |  |  |  |  |  |  |
| a | t | + | 1 | , and updates the | Q | ( | e | t | ) | , | been executed at least twice under the former guidance. |  |
| new | We still use the softmax function to calculate | p | s | , |  |  |  |  |  |  |  |  |

| Q | ( | e | t | ) | = | (1 | − | β | ) | × | Q | ( | e | t | ) | + |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| s | r |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| β | × | ( | Q | t | ( | e | t | ) | + | Q | t | ( | e | t | )) | (4) |

where β is the learning rate and is set as 0.8. Q s

t ( e t ) is

the reward earned from this event e t , including the

immediate reward r t from e t and the potential future

rewards. Q r

t ( e t ) is a bonus reward, indicating whether

the selection at t is better than that at t − 1 .

Q s

for sequential decision guidance,

s

m − 1 m

where γ is the discount factor and is set as 0.5. m is the

number of steps taken into account for updating the Q-

values and set as 3. r t + i is the immediate reward from

event e t + i executed at time t + i .

The design of the reward can be approached from

two perspectives. From the aspect of events, the

benefits are higher when executing events with fewer

execution times but higher probabilities of reaching the

unvisited activities. From the aspect of activities, the

benefits are higher when accessing activities with

fewer visit times and more unexecuted events on the

| page. | Therefore, | r | e |
| --- | --- | --- | --- |
| t | = | r | a |

t + r t , where r e

t and r a

t are

calculated as follows:

e p r ( e t )

r t = √ (6)

n ( e t ) + 1

∑

a e i ∈ E t

on a t that have not been executed in the current testing

Q r

r

exp ( α

2 × Q ( e i ))

p s ( e i ) = ∑ (9)

exp ( α 2 × Q ( e j ))

e j ∈ E

where α 2 is set as 10.

3.2.4 Restructure the testing pipeline

In practice, we observe that there is a non-trivial

Benchmark experiments are conducted to identify such

actions with the help of the previous model-based

clicked right after the operation, and the new GUI page

is recorded. We repeat the above steps multiple times

to obtain two sets of GUI pages, and calculate the

difference between the two sets. Significant difference

indicates that the operation is irreversible. The

benchmark experiments ultimately yield 10+

irreversible operations.

To cover both GUI pages before and after these

operations, CamDroid intelligently select the timing to

perform them. When an irreversible action is

encountered, CamDroid checks whether the remaining

widgets on the activity have been selected during the

current test. CamDroid selects the action only after all

the other widgets have been executed at least once.

3.3 Text input generation

To better understand the scenarios of text inputs as well

study.

information, user preferences, and usage patterns.

| t | ( | e | t | ) | is calculated by the | N | -step Sarsa method | [28] | number | of | operations | which | are | irreversible. |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q | t | ( | e | t | ) | = | r | t | + | γ | r | t | + | 1 | + | · · · | + | testing tool. In detail, we record the GUI page before |
| γ | r | t | + | m | − | 1 | + | γ | Q | ( | e | t | + | m | ) | (5) | an operation is performed. Then the backward button is |  |
| n | ne | + | 0 | . | 5 | × | n | nt | + | p | r | ( | e | i | ) | as their categories and correlations in real world apps, |  |  |
| r | t | = | √ | (7) | we conduct a detailed research with one of the largest |  |  |  |  |  |  |  |  |  |  |  |  |  |
| n | ( | a | t | ) | + | 1 | Android | UI | datasets | Rico | [30] | . | Then | we | design | a |  |  |
| where | n | ne | denotes the number of events on | a | t | that have | lightweight tool for automated text input generation |  |  |  |  |  |  |  |  |  |  |  |
| never been executed. | n | nt | denotes the number of events | based | on | the | experience | from | the | aforementioned |  |  |  |  |  |  |  |  |
| run but executed in previous ones. | E | t | denotes the set of | Especially, the research on correlations between text |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| all events on | a | t | . | n | ( | a | t | ) | denotes the number of times | a | t | inputs is not straightforward, due to the lack of datasets |  |  |  |  |  |  |
| is visited in this testing run. | of real users’ continuous text inputs. Fortunately, we |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| t | ( | e | t | ) | is | designed | according | to | potential-based | notice that there are abundant datasets containing user |  |  |  |  |  |  |  |  |
| reward shaping | [29] | : | information from various apps, including basic user |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Q | t | ( | e | t | ) | = | γ | × | r | t | − | r | t | − | 1 | (8) | These pieces of information largely originate from the |  |

---

## Page 7

| Hongyi Wang et al.: | CamDroid: Context-Aware Model-Based Automated GUI Testing for Android Apps | 61 |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| text inputs during user interactions. Hence, we utilize | evaluate sentence similarity. We name each text input |  |  |  |  |  |  |  |  |  |  |  |  |  |
| open datasets of app user profiles for our research. | category by decoding the feature vector of its cluster |  |  |  |  |  |  |  |  |  |  |  |  |  |
| In addition, in order to address the problem of low | centroid (termed input context vector). We ultimately |  |  |  |  |  |  |  |  |  |  |  |  |  |
| efficiency in real-time text input generation, CamDroid | identify 81 classes of text input scenarios and list the |  |  |  |  |  |  |  |  |  |  |  |  |  |
| performs the generation before testing. During testing, | detailed information for the top-5 classes in Table 1. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CamDroid only selects the appropriate text according | 3.3.2 | Correlations between different categories |  |  |  |  |  |  |  |  |  |  |  |  |
| to the scenario, which greatly improves efficiency. The | According to the text input categories identified in |  |  |  |  |  |  |  |  |  |  |  |  |  |
| detailed pipeline is explained in Section 3.3.3. | Section 3.3.1, we select 11 datasets | [10–20] | to cover them. |  |  |  |  |  |  |  |  |  |  |  |
| 3.3.1 | Text input categories | We associate each category with attributes in public |  |  |  |  |  |  |  |  |  |  |  |  |
| Rico, the dataset we used for analysis, contains UI | datasets based on their meanings. Some categories, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| screenshots and their view hierarchy files from over | such | as | user | age | and | gender, | may | have |  |  |  |  |  |  |
| 9300 Android apps. We filter out pages that contain | correspondences in multiple public datasets. Attributes |  |  |  |  |  |  |  |  |  |  |  |  |  |
| text input widgets by checking if the | class | - | name | of a | in public datasets that do not have a corresponding text |  |  |  |  |  |  |  |  |  |
| widget | includes | the | keywords | “EditText” | and | input | category | are | removed. | Next, | we | calculate |  |  |
| “AutoCompleteTextView” | [31] | . | As | widgets | related | to | regression models | [33] | between each pair of attributes in |  |  |  |  |  |
| login are handled specifically in Section 3.2.4, we do | the same dataset, and then perform F-tests | [34] | on the |  |  |  |  |  |  |  |  |  |  |  |
| not consider them in the subsequent analysis. | obtained models. If the | p | -value of F-statistic is less |  |  |  |  |  |  |  |  |  |  |  |
| Finally, we get 2866 pages with 6846 text inputs | than 0.05, it indicates a significant correlation between |  |  |  |  |  |  |  |  |  |  |  |  |  |
| from a total of 2241 apps. We classify these apps into | them. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 categories referring to Google Play, i.e., finance, | Because not all inputs depend on others, we further |  |  |  |  |  |  |  |  |  |  |  |  |  |
| information, | entertainment, | video | streaming, | social, | divide these text input categories into independent and |  |  |  |  |  |  |  |  |  |
| reading, shopping, health, map, and travel, with each | non-independent | ones | based | on | the | results | of |  |  |  |  |  |  |  |
| category including 87 to 427 apps. | correlation calculations. First, we examine categories |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For each text input, we utilize the contexts of the | with | p | -values higher than 0.05 for all other columns in |  |  |  |  |  |  |  |  |  |  |  |
| GUI widget it belongs to along with the app metadata | the same dataset. In other words, the inputs for these |  |  |  |  |  |  |  |  |  |  |  |  |  |
| to | describe | the | scenario. | The | contexts | include | the | categories are independent of those in other scenarios. |  |  |  |  |  |  |
| hint | - | text | , | resource | - | id | , and | text | properties of the | We refer to them as independent categories. |  |  |  |  |
| widget, while app metadata includes the app category | Next, we look at combinations of categories with |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and the activity name. We tokenize and encode these | p | -values less than 0.05. For such a pair of categories, if |  |  |  |  |  |  |  |  |  |  |  |  |
| identities with Bert | [32] | , a well-established and widely | one of them has similar text input scenarios in more |  |  |  |  |  |  |  |  |  |  |  |
| used model in the field of NLP. As a result, we obtain a | than 5 app types, it indicates that it is common enough |  |  |  |  |  |  |  |  |  |  |  |  |  |
| vectorized | representation | of | the | current | text | input | to | be | regarded | as | an | independent | category. | The |
| scenario, which we refer to as a feature vector. Next, | threshold for universality 5 is set empirically based on |  |  |  |  |  |  |  |  |  |  |  |  |  |
| we | cluster | the | 6846 feature | vectors | to | explore | the | our manual inspection of representative samples. If |  |  |  |  |  |  |
| distribution | of | input | text | scenarios. | Specifically, | both categories are very universal, the one with similar |  |  |  |  |  |  |  |  |
| considering | our | large | data | scale, | we | employ | the | scenarios in more app types is an independent category, |  |  |  |  |  |  |
| DBSCAN clustering algorithm. The similarity between | while | the | other | one | is | not. | If | they | have | similar |  |  |  |  |
| vectors is measured by BERTScore | [21] | , a metric used to | scenarios in an equal number ( | ⩾ | 5) of app types, then |  |  |  |  |  |  |  |  |  |

Table 1 Detailed information for top-5 text input categories.

| Name | Brief description | Percentage ( | % | ) | Attribute | Independent |
| --- | --- | --- | --- | --- | --- | --- |
| Information-search-news | Input news keywords and search | 5.9 | News headlines | [12] | Yes |  |
| Health-host-height | Input the user’s height on the profile page | 4.7 | Height | [10] | No |  |

Input the destination on the navigation/

Travel-map-destination 4.3 Neighbourhood_group [20] No

booking page

| Social-profile-country | Input the country the user is from | 2.8 | Tweet_location | [15] | Yes |
| --- | --- | --- | --- | --- | --- |
| Shopping-product-name-search | Input a product name and search | 2.4 | Product_name | [17] | No |

Note: The columns respectively denote the classes’ names (Name, i.e., input context vector), a brief description of the scenario of the

text input category (Brief description), the percentage it occupies among all text inputs in Rico (Percentage), its corresponding attribute

in public datasets (Attribute), and whether it is an independent category or not.

---

## Page 8

| 62 | Tsinghua Science and Technology, February | 2025, 30(1): 55−67 |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| both are considered independent. | CamDroid determines the distribution functions for |  |  |  |  |  |  |  |  |  |  |  |  |
| This process allows us to identify all the independent | each independent category based on the app type. It |  |  |  |  |  |  |  |  |  |  |  |  |
| text input categories, while the remaining categories | then generates their text inputs using these distribution |  |  |  |  |  |  |  |  |  |  |  |  |
| are considered non-independent. Finally, the 81 text | functions. Then, these text inputs are input into the |  |  |  |  |  |  |  |  |  |  |  |  |
| input categories are classified into 33 independent ones | trained GAN model to produce content of all non- |  |  |  |  |  |  |  |  |  |  |  |  |
| and 48 non-independent ones. The pipeline for this | independent categories. During the test, if an event |  |  |  |  |  |  |  |  |  |  |  |  |
| classification is shown in Fig. 3 and the results of the | with | text | input | is | selected, | CamDroid | encodes | its |  |  |  |  |  |
| top-5 categories are recorded in Table 1. | context into a feature vector with the method described |  |  |  |  |  |  |  |  |  |  |  |  |
| After that, we utilize the Residual Sum of Squares | in Section 3.3.1. It calculates the BERTScore between |  |  |  |  |  |  |  |  |  |  |  |  |
| (RSS) | [35] | and Goodness Of Fit (GOF) | [36] | tests to study | this vector and each of the 81 input context vectors. |  |  |  |  |  |  |  |  |
| the | statistical | distribution | of | the | content | of | each | CamDroid | then | selects | the | pre-generated | content |
| independent category. Due to the distribution of an | corresponding to the input context vector with the |  |  |  |  |  |  |  |  |  |  |  |  |
| independent category may vary across different types | highest score to fill in. |  |  |  |  |  |  |  |  |  |  |  |  |

of apps, we perform fitting for each app class.

Furthermore, we employ a GAN [37] to learn the

relationship between the content of non-independent

and independent categories. The GAN takes the

content of all independent ones as input and outputs the

corresponding content for all non-independent ones. In

this method, we obtain the distributions and

dependency relationships among various text input

categories, which prepares us for the automatic

generation.

3.3.3 Text input generation pipeline

The pipeline is divided into two stages: pre-test and in-

test. Before the test, CamDroid utilizes the knowledge

from Section 3.3.2 to generate all the potential inputs,

i.e., the content of the 81 text input categories.

in the same dataset

No

No

Independent Dose A appear in more No

Non-independent

than 5 app types ?

Yes

No Dose B appear in more

than 5 app types ?

Yes

A Which category appears B

Independent Non-independent

3.4 Implementation

The prototype of CamDroid is implemented based on

the source of Android Monkey and includes server and

client components. The client part can be installed and

used directly through Android Debug Bridge (ADB)

without any additional modifications to the device or

the app under test. It is compatible with both physical

and virtual devices and supports Android 10−13. The

selection of events and the generation of text inputs are

carried out on the server side, and the historical context

information is stored in an online database. Therefore,

CamDroid only occupies a minimal amount of

hardware resources on the device.

4 Evaluation

APE [6] , and Fastbot2 [7] . The highlights are as follows:

CamDroid improves the average (median) activity

CamDroid detects 1.89× to 8.50× more crashes than

the baselines.

● The learning-based text input generation approach

alone improves the activity coverages of CamDroid

4.1 Experimental setup

Setup. All tools can run without modifications to apps

phones with the same configuration (i.e., Snapdragon

| Category A | We evaluate CamDroid on 20 widely-used apps from |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Loop: | Google Play and compare its performance with 3 state- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Category B | of-the-art | automated | testing | tools | i.e., | Monkey | [22] | , |  |  |  |  |  |  |  |  |
| F-testing | ● | Compared | with | the | field-renowned | baselines, |  |  |  |  |  |  |  |  |  |  |
| Last category? | p | -value | ≤ | 0.05 | coverage by 1.25× to 3.69× (1.27× to 5.45×). |  |  |  |  |  |  |  |  |  |  |  |
| Yes | Yes | ● Within the time limitation of industrial app testing, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Independent | and all the baselines by 1.13× to 1.19×. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| in more app types? | and devices. We conduct parallel tests on four mobile |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Fig. 3 | Pipeline | of | classifying | text | input | categories | into | 855 | 2.84 | GHz | CPU, | 6 | GB | RAM, | and | Android |
| independent and non-independent ones. | 11 operating system) to mitigate potential bias. We |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 9

Hongyi Wang et al.: CamDroid: Context-Aware Model-Based Automated GUI Testing for Android Apps 63

choose Android 11 because it had the highest market

share when we started our development (Jan. 2023),

and it can cover the new functions and performance

improvements introduced in Android 10 compared to

Android 9 [38] . Following previous work [6, 24, 39] , the

four tools are set to perform a 1-hour test on each app.

Each test is repeated 5 times. The average activity

coverage and the total number of detected crashes are

used to evaluate their performance.

Benchmark collection. We select 20 widely-used

apps as our test subjects. Specifically, for each of the

choose 2 apps with high downloads on Google Play.

4.2 Performance on benchmark apps

Figure 4 illustrates the activity coverage of four tools

across the 20 apps. It is evident that CamDroid

Table 2 Mobile apps used for testing.

Number of

downloads Total

ID App Type

on Google activities

Play

Video

5 Youtube 55

streaming > 1 × 10 10

Video

| 7 | iQiyi |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | Resso Music | Entertainment | > | 5 | × | 10 | 7 | 53 |
| 9 | Booking | Travel | > | 5 | × | 10 | 8 | 295 |
| 10 | YahooFinance | Finance | > | 1 | × | 10 | 7 | 92 |
| 11 | Tencent News | Information | > | 1 | × | 10 | 5 | 149 |
| 12 | Vested | Finance | > | 5 | × | 10 | 5 | 31 |
| 13 | Fitbit | Health | > | 5 | × | 10 | 7 | 456 |
| 14 | Kindle | Reading | > | 1 | × | 10 | 8 | 142 |
| 15 | Fizzo Novel | Reading | > | 5 | × | 10 | 4 | 118 |
| 16 | Amazon | Shopping | > | 5 | × | 10 | 8 | 85 |
| 17 | AliExpress | Shopping | > | 5 | × | 10 | 8 | 379 |
| 18 | Google Map | Maps | > | 1 | × | 10 | 10 | 36 |
| 19 | Citymapper | Maps | > | 1 | × | 10 | 7 | 100 |
| 20 | Fasting | Health | > | 1 | × | 10 | 7 | 94 |

Activity coverage (%)

tools.

universality.

Overall, CamDroid shows a more pronounced

improvement over the baselines in apps with more

activities, such as Booking and AliExpress. This is

because the baselines face more difficulties in

comprehensively exploring these complex apps. In

contrast, apps with fewer activities are more prone to

reaching saturation, limiting the potential for

compared to human users.

In terms of crash detection, as shown in Fig. 5,

number of crashes uncovered by these tools is

relatively low. Nevertheless, CamDroid, with its high

testing efficiency, manages to discover 34 crashes

across the 20 apps, whereas Monkey, APE, and

Fastbot2 only find 4, 8, and 18 crashes, respectively.

All the crashes detected by CamDroid can be

reproduced reliably.

4.3 Ablation study

We conduct ablation study to explore the effectiveness

of our model-based testing tool and learning-based text

input generation method. We integrate the text

generation method into Monkey, APE, and Fastbot2,

and test them following the approach described in

| 10 app types mentioned in Section 3.3.1, we randomly | Fig. 4 | Results of activity coverage by CamDroid and other |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| We filter out apps if (1) they contain too few activities | achieves the highest coverage on each app. Its average |  |  |  |  |  |  |  |  |  |  |  |  |
| ( | ⩽ | 30 | ); (2) they have no text input widgets; (3) their | (median) activity coverage on the 20 apps is 3.69× |  |  |  |  |  |  |  |  |  |
| view hierarchy files are inaccessible by UIAutomator | [40] | ; | (5.45×), | 1.94× | (2.11×), | 1.25× | (1.27×) | higher | than |  |  |  |  |
| and (4) one or more baselines crash on them. We | Monkey, | APE, | and | Fastbot2, | respectively. |  |  |  |  |  |  |  |  |
| present the basic information of the 20 selected apps in | Furthermore, CamDroid performs well regardless of |  |  |  |  |  |  |  |  |  |  |  |  |
| Table 2. | app’s type and number of activities, which indicates its |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | Dianping | Travel | > | 1 | × | 10 | 6 | 535 | enhancement. Relatively, all four tools exhibit poorer |  |  |  |  |
| 2 | Weibo | Social | > | 1 | × | 10 | 7 | 778 | performance on Dianping, Weibo, and Facebook. This |  |  |  |  |
| 3 | Facebook | Social | > | 5 | × | 10 | 9 | 862 | is due to the strong interactivity of these three apps, |  |  |  |  |
| 4 | Netease News | Information | > | 1 | × | 10 | 4 | 249 | where automated testing tools still face certain gaps |  |  |  |  |
| 6 | Kugou Music Entertainment | > | 5 | × | 10 | 4 | 258 | CamDroid also performs the best. Since these apps |  |  |  |  |  |
| streaming | > | 5 | × | 10 | 7 | 279 | undergo | thorough | test | before | being | released, | the |

---

## Page 10

64 Tsinghua Science and Technology, February 2025, 30(1): 55−67

Fig. 5 Results of crash detection by CamDroid and other

tools.

method improves the activity coverage of Monkey,

APE, and Fastbot2 by 1.13×, 1.19×, and 1.15×,

Activity coverage ( % )

ID

one without it. Relatively speaking, Monkey shows the

lowest improvement, which can be attributed to its

lower activity coverage, thus triggering fewer pages

containing text input widgets. On the other hand, APE

demonstrates the highest improvement. This is because

both Fastbot2 and CamDroid already achieve high

reach saturation. The numbers of crashes discovered by

Monkey, APE, and Fastbot2 increase by 1.75× (7 vs. 4),

1.89× (15 vs. 8), and 1.78× (32 vs. 18), respectively.

Additionally, as shown in Table 3, CamDroid

without text input generation (referred to as C-T) also

performs better than the baselines. Its average activity

5 Related Work

# Uncovered crashes

| Uncovered crashes | activity coverages, and their effectiveness may easily |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Section | 4.1. | We | also | evaluate | the | performance | of | coverage is 16.7 | % | , which is 3.21× higher than Monkey |  |
| CamDroid | without | the | text | input | generation. | The | (5.2 | % | ), 1.69× higher than APE (9.9 | % | ), and 1.09× |
| results in Table 3 illustrate that both aspects of our | higher than Fastbot2 (15.3 | % | ). It discovers a total of |  |  |  |  |  |  |  |  |
| efforts contribute to CamDroid's overall performance. | 21 unique crashes, which are 5.25×, 2.62×, and 1.17× |  |  |  |  |  |  |  |  |  |  |
| It can be observed that our text input generation | as many as Monkey (4), APE (8), and Fastbot2 (18). |  |  |  |  |  |  |  |  |  |  |
| respectively. CamDroid, with text input generation, | Our | work | integrates | learning-based | text | input |  |  |  |  |  |
| achieves a coverage increase of 1.15× compared to the | generation with model-based automated GUI testing |  |  |  |  |  |  |  |  |  |  |

Table 3 Activity coverage and crash detection with automated GUI testing tool with and without text input generation.

| M | M+T | A | A+T | F | F+T | C-T | C | M | M+T | A | A+T | F | F+T | C-T | C |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2.2 | 2.6 ↑ | 3.2 | 3.6 ↑ | 4.7 | 5.2 ↑ | 4.9 | 5.6 ↑ | 0 | 0 − | 1 | 1 − | 0 | 2 ↑ | 1 | 2 ↑ |
| 2 | 2.1 | 2.3 ↑ | 3.7 | 4.5 ↑ | 5.5 | 6.4 ↑ | 5.8 | 6.6 ↑ | 0 | 1 ↑ | 0 | 1 ↑ | 1 | 1 − | 2 | 2 − |
| 3 | 2.6 | 3.0 ↑ | 4.8 | 5.0 ↑ | 5.8 | 6.7 ↑ | 6.4 | 8.0 ↑ | 0 | 0 − | 0 | 0 − | 1 | 1 − | 1 | 1 − |
| 4 | 1.6 | 1.6 − | 3.2 | 3.6 ↑ | 5.6 | 7.6 ↑ | 6.4 | 8.0 ↑ | 0 | 0 − | 0 | 0 − | 1 | 2 ↑ | 1 | 3 ↑ |
| 5 | 1.8 | 1.8 − | 3.6 | 3.6 − | 5.5 | 7.3 ↑ | 7.3 | 9.0 ↑ | 0 | 0 − | 1 | 1 − | 1 | 2 ↑ | 1 | 2 ↑ |
| 6 | 1.9 | 2.3 ↑ | 5.4 | 5.8 ↑ | 8.5 | 9.3 ↑ | 9.7 | 10.9 ↑ | 0 | 0 − | 0 | 0 − | 1 | 1 − | 1 | 1 − |
| 7 | 3.6 | 3.9 ↑ | 7.2 | 8.2 ↑ | 10.4 | 11.1 ↑ | 10.8 | 12.2 ↑ | 0 | 0 − | 0 | 0 − | 1 | 1 − | 1 | 2 ↑ |
| 8 | 1.9 | 3.8 ↑ | 7.5 | 7.5 − | 13.2 | 13.2 − | 13.2 | 15.6 ↑ | 1 | 1 − | 0 | 1 ↑ | 0 | 2 ↑ | 1 | 1 − |
| 9 | 7.1 | 7.1 − | 9.5 | 11.9 ↑ | 14.2 | 17.3 ↑ | 15.9 | 17.4 ↑ | 0 | 0 − | 0 | 0 − | 1 | 1 − | 0 | 1 ↑ |
| 10 | 3.3 | 5.4 ↑ | 7.6 | 9.8 ↑ | 16.3 | 18.5 ↑ | 18.5 | 20.6 ↑ | 0 | 1 ↑ | 1 | 1 − | 1 | 1 − | 1 | 1 − |
| 11 | 10.1 | 10.1 − | 14.1 | 16.8 ↑ | 16.8 | 19.5 ↑ | 19.5 | 20.8 ↑ | 1 | 1 − | 1 | 2 ↑ | 1 | 2 ↑ | 2 | 2 − |
| 12 | 6.5 | 6.5 − | 12.9 | 12.9 − | 16.1 | 19.4 ↑ | 16.1 | 20.9 ↑ | 0 | 0 − | 1 | 2 ↑ | 1 | 2 ↑ | 1 | 2 ↑ |
| 13 | 2.0 | 3.1 ↑ | 11.2 | 15.4 ↑ | 18.4 | 23.5 ↑ | 19.5 | 22.7 ↑ | 0 | 1 ↑ | 0 | 1 ↑ | 1 | 2 ↑ | 0 | 1 ↑ |
| 14 | 7.0 | 9.2 ↑ | 14.1 | 16.9 ↑ | 18.3 | 21.8 ↑ | 18.3 | 22.9 ↑ | 1 | 1 − | 0 | 0 − | 1 | 1 − | 2 | 2 − |
| 15 | 5.1 | 5.1 − | 11.9 | 15.3 ↑ | 17.8 | 19.5 ↑ | 20.3 | 23.0 ↑ | 0 | 0 − | 0 | 0 − | 1 | 1 − | 1 | 2 ↑ |
| 16 | 5.9 | 5.9 − | 12.9 | 15.3 ↑ | 21.2 | 22.4 ↑ | 22.4 | 26.2 ↑ | 0 | 0 − | 1 | 1 − | 2 | 2 ↑ | 1 | 2 ↑ |
| 17 | 4.0 | 5.0 ↑ | 10.0 | 14.2 ↑ | 20.3 | 21.9 ↑ | 23.5 | 26.5 ↑ | 0 | 0 − | 1 | 1 − | 2 | 2 − | 2 | 3 ↑ |
| 18 | 5.6 | 8.3 ↑ | 11.1 | 13.9 ↑ | 19.4 | 22.2 ↑ | 22.2 | 27.0 ↑ | 0 | 0 − | 0 | 1 ↑ | 0 | 2 ↑ | 0 | 1 ↑ |
| 19 | 19.0 | 21.0 ↑ | 25.0 | 26.0 ↑ | 31.0 | 35.0 ↑ | 31.0 | 35.0 ↑ | 1 | 1 − | 1 | 1 − | 0 | 2 ↑ | 0 | 1 ↑ |
| 20 | 10.6 | 10.6 − | 19.1 | 26.6 ↑ | 36.2 | 44.7 ↑ | 42.6 | 47.3 ↑ | 0 | 0 − | 0 | 1 ↑ | 1 | 2 ↑ | 2 | 1 − |

Note: “M” denotes Monkey, “A” denotes APE, and “F” denotes Fastbot2. “M+T”, “A+T”, and “F+T” denote Monkey, APE, and

Fastbot2 with our text input generation method. “C-T” denotes CamDroid without text input generation. “C” denotes CamDroid. “↑”

means performance increase of automated testing tools after integrating text input generation and “−” means no growth.

---

## Page 11

| Hongyi Wang et al.: | CamDroid: Context-Aware Model-Based Automated GUI Testing for Android Apps | 65 |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| for Android apps. CamDroid automates the GUI testing | reinforcement | learning, | CamDroid | leverages | the |  |  |  |  |  |  |  |
| of Android apps using a combinatorial model with the | context knowledge of previous tests to efficiently and |  |  |  |  |  |  |  |  |  |  |  |
| one-step guidance of event-activity transitions and the | effectively explore app activities. Moreover, CamDroid |  |  |  |  |  |  |  |  |  |  |  |
| multi-step | guidance | of | reinforcement | learning, | and | efficiently | generates | text | inputs | regarding | the | GUI |
| generates text inputs like real users with a GAN based | context like real users through pre-training a GAN |  |  |  |  |  |  |  |  |  |  |  |
| on public datasets. We review related literature in this | based | on | public | datasets | when | encountering | GUI |  |  |  |  |  |
| section. | widgets | requiring | text | inputs. | Experiments | with |  |  |  |  |  |  |
| Monkey | [22] | is the most classical and lightweight tool | 20 widely-used | apps | from | Google | Play | show | that |  |  |  |
| to perform black box testing. Given that the exploration | CamDroid outperforms 3 state-of-the-art testing tools |  |  |  |  |  |  |  |  |  |  |  |
| strategy of Monkey is completely random, Monkey | in terms of both activity coverage and number of |  |  |  |  |  |  |  |  |  |  |  |
| lacks extensibility and is easy to bypass intentionally. | detected | crashes | within | industrial | testing | time |  |  |  |  |  |  |
| To strategically automate the GUI testing for Android | limitation. |  |  |  |  |  |  |  |  |  |  |  |

apps, learning-based approaches have been widely

studied [8, 41, 42] . Humanoid [8] is a representative one that

Since the GUI switches of apps can be modeled as

state transitions via UI actions, a plethora of model-

based testing approaches [6, 7, 25, 43] emerge. Recently,

proposed by ByteDance and achieves outstanding

industrial success. However, when encountering

to generating text inputs like real users [27, 44, 45] .

Existing text input generation methods either rely on

language models requiring undesirable prompt

generation effects with the help of the generation-and-

selection pipeline. In addition, CamDroid considers the

correlations of multiple text inputs during a single test,

This paper presents a context-aware model-based GUI

Acknowledgment

100336949).

References

scales: Systematically adapting to the new technological

landscape, IEEE Transactions on Mobile Computing , vol.

21, no.12, pp. 4488–4501, 2021.

1615–1628, 2020.

[4] L. Gong, Z. Li, F. Qian, Z. Zhang, Q. Chen, Z. Qian, H.

Lin, and Y. Liu, Experiences of landing machine learning

France, 2020, pp. 1–14.

android malware at market scales, in Proc. 17th Annual

International Conference on Mobile Systems,

Applications, and Services , Seoul, Republic of Korea,

2019, pp. 168–179.

Lu, and Z. Su, Practical GUI testing of android

Proc. 41st International Conference on Software

Engineering , Montreal, Canada, 2019, pp. 269–280.

| uses a deep neural network model to learn how users | This work was supported by the National Key R&D |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| choose UI actions from human interaction traces. Such | Program of China (No. 2022YFB4500703), the National |  |  |  |  |  |  |  |  |  |
| approaches require specific sequential trace data and in | Natural Science Foundation of China (Nos. 61902211 and |  |  |  |  |  |  |  |  |  |
| the | early | stage | of | the | test, | they | have | similar | 62202266), the China Postdoctoral Science Foundation |  |
| performance with the random strategy. | (No. 2022M721831), and Microsoft Research Asia (No. |  |  |  |  |  |  |  |  |  |
| APE, a practical model-based approach via dynamic | [1] | Number of android apps, https://www.appbrain.com/stats/ |  |  |  |  |  |  |  |  |
| model abstraction, has significantly advanced the state- | number-of-android-apps, 2022. |  |  |  |  |  |  |  |  |  |
| of-the-art | model-based | techniques | [6] | . | Furthermore, | [2] | L.i Gong, Z. Li, H. Wang, H. Lin, X. Ma, and Y. Liu, |  |  |  |
| based on the implementation of APE, Fastbot2 | [7] | is | Overlay-based | android | malware | detection | at | market |  |  |
| scenarios with text input requirements, these methods | [3] | L. Gong, H. Lin, Z. Li, F. Qian, Y. Li, X. Ma, and Y. Liu, |  |  |  |  |  |  |  |  |
| just randomly input and thus possibly miss the hidden | Systematically | landing | machine | learning | onto | market- |  |  |  |  |
| activities with specific inputs to reach. | scale mobile malware detection, | IEEE Transactions on |  |  |  |  |  |  |  |  |
| To fill the above gap, many efforts have been devoted | Parallel | and | Distributed | Systems | , | vol. | 32, | no. | 7, | pp. |
| large amounts of manual text input samples and thus | onto market-scale mobile malware detection, in | Proc. 15th |  |  |  |  |  |  |  |  |
| lack | generalizability | [44] | , | or | adopt | heavy-weight | European Conference on Computer Systems | , Bordeaux, |  |  |
| processing time | [27] | . Different from them, CamDroid | [5] | Y. Yan, Z. Li, Q. Chen, C. Wilson, T. Xu, E. Zhai, Y. Li, |  |  |  |  |  |  |
| achieves | high | input | efficiency, | as | well | as | good | and Y. Liu, Understanding and detecting overlay-based |  |  |
| resulting in more realistic behaviors. | [6] | T. Gu, C. Sun, X. Ma, C. Cao, C. Xu, Y. Yao, Q. Zhang, J. |  |  |  |  |  |  |  |  |
| 6 | Conclusion | applications | via | model | abstraction | and | refinement, | in |  |  |
| testing approach for Android apps, named CamDroid. | [7] | Z. Lv, C. Peng, Z. Zhang, T. Su, K. Liu, and P. Yang, |  |  |  |  |  |  |  |  |
| Through combining the one-step guidance of event- | Fastbot2: Reusable automated model-based GUI testing |  |  |  |  |  |  |  |  |  |
| activity | transitions | and | the | multi-step | guidance | of | for android enhanced by reinforcement learning, in | Proc. |  |  |

---

## Page 12

| 66 | Tsinghua Science and Technology, February | 2025, 30(1): 55−67 |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 37th | International | Conference | on | Automated | Software | Wang, Fill in the blank: Context-aware automated text |  |  |  |  |  |  |
| Engineering | , Rochester, MI, USA, 2022, pp. 1–5. | input generation for mobile GUI testing, in | Proc. 45th |  |  |  |  |  |  |  |  |  |
| [8] | Y. Li, Z. Yang, Y. Guo, and X. Chen, Humanoid: A deep | International | Conference | on | Software | Engineering | , |  |  |  |  |  |
| learning-based approach to automated black-box android | Melbourne, Australia, 2023, pp. 1355–1367. |  |  |  |  |  |  |  |  |  |  |  |
| app testing, in | Proc. 34th International Conference on | [28] | K. | De | Asis, | J | Hernandez-Garcia, | G | Holland, | and | R. |  |
| Automated Software Engineering | , San Diego, CA, USA, | Sutton, | Multi-step | reinforcement | learning: | A | unifying |  |  |  |  |  |
| 2019, pp. 1070–1073. | algorithm, in | Proc. 32nd AAAI Conference on Artificial |  |  |  |  |  |  |  |  |  |  |
| [9] | H. Lin, J. Qiu, H. Wang, Z. Li, L.i Gong, D. Gao, Y. Liu, | Intelligence | , New Orleans, LA, USA, 2018, pp. 2902– |  |  |  |  |  |  |  |  |  |
| F. Qian, Z. Zhang, P. Yang, et al., Virtual device farms for | 2909. |  |  |  |  |  |  |  |  |  |  |  |
| mobile | app | testing | at | scale, | in | Proc. | 29th | ACM | [29] | Y. Gao and F. Toni, Potential based reward shaping for |  |  |
| International | Conference | on | Mobile | Computing | and | hierarchical | reinforcement | learning, | in | Proc. | 24th |  |
| Networking | , Madrid, Spain, 2023, pp. 1–17. | International Joint Conference on Artificial Intelligence | , |  |  |  |  |  |  |  |  |  |
| [10] | Body | fat | prediction | dataset, | https://www.kaggle.com/ | Buenos Aires, Argentina, 2015, pp 3504–3510. |  |  |  |  |  |  |
| datasets/fedesoriano/body-fat-prediction-dataset, 2021. | [30] | B. Deka, Z. Huang, C. Franzen, J. Hibschman, D. Afergan, |  |  |  |  |  |  |  |  |  |  |
| [11] | Bank customers churn, https://www.kaggle.com/datasets/ | Y. Li, J. Nichols, and R. Kumar, Rico: A mobile app |  |  |  |  |  |  |  |  |  |  |
| santoshd3/bank-customers, 2018. | dataset for building data-driven design applications, in |  |  |  |  |  |  |  |  |  |  |  |
| [12] | A | million | news | headlines, | https://www.kaggle.com/ | Proc. 30th Annual ACM Symposium on User Interface |  |  |  |  |  |  |
| datasets/therohk/million-headlines, 2022. | Software and Technology | , Quebec City, Canada, 2017, pp. |  |  |  |  |  |  |  |  |  |  |
| [13] | Movielens 20m dataset, https://www.kaggle.com/datasets/ | 845–854. |  |  |  |  |  |  |  |  |  |  |
| grouplens/movielens-20m-dataset, 2018. | [31] | Google, Introduction of text input, https://developer.android. |  |  |  |  |  |  |  |  |  |  |
| [14] | Dataset | for | chatbot, | https://www.kaggle.com/datasets/ | com/reference/android/widget/EditText?hl=en, 2023. |  |  |  |  |  |  |  |
| grafstor/simple-dialogs-for-chatbot, 2020. | [32] | J. Devlin, M. Chang, K. Lee, and K. Toutanova. Bert: Pre- |  |  |  |  |  |  |  |  |  |  |
| [15] | Twitter | friends, | https://www.kaggle.com/datasets/ | training of deep bidirectional transformers for language |  |  |  |  |  |  |  |  |
| hwassner/TwitterFriends, 2016. | understanding, arXiv preprint arXiv: 1810.04805, 2018. |  |  |  |  |  |  |  |  |  |  |  |
| [16] | Goodreads | books, | https://www.kaggle.com/datasets/ | [33] | T. Amemiya, Non-linear regression models, | Handbook of |  |  |  |  |  |  |
| jealousleopard/goodreadsbooks, 2019. | Econometrics | , vol. 1, pp. 333–389, 1983. |  |  |  |  |  |  |  |  |  |  |
| [17] | Amazon sales dataset, https://www.kaggle.com/datasets/ | [34] | L. | M. | Lix, | J. | C. | Keselman, | and | H. | J. | Keselman, |
| karkavelrajaj/amazon-sales-dataset, 2019. | Consequences | of | assumption | violations | revisited: | A |  |  |  |  |  |  |
| [18] | Medical transcriptions, https://www.kaggle.com/datasets/ | quantitative review of alternatives to the one-way analysis |  |  |  |  |  |  |  |  |  |  |
| tboyle10/medicaltranscriptions, 2018. | of variance f test, | Review of Educational Research | , vol. |  |  |  |  |  |  |  |  |  |

[19] China city dataset, https://github.com/brightgems/china_

[20] New york city airbnb 2023, public data, https://www.

kaggle.com/datasets/godofoutcasts/new-york-city-airbnb-

[23] R. Mahmood, N. Mirzaei, and S. Malek, Evodroid:

[24] K. Mao, M. Harman, and Y. Jia, Sapienz: Multi-objective

automated testing for android applications, in Proc. 25th

Proc. 39th International Conference on Software

66, no. 4, pp. 579–619, 1996.

sum of squares for all possible regressions, Technometrics ,

vol. 14, no. 2, pp. 317–325, 1972.

Canada, 2014, pp. 2672–2680.

Technologies, Architectures, and Protocols for Computer

Communication , Virtual Event, 2021, pp. 597–609.

623–640, 2013.

| city_dataset, 2017. | [35] | J. A. Morgan and J. F. Tatar, Calculation of the residual |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2023-public-data, 2023. | [36] | E. B. Andersen, A goodness of fit test for the rasch model. |  |  |  |  |  |  |  |  |  |  |  |
| [21] | T. Zhang, V. Kishore, F. Wu, K. Weinberger, and Y. | Psychometrika | , vol. 38, pp. 123–140, 1973. |  |  |  |  |  |  |  |  |  |  |
| Artzi, BERTScore: Evaluating text generation with bert, | [37] | I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. |  |  |  |  |  |  |  |  |  |  |  |
| arXiv preprint arXiv: 1904.09675, 2019. | Warde-Farley, S. Ozair, A. Courville, and Y. Bengio, |  |  |  |  |  |  |  |  |  |  |  |  |
| [22] | Google, Ui/application exerciser monkey, https://developer. | Generative adversarial nets, in | Proc. 28th Conference on |  |  |  |  |  |  |  |  |  |  |
| android.com/studio/test/monkey.html, 2018. | Neural | Information | Processing | Systems | , | Montreal, |  |  |  |  |  |  |  |
| Segmented evolutionary testing of android apps, in | Proc. | [38] | Y. Li, H. Lin, Z. Li, Y. Liu, F. Qian, L. Gong, X. Xin, and |  |  |  |  |  |  |  |  |  |  |
| 22nd | ACM | SIGSOFT | International | Symposium | on | T. | Xu, | A | nationwide | study | on | cellular | reliability: |
| Foundations of Software Engineering | , Hong Kong, China, | Measurement, analysis, and enhancements, in | Proc. of |  |  |  |  |  |  |  |  |  |  |
| 2014, pp. 599–609. | 2021 ACM | International | Conference | on | Applications, |  |  |  |  |  |  |  |  |
| International | Symposium | on | Software | Testing | and | [39] | S. Choudhary, A. Gorla, and A. Orso, Automated test |  |  |  |  |  |  |
| Analysis | , Saarbrucken, Germany, 2016, pp. 94–105. | input generation for android: Are we there yet? in | Proc. |  |  |  |  |  |  |  |  |  |  |
| [25] | T. Su, G. Meng, Y. Chen, K. Wu, W. Yang, Y. Yao, G. | 30th | International | Conference | on | Automated | Software |  |  |  |  |  |  |
| Pu, Y. Liu, and Z. Su, Guided, stochastic model-based | Engineering | , Lincoln, NE, USA, 2015, pp. 429–440. |  |  |  |  |  |  |  |  |  |  |  |
| GUI testing of android apps, in | Proc. 11th Joint Meeting | [40] | Google, | Ui | automator, | https://developer.android.com/ |  |  |  |  |  |  |  |
| on | Foundations | of | Software | Engineering | , | Paderborn, | training/testing/other-components/ui-automator, 2021. |  |  |  |  |  |  |
| Germany, 2017, pp. 245–256. | [41] | W. Choi, G. Necula, and K. Sen, Guided GUI testing of |  |  |  |  |  |  |  |  |  |  |  |
| [26] | Y. Li, Z. Yang, Y. Guo, and X. Chen, Droidbot: A | android | apps | with | minimal | restart | and | approximate |  |  |  |  |  |
| lightweight UI-guided test input generator for android, in | learning, | ACM | Sigplan | Notices | , | vol. | 48, | no. | 10, | pp. |  |  |  |
| Engineering Companion | , Buenos, Aires, 2017, pp. 23–26. | [42] | C. Degott, N. B. Jr, and A. Zeller, Learning user interface |  |  |  |  |  |  |  |  |  |  |
| [27] | Z. Liu, C. Chen, J. Wang, X. Che, Y. Huang, J. Hu, and Q. | element | interactions, | in | Proc. | 28th | ACM | SIGSOFT |  |  |  |  |  |

---

## Page 13

| Hongyi Wang et al.: | CamDroid: Context-Aware Model-Based Automated GUI Testing for Android Apps | 67 |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| International | Symposium | on | Software | Testing | and | L. | Zeng, | Automatic | text | input | generation | for | mobile |
| Analysis | , Beijing, China, 2019, pp. 296–306. | testing, | in | Proc. | 39th | International | Conference | on |  |  |  |  |  |
| [43] | S. Hao, B. Liu, S. Nath, W. Halfond, and R. Govindan, | Software Engineering | , Buenos, Aires, 2017, pp. 643–653. |  |  |  |  |  |  |  |  |  |  |
| Puma: | Programmable | ui-automation | for | large-scale | [45] | Y. He, L. Zhang, Z. Yang, Y. Cao, K. Lian, S. Li, W. |  |  |  |  |  |  |  |
| dynamic analysis of mobile apps, in | Proc. 12th Annual | Yang, Z. Zhang, M. Yang, Y. Zhang, et al., Textexerciser: |  |  |  |  |  |  |  |  |  |  |  |
| International | Conference | on | Mobile | Aystems, | Feedback-driven | text | input | exercising | for | android |  |  |  |
| Applications, and Services | , Bretton Woods, NH, USA, | applications, in | Proc. 41st IEEE Symposium on Security |  |  |  |  |  |  |  |  |  |  |

and Privacy , San Francisco, CA, USA, 2020, pp.

2014, pp. 204–217.

| [44] | P. Liu, X. Zhang, M. Pistoia, Y. Zheng, M. Marques, and | 1071–1087. |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hongyi Wang | received the BEng degree | Daqiang Hu | received the BEng degree |  |  |  |  |  |
| from Tsinghua University, China in 2021. | from University of Electronic Science and |  |  |  |  |  |  |  |
| She is working towards the PhD degree at | Technology | of | China | in | 1993, | and | the |  |
| School of Software, Tsinghua University, | MEng degree from Chongqing University |  |  |  |  |  |  |  |
| Beijing, China. Her research areas mainly | of Posts and Telecommunications, China |  |  |  |  |  |  |  |
| include network measurement and machine | in | 1996. | He | is | the | CEO | of | Hangzhou |
| learning. | Uusense | Technology | Inc., | China. | His |  |  |  |

research areas mainly include automated

software testing and network measurement.

Yang Li received the BEng and MEng

| degrees from Tsinghua University, China | Zhi Liao | received the BEng degree from |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| in | 2018 and | 2021, | respectively. | He | is | Central China Normal University in 2001. |  |
| working towards the PhD degree at School | He | is | the | CTO | of | Hangzhou | Uusense |
| of Software, Tsinghua University, Beijing, | Technology Inc., China. His research areas |  |  |  |  |  |  |
| China. His research areas mainly include | mainly include automated software testing |  |  |  |  |  |  |
| big data analysis, network measurement, | and network measurement. |  |  |  |  |  |  |

and machine learning.

Jing Yang received the BEng degree from

Tongji University, China in 2023. She is

currently a master student at School of

Software, Tsinghua University, Beijing,

China. Her research areas mainly include

network measurement and machine

learning.

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*

*[Image: Page 13 Image]*
