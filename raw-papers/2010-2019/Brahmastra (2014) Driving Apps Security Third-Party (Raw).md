---
title: "81_Bhoraskar_et_al.,_Brahmastra_Driving_Apps_Security_Third-Party"
creator: "Adobe InDesign CC 2014 (Macintosh)"
pages: 17
---

# 81_Bhoraskar_et_al.,_Brahmastra_Driving_Apps_Security_Third-Party

> **總頁數**：17 頁

---

## Page 1

Brahmastra: Driving Apps to Test the Security of

Third-Party Components

Ravi Bhoraskar, Microsoft Research and University of Washington; Seungyeop Han,

University of Washington; Jinseong Jeon, University of Maryland, College Park;

Tanzirul Azim, University of California, Riverside; Shuo Chen, Jaeyeon Jung, Suman Nath,

and Rui Wang, Microsoft Research; David Wetherall, University of Washington

https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/bhoraskar

This paper is included in the Proceedings of the

23rd USENIX Security Symposium.

August 20–22, 2014 • San Diego, CA

ISBN 978-1-931971-15-7

Open access to the Proceedings of

the 23rd USENIX Security Symposium

is sponsored by USENIX

*[Image: Page 1 Image]*

*[Image: Page 1 Image]*

---

## Page 2

Brahmastra: Driving Apps to Test the Security of Third-Party Components

1 , 2 2 3 4

Ravi Bhoraskar , Seungyeop Han , Jinseong Jeon , Tanzirul Azim ,

1 1 1 1 2

Shuo Chen , Jaeyeon Jung , Suman Nath , Rui Wang , David Wetherall

1

2

3

4

We present an app automation tool called Brahmastra for

helping app stores and security researchers to test third-

party components in mobile apps at runtime. The main

challenge is that call sites that invoke third-party code

may be deeply embedded in the app, beyond the reach

of traditional GUI testing tools. Our approach uses static

analysis to construct a page transition graph and discover

execution paths to invoke third-party code. We then per-

form binary rewriting to “jump start” the third-party code

by following the execution path, efficiently pruning out

bile application developers to integrate external services

Microsoft Research

University of Washington

University of Maryland, College Park

University of California, Riverside

without isolation under existing mobile application mod-

els. This behavior is especially problematic because a

number of third-party libraries are widely used by many

applications; any vulnerability in these libraries can im-

pact a large number of applications. Indeed, our inter-

est in this topic grew after learning that popular SDKs

provided by Facebook and Microsoft for authentication

were prone to misuse by applications [30], and that ap-

plications often make improper use of Android cryptog-

raphy libraries [20].

focus is to develop tools that enable testers to observe in

runtime.

| Abstract | library and application run with the same privileges and |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| undesired executions. | Compared with the state-of-the- | In this paper, we present our solution to the problem |  |  |  |
| art GUI testing tools, Brahmastra is able to successfully | of | third-party component integration testing at scale | , in |  |  |
| analyse third-party code in 2 | . | 7 | × | more apps and decrease | which one party wishes to test a large number of appli- |
| test duration by a factor of 7. We use Brahmastra to un- | cations using the same third-party component for a po- |  |  |  |  |
| cover interesting results for two use cases: 175 out of | tential vulnerability. To be useful in the context of mo- |  |  |  |  |
| 220 children’s apps we tested display ads that point to | bile app stores, we require that a successful solution test |  |  |  |  |
| web pages that attempt to collect personal information, | many applications without human involvement. Observe |  |  |  |  |
| which is a potential violation of the Children’s Online | that it is | not | sufficient to simply test the third-party li- |  |  |
| Privacy Protection Act (COPPA); and 13 of the 200 apps | brary for bugs in isolation. This is because vulnerabil- |  |  |  |  |
| with the Facebook SDK that we tested are vulnerable to | ities often manifest themselves due to the interaction of |  |  |  |  |
| a known access token attack. | the application and the third-party component. Thus our |  |  |  |  |
| 1 | Introduction | situ | interactions between the third-party component and |  |  |
| Third-party libraries provide a convenient way for mo- | remote services in the context of a specific application at |  |  |  |  |
| in the application code base. Advertising that is widely | We began our research by exploring automated run- |  |  |  |  |
| featured in “free” applications is one example: 95% of | time analysis tools that drive mobile UIs (e.g., [5, 23, |  |  |  |  |
| 114,000 popular Android applications contain at least | 26]) to exercise the third-party component, but quickly |  |  |  |  |
| one known advertisement library according to a recent | found this approach to be insufficient. | Although these |  |  |  |
| study [22]. Social media add-ons that streamline or en- | tools are effective at executing | many | different code paths, |  |  |
| rich the user experience are another popular family of | they are often unable to reach | specific | interactions deep |  |  |
| third-party components. | For example, | Facebook Login | within the applications for a number of reasons that we |  |  |
| lets applications authenticate users with their existing | explore within this paper. | Instead, our approach lever- |  |  |  |
| Facebook credentials, and post content to their feed. | ages the structure of the app to improve test hit rate and |  |  |  |  |
| Despite this benefit, the use of third-party components | execution speed. To do this, we characterize an app by |  |  |  |  |
| is not without risk: if there are bugs in the library or the | statically building a graph of its pages and transitions |  |  |  |  |
| way it is used then the host application as a whole be- | between them. | We then use path information from the |  |  |  |
| comes vulnerable. This vulnerability occurs because the | graph to guide the runtime execution towards the third- |  |  |  |  |
| USENIX Association | 23rd USENIX Security Symposium | 1021 |  |  |  |

---

## Page 3

| party component under test. Rather than relying on GUI | nerable to the Facebook access token attack as discussed |  |  |
| --- | --- | --- | --- |
| manipulation (which requires page layout analysis) we | in | § | 8; A Facebook security team responded immediately |
| rewrite the application under test to directly invoke the | to our findings on 2/27/2014 and had contacted the af- |  |  |
| callback functions that trigger the desired page transi- | fected developers with the instructions to fix. |  |  |

tions.

2 Background

We built Brahmastra to implement our approach for

| Android apps. Our tool statically determines short exe- | As our system is developed in the context of Android, |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cution paths, and dynamically tests them to find one that | we begin by describing the structure of Android apps and |  |  |  |  |  |  |  |  |  |
| correctly invokes a target method in the third-party li- | support for runtime testing. |  |  |  |  |  |  |  |  |  |
| brary. | At this stage, behavior that is specific to the li- | Android app structure: | An Android app is organized as |  |  |  |  |  |  |  |
| brary is checked. Because our techniques do not require | a set of pages (e.g., Figure 1) that users can interact with |  |  |  |  |  |  |  |  |  |
| human involvement, Brahmastra scales to analyze a large | and navigate between. In Android, each page is repre- |  |  |  |  |  |  |  |  |  |
| number of applications. To show the benefits of our ap- | sented by an | activity | object. Each activity class repre- |  |  |  |  |  |  |  |
| proach, we use our tool for two new studies that con- | sents one kind of page and may be initialized with differ- |  |  |  |  |  |  |  |  |  |
| tribute results to the literature: 1) checking whether chil- | ent data, resulting in different | activity instances | . We |  |  |  |  |  |  |  |
| dren’s apps that source advertisements from a third-party | use the terms page and activity instance interchangeably. |  |  |  |  |  |  |  |  |  |
| comply with COPPA privacy regulations; and 2) check- | Each page contains various GUI elements (e.g., buttons, |  |  |  |  |  |  |  |  |  |
| ing that apps which integrate the Facebook SDK do not | lists, and images), known as | views | . A view can be as- |  |  |  |  |  |  |  |
| have a known security vulnerability [30]. | sociated with a callback function that is invoked when a |  |  |  |  |  |  |  |  |  |
| From our analysis of advertisements displayed in 220 | user interacts with the view. The callback function can |  |  |  |  |  |  |  |  |  |
| kids apps that use two popular ad providers, we find that | instantiate a new activity by using a late binding mecha- |  |  |  |  |  |  |  |  |  |
| 36% apps have displayed ads whose content is deemed | nism called | intent | . An intent encapsulates the descrip- |  |  |  |  |  |  |  |
| inappropriate for kids—such as offering free prizes, or | tion of a desired action (e.g., start a target activity) and |  |  |  |  |  |  |  |  |  |
| displaying sexual imagery. | We also discover that 80% | associated parameters. The main | activity | (or the first |  |  |  |  |  |  |
| apps have displayed ads with landing pages that attempt | page) of an app, defined in its manifest file, is started by |  |  |  |  |  |  |  |  |  |
| to collect personal information from the users, such as | the application launcher by passing a | START | intent to it. |  |  |  |  |  |  |  |
| name, address, and online contact information—which | For example, in Figure 1, clicking the “Done” button |  |  |  |  |  |  |  |  |  |
| can be a violation of the Children’s Online Privacy Pro- | on activity | A1 | invokes its event handler, which calls a |  |  |  |  |  |  |  |
| tection Act [6]. Apart from creating an unsafe environ- | callback function defined by the app developer. The call- |  |  |  |  |  |  |  |  |  |
| ment for kids, this also leaves the app developers vulner- | back constructs an intent to start activity | A2 | with nec- |  |  |  |  |  |  |  |
| able to prosecution, since they are considered liable for | essary parameter | P12 | . The | Activity Manager | then con- |  |  |  |  |  |
| all content displayed by their app. | structs an instance of | A2 | , and starts it with | P12 | as parame- |  |  |  |  |  |
| For our analysis of a vulnerability in third party login | ters. We refer to the documentation of Android internals |  |  |  |  |  |  |  |  |  |
| libraries, we run a test case proposed by Wang et al. [30] | for more details [2]. |  |  |  |  |  |  |  |  |  |
| against 200 Android apps that bundle Facebook SDK. | Automated dynamic analysis: | Recent works have used |  |  |  |  |  |  |  |  |
| We find that 13 of the examined apps are vulnerable. | a class of automation tools, commonly called a Mon- |  |  |  |  |  |  |  |  |  |
| Contributions: | We make two main contributions. The | key, that, given a mobile app binary, can automatically |  |  |  |  |  |  |  |  |
| first is Brahmastra, which embodies our hybrid approach | execute it and navigate to various parts (i.e., states) of |  |  |  |  |  |  |  |  |  |
| of static and dynamic analysis to solve the third-party | the app. | Examples include PUMA [23], DECAF [25], |  |  |  |  |  |  |  |  |
| component integration testing problem for Android apps. | AppsPlayground [26], A3E [14], and VanarSena [27]. A |  |  |  |  |  |  |  |  |  |
| We discuss our approach and key techniques in | § | 4 and | Monkey launches the app in a phone or an emulator, in- |  |  |  |  |  |  |  |
| their implementation in | § | 5. | We show in | § | 6 that our | teracts with it by emulating user interactions (e.g., click- |  |  |  |  |
| techniques work for a large fraction of apps while ex- | ing a button or swiping a page) to recursively visit vari- |  |  |  |  |  |  |  |  |  |
| isting tools such as randomized testing (Monkey) often | ous pages, and performs specific tasks (e.g., checking ad |  |  |  |  |  |  |  |  |  |
| fail. | We have made the static analysis part of Brah- | frauds in the page or injecting faults) on each page. |  |  |  |  |  |  |  |  |
| mastra available at | https://github.com/plum- | In Figure 1, a Monkey may be able to visit the se- |  |  |  |  |  |  |  |  |
| umd/redexer | . | quence of states | A1 | → | A2 | → | A3 | → | A4 | if it knows the |
| Our second contribution is an empirical study of two | right UI actions (e.g., type in mother’s name and select |  |  |  |  |  |  |  |  |  |
| security and privacy issues for popular third-party com- | “Due Date” in | A1 | ) to trigger each transition. However, if |  |  |  |  |  |  |  |
| ponents. We find potential violations of child-safety laws | Monkey clicks a button in | A3 | other than “Account”, the |  |  |  |  |  |  |  |
| by ads displayed in kids apps as discussed in | § | 7; several | app would navigate to a different activity. If the goal of |  |  |  |  |  |  |  |
| apps used in the wild display content in potential viola- | testing is to invoke specific methods (e.g., Facebook lo- |  |  |  |  |  |  |  |  |  |
| tion of COPPA due to the behavior of embedded compo- | gin as shown in the example), then without knowing the |  |  |  |  |  |  |  |  |  |
| nents. We find that several popular Android apps are vul- | structure of the app, a Monkey is likely to wander around |  |  |  |  |  |  |  |  |  |
| 1022 | 23rd USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |  |

---

## Page 4

| P12 | P34 |  |  |  |
| --- | --- | --- | --- | --- |
| E1 | E2 | E3 | E4 | E5 |
| A1 | A2 | A3 | A4 |  |

Figure 1: Activity sequences of com . alt12 . babybumpfree that invoke Facebook single sign-on window in the forth

activity ( A4 ): Clicking “I Agree” ( E1 ) then clicking “Done” ( E2 ) opens up A2 with the parameter, fromLoader : tru

( P12 ). Clicking “Settings” ( E3 ) in A2 opens up the settings activity, A3 and then clicking “Account” ( E4 ) opens up the

login activity, A4 with the parameter, WHICHCLASS : com . alt12 . babybumpcore . activity . settings . Settings . Finally,

clicking “Login with Facebook” ( E5 ) opens up the sign-on window within the same activity, A4 .

many activities until it reaches A4 , if it ever does. R1. Timeout: A Monkey can exhaust its time budget be-

fore reaching the target pages due to its trial-and-

3 Problem and Insights

error search of the application, especially for apps

| Our goal is to develop the ability to automatically and | with many pages that “blow up” quickly. |  |  |
| --- | --- | --- | --- |
| systematically test a large set of mobile apps that embed | R2. Human inputs: A Monkey is unable to visit pages |  |  |
| a specific third-party component for a potential vulnera- | that are reached after entering human inputs such |  |  |
| bility associated with the use of that component. | This | as login/password, or gestures beyond simple clicks |  |
| ability would let app store operators rapidly vet apps | that the automated tester cannot produce. |  |  |
| to contain security vulnerabilities caused by popular li- | R3. Unidentified elements: A Monkey fails to explore |  |  |
| braries. | It would let component developers check how | clickable UI elements that are not visible in the cur- |  |
| apps use or misuse their interfaces. It would also let se- | rent screen (e.g., hidden in an unselected tab) or are |  |  |
| curity researchers such as ourselves empirically assess | not activated yet (e.g., a “Like” button that is acti- |  |  |
| vulnerabilities related to third-party libraries. | vated only after the user registers to the app) or are |  |  |
| A straightforward approach is to use existing Mon- | not identified by underlying UI automation frame- |  |  |
| keys. Unfortunately, this approach does not work well: | work (e.g., nonstandard custom control). |  |  |
| it often fails to exercise the target third-party compo- | R4. Crashes: By stressing the UI, a Monkey exacerbates |  |  |
| nent of the app under test. Although recent works pro- | app crashes (due to bugs and external dependencies |  |  |
| pose techniques to improve various types of | coverages | , | such as the network) that limit exploration. |

computed as the fraction of app activities or methods in-

| voked by the Monkey, coverage still remains far from | Note that, unlike existing Monkeys, our goal is not to |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| perfect [26, 14, 13, 25, 27]. Moreover, in contrast to tra- | exhaustively execute all the possible code paths but to |  |  |  |  |
| ditional coverage metrics, our success metric is binary | execute | particular code paths | to invoke methods of in- |  |  |
| for a given app indicating whether the target third-party | terest in the third-party library. Therefore, our insight is |  |  |  |  |
| component (or a target method in it) is invoked (i.e., | hit | ) | to improve coverage by leveraging ways how third party |  |  |
| or not (i.e., | miss | ). | Our experiments show that even a | components are integrated with application code base. |  |
| Monkey with a good coverage can have a poor hit rate | These components are incorporated into an app at the |  |  |  |  |
| for a target third-party component that may be embed- | activity level. | Even if the same activity is instantiated |  |  |  |
| ded deep inside the app. We used an existing Monkey, | multiple times with different contents, third-party com- |  |  |  |  |
| PUMA that reports a | > | 90% activity coverage compared | ponents typically behave in the same way in all those |  |  |
| to humans [23], but in our experiments it was able to in- | instantiations. This allows us to restrict our analysis at |  |  |  |  |
| voke a target third-party component only in 13% of the | the level of | activity | rather than | activity instances | . Fur- |
| apps we tested (see | § | 6 for more details). On a close ex- | ther, even if an app contains a large number of activities, |  |  |
| amination, we discovered several reasons for this poor | only a small number of them may actually contain the |  |  |  |  |
| hit rate of existing Monkeys: | third-party component of interest. Invoking that compo- |  |  |  |  |
| USENIX Association | 23rd USENIX Security Symposium | 1023 |  |  |  |

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

---

## Page 5

nent requires successfully executing any and only one of

Using this insight, our testing system, Brahmastra,

“useful” paths that eventually invoke the target third-

Figure 1, Brahmastra considers the execution path A1 →

A2 → A3 → A4 for exploration and ignores many other

Such useful paths need to be identified statically be-

fore dynamic analysis is performed. The key challenges

in identifying such paths by static analysis arise due to

highly asynchronous nature of Android apps. We discuss

the challenges and our solution in § 4.

If such “jump start” is successful, Brahmastra can ignore

all preceding activities of the path. For example, in Fig-

ure 1, Brahmastra can directly start activity A3 , which can

case we need to find a different activity that is close to

the target, for which jump start succeeds. We discuss

these in detail in next section.

if they are invisible in the current screen.

analysis fast by visiting only a small number of activ-

tion helps Brahmastra to make transitions where a Mon-

|  |  |  " |  |
| --- | --- | --- | --- |
|   |   |   |  |
|  |   |  |  ! |
|  |    |    |  |

 

      

ch . smalltech . battery . free that shows multiple transi-

tion paths composed of multiple activities. Boxes and

ovals represent classes and methods. Solid edges corre-

spond to synchronous calls; (red) dotted edges indicate

activity transitions; and (blue) dashed edges represent

implicit calls due to user interactions. Three different

4 Design

1. Execution Planner statically analyzes the test app

binary and discovers an execution path to invoke the

target third-party method.

ity transitions.

| those activities. |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| uses three techniques described below to significantly |  |  |  |    |  |  |  |  |  |
| boost test hit rate and speed compared to a Monkey that |  | %%% |  |  |  |  |  |  |  |
| tries to reach all pages of the app. |   |   |  |  |  |  |  |  |  |
| Static path pruning: | Brahmastra considers only the |  |  |   |   |  |  |  |  |
| party methods and ignores all other “useless” paths. In |  |  | # |  |  |  |  |  |  |
| paths that do not lead to a target activity, | A4 | . | Figure | 2: | A | simplified | call | graph | of |
| Dynamic node pruning: | Brahmastra opportunistically | paths starting from | Home | . | onOptionItemSelected | () | reach |  |  |
| tries to start from an activity in the middle of the path. | AboutBox | . | onCreate | () | and share the remaining part. |  |  |  |  |
| lead to the target activity | A4 | . | Brahmastra requires as input: a test application binary; |  |  |  |  |  |  |
| Dynamic node pruning poses several challenges — | the names of target methods to be invoked within the |  |  |  |  |  |  |  |  |
| first, we need to enable jump-starting an arbitrary activity | context of the application; and the plug-in of a spe- |  |  |  |  |  |  |  |  |
| directly. Second, jump starting to the target activity may | cific security analysis to run once the target method is |  |  |  |  |  |  |  |  |
| fail due to incorrect parameters in the intent, in which | reached. Our system is composed of three parts: |  |  |  |  |  |  |  |  |
| Self-execution of app: | Brahmastra rewrites the app bi- | 2. | Execution Engine | receives execution paths from the |  |  |  |  |  |
| nary to automatically call methods that cause activity | Planner and launches the test app in one or multi- |  |  |  |  |  |  |  |  |
| transitions. The appropriate methods are found by static | ple emulators and automatically navigates through |  |  |  |  |  |  |  |  |
| analysis. In Figure 1, instead of clicking on the button | various pages according to the execution path. |  |  |  |  |  |  |  |  |
| with label “Done” in | A1 | , Brahmastra would invoke the | 3. | Runtime Analyzer | is triggered when the test app in- |  |  |  |  |
| onClick | () | method that would make the transition from | vokes the target method. It captures the test app’s |  |  |  |  |  |  |
| A1 | to | A2 | . The advantage over GUI-driven automation is | runtime state (e.g., page content, sensors accessed, |  |  |  |  |  |
| that it can discover activity-transitioning callbacks even | network trace) and runs the analysis plug-in. |  |  |  |  |  |  |  |  |
| In summary, our optimizations can make dynamic | 4.1 | Execution Planner |  |  |  |  |  |  |  |
| ities of an app. | More importantly, they also improve | The job of the Execution Planner is to determine: (1) the |  |  |  |  |  |  |  |
| the test hit rate of such analysis. | Faster analysis helps | activities that invoke the target third-party method; and |  |  |  |  |  |  |  |
| to avoid any timeouts ( | R1 | ). Dynamic node pruning can | (2) the method-level execution paths that lead to the tar- |  |  |  |  |  |  |
| bypass activities that require human inputs ( | R2 | ). In Fig- | get activities. | To accomplish these tasks, we statically |  |  |  |  |  |
| ure 1, Brahmastra can jump to | A3 | and bypass | A1 | that re- | analyze the app binary to construct a | call graph | that en- |  |  |
| quires selecting a | future | due date. Intent-driven naviga- | compasses its activities and interactions that cause activ- |  |  |  |  |  |  |
| key fails due to unidentified GUI elements ( | R3 | ). Finally, | Constructing call graph: | A call graph is a graph where |  |  |  |  |  |
| visiting fewer activities reduces the likelihood of crashes | vertices are methods and edges are causal relationship |  |  |  |  |  |  |  |  |
| ( | R4 | ). We quantitatively support these claims in | § | 6. | between method invocation. More precisely, there exists |  |  |  |  |
| 1024 | 23rd USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

*[Image: Page 5 Image]*

---

## Page 6

| 1 | ImageButton | b | = | (ImageButton) | 1 | // | layout/about_box_share.xml |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | findViewById(R.id.b1); | 2 | <Button | android:id="@id/mShareFacebook" |  |  |  |  |
| 3 | b.setOnClickListener( | new | OnClickListener() | { | 3 | style="@style/ABB_Black_ShareButton" | ... | /> |
| 4 | public | void | onClick(View | v) | { | 4 | <Button | android:id="@id/mShareTwitter" |
| 5 | ... | 5 | style="@style/ABB_Black_ShareButton" | ... | /> |  |  |  |
| 6 | }}); | 6 | // | values/styles.xml |  |  |  |  |

Figure 3: Example of a programmatic handler registra-

11

12

an edge from method m 1 to m 2 if m 1 invokes m 2. Based 13

on how m 2 is invoked by m 1, there are three types of

of one real app.

While synchronous edges can be identified easily by

scanning the app binary code, discovering other edges

1. Programmatic handler registrations: These are call-

backs explicitly bound to methods (e.g., event han-

dler of GUI elements) within the code. Figure 3

shows an example.

2. XML-based handler registrations: These are call-

3. Lifetime methods: These are methods provided by

the underlying framework that automatically make

transitions to other methods on specific events. Ex-

amples are splash screens and message boxes that

transition to next activities after a timeout or after

user acknowledgment, respectively.

7 <style name="ABB_Black_ShareButton ... >

8 <item name="android:onClick">onShareClick</item>

9 </style>

public void onShareClick(View v){

// different behavior depending on argument v

}

can be determined through layout and styles XML files.

component transitions via intent and bindings between

views and listeners. Finally, starting from the call sites,

we build backward transition paths, until public compo-

nents including the main activity are reached. If failed,

partial paths collected at the last phase will be returned.

voke the method as follows. From the call graph, we

can identify the activity boundaries such that all meth-

ods within the same boundary are invoked by the same

activity. Since an activity can be started only through

an activity transition edge in the call graph, any maxi-

mal connected component whose edges are either syn-

chronous or asynchronous define the boundary of an ac-

| tion. | onClick | () | is bound to | setOnClickListener | () | 10 | // | ch.smalltech.common.feedback.ShareActivity |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| edges: (1) synchronous edges, if | m | 1 directly calls | m | 2, (2) | Figure 4: Example of a XML-based handler registration |  |  |  |  |  |  |  |  |
| asynchronous edges, if | m | 1 invokes | m | 2 asynchronously, | observed from | ch | . | smalltech | . | battery | . | free | . Two buttons |
| and (3) activity transition edges, if | m | 1 starts an activity | share the | onShareClick | callback. The binding between |  |  |  |  |  |  |  |  |
| that automatically calls | m | 2. Figure 2 depicts a call graph | onShareClick | and | setOnClickListener | of each button |  |  |  |  |  |  |  |
| can be difficult. | To find activity transition edges, we | be very expensive. For example, the app shown in Fig- |  |  |  |  |  |  |  |  |  |  |  |
| rely on the fact that one activity can start another ac- | ure 1 declares 74 activities in the manifest; we find at |  |  |  |  |  |  |  |  |  |  |  |  |
| tivity by generating an intent and passing it to the | least 281 callbacks over 452 registering points; and its |  |  |  |  |  |  |  |  |  |  |  |  |
| startActivity | () | method. | We perform constant propa- | call graph is composed of 1,732 nodes and 17,723 edges. |  |  |  |  |  |  |  |  |  |
| gation analysis [12] so as to track such intent creations | To address this, we use two optimizations to compute a |  |  |  |  |  |  |  |  |  |  |  |  |
| and detect activity transitions. We also conduct class hi- | partial | call graph that includes target methods and the |  |  |  |  |  |  |  |  |  |  |  |
| erarchy analysis [19] to conservatively determine possi- | start activity methods. First, we exclude system’s static |  |  |  |  |  |  |  |  |  |  |  |  |
| ble receiver types for dynamic dispatch, where the target | libraries and other third-party libraries that are not re- |  |  |  |  |  |  |  |  |  |  |  |  |
| call sites depend on the runtime types of the receivers. | lated to the target methods. Second, we search transition |  |  |  |  |  |  |  |  |  |  |  |  |
| To discover asynchronous edges, we need to consider | paths backwards on call graph. | We pinpoint call sites |  |  |  |  |  |  |  |  |  |  |  |
| all the different ways asynchronous methods can be in- | of target methods while walking through bytecodes. We |  |  |  |  |  |  |  |  |  |  |  |  |
| voked by a mobile app: | then construct a partial call graph, taking into accounts |  |  |  |  |  |  |  |  |  |  |  |  |
| backs specified in the layout or resource XML files. | Determining target activity(s): | Given the call graph |  |  |  |  |  |  |  |  |  |  |  |
| Figure 4 shows an example. | and a target method, we determine the activities that in- |  |  |  |  |  |  |  |  |  |  |  |  |
| To discover the first and third types, we use constant | tivity. In Figure 2, bigger rectangles denote the activity |  |  |  |  |  |  |  |  |  |  |  |  |
| propagation analysis to trace callbacks attached to var- | boundaries. Given the boundaries, we identify the activ- |  |  |  |  |  |  |  |  |  |  |  |  |
| ious event handlers. To handle the second case, we parse | ities that contain the target method. |  |  |  |  |  |  |  |  |  |  |  |  |
| layout XML files corresponding to each activity to figure | Finding activity transition paths: | Reaching a target ac- |  |  |  |  |  |  |  |  |  |  |  |
| out the binding between UI elements and callback meth- | tivity from the start activity may require several transi- |  |  |  |  |  |  |  |  |  |  |  |  |
| ods. | tions between multiple activities. For example, in Fig- |  |  |  |  |  |  |  |  |  |  |  |  |
| Efficient call graph computation: | A call graph can be | ure 2, navigating from the start activity ( | HomeFree | ) to |  |  |  |  |  |  |  |  |  |
| extremely large, thus computing the entire call graph can | a target activity ( | ShareActivity | ) requires three transi- |  |  |  |  |  |  |  |  |  |  |
| USENIX Association | 23rd USENIX Security Symposium | 1025 |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 7

| tions. This implies that Brahmastra requires techniques | We address this limitation with a technique we develop |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| for automatic activity transitions, which we describe in | called | self execution | . At a high level, we rewrite app bi- |  |  |  |  |  |  |  |  |  |  |  |
| the next subsection. | Second, a target activity may be | naries to insert code that automatically invokes the call- |  |  |  |  |  |  |  |  |  |  |  |  |
| reachable via multiple transition paths. While the short- | backs that trigger desired activity transitions, even if their |  |  |  |  |  |  |  |  |  |  |  |  |  |
| est path is more attractive for fast exploration, the path | corresponding GUI elements are not visible. Such code |  |  |  |  |  |  |  |  |  |  |  |  |  |
| may contain blocking activities and hence not executable | is inserted into all the activities in a useful path such that |  |  |  |  |  |  |  |  |  |  |  |  |  |
| by Brahmastra. Therefore, Brahmastra considers all tran- | the rewritten app, after being launched in a phone or an |  |  |  |  |  |  |  |  |  |  |  |  |  |
| sition paths (in increasing order of their length); if exe- | emulator, would automatically make a series of activity |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cution of a short path fails, it tries a longer one. | transitions to the target activity, without any external in- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Given the call graph | G | , the Planner computes a small | teraction with its GUI elements. |  |  |  |  |  |  |  |  |  |  |  |
| set | P | of acyclic transition paths that the Execution En- | Jump start: | Brahmastra goes beyond the above opti- |  |  |  |  |  |  |  |  |  |  |
| gine need to consider. | P | includes a path if and only if | mization with a node pruning technique called “jump |  |  |  |  |  |  |  |  |  |  |  |
| it terminates at a target activity without a cycle and is | start”. Consider a path | p | = ( | a | 0 | , | a | 1 | , . . . , | at | ) | , where | at | is a |
| not a suffix of any other path in | P | . This ensures that | P | is | target activity. Since we are interested only in the target |  |  |  |  |  |  |  |  |  |
| useful, complete (i.e., Execution Engine does not need to | activity, success of Brahmastra is not affected by what |  |  |  |  |  |  |  |  |  |  |  |  |  |
| consider any path not in | P | ), and compact. For instance | activity | ai | in | p | the execution starts from, as long as the |  |  |  |  |  |  |  |
| Figure 5 shows one out of three paths contained in | P | . | last activity | at | is successfully executed. In other words, |  |  |  |  |  |  |  |  |  |
| HomeFree;.onCreate | one can execute any suffix of | p | without affecting the hit |  |  |  |  |  |  |  |  |  |  |  |
| ---> | Home;.onCreate | rate. The jump start technique tries to execute a suffix — |  |  |  |  |  |  |  |  |  |  |  |  |
| -#-> | Home;.onOptionsItemSelected | instead of the whole — useful path. This can improve |  |  |  |  |  |  |  |  |  |  |  |  |
| ---> | Home;.showAbout | Brahmastra’s speed since it can skip navigating through |  |  |  |  |  |  |  |  |  |  |  |  |
| ---> | AboutBox;.onCreate | few activities (in the prefix) of a useful path. | Interest- |  |  |  |  |  |  |  |  |  |  |  |
| -#-> | AboutBox;.onLikeClicked | ingly, this can also improve the hit rate of Brahmastra. |  |  |  |  |  |  |  |  |  |  |  |  |
| ---> | ShareActivity;.onCreate | For example, if the first activity | a | 0 requires human in- |  |  |  |  |  |  |  |  |  |  |

-#-> ShareActivity;.onShareClick

---> ShareActivity;.share

---> ShareActivity;.onFacebookShare

4.2 Execution Engine

ties from the beginning of the path (by using techniques

described later). Exploration can stop as soon as a target

puts such as user credentials that an automation system

cannot provide, any effort to go beyond state a 0 will fail.

Note that directly executing an activity ai , i > 0, with-

out navigating to it from the start activity a 0, may fail.

ity at is successfully reached or all the suffixes are tried.

tries to execute the suffixes in increasing order of their

length. The algorithm returns true on successful execu-

runtime.

| Figure | 5: | An | example | path | information | for | This is because some activities are required to be invoked |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ch | . | smalltech | . | battery | . | free | Dashed | arrows | stand | with specific intent parameters. In such cases, Brahmas- |  |
| for | explicit | calls | or | activity | transition, | whereas | ar- | tra tries to jump start to the previous activity | ai | − | 1 in the |
| rows with a hash tag represent implicit invocations, | path. In other words, Brahmastra progressively tries to |  |  |  |  |  |  |  |  |  |  |
| which are either callbacks due to user interactions or | execute suffixes of useful paths, in increasing order of |  |  |  |  |  |  |  |  |  |  |
| framework-driven callbacks, such as lifecycle methods. | lengths, until the jump start succeeds and the target activ- |  |  |  |  |  |  |  |  |  |  |
| P | can be computed by breadth-first traversals in | G | , | Algorithm 1 shows the pseudocode of how execution |  |  |  |  |  |  |  |
| starting from each target activity and traversing along the | with jump start works. | Given the set of paths, the al- |  |  |  |  |  |  |  |  |  |
| reverse direction of the edges. | gorithm first generates suffixes of all the paths. Then it |  |  |  |  |  |  |  |  |  |  |
| The useful paths | P | produced by the Execution Planner | tion of any suffix. Note that Algorithm 1 needs to know |  |  |  |  |  |  |  |  |
| already give an opportunity to prune exploration: Brah- | if a path suffix has been successfully executed (line 9). |  |  |  |  |  |  |  |  |  |  |
| mastra considers only paths in | P | (and ignore others), and | We inject lightweight logging into the app binary to de- |  |  |  |  |  |  |  |  |
| for each path, it can simply navigate through its activi- | termine when and whether target methods are invoked at |  |  |  |  |  |  |  |  |  |  |
| method is invoked. | 4.3 | Runtime Analyzer |  |  |  |  |  |  |  |  |  |
| Rewriting apps for self-execution: | One might use a | Runtime Analyzer collects various runtime states of the |  |  |  |  |  |  |  |  |  |
| Monkey to make activity transitions along useful paths. | test app and makes it available to custom analysis plug- |  |  |  |  |  |  |  |  |  |  |
| Since a Monkey makes such transitions by interacting | ins for scenario-specific analysis. Runtime states include |  |  |  |  |  |  |  |  |  |  |
| with GUI elements, this requires identifying mapping be- | UI structure and content (in form of a DOM tree) of the |  |  |  |  |  |  |  |  |  |  |
| tween GUI elements and transitioning activities and in- | current app page, list of system calls and sensors invoked |  |  |  |  |  |  |  |  |  |  |
| teract with only the GUI elements that make desired tran- | by the current page, and network trace due to the current |  |  |  |  |  |  |  |  |  |  |
| sitions. | page. We describe two plug-ins and analysis results in |  |  |  |  |  |  |  |  |  |  |
| 1026 | 23rd USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |  |  |

---

## Page 8

| Algorithm 1 | Directed Execution | 1 | // | { | v3 | → | this | } |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1: | INPUT: | Set of useful paths | P | from the Planner | 2 | new-instance | v0, | Landroid/content/Intent; |  |  |  |  |
| 2: | OUTPUT: | Return | true | if execution is successful | 3 | // | { | v0 | → | Intent(), | ... | } |

3: S ← set of suffixes of all paths in P

4: for i from 0 to ∞ do

7: return false

8: for each path suffix p in Si do

later sections.

5 Implementation of Brahmastra

5.1 Execution Planner

perform data-flow analysis, along with call graph and

control-flow graph.

5.2 App Rewriting

4 const-class v1, ...AboutBox;

5 // { v1 → Clazz(AboutBox), ... }

6 invoke-direct {v0, v3, v1}, ...Intent;.<init>

9 // { ... }

newly added values are shown.

ease analysis and manipulation. The re-writing tool is

composed of Soot’s class visitor methods and an An-

of asynchronous edges described in § 4.1). For program-

matic and XML-based registrations, the rewriter finds the

5.3 Jump Start

to it. We use the Android Debug Bridge (ADB) [4] for

performing jump start. ADB allows us to create an intent

| 5: | Si | ← | set of paths of length | i | in | S | 7 | // | { | v0 | → | Intent(AboutBox), | ... | } |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6: | if | Si | is empty | then | 8 | invoke-virtual | {v3, | v0}, | ...;.startActivity |  |  |  |  |  |
| 9: | if | Execute | ( | p | ) | = | true then | Figure 6: An example bytecode of activity transition ex- |  |  |  |  |  |  |
| 10: | return true | cerpted from | ch | . | smalltech | . | battery | . | free | . Mappings be- |  |  |  |  |
| 11: | tween bytecode represent data-flow information, which |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 12: | return false | shows what values registers | must | have. Only modified or |  |  |  |  |  |  |  |  |  |  |
| We implement Brahmastra for analyzing Android apps, | droid XML parser. Given an app binary and an execution |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and use the tool to perform two security analyses which | path, the rewriter generates a rewritten binary which ar- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| we will describe in | § | 7 and | § | 8. | This section describes | tificially invokes a callback method upon the completion |  |  |  |  |  |  |  |  |
| several highlights of the tool, along with practical chal- | of the exercising the current activity, triggering the next |  |  |  |  |  |  |  |  |  |  |  |  |  |
| lenges that we faced in the implementation process and | activity to be launched. The inserted code depends on the |  |  |  |  |  |  |  |  |  |  |  |  |  |
| how we resolved them. | type of the edge found by the Planner (Recall three kinds |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Static analyses for constructing a call graph and find- | view | attached to it — by parsing the activity code, and |  |  |  |  |  |  |  |  |  |  |  |  |
| ing transition paths to target methods are performed us- | the manifest respectively — and invokes the appropri- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ing Redexer [24], a general purpose bytecode rewriting | ate UI interaction on it after it has completed loading. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| framework for Android apps. | Redexer takes as input | Lifetime methods are invoked by the Android framework |  |  |  |  |  |  |  |  |  |  |  |  |
| an Android app binary (APK file) and constructs an in- | directly, and the rewriter skips code insertion for these |  |  |  |  |  |  |  |  |  |  |  |  |  |
| memory data structure representing | DEX | file for various | cases. In other cases, the rewriter inserts a timed call to |  |  |  |  |  |  |  |  |  |  |  |
| analyses. Redexer offers several utility functions to ma- | the transition method directly, to allow the activity and |  |  |  |  |  |  |  |  |  |  |  |  |  |
| nipulate such | DEX | file and provides a generic engine to | any dependencies of the method to load completely. |  |  |  |  |  |  |  |  |  |  |  |
| For special APIs that trigger activity transitions, e.g., | Jump start requires starting an activity even if it is not de- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Context | . | startActivity | () | , we perform constant propa- | fined as the | Launcher | activity in the app. To achieve that, |  |  |  |  |  |  |  |
| gation analysis (see Appendix A for details) and identify | we manipulate the manifest file of the Android app. The |  |  |  |  |  |  |  |  |  |  |  |  |  |
| a target activity stored inside the intent. | Figure 6 de- | Intent | . | ACTION MAIN | entry in the manifest file declares |  |  |  |  |  |  |  |  |  |
| picts example bytecode snippets that create and initial- | activities that Android activity manager can start directly. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ize an intent (lines 2 and 6), along with the target activ- | To enable jump start, we insert an | ACTION MAIN | entry for |  |  |  |  |  |  |  |  |  |  |  |
| ity (line 4), and starts that activity via | startActivity | () | each activity along the path specified, so that it can be |  |  |  |  |  |  |  |  |  |  |  |
| (line 8). | Mappings between each bytecode show how | started by the Execution Engine. Manifest file also de- |  |  |  |  |  |  |  |  |  |  |  |  |
| we accumulate data-flow information, from empty intent | clares an intent filter, which determines the sources from |  |  |  |  |  |  |  |  |  |  |  |  |  |
| through class name to intent with the specific target ac- | which an activity may be started, which we modify to |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tivity. We apply the same analysis to bindings between | allow the Execution Engine to launch the activity. The |  |  |  |  |  |  |  |  |  |  |  |  |  |
| views and listeners. | Engine then invokes desired activity by passing an intent |  |  |  |  |  |  |  |  |  |  |  |  |  |
| We use the Soot framework [29] to perform the byte- | with the desired parameters and target, and then passes |  |  |  |  |  |  |  |  |  |  |  |  |  |
| code rewriting that enables self execution. Dexpler [7] | it to the Android Activity Manager. | The activity man- |  |  |  |  |  |  |  |  |  |  |  |  |
| converts an Android app binary into Soot’s intermedi- | ager in turn loads the appropriate app data and invokes |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ate representation, called Jimple, which is designed to | the specified activity. Starting the (jump started) activ- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| USENIX Association | 23rd USENIX Security Symposium | 1027 |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 9

| ity immediately activates self execution from that activ- |  |  |  |  |
| --- | --- | --- | --- | --- |
| ity onwards. |  |  |  |    |
| 6 | Evaluation of Brahmastra |  |  |  |

We evaluate Brahmastra in terms of two key metrics: (1)

hit rate, i.e., the fraction of apps for which Brahmastra

can invoke any of target methods, and (2) speed, i.e.,

time (or number of activity transitions) Brahmastra takes

tra has a hit. Since we are not aware of any existing tool

that can achieve the same goal, we compare Brahmas-

tra against a general Android app exploration tool called,

PUMA [23]. This prototype is the best-performing Mon-

key we were able to find that is amenable to experimen-

6.1 Experiment Methodology

book SDK because this is a popular SDK and its meth-

ods are often invoked only deep inside the apps. Using

SDK version 3.0.2b or earlier 2

Figure 7: Target methods for evaluation

tool chain, e.g., crash on the emulator or have issues with

apktool [1] since our analysis depends on the disassem-

bled code of an apk file. This leaves us with 1,010 apps.

2 The later version of Facebook SDK was released in the middle

of data collection and appears to use different methods to display a



#









Figure 8: Failure causes of Brahmastra and PUMA.

ods with signatures of target methods. For Brahmastra,

we consider only 5 of all paths generated by the Execu-

6.2 Hit Rate

coverage ( > 90% compared to humans) reported in [23],

successfully able to invoke a target method in 344 (34%)

apps, a 2 . 7 × improvement over PUMA. A closer exam-

ination of our results, as shown in Table 1, reveals that

Brahmastra’s technique can help circumventing all the

key reasons are as follows:

Blocking page: Even if jump start succeeds, successive

activity transition may fail on a blocking page. Brah-

more blocking pages than PUMA only because Brah-

| to invoke a target method in an app for which Brahmas- |   |    |  |    |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tation. | In terms of speed and coverage, PUMA is far | App execution: | In order to determine if Brahmastra or |  |  |  |  |
| better than a basic “random” Monkey. PUMA incorpo- | PUMA is able to reach a program point that invokes the |  |  |  |  |  |  |
| rates many key optimizations in existing Monkeys such | target method, we instrument apps. The instrumentation |  |  |  |  |  |  |
| as AppsPlayground [26], A3E [14], and VanarSena [27] | detects when any of the target methods are invoked dur- |  |  |  |  |  |  |
| and we expect it to perform at least on a par with them. | ing runtime, by comparing signatures of executing meth- |  |  |  |  |  |  |
| Target method: | For the experiments in this section, we | tion Planner. For PUMA, we explore each app for up to |  |  |  |  |  |
| configure Brahmastra to invoke authentication methods | 250 steps; higher timeouts significantly increase overall |  |  |  |  |  |  |
| in the Facebook SDK for Android. | 1 | We choose Face- | testing time for little gain in hit rate. |  |  |  |  |
| the public documentation for the Facebook SDK for An- | In our experiments, PUMA was able to successfully in- |  |  |  |  |  |  |
| droid, we determined that it has two target methods for | voke a target method in 127 apps (13%). | Note that |  |  |  |  |  |
| testing. Note that apps in our dataset use the Facebook | PUMA’s hit rate is significantly lower than its activity |  |  |  |  |  |  |
| Lcom/facebook/android/Facebook;->authorize | highlighting the difficulty in invoking specific program |  |  |  |  |  |  |
| Lcom/facebook/android/Facebook;->dialog | points deep inside an app. In contrast, Brahmastra was |  |  |  |  |  |  |
| Apps: | We crawled 12,571 unique apps from the Google | root causes for PUMA’s poor hit rate as mentioned in | § | 3. |  |  |  |
| Play store from late December 2012 till early January | We | now | investigate | why | PUMA | and | Brahmastra |
| 2013. These apps were listed as 500 most popular free | sometimes fail to invoke the target method. For PUMA, |  |  |  |  |  |  |
| apps in each category provided by the store at the time. | this is due to the aforementioned four cases. | Figure 8 |  |  |  |  |  |
| Among them, we find that 1,784 apps include the Face- | shows the distribution of apps for which PUMA fails due |  |  |  |  |  |  |
| book SDK for Android. We consider only apps that in- | to specific causes. | As shown, all the causes happen in |  |  |  |  |  |
| voke the authentication method—Over 50 apps appear to | practice. The most dominant cause is the failure to find |  |  |  |  |  |  |
| have no call sites to Facebook APIs, and over 400 apps | UI controls to interact with, which is mostly due to com- |  |  |  |  |  |  |
| use the API but do not invoke any calls related to autho- | plex UI layouts of the popular apps we tested. Figure 8 |  |  |  |  |  |  |
| rization. We also discard apps that do not work with our | also shows the root causes for Brahmastra’s failure. The |  |  |  |  |  |  |
| 1 | https://developers.facebook.com/docs/ | mastra fails for 20% of the apps due to this cause. We |  |  |  |  |  |
| android/login-with-facebook | would like to emphasize that Brahmastra experiences |  |  |  |  |  |  |
| login screen. However, we find that almost no apps in our data set had | mastra explores many paths that PUMA does not (e.g., |  |  |  |  |  |  |
| adapted the new version yet. | because those paths are behind a custom control that |  |  |  |  |  |  |
| 1028 | 23rd USENIX Security Symposium | USENIX Association |  |  |  |  |  |

---

## Page 10

Case Apps 

| R1: Timeout in PUMA, success in Brahmastra | 62% |
| --- | --- |
| R2: Blocking page in PUMA, success in Brahmastra | 48% |
| R3: Unknown control in PUMA, success in Brahmastra | 43% |

Table 1: % of apps for which Brahmastra succeeds but

PUMA fails due to various reasons mentioned in § 3.

invoke the associated callback) and many of these paths

paths, it would have failed as well due to these blocking

pages.

Crash: Jump start can crash if the starting activity ex-

pects specific parameters in the intent and Brahmastra

Custom components: Execution Planner may fail to

,

which can be used to override standard event handlers,

thus breaking our model of standard Android apps. With-

out useful paths, Brahmastra can fail to invoke the target

methods. In our experiments, this happens with 16% of

the apps. We leave as future work a task to extend Execu-

tion Planner to handle custom components. We find that

PUMA also failed 91% on these apps, proving the dif-

ficulty of navigating apps with custom components. In

fact, PUMA suffers much more than Brahmastra due to

custom components.

paths. This suggests that considering more paths is likely

to improve the hit rate. Additionally, we should select

the paths to avoid any nodes or edges for which explo-

ui/custom-components.html

$

"  

'

!



 ! " # $ 

PUMA

behavior was not encoded in the instrumentation engine.

and more views would increase hit rate. We plan to ex-

plore such optimizations in future. Finally, PUMA (and

other Monkeys) and Brahmastra use fundamentally dif-

ferent techniques to navigate between app pages and it

might be possible to combine them in a single system

where PUMA is used if Brahmastra fails (or vice versa).

In our experiments, such a hybrid approach would give

an overall hit rate of 39% (total 397 apps).

6.3 Speed

7 fold speedup.

7 Analysis of Ads in Kids Apps

inappropriate to children.

| R4: Crash in PUMA, success in Brahmastra | 30% | # |  |    |
| --- | --- | --- | --- | --- |
| PUMA cannot interact with, but Brahmastra can find and |  |     |  |  |
| contain blocking pages. If PUMA tried to explore those | Figure 9: | Test speed comparison of Brahmastra and |  |  |
| fails to provide that. Brahmastra fails for 7% of the apps | apps, Brahmastra deemed a page blocked due to UI el- |  |  |  |
| due to this cause. | ements in the Android SDK (e.g., list elements) whose |  |  |  |
| find useful paths if the app uses custom components | 3 | An engineering effort in special-case handling of these |  |  |
| Improving the hit rate: | There are several ways we can | We use the number of activity transitions required to |  |  |
| further improve the hit rate of Brahmastra. | First, 16% | reach the target activity as a proxy for speed, since the |  |  |
| failures of Brahmastra come because the static analysis | actual time will vary depending on a variety of com- |  |  |  |
| fails to identify useful paths. A better static analysis that | putational factors (e.g., network speed, device specifi- |  |  |  |
| can discover more useful paths can improve Brahmas- | cations). | In Figure 9, we plot the CDF of the number |  |  |
| tra’s hit rate. | Second, in our experiments, Brahmastra | of transitions required to reach the target activity for the |  |  |
| tried only up to 5 randomly selected useful paths to in- | apps which are successfully tested by both Brahmastra |  |  |  |
| voke the target method and gave up if they all failed. In | and PUMA. Since Brahmastra prunes away many un- |  |  |  |
| many apps, our static analysis found many tens of use- | necessary paths using static analysis, it runs faster than |  |  |  |
| ful paths, and our results indicate that the more paths we | PUMA that suffers from uninformed activity transitions |  |  |  |
| tried, the better was the hit rate. More specifically, Brah- | and large fanout in the activity transition graphs. On av- |  |  |  |
| mastra succeeded for 207 apps after considering only | erage, PUMA requires 18.7 transitions per app, while |  |  |  |
| one path, and for 344 apps after considering up to five | Brahmastra requires 2.5 transitions per app, resulting in |  |  |  |
| ration failed in previously considered paths instead of | Our first scenario is to use Brahmastra to study whether |  |  |  |
| choosing them randomly. | In 72 apps, Brahmastra was | ad libraries for Android apps meet guidelines for protect- |  |  |
| unable to find the binding between a callback method | ing the online privacy of children. We give results for two |  |  |  |
| and the UI element associated with it, causing it to fall | popular ad components embedded in 220 kids apps. Our |  |  |  |
| back on a direct invocation of the callback method. | A | analysis shows that 80% of the apps displayed ads with a |  |  |
| better static analysis can help in this case as well. In 22 | link to landing pages that have forms for collecting per- |  |  |  |
| 3 | http://developer.android.com/guide/topics/ | sonal information, and 36% apps displayed ads deemed |  |  |
| USENIX Association | 23rd USENIX Security Symposium | 1029 |  |  |

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

*[Image: Page 10 Image]*

---

## Page 11

7.1 Motivation and Goals proxy [8]. We install the Fiddler SSL certificate on the

The Children’s Online Privacy Protection Act (COPPA)

lays down a variety of stipulations that mobile app de-

velopers must follow if their apps are directed at children

under 13 years old [6]. In particular, COPPA disallows

the collection of personal information by these apps un-

less the apps have first obtained parental consent.

COPPA holds the app developer responsible for the

personal information collected by the embedded third

party components as well as by the app’s code [6]. Since

it is common to see ad components included in free apps,

we aim to measure the extent of potentially non-COPPA-

compliant ad components in kids apps. Specifically, our

Our second goal is to test whether content displayed in

in-app ads or landing pages is appropriate for children .

Since this kind of judgement is fundamentally subjective,

7.2 Testing Procedure

tomatically drive apps to display ads. In this study, we

focus on two popular ad libraries, AdMob and Millen-

nial Media, because they account for over 40% of free

Android apps with ads [11]. To get execution paths that

produce ads, we use the following target methods as in-

put to Brahmastra:

Collecting ads & landing pages: We redirect all the net-

phone emulator as a trusted certificate to allow it to ex-

amine SSL traffic as well. We then identify the requests

made by the ad libraries to their server component us-

ing domain names. Once these requests are collected,

we replay these traces (several times, over several days),

to fetch ad data from the ad servers as if these requests

were made from these apps. This ad data is generally in

the form of a JSON or XML object that contains details

about the kind of ad served (image or text), the content

to display on the screen (either text or the URL of an im-

age), and the URL to redirect to if the ad is clicked upon.

We record all of above for analysis.

ter out noise.

7.3 Results

Play store for apps with the same package name.

Starting from slightly over 4,000 apps in the Kids cat-

Results: We collected ads from each of the 220 apps

over 5 days, giving us a total collection of 566 unique

ads, and 3,633 unique landing pages. Using WoT, we de-

termine that 183 out of the 3,633 unique landing pages

have the child-safety score below 60, which fall in the

“Unsatisfactory”, “Poor” or “Very Poor” categories. 189

not contain child-safety ratings for 1,806 pages, so these

| first goal is to determine | whether in-app ads or landing | Analyzing ads & landing pages: | We use two methods |
| --- | --- | --- | --- |
| pages pointed by these ads present forms that collect per- | to characterize ads and landing pages. | First, for each |  |
| sonal information | . Although displaying collection forms | landing page URL collected, we probe the Web of Trust |  |
| itself is not a violation, children might type in requested | (WoT) database [9] to get the “child safety” score. Sec- |  |  |
| personal information, especially if these websites claim | ond, to better understand the reasons why landing pages |  |  |
| to offer free prizes or sweepstakes. | In such cases, if | or ads may not be appropriate for children, we use crowd- |  |
| these ads or landing pages do collect personal informa- | sourcing (via Amazon Mechanical Turk [3]) to label each |  |  |
| tion without explicit parental consent, this act could be | ad and landing page and to collect detailed information |  |  |
| considered as a violation according to COPPA. Since it is | such as the type of personal information that landing |  |  |
| difficult to model these legal terms into technical specifi- | pages collect. | As data collected from crowds may in- |  |
| cations, we only report potential concerns in this section. | clude inconsistent labeling, we use majority voting to fil- |  |  |
| we show the breakdown of content categories as labeled | Dataset: | We collected our dataset in January 2014. To |  |
| by human testers. | find apps intended for children, we use a list of apps |  |  |
| Note that runtime observation is critical for this test- | categorized as “Kids” in Amazon’s Android app store | 4 | . |
| ing, since ads displayed within apps change dynamically | Since apps offered from the Amazon store are protected |  |  |
| depending on the inventory of ads at the time of request. | with DRM and resist bytecode rewriting, we crawled the |  |  |
| The testing has two steps. For a given app, we first col- | egory, we found 699 free apps with a matching package |  |  |
| lect ads displayed within apps and landing pages that are | name in the Play store. Among these, we find 242 apps |  |  |
| pointed by the ads. Second, for each ad and landing page, | that contain the AdMob or Millennial Media ad libraries. |  |  |
| we determine: (1) whether they present forms to collect | Using Brahmastra, we were successfully able to retrieve |  |  |
| personal information such as first and last name, home | at least one ad request for 220 of these apps (also in Jan- |  |  |
| address, and online contact as defined in COPPA; and | uary 2014), for which we report results in this section. |  |  |
| (2) whether their content appears inappropriate to chil- | For the remaining 22 apps, either Brahmastra could not |  |  |
| dren and if so why. | navigate to the correct page, or the app did not serve any |  |  |
| Driving apps to display ads: | We use Brahmastra to au- | ad despite reaching the target page. |  |
| Lcom/google/ads/AdView;-><init> | out of the 220 apps (86%) pointed to at least one of these |  |  |
| Lcom/millennialmedia/android/MMAdView;-><init> | pages during the monitoring period. Note that WoT did |  |  |
| work traffic from executing test apps through a | Fiddler | 4 | Google Play store does not have a separate kids category. |
| 1030 | 23rd USENIX Security Symposium | USENIX Association |  |

---

## Page 12

| Info Type | Landing Pages | Apps | Content Type | Image Ads | Apps |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Home address | 47 | 58 | Child exploitation | 2 | 8 |  |  |  |
| First and last name | 231 | 174 | Gambling, contests, lotteries or | 3 | 2 |  |  |  |
| Online contact | 100 | 94 | sweepstakes |  |  |  |  |  |
| Phone number | 17 | 15 | Misleading | users | about | the | 7 | 16 |
| Total | 235 | 175 | product being advertised |  |  |  |  |  |

numbers represent a lower bound. We then used Amazon

Mechanical Turk to characterize all 566 ads, and 2,111

randomly selected landing pages out of the 3,633. For

ical Turk to check whether they collect personal infor-

mation (of each type) and whether they contain inappro-

priate content for children (see Appendix B for the task

details). We offered 7 cents (US) per each task (which

involves answering various questions for each website or

banner ad) and collected three responses per data point.

As discussed above, we only counted responses that were

consistent across at least two out of three respondents, to

filter out noise.

Table 2 summarizes the types of personal informa-

tion that landing pages ask users to provide as labeled

by Amazon Mechanical Turk. We find that at least 80%

of the apps in the dataset had displayed ads that point to

landing pages with forms to collect personal information.

On a manual examination of a subset of these pages, we

found no labeling errors. We also found that none of the

sites we manually checked attempt to acquire parental

consent when collecting personal information. See Ap-

pendix B for examples.

Table 3 breaks down child-inappropriate content of the

ads displayed in apps as labeled by Amazon Mechani-

cal Turk. Although COPPA does not regulate the con-

tent of online services, we still find it concerning that

36% (80 out of 220) of the apps display ads with con-

tent deemed inappropriate for children. In particular 26%

(58 apps) displayed ads that offer free prizes (e.g., Fig-

ure 13), which is considered a red flag of deceptive adver-

tising, especially in ads targeting children as discussed in

guidelines published by the Children’s Advertising Re-

view [10]. We also analysed the content displayed on

the landing pages, and found a similar number of content

violations as the ad images.

8 Analysis of Social Media Add-ons

Our second use case is to test apps against a recently

discovered vulnerability associated with the Facebook

| Violence, weapons or gore | 4 | 5 |
| --- | --- | --- |
| Profanity and vulgarity | 0 | 0 |
| Free prize | 39 | 58 |
| Sexual or sexually suggestive | 12 | 29 |

content

Total 62 80

8.1 Testing Goal

The Facebook access token vulnerability discussed

in [30] can be exploited by attackers to steal the vic-

tim’s sensitive information stored in vulnerable apps. For

instance, if a malicious-yet-seemingly benign news app

can trick the victim once to use the app to post a fa-

vorite news story on the victim’s Facebook wall (which

is a common feature found in many news apps), then the

malicious app can use the access token obtained from the

Facebook identity service to access sensitive information

stored by any vulnerable apps that the victim had inter-

acted with and have been associated with the victim’s

Facebook account. This attack can take place offline—

once the malicious app obtains an access token, then it

can send the token to a remote attacker who can imper-

sonate as the victim to vulnerable apps.

Figure 10 gives the steps that allow a malicious appli-

cation to steal Victim ’s information from VulApp s. The

fact that the online service ( VulApp s) is able to retrieve

the user’s information from Facebook only means that

the client ( MalApp c) possesses the privilege to the Face-

book service, but is not a proof of the client app’s iden-

tity ( MalApp c  = VulApp c). The shaded boxes in Figure 10

highlight the vulnerability. See [30] for more detail.

Wang et al. [30] manually tested 27 Windows 8 apps

and showed that 78% of them are vulnerable to the ac-

cess token attack. Our goal is to scale up the testing to a

large number of Android applications. Note that testing

for this vulnerability requires runtime analysis because

the security violation assumptions are based on the inter-

actions among the application, the application service,

and Facebook service.

8.2 Testing Procedure

| Table 2: Personal information collected by landing pages | Alcohol, tobacco or drugs | 3 | 3 |
| --- | --- | --- | --- |
| each ad and landing page, we asked Amazon Mechan- | Table 3: Breakdown of child-inappropriate content in ads |  |  |
| SDK [30]. | Our testing with Brahmastra shows that 13 | The testing has three steps. For a given app, we first need |  |
| out of 200 Android apps are vulnerable to the attack. | to drive apps to load a Facebook login screen. Second, |  |  |
| Fixing it requires app developers to update the authen- | we need to supply valid Facebook login credentials to ob- |  |  |
| tication logic in their servers as recommended by [30]. | serve interactions between the test application and Face- |  |  |
| USENIX Association | 23rd USENIX Security Symposium | 1031 |  |

---

## Page 13

| 1. Click | Login with Facebook | 1 | if | (oSession.url.Contains("m.facebook.com")) | { |
| --- | --- | --- | --- | --- | --- |
| 2. Initiate login with Facebook | 2 | var | toReplace | = | "access_token=CAAHOi..."; |

3. Prompt Facebook login screen 3

4

5. Return access_token 6

7

7. Get user info with access_token 9

10

8. Provide Victim ’s info

11

9. Authenticate this session as Victim

Figure 10: Facebook’s access token, intended for autho-

rizing access to Victim ’s info, is used by VulApp s to au-

thenticate the session as Victim . From step 9, MalApp c

Manipulating traffic with MITM proxy: As before,

we direct all network traffic through a Fiddler proxy.

Since Facebook sign-in traffic is encrypted over SSL, we

also install a Fiddler SSL certificate on the phone emu-

lator to decrypt all SSL traffic.

To manipulate the login, we record an access token

from a successful login session associated with another

application (and therefore simulating an attacker as illus-

trated in the steps 1-5 of Fig. 10) and use the script shown

in Fig. 11. It runs over HTTP responses, and overwrites

an incoming access token with a recorded one.

Dataset: We randomly draw 200 apps from the dataset

used in § 6 for this testing.

...

if (oSession.oResponse.headers.

{

oSession.oResponse.headers["Location"] =

replace(oRegEx, toReplace);

oSession["ui-customcolumn"] = "changed-header";

} }

We only show the first 6 bytes of the access token used

in the attack.

is sent only to Facebook servers.

To understand how widespread the vulnerability is, we

look at the statistics for the number of downloads on the

structions to fix. The privacy implications of the pos-

sessing the vulnerability are also serious. To look at what

user data can potentially be exfiltrated, we manually in-

vestigated the 13 vulnerable apps. Users of these apps

may share a friends list, pictures, and messages (three

dating apps); photos and videos (two apps); exercise logs

and stats (one app); homework info (one app) or favorite

news articles, books or music preferences (remaining six

apps). By exploiting the vulnerability, a malicious app

could exfiltrate this data.

9 Related Work

efforts proposed improvements over Android Monkey:

AndroidRipper [13] uses a technique known as GUI rip-

ping to create a GUI model of the application, and ex-

| 4. Provide | Victim | ’s Facebook credentials | 5 | ExistsAndContains("Location", | "access_token")) |  |
| --- | --- | --- | --- | --- | --- | --- |
| 6. Authenticate with | access_token | 8 | oSession.oResponse.headers["Location"]. |  |  |  |
| Victim | MalAppc | VulApps | Facebook ID service | Figure 11: A script used to manipulate | access token | : |
| can steal | Victim | ’s sensitive information in | VulApp | s. | work traffic at the login event, and observing that all of it |  |
| book ID service. Third, we need to determine whether | Google Play store. Each of the 13 vulnerable apps has |  |  |  |  |  |
| the test application misuses a Facebook access token for | been downloaded more than 10,000 times, the median |  |  |  |  |  |
| authenticating a client (steps 7-9) by monitoring network | number of app downloads is over 500,000, and the most |  |  |  |  |  |
| traffic and application behavior after providing a fraudu- | popular ones have been downloaded more than 10 mil- |  |  |  |  |  |
| lent access token. | lion times. | Further, these 13 apps have been built by |  |  |  |  |
| Driving apps to display Facebook login: | We use Brah- | 12 distinct publishers. | This shows that the problem is |  |  |  |
| mastra to automatically drive apps to invoke the Face- | not restricted to a few na¨ | ıve developers. We shared the |  |  |  |  |
| book SDK’s authentication methods shown in Figure 7. | list of vulnerable apps with a Facebook security team on |  |  |  |  |  |
| Once the authentication methods open the sign-in win- | 2/27/2014 and got a response immediately that night that |  |  |  |  |  |
| dow, we supply valid Facebook credentials. | they had contacted the affected developers with the in- |  |  |  |  |  |
| 8.3 | Experiments | Automated Android app testing: | A number of recent |  |  |  |
| Results: | We find that 18 out of 200 apps use a Face- | plores its state space. | To improve code coverage, An- |  |  |  |
| book access token for authentication, and among them 13 | droidRipper relies on human testers to type in user cre- |  |  |  |  |  |
| apps are vulnerable to a fraudulent access token (72%). 5 | dentials to get through blocking pages. | However, de- |  |  |  |  |
| apps appear not vulnerable, and show some sort of error | spite this manual effort, the tool shows less than 40% |  |  |  |  |  |
| message when given a fraudulent access token. The re- | code coverage after exploring an app for 4.5 hours. App- |  |  |  |  |  |
| maining 182 apps use the Facebook SDK merely to post | sPlayground [26] employs a number of heuristics—by |  |  |  |  |  |
| content to the user’s wall, and not as an authentication | guessing the right forms of input (e.g., email address, zip |  |  |  |  |  |
| mechanism. We determined this by looking at the net- | code) and by tracking widgets and windows in order to |  |  |  |  |  |
| 1032 | 23rd USENIX Security Symposium | USENIX Association |  |  |  |  |

---

## Page 14

reduce duplicate exploration. It shows that these heuris- 10 Discussion

tics are helpful although the coverage is still around 33%.

Security analysis of in-app ads: Probably because only

recently COPPA [6] had been updated to include mo-

tifiers and the collection of private user information [28].

Worse, through a longitudinal study, Book et al. show

Analyzing logic flaws in web services and SDKs: The

authentication vulnerability discussed in § 8 falls into the

category of logic flaws in web programming. Recent pa-

pers have proposed several technologies for testing var-

ious types of logic flaws [16, 17, 21]. However, these

techniques mainly target logic flaws in two-party web

programs , i.e., programs consisting of a client and a

server. Logic flaws become more complicated and in-

triguing in multi-party web programs, in which a client

mine dependent activities to find activities to jump-start

to without affecting the program behavior.

11 Conclusion

can use to test third-party components at runtime as they

are used by real applications. To overcome the known

shortcomings of GUI exploration techniques, we analyze

application structure to discover desired execution paths.

Then we re-write test apps to follow a short path that in-

vokes the target third-party component. We find that we

can more than double the test hit rate while speeding up

testing by a factor of seven compared to a state-of-the-art

Monkey tool.

consent. Among the apps that use Facebook Login, we

| SmartDroid [31] uses a combination of static and dy- | Limitations: | Although Brahmastra improves test hit |  |  |
| --- | --- | --- | --- | --- |
| namic analysis to find the UI elements linked to sensitive | rates over Monkey-like tools, we discover several id- |  |  |  |
| APIs. However, unlike Brahmastra, SmartDroid explores | iosyncratic behaviors of mobile apps that challenge run- |  |  |  |
| every UI element at runtime to find the right view to | time testing. | Some apps check servers upon launching |  |  |
| click. A3E [14] also uses static analysis to find an activ- | and force upgrading if newer versions exist. Some apps |  |  |  |
| ity transition graph and uses the graph to efficiently ex- | constantly load content from remote servers, showing |  |  |  |
| plore apps. We leveraged the proposed technique when | transient behaviors (e.g., extremely slow at times). We |  |  |  |
| building an execution path. | However, similarly to the | also have yet to implement adding callbacks related to |  |  |
| tools listed above, A3E again uses runtime GUI explo- | sensor inputs. Another challenge is to isolate dependent |  |  |  |
| ration to navigate through activities. In contrast to these | components in the code. We assume that each activity is |  |  |  |
| works, Brahmastra determines an execution path using | more or less independent (except that they pass parame- |  |  |  |
| static analysis and rewrites an app to trigger a planned | ters along with intent) and use our jump start technique |  |  |  |
| navigation, bypassing known difficulties related to GUI | to bypass blocking pages and to speed up testing. How- |  |  |  |
| exploration. | ever, we leave as future work a task to statically deter- |  |  |  |
| bile apps | 5 | , we are not aware of any prior work looking | Other runtime security testing of mobile apps: | As |
| into the issues around COPPA compliance of advertise- | mobile apps are highly driven by user interaction with |  |  |  |
| ments (and the corresponding landing pages) displayed | visual components in the program, it is important to an- |  |  |  |
| within apps directed at children. However, several past | alyze the code behavior in conjunction with runtime UI |  |  |  |
| works investigated security and privacy issues with re- | states. | For instance, malicious third-party components |  |  |
| spect to Android advertising libraries. AdRisk [22] is a | can trick users into authorizing the components to access |  |  |  |
| static analysis tool to examine advertising libraries inte- | content (e.g., photos) that the users intended to share with |  |  |  |
| grated with Android apps. They report that many ad li- | the application. Brahmastra can be used to capture visual |  |  |  |
| braries excessively collect privacy-sensitive information | elements when certain APIs are invoked to check against |  |  |  |
| and expose some of the collected information to adver- | such click jacking attempts. Brahmastra can also auto- |  |  |  |
| tisers. Stevens et al. examine thirteen popular Android | mate the testing to check whether privacy-sensitive APIs |  |  |  |
| ad libraries and show the prevalent use of tracking iden- | are only invoked with explicit user interactions. |  |  |  |
| that the use of permissions by Android ad libraries has | We have presented a mobile app automation tool, Brah- |  |  |  |
| increased over the past years [18]. | mastra, that app store operators and security researchers |  |  |  |
| communicating with multiple servers to accomplish a | We use Brahmastra for two case studies, each of which |  |  |  |
| task, such as the Facebook-based authentication that we | contributes new results: checking if third-party ad com- |  |  |  |
| focus in this paper. | AuthScan is a recently developed | ponents in kids apps are compliant with child-safety reg- |  |  |
| technique to automatically extract protocol specifications | ulations; and checking whether apps that use Facebook |  |  |  |
| from concrete website implementations, and thus dis- | Login are vulnerable to a known security flaw. Among |  |  |  |
| cover new vulnerabilities in the websites [15]. | In con- | the kids apps, we discover 36% of 220 kids apps dis- |  |  |
| trast, our goal is not to discover any new vulnerability on | play ads deemed inappropriate for children, and 80% of |  |  |  |
| a website, but to scale up the testing of a known vulnera- | the apps display ads that point to landing pages which |  |  |  |
| bility to a large number of apps. | attempt to collect personal information without parental |  |  |  |
| 5 | The revision was published on July 2013. | find that 13 applications are still vulnerable to the Face- |  |  |
| USENIX Association | 23rd USENIX Security Symposium | 1033 |  |  |

---

## Page 15

| book access token attack even though the attack has been | [12] A. V. Aho, R. Sethi, and J. D. Ullman. | Compilers: |
| --- | --- | --- |
| known for almost a year. Brahmastra let us quickly check | Principles, Techniques and Tools | . Addison-Wesley, |
| the behavior of hundreds of apps for these studies, and | 1986. |  |

it can easily be used for other studies in the future—

This material is based on research sponsored in part by

nership with the Laboratory of Telecommunications Sci-

ences, Contract Number H9823013D00560002. The

U.S. Government is authorized to reproduce and dis-

tribute reprints for Governmental purposes notwithstand-

ing any copyright notation thereon.

References

[1] A tool for reverse engineering Android apk files.

http://code.google.com/p/android-

apktool/ .

[2] Activity — Android Developers. http:

//developer.android.com/reference/

android/app/Activity.html .

mturk.com .

[6] Complying with COPPA: Frequently Asked

[8] Fiddler. http://www.telerik.com/

fiddler .

[9] Web of Trust. https://www.mywot.com/ .

vertising, 2009. http://www.caru.org/

Proceedings of the IEEE Conference on Automated

In OOPSLA , 2013.

[15] G. Bai, J. Lei, G. Meng, S. S. V. P. Saxena, J. Sun,

Y. Liu, and J. S. Dong. Authscan: Automatic ex-

traction of web authentication protocols from im-

plementations. In NDSS , 2013.

[16] P. Bisht, T. Hinrichs, N. Skrupsky, R. Bobrowicz,

and V. N. Venkatakrishnan. Notamper: Automati-

cally detecting parameter tampering vulnerabilities

in web applications. In CCS , 2010.

[17] P. Bisht, T. Hinrichs, N. Skrupsky, and V. N.

Venkatakrishnan. Waptec: Whitebox analysis of

web applications for parameter tampering exploit

[18] T. Book, A. Pridgen, and D. S. Wallach. Longitu-

ming , pages 77–101, 1995.

abilities in web applications. In USENIX Security ,

2010.

[22] M. Grace, W. Zhou, X. Jiang, and A.-R. Sadeghi.

Unsafe Exposure Analysis of Mobile In-App Ad-

and R. Govindan. PUMA: Programmable UI-

| checking whether privacy-sensitive APIs can be invoked | [13] D. Amalfitano, A. R. Fasolino, S. D. Carmine, |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| without explicit user interaction, discovering visible UI | A. Memon, and P. Tramontana. Using GUI Ripping |  |  |  |  |  |  |  |  |  |
| elements implicated in click jacking attempts, and more. | for Automated Testing of Android Applications. In |  |  |  |  |  |  |  |  |  |
| Acknowledgments | Software Engineering (ASE) | , 2012. |  |  |  |  |  |  |  |  |
| DARPA under agreement number FA8750-12-2-0107, | [14] T. Azim and I. Neamtiu. | Targeted and depth-first |  |  |  |  |  |  |  |  |
| NSF CCF-1139021, and University of Maryland Part- | exploration for systematic testing of android apps. |  |  |  |  |  |  |  |  |  |
| [3] Amazon | Mechanical | Turk. | https://www. | construction. In | CCS | , 2011. |  |  |  |  |
| [4] Android Debug Bridge. | http://developer. | dinal analysis of android ad library permissions. In |  |  |  |  |  |  |  |  |
| android.com/tools/help/adb.html | . | IEEE Mobile Security Technologies (MoST) | , 2013. |  |  |  |  |  |  |  |
| [5] Android | Developers, | The | Developer’s | [19] J. Dean, D. Grove, and C. Chambers. Optimization |  |  |  |  |  |  |
| Guide. | UI/Application | Exerciser | Monkey. | of Object-Oriented Programs Using Static Class |  |  |  |  |  |  |
| http://developer.android.com/ | Hierarchy Analysis. In | Proceedings of the 9th Eu- |  |  |  |  |  |  |  |  |
| tools/help/monkey.html | . | ropean Conference on Object-Oriented Program- |  |  |  |  |  |  |  |  |
| Questions. | http://business.ftc.gov/ | [20] M. | Egele, | D. | Brumley, | Y. | Fratantonio, | and |  |  |
| documents/Complying-with-COPPA- | C. Kruegel. An Empirical Study of Cryptographic |  |  |  |  |  |  |  |  |  |
| Frequently-Asked-Questions | . | Misuse in Android Applications. In | CCS | , 2013. |  |  |  |  |  |  |
| [7] Dexpler: | A Dalvik to Soot Jimple Translator. | [21] V. Felmetsger, L. Cavedon, C. Kruegel, and G. Vi- |  |  |  |  |  |  |  |  |
| http://www.abartel.net/dexpler/ | . | gna. Toward automated detection of logic vulner- |  |  |  |  |  |  |  |  |
| [10] Self-Regulatory | Program | for | Childrens | Ad- | vertisements. In | WiSec | , 2012. |  |  |  |
| guidelines/guidelines.pdf | . | [23] S. | Hao, | B. | Liu, | S. | Nath, | W. | G. | Halfond, |
| [11] AppBrain, | Feb. | 2014. | http://www. | Automation for Large Scale Dynamic Analysis of |  |  |  |  |  |  |
| appbrain.com/stats/libraries/ad | . | Mobile Apps. In | Mobisys | , 2014. |  |  |  |  |  |  |
| 1034 | 23rd USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |  |

---

## Page 16

[24] J. Jeon, K. K. Micinski, J. A. Vaughan, A. Fogel, A Constant Propagation Analysis

N. Reddy, J. S. Foster, and T. Millstein. Dr. Android

and Mr. Hide: Fine-grained Permissions in Android

Applications. In ACM CCS Workshop on Security

and Privacy in Smartphones and Mobile Devices ,

2012.

[26] V. Rastogi, Y. Chen, and W. Enck. Appsplay-

ground: Automatic security analysis of smartphone

applications. In Proceedings of the ACM Confer-

[27] L. Ravindranath, S. Nath, J. Padhye, and H. Balakr-

ishnan. Automatic and Scalable Fault Detection for

Mobile Applications. In Mobisys , 2014.

H. Chen. Investigating user privacy in android ad

(MoST) , 2012.

[29] R. Valle-Rai, P. Co, E. Gagnon, L. J. Hendren,

P. Lam, and V. Sundaresan. Soot - a Java byte-

code optimization framework. In IBM Centre for

Advanced Studies Conference , 1999.

[30] R. Wang, Y. Zhou, S. Chen, S. Qadeer, D. Evans,

and Y. Gurevich. Explicating SDKs: Uncover-

[31] C. Zheng, S. Zhu, S. Dai, G. Gu, X. Gong, X. Han,

and W. Zou. Smartdroid: an automatic system for

revealing ui-based trigger conditions in android ap-

plications. In ACM CCS Workshop on Security and

Privacy in Smartphones and Mobile Devices , 2012.

We extend the existing constant propagation analysis so

as to trace intent s, UI elements, and listeners. In ad-

dition to traditional value types, such as numerical or

objects; load class ids; or invoke special APIs such as

Intent . setClass () , we add their semantics into the data-

flow transfer function.

define semantics of relevant instructions.

1 type lattice = ...

3 | Object of string ( ∗ instance ∗ )

5 | ...

6 let meet l1 l2 = match l1 , l2 with ...

7 | Clazz c1, Clazz c2 when 0 = compare c1 c2 → l1

8 | Object o1, Object o2 when 0 = compare o1 o2 → l1

9 | Intent i1 , Intent i2 when 0 = compare i1 i2 → l1

10 | ...

11 let transfer (inn : lattice Map.t) ( op , opr) = ...

12 else if OP NEW = op then ( ∗ NEW ∗ )

13 (

| 14 | let | dst :: id ::[] | = opr | in |
| --- | --- | --- | --- | --- |
| 15 | let | cname = Dex.get ty name id | in |  |
| 16 | if | 0 = compare cname ‘‘ Intent ’’ |  |  |
| 17 | then | Map.add dst ( Intent | ‘‘’’) | inn |
| 18 | else | Map.add dst (Object cname) inn |  |  |

19 ) ...

maintain information as string, and they can be merged

only if internal values are identical, hence must -analysis.

As an example, this shows how to handle opcode NEW .

| [25] B. Liu, S. Nath, R. Govindan, and J. Liu. DECAF: | string constant, we add meta-class, object, and intent |  |  |  |
| --- | --- | --- | --- | --- |
| Detecting and Characterizing Ad Fraud in Mobile | sorts, which track class ids, object references, and in- |  |  |  |
| Apps. In | USENIX NSDI | , 2014. | tent instances, respectively. For instructions that create |  |
| ence on Data and Application Security and Pri- | Figure 12 illustrates how we extend data-flow lattice; |  |  |  |
| vacy | , 2013. | how we conform to | meet | operation property; and how we |

[28] R. Stevens, C. Gibler, J. Crussell, J. Erickson, and 2 | Clazz of string ( ∗ const − class ∗ )

libraries. In IEEE Mobile Security Technologies 4 | Intent of string ( ∗ Intent for a specific component ∗ )

| ing Assumptions Underlying Secure Authentica- | Figure 12: Abbreviated source code of extended constant |  |  |
| --- | --- | --- | --- |
| tion and Authorization. In | USENIX Security | , 2013. | propagation analysis. Meta-class, object, and intent sorts |
| USENIX Association | 23rd USENIX Security Symposium | 1035 |  |

---

## Page 17

B Examples of Ads in Kids Apps

(b) (e) clicking

the banner ad

(c)

(a) (d) A1

Figure 13: a) and (b) offer a free prize and (c) and (d) are sexually suggestive. (e) shows an example where clicking a

banner ad displayed in a kids app opens up a landing page that presents forms to collect personal information.

Figure 14: A screenshot of the Amazon Mechanical Turk task that we created to characterize landing pages pointed

by ads displayed in kids apps

1036 23rd USENIX Security Symposium USENIX Association

*[Image: Page 17 Image]*

*[Image: Page 17 Image]*

*[Image: Page 17 Image]*
