---year: 2022

secverify_category: "Category A"
categories:
  - "[[2A.1-Web與API動態漏洞掃描 (DAST)]]"
  - "[[1B.1-資料流分析 (Data Flow Analysis)]]"
title: "Driving Execution of Target Paths in Android Applications with (a) CAR"
author: "Michelle Y. Wong"
creator: "LaTeX with acmart 2021/09/24 v1.80 Typesetting articles for the Association for Computing Machinery and hyperref 2020-05-15 v7.00e Hypertext links for LaTeX"
pages: 15
source: "Target-Path-Method (2022) Driving Execution of Target Paths in Android Applications.pdf"
---

# Driving Execution of Target Paths in Android Applications with (a) CAR

> **文獻存檔**：[PDF 原文](<../../raw-papers/2022/Target-Path-Method (2022) Driving Execution of Target Paths in Android Applications.pdf>) | [Markdown 原文](<../../raw-papers/2022/Target-Path-Method (2022) Driving Execution of Target Paths in Android Applications (Raw).md>)

> **作者**：Michelle Y. Wong
> **總頁數**：15 頁

---

## Page 1

Session 7B: Software Security #2 ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan

Driving Execution of Target Paths in Android Applications with

(a) CAR

Michelle Y. Wong

University of Toronto

Toronto, Canada

ABSTRACT

context, which represents the program state expected by the path

program analysis; static analysis; dynamic analysis; malware detec-

tion; android malware; android security; mobile security; computer

security; symbolic execution

May 30-June 3, 2022, Nagasaki, Japan. ACM, New York, NY, USA, 15 pages.

https://doi.org/10.1145/3488932.3497765

on the first page. Copyrights for components of this work owned by others than the

and/or a fee. Request permissions from permissions@acm.org.

ASIA CCS ’22, May 30-June 3, 2022, Nagasaki, Japan

https://doi.org/10.1145/3488932.3497765

888

David Lie

University of Toronto

Toronto, Canada

1 INTRODUCTION

analyzed.

provide the information required for the dynamic analysis to reach

properties of the method’s parent object, as well as the properties

We represent a path’s dependencies through its context , which we

define as the constrained inputs and program state that satisfy these

dependencies and are required for the path to execute. However,

statically extracting the complete context does not scale [48, 49],

can also result in low coverage due to scalability issues, and they

cannot easily integrate with dynamic analysis tools that operate on

In this work, we propose a different approach, C ontext A pproxi-

| Dept. of Electrical and Computer Engineering | Dept. of Electrical and Computer Engineering |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Dynamic program analysis is commonly used to vet Android appli- | Mobile devices have become an intrinsic part of daily life and the |  |  |  |  |
| cations. One approach is targeted execution, in which interesting or | use of third-party applications on these devices provides a variety |  |  |  |  |
| suspicious code is specifically targeted and analyzed dynamically. | of beneficial functionality and services. With an estimated 2.8 mil- |  |  |  |  |
| However, faithful execution to just the paths that reach these targets | lion applications on the Google Play store, attackers who create |  |  |  |  |
| can be difficult due to the dependencies they have on other parts of | and distribute malicious applications (i.e. malware) for gain are |  |  |  |  |
| the application. Prior works that handle dependencies must favor | naturally drawn to such a large market and user base. To maintain |  |  |  |  |
| either soundness or completeness to the detriment of the other. | the security of their users, application marketplaces endeavor to |  |  |  |  |
| Techniques that rely on precise dependency tracking ultimately | remove malware from their offerings by analyzing submissions |  |  |  |  |
| result in lower coverage of targets due to overhead. Meanwhile, | to detect whether they perform any malicious behavior. Dynamic |  |  |  |  |
| other techniques that aim for completeness by ignoring or bypass- | program analysis techniques are commonly used to perform this |  |  |  |  |
| ing dependencies lead to unsound execution and false positives. | security analysis due to their precision, but they are limited by code |  |  |  |  |
| In this paper, we treat dependencies through the lens of a path | coverage since only code that is executed during testing can be |  |  |  |  |
| as it is executing. We propose an approach that provides better | A challenge to these analysis is scalability. Purely dynamic analy- |  |  |  |  |
| completeness and low false positives using Context Approximation | ses are generally unable to obtain significant code coverage on real |  |  |  |  |
| and Refinement (Car), which combines static constraint analysis | applications and may thus miss malicious functionality [2, 15, 20, 27, |  |  |  |  |
| and dynamic error recovery to infer a context based on the desired | 41]. An alternative approach is to guide the dynamic analysis with |  |  |  |  |
| path flow and refine it during execution. We show that the inte- | statically extracted information, so as to only execute sections of |  |  |  |  |
| gration of Car with targeted execution can reach 3.1× more target | the application that are likely to contain malicious code [7, 48, 49]. |  |  |  |  |
| locations in popular Android applications than the existing state | Critical to the success of such approaches is the precision and scal- |  |  |  |  |
| of the art while having a false detection rate of 9%, enabling more | ability of the static analysis component—an overly precise static |  |  |  |  |
| complete analysis and detection of security-sensitive behaviors. | analysis will not scale, while an overly imprecise analysis may not |  |  |  |  |
| CCS CONCEPTS | and execute malicious code, thus preventing it from detecting the |  |  |  |  |
| • | Security and privacy | → | Software reverse engineering | ; Software | malicious code. In particular, paths in Android applications may |
| security engineering; | Malware and its mitigation | . | depend not only on the inputs to the entry point method, but on the |  |  |
| KEYWORDS | of other objects in the application. |  |  |  |  |
| ACM Reference Format: | resulting in an incomplete context and the inability to execute and |  |  |  |  |
| Michelle Y. Wong and David Lie. 2022. Driving Execution of Target Paths | dynamically analyze application paths. Guided symbolic execu- |  |  |  |  |
| in Android Applications with (a) CAR. In | Proceedings of the 2022 ACM | tion [5, 30, 53] can resolve path dependencies as they arise but |  |  |  |
| Asia Conference on Computer and Communications Security (ASIA CCS ’22), | requires expensive symbolic tracking of all program state, which |  |  |  |  |
| Permission to make digital or hard copies of all or part of this work for personal or | concrete execution. Other work that ignore context altogether by |  |  |  |  |
| classroom use is granted without fee provided that copies are not made or distributed | skipping the parts of the path that enforce the dependencies (e.g. |  |  |  |  |
| for profit or commercial advantage and that copies bear this notice and the full citation | through instrumented forced branching [34, 46] or arbitrary invo- |  |  |  |  |
| author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or | cation [32]) can lead to the execution of unsound (i.e. infeasible) |  |  |  |  |
| republish, to post on servers or to redistribute to lists, requires prior specific permission | paths, resulting in many false positives. |  |  |  |  |
| © 2022 Copyright held by the owner/author(s). Publication rights licensed to ACM. | mation and | R | efinement (Car), to achieve a balance between forced |  |  |
| ACM ISBN 978-1-4503-9140-5/22/05. . . $15.00 | execution, which produces unsound paths, and complete context |  |  |  |  |

---

## Page 2

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | class | EnterKeyListener | implements | View . OnKeyListener | { | 32 | /* | Secondary | activity | in | the | application | */ |
| 2 | @ Override | 33 | class | InnerActivity | extends | Activity | { |  |  |  |  |  |  |
| 3 | public | void | onKey( View | v , | int | code , | KeyEvent | event ) | { | 34 | @ Override |  |  |
| 4 | if | ( code | == | KeyEvent . KEYCODE_ENTER ) | { | 35 | public | onResume( Bundle | savedInstanceState ) | { |  |  |  |
| 5 | handleEnterKey (v , | event ); | 36 | View | view | = | new | UserInputText (...) ; |  |  |  |  |  |
| 6 | } | } | 37 | View . OnKeyListener | listen | = | new | EnterKeyListener () ; |  |  |  |  |  |
| 7 | private | void | handleEnterKey( View | v , | KeyEvent | event ) | { | 38 | process ( view , | listen ); |  |  |  |

8 UserInputText textView = ( UserInputText )v;

11 class UserInputText extends EditText {

| 12 | static | public | String | keyword | = | null ; |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | int | detectionMode | = | 0; |  |  |  |
| 14 | public | List < String > | detectedInput | = | null ; |  |  |
| 17 | if | ( detectionMode | == | 2 | && | detectMode2 () ) | { |
| 18 | recordInput ( getText () ); |  |  |  |  |  |  |
| 19 | <target sensitive action> |  |  |  |  |  |  |
| 20 | } | else | { | ... | } |  |  |
| 21 | } |  |  |  |  |  |  |
| 30 | write (< output | file >, | detectedInput ); |  |  |  |  |

31 } }

Figure 1: Example of targeting sensitive behavior in an Android application

bination of static constraint analysis and dynamic error recovery

can approximate a context for a path such that execution is driven

to the target code location. The approximation is constructed to re-

duce the amount of false positives, which we define as the execution

of unsound paths. Car achieves this by: (1) generating an initial

context inferred from the desired control flow and (2) dynamically

configurable set of behaviors. The paths are then executed dynami-

approximated contexts for targeted dynamic analysis enables much

higher coverage of target code locations in applications, including

accesses to sensitive device functionality for security analysis.

889

39

| 42 | process ( view , | listen ); |
| --- | --- | --- |
| 43 | ... |  |
| 44 | } |  |

45

| 48 | v. setOnKeyListener (k) }; |
| --- | --- |
| 49 | } |

50

51 ...

52

61 } }

62 }

targeted execution.

(3) We evaluate Car on the most popular applications in Google

Play and show that it is able to reach 3.1× more non-trivial

target locations for an application than the existing state of

the art, with a false detection rate of 9.0%.

In Figure 1, we present an example of a code path to a sensitive

behavior in an Android application, in which the execution of the

path depends on data from other parts of the application. While this

is not extracted from a real application, it contains code patterns

similar to what we have seen.

detected within the user’s text input after the user presses the “enter”

| 9 | textView . checkText () ; | 40 | view | = | new | OtherTextView (...) ; |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | } | } | 41 | listen | = | new | OtherKeyListener () ; |  |  |  |  |  |  |  |  |
| 15 | ... | 46 | private | void | process( View | v , | View . OnKeyListener | k) | { |  |  |  |  |  |  |
| 16 | public | void | checkText() | { | 47 | /* | Register | a | key | event | handler | for | the | view | */ |
| 22 | private | boolean | detectMode2 () | { | 53 | /* | Called | by | an | SMS | receiver | elsewhere | ( not | shown ) | */ |
| 23 | return | hasKeyword () | && | keyword . equals ( getText () ); | 54 | public | void | onSmsReceived( SmsMessage | msg ) | { |  |  |  |  |  |
| 24 | } | 55 | if | ( msg . getOriginatingAddress () . equals ( |  |  |  |  |  |  |  |  |  |  |  |
| 25 | private | boolean | hasKeyword () | { | 56 | ServerInfo . getAddress () )) | { |  |  |  |  |  |  |  |  |
| 26 | return | keyword | != | null | && | ! keyword . isEmpty () ; | 57 | UserInputText | view | = | findViewById (...) ; |  |  |  |  |
| 27 | } | 58 | view . detectionMode | = | extractMode ( msg ); |  |  |  |  |  |  |  |  |  |  |
| 28 | private | void | recordInput ( String | text ) | { | 59 | view . detectedInput | = | new | ArrayList < String >() ; |  |  |  |  |  |
| 29 | detectedInput . add ( text ); | 60 | UserInputText . keyword | = | extractKeyword ( msg ); |  |  |  |  |  |  |  |  |  |  |
| (a) Target path that performs a sensitive action when a keyword is | (b) Dependent code paths that register the key event handler with |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| detected in the user’s input after they press the “enter” key | the framework and set the heap variables to their expected state |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| extraction, which does not scale. Rather than tracking dependent | (2) We design and implement Car for Android application anal- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| paths precisely or ignoring them altogether, we show how the com- | ysis to show how context approximation can be used for |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| refining the incomplete context when any unresolved dependencies | (4) We show that the use of approximated contexts for path |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| trigger errors during the path’s execution. The hybrid approach | driving can uncover a variety of security-sensitive behaviors |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| to dependency resolution enables Car address the trade-offs that | in both benign and malicious applications. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| must be made in static dependency tracking between precision, | We begin by providing background on the challenges of isolated |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| completeness, and scalability. Through the combination of static | path execution in Android in Section 2. We then present our design |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and dynamic resolution, we can achieve much greater coverage of | for Car in Section 3 and provide implementation details in Section 4. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| target behaviors in an application while maintaining reasonable | We evaluate Car on popular applications from Google Play in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| soundness in the paths that are executed. | Section 5 and compare it against several state-of-the-art dynamic |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| We implement Car on an existing Android targeted execution | tools. We discuss our limitations in Section 6 and the related work |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| framework, Tiro [49], which statically extracts target paths for a | in Section 7. Finally, we conclude in Section 8. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cally to trigger and analyze the behaviors. We show that the use of | 2 | MOTIVATING EXAMPLE |  |  |  |  |  |  |  |  |  |  |  |  |  |
| We make four main contributions: | Figure 1(a) shows a sensitive action taken when a keyword is |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (1) We describe Car, which effectively resolves dependencies | button. The key event handler ( | EnterKeyListener | ) is the entry- |  |  |  |  |  |  |  |  |  |  |  |  |
| for an targeted code path by approximating and refining its | point of this path. It first checks if the key pressed is the “enter” |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| expected context through hybrid static and dynamic analysis. | key and if so, it calls | UserInputText | , a custom UI text element, to |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 3

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| check the user’s input text. It determines whether a keyword has | constraint solving time. Decreasing breadth while maintaining com- |  |  |  |  |
| been loaded, checks it against the user’s input, and saves the input | plexity maintains precision, but limits the types of paths that can be |  |  |  |  |
| text if the keyword was detected. Finally, it performs a sensitive | analyzed dynamically. For instance, IntelliDroid does not support |  |  |  |  |
| action if these conditions have been met (e.g. it may send the input | the injection of UI events, which precludes it from triggering paths |  |  |  |  |
| text to a network server or access a device sensor). | in most Android applications (it would also be unable to inject the |  |  |  |  |
| If we wished to target the sensitive action and trigger it dynami- | UI key event in our example). In contrast, reducing complexity by |  |  |  |  |
| cally, the call path that reaches the target is: | discarding paths with unsupported operations or excessive length |  |  |  |  |
| 1) | EnterKeyListener::onKey() | reduces completeness. |  |  |  |
| 2) | EnterKeyListener::handleEnterKey() | One solution might be to decrease the amount of dependency |  |  |  |
| 3) | UserInputText::checkText() | tracking required, enabling greater coverage of target code in exe- |  |  |  |
| 4) | <target sensitive action> | cution (i.e. completeness). GroddDroid [1], Harvester [34], Direct- |  |  |  |
| Based on the path constraints, we can surmise that the path depends | Droid [46], and Ares [6] operate on path slices leading to target |  |  |  |  |
| on its inputs, heap state, and Android framework state. | code locations (i.e. they abstract at the instruction level). To guide |  |  |  |  |
| Figure 1(b) shows how the non-input dependencies are normally | execution, they use static instrumentation to force specific branch |  |  |  |  |
| satisfied by the execution of other application paths. For example, | outcomes. Instead of resolving dependencies, this essentially by- |  |  |  |  |
| onSmsReceived | should be executed (with appropriate context) be- | passes them since the branch conditions are no longer enforced. |  |  |  |
| fore | checkText | in the target path is executed. Furthermore, there | Forcing branch outcomes and ignoring their dependencies can en- |  |  |
| may be recursive constraints or dependencies in the dependent | sure that target paths are executed in full; however, this can easily |  |  |  |  |
| paths; for instance, the | detectionMode | and | keyword | fields are set | lead to inconsistent data values such as the forcing of the null check |
| on receipt of an SMS message from a certain address, which might | in Line 26. This leads to an inconsistency if the checked object is |  |  |  |  |
| be set in yet another dependent path. Likewise, the enclosing com- | actually null, the branch is forced anyway, and the object is then |  |  |  |  |
| ponent, | InnerActivity | , is not the application’s main activity and | dereferenced later in the line. Forcing of multiple branches can |  |  |
| may require navigation through multiple screens in the UI flow | also lead to a combination of infeasible branch outcomes, as pro- |  |  |  |  |
| before it can be started. | gram logic is modified without reconciling the control flow with |  |  |  |  |
| To execute the path in Figure 1(a), the path’s constraints must | the data compared within the branches. This can lead to the exe- |  |  |  |  |
| be resolved. A dynamic approach, such as guided symbolic execu- | cution of unrealistic or unsound paths. As such, forced execution |  |  |  |  |
| tion [5, 30, 53], would resolve dependencies along the target path | is well-suited for obtaining coverage but less so for the analysis |  |  |  |  |
| by symbolically tracking the input and non-input variables that are | of security-related behaviors, which usually require tracking how |  |  |  |  |
| accessed (e.g. | detectionMode | and | keyword | ). However, this track- | applications access and manipulate system resources and data. Due |
| ing is expensive and requires a symbolic execution environment | to soundness issues, it is not a reliable means for determining if an |  |  |  |  |
| that does not integrate easily with the numerous dynamic analysis | application will perform a malicious action. |  |  |  |  |
| tools are based on concrete execution [11, 14, 19, 42, 43, 51, 56]. | Other work, such as FuzzDroid [35] or CrashScope [28], abstracts |  |  |  |  |
| A hybrid approach could instead use static analysis to resolve de- | at the application level. FuzzDroid achieves semi-targeted execution |  |  |  |  |
| pendencies and guide concrete execution of the path [34, 35, 46, 48, | by manipulating the inputs received at application entry-points and |  |  |  |  |
| 49]. There are several methods of static guiding, which are differen- | framework APIs. However, it does not track or resolve dependencies |  |  |  |  |
| tiated by the execution abstraction used. A holistic abstraction that | on state within the application, such as the constraints on the |  |  |  |  |
| is faithful to normal execution (i.e. sound) is to abstract at the level | detectionMode | and | keyword | fields; it would have to execute the |  |
| of the Android framework, which manages the application’s execu- | dependent paths in order by chance to reach the target code location. |  |  |  |  |
| tion and facilitates access to underlying hardware. IntelliDroid [48] | This is also true for any other untargeted fuzzing tool. |  |  |  |  |
| and Tiro [49] guides execution by injecting events into the frame- | In Car, we propose a fully targeted approach that achieves a |  |  |  |  |
| work to trigger a target path. They use static dependency tracking | balance between forced branching, which is unsound, and full de- |  |  |  |  |
| to determine exactly which framework events to inject such that | pendency tracking across the Android system, which is unscalable. |  |  |  |  |
| the path’s constraints and dependencies are resolved. For Figure 1, | Instead, we target paths by abstracting at the level of code objects |  |  |  |  |
| they might execute the following ordered chain of events to reach | and guide execution by controlling the inputs, fields, and method |  |  |  |  |
| the target code: | return values accessed by a path. There are several advantages to |  |  |  |  |
| i) UI or lifecycle event(s) to start | InnerActivity | an object-level abstraction. First, abstracting at the granularity of |  |  |  |
| ii) Lifecycle event to register | EnterKeyListener | an object, as opposed to the entire Android framework, reduces |  |  |  |
| iii) SMS event with an input message that sets the required | dependencies on dynamic components like the underlying Android |  |  |  |  |
| values for | detectionMode | and | keyword | system, and allows injection of inputs and dependencies simply by |  |
| iv) UI key event for the target path from | onKey() | calling object methods or setting object properties without having |  |  |  |
| There are two drawbacks to this approach: (1) the breadth of | to understand Android framework APIs. Dependencies on state |  |  |  |  |
| the abstraction can be large and satisfying each dependency at run- | within the application and from the framework, such as heap vari- |  |  |  |  |
| time requires custom Android framework modifications for each | ables or API calls, are implicitly handled, as accesses to this state are |  |  |  |  |
| event type; and (2) the complexity of the abstraction can become | performed through field accesses and method invocations. Second, |  |  |  |  |
| excessive for long paths, requiring the tracking of a large number | unlike smaller abstractions such as a path slice, injecting and ma- |  |  |  |  |
| and variety of constraints, which may require models for complex | nipulating objects enables the full execution of methods in the path, |  |  |  |  |
| operations (i.e. string operation) and result in exponentially long | resulting in greater soundness. Also, the tracking of dependencies |  |  |  |  |

890

---

## Page 4

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| on object accesses ensures that the data accessed within a path is | the methods in the target call path as well as the auxiliary meth- |  |  |  |  |  |  |  |  |
| consistent. In our example from Figure 1(a), Car would trigger the | ods | detectMode2() | , | hasKeyword() | , | getText() | , | recordInput() | , |
| target path by injecting the input object | v | such that the constrained | write() | , and any other methods they may invoke. |  |  |  |  |  |
| field access to | v.detectionMode | is satisfied. It will also ensure that | A purely static analysis can sacrifice the precision of this anal- |  |  |  |  |  |  |
| the static field access to | UserInputText::keyword | is satisfied by | ysis for scalability such that constraints and dependencies can be |  |  |  |  |  |  |
| controlling the field value visible to the target path. | tracked across this sub-graph and across the application (albeit |  |  |  |  |  |  |  |  |

targeted execution framework for Android, Tiro [49]. It first con-

structs a conservative context-insensitive call-graph to find code

paths to a set of configurable target behaviors. We define a target

point to a target location, where an entry-point is any location

where normal execution can be transferred from Android frame-

work code to application code (e.g. a callback method). For each

path, a context- and flow-sensitive analysis extracts its constraints

on inputs, fields, and methods that define its execution. Constraints

on inputs can be resolved by injecting the path’s entry event with

values derived from the solved constraints. Constraints that cannot

be resolved through entry-point inputs (e.g. heap or framework

API values) form dependencies on other paths in the application.

haviors and the need for precision when extracting path constraints.

891

imprecisely). However, in a hybrid system where the static results

are then used to generate values for execution, this can result in

limitation. We directly address the trade-off between precision, com-

pleteness, and scalability by separating the dependency resolution

the code example in Figure 1.

approximated context

onKey handleEnter… checkText <target>

detectMode2

realized target path

hasKeyword getText keyword

realized modeled unconstrained recordInput …

| 3 | DESIGN | under-constrained program state that does not actually resolve a |  |
| --- | --- | --- | --- |
| Using the object-level abstraction for targeted execution, Car con- | path’s dependencies dynamically, resulting in the incomplete execu- |  |  |
| structs a context for a target path to resolve its dependencies on | tion of the path. For instance, the imprecise results of an any-path |  |  |
| inputs, fields, and methods. However, using static dependency track- | analysis may indicate that a constrained variable may have one of |  |  |
| ing to construct this context a priori can fail due to the trade-off | several values (due to the union of data flows from different paths) |  |  |
| between precision, completeness, and scalability. When this hap- | while only one of these values is actually valid for a particular |  |  |
| pens, the unresolved dependencies limit dynamic target coverage or | target path. Previous hybrid tools accounted for this by using a |  |  |
| lead to unsound paths. Car addresses this in a hybrid approach. We | different trade-off where precision is maintained but completeness |  |  |
| start from a set of statically extracted constraints that are necessar- | is heuristically scaled back: IntelliDroid [48] and Tiro [49] only |  |  |
| ily incomplete due to the trade-offs that must be made (Section 3.1). | perform constraint analysis on the methods directly in the target’s |  |  |
| We account for this by separating the constraint extraction and | call path and one level of auxiliary methods they invoke, and Har- |  |  |
| dependency resolution of a path into three levels of progressive | vester [34] uses a cut-off value to limit the depth of analysis into |  |  |
| approximation (realized, modeled, and unconstrained). Static con- | callers and callees when computing the path slice to force execute. |  |  |
| straints are used to infer an initial approximate context for the path. | Constraints imposed by code in deeper auxiliary/callee methods are |  |  |
| This context is constructed at run-time using a statically generated | ignored and unresolved. This is propagated when the constraints |  |  |
| path driving framework (Section 3.2). We then refine this context | are used to perform dependency tracking, resulting in unresolved |  |  |
| dynamically by monitoring for unresolved dependencies and re- | dependencies and incomplete execution of target paths. |  |  |
| solving them by re-using objects from the application’s execution | The key intuition behind Car’s design is that a combination of |  |  |
| (Section 3.3). | both static and dynamic techniques can be used to mitigate this |  |  |
| 3.1 | Static constraint analysis | of a target path into three levels of approximation, each of which |  |
| The initial static analysis to extract target paths uses an existing | are handled separately. This separation is illustrated in Figure 2 for |  |  |
| code path as the interprocedural control-flow path from an entry- | detectionMode |  |  |
| The separation of the initial path extraction from the constraint | Figure 2: Separation of the target path flow based on the ap- |  |  |
| analysis balances the need for coverage when detecting target be- | proximation level and scope of the constraint analysis |  |  |
| The precision required to determine the exact program values re- | The approximation is determined by the scope of the static con- |  |  |
| quired for the path (akin to symbolic execution) is expensive and | straint analysis (i.e. the depth of auxiliary methods analyzed). Meth- |  |  |
| impractical to perform over the entire application. The trade-off | ods that are within the scope form the | realized | path and are executed |
| between the precision and cost of this analysis impacts its complete- | in full with constrained inputs. Methods at the boundary of the |  |  |
| ness: to fully analyze all constraints, it requires performing precise | scope (they are invoked by realized methods but are themselves |  |  |
| symbolic constraint analysis over methods directly in the target’s | excluded from constraint analysis) are | modeled | if there are any con- |
| call path and all side/auxiliary methods they invoke; essentially, | straints on their return values. These constraints will be captured |  |  |
| this is comprises of the sub-graph of the call-graph starting at the | by the analysis performed on their realized caller methods. We treat |  |  |
| path’s entry-point, which can be prohibitively large. In our earlier | the constrained return values as part of the program state accessed |  |  |
| example from Figure 1, this would require constraint analysis over | by the path and encode them in the approximated context. |  |  |

---

## Page 5

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |  |  |
| --- | --- | --- | --- |
| All other methods that might be invoked by the target path are | similar to the generation of input values from constraints in sym- |  |  |
| unconstrained | . We execute them to ensure that any side effects are | bolic execution systems; however, in Car, we want to generate |  |
| performed and can be analyzed later, such as updates to persistent | the context for input and non-input variables, and enforce it as |  |  |
| storage or the scheduling of future tasks. These side effects are | the target path is executed concretely. Car uses a static phase that |  |  |
| essentially implicit dependencies that our object-level constraint | generates code to set up the context (which we call the path-driving |  |  |
| analysis does not track but that might affect the semantics of the | framework) and a dynamic phase that invokes the generated code |  |  |
| path. One might expect that it would also be beneficial to likewise | to produce the context at run-time. The majority of the work in |  |  |
| execute modelled methods and then force their return values to the | constructing the initial approximated context is therefore in the |  |  |
| constrained values. However, we find that this, similar to forced | static generation of the code in the path-driving framework. The |  |  |
| branching, results in inconsistencies between program state mod- | generation and invocation of this code is fully automated and is |  |  |
| ified by the method and its forced return value, and can lead to | performed for each target path. |  |  |
| excessive loss of analysis soundness. Unconstrained methods do | The path-driving framework consists of a test harness that sets |  |  |
| not need to have their return values forced. | up each path with classes, methods, and fields that contain the mod- |  |  |
| In Figure 2, which is based on a constraint analysis that ex- | eled values for the path. In addition to this context, the framework |  |  |
| tends to one level of auxiliary methods, the methods in the tar- | will directly invoke the path’s entry-point method to trigger the |  |  |
| get’s call path and the callee | v.detectMode2() | would be realized, | path. |

while v.hasKeyword() and v.getText() are modeled since they

| must return specific values for the path’s control flow. The method | 3.2.1 | Inferring and constructing the context. | For each variable in a |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| v.recordInput() | is unconstrained, as the realized path imposes | path’s constraints, we infer the context by encoding a value from |  |  |  |  |  |  |
| no constraints on its return value. | the solved constraints that can satisfy it—we refer to these as the |  |  |  |  |  |  |  |
| Any program state that influences the normal control flow of the | enforced context value for a given constrained variable. There can |  |  |  |  |  |  |  |
| realized path is handled by the context we generate from the con- | be many values that satisfy the constraints and therefore many |  |  |  |  |  |  |  |
| straint analysis. Therefore, the execution of unconstrained methods | feasible contexts, though we only generate one for each path. For |  |  |  |  |  |  |  |
| does not directly affect the realized path, except if an error occurs | Figure 1, a context that can satisfy the target path’s constraints |  |  |  |  |  |  |  |
| while the method is running. These errors, which will trigger unde- | might be: |  |  |  |  |  |  |  |
| sired exceptional control flow, arise due to unresolved dependencies | 𝑣 | = | UserInputText | { | detectionMode | = | 2 | , |
| (since constraint analysis was not performed for these methods). | hasKeyword | () | = | 𝑡𝑟𝑢𝑒, |  |  |  |  |
| Car handles these dependencies during execution through dynamic | getText | () | = | ” | a | ” | } |  |

context refinement, which tries to recover from the errors. We de-

𝑐𝑜𝑑𝑒 = KeyEvent . KEYCODE _ ENTER

scribe the refinement process in Section 3.3.

| The scope of the static constraint analysis and degree of path re- | 𝑒𝑣𝑒𝑛𝑡 | = | KeyEvent | { } |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| alization are configurable. Increasing it will result in greater sound- | 𝑈 𝑠𝑒𝑟𝐼𝑛𝑝𝑢𝑡𝑇 𝑒𝑥𝑡 | :: | 𝑘𝑒𝑦𝑤𝑜𝑟𝑑 | = | ” | a | ” |
| ness but requires more resources and can reduce coverage if the | To enforce context values when injecting the target path, Car |  |  |  |  |  |  |
| larger approximated context must satisfy constraints that cannot | considers whether they are input or non-input variables and whether |  |  |  |  |  |  |
| be resolved statically (e.g. a constrained encrypted value). Reducing | they are primitives or objects (we treat strings as primitive-like). |  |  |  |  |  |  |
| the scope will result in more unconstrained methods requiring dy- | The primary challenge is constraining accesses to objects. For ex- |  |  |  |  |  |  |
| namic context refinement, which is based on heuristics and can lead | ample, to enforce the context for Figure 1, we must inject the target |  |  |  |  |  |  |
| to the execution of unsound paths. In Car, we perform constraint | path with an object for the variable | v | such that when the path |  |  |  |  |
| analysis with one level of auxiliary methods which, from our cover- | accesses the field | detectionMode | at Line 17 and invokes the meth- |  |  |  |  |
| age and false positive results, achieves a good balance of soundness | ods | hasKeyword() | and | getText() | at Line 23, it receives the con- |  |  |
| and completeness through the size of the approximated context (i.e. | strained context values. To accomplish this, Car generates a | con- |  |  |  |  |  |
| number of solved constraints) and the amount of dynamic recovery. | strained subclass | for each constrained object, which is a modified |  |  |  |  |  |

version of the variable’s class type similar to the mock classes used

in unit testing [26]. Each constrained subclass is only used within

the context for one path for a particular constrained object vari-

| 3.2 | Generating an approximate context | able. Constraints placed on members of the object are handled by |  |
| --- | --- | --- | --- |
| While static constraint analysis can determine the values required | controlling method return and field values. Method return values |  |  |
| to resolve a path’s dependencies, concrete execution of the path re- | (i.e. for modeled methods) are handled by overriding the method |  |  |
| quires that these values be injected into application as it is running. | in the constrained subclass such that they return their context val- |  |  |
| The dependencies can include constrained inputs and global/system | ues. Field members are set to their context values in the subclass’s |  |  |
| state that the path accesses. To inject the constrained values for | constructor when the object is initialized. An example of the con- |  |  |
| concrete execution of the target path, Car uses the context to set | strained subclass generated for the input object for | v | in Figure 1 is |
| up the dependent state required. | shown in Figure 3(a). |  |  |

Given an extracted path, Car triggers the path dynamically by

| directly invoking its entry-point method. The path’s dependen- | 3.2.2 | Driving the target path. | In addition to initializing constrained |
| --- | --- | --- | --- |
| cies are resolved through a generated context that is automatically | variables with context values (either a solved primitive value or an |  |  |
| inferred from its constraints. The construction of the context is | instantiated constrained subclass object), they must be injected with |  |  |

892

---

## Page 6

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | class | ConstrainedUserInputText_Path0 | extends | without reaching the target sensitive location. Car handles un- |
| 2 | UserInputText | { | resolved dependencies by refining the path’s incomplete context |  |

| 3 | public | ConstrainedUserInputText_Path0 ( Context | c) | { |
| --- | --- | --- | --- | --- |
| 6 | } |  |  |  |
| 9 | } |  |  |  |
| 11 | return | "a"; |  |  |

(a) Constrained subclass enforced for the input object for v

| 14 | EnterKeyListener | receiver | = | new | EnterKeyListener () ; |
| --- | --- | --- | --- | --- | --- |
| 16 | int | arg2 | = | KeyEvent . KEYCODE_ENTER ; |  |
| 19 | UserInputText . keyword | = | "a"; |  |  |

22 }

text values as arguments to the invocation to the path’s entry-point

erated context. This can occur for the target path in Figure 1 for

893

the error to return to the target path.

3.3.1 Unresolved dependency monitoring. Unresolved dependency

IllegalStateException , which are thrown by the application af-

ArithmeticException can be thrown for divide-by-zero errors. In

strument the Android runtime’s (ART) exception handling code to

detect when common dependency-related exceptions occur while

such as IllegalState/ArgumentException , we perform partial

static information.

| 4 | super (c); | through dynamic dependency recovery. In essence, the dependen- |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | this . detectionMode | = | 2; | cies which could not be resolved through static means (i.e. tracked |  |  |  |  |  |  |
| 7 | @ Override | public | bool | hasKeyword () | { | by constraint analysis and resolved in the generated context) are |  |  |  |  |
| 8 | return | true ; | now handled by inferring them from the resulting dynamic de- |  |  |  |  |  |  |  |
| 10 | @ Override | public | String | getText () | { | pendency error. The refinement process is composed of two parts: |  |  |  |  |
| 12 | } | } | monitoring for unresolved dependency errors and recovering from |  |  |  |  |  |  |  |
| 13 | public | static | void | PathDriver0 | { | errors usually occur when an unconstrained input for the realized |  |  |  |  |
| 15 | View | arg1 | = | new | ConstrainedUserInputText_Path0 ( null ); | path (e.g. | detectedInput | in | arg1 | in Figure 3(b)) is passed to an |
| 17 | KeyEvent | arg3 | = | new | KeyEvent (0 , | 0) ; | unconstrained method that does impose a constraint. The most com- |  |  |  |
| 18 | /* | Constrain | global | heap | state | */ | mon error is a runtime-generated | NullPointerException | , mainly |  |
| 20 | /* | Inject | the | path | by | invoking | its | entry - point | */ | due to the default null values Car uses for unconstrained vari- |
| 21 | receiver . onKey ( arg1 , | arg2 , | arg3 ); | ables. Other common errors are | InvalidArgumentException | and |  |  |  |  |
| (b) Path driver method constructing the path’s context at run-time | ter a check for well-formed input. For primitive variables, a runtime |  |  |  |  |  |  |  |  |  |
| Figure 3: Path-driving framework automatically generated | general, technically any exception can be thrown by the application |  |  |  |  |  |  |  |  |  |
| by Car for the target path in Figure 1 | in response to unexpected (i.e. unresolved) program state. We in- |  |  |  |  |  |  |  |  |  |
| the target path. Input constraints are enforced by passing their con- | a path driver method is executing a target path. |  |  |  |  |  |  |  |  |  |
| method. Non-input constrained variables include accesses to static | 3.3.2 | Error recovery. | Recovery from a dependency error requires |  |  |  |  |  |  |  |
| fields and return values for static method invocations. For static | the identification of the error’s root cause, which is the dependent |  |  |  |  |  |  |  |  |  |
| fields, we explicitly set the field to its context value prior to inject- | variable that is incorrectly unconstrained during the execution of |  |  |  |  |  |  |  |  |  |
| ing the target path. For static methods, we instrument the method | an unconstrained method. For exceptions generated by the runtime, |  |  |  |  |  |  |  |  |  |
| to return the context value when the target path is executing and | such as | NullPointerException | , the root cause can be identified by |  |  |  |  |  |  |  |
| to invoke the method’s original functionality otherwise. | the runtime processes that generated the exception. For exceptions |  |  |  |  |  |  |  |  |  |
| To manage the constrained variables and context values, a central | that are thrown by the application, the cause of the exception is |  |  |  |  |  |  |  |  |  |
| path driver method is generated for each path to construct its | determined by the application itself (e.g. in a conditional branch |  |  |  |  |  |  |  |  |  |
| approximated context at run-time. When invoked, it instantiates | performing an error check) and the runtime environment only |  |  |  |  |  |  |  |  |  |
| the constrained subclasses, sets the input and non-input constrained | propagates the exception object. Therefore, to identify the root |  |  |  |  |  |  |  |  |  |
| variables, and injects the path’s entry-point method with initialized | cause, information from the application’s control and data flow |  |  |  |  |  |  |  |  |  |
| inputs. For unconstrained primitive inputs, they are set to zero or an | is required. This can be provided to Car’s dynamic refinement |  |  |  |  |  |  |  |  |  |
| empty string. If they are unconstrained objects, they are initialized | through an intraprocedural static analysis of | throw | instructions to |  |  |  |  |  |  |  |
| with an instantiated object of the declared input parameter type | extract their root cause variables and/or conditionals. |  |  |  |  |  |  |  |  |  |
| (or a concrete subtype if it is abstract), with fields set to a default | In the current implementation of Car, we only perform full |  |  |  |  |  |  |  |  |  |
| zero or null value. Figure 3(b) shows the path driver method for | recovery for runtime-generated exceptions where the root cause |  |  |  |  |  |  |  |  |  |
| the target path in Figure 1. During dynamic analysis, this method | of the dependency error is available directly from the runtime. |  |  |  |  |  |  |  |  |  |
| will be invoked in the application’s process to inject the target path, | This covers the | NullPointerException | , which comprises over 75% |  |  |  |  |  |  |  |
| which in turn will trigger the target sensitive location. | of dependency-related errors in our evaluation. For other errors, |  |  |  |  |  |  |  |  |  |
| 3.3 | Dynamic context refinement | recovery by suppressing the exception and continuing execution in |  |  |  |  |  |  |  |  |
| The approximated context set up by the path-driving framework | the caller of the excepting method (i.e. oblivious to the failure [36]). |  |  |  |  |  |  |  |  |  |
| is limited by the scope of the static constraint analysis. Uncon- | As unresolved dependencies only occur in unconstrained methods, |  |  |  |  |  |  |  |  |  |
| strained methods that are invoked by the target path, but were | the realized path is not affected. Car’s implementation can be |  |  |  |  |  |  |  |  |  |
| not analyzed, may depend on program state outside of the gen- | extended to instead recover fully from these exceptions by using |  |  |  |  |  |  |  |  |  |
| v.recordInput() | , which is an unconstrained auxiliary method. | To recover from a | NullPointerException | , Car identifies the |  |  |  |  |  |  |
| Its dereference of | detectedInput | imposes a dependency since the | error’s root cause from the runtime’s exception processing routines, |  |  |  |  |  |  |  |
| field may not yet have been initialized. When the target path is | which track the register that caused the error. Car overwrites this |  |  |  |  |  |  |  |  |  |
| triggered with the approximated context, execution can end pre- | variable with the address of an object that can resolve the depen- |  |  |  |  |  |  |  |  |  |
| maturely in a runtime exception or crash inside | recordInput() | dency, which we call the | recovery object | , and transparently returns |  |  |  |  |  |  |

---

## Page 7

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |  |  |
| --- | --- | --- | --- |
| execution to the instruction where the error occurred (i.e. the | re- | 4.1 | Static targeting and context inference |
| covery location | ). Since the register now contains a value expected | We base the static extraction of target paths and constraints on |  |
| by the application, execution continues along the target path as if | the publicly available static component of Tiro [49]. We augment |  |  |
| the error never occurred. The recovery object does not affect the | Tiro’s constraint analysis with greater support for different types |  |  |
| control flow of the realized target path, as dependency recovery | of constraints, including class type constraints and non-null con- |  |  |
| is needed only for unconstrained methods (any variables influenc- | straints for instance object accesses. |  |  |
| ing the realized path would have been captured by the constraint | For each path, Car must generate code to construct the approx- |  |  |
| analysis and already resolved). | imated contexts and create the path driving framework. We also |  |  |
| To obtain the recovery object, a seemingly obvious approach | instrument application code at target locations to log when a target |  |  |
| would be to simply instantiate an object based on the declared type | has been reached (for evaluation). We use Soot’s [45] bytecode |  |  |
| of the root cause variable. However, it is unclear how to initialize | generation to construct these elements and store them with the rest |  |  |
| the object properly, as constraints are not extracted for uncon- | of the static analysis output (we do not repackage the original APK |  |  |
| strained methods. Initializing the fields of the object to null values | or binary of the application). |  |  |

will trigger further errors in the execution, as the application will

| expect objects to be initialized properly. Invoking the default con- | 4.1.1 | Generating constrained subclasses. | For each constrained ob- |  |  |
| --- | --- | --- | --- | --- | --- |
| structor may set some fields to an expected default value but many | ject variable, the generation of its constrained subclass in the path- |  |  |  |  |
| application classes define a custom parameterized constructor that | driving framework requires identifying the base class to extend. |  |  |  |  |
| populate its fields from the arguments (it may even throw a further | One might assume that this would be the constrained variable’s |  |  |  |  |
| exception if these arguments are null). Instantiating other objects | declared type in the application bytecode, but it often cannot be |  |  |  |  |
| to populate the fields can lead to a series of instantiations due to | directly used for two reasons: (1) the declared type is abstract and |  |  |  |  |
| chained object references. In the worst case, one might reinstantiate | cannot be instantiated to create a context object (especially true for |  |  |  |  |
| all of the objects in the application for each recovery. | constraints on inputs of entry-point methods), and (2) the target |  |  |  |  |
| Instead, Car heuristically obtains the recovery object by re-using | path itself may assume a specific type (i.e. it imposes type con- |  |  |  |  |
| an already instantiated object from the application. It maintains a | straints, like Line 8 in Figure 1). To resolve these conditions, when |  |  |  |  |
| cache of recently allocated objects and constrains the re-used object | performing static constraint analysis, Car also extracts type con- |  |  |  |  |
| based on type compatibility with the root cause variable. By re- | straints for variables used in class- or type-related operations, such |  |  |  |  |
| using objects in this way, we are essentially resolving a dependency | as | cast | , | instanceof | , and any object accesses. When constructing |
| as if the injected path had been triggered normally and preceded | a constrained object, it searches the application’s class hierarchy |  |  |  |  |
| by its dependent paths that would have provided the dependent | tree for a concrete class that fulfills all of the type constraints on the |  |  |  |  |
| object. If no compatible object can be found, Car then instantiates | variable. If there are multiple such classes, Car randomly chooses |  |  |  |  |
| a new object and initializes it with null values. | the most specific subclass (i.e. a leaf of the class hierarchy tree), |  |  |  |  |
| To complete the example from Figure 1, if | detectedInput | is null | preferring an application class over one declared by the Android |  |  |
| when the realized target path executes, a | NullPointerException | framework or Java runtime library. This heuristic is based on the |  |  |  |
| will be thrown in | recordInput() | at Line 29. When the exception | notion that the application has extended a class for a purpose and |  |  |
| is generated, Car will detect that a dependency error has occurred | unconstrained methods may depend on the extra functionality. |  |  |  |  |

in a target path, determine that the faulting instruction is a method

| invocation, and that the (null) receiver object is a | List | . It will | 4.1.2 | Initialization of constrained subclasses. | When Car gener- |
| --- | --- | --- | --- | --- | --- |
| search for a previously allocated | List | object or instantiate a new | ates constrained subclasses for approximated contexts, it needs to |  |  |
| concrete subclass of | List | (e.g. | ArrayList | ). After generating the | specify how they should be initialized when they are instantiated. |
| recovery | List | object, Car will set the register for | detectedInput | We assume that a constrained subclass should behave in the same |  |
| to its address and return the execution to | recordInput() | . The | manner as its extended base class for unconstrained members. For |  |  |
| invocation in Line 29 will succeed and the execution will continue | each constrained subclass, we generate a constructor method that |  |  |  |  |
| to the file write instruction and the target sensitive action. | invokes the base class’s constructor, which will presumably set all |  |  |  |  |

unconstrained fields to their initial or default values. Car heuris-

tically chooses to invoke the base constructor method with the

fewest input parameters. In cases in which the base class construc-

tor requires input arguments, we set them to a default zero or null

| 4 | IMPLEMENTATION | value if they are unconstrained by the target path. The generated |  |
| --- | --- | --- | --- |
| Car’s implementation consists of: (1) a static context inference | constructor will set any constrained field members after the base |  |  |
| component to extract target paths and generate approximated con- | constructor invocation to ensure the enforced context values are |  |  |
| texts, (2) a dynamic driving controller to inject the paths, and (3) | visible to the target path |  |  |
| an instrumented version of the Android OS (AOSP) to facilitate | We found that some classes are meant to be constructed in a |  |  |
| the path driving process and perform dynamic context refinement. | certain way and may rely on a static initializer method to ensure |  |  |
| The static component is in Java and operates directly on the ap- | all state is initialized properly. For instance, the | MotionEvent | class |
| plication’s bytecode (APK file). It uses Soot [45] for its base static | in the Android framework is backed by a native class that pro- |  |  |
| analysis and Z3 [10] for constraint solving. The dynamic controller | vides most of its functionality. Rather than using constructors, |  |  |
| is in Python and the instrumentation of AOSP is for Android 10. | static initializer methods are provided to ensure that when the |  |  |

894

---

## Page 8

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |  |  |
| --- | --- | --- | --- |
| Java | MotionEvent | class is instantiated, the native backend object | issue with our datasets since applications containing native code |
| is created as well—if the native object is not constructed, we find | usually include both ARM and ARM64 binaries for greater com- |  |  |
| that segmentation faults arise later when the Java object is used. | patibility. Also, the generation of recovery objects requires a cache |  |  |
| We identified several commonly used classes that are irregularly | of previously allocated objects. We instrument the class initializa- |  |  |
| constructed and specifically invoke their initializer methods when | tion process to store the addresses of allocated objects in reverse |  |  |
| we need to create a constrained subclass for them. | chronological order. |  |  |

The construction of constrained subclasses can be recursive if

first construct a constrained subclass for x that overrides method

Our modifications to AOSP span ~3000 added or modified lines of

code and include instrumentation of the Android framework and

the Android runtime (ART).

which often trip code integrity checks.

4.3.2 Dynamic dependency recovery. Car’s dynamic context re-

tions are generated by ART. The recovery process is architecture

dependent due to the manipulation of machine registers, including

895

is precompiled.

When ART is in “quick” mode, it is executing precompiled DEX

the segmentation fault and eventually generate a NullPointer-

at the point when it has determined that the signal is the result of a

null pointer error. We then identify the DEX instruction correspond-

ing to the native PC where the error occurred and use the declared

receiver class type for the generation of the recovery object. We

5 EVALUATION

research questions:

| constraints exist for chained object references. For instance, a path | 4.3.3 | Null recovery instrumentation in ART. | The exact method of |  |  |
| --- | --- | --- | --- | --- | --- |
| may require that when method | x.foo() | is invoked, it returns an | recovering from a dependency-related null pointer exception in |  |  |
| object | y | where the field | y.a | contains a specific value. Car would | ART depends on the current execution mode and whether the code |
| foo() | . This method must return a constrained object for | y | , so it | When ART is in the DEX “interpreter” mode, the routines for |  |
| constructs another constrained subclass where field | a | is set to the | handling object access instructions contain explicit checks for a |  |  |
| required context value. | null receiver object. We add a hook into these checks to determine |  |  |  |  |
| Our current implementation returns only one context value for | whether the null error is occurring during Car’s path driving, which |  |  |  |  |
| each constrained variable. However, we can easily return a sequence | we determine by searching backward through the stack trace to find |  |  |  |  |
| of values for cases when the path makes multiple accesses to the | a path driver caller method. If so, the recovery process is triggered |  |  |  |  |
| same object/state (e.g. invocations to the same method) and expects | and the recovery object is returned to the original object access |  |  |  |  |
| a different value for each access. | routine, which can now operate on the non-null receiver. |  |  |  |  |
| 4.2 | Dynamic driving controller | code. Object accesses in this mode are handled in one of two ways: |  |  |  |
| The dynamic controller receives information from the static com- | through a trampoline function to handle a virtual field or method |  |  |  |  |
| ponent, including the extracted target paths and their path driving | reference (when the compiler cannot statically resolve the receiver |  |  |  |  |
| code, and runs on a machine connected to a physical Android de- | type precisely) or a direct native memory access at the resolved |  |  |  |  |
| vice. For each application, it sequentially injects each target path | field/method offset within the receiver object. For the trampoline |  |  |  |  |
| by sending a control message to a custom system service running | case, explicit null receiver object checks are also present within |  |  |  |  |
| within an instrumented OS on the test device. It monitors the output | the trampoline function and dependency recovery proceeds in the |  |  |  |  |
| log to determine whether the target location for each path has been | same manner as the interpreter mode. |  |  |  |  |
| reached and to restart the application on a crash, which usually | For direct native memory accesses, a null receiver object will |  |  |  |  |
| occurs when an incomplete context is inferred for a target path and | result in a segmentation fault when ART tries to access a field or |  |  |  |  |
| our heuristics for dynamic recovery fail. | method within. ART has a custom signal handler that will triage |  |  |  |  |
| 4.3 | Custom Android OS | Exception | object to be thrown. We instrument the signal handler |  |  |
| 4.3.1 | Delivery of injected paths. | We instrument the framework to | determine the machine register assigned to hold the receiver vari- |  |  |
| add a custom system service to deliver injected events. Through | able for the DEX instruction and overwrite it with the address of |  |  |  |  |
| socket and interprocedural (IPC) calls, the service invokes the path | the generated recovery object. Using the signal context from the |  |  |  |  |
| driving frameworks in the application’s main thread. To load our | original segfault signal, we restore the machine’s context to the |  |  |  |  |
| custom path driver methods and contexts, we modify the class | PC where the error originally occurred, with the original register |  |  |  |  |
| loader within ART. When an context class is requested, the class | values (with the exception of the register now holding the recovery |  |  |  |  |
| loader will load it from Car. We also load instrumented application | object). The execution should return to the faulting instruction, |  |  |  |  |
| classes in this way so that the code modifications occur only in | with the memory access now performed on the recovery object’s |  |  |  |  |
| memory and the application cannot detect any changes to its binary, | address rather than a null address. |  |  |  |  |
| finement and recovery of dependency errors involve instrumenting | We evaluate Car on popular applications from the Google Play |  |  |  |  |
| ART’s code interpretation processes. Monitoring requires the mod- | application marketplace to demonstrate its ability to generate con- |  |  |  |  |
| ification of exception handling code to detect when an exception is | texts and trigger a wide range of target sensitive behaviors in large, |  |  |  |  |
| thrown. For recovery, we instrument locations where null excep- | complex applications. We are interested in answering the following |  |  |  |  |
| the PC. We currently implement dependency recovery for ARM | Q1: | Does the use of context approximation and refinement im- |  |  |  |
| and we force ART to run in ARM mode, if possible. This was not an | prove dependency resolution for targeted execution? |  |  |  |  |

---

## Page 9

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |  |
| --- | --- | --- |
| Q2: | Is Car effective at reaching target code locations in Android | also extracts the same target paths. We execute the target paths dy- |
| applications? | namically with Car and measure the effectiveness of using contexts |  |

Q3: Are the paths that Car executes sound, despite forgoing full

dependency tracking?

due to device incompatibilities or dependencies on Google Play

Services, which is not included with AOSP. Some applications trig-

To evaluate Car on a variety of sensitive behaviors and paths, we

configured it to target the sensitive source and sink methods from

FlowDroid [3]. While we are not performing taint analysis, the

methods include a variety of different sensitive actions on Android

that are likely of interest when performing security analysis. In

addition, we also target invocations to reflection APIs, code loading

APIs, and native methods, which may be used for obfuscation. In

total, we target over 235 different APIs in our evaluation, which is

likely greater than what would be targeted during realistic usage.

This overapproximation of targets places greater strain on the static

and dynamic analyses, as more paths must be targeted, and allows

us to fully exercise Car’s abilities.

We compare Car’s ability to resolve dependencies for targeted

execution against IntelliDroid [48] and Tiro [49], which are similar

hybrid targeted execution frameworks for Android. Tiro is based

on IntelliDroid and they employ the same target path extraction

and dependency resolution techniques, which favor precise static

896

to resolve dependencies. We were unable to run IntelliDroid [48] or

Tiro [49] as their dynamic frameworks only support Android 4.3

and 6.0, respectively, which is incompatible with our devices and

Car’s dynamic dependency recovery). Instead, we analyze the out-

provement of 3.6× in target coverage.

over purely static tracking.

targeted or forced execution tools to compare against Car on the

We compare Car’s results with these published numbers for Droid-

Bot [20] (a purely dynamic exploration tool), GroddDroid [1] (a hy-

brid GUI exploration and forced execution tool), and IntelliDroid [48].

EvaDroid contains 22 synthetic applications representative of

evasive malware. “Payloads” are hidden from dynamic analysis

through complex activation conditions, such as timing conditions

or device fingerprinting. We ran Car on the EvaDroid dataset and

in Table 1, we compare Car’s payload coverage with the results

from the previous study. We also confirmed that Car triggered no

false positive paths on the test applications.

Car can reach a greater number of payloads than the purely

dynamic tool, DroidBot; this agrees with the results from our large-

scale evaluation below. It also achieves greater payload coverage

than GroddDroid, likely because GroddDroid only forces branches

encountered during its initial dynamic GUI exploration, which

has limited coverage. Car also outperforms IntelliDroid, which is

expected from our results in Section 5.3.

| Q4: | Can Car uncover new security-sensitive behaviors? | our dataset (Android 4.3 also predates ART, where we implemented |  |  |
| --- | --- | --- | --- | --- |
| 5.1 | Experimental setup | put from their dependency analysis and generously assume that the |  |  |
| We ran Car’s static component on machines with Intel Xeon E5- | lack of dependency tracking errors reported by IntelliDroid/Tiro |  |  |  |
| 2650 CPUs, with a JVM configuration of 200 GB of memory and | means they would have triggered the path. |  |  |  |
| 24 threads. The dynamic driving controller ran on an Intel i7-3770 | Of the targets triggered by Car, IntelliDroid/Tiro reported in- |  |  |  |
| machine with a tunneled USB-A connection to physical Android de- | complete dependency tracking or unsupported event injection for |  |  |  |
| vices. | 1 | We tested on Pixel and Pixel 2 devices running our modified | 72.1%. These errors would have prevent the tools from executing |  |
| version of Android 10 without Google Play Services installed. We | the target paths at run-time. This would result in IntelliDroid/Tiro |  |  |  |
| used the same device type for all of the testing for each application. | reaching less than a third of the targets reached by Car—an im- |  |  |  |
| 5.2 | Dataset | Of the paths that IntelliDroid/Tiro could not execute, we ana- |  |  |
| To demonstrate Car’s generalizability on a variety of common | lyzed the techniques used by Car to resolve their dependencies. |  |  |  |
| applications, we crawled the Google Play marketplace for the bi- | Statically generated contexts were necessary in 84.7%. Dynamic |  |  |  |
| naries and metadata of all free applications in June 2019. To form | context refinement in unconstrained methods was necessary in |  |  |  |
| our dataset, we sorted Google Play’s application categories into 15 | 53.3%. This consisted of recovery from runtime-generated null ex- |  |  |  |
| related category groups. For each group, we extracted the 25 most | ceptions, with 92.7% of the recovered paths re-using objects from |  |  |  |
| popular applications (determined by the total number of down- | the application. Other dependency-related exceptions that were |  |  |  |
| loads), resulting in 375 applications in total. This set includes well- | only partially recovered (by suppressing the exceptional control |  |  |  |
| known applications such as Facebook, WhatsApp, Pokémon Go, | flow) occurred in 18.1%, with | IllegalStateException | ’s forming |  |
| Spotify, BBC News, Microsoft Office, eBay, Instagram, Uber, and | the majority of the cases (13.5%). Car’s ability to reach the targets, |  |  |  |
| AccuWeather. | despite the approximations made in the static constraint analysis, |  |  |  |
| Several applications crashed when launched on our test devices | shows the effectiveness of hybrid dependency resolution techniques |  |  |  |
| gered errors in our version of Soot, due to incomplete support for | 5.4 | Triggering target locations ( | Q2 | ) |
| specific DEX instruction sequences. We skipped them, resulting in | 5.4.1 | Evaluation on EvaDroid. | Due to lack of availability and/or |  |
| an effective dataset of 310 applications. | incompatible Android versions, we were unable to run previous |  |  |  |
| 5.3 | Effectiveness of contexts for dependency | Google Play dataset. Instead, we ran Car on the EvaDroid test |  |  |
| resolution ( | Q1 | ) | suite [6], which was used to evaluate several previous tools [38]. |  |
| dependency tracking. As Car uses the initial targeting from Tiro, it | 5.4.2 | Large-scale evaluation. | We perform a large-scale compar- |  |
| 1 | Tunneling over SSH and VPN was required due to COVID-19 access restrictions for | ison of target coverage in popular applications against several |  |  |
| the building where our analysis infrastructure was located. | state-of-the-art dynamic GUI and model-based exploration tools: |  |  |  |

---

## Page 10

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |
| --- | --- |
| 8× | 100% |

6×

4×

2×

Books News

Finance Games Health Leisure Media

Lifestyle

Shopping

Productivity

Communicate

Categories

Figure 4: Comparison of non-trivial sensitive targets triggered by Car and by existing dynamic driver tools

number of targets of all the dynamic tools tested.

Table 1: Comparison of payload coverage on the

EvaDroid [6] test suite of evasive applications

Monkey similar to previous work (and gives a slight edge in its

coverage [31]). To account for the delays caused by Car’s dynamic

dependency recovery, we conservatively used a longer wait time of

cantly reduced, as we explain in Section 5.9). We also identified the

targets that were trivially triggered without any user input during

the first 30 seconds when the application launched. We remove

these targets in our comparisons, as they can be reached without 5.5

than others. We compared Car against the best-performing tool for

897

92.3%

90%

80%

3.1×

70%

60%

Social Tools Travel

Overall

Weather

tools from making much progress.

launch. A large portion (44.2%) were reached only by Car.

Triggered only by CAR

| 27.1% | Triggered by CAR and |
| --- | --- |
| 44.2% | other tool(s) |
| 19.5% | launch (i.e. trivial) |

Est. false detection rate

gered by the different dynamic tools

False positives ( Q3 )

total, we manually inspected 75 target paths.

Improvement over best existing tool for each app 0× 50% Applications where CAR triggers the most targets

The solid green bars (left axis) show the average improvement in the number of non-trivial targets triggered by Car against the best-performing tool

(Monkey, DroidBot, or Ape) for each application. The striped blue bars (right axis) show the percentage of applications for which Car triggers the greatest

| Tool | Payloads triggered | can be accessed; this log-in dependency blocked the GUI exploration |  |
| --- | --- | --- | --- |
| Car | 73% | In addition to the blanket coverage, we also considered which |  |
| DroidBot | (evaluation from [38]) | 17% | targets were triggered by Car and by the other tools. Figure 5 shows |
| GroddDroid | (evaluation from [38]) | 37% | a breakdown of targets triggered in an application by the various |
| IntelliDroid | (evaluation from [38]) | 33% | tools, including those trivially triggered during the application’s |
| Monkey [27], DroidBot [20], and Ape [15]. We ran the tools for | Triggered only by Monkey, |  |  |
| an average of three hours for each application, using the default | 9.1% | DroidBot, and/or APE |  |
| configuration for DroidBot and Ape, and a throttle of 100 ms for | Triggered during application |  |  |
| 10 seconds between injections for Car (this could have been signifi- | Figure 5: Average breakdown of the sensitive targets trig- |  |  |
| the use of any tool. | Of the 44.2% of newly triggered targets in Figure 5, we manually |  |  |
| In Figure 4, we show Car’s improvement in triggering target | inspected a subset to determine whether they are truly reachable |  |  |
| behavior on our dataset. Car dynamically reached 125 sensitive tar- | or whether they were the result of unsound path execution (i.e. |  |  |
| gets for each application on average. When comparing Car to each | false positives). Our sample set was chosen as follows: (1) for each |  |  |
| tool individually, Car triggered 4.5× more non-trivial targets in an | category, we randomly sampled five applications; (2) for each ap- |  |  |
| application than Monkey, 5.2× more than DroidBot, and 7.1× more | plication, we computed the list of targets that were triggered by |  |  |
| than Ape. However, we also found that between Monkey, DroidBot, | Car but not by any other tool; (3) we randomly chose one of those |  |  |
| and Ape, some perform significantly better for certain applications | targets and analyzed the decompiled code that would trigger it. In |  |  |
| each application and found that we were able to reach an average of | Our primary objective was to determine whether a target newly |  |  |
| 3.1× more targets. Furthermore, Car triggered the greatest number | triggered by Car would be executed during normal execution. From |  |  |
| of targets for 92.3% of the applications. | our experience, applications often include third-party libraries in |  |  |
| Car showed the greatest improvement in the “Communication” | their APKs but may not use all of the code within them. Since Car |  |  |
| and “Social” categories (> 5× more non-trivial targets). These appli- | invokes path entry-point methods directly, it is possible that some |  |  |
| cations often require the user to log in before certain functionality | of the injected events would not have been registered or triggered |  |  |

---

## Page 11

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| during normal execution. For each target in our sample set, we | Sensitive | Google Play | Creepware |  |  |  |  |
| checked whether all of the invocations, control flows, and data | functionality |  |  |  |  |  |  |
| flows were valid across the path methods. We also checked whether | Apps | Calls | Cxt. | Apps | Calls | Cxt. |  |
| the path’s entry-point is live. For entry-point event handlers that | Location | 84 | 237 | 89% | 14 | 42 | 86% |
| must be registered with the framework, we recursively checked the | Personal data | 6 | 6 | 83% | 4 | 4 | 100% |
| path(s) to the registration call-sites. | Media | 3 | 3 | 100% | 1 | 1 | 100% |

We determined that 18.7% of the sampled targets were reached

through infeasible paths, where the samples were drawn from the

subset of targets that were triggered only by Car. When we trans-

late this rate across all of the targets triggered by Car and assume

number of false positives found was 0.7 out of 5.

We found the underlying reason to be static imprecision in the

points-to analysis when extracting target paths. This manifested in

two ways: (1) the entry-point analysis incorrectly identified event

handlers as application entry-points due to the conservative alias-

ing of objects at registration call-sites; and (2) method invocation

edges were incorrectly constructed in the call-graph due to con-

servative aliasing of the invocations’ receiver objects. All the false

positives found were located in first- or third-party libraries pack-

screen. For a further 15% of cases, the application was blocked by

898

| Telephony | 7 | 11 | 100% | 4 | 4 | 50% |
| --- | --- | --- | --- | --- | --- | --- |
| Network | 59 | 99 | 74% | 11 | 20 | 85% |
| Files | 220 | 1199 | 88% | 63 | 361 | 10% |

Table 2: New sensitive behaviors missed by other tools that

only Car could find (and the percentage requiring contexts)

requirements, and used the path’s context to return true when the

application queried the framework for the other application.

5.7 Analysis of sensitive behaviors ( Q4 )

a set of 91 malicious applications recently labeled as evasion or

surveillance “creepware” [37]; these were used for interpersonal

attacks, such as harassment or stalking.

trigger.

| that overlapping targets that were also reached by Monkey, Droid- | Databases | 76 | 187 | 90% | 11 | 47 | 94% |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bot, and/or Ape are true positives, we have a false detection rate | Package mgr. | 134 | 222 | 93% | 12 | 21 | 90% |
| of 9.0%. This was heavily skewed by the targets sampled from the | Reflection | 169 | 447 | 84% | 25 | 113 | 75% |
| “Games” category, where 4 out of 5 inspected targets were deter- | Code loading | 7 | 7 | 71% | 10 | 10 | 60% |
| mined to be dead code. For the rest of the categories, the average | Native code | 223 | 1090 | 88% | 29 | 120 | 68% |
| aged with the applications as determined by the package name | The new behaviors uncovered by Car ranged over a variety of |  |  |  |  |  |  |
| of methods in the paths. The spike of false positives within the | different security-sensitive actions missed by the other tools. In |  |  |  |  |  |  |
| “Games” category is likely due to the large number of libraries used, | Table 2, we break down the sensitive actions that only Car was able |  |  |  |  |  |  |
| including graphics rendering, analytics, and advertisement libraries. | to find. We further show that Car’s context-based techniques were |  |  |  |  |  |  |
| Libraries introduce a great deal of code that must be analyzed but | essential and measured the percentage that required contexts or |  |  |  |  |  |  |
| may not necessarily be used by the main application, increasing | dynamic dependency recovery. Since our original dataset contained |  |  |  |  |  |  |
| the effects of conservatism due to imprecision. | only benign applications, we also compared Car and Monkey on |  |  |  |  |  |  |
| 5.6 | Analysis of newly triggered targets | Car operates effectively on both benign and malicious applica- |  |  |  |  |  |
| During our manual analysis, we also enumerated the different rea- | tions and uncovers new sensitive or malicious behaviors missed |  |  |  |  |  |  |
| sons why the other dynamic tools were unable to trigger the cases | by the other tools. This ranged from recurring location accesses |  |  |  |  |  |  |
| where the target was a true positive for Car (i.e. not a false positive | that leak location data to the network, to accesses to local email |  |  |  |  |  |  |
| from the previous section). For 21%, the target could not be reached | accounts hidden under misleading UI. We also found cases in which |  |  |  |  |  |  |
| by the other tools because the application was blocked by a login | code was dynamically loaded on paths that only Car was able to |  |  |  |  |  |  |
| a dialog for Google Play Services. For 13%, the target could only | To verify that Car is able to uncover sensitive behaviors in |  |  |  |  |  |  |
| have been reached for certain devices or versions or if a specific | malicious applications, we ran Car on the Creepware [37] dataset |  |  |  |  |  |  |
| error, such as a network failure, had occurred. While these condi- | and find it can detect a variety of malicious behaviors that were |  |  |  |  |  |  |
| tions could not have been achieved in our test environment, Car’s | manually confirmed to be true positives. We provide an analysis of |  |  |  |  |  |  |
| inferred path contexts was able to mimic the environment required. | these cases below to demonstrate Car’s ability to uncover malicious |  |  |  |  |  |  |
| For the remaining 51%, we found that they could have been | or evasive activity in applications, by guiding or targeting execution |  |  |  |  |  |  |
| reached by normal UI interactions or system event injections. How- | toward sensitive actions. While a dynamic taint tracking tool would |  |  |  |  |  |  |
| ever, a few would have required extremely complex interactions | have been ideal for detecting the cases of private data leakage, we |  |  |  |  |  |  |
| between event paths. In one case, the target occurs after the user | were unable to integrate Car with previous taint tracking tools |  |  |  |  |  |  |
| purchases a travel package through the application, is located at | because they were implemented for older versions of Android or |  |  |  |  |  |  |
| an airport, and has Uber installed on their device. The conditions | their implementation was not fully available [11, 42, 54] We instead |  |  |  |  |  |  |
| required for this path include UI flow across multiple screens (pur- | relied on manual analysis and instrumentation to determine the |  |  |  |  |  |  |
| chase process), input that is difficult to generate (purchase informa- | flow of data triggered by Car’s targeting. |  |  |  |  |  |  |
| tion), specific system state (location), and dependence on other in- | Periodic background location tracking: | One malicious appli- |  |  |  |  |  |
| stalled applications. Car directly invoked the location event handler | cation was intended to surreptitiously track the location of an |  |  |  |  |  |  |
| for the target path, thus bypassing the multiple purchase-related | unsuspecting victim. It uses Android’s alarm service was used to |  |  |  |  |  |  |

---

## Page 12

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |
| --- | --- |
| periodically invoke a location gathering method, which regularly | into the calculator. Car was able to explore past the initial calculator |
| accesses the device’s location data and send it to the network. Car | interface without having to decipher the correct password. |

was able to trigger the periodic location gathering function and ex-

ecute this behavior by directly invoking the alarm callback method

Location tracking on a location change: There are several meth-

ods of accessing location information, including a callback-based

approach. One application registers a location callback that is in-

voked by the framework when the device’s location has changed.

The application then stores the new location information into a

cloud storage location and sends it to the network asynchronously.

Car was able to execute the location leakage path while Monkey

was unable to trigger the location change required for the callback

to be activated.

can also be used for spying). In some of the applications, Monkey

was able to trigger the private data leakage. However, in at least

Hidden access to device accounts: One application provided a

“cloning” functionality, in which the application’s main activity

shows a set of public accounts and a secondary hidden activity

enables access to a set of private accounts. We manually confirmed

that Car was able to access both interfaces and detect access to both

sets of accounts. The hidden interface would have been particularly

difficult for dynamic tools such as Monkey, as there were complex

UI actions required to make the activity visible. In contrast, Car

was able to trigger the intentionally hidden account functionality.

Similarly, we also found similar evasive applications that hide an

899

5.8 False negatives

handling of constraints, especially for lists and arrays; (3) reliance

on the stack trace for dependency error monitoring, which misses

errors in new threads as they have a new stack; (4) constraints on

the results of one-way computations, such as encryption or hashing,

which could not be inversed to generate a context value; and (5) any-

path extraction of target paths, which may extract infeasible paths

to a target due to the conservative call-graph and miss a true path.

Items (1) – (3), which applied to over 75% of the sampled false

negatives, are artifacts of the implementation and can be fixed with

more engineering. They were the primary reason why Car pro-

5.9 Performance

dynamic component, we injected all of the paths extracted by the

extracted targets were dynamically triggered by the tested tools,

we suspect that many of the unreached targets were actually in-

feasible due to static imprecision. Car steadily made progress as it

injected each statically extracted path. For the others, while they

were successful at finding targets near the beginning, they made

significantly less progress over time. After an hour of analysis, Car

already shows a large improvement in the number of triggered

targets.

6 DISCUSSION AND LIMITATIONS

entry-point methods directly can lead to the execution of paths

| and using contexts to resolve the dependencies and constraints | While there is overlap in the targets reached by Car and the other |  |
| --- | --- | --- |
| imposed by the callback path. In contrast, Monkey was unable to | tools, we did find that 9.1% of all triggered targets in Figure 5 could |  |
| access this functionality due to log in and set up requirements that | be reached by at least one of the other tools but were missed by |  |
| were necessary to enable the tracking. The leakage of location data | Car. We consider these known false negatives of Car. We manually |  |
| in the background is performed without user awareness and should | analyzed 15 of these targets across all of the categories and found |  |
| be triggered for dynamic security analysis to evaluate whether an | the following underlying reasons: (1) incomplete object handling |  |
| application violates the privacy of the device’s user. | across Android interprocedural (IPC) invocations; (2) incomplete |  |
| Leakage of private data to the network: | A large number of the | duced lower coverage in a few applications. (4) is a fundamental |
| tested malicious applications (approximately half) are surveillance | limitation of symbolic analysis, although in some cases, it was miti- |  |
| applications that registers the device for a tracking service. This | gated when the required result of a one-way computation can be |  |
| tracking enables the device’s location, phone number, identifiers, | statically extracted and set by a modeled method. (5) can be miti- |  |
| photos, videos and/or received messages are sent to a third-party | gated by sampling more paths for each target, though the extraction |  |
| (supposedly for emergency situations, though this functionality | of all paths to a target would ultimately be exponential. |  |
| two of the tracking applications, Car was able to trigger private | We measure the performance of the static and dynamic compo- |  |
| data leakage of device identifiers and location data to the network | nents of Car separately on our Google Play dataset. We ran the |  |
| that Monkey was unable to reach. This was primarily due to a | static context inference analysis with a timeout of 240 minutes |  |
| requirement to register the device with the tracking service, which | and retrieved partial results in cases in which full analysis had not |  |
| Car was able to bypass. | completed. For most applications, the full time was used. For the |  |
| Transmitting microphone recording over Bluetooth: | A spy- | static analysis (maximum of 2700 for each application). We throt- |
| ing application streams input from the microphone to a Bluetooth | tled Car execution with a conservative wait time of 10 seconds for |  |
| headset, allowing someone to eavesdrop on the device’s surround- | a target to be reached before injecting the next path. On further |  |
| ings and on the user’s conversations. The functionality is only | analysis, this could have been significantly reduced as an average |  |
| accessibly if a Bluetooth headset is connected to the device. Other | path took 1.4 seconds to reach the target location. |  |
| dynamic tools would have difficulty triggering the spying behavior | We examined the sensitive targets triggered over the duration |  |
| unless the analysis environment specifically includes such a headset. | of the analysis for each tool and plotted the cumulative number of |  |
| Car used its contexts to resolve the system Bluetooth dependency. | triggered targets in Figure 6. While only a portion of the statically |  |
| account-related activity behind a calculator interface. The hidden | As stated in Section 5.8, a fundamental limitation is that some |  |
| accounts are accessible only when a specific password is entered | constraints cannot feasibly be solved. Furthermore, injecting path |  |

---

## Page 13

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |
| --- | --- |
| 30% | Car’s static constraint analysis is related to symbolic execu- |

10%

triggered dynamically 0

that might not occur normally if their entry-points were never

registered with the framework. Because the dynamic dependency

recovery refines the context heuristically, it may also construct

infeasible contexts that would never occur during normal execu-

tion (by returning an incorrect recovery object). All of these can

affect the soundness of the paths triggered; however, these issues

are not unique to Car. Forced execution tools will also execute in-

feasible paths from unreachable entry-point methods and incorrect

data accesses, especially as they enforce branch outcomes without

ensuring that the accompanying data dependencies are resolved.

Furthermore, without analysis of how data values are used, forced

execution can result in infeasible control-flow paths due to the

forcing of a normally impossible combination of branch outcomes.

Car’s constraint analysis ensures that the extracted path is con-

sistent with respect to the data it accesses; the context will either

contain values that satisfy all of the constraints imposed by the

path’s conditional branches or, if the branches required are incom-

patible and the path is infeasible, no context would be generated.

We believe Car achieves a good balance between its sources of

unsoundness and its coverage of target locations, demonstrated

by its ability to outperform existing dynamic tools in target cov-

erage while maintaining a 9.0% false detection rate on popular

applications. In addition, our false positive evaluation in Section 5.5

showed that the primary source of infeasible paths in Car were due

to static imprecision (i.e. over-conservative entry-point detection

and points-to analysis), which also affect forced execution.

7 RELATED WORK

Car is most closely related to other targeted dynamic analysis tools.

IntelliDroid [48] and Tiro [49] perform targeted execution of An-

droid applications, though they rely on precise static dependency

tracking and resolution. Similarly, guided symbolic execution tools

unsound or infeasible paths, resulting in false positives.

900

tion (such as EXE [9] and KLEE [8]) and concolic execution (such

ing constraints dynamically, which adds significant overhead, Car

uses hybrid dependency resolution. UC-KLEE [32], which performs

ecuting paths rather than individual methods. Car is also similar

calls are skipped. Chopped functions are similar to Car’s modeled

methods and any unconstrained methods that are aborted.

Car is a hybrid tool and is related to other static-guided dynamic

analysis tools. Brahmastra [7], AppDoctor [17], SmvHunter [40]

and SmartDroid [57] guide execution by driving component and

UI transitions, which are more coarse-grained than code paths,

and they do not handle dependencies between event paths. Con-

tentScope [58] generates inputs for paths in content providers and

also does not handle inter-path dependencies. AppAudit [50] and

AppIntent [53] use static analysis to guide approximate or symbolic

execution, respectively, for the verification of static information

flows. In contrast, Car guides concrete execution and can be inte-

grated with general dynamic analyses. Car’s static component is

also similar to other static Android tools, such as FlowDroid [3],

Epicc [29], Apposcopy [12], Amandroid [47], CHEX [21], and [52].

Car’s aims to drive the execution of Android applications, simi-

lar to testing frameworks such as DynoDroid [22], EvoDroid [23]

and Sapienz [24], and model-based explorers such as Ape [15],

Stoat [41], DroidBot [20], TrimDroid [25], and A 3 E [4]. Fuzzing

tools, such as AFL [55], are also commonly used outside of An-

droid. They aim for full coverage, while Car focuses on coverage

of target locations. The techniques we use to focus execution to

target paths enables greater coverage of locations of interest to

an analyzer. Semi-targeted exploration, such as FuzzDroid [35]

and Xdroid [33], inject system/framework values, which also helps

resolve dependencies on framework state. CrashScope [28] dynam-

ically triggers application crashes by exploring different system

configurations; however, it does not handle dependencies on data

within the application. Similarly, generating useful test inputs, such

as TextExerciser [16], is also a form of guided fuzzing.

8 CONCLUSION

applications.

| 20% | as DART [13], CUTE [39], and ACTEve [2]). Rather than track- |  |  |  |
| --- | --- | --- | --- | --- |
| CAR | DroidBot | under-constrained symbolic execution by invoking arbitrary meth- |  |  |
| % of static targets | Monkey | APE | ods directly, is in a way bypassing the dependencies of the path. |  |
| 0 | 1 | 2 | 3 | The preconditions imposed by a method on its inputs [18, 32] are |
| Analysis time (hours) | similar to contexts. We can achieve more sound execution by ex- |  |  |  |
| Figure 6: Cumulative number of targets triggered over time | to chopped symbolic execution [44], in which irrelevant function |  |  |  |
| such as AppIntent [53], WatSym [30], and [5] implicitly handle de- | We present Car, a hybrid approach to dependency resolution through |  |  |  |
| pendencies by modeling the program state symbolically. However, | context approximation and refinement. We use a combination of |  |  |  |
| the resources required to precisely track and resolve the program | static constraint analysis and dynamic error recovery to resolve |  |  |  |
| state either statically or dynamically can ultimately reduce the cov- | dependencies on program state while mitigating the trade-off that |  |  |  |
| erage of targets due to overhead. Furthermore, guided symbolic | must be made between precision, completeness, and scalability in |  |  |  |
| execution cannot easily integrate with dynamic analysis tools that | static dependency tracking. We applied Car to the targeted exe- |  |  |  |
| require concrete execution of the application. GroddDroid [1], Har- | cution of Android applications and were able to reach 3.1× more |  |  |  |
| vester [34], DirectDroid [46], and Ares propose forced execution, | non-trivial sensitive targets for an application with a false detection |  |  |  |
| which bypasses a path’s constraints on its dependencies by en- | rate of 9.0%. These sensitive behaviors, which would have other- |  |  |  |
| forcing specific branch outcomes. Forced branching can lead to | wise been missed, are essential for the security analysis of Android |  |  |  |

---

## Page 14

Session 7B: Software Security #2 ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan

ACKNOWLEDGMENTS Symposium on Security and Privacy (SP 2020) . IEEE, 1071–1087.

[17] Gang Hu, Xinhao Yuan, Yang Tang, and Junfeng Yang. 2014. Efficiently, effectively

| We would like to thank He (Shawn) Shuang, Mingyue (Shirley) | detecting mobile app bugs with AppDoctor. In | Proceedings of the 9th European |
| --- | --- | --- |
| Yang, and Ivan Pustogarov for their suggestions and feedback on | Conference on Computer Systems (EuroSys 2014) | . ACM, 18:1–18:15. |
| this work. We also thank Kevin Roundy for sharing their Creepware | [18] Sarfraz Khurshid, Corina S Păsăreanu, and Willem Visser. 2003. Generalized |  |

symbolic execution for model checking and testing. In Proceedings of the 9th

dataset. We thank the anonymous reviewers for their constructive International Conference on Tools and Algorithms for the Construction and Analysis

comments. The research in this paper was supported by an NSERC of Systems (TACAS 2003) . Springer, 553–568.

[19] Patrik Lantz and Anthony Desnos. 2011. DroidBox: An Android application sand-

| CGS-D scholarship, NSERC Discovery Grant RGPIN-2018-05931, | box for dynamic analysis. https://www.honeynet.org/projects/active/droidbox/. |
| --- | --- |
| and a Tier 1 Canada Research Chair. | Accessed: June 2020. |

[20] Yuanchun Li, Ziyue Yang, Yao Guo, and Xiangqun Chen. 2017. DroidBot: A

lightweight UI-guided test input generator for Android. In Proceedings of the

| REFERENCES | 39th International Conference on Software Engineering Companion Volume (ICSE-C |  |  |  |
| --- | --- | --- | --- | --- |
| [1] Adrien Abraham, Radoniaina Andriatsimandefitra, Adrien Brunelat, J-F Lalande, | 2017) | . IEEE, 23–26. |  |  |
| and V Viet Triem Tong. 2015. GroddDroid: A gorilla for triggering malicious | [21] Long Lu, Zhichun Li, Zhenyu Wu, Wenke Lee, and Guofei Jiang. 2012. CHEX: |  |  |  |
| behaviors. In | Proceedings of the 10th International Conference on Malicious and | statically vetting Android apps for component hijacking vulnerabilities. In | Pro- |  |
| Unwanted Software (MALWARE, 2015) | . IEEE, 119–127. | ceedings of the 2012 ACM SIGSAC Conference on Computer and Communications |  |  |
| [2] Saswat Anand, Mayur Naik, Mary Jean Harrold, and Hongseok Yang. 2012. Au- | Security (CCS 2012) | . ACM, 229–240. |  |  |
| tomated concolic testing of smartphone apps. In | Proceedings of the 20th ACM | [22] Aravind Machiry, Rohan Tahiliani, and Mayur Naik. 2013. Dynodroid: An input |  |  |
| SIGSOFT International Symposium on the Foundations of Software Engineering | generation system for Android apps. In | Proceedings of the 21st ACM SIGSOFT |  |  |
| (FSE 2012) | . ACM, 59. | International Symposium on the Foundations of Software Engineeringg (FSE 2013) | . |  |
| [3] Steven Arzt, Siegfried Rasthofer, Christian Fritz, Eric Bodden, Alexandre Bartel, | ACM, 224–234. |  |  |  |
| Jacques Klein, Yves Le Traon, Damien Octeau, and Patrick Drew McDaniel. 2014. | [23] Riyadh Mahmood, Nariman Mirzaei, and Sam Malek. 2014. Evodroid: Segmented |  |  |  |
| FlowDroid: Precise context, flow, field, object-sensitive and lifecycle-aware taint | evolutionary testing of Android apps. In | Proceedings of the 22nd ACM SIGSOFT |  |  |
| analysis for Android apps. In | Proceedings of the 35th ACM SIGPLAN Conference on | International Symposium on Foundations of Software Engineering (FSE 2014) | . ACM, |  |
| Programming Language Design and Implementation (PLDI 2014) | . ACM, 259–269. | 599–609. |  |  |
| [4] Tanzirul Azim and Iulian Neamtiu. 2013. Targeted and depth-first exploration | [24] Ke Mao, Mark Harman, and Yue Jia. 2016. Sapienz: Multi-objective automated test- |  |  |  |
| for systematic testing of Android apps. In | Proceedings of the 2013 ACM SIGPLAN | ing for Android applications. In | Proceedings of the 25th International Symposium |  |
| International Conference on Object Oriented Programming Systems Languages & | on Software Testing and Analysis (ISSTA 2016) | . ACM, 94–105. |  |  |
| Applications (OOPSLA 2013) | . ACM, 641–660. | [25] Nariman Mirzaei, Joshua Garcia, Hamid Bagheri, Alireza Sadeghi, and Sam Malek. |  |  |
| [5] Domagoj Babić, Lorenzo Martignoni, Stephen McCamant, and Dawn Song. 2011. | 2016. Reducing combinatorics in GUI testing of Android applications. In | Proceed- |  |  |
| Statically-directed dynamic automated test generation. In | Proceedings of the 20th | ings of the 39th IEEE/ACM International Conference on Software Engineering (ICSE |  |  |
| International Symposium on Software Testing and Analysis (ISSTA 2011) | . ACM, | 2016) | . IEEE/ACM, 559–570. |  |
| 12–22. | [26] Mockito 2020. Mockito. https://site.mockito.org/. Accessed: June 2020. |  |  |  |
| [6] Luciano Bello and Marco Pistoia. 2018. ARES: Triggering payload of evasive | [27] Monkey 2020. UI/Application Exerciser Monkey. https://developer.android.com/ |  |  |  |
| Android malware. In | Proceedings of the 5th International Conference on Mobile | studio/test/monkey. Accessed: June 2020. |  |  |
| Software Engineering and Systems (MOBILESoft@ICSE 2018) | . ACM, 2–12. | [28] Kevin Moran, Mario Linares-Vásquez, Carlos Bernal-Cárdenas, Christopher Ven- |  |  |
| [7] Ravi Bhoraskar, Seungyeop Han, Jinseong Jeon, Tanzirul Azim, Shuo Chen, | dome, and Denys Poshyvanyk. 2016. Automatically discovering, reporting and |  |  |  |
| Jaeyeon Jung, Suman Nath, Rui Wang, and David Wetherall. 2014. Brahmastra: | reproducing Android application crashes. In | Proceedings of the 2016 IEEE Inter- |  |  |
| Driving apps to test the security of third-party components. In | Proceedings of the | national Conference on Software Testing, Verification and Validation (ICST 2016) | . |  |
| 23rd USENIX Security Symposium (USENIX Security 2014) | . USENIX Association, | IEEE, 33–44. |  |  |
| 1021–1036. | [29] Damien Octeau, Patrick McDaniel, Somesh Jha, Alexandre Bartel, Eric Bodden, |  |  |  |
| [8] Cristian Cadar, Daniel Dunbar, Dawson R Engler, et al. 2008. KLEE: Unassisted and | Jacques Klein, and Yves Le Traon. 2013. Effective inter-component communica- |  |  |  |
| Automatic Generation of High-Coverage Tests for Complex Systems Programs. | tion mapping in Android: An essential step towards holistic security analysis. |  |  |  |
| In | Proceedings of the 8th USENIX Symposium on Operating Systems Design and | In | Proceedings of the 22nd USENIX Security Symposium (USENIX Security 2013) | . |
| Implementation (OSDI 2008) | . USENIX Association, 209–224. | USENIX Association, 543–558. |  |  |
| [9] Cristian Cadar, Vijay Ganesh, Peter M. Pawlowski, David L. Dill, and Dawson R. | [30] Riyad Parvez, Paul AS Ward, and Vijay Ganesh. 2016. Combining static analysis |  |  |  |
| Engler. 2007. EXE: A system for automatically generating inputs of death using | and targeted symbolic execution for scalable bug-finding in application binaries. |  |  |  |
| symbolic execution. In | Proceedings of the 13th ACM Conference on Computer and | In | Proceedings of the 26th Annual International Conference on Computer Science |  |
| Communications Security (CCS 2007) | . ACM. | and Software Engineering (CASCON 2016) | . IBM/ACM, 116–127. |  |
| [10] Leonardo De Moura and Nikolaj Bjørner. 2008. | Z3: An efficient SMT solver. | [31] Priyam Patel, Gokul Srinivasan, Sydur Rahaman, and Iulian Neamtiu. 2018. On the |  |  |
| In | Tools and Algorithms for the Construction and Analysis of Systems | . Springer, | effectiveness of random testing for Android: or how I learned to stop worrying and |  |
| 337–340. | love the monkey. In | Proceedings of the 13th International Workshop on Automation |  |  |
| [11] William Enck, Peter Gilbert, Byung-Gon Chun, Landon P. Cox, Jaeyeon Jung, | of Software Test (AST@ICSE 2018) | . ACM, 34–37. |  |  |
| Patrick McDaniel, and Anmol N. Sheth. 2010. TaintDroid: An information-flow | [32] David A Ramos and Dawson R Engler. 2015. Under-constrained symbolic exe- |  |  |  |
| tracking system for realtime privacy monitoring on smartphones. In | Proceedings | cution: Correctness checking for real code. In | Proceedings of the 24th USENIX |  |
| of the 9th USENIX Symposium on Operating Systems Design and Implementation | Security Symposium (USENIX Security 2015) | . USENIX Association, 49–64. |  |  |
| (OSDI 2010) | . USENIX Association, 393–407. | [33] Bahman Rashidi and Carol Fung. 2016. Xdroid: An Android permission control |  |  |
| [12] Yu Feng, Saswat Anand, Isil Dillig, and Alex Aiken. 2014. Apposcopy: Semantics- | using hidden Markov chain and online learning. In | Proceedings of the 2016 IEEE |  |  |
| based detection of Android malware through static analysis. In | Proceedings of | Conference on Communications and Network Security (CNS 2016) | . IEEE, 46–54. |  |
| the 22nd ACM SIGSOFT International Symposium on Foundations of Software | [34] Siegfried Rasthofer, Steven Arzt, Marc Miltenberger, and Eric Bodden. 2016. |  |  |  |
| Engineering (FSE 2014) | . ACM, 576–587. | Harvesting runtime values in Android applications that feature anti-analysis |  |  |
| [13] Patrice Godefroid, Nils Klarlund, and Koushik Sen. 2005. DART: Directed auto- | techniques. In | Proceedings of the 23rd Annual Network and Distributed System |  |  |
| mated random testing. In | Proceedings of the 2005 ACM SIGPLAN Conference on | Security Symposium (NDSS 2016) | . The Internet Society. |  |
| Programming Language Design and Implementation (PLDI 2005) | . ACM, 213–223. | [35] Siegfried Rasthofer, Steven Arzt, Stefan Triller, and Michael Pradel. 2017. Making |  |  |
| [14] Michael Grace, Yajin Zhou, Qiang Zhang, Shihong Zou, and Xuxian Jiang. 2012. | Malory behave maliciously: Targeted fuzzing of Android execution environ- |  |  |  |
| Riskranker: Scalable and accurate zero-day Android malware detection. In | Pro- | ments. In | Proceedings of the 39th IEEE/ACM International Conference on Software |  |
| ceedings of the 10th International Conference on Mobile Systems, Applications, and | Engineering (ICSE 2017) | . IEEE/ACM, 300–311. |  |  |
| Services (MobiSys 2012) | . ACM, 281–294. | [36] Martin C Rinard, Cristian Cadar, Daniel Dumitran, Daniel M Roy, Tudor Leu, and |  |  |
| [15] Tianxiao Gu, Chengnian Sun, Xiaoxing Ma, Chun Cao, Chang Xu, Yuan Yao, | William S Beebee. 2004. Enhancing Server Availability and Security Through |  |  |  |
| Qirun Zhang, Jian Lu, and Zhendong Su. 2019. | Practical GUI testing of An- | Failure-Oblivious Computing. In | Proceedings of the 6th USENIX Symposium on |  |
| droid applications via model abstraction and refinement. In | Proceedings of the | Operating System Design and Implementation (OSDI 2004) | . USENIX Association, |  |
| 41st IEEE/ACM International Conference on Software Engineering (ICSE 2019) | . | 303–316. |  |  |
| IEEE/ACM, 269–280. | [37] Kevin A Roundy, Paula Barmaimon Mendelberg, Nicola Dell, Damon McCoy, |  |  |  |
| [16] Yuyu He, Lei Zhang, Zhemin Yang, Yinzhi Cao, Keke Lian, Shuai Li, Wei Yang, | Daniel Nissani, Thomas Ristenpart, and Acar Tamersoy. 2020. The Many Kinds |  |  |  |
| Zhibo Zhang, Min Yang, Yuan Zhang, et al. 2020. TextExerciser: Feedback-driven | of Creepware Used for Interpersonal Attacks. In | Proceedings of the 2020 IEEE |  |  |
| Text Input Exercising for Android Applications. In | Proceedings of the 2020 IEEE | Symposium on Security and Privacy (SP 2020) | . IEEE. |  |

901

---

## Page 15

| Session 7B: Software Security #2 | ASIA CCS ’22, May 30–June 3, 2022, Nagasaki, Japan |  |  |  |
| --- | --- | --- | --- | --- |
| [38] Aleieldin Salem, Michael Hesse, Jona Neumeier, and Alexander Pretschner. 2019. | Network and Distributed System Security Symposium (NDSS 2016) | . The Internet |  |  |
| Towards Empirically Assessing Behavior Stimulation Approaches for Android | Society. |  |  |  |
| Malware. In | Proceedings of the 13th International Conference on Emerging Security | [49] Michelle Y Wong and David Lie. 2018. | Tackling runtime-based obfuscation |  |
| Information, Systems and Technologies (SECURWARE 2019) | . IARIA XPS Press, | in Android with TIRO. In | Proceedings of the 27th USENIX Security Symposium |  |
| 47–52. | (USENIX Security 2018) | . USENIX Association, 1247–1262. |  |  |
| [39] Koushik Sen, Darko Marinov, and Gul Agha. 2005. CUTE: A concolic unit testing | [50] Mingyuan Xia, Lu Gong, Yuanhao Lyu, Zhengwei Qi, and Xue Liu. 2015. Effective |  |  |  |
| engine for C. | ACM SIGSOFT Software Engineering Notes | 30, 5 (2005), 263–272. | real-time Android application auditing. In | Proceedings of the 2015 IEEE Symposium |
| [40] David Sounthiraraj, Justin Sahs, Garret Greenwood, Zhiqiang Lin, and Latifur | on Security and Privacy (SP 2015) | . IEEE, 899–914. |  |  |
| Khan. 2014. SMV-Hunter: Large scale, automated detection of SSL/TLS man- | [51] Lok Kwong Yan and Heng Yin. 2012. Droidscope: Seamlessly reconstructing the |  |  |  |
| in-the-middle vulnerabilities in Android apps. In | Proceedings of the 21st Annual | OS and Dalvik semantic views for dynamic Android malware analysis. In | Pro- |  |
| Network and Distributed System Security Symposium (NDSS 2014 | . The Internet | ceedings of the 21st USENIX Security Symposium (USENIX Security 2012) | . USENIX |  |
| Society. | Association, 569–584. |  |  |  |
| [41] Ting Su, Guozhu Meng, Yuting Chen, Ke Wu, Weiming Yang, Yao Yao, Geguang | [52] Shengqian Yang, Dacong Yan, Haowei Wu, Yan Wang, and Atanas Rountev. 2015. |  |  |  |
| Pu, Yang Liu, and Zhendong Su. 2017. | Guided, stochastic model-based GUI | Static control-flow analysis of user-driven callbacks in Android applications. In |  |  |
| testing of Android apps. In | Proceedings of the 11th Joint Meeting on Foundations | Proceedings of the 37th IEEE/ACM International Conference on Software Engineering |  |  |
| of Software Engineering (ESEC/FSE 2017) | . ACM, 245–256. | (ICSE 2015) | . IEEE/ACM, 89–99. |  |
| [42] Mingshen Sun, Tao Wei, and John Lui. 2016. TaintART: A practical multi-level | [53] Zhemin Yang, Min Yang, Yuan Zhang, Guofei Gu, Peng Ning, and Xiaoyang Sean |  |  |  |
| information-flow tracking system for Android runtime. In | Proceedings of the 2016 | Wang. 2013. AppIntent: Analyzing sensitive data transmission in Android for |  |  |
| ACM SIGSAC Conference on Computer and Communications Security (CCS 2016) | . | privacy leakage detection. In | Proceedings of the 2013 ACM SIGSAC Conference on |  |
| ACM, 331–342. | Computer and Communications Security (CCS 2013) | . ACM, 1043–1054. |  |  |
| [43] Kimberly Tam, Salahuddin J Khan, Aristide Fattori, and Lorenzo Cavallaro. 2015. | [54] Wei You, Bin Liang, Wenchang Shi, Peng Wang, and Xiangyu Zhang. 2017. Taint- |  |  |  |
| CopperDroid: Automatic Reconstruction of Android Malware Behaviors. In | Pro- | Man: An ART-compatible dynamic taint analysis framework on unmodified |  |  |
| ceedings of the 22nd Annual Network and Distributed System Security Symposium | and non-rooted Android devices. | IEEE Transactions on Dependable and Secure |  |  |
| (NDSS 2015) | . The Internet Society. | Computing (DSC) | 17, 1 (2017), 209–222. |  |
| [44] David Trabish, Andrea Mattavelli, Noam Rinetzky, and Cristian Cadar. 2018. | [55] Michal Zalewski. 2020. AFL. https://lcamtuf.coredump.cx/afl/. Accessed: June |  |  |  |
| Chopped symbolic execution. In | Proceedings of the 40th International Conference | 2020. |  |  |
| on Software Engineering (ICSE 2018) | . ACM, 350–360. | [56] Yuan Zhang, Min Yang, Bingquan Xu, Zhemin Yang, Guofei Gu, Peng Ning, X Sean |  |  |
| [45] Raja Vallée-Rai, Phong Co, Etienne Gagnon, Laurie Hendren, Patrick Lam, and | Wang, and Binyu Zang. 2013. Vetting undesirable behaviors in Android apps |  |  |  |
| Vijay Sundaresan. 1999. Soot - a Java bytecode optimization framework. In | Pro- | with permission use analysis. In | Proceedings of the 2013 ACM SIGSAC Conference |  |
| ceedings of the 1999 Conference of the Centre for Advanced Studies on Collaborative | on Computer and Communications Security (CCS 2013) | . ACM, 611–622. |  |  |
| Research (CASCON 1999) | . IBM, 13. | [57] Cong Zheng, Shixiong Zhu, Shuaifu Dai, Guofei Gu, Xiaorui Gong, Xinhui Han, |  |  |
| [46] Xiaolei Wang, Yuexiang Yang, and Sencun Zhu. 2018. Automated hybrid analysis | and Wei Zou. 2012. SmartDroid: an automatic system for revealing ui-based trig- |  |  |  |
| of Android malware through augmenting fuzzing with forced execution. | IEEE | ger conditions in Android applications. In | Proceedings of the 2nd ACM Workshop |  |
| Transactions on Mobile Computing | 18, 12 (2018), 2768–2782. | on Security and Privacy in Smartphones and Mobile Devices (SPSM 2012) | . ACM, |  |
| [47] Fengguo Wei, Sankardas Roy, and Xinming Ou. 2014. Amandroid: A precise and | 93–104. |  |  |  |
| general inter-component data flow analysis framework for security vetting of | [58] Yajin Zhou and Xuxian Jiang. 2013. Detecting passive content leaks and pollution |  |  |  |
| Android apps. In | Proceedings of the 2014 ACM SIGSAC Conference on Computer | in Android applications. In | Proceedings of the 20th Annual Network and Distributed |  |
| and Communications Security (CCS 2014) | . ACM, 1329–1341. | System Security Symposium (NDSS 2013) | . The Internet Society. |  |

[48] Michelle Y Wong and David Lie. 2016. IntelliDroid: A targeted input generator

for the dynamic analysis of Android malware. In Proceedings of the 23rd Annual

902
