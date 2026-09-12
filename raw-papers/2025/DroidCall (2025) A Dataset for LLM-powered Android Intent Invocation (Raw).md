---
title: "DroidCall: A Dataset for LLM-powered Android Intent Invocation"
author: "Weikai Xie, Li Zhang, Shihe Wang, Rongjie Yi, Mengwei Xu"
creator: "LaTeX with hyperref"
pages: 19
---

# DroidCall: A Dataset for LLM-powered Android Intent Invocation

> **作者**：Weikai Xie, Li Zhang, Shihe Wang, Rongjie Yi, Mengwei Xu
> **總頁數**：19 頁

---

## Page 1

DroidCall : A Dataset for LLM-powered Android Intent Invocation

Weikai Xie 1 Li Zhang 1 Shihe Wang 1 Rongjie Yi 1 Mengwei Xu 1

Abstract

The growing capabilities of large language mod-

els in natural language understanding signifi-

cantly strengthen existing agentic systems. To

power performant on-device mobile agents for

better data privacy, we introduce DroidCall ,

the first training and testing dataset for accurate

Android intent invocation. With a highly flexible

and reusable data generation pipeline, we con-

structed 10k samples in DroidCall . Given a

task instruction in natural language, small lan-

guage models such as Qwen2.5-3B and Gemma2-

2B fine-tuned with DroidCall can approach

or even surpass the capabilities of GPT-4o for

accurate Android intent invocation. We also

provide an end-to-end Android app equipped

with these fine-tuned models to demonstrate the

Android intent invocation process. The code

and dataset are available at https://github.

com/UbiquitousLearning/DroidCall .

natural language processing, enabling machines to under-

stand and generate human-like language with unprecedented

accuracy. In the realm of mobile computing, this advance-

ment presents a significant opportunity for developing intel-

ligent mobile agents (Li et al., 2024; Zhang et al., 2024b;

Wen et al., 2024; Wang et al., 2023a). Specifically, these

arXiv:2412.00402v1 [cs.AI] 30 Nov 2024 agents can leverage the rich ecosystem of built-in intents

(int, 2024) provided by both the operating system and third-

party applications on Android devices. These intents serve

as a fundamental mechanism for inter-app communication

and function invocation, such as sending messages, making

phone calls, or triggering specific app features. By harness-

ing LLMs, mobile agents can interpret diverse and complex

On-device LLMs are necessary for building mobile agents

have the capability to assist users in completing common tasks

due to privacy and latency constraints (goo, 2024; Lu et al.,

2024b; Yin et al., 2024; Xu et al., 2023b; Yuan et al., 2024).

Since user data are processed locally, sensitive informa-

tion remains on devices, thereby mitigating risks associated

with data transmission over networks. Moreover, on-device

inference eliminates the need for constant internet connec-

tivity. Various on-device LLM inference optimizations sig-

nificantly reduce response time (Xu et al., 2024b; Yi et al.,

2023a; Xu et al., 2024a), leading to a more responsive and

fluid user experience.

et al., 2024) only succeeds in 31.5% and 60.5% of the tasks

in zero-shot and few-shot scenarios, respectively. This limi-

| 1. Introduction | Figure 1. | Small language models fine-tuned with | DroidCall |
| --- | --- | --- | --- |
| The advent of large language models (LLMs) revolutionizes | such as adding events to the calendar. |  |  |
| user instructions, seamlessly mapping them to the appropri- | However, our investigations reveal a critical challenge: Ex- |  |  |
| ate intents, and therefore automating user interaction with | isting device-affordable LLMs lack the capability of accu- |  |  |
| mobile devices. | rate intent invocation. For example, Llama3.2-1B (Dubey |  |  |
| 1 | Beijing University of Posts and Telecommunications (BUPT), | tation is not due to inherent deficiencies in the models them- |  |
| China. Correspondence to: Mengwei Xu <mwx@bupt.edu.cn>. | selves but stems from the absence of specialized datasets tai- |  |  |

---

## Page 2

DroidCall : A Dataset for LLM-powered Android Intent Invocation

| lored for this purpose. Existing LLMs are typically trained | into the era LLMs, which have begun to enter the public eye |
| --- | --- |
| on broad datasets that do not encompass the specific lan- | and develop rapidly. Subsequently, numerous open-source |
| guage patterns and contextual nuances required for accurate | LLMs (Yang et al., 2024; Team, 2024; Bai et al., 2023; |
| intent invocation. | Dubey et al., 2024; Liu et al., 2024a; Zhu et al., 2024; GLM |

To address this gap, we introduce DroidCall , the first

open-sourced, high-quality dataset designed for fine-tuning

LLMs for accurate intent invocation on Android devices.

DroidCall comprises an extensive collection of user in-

structions paired with their corresponding intents, cover-

ing a wide array of functionalities across the system and

third-party apps. We predefined functions encapsulating the

process of intent invocation, aiming for the model to learn

Evaluation. Based on DroidCall , we fine-tuned a few

small language models (SLMs), including PhoneLM-1.5B

(Yi et al., 2024), Qwen2.5-1.5B-Instruct, Qwen2.5-3B-

Instruct, Qwen2.5-Coder-1.5B (Team, 2024), Gemma2-2B-

it (Team et al., 2024), Phi-3.5-mini-instruct (Abdin et al.,

2024), MiniCPM3-4B (Hu et al., 2024), Llama3.2-1B-

End-to-end demo and open-source. We also provide an

end-to-end Android demonstration with the fine-tuned mod-

els based on mllm (Yi et al., 2023b), a fast and lightweight

LLMs have emerged as a significant advancement in the

field of artificial intelligence, marking a new era in natu-

ral language processing and understanding. Among them,

OpenAI’s GPT series (Achiam et al., 2023) has ushered AI

et al., 2024) have emerged, gradually approaching and even

rivaling the capabilities of GPT-4, which has empowered

developers and researchers alike to harness the power of

these advanced models to implement a variety of applica-

tions. Furthermore, models such as GPT-4V have endowed

LLMs with visual capabilities (Yang et al., 2023b; Lu et al.,

2024a; Wang et al., 2024c; Liu et al., 2024b), enabling them

to undertake a broader and more complex array of tasks.

methods, a variety of agents such as AutoGPT (Yang et al.,

2023a), MetaGPT (Hong et al., 2023) and HuggingGPT

(Shen et al., 2024b) which can serve as assistants to humans

have emerged.

2.2. Mobile Device Control Agents

gent (Yang et al., 2023c) and Mobile Agent (Wang et al.,

2024b;a) integrate visual capabilities to implement agents

on mobile devices.

Our work addresses these issues by deploying SLMs on

avoids the aforementioned problems. (2) Existing agents

devices, such as through tap and swipe gestures. In this

study, we envision agents directly interfacing with mobile

devices through intent invocation as a more efficient and

accurate approach to replace potentially tedious and error-

| their invocation for acquiring intent invocation capabilities. | By employing some prompting techniques, such as React |  |  |  |
| --- | --- | --- | --- | --- |
| With predefined functions, this pipeline automatically gen- | (Yao et al., 2022), Plan and Solve (Wang et al., 2023b), |  |  |  |
| erates data followed by format validation and deduplication | ReWOO (Xu et al., 2023a), it is possible to guide LLMs |  |  |  |
| to ensure accuracy, relevance, and diversity. Unlike other | in planning for specific tasks. | These approaches enable |  |  |
| similar methods (Wang et al., 2022; Taori et al., 2023; Qin | the models to use tools and interact with the external envi- |  |  |  |
| et al., 2023), our pipeline does not require manual writing | ronment, thus enhancing their capabilities to perform more |  |  |  |
| of seed data, thus saving a significant amount of labor. | intricate tasks. Based on LLMs and innovative prompting |  |  |  |
| Instruct, Llama3.2-3B-Instruct (Dubey et al., 2024). We | Significant efforts have been made in controlling mobile |  |  |  |
| demonstrate that by fine-tuning models on | DroidCall | , | devices using agents. Early work (Venkatesh et al., 2022; |  |
| the Android Intent invocation capabilities of these SLMs | Wang et al., 2023a; Wen et al., 2024) design UI representa- |  |  |  |
| can be effectively unleashed. Some models can even achieve | tions to bridge the gap between GUIs and natural language, |  |  |  |
| higher accuracy than GPT-4o using simpler prompts. While | enabling models to understand mobile screens. Later, with |  |  |  |
| prompts for GPT-4o contain an average of 1,367 tokens, | the advent of multimodal LLMs, agents become capable |  |  |  |
| models after fine-tuning, achieve this with an average of just | not only of processing textual inputs but also of receiving |  |  |  |
| 645 tokens. The accuracy of using Gemma2-2B improves | images, audio, or video as inputs. This enhancement allows |  |  |  |
| from 59% to 85% after fine-tuned on | DroidCall | , while | them to perceive the external environment more effectively |  |
| GPT-4o only achieves an accuracy of 77%. | and accomplish more complex tasks. Work such as AppA- |  |  |  |
| multimodal LLM inference engine, which demonstrates the | However, most existing agents have certain limitations. (1) |  |  |  |
| feasibility of our work. The demo is illustrated in Figure 1, | Most of them utilize cloud-side LLMs such as GPT-4. Ap- |  |  |  |
| which can assist users in completing common operations | plications on edge devices prioritize user privacy protection, |  |  |  |
| such as composing emails, setting alarms, making phone | and implementing edge agents through invoking cloud-side |  |  |  |
| calls, and so on. | DroidCall | is available at | https:// | LLMs cannot effectively safeguard user privacy. Addition- |
| github.com/UbiquitousLearning/DroidCall | ally, agents cannot be used under poor network conditions. |  |  |  |
| 2. Related Work | edge devices to control Android devices, which effectively |  |  |  |
| 2.1. LLM-based Agents | heavily rely on simulating human actions to operate mobile |  |  |  |

---

## Page 3

DroidCall : A Dataset for LLM-powered Android Intent Invocation

Figure 2. Workflow of DroidCall , which consist of three key phases:(1) Functions Predefinition; (2) Data Generation; (3) Finetuning

and Evaluation.

LLMs possess a certain level of reasoning capability, which

enables them to make function calls when needed. Tool-

area; it attempts to teach LLMs to use tools during interac-

tions with users. This work demonstrates the feasibility of

LLMs performing function calls and provided a framework

for subsequent research and development. To equip models

with the capability of function calling, a substantial amount

of data is often required. Self-Instruct (Wang et al., 2022)

proves that it is possible to use LLMs like GPT to generate

a significant volume of data for fine-tuning. Following the

self-instruct paradigm, numerous efforts (Qin et al., 2023;

Tang et al., 2023; Patil et al., 2023; Kim et al., 2023) have

been made to generate vast amount of function calling data

for the purpose of fine-tuning models. This kind of approach

makes it possible to equip models with function-calling ca-

pabilities by fine-tuning open-source models. Some work

like APIGen (Liu et al., 2024d), ShortcutsBench (Shen et al.,

2024a) and ToolACE (Liu et al., 2024c) focus on dataset

construction. To effectively utilize diverse data sources,

adjustments to the model architecture (by expanding the

or model fine-tuning.

In this section, we introduce the overall workflow of

DroidCall , which comprises three key phases as shown

in Figure 2: Function Predefinition, Data generation, Fine-

tuning and Evaluation. In § 3.1, we first introduce Android

intent, a key mechanism of Android. Based on the common

intents in Android, we manually predefine 24 functions that

can assist users in performing some common operations

on Android. In § 3.2, we detail our method for generating

the DroidCall dataset, the first open-sourced dataset for

Android intent invocation. Our method requires minimal

human supervision and can be easily extended. In § 3.3, we

describe how we fine-tune LLMs and evaluate their perfor-

mance. § 3.4 shows an end-to-end demonstration of device

control using fine-tuned LLMs with DroidCall .

3.1. Collecting Android Intents

| prone UI actions. Taking the task | “setting of an alarm” | as | work that generate general function calling data, we focus |
| --- | --- | --- | --- |
| an example, an agent could directly tell the app the user’s | on generating function-calling data related to Android in- |  |  |
| intent to set an alarm, rather than acting on behalf of the user | tent invocation, which makes it possible to achieve a better |  |  |
| to locate and enter the alarm app, tap to set the alarm, adjust | performance on edge than GPT-4o. We also provide a set of |  |  |
| the time, and then confirm. The latter approach complicates | simple and easy-to-use methods for fine-tuning and evalua- |  |  |
| the agent and reduces efficiency. Therefore, our work ab- | tion. TinyAgent (Erdogan et al., 2024) and Octopus (Chen |  |  |
| stracts intent invocation as function calling and implements | & Li, 2024) are similar to our work; they both implement |  |  |
| operations on Android through function calling, rather than | function-calling agents on mobile devices. However, TinyA- |  |  |
| through UI interactions. | gent focuses on operations on Mac, while Octopus requires |  |  |
| 2.3. LLMs for Function Calling | vocabulary). None of them provide code for data generation |  |  |
| former (Schick et al., 2024) is a pioneering work in this | 3. | DroidCall | Dataset and Workflow |
| AgentOhana (Zhang et al., 2024a) standardizes the data | In Android development, an intent is a fundamental mes- |  |  |
| format and designs a training pipeline for effective agent | saging object used to request an action from another app |  |  |
| learning. In our work, we construct a reusable and highly | component. Despite its simplicity, the intent system plays |  |  |
| customizable data generation pipeline. Unlike some other | a crucial role in facilitating communication between com- |  |  |

---

## Page 4

DroidCall : A Dataset for LLM-powered Android Intent Invocation

(a) Implicit intent (imp, 2024) (b) Set alarm

Figure 3. (a) shows how implicit intent works in Android; (b) shows an example to help user set an alarm with implicit intent.

| ponents in an Android application. It acts as a glue that | including but not limited to alarm configuration, email com- |
| --- | --- |
| connects individual components such as activities, services, | position, web searching. |

broadcast receivers, and content providers. Android intent

can be divided into two categories:

• Explicit Intents specify the exact component to start

by providing the fully qualified class name. This type

is typically used for internal communication within the

app. One can start an activity in response to a user

action or start a service to do some background work.

stead, they declare a general action to perform as shown

in Figure 3(a), which allows any app component that

can handle this action to respond. This makes implicit

intents especially useful for interacting with compo-

nents from different applications. For instance, if an

app needs to capture a photo, it can issue an implicit

intent to utilize the camera application installed on the

device.

The primary motivation to build DroidCall is to enable

models to perform function calling on Android devices for

common operations, thereby enhancing user assistance ca-

pabilities. Android intent, as its name suggests, serves as

mon mobile operations, as they effectively articulate user

intentions while maximizing the utilization of system re-

sources to meet user requirements. Figure 3(b) shows an

example of setting an alarm using implicit intent.

To construct the DroidCall dataset, we review the

frequently-used intents. These intents will be encapsu-

lated into a set of functions that serve as the foundation

for the DroidCall dataset generation. These functions

3.2. Dataset Generation

In this section, we present a detailed description of the

DroidCall dataset generation process. We first introduce

the key components utilized in data generation: the sampler ,

collector , LLM and filter components. Subsequently, we

elaborate on the critical phases of data generation: function

predefinition, seed data generation, and data generation. The

workflow of data generation.

Subsequently, the data is used as seed data to continuously gener-

ate new data, thereby eliminating the need for laborious manual

work. All the generated data will go through a set of customized

filters to ensure the correctness of data formats and the diversity of

the data.

Sampler , LLM , Filter , and Collector are essential compo-

nents of the data generation pipeline.

| • | Implicit Intents. | Unlike explicit intents, implicit in- | entire dataset generation process leverages GPT-4-turbo as |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tents do not directly specify the target component. In- | the underlying language model. Figure 4 shows an overall |  |  |  |  |  |  |  |
| a mechanism to express user “intentions” and trigger cor- | Figure 4. | Details of data generation in | DroidCall | . | To avoid |  |  |  |
| responding activities to fulfill these intentions. We identify | manually creating seed data, | DroidCall | initially samples ex- |  |  |  |  |  |
| implicit intents as the optimal choice for implementing com- | amples from an external dataset to generate its first set of data. |  |  |  |  |  |  |  |
| Android official documentation (com, 2024) and select | 3.2.1. K | EY | C | OMPONENTS OF | G | ENERATION | P | IPELINE |
| encompass a broad range of common Android operations, | Sampler. | A sampler is the component capable of taking |  |  |  |  |  |  |

---

## Page 5

DroidCall : A Dataset for LLM-powered Android Intent Invocation

| multiple data sources as input (such as lists, jsonl files, etc.), | particular, these functions can perform common operations |
| --- | --- |
| sampling the required data from each data source according | on Android, which include: |

to a specific sampling strategy, and organizing the sampled

LLM . LLM serves as the engine for data generation. We

employ the self-instruct (Wang et al., 2022) paradigm for

data generation, which involves integrating data sampled by

capabilities directly impact the quality of the generated data.

generation.

Filter. A filter is used to process the output from the LLM

after it has been generated, such as extracting structured

data from the output of LLMs, discarding data that does not

meet the required format, and eliminating data that is highly

similar to existing data. In the framework, the LLM can

be processed by a series of custom filters, offering a high

degree of flexibility.

Collector. A collector is the component designed to co-

ordinate and utilize the aforementioned three components,

acting as the manager of the entire data generation pipeline.

After obtaining data from the sampler, the collector inte-

grates the data into specified prompt templates, generates

raw data through the LLM, processes the data generated by

results obtained.

3.2.2. F UNCTIONS P REDEFINITION

The automated extraction of intents from the Android Open

Source Project (AOSP) (AOS, 2024) source code is a com-

plex endeavor due to the multitude of intents and the dy-

namic nature of the Android platform. Given the complex-

methodology diverges from such approaches.

We have predefined 24 functions that cover common opera-

tions on Android and utilize common intents within these

as an interface between the LLM and the intents, conceal-

• Contact Management : Add contacts, make phone

calls.

emails.

In our framework, the method for predefining functions is

the same as that for defining ordinary Python functions. We

only need to write out the function signatures and provide

the Google-style docstrings (Goo, 2024) for the function.

Subsequently, we can automatically extract structured infor-

mation describing the function from the function signature

and the docstring. The extracted data have the format shown

in Listing 1.

{

"name": "func1",

"description": "This function is ...",

"arguments": {

"arg1": {

"description": "This arg is...",

"type": "<type>",

"default": "<default_value>"

},

"arg2": ...

},

"returns": {

"type": "...",

"description": "..."

},

"example": [...]

}

are optional.

3.2.3. D ATA GENERATION

seed data, we automatically generate a series of seed data

| data into a particular format as intended by the user for | • | Scheduling Assistant | : Help users to set an alarm/timer, |  |
| --- | --- | --- | --- | --- |
| output. | insert an event on calendar. |  |  |  |
| the sampler into specific prompt templates and then handing | • | Common Operations | : | Internet search, search on |
| it over to the LLM for data generation. | Therefore, the | maps, open camera for taking photos or recording |  |  |
| LLM is the core component of data generation, and its | videos, open various settings. |  |  |  |
| In this paper, GPT-4-turbo is utilized as the LLM for data | • | Messaging Services | : | Compose text messages or |
| the LLM with a series of filters, and ultimately collects the | "required": | "true | or | false", |
| ities involved in the automated extraction of intents, our | Listing 1. | Extracted function. “returns” field and “example” field |  |  |
| functions for their specific implementations. Subsequently, | We follow the self-instruct paradigm (Wang et al., 2022; |  |  |  |
| we will teach the LLM to operate Android by learning to use | Taori et al., 2023) to build our data generation pipeline. We |  |  |  |
| these predefined functions. These predefined functions act | have two stages to generate data. |  |  |  |
| ing the specific details of the intents from the LLM. This | Seed Generation Stage. | When leveraging LLMs for syn- |  |  |
| approach also circumvents the issue of different versions of | thetic data generation, incorporating high-quality examples |  |  |  |
| Android causing the LLM’s learned intent knowledge to be- | in the prompt is crucial. This guidance helps maintain the |  |  |  |
| come obsolete. Once the LLM has learned these functions, | data’s quality and aligns it closely with human standards. |  |  |  |
| we only need to implement them on different versions of | These examples are called seed. It is often the case that |  |  |  |
| Android, and the LLM will be able to do the intents invoca- | these seeds are manually written and verified, which can be |  |  |  |
| tion on different versions of Android through the functions | very labor-intensive and time-consuming. To avoid the time- |  |  |  |
| without needing to know the specifics of the intents. | In | consuming and labor-intensive task of manually writing |  |  |

---

## Page 6

DroidCall : A Dataset for LLM-powered Android Intent Invocation

| for the function before formally generating data. The spe- | requiring the use of a single function for one call. In |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| cific method is to use existing function-calling datasets as | this case, the sampler just sample a single predefined |  |  |  |  |  |
| examples to guide the LLM in generating seed data. Specif- | function for LLM to generate data. |  |  |  |  |  |
| ically, we sample data from xlam-function-calling-60k (Liu | { |  |  |  |  |  |
| et al., 2024d) and prompt the LLM to generate user queries | "query": | "Wake | me | up | at | 8:30", |

and calling examples for our predefined functions based on

the given instances. The data generated from this process

will serve as seed data for subsequent data generation stages.

employ the self-instruct paradigm for data generation. For

a predefined function, denoted as func , we have previously

generated a series of data for func in the seed generation

stage. In this stage, we will extract several instances from

it to produce more user queries and func calling examples.

The format of generated data is shown in Listing 4.

"answers": [

"name": "func_name",

...

},

...

]

Listing 2. An example of generated data

Regardless of the stage, the output from the LLM will be

following three filters were utilized in sequence.

JsonExtractor. This filter is designed to extract JSON data

from the output of LLM. It has been observed that GPT4-

for output. To properly handle the output of LLM, this

filter employs a syntax parser to extract JSON data from the

output of LLM.

those not in the proper format.

against the existing data. When the F-measure value exceeds

75%, the data is filtered out.

In our experiment, we generate two types of function-calling

"answers": [

{

"id": 0,

"name": "ACTION_SET_ALARM",

"arguments": {

"EXTRA_HOUR": 8,

}

}

]

}

invocation of ACTION_SET_ALARM can fulfill the

user’s requirement.

calls.

{

456",

"answers": [

{

"id": 0,

"name": "ACTION_SET_TIMER",

"arguments": {

}

},

{

"id": 1,

"name": "dial",

"arguments": {

}

}

]

}

pendix A.

3.3. Fine-tuning SLMs with DroidCall

DroidCall dataset, including PhoneLM-1.5B (Yi et al.,

| Data Generation Stage. | During this stage, we directly | "EXTRA_MINUTE": | 30 |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| these seed data to serve as examples for the LLM, enabling | Listing 3. | An example of simple call in which a simple |  |  |  |  |  |  |  |
| { | • | Complex. | The user’s query is intricate and cannot |  |  |  |  |  |  |
| "query": | "user | query | here", | be resolved with a single function call. | Instead, it |  |  |  |  |
| { | requires the combination of two or more functions to |  |  |  |  |  |  |  |  |
| "id": | id, | address the complexity of the request. In the process of |  |  |  |  |  |  |  |
| "arguments": | { | generating this type of data, the sampler samples two |  |  |  |  |  |  |  |
| "arg1": | "value1", | to three functions from the predefined set and prompts |  |  |  |  |  |  |  |
| } | the LLM to generate examples of complex function |  |  |  |  |  |  |  |  |
| } | "query": | "Set | a | timer | for | 30 | minutes | and | dial 123 |
| processed through several custom filters. In our setup, the | "duration": | "30 | minutes" |  |  |  |  |  |  |
| turbo does not always strictly adhere to a specific format | "phone_number": | "123456" |  |  |  |  |  |  |  |
| FormatFilter. | To ensure the extracted JSON strictly match | Listing 4. | An example of complex call in which we need to |  |  |  |  |  |  |
| the format in Listing 4, we use | FormatFilter | to filter out | call two functions to fulfill the user’s requirement. |  |  |  |  |  |  |
| SimilarityFilter. | This filter is designed to address the issue | Using the method described above, we generated the |  |  |  |  |  |  |  |
| of high data similarity and poor quality due to the LLM’s | DroidCall | dataset, which is made up of two parts: train |  |  |  |  |  |  |  |
| tendency to generate similar examples. It works by tracking | and test. | The train split contains 10,000 data entries, |  |  |  |  |  |  |  |
| the user queries that have been generated and calculating | while the test split contains 200 data entries. We provide |  |  |  |  |  |  |  |  |
| the LCS ROUGE score (Lin, 2004) for each new user query | all prompt templates used to create | DroidCall | in Ap- |  |  |  |  |  |  |
| data. | Models. | We fine-tuned a series of SLMs using the |  |  |  |  |  |  |  |
| • | Simple. | The user’s query is simple and straightforward, | 2024), Qwen2.5-1.5B, Qwen2.5-3B (Yang et al., 2024; |  |  |  |  |  |  |

---

## Page 7

DroidCall : A Dataset for LLM-powered Android Intent Invocation

| Team, 2024), Llama3.2-1B, Llama3.2-3B (Dubey et al., | model. It is worth noting that all of our model inference pro- |
| --- | --- |
| 2024), MiniCPM3-4B (Hu et al., 2024), Phi3.5-3.8B (Ab- | cesses are completed on mobile phones. We utilized mllm |
| din et al., 2024) and Gemma2-2B (Team et al., 2024). | (Yi et al., 2023b), a fast and lightweight multimodal LLM |

Modeling function-calling tasks. We regard function call-

ing as an instruction following task, where the model’s input

consists of user query , available function descriptions , and

task instructions . The output of the model is a specific

representation for calling a function .

If a unified input-output format is designed for fine-tuning

models from different vendors, there would be issues: dif-

ferent models use different formats instruction tuning. If

we use a unified format for fine-tuning, this format may

have a gap compared to the format used during the model’s

instruction tuning. This could potentially affect the model’s

performance when it comes to function calling. Most cur-

rent models have undergone fine-tuning specifically for chat,

which typically involve three roles: system, user, and as-

sistant. So we can reuse model’s own chat template to do

function calling. Specifically, we put user query and avail-

able function descriptions in system prompt and user prompt

and put the function calling result in assistant output. By

capability for function calling while avoiding a significant

gap between the data used for fine-tuning and the knowledge

Setups. We formatted the DroidCall dataset into the

chat format described above, resulting in 10K training sam-

ples. We then fine-tuned the model using LoRA (Hu et al.,

2022), with a LoRA rank of 8 and a LoRA alpha of 16.

Additionally, we employed a linear learning rate scheduler,

setting the learning rate to 1.41e-5 and the warmup ratio

to 0.1. We train for 24 epoch and pick the best checkpoint.

Details of prompt format are provided in Appendix B.

word embeddings for the function descriptions and stored

them in ObjectBox (obj, 2024), a vector database. When a

inference engine designed for mobile and edge devices, to

carry out the inference for both GTE and PhoneLM. Finally,

we have a demo that can help us completing common tasks

on Andrid devices.

which the fine-tuned model understands the user’s intent

and assists users in adding an event to the calendar.

4. Experiments

We first explored the impact of different prompt designs

on model fine-tuning. After considering both the length of

the prompts and the model’s performance after fine-tuning,

we selected an appropriate format for our prompts. Sub-

sequently, through experimentation, we demonstrated that

| adopting this approach, we can equip the model with the | Figure 5. | Design of our demo. |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| the model has already acquired. | Figure 1 illustrates an example of the end-to-end demo, in |  |  |  |  |  |
| 3.4. Putting It All Together | using the | DroidCall | dataset is more effective than using |  |  |  |
| Using the | DroidCall | dataset, we equip SLMs with cer- | a general function calling dataset in scenarios aimed at An- |  |  |  |
| tain capabilities for Android intent invocation. To verify its | droid intent invocation. Finally, we presented a series of |  |  |  |  |  |
| effectiveness, we developed an Android application. The | results showcasing the effectiveness of models fine-tuned |  |  |  |  |  |
| design of our demo is shown in Figure 5. This demo consists | with the | DroidCall | dataset. |  |  |  |
| of two important components. One is the retriever, which is | Metrics. | To quantitatively assess the efficacy of function |  |  |  |  |
| used to retrieve the most relevant functions. To implement | calling within our model, we introduce two distinct metrics: |  |  |  |  |  |
| this retriever, we utilized GTE (Li et al., 2023) to create | Accuracy | and | Soft Accuracy | . |  |  |
| user query arrives, we employ GTE for word embedding and | • | Accuracy. | This metric evaluates the model’s ability |  |  |  |
| retrieve the most relevant functions from ObjectBox, thus | to precisely replicate the ground-truth function calls |  |  |  |  |  |
| we have a simple and effective retriever. Another important | associated with a user query. A sample is deemed cor- |  |  |  |  |  |
| component is a model capable of intent invocation, which | rect if and only if the model’s output perfectly matches |  |  |  |  |  |
| takes in the user’s query along with the functions retrieved | the ground truth in terms of both function identity and |  |  |  |  |  |
| by the retriever and outputs the function calls that can fulfill | parameter values. Mathematically, Accuracy ( | Acc | ) is |  |  |  |
| the user query. In our demo, we used PhoneLM-1.5B (Yi | formalized as the ratio of the number of perfectly pre- |  |  |  |  |  |
| et al., 2024) fine-tuned on the | DroidCall | dataset as this | dicted samples ( | N | perfect | ) to the total number of samples |

---

## Page 8

DroidCall : A Dataset for LLM-powered Android Intent Invocation

( N total ): specific representation for calling a function . We opt for

N perfect JSON formatting due to its simplicity.

Acc =

N total

scores across all function calls:

X F

correct ,i

F P

i =1 total ,i

It is important to note that the parameters of some functions

are not straightforward to compare directly for correctness,

such as parameters like title or subject . Semantic consis-

tency is sufficient for these parameters; they do not need to

match exactly to be considered correct. For such parameters,

We use the 200 data entries from the test split of

DroidCall to evaluate SLMs. It is worth noting that

in real-world applications, we need to use a retriever to re-

trieve the functions that are likely to be used. But in our

work, we are not focused on the retriever. So when testing

the Acc and Acc sof t , we use a fake retriever that always

retrieves the ground-truth functions.

4.1. Effect of Different Prompts

| Prompt | Average Number of Tokens |
| --- | --- |
| code_short | 645.195 |
| json_short | 950.340 |
| code | 931.555 |

tions , and task instructions . The model output is a specific

representation for calling a function . The user query is

use JSON data as available function descriptions and a

code Another approach is to leverage the prevalence of code

short In the above two formats, we provided a detailed

cantly increases the length of the prompt. We posit that for

be essential. Through the fine-tuning process, models can

learn to perform the function calling task without the need

for explicit task instructions in the prompt. Consequently,

we experimented with removing the task instructions from

the previous formats, which we denote as json_short and

code_short .

sults shown in Figure 6(a). As can be observed from the

figure, the final outcome indicates that the json format per-

formed slightly better. However, the upward trend among

all four formats is consistent, and the code_short format is

essentially on par with the code and json formats. Addition-

ally, we tested the average of input tokens for the model

under four different prompt formats on the DroidCall

test dataset, as shown in Table 1. The code_short format

has a significantly smaller number of tokens compared to

the other prompts. After comprehensive consideration, we

ultimately chose the code_short format for subsequent fine-

tuning experiments.

4.2. Effectiveness of DroidCall

results in the task of controlling Android phones through

the Qwen2.5-1.5B-Instruct and PhoneLM-1.5B models after

dataset.

calling-60k dataset comprises 60k data points, while

| • | Soft Accuracy. | This metric offers a nuanced evalua- | data in large language models’ pre-training. We hypothe- |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| tion of the model’s performance, especially when it | size that using | docstrings | as | available function descriptions |  |  |
| produces function calls that are partially correct. For | and adopting a | Python function call | format for the | specific |  |  |
| each function call, a score is assigned based on the | representation for calling a function | may yield superior |  |  |  |  |
| proportion of accurately predicted parameters ( | P | correct | ) | results. This is because such data closely resembles the cod- |  |  |
| relative to the total number of parameters ( | P | total | ). Soft | ing examples encountered during pre-training, potentially |  |  |
| Accuracy ( | A | soft | ) is then computed as the mean of these | enhancing the model’s comprehension and performance. |  |  |
| 1 | P | description of the tasks the model is required to complete |  |  |  |  |
| Acc | soft | = | as the | task instructions | . | However, this approach signifi- |
| where | F | denotes the total number of function calls. | models undergoing fine-tuning, | task instructions | may not |  |
| we employ models from the RoBERTa (Liu et al., 2019) se- | We experimented with fine-tuning the Qwen2.5-1.5B- |  |  |  |  |  |
| ries to compare semantic similarity. If the similarity exceeds | Instruct model using four different types of prompts men- |  |  |  |  |  |
| a set threshold, it is considered correct. We set the threshold | tioned above. We selected nine checkpoints throughout the |  |  |  |  |  |
| to 0.75. | entire fine-tuning process to test for accuracy, with the re- |  |  |  |  |  |
| json | 1367.905 | To verify that the | DroidCall | dataset can achieve better |  |  |
| Table 1. | Average number of tokens of different prompts. | Android Intent invocation, we compared the performance of |  |  |  |  |
| In | § | 3.3, we mentioned that the model input includes several | fine-tuning on the | DroidCall | dataset and xlam-function- |  |
| key components: | user query | , | available function descrip- | calling-60k (Liu et al., 2024d), a general function calling |  |  |
| provided by the user and is beyond our control. However, | To eliminate the influence of prompt design, we format- |  |  |  |  |  |
| we can design the remaining three parts and observe how | ted both the xlam-function-calling-60k and | DroidCall |  |  |  |  |
| models perform after fine-tuning using different designs. | datasets using the | code_short | format. The xlam-function- |  |  |  |
| json | A minimalist and straightforward design is to directly | DroidCall | contains 10k. To ensure an equivalent number |  |  |  |

---

## Page 9

DroidCall : A Dataset for LLM-powered Android Intent Invocation

(a) Accuracy of Qwen2.5-1.5B-Instruct on different prompts (b) Different models fine-tuned on different datasets

Figure 6. Figure 6(a) illustrates the performance of Qwen2.5-1.5B-Instruct after fine-tuning under different prompt formats. Figure 6(b)

shows the performance of PhoneLM-1.5B and Qwen2.5-1.5B-Instruct after finetuning on different datasets.

Model Size

Acc

| PhoneLM-1.5B | 1.5B | 17.5 |
| --- | --- | --- |
| Qwen2.5-1.5B-Instruct | 1.5B | 61 |
| Qwen2.5-3B-Instruct | 3B | 62 |
| Qwen2.5-Coder-1.5B | 1.5B | 42.5 |
| Gemma2-2B-it | 2B | 59 |
| Phi-3.5-mini-instruct | 3.8B | 62 |
| MiniCPM3-4B | 4B | 67 |
| Llama3.2-1B-Instruct | 1B | 31.5 |
| Llama3.2-3B-Instruct | 3B | 66.5 |
| GPT-4o | 77 |  |
| GPT-4o-mini | 71.5 |  |

Table 2.

From the experimental results, we can observe that, re-

gardless of the dataset used, accuracy improves with the

fine-tuning process. However, the model fine-tuned with

the xlam-function-calling-60k dataset quickly reaches a

plateau. In contrast, the improvement brought by using

the DroidCall dataset is significantly more substantial.

It is evident that when a model is required to perform a

specific task, a dataset constructed for that task, such as

DroidCall , can yield better results compared to a general-

| Zero-Shot | Few-Shot | Fine-Tuning |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Acc | sof t | Acc | Acc | sof t | Acc | Acc | sof t |
| 17.5 | 55.5 | 62.8 | 75 | 86.1 |  |  |  |
| 76.6 | 64.5 | 81 | 76 | 90.3 |  |  |  |
| 79.4 | 71 | 86.1 | 83 | 93.5 |  |  |  |
| 48.8 | 65.5 | 81.6 | 82 | 93.2 |  |  |  |
| 77.2 | 67.5 | 83.7 | 85 | 93.9 |  |  |  |
| 77.8 | 67.5 | 82.1 | 83.5 | 93.8 |  |  |  |
| 84.3 | 75 | 89.6 | 74.5 | 82.3 |  |  |  |
| 37.7 | 60.5 | 76.3 | 75.5 | 87.3 |  |  |  |
| 79.8 | 72 | 87.2 | 82 | 92.7 |  |  |  |
| 89.1 | 80.5 | 91.5 |  |  |  |  |  |
| 86.6 | 76 | 88.6 |  |  |  |  |  |

Evaluation of different models

edge efficiently. The DroidCall dataset, however, aids

the model in learning to utilize its pre-trained knowledge to

control Android devices. Since the pre-trained knowledge

of both PhoneLM and Qwen is comparable, they eventually

reach a similar level of performance.

4.3. Performance of Different SLMs

To test the Android intent invocation capabilities of some

existing SLMs tailored for the edge scenario and further ver-

ify the effectiveness of DroidCall , we tested the Acc and

| of training data instances, we trained the model for 4 epochs | purpose dataset. Furthermore, from Figure 6(b), we can |  |  |
| --- | --- | --- | --- |
| on the xlam-function-calling-60k dataset and for 24 epochs | discern that initially, Qwen’s capabilities are significantly |  |  |
| on | DroidCall | . We selected 9 checkpoints for testing, and | higher than PhoneLM’s. However, by the end of the fine- |
| the results are presented in Figure 6(b). Note that the 0th | tuning process, PhoneLM’s performance is on par with |  |  |
| checkpoint in the figure represents the model’s performance | Qwen’s. We speculate that initially, PhoneLM’s Supervised |  |  |
| when directly evaluated with the | code | format of prompts | Fine-Tuning (SFT) and alignment were not as effective as |
| before any fine-tuning took place. | Qwen’s, preventing it from leveraging its pre-trained knowl- |  |  |

---

## Page 10

DroidCall : A Dataset for LLM-powered Android Intent Invocation

Acc sof t of a few models under three conditions: zero-shot, github.io/styleguide/pyguide.html#

few-shot, and after fine-tuning. When testing the models’ 381-docstrings , 2024.

zero-shot and few-shot performance, we used json format

ing the task. In comparison, the json format has been found

to be more effective than the code format.

a comprehensive overview of the Android intent invoca-

tion capabilities across various models. Judging from the

zero-shot results, there is a significant performance variation

among different models. The zero-shot scenario is a critical

test of a model’s ability to complete tasks based on instruc-

tions without having seen relevant examples. We believe

the primary reason for the differences in zero-shot perfor-

ities. It is also observable that all models exhibit improved

After fine-tuning with DroidCall , there is a significant

improvement in the model’s performance. Additionally,

compared to the zero-shot and few-shot scenarios.

5. Conclusion

specifically engineered to enhance the Android intent invo-

cation capabilities of LLMs. Our approach diverged from

conventional cloud-based models, focusing instead on on-

struct DroidCall , a first-of-its-kind open-sourced dataset

for Android intent invocation based on the pipeline, (3) fine-

potential applications of small models on the edge. We have

open-sourced all the code of the data generation, fine-tuning,

and evaluation.

References

Aosp. https://source.android.com/ , 2024.

2024.

Google ai edge sdk for gemini nano. https://

Android developer guides. https://developer.

android.com/guide/components/

intents-filters , 2024.

intent. https://developer.android.com/

reference/android/content/Intent , 2024.

language model locally on your phone. arXiv preprint

arXiv:2404.14219 , 2024.

arXiv:2303.08774 , 2023.

Bai, J., Bai, S., Chu, Y., Cui, Z., Dang, K., Deng, X., Fan,

Y., Ge, W., Han, Y., Huang, F., et al. Qwen technical

Chen, W. and Li, Z. Octopus v2: On-device language model

for super agent. arXiv preprint arXiv:2404.01744 , 2024.

arXiv:2407.21783 , 2024.

GLM, T., Zeng, A., Xu, B., Wang, B., Zhang, C., Yin, D.,

Zhang, D., Rojas, D., Feng, G., Zhao, H., et al. Chatglm:

A family of large language models from glm-130b to

glm-4 all tools. arXiv preprint arXiv:2406.12793 , 2024.

Hong, S., Zheng, X., Chen, J., Cheng, Y., Wang, J., Zhang,

C., Wang, Z., Yau, S. K. S., Lin, Z., Zhou, L., et al.

Metagpt: Meta programming for multi-agent collabora-

| prompts for both, as the | json-short | and | code-short | formats | Common intents. | https://developer.android. |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lack | task instructions | , which prevents the model from finish- | com/guide/components/intents-common | , |  |  |  |
| The experimental outcomes, as depicted in Table 2, provide | developer.android.com/ai/aicore | , 2024. |  |  |  |  |  |
| mance among models lies in the effectiveness of their SFT | Objectbox: | Fast | and | efficient | database | with | vec- |
| and alignment. These training stages determine whether | tor search. | https://github.com/objectbox/ |  |  |  |  |  |
| the model can develop strong instruction-following capabil- | objectbox-java | , 2024. |  |  |  |  |  |
| performance under few shots. We credit the performance | Abdin, M., Jacobs, S. A., Awan, A. A., Aneja, J., Awadallah, |  |  |  |  |  |  |
| boost to the models’ improved use of their knowledge from | A., Awadalla, H., Bach, N., Bahree, A., Bakhtiari, A., |  |  |  |  |  |  |
| pretraining. | Behl, H., et al. Phi-3 technical report: A highly capable |  |  |  |  |  |  |
| during inference, the model only requires a prompt that | Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., |  |  |  |  |  |  |
| essentially consists of the | user query | and | available func- | Aleman, F. L., Almeida, D., Altenschmidt, J., Altman, S., |  |  |  |
| tion descriptions | , which greatly reduces the prompt length | Anadkat, S., et al. Gpt-4 technical report. | arXiv preprint |  |  |  |  |
| In this paper, we introduce | DroidCall | , a novel dataset | report. | arXiv preprint arXiv:2309.16609 | , 2023. |  |  |
| device deployment to address privacy concerns inherent in | Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, |  |  |  |  |  |  |
| mobile environments. In our work, we (1) build a highly | A., Letman, A., Mathur, A., Schelten, A., Yang, A., Fan, |  |  |  |  |  |  |
| customizable and reusable data generation pipeline, (2) con- | A., et al. The llama 3 herd of models. | arXiv preprint |  |  |  |  |  |
| tune a series of models tailored for edge devices, enabling | Erdogan, L. E., Lee, N., Jha, S., Kim, S., Tabrizi, R., Moon, |  |  |  |  |  |  |
| them to approach or even surpass the performance of GPT- | S., Hooper, C., Anumanchipalli, G., Keutzer, K., and |  |  |  |  |  |  |
| 4o in the specific task of intent invocation, (4) implement | Gholami, A. | Tinyagent: Function calling at the edge. |  |  |  |  |  |
| an end-to-end demo with mllm. Our work demonstrates the | arXiv preprint arXiv:2409.00608 | , 2024. |  |  |  |  |  |
| Google-style | docstrings. | https://google. | tive framework. | arXiv preprint arXiv:2308.00352 | , 2023. |  |  |

---

## Page 11

DroidCall : A Dataset for LLM-powered Android Intent Invocation

| Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, | Lu, H., Liu, W., Zhang, B., Wang, B., Dong, K., Liu, B., |  |  |  |
| --- | --- | --- | --- | --- |
| S., Wang, L., and Chen, W. LoRA: Low-rank adaptation | Sun, J., Ren, T., Li, Z., Yang, H., et al. | Deepseek-vl: |  |  |
| of large language models. In | International Conference | towards real-world vision-language understanding. | arXiv |  |
| on Learning Representations | , 2022. URL | https:// | preprint arXiv:2403.05525 | , 2024a. |

openreview.net/forum?id=nZeVKeeFYf9 .

the potential of small language models with scalable train-

Kim, S., Moon, S., Tabrizi, R., Lee, N., Mahoney, M. W.,

Keutzer, K., and Gholami, A. An llm compiler for parallel

Insights and survey about the capability, efficiency and

2023.

Out , pp. 74–81, Barcelona, Spain, July 2004. Asso-

Liu, A., Feng, B., Wang, B., Wang, B., Liu, B., Zhao, C.,

Dengr, C., Ruan, C., Dai, D., Guo, D., et al. Deepseek-v2:

Liu, H., Li, C., Wu, Q., and Lee, Y. J. Visual instruction tun-

ning the points of llm function calling. arXiv preprint

arXiv:2409.00920 , 2024c.

A robustly optimized bert pretraining approach, 2019.

Liu, Z., Hoang, T., Zhang, J., Zhu, M., Lan, T., Kokane,

S., Tan, J., Yao, W., Liu, Z., Feng, Y., et al. Api-

arXiv:2406.18518 , 2024d.

Lu, Z., Li, X., Cai, D., Yi, R., Liu, F., Zhang, X., Lane, N. D.,

2024b.

Large language model connected with massive apis. arXiv

preprint arXiv:2305.15334 , 2023.

Cong, X., Tang, X., Qian, B., et al. Toolllm: Facilitating

M., Hambro, E., Zettlemoyer, L., Cancedda, N., and

Shen, H., Li, Y., Meng, D., Cai, D., Qi, S., Zhang, L.,

arXiv:2407.00132 , 2024a.

friends in hugging face. Advances in Neural Information

Processing Systems , 36, 2024b.

arXiv:2306.05301 , 2023.

Stanford alpaca: An instruction-following llama

Team, G., Riviere, M., Pathak, S., Sessa, P. G., Hardin, C.,

Bhupatiraju, S., Hussenot, L., Mesnard, T., Shahriari, B.,

2024.

ber 2024. URL https://qwenlm.github.io/

blog/qwen2.5/ .

arXiv:2211.07615 , 2022.

| Hu, S., Tu, Y., Han, X., He, C., Cui, G., Long, X., Zheng, Z., | and Xu, M. Small language models: Survey, measure- |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fang, Y., Huang, Y., Zhao, W., et al. Minicpm: Unveiling | ments, and insights. | arXiv preprint arXiv:2409.15790 | , |  |  |  |  |  |  |  |  |
| ing strategies. | arXiv preprint arXiv:2404.06395 | , 2024. | Patil, S. G., Zhang, T., Wang, X., and Gonzalez, J. E. Gorilla: |  |  |  |  |  |  |  |  |
| function calling. | arXiv preprint arXiv:2312.04511 | , 2023. | Qin, Y., Liang, S., Ye, Y., Zhu, K., Yan, L., Lu, Y., Lin, Y., |  |  |  |  |  |  |  |  |
| Li, Y., Wen, H., Wang, W., Li, X., Yuan, Y., Liu, G., Liu, | large language models to master 16000+ real-world apis. |  |  |  |  |  |  |  |  |  |  |
| J., Xu, W., Wang, X., Sun, Y., et al. Personal llm agents: | arXiv preprint arXiv:2307.16789 | , 2023. |  |  |  |  |  |  |  |  |  |
| security. | arXiv preprint arXiv:2401.05459 | , 2024. | Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, |  |  |  |  |  |  |  |  |
| Li, Z., Zhang, X., Zhang, Y., Long, D., Xie, P., and Zhang, | Scialom, T. | Toolformer: Language models can teach |  |  |  |  |  |  |  |  |  |
| M. Towards general text embeddings with multi-stage | themselves to use tools. | Advances in Neural Information |  |  |  |  |  |  |  |  |  |
| contrastive learning. | arXiv preprint arXiv:2308.03281 | , | Processing Systems | , 36, 2024. |  |  |  |  |  |  |  |
| Lin, C.-Y. | ROUGE: A package for automatic evalua- | Xu, M., and Ma, Y. Shortcutsbench: A large-scale real- |  |  |  |  |  |  |  |  |  |
| tion of summaries. | In | Text Summarization Branches | world benchmark for api-based agents. | arXiv preprint |  |  |  |  |  |  |  |
| ciation for Computational Linguistics. | URL | https: | Shen, Y., Song, K., Tan, X., Li, D., Lu, W., and Zhuang, |  |  |  |  |  |  |  |  |
| //aclanthology.org/W04-1013 | . | Y. | Hugginggpt: Solving ai tasks with chatgpt and its |  |  |  |  |  |  |  |  |
| A strong, economical, and efficient mixture-of-experts | Tang, Q., Deng, Z., Lin, H., Han, X., Liang, Q., Cao, B., |  |  |  |  |  |  |  |  |  |  |
| language model. | arXiv preprint arXiv:2405.04434 | , | and Sun, L. Toolalpaca: Generalized tool learning for lan- |  |  |  |  |  |  |  |  |
| 2024a. | guage models with 3000 simulated cases. | arXiv preprint |  |  |  |  |  |  |  |  |  |
| ing. | Advances in neural information processing systems | , | Taori, | R., | Gulrajani, | I., | Zhang, | T., | Dubois, | Y., | Li, |
| 36, 2024b. | X., | Guestrin, | C., | Liang, | P., | and Hashimoto, | T. B. |  |  |  |  |
| Liu, W., Huang, X., Zeng, X., Hao, X., Yu, S., Li, D., | model. | https://github.com/tatsu-lab/ |  |  |  |  |  |  |  |  |  |
| Wang, S., Gan, W., Liu, Z., Yu, Y., et al. Toolace: Win- | stanford_alpaca | , 2023. |  |  |  |  |  |  |  |  |  |
| Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., Levy, | Ramé, A., et al. Gemma 2: Improving open language |  |  |  |  |  |  |  |  |  |  |
| O., Lewis, M., Zettlemoyer, L., and Stoyanov, V. Roberta: | models at a practical size. | arXiv e-prints | , pp. arXiv–2408, |  |  |  |  |  |  |  |  |
| URL | https://arxiv.org/abs/1907.11692 | . | Team, Q. Qwen2.5: A party of foundation models, Septem- |  |  |  |  |  |  |  |  |
| gen: | Automated | pipeline | for | generating | verifiable | Venkatesh, S. G., Talukdar, P., and Narayanan, S. | Ugif: |  |  |  |  |
| and diverse function-calling datasets. | arXiv preprint | Ui grounded instruction following. | arXiv preprint |  |  |  |  |  |  |  |  |

---

## Page 12

DroidCall : A Dataset for LLM-powered Android Intent Invocation

| Wang, B., Li, G., and Li, Y. Enabling conversational in- | Yang, H., Yue, S., and He, Y. Auto-gpt for online decision |  |  |
| --- | --- | --- | --- |
| teraction with mobile ui using large language models. | making: Benchmarks and additional opinions. | arXiv |  |
| In | Proceedings of the 2023 CHI Conference on Human | preprint arXiv:2306.02224 | , 2023a. |

Factors in Computing Systems , pp. 1–17, 2023a.

Mobile device operation assistant with effective nav-

igation via multi-agent collaboration. arXiv preprint

arXiv:2406.01014 , 2024a.

Huang, F., and Sang, J. Mobile-agent: Autonomous

multi-modal mobile device agent with visual perception.

arXiv preprint arXiv:2401.16158 , 2024b.

Wang, L., Xu, W., Lan, Y., Hu, Z., Lan, Y., Lee, R. K.-W.,

and Lim, E.-P. Plan-and-solve prompting: Improving

zero-shot chain-of-thought reasoning by large language

models. arXiv preprint arXiv:2305.04091 , 2023b.

Wang, P., Bai, S., Tan, S., Wang, S., Fan, Z., Bai, J., Chen,

K., Liu, X., Wang, J., Ge, W., et al. Qwen2-vl: Enhancing

vision-language model’s perception of the world at any

resolution. arXiv preprint arXiv:2409.12191 , 2024c.

language model with self generated instructions, 2022.

of the 30th Annual International Conference on Mobile

Computing and Networking , pp. 543–557, 2024.

D. Rewoo: Decoupling reasoning from observations for

efficient augmented language models. arXiv preprint

arXiv:2305.18323 , 2023a.

2023b.

arXiv:2407.05858 , 2024a.

preprint arXiv:2401.08092 , 2024b.

Yang, Z., Li, L., Lin, K., Wang, J., Lin, C.-C., Liu, Z., and

(1):1, 2023b.

Yang, Z., Liu, J., Han, Y., Chen, X., Huang, Z., Fu, B.,

and Yu, G. Appagent: Multimodal agents as smartphone

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan,

K., and Cao, Y. React: Synergizing reasoning and acting

in language models. arXiv preprint arXiv:2210.03629 ,

2022.

Yi, R., Guo, L., Wei, S., Zhou, A., Wang, S., and Xu,

M. Edgemoe: Fast on-device inference of moe-based

large language models. arXiv preprint arXiv:2308.14352 ,

2023a.

Yi, R., Li, X., Qiu, Q., Lu, Z., Zhang, H., Xu, D., Yang,

L., Xie, W., Wang, C., and Xu, M. mllm: fast and

lightweight multimodal llm inference engine for mobile

Yi, R., Li, X., Xie, W., Lu, Z., Wang, C., Zhou, A., Wang,

2411.05046 .

Yin, W., Xu, M., Li, Y., and Liu, X. Llm as a system service

2024.

Yuan, J., Yang, C., Cai, D., Wang, S., Yuan, X., Zhang,

Z., Li, X., Zhang, D., Mei, H., Jia, X., et al. Mobile

Zhang, J., Lan, T., Murthy, R., Liu, Z., Yao, W., Tan, J.,

Zhang, L., Wang, S., Jia, X., Zheng, Z., Yan, Y., Gao, L.,

Zhu, Q., Guo, D., Shao, Z., Yang, D., Wang, P., Xu, R.,

| Wang, J., Xu, H., Jia, H., Zhang, X., Yan, M., Shen, W., | Wang, L. The dawn of lmms: Preliminary explorations |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Zhang, J., Huang, F., and Sang, J. | Mobile-agent-v2: | with gpt-4v (ision). | arXiv preprint arXiv:2309.17421 | , 9 |  |
| Wang, J., Xu, H., Ye, J., Yan, M., Shen, W., Zhang, J., | users. | arXiv preprint arXiv:2312.13771 | , 2023c. |  |  |
| Wang, Y., Kordi, Y., Mishra, S., Liu, A., Smith, N. A., | and edge devices, 2023b. | URL | https://github. |  |  |
| Khashabi, D., and Hajishirzi, H. Self-instruct: Aligning | com/UbiquitousLearning/mllm | . |  |  |  |
| Wen, H., Li, Y., Liu, G., Zhao, S., Yu, T., Li, T. J.-J., Jiang, | S., Zhang, X., and Xu, M. Phonelm:an efficient and capa- |  |  |  |  |
| S., Liu, Y., Zhang, Y., and Liu, Y. | Autodroid: Llm- | ble small language model family through principled pre- |  |  |  |
| powered task automation in android. | In | Proceedings | training, 2024. | URL | https://arxiv.org/abs/ |
| Xu, B., Peng, Z., Lei, B., Mukherjee, S., Liu, Y., and Xu, | on mobile devices. | arXiv preprint arXiv:2403.11805 | , |  |  |
| Xu, D., Yin, W., Jin, X., Zhang, Y., Wei, S., Xu, M., and | foundation model as firmware. In | Proceedings of the 30th |  |  |  |
| Liu, X. Llmcad: Fast and scalable on-device large lan- | Annual International Conference on Mobile Computing |  |  |  |  |
| guage model inference. | arXiv preprint arXiv:2309.04255 | , | and Networking | , pp. 279–295, 2024. |  |
| Xu, D., Zhang, H., Yang, L., Liu, R., Huang, G., Xu, | Hoang, T., Yang, L., Feng, Y., Liu, Z., et al. Agentohana: |  |  |  |  |
| M., and Liu, X. | Empowering 1000 tokens/second on- | Design unified data and training pipeline for effective |  |  |  |
| device llm prefilling with mllm-npu. | arXiv preprint | agent learning. | arXiv preprint arXiv:2402.15506 | , 2024a. |  |
| Xu, M., Yin, W., Cai, D., Yi, R., Xu, D., Wang, Q., Wu, B., | Li, Y., and Xu, M. Llamatouch: A faithful and scalable |  |  |  |  |
| Zhao, Y., Yang, C., Wang, S., et al. A survey of resource- | testbed for mobile ui automation task evaluation. | arXiv |  |  |  |
| efficient llm and multimodal foundation models. | arXiv | preprint arXiv:2404.16054 | , 2024b. |  |  |
| Yang, A., Yang, B., Hui, B., Zheng, B., Yu, B., Zhou, C., | Wu, Y., Li, Y., Gao, H., Ma, S., et al. Deepseek-coder- |  |  |  |  |
| Li, C., Li, C., Liu, D., Huang, F., et al. Qwen2 technical | v2: Breaking the barrier of closed-source models in code |  |  |  |  |
| report. | arXiv preprint arXiv:2407.10671 | , 2024. | intelligence. | arXiv preprint arXiv:2406.11931 | , 2024. |

---

## Page 13

DroidCall : A Dataset for LLM-powered Android Intent Invocation

A. Data Generation Prompts

At the beginning of data generation, we first generate seed data. The prompt used to generate seed is shown as following:

I need your help to generate some function calling datasets. I will provide you with a tool description, and you need to

generate queries and corresponding answers based on this tool, i.e., the answers that call the tool to resolve the user’s

query. Here are my requirements:

1. For queries, try to use different vocabulary and syntax to ensure query diversity. Queries can be long or short,

complex or concise. In short, try not to generate similar queries; I want to ensure query diversity.

2. The language of the queries should be as diverse as possible. This means a query can be a command, a question, or

a request with detailed descriptions, etc.

3. The generated queries should cover all possible uses of the tool as much as possible, meaning the coverage of

various parameters should be comprehensive, ensuring the tool can be used to complete various forms of work.

4. The generated queries should be solvable using the given tools.

5. For the queries you generate, you should provide answers using the tool, i.e., give the tool used and the values for

each parameter.

6. When providing parameters, if a parameter has required=False, you may omit its value.

7. The generated data must be presented in the format given in my example.

8. The parameter values generated with function call generated must be values that can be inferred from the user’s

query; YOU CANNOT FABRICATE PARAMETERS THAT CANNOT BE OBTAINED FROM THE USER’S

REQUEST.

9. Attach each answer with an id starting from 0. And if a tool should use the respone from another tool, you can

reference it using #id, where id is the id of the tool.

following are some examples:

$examples

Now I will give you a tool, and you help me generate 15 query-answer pairs.

REMEMBER TO GENERATE THE RESULT IN JSON FORMAT LIKE THE EXAMPLE ABOVE REMEMBER

NOT TO FABRICATE PARAMETERS FOR TOOLS. PARAMETERS SHOULD BE INFERED FROM USER

QUERY.

tool: $tool

In the prompt above, $examples will be replace by random samples sampled from xlam-function-calling-60k (Liu et al.,

2024d). Below is an example:

tool: {

"name: "...",

"description": "...",

"arguments": {

...

}

}

response: {

"query": "...",

"answers": [

{

...

}

]

}

$tools will be replace by json formatted predefined function, below is an example:

---

## Page 14

DroidCall : A Dataset for LLM-powered Android Intent Invocation

tool: {

"name": "ACTION_SET_ALARM",

"description": "...".

"arguments": {

...

}

}

After seed generation stage, we will use another prompt to continuously generate data. Prompt is shown as following:

I need your help to generate some function calling datasets. I will provide you with a tool description and some

example data for you. You need to generate queries and corresponding answers based on this tool, i.e., the answers that

call the tool to resolve the user’s query. Here are my requirements:

1. For queries, try to use different vocabulary and syntax to ensure query diversity. Queries can be long or short,

complex or concise. In short, try not to generate similar queries; I want to ensure query diversity.

2. The language of the queries should be as diverse as possible. This means a query can be a command, a question, or

a request with detailed descriptions, etc.

3. The generated queries should cover all possible uses of the tool as much as possible, meaning the coverage of

various parameters should be comprehensive, ensuring the tool can be used to complete various forms of work.

4. The generated queries should be solvable using the given tools.

5. For the queries you generate, you should provide answers using the tool, i.e., give the tool used and the values for

each parameter.

6. When providing parameters, if a parameter has required=False, it is not necessary to provide its value.

7. The query-answer pairs should cover as many possible uses of the tool as possible.

8. The generated data must be presented in the format given in my example.

9. The parameter values generated with function call generated must be values that can be inferred from the user’s

query; YOU CANNOT FABRICATE PARAMETERS THAT CANNOT BE OBTAINED FROM THE USER’S

REQUEST.

following are tool I provided and some examples of query-answer pairs: tool: $tool examples: $examples

Now please help me generate 40 query-answer pairs. REMEMBER TO GENERATE THE RESULT IN JSON

FORMAT LIKE THE EXAMPLE ABOVE REMEMBER NOT TO FABRICATE PARAMETERS FOR TOOLS.

PARAMETERS SHOULD BE INFERED FROM USER QUERY.

$tool will be replaced by the json format of predefined functions shown early. $examples is the data sampled from the seed

data generated previously.

When generating data of complex call, we slightly modify the prompt shown above. The seed generation prompt is shown

below:

I need your help to generate some function calling datasets. I will provide you with a tool description, and you need to

generate queries and corresponding answers based on this tool, i.e., the answers that call the tool to resolve the user’s

query. Here are my requirements:

1. For queries, try to use different vocabulary and syntax to ensure query diversity. Queries can be long or short,

complex or concise. In short, try not to generate similar queries; I want to ensure query diversity.

2. The language of the queries should be as diverse as possible. This means a query can be a command, a question, or

a request with detailed descriptions, etc.

3. The generated queries should cover all possible uses of the tool as much as possible, meaning the coverage of

various parameters should be comprehensive, ensuring the tool can be used to complete various forms of work.

4. The generated queries should be solvable using the given tools.

5. For the queries you generate, you should provide answers using the tool, i.e., give the tool used and the values for

each parameter.

---

## Page 15

DroidCall : A Dataset for LLM-powered Android Intent Invocation

6. When providing parameters, if a parameter has required=False, you may omit its value.

7. The generated data must be presented in the format given in my example.

8. THE PARAMETER VALUES GENERATED WITH FUNCTION CALL GENERATED MUST BE VALUES

THAT CAN BE INFERRED FROM THE USER’S QUERY; YOU CANNOT FABRICATE PARAMETERS THAT

CANNOT BE OBTAINED FROM THE USER’S REQUEST.

9. THE GENERATED QUERY SHOULD CONTAIN ENOUGH INFOMATION SO THAT YOU COULD

CORRECTLY GENERATE PARAMETER USED BY THE TOOLS. THIS IS ALSO TO GUARANTEE THAT YOU

DON’T FABRICATE PARAMETERS.

10. You should use all the tools I provided to generate the query and answer. It means that you should generate a query

that needs to use all the tools I provided to solve, and remember to provider an answer that uses all the tools to solve

the query.

11. You can use the same tool multiple times in a single query to ensure the query diversity.

12. Attach each answer with an id starting from 0. And if a tool should use the respone from another tool, you can

reference it using #id, where id is the id of the tool.

13. Generate data of nested function calls if possible. i.e., the argument of a function call is the response of another

function call.

following are some examples:

$examples

Now I will give you a tool, and you help me generate 15 query-answer pairs. REMEMBER TO GENERATE THE

RESULT IN JSON FORMAT LIKE THE EXAMPLE ABOVE AND PUT IT IN A JSON LIST.

REMEMBER YOU SHOULD USE ALL THE TOOLS AT ONE QUERY AND SOLVE IT WITH ALL TOOLS, AND

GENERATE NESTED CALL IF POSSIBLE.

REMEMBER NOT TO FABRICATE PARAMETERS FOR TOOLS. PARAMETERS SHOULD BE INFERED FROM

USER QUERY.

tools:

$tools

Prompt for continuously generating complex function calling data is:

I need your help to generate some function calling datasets. I will provide you with a tool description, and you need to

generate queries and corresponding answers based on this tool, i.e., the answers that call the tool to resolve the user’s

query. Here are my requirements:

1. For queries, try to use different vocabulary and syntax to ensure query diversity. Queries can be long or short,

complex or concise. In short, try not to generate similar queries; I want to ensure query diversity.

2. The language of the queries should be as diverse as possible. This means a query can be a command, a question, or

a request with detailed descriptions, etc.

3. The generated queries should cover all possible uses of the tool as much as possible, meaning the coverage of

various parameters should be comprehensive, ensuring the tool can be used to complete various forms of work.

4. The generated queries should be solvable using the given tools.

5. For the queries you generate, you should provide answers using the tool, i.e., give the tool used and the values for

each parameter.

6. When providing parameters, if a parameter has required=False, you may omit its value.

7. The generated data must be presented in the format given in my example.

8. THE PARAMETER VALUES GENERATED WITH FUNCTION CALL GENERATED MUST BE VALUES

THAT CAN BE INFERRED FROM THE USER’S QUERY; YOU CANNOT FABRICATE PARAMETERS THAT

CANNOT BE OBTAINED FROM THE USER’S REQUEST.

9. THE GENERATED QUERY SHOULD CONTAIN ENOUGH INFOMATION SO THAT YOU COULD

CORRECTLY GENERATE PARAMETER USED BY THE TOOLS. THIS IS ALSO TO GUARANTEE THAT YOU

DON’T FABRICATE PARAMETERS.

10. You should use all the tools I provided to generate the query and answer. It means that you should generate a query

that needs to use all the tools I provided to solve, and remember to provider an answer that uses all the tools to solve

---

## Page 16

DroidCall : A Dataset for LLM-powered Android Intent Invocation

the query.

11. You can use the same tool multiple times in a single query to ensure the query diversity.

12. Attach each answer with an id starting from 0. And if a tool should use the respone from another tool, you can

reference it using #id, where id is the id of the tool.

13. Generate data of nested function calls if possible. i.e., the argument of a function call is the response of another

function call.

Now I will give you some tools and some example data of query-answer pairs using these tools. Please help me

generate 40 query-answer pairs. tools: $tools

examples: $examples

REMEMBER TO GENERATE THE RESULT IN JSON FORMAT LIKE THE EXAMPLE ABOVE AND PUT IT IN

A JSON LIST.

REMEMBER YOU SHOULD USE ALL THE TOOLS AT ONE QUERY AND SOLVE IT WITH ALL TOOLS, AND

GENERATE NESTED CALL IF POSSIBLE.

REMEMBER NOT TO FABRICATE PARAMETERS FOR TOOLS. PARAMETERS SHOULD BE INFERED FROM

USER QUERY.

B. Function Calling Prompts

In § 4.1, we’ve mentioned that we have tested 4 format of prompt: json , code , json_short and code_short . To unify our

fine-tuning, we use chat to do function calling thus we only need to design the part of system, user and assistant using chat

template.

In json or code format, the system prompt would be:

You are an expert in composing functions. You are given a query and a set of possible functions. Based on the query,

you will need to make one or more function calls to achieve the purpose. If none of the function can be used, point it

out. If the given question lacks the parameters required by the function, also point it out. Remember you should not

use functions that is not suitable for the query and only return the function call in tools call sections.

in json_short or code_short the system prompt would be:

You are an expert in composing functions.

The user part of json or code is:

Here is a list of functions that you can invoke:

$functions

Should you decide to return the function call(s), Put it in the format of

$format_description

$example

If there is a way to achieve the purpose using the given functions, please provide the function call(s) in the above

format. REMEMBER TO ONLY RETURN THE FUNCTION CALLS LIKE THE EXAMPLE ABOVE, NO OTHER

INFORMATION SHOULD BE RETURNED.

Now my query is: $user_query

$functions is the functions descriptions provided by retriever, in code or code_short format, it would be like:

Name:

send_email

Description:

Compose and send an email with optional attachments.

---

## Page 17

DroidCall : A Dataset for LLM-powered Android Intent Invocation

This function allows the user to compose an email with various options,

including multiple recipients, CC, BCC, and file attachments.

Args:

to (List[str]): ...

subject (str): ...

...

Returns:

None

Example:

# Send an email with a content URI attachment

send_email(

to=["recipient@example.com"],

subject="Document",

body="Please find the attached document.",

attachments=...

)

In json or json_short , functions would be describe directly in json format as shown in Listing 1.

$format_description in the prompt will be replace by detailed output format the model should follow. In json it will be:

[

{

"id": 0,

"name": "func0",

"arguments": {

"arg1": "value1",

"arg2": "value2",

...

}

},

{

"id": 1,

"name": "func1",

"arguments": {

"arg1": "value1",

"arg2": "value2",

...

}

},

...

]

If an argument is a response from a previous function call,

you can reference it in the following way like the argument

value of arg2 in func1:

[

{

"id": 0,

"name": "func0",

"arguments": {

"arg1": "value1",

"arg2": "value2",

...

---

## Page 18

DroidCall : A Dataset for LLM-powered Android Intent Invocation

}

},

{

"id": 1,

"name": "func1",

"arguments": {

"arg1": "value1",

"arg2": "#0",

...

}

},

...

]

This means that the value of arg2 in func1 is the return

value from func0 (#0 means the response from the function call with id 0).

In code format this will be

result1 = func0(arg1="value1", arg2="value2", ...)

result2 = func1(arg1="value1", arg2=result1, ...)

...

You can do nested function calling in the following way:

result1 = func0(arg1="value1", arg2="value2", ...)

result2 = func1(arg1="value1", arg2=result1, ...)

...

This means that the value of arg2 in func1 is the return value from func0.

$example in the prompt is used to test few-shot performance of a model.

The user prompt of json_short or code_short is much simpler withou task instructions :

Here is a list of functions: $functions

Now my query is: $user_query

In code or code_short format the assistant output would be:

<sep>result1 = func0(arg1="value1", arg2="value2", ...)

result2 = func1(arg1="value1", arg2=result1, ...)</sep>

where < sep > and < /sep > can be any seperator set before fine-tuning.

In json or json_short format the assistant output would be:

[

{

"id": 0,

"name": "func0",

"arguments": {

"arg1": "value1",

"arg2": "value2",

...

}

},

---

## Page 19

DroidCall : A Dataset for LLM-powered Android Intent Invocation

...

]
