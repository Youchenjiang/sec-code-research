---
title: "LLM-Assisted Model-Based Fuzzing of Protocol Implementations"
author: "Changze Huang; Di Wang; Zhi Quan Zhou"
creator: "arXiv GenPDF (tex2pdf:)"
pages: 11
---

# LLM-Assisted Model-Based Fuzzing of Protocol Implementations

> **作者**：Changze Huang; Di Wang; Zhi Quan Zhou
> **總頁數**：11 頁

---

## Page 1

LLM-Assisted Model-Based Fuzzing of Protocol Implementations

| Changze Huang | Di Wang | Zhi Quan Zhou |  |
| --- | --- | --- | --- |
| hcz@stu.pku.edu.cn | wangdi95@pku.edu.cn | george.zhou@nio.com |  |
| Key Lab of HCST (PKU), MOE; | Key Lab of HCST (PKU), MOE; | NIO Inc. |  |
| SCS, Peking University | SCS, Peking University | Shanghai, China |  |
| Beijing, China | Beijing, China |  |  |
| Abstract | Nevertheless, having domain knowledge about protocols can be |  |  |
| Testing network protocol implementations is critical for ensuring | helpful. | Model-based fuzzing | of protocol implementations [9, 10, |
| the reliability, security, and interoperability of distributed systems. | 38, 39] is a method that uses knowledge about protocols. These |  |  |
| Faults in protocol behavior can lead to vulnerabilities and system | methods use a predefined (usually coarse-grained) model of pro- |  |  |
| failures, especially in real-time and mission-critical applications. A | tocol behavior to generate | sequences | of messages, systematically |
| common approach to protocol testing involves constructing Mar- | exploring the state space of the protocol. One widely employed |  |  |
| kovian models that capture the state transitions and expected be- | family of models is finite-state machines (FSMs) [20, 22, 42, 43]. |  |  |
| haviors of the protocol. However, building such models typically | These methods use an FSM to represent the states and transitions |  |  |
| requires significant domain expertise and manual effort, making | defined by a protocol, enabling the fuzzer to produce sequences of |  |  |
| the process time-consuming and difficult to scale across diverse | messages that reflect protocol-specific communication patterns. Fol- |  |  |
| protocols and implementations. | lowing the predefined model, these methods improve input validity, |  |  |
| We propose a novel method that leverages large language models | enhance code coverage, and increase the chances of identifying |  |  |
| (LLMs) to automatically generate sequences for testing network pro- | bugs that depend on specific protocol states or message sequences. |  |  |
| tocol implementations. Our approach begins by defining the full set | However, the reliance on predefined models is a double-edged |  |  |
| of possible protocol states, from which the LLM selects a subset to | sword: the applicability and effectiveness of model-based fuzzing |  |  |
| model the target implementation. Using this state-based model, we | depend on the availability and quality of these models. Adapting |  |  |
| prompt the LLM to generate code that produces sequences of states. | model-based fuzzing to different protocols requires the manual |  |  |
| This program serves as a protocol-specific sequences generator. The | construction of protocol models, and adjusting these models to |  |  |
| sequences generator then generates test inputs to call the protocol | optimize fuzzing performance would be an effort-consuming task. |  |  |
| implementation under various conditions. We evaluated our ap- | In this paper, we propose ChatFuMe, a model-based protocol- |  |  |
| proach on three widely used network protocol implementations and | implementation fuzzing method that leverages large language mod- |  |  |
| successfully identified 12 previously unknown vulnerabilities. We | els (LLMs) [17] to construct and adjust protocol models | automati- |  |
| have reported them to the respective developers for confirmation. | cally | . LLMs have emerged as a novel tool for general fuzzing [52, 53], |  |
| This demonstrates the practical effectiveness of our LLM-assisted | as well as protocol-implementation fuzzing [35, 37, 49]. These LLM- |  |  |
| fuzzing framework in uncovering real-world security issues. | assisted fuzzing methods leverage the understanding and genera- |  |  |

Keywords

Network-protocol implementations are widely deployed across sys-

arXiv:2508.01750v1 [cs.CR] 3 Aug 2025 tems from cloud services and web applications [11, 13] to embedded

devices [15, 27] and industrial control systems [48]. Bugs in these

implementations can persist for an extended period, compromising

the security and stability of the systems. Studies show that even a

tion capabilities of LLMs to produce syntactically and semantically

valid messages for different protocols. Unlike ChatFuMe, none of

these are model-based: they rely on LLMs to directly generate a

Instead of direct generation of message sequences, ChatFuMe

uses LLMs to automatically construct and adjust protocol models

ate random message sequences. Our motivation is driven by the

LLMs’ strong capabilities in generating programs , inferring state

transitions, and embedding domain knowledge from protocol doc-

umentation and usage patterns. Our design of ChatFuMe aims to

strike a balance among the following desiderata:

| Protocol-Implementation Fuzzing, Model-Based Fuzzing, LLM- | large number of sequences of protocol messages, resulting in long |  |  |  |
| --- | --- | --- | --- | --- |
| Assisted Testing | generation time and high token consumption. |  |  |  |
| 1 | Introduction | in the form of random sequence-generator | programs | that gener- |
| single malformed input or unhandled edge case can disrupt services | • | Flexibility | . ChatFuMe handles implementations of different |  |
| and cause catastrophic consequences [12, 28, 54]. Thus, identifying | protocols with little adaptation effort. |  |  |  |
| these bugs is an essential step when implementing protocols. | • | Effectiveness | . ChatFuMe achieves comparable performance |  |
| In this paper, we focus on | fuzzing | of protocol implementations. | against model-based fuzzing with predefined models. |  |
| Studies show that fuzzing is an effective method for testing protocol | • | Cost-efficiency | . ChatFuMe consumes much fewer tokens |  |
| implementations [21, 24, 25, 40]. In these methods, a fuzzer usually | than prior LLM-assisted protocol fuzzing methods. |  |  |  |
| sends crafted protocol messages over a network interface or di- | ChatFuMe consists of two major components: (i) automatic |  |  |  |
| rectly to a broker to trigger unexpected states, crashes, or abnormal | model construction, and (ii) feedback-guided fuzzing loop. The |  |  |  |
| responses. One major benefit of fuzzing is its capacity to explore a | model construction starts with identifying protocol states, using |  |  |  |
| large state space without requiring a formal protocol specification. | the protocol’s documentation (possibly with some user prompts to |  |  |  |

---

## Page 2

encode domain knowledge) as input. ChatFuMe then asks the LLM Table 1: A summary of MQTT control packets.

to summarize the protocol behavior, capturing high-level domain-

a coarse-grained protocol model. Rather than directly generating

message sequences, ChatFuMe asks the LLM to construct a se-

FuMe then collects the behavior of the protocol implementation,

such as its responses, and prompts the LLM to evaluate these re-

sults and suggest adjustments to the protocol model. In particular,

the LLM is supposed to provide feedback on whether to add new

states, remove existing ones, or update transition probabilities. With

the feedback, ChatFuMe’s model-construction component adjusts

the protocol model and the generator program. The fuzzing-loop

2 Background: Model-Based Fuzzing of Protocol

2

| PINGREQ | Check if connection to broker is alive | FH |
| --- | --- | --- |
| PINGRESP | Confirm connection is active | FH |

DISCONNECT Close network connection gracefully FH

UNSUBACK Acknowledge UNSUBSCRIBE packet FH, VH, payload

in Section 3. We then sketch FUME’s predefined model that guides

the fuzzing of MQTT implementations.

tated through topics , which serve as virtual channels for message

broker (i.e., server), which manages connections, filters incoming

Table 1 summarizes the 15 MQTT packet types.

The explicit connection management packets highlight MQTT’s

stateful nature. Such statefulness enables the broker to retain a

| specific patterns of the states and transitions. Next, ChatFuMe | Name | Purpose | Components |
| --- | --- | --- | --- |
| prompts the LLM to select key states and summarize the transition | CONNECT | Initiate connection to broker | FH, VH, payload |
| rules among them. These states and transitions form the basis of | CONNACK | Acknowledge connection request | FH, VH |
| quence generator, which is an executable program that samples | AUTH | Exchange authentication data | FH, VH |
| state transitions and generates random message sequences. | PUBLISH | Deliver message to subscribers | FH, VH, payload |
| After the model construction, ChatFuMe’s fuzzing loop starts | PUBACK | Acknowledge QoS 1 PUBLISH | FH, VH |
| with pairing the random sequence generator with a user-provided | PUBREC | Acknowledge QoS 2 PUBLISH | FH, VH |
| payload generator that handles the low-level field formatting of | PUBREL | Confirm receipt of PUBREC | FH, VH |
| messages. The user can once again use an LLM to program the | PUBCOMP | Confirm receipt of PUBREL | FH, VH |
| payload generator in advance. Executing the random generator | SUBSCRIBE | Request subscription to topics | FH, VH, payload |
| multiple times, ChatFuMe generates multiple message sequences | SUBACK | Acknowledge SUBSCRIBE packet | FH, VH, payload |
| and sends them to the protocol implementation being tested. Chat- | UNSUBSCRIBE Request to cancel subscriptions | FH, VH, payload |  |
| component then begins another iteration using the adjusted model. | 2.1 | The MQTT Protocol |  |
| Our experiments demonstrate that ChatFuMe is reasonably flex- | The Message Queuing Telemetry Transport (MQTT) protocol [4] |  |  |
| ible, effective, and cost-efficient. In testing three different real-world | has emerged as the de facto standard for messaging in the Internet |  |  |
| protocol implementations, our approach discovered 12 potential | of Things (IoT) and Industrial IoT (IIoT) domains [47]. Standardized |  |  |
| bugs, validating its fault detection capability. Compared to a prior | by OASIS and ISO, MQTT is a lightweight, event-driven protocol de- |  |  |
| model-based fuzzer, our method identified more new protocol states | signed for environments with limited bandwidth and high latency, |  |  |
| within the same time window, demonstrating its effectiveness in | making it ideal for devices such as sensors, embedded systems, |  |  |
| exploration. Additionally, compared to a prior LLM-based fuzzer, | and industrial PLCs. At its core, MQTT operates on a publish/sub- |  |  |
| our technique achieves lower token consumption, highlighting its | scribe model, which inherently decouples message | publishers | (i.e., |
| cost efficiency and scalability in practical fuzzing scenarios. | senders) from | subscribers | (i.e., receivers). Communication is facili- |
| Contributions. | The paper’s contributions include the following: | exchange. The central component of this architecture is the MQTT |  |
| • | We propose ChatFuMe, an LLM-assisted model-based | messages from publishers based on their topics, and efficiently |  |
| fuzzing method for protocol implementations. The key inno- | distributes them to all interested subscribers. |  |  |
| vation is that it uses LLMs to construct and adjust a protocol- | In MQTT, all communication between clients and brokers is |  |  |
| model program that generates message sequences. | facilitated through the exchange of | control packets | , which are the |
| • | We implement ChatFuMe and conduct an experimental | fundamental units of data transfer. These packets encapsulate vari- |  |
| evaluation of it. Our experiments demonstrate the flexibility | ous operational commands, enabling functions such as establishing |  |  |
| of ChatFuMe by applying it to three different protocols, its | connections, managing subscriptions, and publishing application |  |  |
| effectiveness by comparing it against a prior model-based | messages. Each control packet adheres to a structured format con- |  |  |
| method FUME [39], and its cost efficiency by comparing it | sisting of up to three main components: a fixed header (FH), a |  |  |
| against a prior LLM-assisted method ChatAFL [37]. | variable header (VH), and the | payload | , which contains the actual |
| • | We apply ChatFuMe on three real-world protocol imple- | data or message that may vary depending on the control packet type. |  |
| mentations (HMQ, PyModbus, and Moquette) and discover | MQTT supports 15 different packet types, including connection |  |  |
| 12 potential bugs in these implementations. | management, message publishing, and subscription management. |  |  |
| Implementations | client’s subscriptions and buffer messages for delivery upon re- |  |  |
| In this section, we review FUME [39], a model-based fuzzing tech- | connection, which is crucial for maintaining persistent sessions. |  |  |
| nique designed for Message Queuing Telemetry Transport (MQTT) | However, the statefulness results in a vast and complex input space |  |  |
| implementations. We begin by reviewing the MQTT protocol, | for fuzzing. A fuzzing method needs domain knowledge about |  |  |
| which we will use as a concrete protocol to demonstrate our method | MQTT to generate valid message sequences (e.g., they should start |  |  |

---

## Page 3

| Start | Generate | Fuzz |
| --- | --- | --- |
| payload | payload | Send |

15 states for 15 packet types

Figure 1: FUME’s generation-guided fuzzing model.

els (i.e., FSMs with probabilistic transitions) to describe mutation-

guided and generation-guided fuzzing, respectively. Mutation -

guided fuzzing requires an input corpus of valid message sequences

as test cases. On the other hand, generation -guided fuzzing requires

domain knowledge of the protocol to generate valid message se-

quences. In this paper, we aim to develop a flexible fuzzing method

applicable to different protocol implementations, where informal

protocol descriptions are often more readily available than a corpus

of test cases; thus, we focus on generation-guided fuzzing.

Figure 1 demonstates FUME’s fuzzing model of one iteration of

generation-guided fuzzing. We ignore the state-transition probabil-

ities, so it appears just like an FSM. The model describes a random

generation process: it starts with generating a CONNECT mes-

sage and its payload, then stochastically generates some follow-up

messages, applies fuzzing (e.g., insertion, deletion, and mutation)

to the payloads multiple times, and finally sends the message se-

quences to the MQTT broker. FUME has another fuzzing model for

its mutation-guided fuzzing process, and it alternates between the

two fuzzing models to leverage the strengths of both models.

We take inspiration from FUME with a key observation: such

fuzzing models can be easily expressed by executable programs that

generate random message sequences. Moreover, payload genera-

tors are also executable programs. The observation motivates us

to leverage the understanding and programming capabilities of

LLMs to extract domain knowledge about protocols and generate

executable programs that represent the fuzzing models.

3

Sections 3.2 and 3.3 use MQTT as a demonstration protocol to

explain the two components, respectively.

3.1 Overview of the Workflow

it uses LLMs to automate various steps in the workflow, including

the construction and adjustment of the fuzzing model. In this way,

ChatFuMe achieves flexibility to handle different protocols.

Automatic model construction. ChatFuMe begins with user-

provided protocol documentation, which may include prompts to

describe protocol states as a high-level summary of a protocol’s

With the augmented set of states, ChatFuMe again requests the

Feedback-guided fuzzing loop. Based on the constructed protocol

model, ChatFuMe uses an LLM to generate a sequence-generator

program, which produces randomized state sequences that con-

form to transition rules. The sequence generator is paired with a

user-provided payload generator—which an LLM could generate

in advance—to generate complete message sequences. ChatFuMe

then sends these sequences to the protocol implementation and

monitors its behavior, e.g., whether it crashes or reports abnormal

responses. After collecting the testing results, ChatFuMe decides

whether to adjust the protocol model. We employ two mechanisms

for this decision: (i) with a predefined probability, ChatFuMe resets

the protocol model to the initial one constructed at the beginning

of the workflow, i.e., incorporates random restart ; or (ii) ChatFuMe

prompts the LLM to analyze the testing results and decide if the

model needs refinement, and if so, further prompts it to identify

states that contribute to effective testing outcomes. Typically, the

LLM would add a few new states or remove existing ones from

the protocol model. If the model gets adjusted, ChatFuMe loops

back to the phase of generating a sequence-generator program

via an LLM. Otherwise, it keeps the sequence-generator program

unchanged and starts the next loop iteration.

Incorporation of LLMs. We use LLMs because they provide capa-

bilities for understanding documentation (for model construction),

generating code (for program generation), and analyzing testing

results (for model adjustment). Furthermore, for widely used proto-

cols, even if the user does not possess domain knowledge, LLMs’

| Generate | Generate | Generate | Figure 2 presents an overview of ChatFuMe. Its key feature is com- |  |
| --- | --- | --- | --- | --- |
| CONNECT | CONNACK | UNSUBACK | Finish | bining model-based protocol-implementation fuzzing with LLMs: |
| with a CONNECT message) and explore deep states (e.g., some | specification. ChatFuMe uses an LLM to augment the set of states |  |  |  |
| states can only be reached by subscribing to a specific topic). | by extracting domain knowledge from the protocol documentation. |  |  |  |
| 2.2 | FUME’s Fuzzing Model for MQTT Brokers | LLM to perform state selection and summarize the state-transition |  |  |
| FUME is a fuzzing method designed explicitly for testing MQTT | rules, narrowing down to a small but essential subset of states as |  |  |  |
| implementations [39]. To this end, FUME is a model-based fuzzing | the starting point for fuzzing and capturing how the protocol al- |  |  |  |
| method because it requires a predefined model of the MQTT proto- | lows moving between different states. These transitions, with the |  |  |  |
| col to guide the fuzzing process. FUME’s model is coarse-grained: | selected states, form a lightweight coarse-grained model of protocol |  |  |  |
| it only knows the 15 message types shown in Table 1, and every | behavior. This component also provides the functionality to adjust |  |  |  |
| message sequence must start with CONNECT. | the model by prompting an LLM to modify the selected states based |  |  |  |
| FUME then uses the MQTT model to construct two Markov mod- | on feedback from the fuzzing loop, which we explain below. |  |  |  |
| 3 | Our Method | familiarity with these protocols enables ChatFuMe to perform |  |  |
| In this section, we describe the workflow and technical details | fuzzing effectively with minimal guidance. Instead of asking the |  |  |  |
| of our ChatFuMe method. Section 3.1 presents an overview of | LLM to generate individual test cases directly, we prompt it to gen- |  |  |  |
| ChatFuMe’s workflow and its two major components: (i) auto- | erate an executable program as a random sequence generator. This |  |  |  |
| matic model construction, and (ii) feedback-guided fuzzing loop. | generator-based design significantly reduces token consumption |  |  |  |

---

## Page 4

| Automatic Model Construction | Feedback-Guided Fuzzing Loop |  |  |  |
| --- | --- | --- | --- | --- |
| ① | Input | ① | Input |  |
| Protocol | ④ | Code | Sequence-Generator | Payload-Generator |
| Description | Program | Program |  |  |
| ② | Extract | ⑤ | Generate |  |

S1 S2

Summarize

③

…… S3

S1

Initial States … S3

…

⑧

Key States and Transitions

The construction of our fuzzing model begins with user-provided

identification of protocol states, which can be derived from existing

initions, enabling better downstream reasoning during fuzzing. By

combining user input with LLM-driven knowledge expansion, we

strike a balance between manual guidance and automated insight.

4 " UNSUBSCRIBE " , " UNSUBACK " , " PINGREQ " ,

5 " PINGRESP " , " DISCONNECT " , " AUTH " ]

Once domain knowledge is incorporated, we leverage the LLM to

⑦

Decide

LLM

⑥ Test

Feedback Whether to Testing Message

Adjust Model Results Sequences

cise justifications for their importance. This automated abstraction

balancing coverage and efficiency in the input space exploration.

protocol into a small number of essential states

while preserving enough semantics to be useful for

testing client and broker implementations .

3 Output Format : { example } '''

4 ` " select " ` : A short name for the state

8 '''

4

Figure 2: An overview of ChatFuMe’s workflow. Dotted arrows indicate prompting the LLM for specific tasks.

| by generating numerous message sequences from a single genera- | of reducing the input space by selecting a small number of high- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tor, making ChatFuMe cost-efficient for LLM-assisted fuzzing of | impact states. The Listings 3 specifies a structured output format, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| real-world protocol implementations. | requiring the LLM to return a JSON array of state names and con- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3.2 | Automatic Model Construction | enables ChatFuMe to focus on high-impact areas of the protocol, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| work, specifications, documentation, or manual analysis. Listing | Listing 2: The prompt for state selection. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 provides an example of the initial states of MQTT. These initial | 1 | Prompt_for_States_Selection | = | f '''I | am | designing | a | model - |  |  |  |  |  |  |  |  |
| states can be extracted from the MQTT specification [4]. These | based | testing | framework | for | the | { protocol }. | To |  |  |  |  |  |  |  |  |  |
| states provide a coarse-grained foundation for understanding the | reduce | the | search | space , | I | want | to | abstract | the |  |  |  |  |  |  |  |
| protocol’s high-level behavior. To enrich this initial model, we | that | capture | the | most | important | aspects | of | its |  |  |  |  |  |  |  |  |
| prompt the LLM to incorporate domain knowledge, such as typical | behavior | for | testing | purposes . |  |  |  |  |  |  |  |  |  |  |  |  |
| client-server interactions and expected message sequences. This | 2 | Please | help | me | identify | { number } | essential | states | above |  |  |  |  |  |  |  |
| step enhances the completeness and semantic accuracy of state def- | that | cover | the | core | functionality | of | { protocol } |  |  |  |  |  |  |  |  |  |
| Listing 1: An example of initial states. The list above repre- | Listing 3: The Example for state selection. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| sents the primary MQTT control packet types. Each state | 1 | Example_for_States_Selection | = | f ''' |  |  |  |  |  |  |  |  |  |  |  |  |
| corresponds to a specific control packet used in the commu- | 2 | Return | a | JSON | array | of | { number } | objects . |  |  |  |  |  |  |  |  |
| nication between MQTT clients and brokers. | 3 | Each | object | should | have | ONLY | the | following | fields : |  |  |  |  |  |  |  |
| 1 | states | = | [ | " CONNECT " , | " CONNACK " , | " PUBLISH " , | 5 | (e.g., | ` | " CONNECT " | ` | , | ` | " PUBLISH " | ` | ) |
| 2 | " PUBACK " , | " PUBREC " , | " PUBREL " , | 6 | ` | " reason " | ` | : | A | concise | explanation | of | why | this | state | is |
| 3 | " PUBCOMP " , | " SUBSCRIBE " , | " SUBACK " , | 7 | essential | for | { protocol } | testing |  |  |  |  |  |  |  |  |
| refine the state space by selecting a concise set of essential protocol | 3.3 | Feedback-Guided Fuzzing Loop |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| states for testing. This step abstracts the protocol into a manage- | In the feedback-guided fuzzing loop, we leverage the LLM to analyze |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| able number of representative states that retain sufficient semantic | execution results and guide the adjustment of the protocol model. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| coverage while reducing unnecessary complexity. As illustrated in | The loop begins with the LLM-generated sequence generator, which |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Listings 2 and 3, we construct a two-part prompt to guide the LLM | produces message sequences following the current state transition |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| in identifying essential protocol states for testing. The Listings 2 | model. These sequences serve as high-level plans for how a client |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| provides contextual information about the protocol and the goal | might interact with a protocol implementation. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 5

| To guide the LLM in producing a realistic sequence generator, | The generated sequences are then passed to a user-provided |  |  |
| --- | --- | --- | --- |
| we apply an | autoprompting | strategy [17, 50, 52] to create a high- | payload generator, which translates each sequence into concrete |
| quality prompt that encapsulates the protocol specification. Given | protocol messages. Note that the payload generator could also be |  |  |
| a set of selected states, we ask the LLM to construct a prompt that | generated in advance by an LLM. The resulting payloads are sent |  |  |
| will later be used to generate Python code implementing a random | to the target protocol implementation, and ChatFuMe records the |  |  |
| state sequence generator. This prompt includes constraints to pre- | feedback from each run to inform further model adjustment. |  |  |
| serve realistic protocol behavior, such as capturing state transition | After sending a sufficient number of fuzzing sequences (ranging |  |  |
| probabilities, enforcing randomness, and ensuring variable-length | from 20,000 to 50,000 in our experiments), ChatFuMe analyzes the |  |  |
| sequences. In this way, we distill the protocol specification into | feedback from the target protocol implementation and evaluates |  |  |
| a reusable instruction, forming a bridge between abstract state | the fuzzing effectiveness, guiding model adjustment. The analysis |  |  |
| modeling and a concrete generation of the generator. | focuses on identifying failure patterns by computing statistics such |  |  |
| After generating a prompt tailored for protocol behavior, we use | as the number of failures per protocol function, total request dis- |  |  |
| the LLM to produce a Python program as the sequence generator, | tribution, and failure rates. Specifically, we categorize responses |  |  |
| which we write into a module and dynamically import for execution. | like timeouts or connection resets as failures and calculate their |  |  |
| This integration step serves both as a code validity check and as | frequency relative to the total number of generated sequences. This |  |  |
| the mechanism to link LLM output with our fuzzing pipeline. If the | analysis provides insight into which parts of the protocol are more |  |  |
| generated code passes import and runtime validation, we invoke | error-prone, helping to inform the LLM-driven model adjustment |  |  |
| it repeatedly in the loop. Listing 4 presents an example of the | in subsequent fuzzing iterations. |  |  |
| code generated by the LLM, which incorporates both the protocol | The analysis above is then formatted and sent as part of a prompt |  |  |
| specification and random control structures. | to the LLM, asking it to interpret the results in the context of the |  |  |

2

3 def MQTT_state_generator () :

7 state_sequence . append ( current_state )

8

| 9 | while | True : |  |  |
| --- | --- | --- | --- | --- |
| 13 | next_state | = | random . choices ([ ' PUBLISH ', | ' |
| 14 | elif | current_state | == | ' PUBLISH ': |

SUBSCRIBE ', ' DISCONNECT '], weights =[60 , 30 , 10]) [0]

DISCONNECT ', ' PINGREQ '], weights =[40 , 30 , 30]) [0]

19 if random . random () < 0.5:

20 break

PUBACK '], weights =[70 , 30]) [0]

| 28 | state_sequence . append ( next_state ) |  |  |
| --- | --- | --- | --- |
| 29 | current_state | = | next_state |
| 34 | return | state_sequence |  |

target protocol and suggest whether any states should be added or

to analyze or reason about correlations between different types of

protocol implementations.

3 { states }

search space ?

6 It should ONLY have two fields :

search space ?

more states . '''

unselected candidates) or recommend removing underperforming

effective sequences and exploring new protocol behaviors.

5

| Listing 4: The Python code of an LLM-generated random | removed from the model to improve test effectiveness, as shown in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sequence generator for the MQTT protocol. | Listing 5. Notably, we only ask the LLM to interpret the statistical |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | import | random | results and enhance test effectiveness. We do not explicitly ask it |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | states | = | [ ' CONNECT ', | ' CONNACK ', | ' PUBLISH ', | ' SUBSCRIBE | failures. To ensure reliability, we validate any LLM-suggested states |  |  |  |  |  |  |  |  |  |  |  |
| ', | ' DISCONNECT ', | ' PINGREQ ', | ' PUBACK '] | to avoid hallucinated or irrelevant protocol behavior. This LLM- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | state_sequence | = | [] | driven evaluation allows our fuzzing process to adapt intelligently |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | current_state | = | ' CONNECT ' | over time, refining the model based on concrete feedback from |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | if | current_state | == | ' CONNECT ': | Listing 5: The prompt for model adjustment. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | next_state | = | random . choices ([ ' CONNACK ', | ' | 1 | Prompt_for_Decision | = | f '''{ reuslt_summary } |  |  |  |  |  |  |  |  |  |  |
| SUBSCRIBE '], | weights =[70 , | 30]) [0] | 2 | Above | is | the | summary | of | fuzzing | results | of | a | { protocol } |  |  |  |  |  |
| 12 | elif | current_state | == | ' CONNACK ': | implementation | using | these | states : |  |  |  |  |  |  |  |  |  |  |
| SUBSCRIBE ', | ' DISCONNECT '], | weights =[50 , | 30 , | 20]) [0] | 4 | Do | you | think | I | should | add | or | remove | more | states | in | the |  |
| 15 | next_state | = | random . choices ([ ' PUBACK ', | ' | 5 | Give | your | result | in | JSON | format . |  |  |  |  |  |  |  |
| 16 | elif | current_state | == | ' SUBSCRIBE ': | 7 | ` | " decision " | ` | : | ADD | or | DELETE | answer | for | should | I | add | more |
| 17 | next_state | = | random . choices ([ ' PUBLISH ', | ' | states | in | search | space | or | delete | one | state | in | the |  |  |  |  |
| 18 | elif | current_state | == | ' DISCONNECT ': | 8 | ` | " reason " | ` | : | A | concise | explanation | of | why | I | should | add |  |
| 21 | else : | To enhance exploration and prevent convergence to a local opti- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 22 | next_state | = | ' CONNECT ' | mum, we introduce controlled randomness into the loop by occa- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 23 | elif | current_state | == | ' PINGREQ ': | sionally re-initializing the model from the beginning, allowing the |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 24 | next_state | = | random . choices ([ ' DISCONNECT ', | ' | system to escape stagnant state configurations. (Note that this mech- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 25 | elif | current_state | == | ' PUBACK ': | anism is not illustrated in Figure 2.) The fuzzing loop continues until |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 26 | next_state | = | random . choices ([ ' PUBLISH ', | ' | a crash or critical fault is observed, ensuring prolonged exploration |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DISCONNECT '], | weights =[60 , | 40]) [0] | when necessary. When analyzing results, if adjustment is needed, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27 | we prompt the LLM to suggest a new state to add (from previously |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30 | states. These decisions are based on summarized feedback from |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 31 | if | random . random () | < | 0.5: | past executions, and each recommendation includes a justification |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 32 | break | to preserve model clarity. By integrating randomness and iterative |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 33 | adjustment, the loop strikes a balance between exploiting known |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 6

| Table 2: A summary of protocol implementations used in our | Modbus is an industrial control protocol based on function codes. |
| --- | --- |
| evaluation. “#Stars” indicates the number of GitHub stars (as | We selected Pymodbus [7] as the target implementation for Mod- |
| of July 2025). “Used in” denotes which research question(s) | bus in our evaluation. Pymodbus is a full-featured, open-source |
| (RQ1–RQ3) each implementation contributed to. | Modbus protocol stack written in Python, supporting both syn- |

Moquette MQTT Java 2382 RQ1

In this section, we describe our experimental design to evaluate

our ChatFuMe method. We propose the following three research

questions, concerning flexibility, effectiveness, and cost efficiency:

RQs they were used to evaluate. This setup helps ensure that Chat-

FuMe is not tied to any single protocol or implementation style,

MQTT is a lightweight publish-subscribe messaging protocol

commonly used in IoT systems. We evaluated our approach on three

6

chronous and asynchronous APIs. It provides built-in client and

external dependencies.

streaming music via DAAP, making it a versatile and realistic target

for fuzz testing. By incorporating OwnTone as our test subject,

implementations layered over HTTP.

RQ2. To evaluate the testing effectiveness of our approach, we

compare it against FUME, a model-based fuzzing technique ex-

sure and compare the number of test cases generated by each

in JavaScript.

ChatAFL [37], a recent LLM-guided protocol fuzzer. ChatAFL

| Name | Protocol | Language | #Stars | Used in | server simulators, payload builder/decoder functions, and supports |
| --- | --- | --- | --- | --- | --- |
| HMQ | MQTT | Go | 1359 | RQ1 | both standard and extended Modbus function codes with minimal |
| Mosquitto | MQTT | C | 9928 | RQ1 & RQ2 | DAAP is a binary protocol layered over HTTP used for media |
| Aedes | MQTT | JavaScript | 1873 | RQ2 | sharing. We chose OwnTone [36] as our DAAP server for evaluation. |
| Pymodbus | Modbus | Python | 2494 | RQ1 | OwnTone is an open-source media server written in C, designed |
| OwnTone | DAAP | C | 2287 | RQ1 & RQ3 | to serve audio content over the DAAP. It supports sharing and |
| 4 | Experimental Design | we demonstrate that our framework can handle binary protocol |  |  |  |
| • | RQ1 | : How flexible and effective is ChatFuMe in discovering | plicitly designed for MQTT. FUME combines mutation-based and |  |  |
| faults across different protocols and implementations? | generation-based fuzzing strategies and introduces Markov chains |  |  |  |  |
| • | RQ2 | : How does ChatFuMe compare to a prior model-based | to guide both payload mutation and generation. It models the |  |  |
| fuzzing method in protocol testing effectiveness? | fuzzing process as a finite Bernoulli process to explore MQTT pro- |  |  |  |  |
| • | RQ3 | : What are the characteristics of ChatFuMe in terms of | tocol behaviors and uncover vulnerabilities thoroughly. |  |  |
| token usage compared with an existing LLM-based fuzzer? | This research question is evaluated in two parts. First, we mea- |  |  |  |  |
| 4.1 | Systems Under Test and Baselines | method within a fixed time window, assessing the throughput and |  |  |  |
| We selected three network protocols and six real-world software | exploration capability of the fuzzers. Second, we analyze the crash |  |  |  |  |
| implementations in total, with varying levels of maturity and pop- | discovery speed, which is the rate at which each tool triggers a fault |  |  |  |  |
| ularity, as reflected by their GitHub star counts. Table 2 presents | or crash in the target protocol implementation. For the throughput |  |  |  |  |
| the statistics, including the protocol and programming language | comparison, we evaluate on Mosquitto. For the crash speed com- |  |  |  |  |
| they are based on, their popularity (GitHub stars), and the specific | parison, we use Aedes [6], a popular MQTT broker implemented |  |  |  |  |
| reinforcing its flexibility and practical applicability. | RQ3. | For token usage analysis, we compare our approach with |  |  |  |
| RQ1. | To demonstrate the flexibility and effectiveness of our ap- | leverages large language models trained on human-readable proto- |  |  |  |
| proach, we conduct experiments across three different protocol | col specifications to extract protocol message grammars and predict |  |  |  |  |
| implementations: MQTT, Modbus, and Digital Audio Access Pro- | stateful interactions. It uses LLMs to generate message sequences |  |  |  |  |
| tocol (DAAP). These protocols span different formats, transport | and detect states in protocol implementations, combining grammar |  |  |  |  |
| layers, and usage domains. The goal of this part of the experiment | construction with mutation and sequence prediction. We conduct a |  |  |  |  |
| is to demonstrate that ChatFuMe is not limited to any specific | comparison focused on: the total number of tokens consumed and |  |  |  |  |
| protocol or domain. | the number of LLM API calls required during the fuzzing process. |  |  |  |  |
| different MQTT broker implementations: HMQ [31], Moquette [3], | 4.2 | Our Implementation |  |  |  |
| and Mosquitto [5]. This demonstrates ChatFuMe’s flexibility across | ChatFuMe is primarily implemented in Python, with an emphasis |  |  |  |  |
| languages and ecosystems. HMQ is a high-performance MQTT bro- | on cost-efficiency and broad applicability. To maximize flexibility, |  |  |  |  |
| ker written in Go, designed for scalability and compatibility with | all experiments in RQ1 and RQ2 were conducted using GPT-4o-mini, |  |  |  |  |
| MQTT 3.1.1 and standard clients. Moquette is a lightweight, embed- | a lightweight language model that is readily interchangeable with |  |  |  |  |
| dable Java broker that supports MQTT versions 3 and 5, featuring | many popular alternatives on the market. This is made possible by |  |  |  |  |
| session expiration and topic aliasing. Finally, Mosquitto is a widely | our design choice to decompose the overall fuzzing workflow into |  |  |  |  |
| used C implementation that offers a compact MQTT broker and | smaller, modular tasks. This eliminates the need for large token |  |  |  |  |
| client suite. Testing across these diverse implementations helps es- | windows or high-capacity models. For RQ3, we additionally evalu- |  |  |  |  |
| tablish that ChatFuMe is protocol-agnostic and language-agnostic. | ated ChatFuMe using GPT-3.5 Turbo, which successfully handled |  |  |  |  |
| It is capable of handling varying runtime environments and code- | all required subtasks, further demonstrating the adaptability of |  |  |  |  |
| bases. | our approach to different LLM configurations. In all experiments, |  |  |  |  |

---

## Page 7

| the temperature parameter was set to 0.5 to introduce controlled | ChatFuMe is broadly applicable, capable of uncovering real-world |
| --- | --- |
| randomness and encourage diverse outputs from the LLM. | bugs, and cost-efficient in terms of token usage. |

We obtain the initial states and payload generators for MQTT,

is compact—just over 100 lines of code—yet effective.

RQ1. We ran each fuzzing campaign for five hours to allow suffi-

cient exploration while limiting the cost of LLM API calls due to

hardware and budget constraints.

To mitigate randomness, we ran both ChatFuMe and FUME for

and recorded the time it took for each to trigger the first crash.

cannot directly compare the number of test cases over a fixed time.

of LLM calls. To ensure a fair comparison, we use GPT-3.5 Turbo

instead of GPT-4o-mini in our evaluation.

Environment. All experiments were conducted on a virtual ma-

chine running Ubuntu 20.04. The VM was allocated 11.4 GB of

Metrics. Because ChatFuMe does not rely on instrumentation,

we do not report traditional code coverage metrics [16, 51]. For

the comparison in RQ2 regarding test case generation, we measure

of LLM API calls made.

7

known issues have been patched.

Listing 6 shows the buggy code we discovered in the HMQ MQTT

in Go, as method calls on a nil interface result in dereferencing a

nil pointer. This leads to a crash if the code path is ever executed

with a nil conn , which our generated input successfully triggered.

This example illustrates how ChatFuMe can uncover subtle but

2 if ! wsEnabled && conn != nil && conn . RemoteAddr () != nil

3 {

RemoteAddr () ))

5 }

nil

7 {

8 result = append ( result , zap . String (" addr " , wsConn .

Request () . RemoteAddr ))

9 }

proper handling of specific malformed or edge-case inputs and

reflect the method’s ability to exercise error-handling paths even

in well-established protocol libraries.

data [0:5])

The bug occurs in the Modbus implementation when parsing

| Modbus, and Digital Audio Access Protocol (DAAP) using the fol- | 5.1 | RQ1: Flexibility and Effectiveness Across |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lowing approach: | Protocol Implementations |  |  |  |  |  |  |  |  |  |  |
| • | For MQTT, we extracted protocol states directly from the | ChatFuMe successfully discovered multiple bugs across diverse |  |  |  |  |  |  |  |  |  |
| official specification[4] and adopted the existing payload | protocol implementations, demonstrating both effectiveness and |  |  |  |  |  |  |  |  |  |  |
| generator from FUME. | flexibility. Table 3 summarizes the 12 potential bugs discovered by |  |  |  |  |  |  |  |  |  |  |
| • | For Modbus, we similarly derived states from the official spec- | ChatFuMe across multiple protocol implementations. |  |  |  |  |  |  |  |  |  |
| ification [2]. To generate payloads, we provided ChatGPT | For the MQTT protocol, we evaluated three broker implementa- |  |  |  |  |  |  |  |  |  |  |
| with examples from the specification. ChatGPT generates a | tions: HMQ, Moquette, and Mosquitto. On HMQ, we identified a crit- |  |  |  |  |  |  |  |  |  |  |
| protocol-aware payload generator totaling 501 lines of code. | ical bug that causes the system to crash. On Moquette, ChatFuMe |  |  |  |  |  |  |  |  |  |  |
| • | For DAAP, which is layered over HTTP and features loosely | uncovered three distinct issues that trigger exceptions, though the |  |  |  |  |  |  |  |  |  |
| structured binary payloads, we used ChatGPT to create a | broker remains operational. No bugs were discovered in Mosquitto, |  |  |  |  |  |  |  |  |  |  |
| lightweight generator based on the specification[1] and in- | likely because we reused the payload generator from FUME, which |  |  |  |  |  |  |  |  |  |  |
| tegrated simple mutation strategies. The resulting generator | has already been used extensively to test Mosquitto, and most |  |  |  |  |  |  |  |  |  |  |
| 4.3 | Experimental Setup | broker. The issue lies in the conditional statement | conn != nil && |  |  |  |  |  |  |  |  |
| We designed fuzzing campaigns tailored to each research question | conn.RemoteAddr() != nil | . While it appears safe, calling | conn |  |  |  |  |  |  |  |  |
| while balancing resource constraints and consistency. | .RemoteAddr() | when | conn | is | nil | will still cause a runtime panic |  |  |  |  |  |
| RQ2. | We conducted a more controlled comparison with FUME. | critical edge-case bugs by exploring under-tested execution paths. |  |  |  |  |  |  |  |  |  |
| one hour, repeated across three independent trials, and measured | Listing 6: Buggy code in HMQ where line 2 contains a faulty |  |  |  |  |  |  |  |  |  |  |
| the total number of unique test cases, the total number of test cases | conditional check: calling | conn.RemoteAddr() | without ensuring |  |  |  |  |  |  |  |  |
| generated, the average test case length, and the new response found. | conn | is non- | nil | leads to a runtime panic. |  |  |  |  |  |  |  |
| To evaluate the crash discovery speed, we ran both tools three times | 1 | // | add | remote | connection | address |  |  |  |  |  |
| RQ3. | Since ChatAFL does not store all generated test cases, we | 4 | result | = | append ( result , | zap . Stringer (" addr " , | conn . |  |  |  |  |
| Therefore, we focus on comparing token usage and the number | 6 | else | if | wsEnabled | && | wsConn | != | nil | && | wsConn . Request () | != |
| memory, 4 CPU cores, and a 50 GB SCSI hard disk. The host ma- | For Modbus, we tested the Pymodbus implementation. Our ap- |  |  |  |  |  |  |  |  |  |  |
| chine is equipped with a 13th Gen Intel(R) Core(TM) i9-13900H @ | proach identified eight unique bugs, each causing exceptions with- |  |  |  |  |  |  |  |  |  |  |
| 2.60 GHz and 32 GB of RAM. All LLM calls in our experiments were | out crashing the system. They are all related to incorrect buffer |  |  |  |  |  |  |  |  |  |  |
| made via the OpenAI API. | lengths during binary unpacking. These exceptions point to im- |  |  |  |  |  |  |  |  |  |  |
| the total number of test cases generated, the number of unique | Listing 7: Buggy code in Pymodbus where line 1 attempts to |  |  |  |  |  |  |  |  |  |  |
| test cases, the average test case length, and the number of distinct | unpack 5 bytes from a buffer without validating its length, |  |  |  |  |  |  |  |  |  |  |
| responses discovered. For RQ3, we focus on efficiency metrics by | leading to a | struct.error | when the data is too short. |  |  |  |  |  |  |  |  |
| comparing the total number of LLM tokens used and the number | 1 | self . address , | count , | _byte_count | = | struct . unpack (" > HHB " , |  |  |  |  |  |
| 5 | Evaluation and Discussion | a request frame with an unexpected or malformed length. Specifi- |  |  |  |  |  |  |  |  |  |
| By evaluating across general-purpose protocols and comparing | cally, the code in Listing 7 attempts to unpack 5 bytes from the in- |  |  |  |  |  |  |  |  |  |  |
| with both traditional and LLM-based fuzzers, we demonstrate that | coming | data | buffer using | struct.unpack(">HHB", data[0:5]) | . |  |  |  |  |  |  |

---

## Page 8

Table 3: A summary of identified potential bugs by protocol, software, error type, and description.

| # | Protocol | Subject | Error Type | Description |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Modbus | PyModbus | struct.error | Buffer too small for | >HH | in | register_message.py:180 | . |
| 2 | Modbus | PyModbus | struct.error | Buffer too short for | >HHB | in | bit_message.py:134 | . |
| 3 | Modbus | PyModbus | struct.error | Buffer too short for | >H | in | file_message.py:238 | . |
| 4 | Modbus | PyModbus | struct.error | Buffer too short for | >BBB | in | mei_message.py:52 | . |
| 5 | Modbus | PyModbus | struct.error | Buffer too short for | >HH | in | bit_message.py:30 | . |
| 6 | Modbus | PyModbus | struct.error | Buffer too short | >HH | in | register_message.py:26 | . |
| 7 | Modbus | PyModbus | struct.error | Buffer too short for | >BHHH | in | file_message.py:61 | . |
| 8 | Modbus | PyModbus | struct.error | Buffer too short for | >HHB | in | register_message.py:225 | . |
| 9 | MQTT | HMP | nil pointer dereference | Crash if | conn.RemoteAddr() | is nil |  |  |
| 10 | MQTT | Moquette | IOException | Invalid MQTT message caused channel closure. |  |  |  |  |
| 11 | MQTT | Moquette | NullPointerException | Null access during | PUBLISH | message handling. |  |  |
| 12 | MQTT | Moquette | StacklessClosedChannelException | Connection closed before sending | CONNACK | . |  |  |

Table 4: The comparison of test-case generation between ChatFuMe and FUME over three runs (on Mosquitto).

ChatFuMe FUME

Run

Total Cases Unique Cases Avg. Length

| 1 | 3,333,073 | 1,796,307 | 127.06 |
| --- | --- | --- | --- |
| 2 | 2,125,908 | 1,179,660 | 137.91 |
| 3 | 1,610,051 | 899,816 | 144.34 |

indicates a missing length check before unpacking, which can cause

In the case of DAAP, we tested the OwnTone media server. Our

testing did not uncover new bugs. One challenge here is that DAAP

is layered over HTTP, and our system currently models only the

DAAP-specific parts, without generating complete HTTP requests.

Furthermore, OwnTone has already been tested by ChatAFL [37],

which may have addressed some common issues. Nevertheless,

ChatFuMe was still able to process and explore DAAP’s binary

structure with minimal manual adjustment, underlining its general

applicability.

To evaluate how our LLM-assisted fuzzing approach compares to

existing model-based fuzzers, we conducted a head-to-head compar-

consists of two parts: the first measures the ability of each tool to

total cases and nearly 1.8 million unique ones, whereas FUME

8

Total Cases Unique Cases Avg. Length

| 1,875,234 | 1,138,751 | 139.26 |
| --- | --- | --- |
| 1,874,732 | 1,137,339 | 135.46 |
| 1,519,627 | 925,739 | 129.8 |

2500

FUME 2389

2000

1500 1489

1022

1000 971

Time to First Crash (seconds)

500

0

Run 1 Run 2 Run 3

Run Index

Figure 3: The comparison of crash discovery time between

approach.

rare protocol behaviors.

| However, if the | data | is shorter than 5 bytes, it results in a | struct. | Crash Discovery Time on Aedes (Lower is Better) |  |
| --- | --- | --- | --- | --- | --- |
| error | with the message | unpack | requires a buffer of 5 bytes. This | ChatFuMe | 2168 |
| the program to crash or throw an exception at runtime. | 1664 |  |  |  |  |
| 5.2 | RQ2: Effectiveness vs. Model-Based Fuzzers | ChatFuMe and FUME over three runs (on Aedes). |  |  |  |
| ison with FUME, a domain-specific MQTT fuzzer. Our evaluation | test case diversity and generation throughput of our LLM-assisted |  |  |  |  |
| generate diverse and voluminous test cases within a fixed time bud- | While the average payload length varies slightly, both tools |  |  |  |  |
| get; the second assesses the efficiency of each method in triggering | produce messages of comparable size, indicating similar levels of |  |  |  |  |
| faults by comparing the time taken to induce a crash. | complexity in the generated data. This suggests that ChatFuMe is |  |  |  |  |
| Table 4 presents the test case generation results of our approach | not simply generating larger or noisier inputs to inflate test cover- |  |  |  |  |
| and FUME across three independent one-hour fuzzing runs on | age, but is instead producing diverse, well-formed messages that are |  |  |  |  |
| the Mosquitto MQTT broker. ChatFuMe consistently generates a | competitive in structure and semantics. Moreover, the consistently |  |  |  |  |
| higher number of total and unique test cases compared to FUME. | higher number of unique cases indicates broader exploration of the |  |  |  |  |
| For example, in the first run, ChatFuMe produced over 3.3 million | input space, which can lead to uncovering more edge cases and |  |  |  |  |
| generated only 1.8 million total cases and 1.1 million unique cases. | To assess crash discovery efficiency, we compared our LLM- |  |  |  |  |
| This trend holds across all three runs, demonstrating the higher | assisted fuzzer against FUME on the Aedes MQTT broker under |  |  |  |  |

---

## Page 9

| Table 5: The comparison of LLM token and API call usage | the dual-use nature of large language models, suggesting that fu- |
| --- | --- |
| between ChatFuMe and ChatAFL over a one-hour run. | ture work should consider safeguards and responsible deployment |

Method Tokens Used LLM Calls

vidual run, our approach detected faults faster (16m11s vs. 17m02s,

To assess the efficiency of ChatFuMe compared to existing LLM-

based fuzzing approaches, we conducted a one-hour experiment

using both ChatFuMe and ChatAFL. We measured the total num-

ber of tokens consumed and the number of LLM calls made during

the fuzzing process. As shown in Table 5, our approach consumed

only 5,980 tokens and made 16 LLM calls, while ChatAFL con-

sumed 216,596 tokens and issued 160 LLM calls in the same period.

This demonstrates that ChatFuMe is more token-efficient—using

roughly 36 times fewer tokens and 10 times fewer LLM calls—

making it more practical for long-running or cost-sensitive fuzzing

campaigns.

While the token and call statistics provide a clear comparison of

efficiency, it is important to note that a direct comparison of the

generated test cases between ChatFuMe and ChatAFL is limited

due to differences in how the two tools store their outputs. Specifi-

cally, ChatAFL only retains test cases that trigger new execution

and replay. Upon inspection of the test cases retained by ChatAFL,

we found that they primarily consisted of HTTP-like requests such

as GET and POST , which aligns with the nature of DAAP as an HTTP-

based protocol. In contrast, the test cases produced by ChatFuMe

are raw hexadecimal payloads that conform to the DAAP message

format.

Our findings suggest that LLMs can be used not only to auto-

9

practices.

level bugs: crashes or exceptions caused by malformed inputs. While

our method generates syntactically diverse and realistic messages, it

does not capture deeper semantic behaviors that may be necessary

issues. We mitigate this by confirming that crashes are triggered

Threat to external validity. Our evaluation focuses on a select set

of protocols (MQTT, Modbus, DAAP) and open-source implemen-

tations. While they cover multiple transport layers and application

domains, generalizing our results to all protocol-based software

may be limited. Proprietary systems, real-time protocols, or those

with more complex state machines may exhibit different behavior.

In some cases, the initial protocol specifications used by our

payload generator were derived from LLM output (e.g., ChatGPT).

While this allows automation, it also introduces potential inaccura-

cies or omissions compared to official standards. The effectiveness of

our fuzzing may partially rely on the correctness of LLM-generated

specifications, which may not generalize well to protocols with

complex or poorly documented semantics.

6 Related Work

Protocol implementation fuzzing is a testing technique that sys-

tematically sends malformed and unexpected inputs to network

protocol implementations to uncover bugs, vulnerabilities, or unex-

pected behavior. Fuzzing techniques in terms of input generation

are commonly categorized into generation-based and mutation-

based approaches. Generation-based fuzzing [14, 23, 41, 46] con-

structs inputs from predefined specifications, ensuring syntactic

model by analyzing traffic loads.

| ChatFuMe | 5,980 | 16 | Theat to construct validity. | One limitation of our method, com- |
| --- | --- | --- | --- | --- |
| ChatAFL | 216,596 | 160 | mon to many fuzzing techniques, is that it primarily exposes surface- |  |
| identical conditions over three trials. ChatFuMe located the first | to uncover subtle logic bugs. This may limit the types of vulner- |  |  |  |
| crash in an average of 1543.0 seconds, compared to 1691.7 seconds | abilities our tool can detect, potentially underestimating deeper |  |  |  |
| for FUME, which is an improvement of roughly 9%. In every indi- | security issues present in the target systems. |  |  |  |
| 24m50s vs. 27m44s, and 36m08s vs. 39m49s), demonstrating that our | Threat to internal validity. | Malformed inputs may not directly |  |  |
| LLM-guided sequence generation can accelerate the identification | cause some bugs discovered during fuzzing, but rather be caused |  |  |  |
| of critical vulnerabilities. | by unrelated factors such as system configuration or dependency |  |  |  |
| 5.3 | RQ3: Cost Efficiency vs. LLM-Based Fuzzers | deterministically with repeated inputs. |  |  |
| paths, whereas ChatFuMe stores all generated cases for analysis | 6.1 | Protocol Implementation Fuzzing |  |  |
| 5.4 | Discussion | correctness and compliance with the protocol. Mutation-based |  |  |
| Limitations. | We do not include an ablation study in this work | fuzzing [10, 29, 38, 40] modifies existing valid inputs to create test |  |  |
| because our goal is to minimize manual effort and demonstrate how | cases, relying on randomness or heuristics to explore unexpected |  |  |  |
| LLMs can be leveraged to model protocol structures with minimal | behaviors. A common approach for fuzzers to improve performance |  |  |  |
| human input automatically. Rather than manually deconstructing | on semantic constraints is to build a protocol communication model. |  |  |  |
| and varying components, our focus is on showcasing the feasibility | The model enables fuzzers to generate structured and context- |  |  |  |
| and effectiveness of using LLMs in a streamlined and integrated way. | sensitive message sequences. FUME [39] manually constructs a com- |  |  |  |
| The strength of our approach lies in its simplicity and automation. | munication model for MQTT and integrates generation-based and |  |  |  |
| We focus our evaluation on comparing the complete system against | mutation-based fuzzing in this model. There are some works that |  |  |  |
| established baselines, including traditional fuzzers and existing | use automated methods to build communication models [26, 34, 55]. |  |  |  |
| LLM-based methods. | For example, Pulsar [26] automatically builds a communication |  |  |  |
| mate the creation of fuzzers but also to generate malicious tools for | There are also several LLM-based fuzzers designed for testing |  |  |  |
| exploiting vulnerabilities. This highlights a broader concern about | protocol implementations. These approaches typically provide the |  |  |  |

---

## Page 10

| LLM with protocol inputs or documentation and prompt it to gen- | under test as a controlled object and the testing process as a feed- |
| --- | --- |
| erate test cases in the form of protocol payloads. ChatAFL [37] | back control loop. The central idea is to collect the outcome data |
| is a general fuzzing framework that directly uses LLM to extract | from the executed test cases. For instance, in the Controlled Markov |
| information and generate initial inputs. In this framework, LLM | Chain model [30], the testing process is governed by an estimated |
| plays an important role in initializing the seed of fuzzing and pro- | state, and optimal actions are selected to meet reliability goals with |
| vides guidance for mutation based on coverage. However, ChatAFL | minimal resource consumption. |
| is primarily designed for string-based protocol implementations, | Our method incorporates the idea of feedback-guided testing |
| leveraging the strengths of LLMs in understanding and generat- | by using LLMs to iteratively adjust the input generator based on |
| ing structured text data. mGPTFuzz [35] is an LLM-based fuzzing | feedback from previous test executions. We adapt the generator |
| framework for Matter IoT Devices [8]. In mGPTFuzz’s fuzzing loop, | by modifying protocol states or transitions, allowing the fuzzer to |
| LLM is first asked to extract information from Matter’s specifica- | explore diverse and previously untested behaviors. This approach |
| tion. Users then prompt the LLM to build finite state machines | brings the principles of ART into the LLM era, enabling automated, |
| (FSMs) based on the extracted information. Finally, it generates | feedback-driven refinement of test strategies in a structured and |
| inputs based on FSMs and a user-defined policy. LLMIF [49] is an | scalable way. |

LLM-based fuzzing framework for Zigbee IoT devices [27], utilizing

LLM in the process of protocol information extraction and response

reasoning.

across multiple tasks in software engineering [32, 33, 45]. By lever-

aging their ability to understand and generate code, LLMs can help

SymPrompt reaches higher code coverage in several open-source

Python projects.

our method finally generates protocol message payloads that must

dling stateful interactions and semantic constraints unique to net-

traditional static testing methods, this approach treats the software

10

7 Conclusion

compared to other LLM-based fuzzers, highlighting its efficiency

and practicality. This study illustrates the potential of large lan-

References

[Accessed 17-07-2025].

moquette/. [Accessed 19-07-2025].

[Accessed 14-07-2025].

[5] 2025. Eclipse Mosquitto — mosquitto.org. https://mosquitto.org/. [Accessed

19-07-2025].

[Accessed 19-07-2025].

19-07-2025].

[8] Connectivity Standards Alliance. 2023. Matter Specification Version 1.2. https://

cessed 27-05-2025].

[9] Max Ammann, Lucca Hirschi, and Steve Kremer. 2024. DY fuzzing: formal Dolev-

Machiry, and James C Davis. 2023. Systematically detecting packet validation

vulnerabilities in embedded network stacks. In 2023 38th IEEE/ACM International

Conference on Automated Software Engineering (ASE) . IEEE, 926–938.

proving TCP/IP performance over wireless networks. In Proceedings of the 1st

Hauck, and Gerhard Habiger. 2021. A survey on resilience in the iot: Taxonomy,

(CSUR) 54, 7 (2021), 1–39.

| Our work differs from existing approaches in several ways. Com- | In this work, we propose a novel LLM-assisted fuzzing method |  |
| --- | --- | --- |
| pared to manually crafted model-based fuzzers and protocol-specific | ChatFuMe that automates protocol modeling and test case genera- |  |
| LLM-based fuzzes like mGPTFuzz, our method uses LLMs to au- | tion with minimal manual effort. ChatFuMe demonstrates strong |  |
| tomatically build and adapt different protocol models, making it | flexibility across multiple protocols and is effective in identifying |  |
| more general and less dependent on expert input. In contrast to | real-world bugs in diverse software systems. Through extensive |  |
| LLM-based fuzzers that directly generate individual test cases, our | evaluation, we show that our approach generates more diverse |  |
| method uses the LLM to program a protocol-aware sequence gen- | and higher-volume test cases than traditional fuzzers, while being |  |
| erator, providing better control over input structure and reducing | significantly more efficient in discovering crashes. Moreover, our |  |
| token consumption. | method achieves these results using far fewer LLM tokens and calls |  |
| 6.2 | LLM in Testing | guage models to streamline and enhance fuzz testing, opening new |
| Large language models (LLMs) have shown strong performance | directions for intelligent and automated software testing. |  |
| identify edge cases, create meaningful test inputs, and detect poten- | [1] [n. d.]. GitHub - bjoernricks/daap-protocol: Digital Audio Access Protocol (DAAP) |  |
| tial vulnerabilities. Fuzz4all[52] is a universal fuzzing framework | documentation — github.com. | https://github.com/bjoernricks/daap-protocol. |
| for compiler testing. It outperforms different baseline tools in 6 dif- | [2] [n. d.]. Modbus Specifications and Implementation Guides — modbus.org. https: |  |
| ferent programming languages. Whitefox [53] is a white-box fuzzer | //www.modbus.org/specs.php. [Accessed 17-07-2025]. |  |
| for testing logic bugs. SymPrompt[44] presents a prompting strat- | [3] [n. d.]. Moquette Broker — moquette-io.github.io. https://moquette-io.github.io/ |  |
| egy for test generation. By implementing a multi-stage workflow, | [4] [n. d.]. MQTT Specification — mqtt.org. https://mqtt.org/mqtt-specification/. |  |
| Our work differs from existing LLM-based fuzzers in other do- | [6] 2025. | GitHub - moscajs/aedes: Barebone MQTT broker that can run on any |
| mains, such as compiler testing or code-based test generation, by | stream server, the node way — github.com. https://github.com/moscajs/aedes. |  |
| focusing on general protocol implementation fuzzing. Unlike those | [7] 2025. GitHub - pymodbus-dev/pymodbus: A full modbus protocol written in |  |
| approaches that typically generate code or API calls as test cases, | python — github.com. https://github.com/pymodbus-dev/pymodbus. [Accessed |  |
| conform to specific communication sequences. This requires han- | csa-iot.org/wp-content/uploads/2023/10/Matter-1.2-Core-Specification.pdf. [Ac- |  |
| work protocols, which we address by using LLMs to model protocol | Yao models meet cryptographic protocol fuzz testing. In | 2024 IEEE Symposium on |
| behavior and guide input generation, rather than producing test | Security and Privacy (SP) | . IEEE, 1481–1499. |
| cases directly. | [10] Paschal C Amusuo, Ricardo Andrés Calvo Méndez, Zhongwei Xu, Aravind |  |
| 6.3 | Feedback-Guided Testing | [11] Hari Balakrishnan, Srinivasan Seshan, Elan Amir, and Randy H Katz. 1995. Im- |
| Feedback-guided testing [18] is a software cybernetics [19] ap- | annual international conference on Mobile computing and networking | . 2–11. |
| proach to software testing where test strategies evolve dynamically | [12] Christian Berger, Philipp Eichhammer, Hans P Reiser, Jörg Domaschka, Franz J |  |
| based on real-time feedback from previous test executions. Unlike | classification, and discussion of resilience mechanisms. | ACM Computing Surveys |

---

## Page 11

| [13] Tim Berners-Lee, Roy Fielding, and Henrik Frystyk. 1996. RFC1945: Hypertext | [37] Ruijie Meng, Martin Mirchev, Marcel Böhme, and Abhik Roychoudhury. 2024. |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Transfer Protocol–HTTP/1.0. | Large language model guided protocol fuzzing. In | Proceedings of the 31st Annual |  |  |  |
| [14] Benjamin Beurdouche, Karthikeyan Bhargavan, Antoine Delignat-Lavaud, Cédric | Network and Distributed System Security Symposium (NDSS) | , Vol. 2024. |  |  |  |
| Fournet, Markulf Kohlweiss, Alfredo Pironti, Pierre-Yves Strub, and Jean Karim | [38] Roberto Natella. 2022. Stateafl: Greybox fuzzing for stateful network servers. |  |  |  |  |
| Zinzindohoue. 2017. A messy state of the union: Taming the composite state | Empirical Software Engineering | 27, 7 (2022), 191. |  |  |  |
| machines of TLS. | Commun. ACM | 60, 2 (2017), 99–107. | [39] Bryan Pearson, Yue Zhang, Cliff Zou, and Xinwen Fu. 2022. | Fume: Fuzzing |  |
| [15] SIG Bluetooth. 2010. Bluetooth Specification Version 2.0. | http://www. bluetooth. | message queuing telemetry transport brokers. In | IEEE INFOCOM 2022-IEEE Con- |  |  |
| com/ | (2010). | ference on Computer Communications | . IEEE, 1699–1708. |  |  |
| [16] Marcel Böhme, László Szekeres, and Jonathan Metzman. 2022. On the reliability | [40] Van-Thuan Pham, Marcel Böhme, and Abhik Roychoudhury. 2020. Aflnet: A |  |  |  |  |
| of coverage-based fuzzer benchmarking. In | Proceedings of the 44th International | greybox fuzzer for network protocols. In | 2020 IEEE 13th International Conference |  |  |
| Conference on Software Engineering | . 1621–1633. | on Software Testing, Validation and Verification (ICST) | . IEEE, 460–465. |  |  |
| [17] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, | [41] Gaganjeet Singh Reen and Christian Rossow. 2020. DPIFuzz: a differential fuzzing |  |  |  |  |
| Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda | framework to detect DPI elusion strategies for QUIC. In | Proceedings of the 36th |  |  |  |
| Askell, et al. 2020. Language models are few-shot learners. | Advances in neural | Annual Computer Security Applications Conference | . 332–344. |  |  |
| information processing systems | 33 (2020), 1877–1901. | [42] Mengfei Ren, Xiaolei Ren, Huadong Feng, Jiang Ming, and Yu Lei. 2021. Z-fuzzer: |  |  |  |
| [18] Kai-Yuan Cai. 2002. Optimal software testing and adaptive software testing in | Device-agnostic fuzzing of zigbee protocol implementation. In | Proceedings of the |  |  |  |
| the context of software cybernetics. | Information and Software Technology | 44, 14 | 14th ACM Conference on Security and Privacy in Wireless and Mobile Networks | . |  |
| (2002), 841–855. | 347–358. |  |  |  |  |
| [19] Kai-Yuan Cai, João W Cangussu, Raymond A DeCarlo, and Aditya P Mathur. 2003. | [43] Jan Ruge, Jiska Classen, Francesco Gringoli, and Matthias Hollick. 2020. Franken- |  |  |  |  |
| An overview of software cybernetics. In | Eleventh Annual International Workshop | stein: Advanced wireless fuzzing to exploit new bluetooth escalation targets. In |  |  |  |
| on Software Technology and Engineering Practice | . IEEE, 77–86. | 29th USENIX Security Symposium (USENIX Security 20) | . 19–36. |  |  |
| [20] Joeri De Ruiter and Erik Poll. 2015. Protocol state fuzzing of | { | TLS | } | implementa- | [44] Gabriel Ryan, Siddhartha Jain, Mingyue Shang, Shiqi Wang, Xiaofei Ma, Mu- |
| tions. In | 24th USENIX Security Symposium (USENIX Security 15) | . 193–206. | rali Krishna Ramanathan, and Baishakhi Ray. 2024. Code-aware prompting: A |  |  |
| [21] Dongliang Fang, Zhanwei Song, Le Guan, Puzhuo Liu, Anni Peng, Kai Cheng, | study of coverage-guided test generation in regression setting using llm. | Pro- |  |  |  |
| Yaowen Zheng, Peng Liu, Hongsong Zhu, and Limin Sun. 2021. Ics3fuzzer: A | ceedings of the ACM on Software Engineering | 1, FSE (2024), 951–971. |  |  |  |
| framework for discovering protocol implementation bugs in ics supervisory soft- | [45] Max Schäfer, Sarah Nadi, Aryaz Eghbali, and Frank Tip. 2023. | An empirical |  |  |  |
| ware by fuzzing. In | Proceedings of the 37th Annual Computer Security Applications | evaluation of using large language models for automated unit test generation. |  |  |  |
| Conference | . 849–860. | IEEE Transactions on Software Engineering | 50, 1 (2023), 85–105. |  |  |
| [22] Paul Fiterau-Brostean, Bengt Jonsson, Robert Merget, Joeri De Ruiter, Konstanti- | [46] Juraj Somorovsky. 2016. | Systematic fuzzing and testing of TLS libraries. In |  |  |  |
| nos Sagonas, and Juraj Somorovsky. 2020. Analysis of | { | DTLS | } | implementations | Proceedings of the 2016 ACM SIGSAC conference on computer and communications |
| using protocol state fuzzing. In | 29th USENIX Security Symposium (USENIX Security | security | . 1492–1504. |  |  |
| 20) | . 2523–2540. | [47] Dipa Soni and Ashwin Makwana. 2017. A survey on mqtt: a protocol of internet |  |  |  |
| [23] Paul Fiterau-Brostean, Bengt Jonsson, Konstantinos Sagonas, and Fredrik Tåquist. | of things (iot). In | International conference on telecommunication, power analysis |  |  |  |
| 2023. Automata-Based Automated Detection of State Machine Bugs in Protocol | and computing techniques (ICTPACT-2017) | , Vol. 20. |  |  |  |
| Implementations.. In | NDSS | . | [48] George Thomas. 2008. Introduction to the modbus protocol. | The Extension | 9, 4 |
| [24] Matheus E Garbelini, Vaibhav Bedi, Sudipta Chattopadhyay, Sumei Sun, and | (2008), 1–4. |  |  |  |  |
| Ernest Kurniawan. 2022. | { | BrakTooth | } | : Causing havoc on bluetooth link manager | [49] Jincheng Wang, Le Yu, and Xiapu Luo. 2024. Llmif: Augmented large language |
| via directed fuzzing. In | 31st USENIX Security Symposium (USENIX Security 22) | . | model for fuzzing iot devices. In | 2024 IEEE Symposium on Security and Privacy |  |
| 1025–1042. | (SP) | . IEEE, 881–896. |  |  |  |
| [25] Matheus E Garbelini, Chundong Wang, and Sudipta Chattopadhyay. 2020. Grey- | [50] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, |  |  |  |  |
| hound: Directed greybox wi-fi fuzzing. | IEEE Transactions on Dependable and | Aakanksha Chowdhery, and Denny Zhou. 2022. Self-consistency improves chain |  |  |  |
| Secure Computing | 19, 2 (2020), 817–834. | of thought reasoning in language models. | arXiv preprint arXiv:2203.11171 | (2022). |  |
| [26] Hugo Gascon, Christian Wressnegger, Fabian Yamaguchi, Daniel Arp, and Konrad | [51] Anjiang Wei, Yinlin Deng, Chenyuan Yang, and Lingming Zhang. 2022. Free |  |  |  |  |
| Rieck. 2015. Pulsar: Stateful black-box fuzzing of proprietary network protocols. | lunch for testing: Fuzzing deep-learning libraries from open source. In | Proceedings |  |  |  |
| In | Security and Privacy in Communication Networks: 11th EAI International Con- | of the 44th International Conference on Software Engineering | . 995–1007. |  |  |
| ference, SecureComm 2015, Dallas, TX, USA, October 26-29, 2015, Proceedings 11 | . | [52] Chunqiu Steven Xia, Matteo Paltenghi, Jia Le Tian, Michael Pradel, and Lingming |  |  |  |
| Springer, 330–347. | Zhang. 2024. Fuzz4all: Universal fuzzing with large language models. In | Pro- |  |  |  |
| [27] Drew Gislason. 2008. | Zigbee wireless networking | . Newnes. | ceedings of the IEEE/ACM 46th International Conference on Software Engineering | . |  |
| [28] Lav Gupta, Raj Jain, and Gabor Vaszkun. 2015. Survey of important issues in | 1–13. |  |  |  |  |
| UAV communication networks. | IEEE communications surveys & tutorials | 18, 2 | [53] Chenyuan Yang, Yinlin Deng, Runyu Lu, Jiayi Yao, Jiawei Liu, Reyhaneh Jab- |  |  |
| (2015), 1123–1152. | barvand, and Lingming Zhang. 2024. Whitefox: White-box compiler fuzzing |  |  |  |  |
| [29] Fengjiao He, Wenchuan Yang, Baojiang Cui, and Jia Cui. 2022. Intelligent fuzzing | empowered by large language models. | Proceedings of the ACM on Programming |  |  |  |
| algorithm for 5g nas protocol based on predefined rules. In | 2022 International | Languages | 8, OOPSLA2 (2024), 709–735. |  |  |
| Conference on Computer Communications and Networks (ICCCN) | . IEEE, 1–7. | [54] Xiaohan Zhang, Cen Zhang, Xinghua Li, Zhengjie Du, Bing Mao, Yuekang Li, |  |  |  |
| [30] Hai Hu, Chang-Hai Jiang, and Kai-Yuan Cai. 2008. Adaptive software testing in | Yaowen Zheng, Yeting Li, Li Pan, Yang Liu, et al. 2024. A survey of protocol |  |  |  |  |
| the context of an improved controlled Markov chain model. In | 2008 32nd Annual | fuzzing. | Comput. Surveys | 57, 2 (2024), 1–36. |  |
| IEEE International Computer Software and Applications Conference | . IEEE, 853–858. | [55] Hui Zhao, Zhihui Li, Hansheng Wei, Jianqi Shi, and Yanhong Huang. 2019. Seq- |  |  |  |
| [31] joy.zhou, chowyu, dependabot[bot], Lucas Vieira, spit4520, gerdstolpmann, | Fuzzer: An industrial protocol fuzzing framework from a deep learning perspec- |  |  |  |  |
| muXxer, Marc Magnin, Rajiv Shah, Thomas, TrickTt, Luca Moser, Ron Evans, | tive. In | 2019 12th IEEE Conference on software testing, validation and verification |  |  |  |
| Yog, chujiangke, foosinn, Jason, YangYuDong, winglq, Michael Stapelberg, Marc | (ICST) | . IEEE, 59–67. |  |  |  |

Magnin, Lijin, Husy, Jayden, Giovanni Rosa, Gary Barnett, and Aleksey Myas-

nikov. 2025. fhmq/hmq. https://github.com/fhmq/hmq. https://github.com/

fhmq/hmq

[32] Sungmin Kang, Gabin An, and Shin Yoo. 2024. A quantitative and qualitative

evaluation of LLM-based explainable fault localization. Proceedings of the ACM

on Software Engineering 1, FSE (2024), 1424–1446.

[33] Haonan Li, Yu Hao, Yizhuo Zhai, and Zhiyun Qian. 2024. Enhancing static

analysis for practical bug detection: An llm-integrated approach. Proceedings of

the ACM on Programming Languages 8, OOPSLA1 (2024), 474–499.

[34] Zhengxiong Luo, Feilong Zuo, Yu Jiang, Jian Gao, Xun Jiao, and Jiaguang Sun.

2019. Polar: Function code aware fuzz testing of ics protocol. ACM Transactions

on Embedded Computing Systems (TECS) 18, 5s (2019), 1–22.

[35] Xiaoyue Ma, Lannan Luo, and Qiang Zeng. 2024. From One Thousand Pages of

Specification to Unveiling Hidden Bugs: Large Language Model Assisted Fuzzing

of Matter { IoT } Devices. In 33rd USENIX Security Symposium (USENIX Security

24) . 4783–4800.

[36] OwnTone maintainers. 2025. OwnTone — owntone.github.io. https://owntone.

github.io/owntone-server/. [Accessed 19-07-2025].

11
