---
title: "25_Romdhana_et_al.,_Assessing_Inter-App_Communications"
creator: "pdftk-java 3.2.2"
pages: 12
---

# 25_Romdhana_et_al.,_Assessing_Inter-App_Communications

> **總頁數**：12 頁

---

## Page 1

Assessing the Security of Inter-App Communications in Android Assessing the Security of Inter-App Communications in Android

through Reinforcement Learning through Reinforcement Learning

This paper was downloaded from TechRxiv (https://www.techrxiv.org).

LICENSE

CC BY 4.0

SUBMISSION DATE / POSTED DATE

11-10-2022 / 14-10-2022

CITATION

Romdhana, Andrea; Merlo, Alessio; Ceccato, Mariano; Tonella, Paolo (2022): Assessing the Security of Inter-

App Communications in Android through Reinforcement Learning. TechRxiv. Preprint.

https://doi.org/10.36227/techrxiv.21310770.v1

DOI

10.36227/techrxiv.21310770.v1

---

## Page 2

Assessing the Security of Inter-App Communications in Android through Reinforcement

Learning

Andrea Romdhana a,b , Alessio Merlo a , Mariano Ceccato c , Paolo Tonella d

a DIBRIS - Universit` a degli Studi di Genova

b FBK-ICT, Security & Trust Unit

c Universit` a di Verona

d Universit` a della Svizzera italiana

Abstract

A central aspect of the Android platform is Inter-Component Communication (ICC), which enables the reuse of functionality

across apps and components via message passing. While a powerful feature, ICC still constitutes a serious attack surface. This

paper addresses the issue of generating exploits for a subset of Android ICC vulnerabilities (i.e., IDOS, XAS, and FI) through

static analysis, Deep Reinforcement Learning-based dynamic analysis and software instrumentation. Our approach, called RONIN,

achieves better results than state-of-the-art and baseline tools, in the number of exploited vulnerabilities.

Keywords: reinforcement learning, security testing, Software security engineering

1. Introduction to automatically find vulnerabilities in Android apps and de-

termine whether such vulnerabilities are exploitable. Discov-

| Nowadays, mobile phones are the most pervasive electronic | ering automatically exploitable security flaws would help soft- |  |  |
| --- | --- | --- | --- |
| devices worldwide [1]. Among the available mobile operating | ware engineers choose which issues to address first. It would |  |  |
| systems, Android rose as the most used platform [2]. The rea- | also give them information useful to fix the security bugs and |  |  |
| son for this success lies in the high number of available apps, | to evaluate the | vulnerability risk | , i.e., likelihood and impact of |
| whose number currently exceeds 3 billion at the time of writ- | the vulnerability. |  |  |
| ing [3]. The presence of app construction frameworks and rich | One challenge to address to enable | automatic exploit gen- |  |
| libraries, as well as easy distribution via online app stores such | eration for Android apps | is how to penetrate Android’s spe- |  |
| as Google Play, have significantly lowered the barrier to entry | cific attack surface, including its distributed event-based and |  |  |
| in app development and deployment [4]. Bhattacharya et al. [5] | message-based frameworks. In particular, asynchronous mes- |  |  |
| claim that the low barrier to enter the market means apps (or | sages, or what Android refers to as Intents, are largely used |  |  |
| app updates) are subject to limited scrutiny before dissemina- | for inter-component communication (ICC) within and between |  |  |
| tion, allowing error-prone apps through and therefore a | ff | ecting | Android apps. Thus, it is essential to model the Android frame- |
| also their security. Therefore, developers and designers of such | work, especially the ICC interface. | When generated, Intents |  |
| apps need to utilize proper approaches, tools, and frameworks | accept parameters that specify which action the app should per- |  |  |
| that assist them in creating secure apps. | form. Additionally, the Android framework o | ff | ers several pre- |
| Numerous methodologies have been developed to find se- | defined components that respond to Intents in various ways. For |  |  |
| curity flaws in Android apps [6]. Most of these methods rely on | example, to show the user a location on a map, a developer can |  |  |
| static analysis of Android apps to find such vulnerabilities [6] | use an Intent to request that another capable app show a spec- |  |  |
| [7] [8] [9], but there are also strategies that make use of dynamic | ified location on a map; or can use Intents to start a service to |  |  |
| analysis [10] [11]. | A few methods detect vulnerabilities by | download a file in the background. |  |
| combining static and dynamic analysis [12] [13] [14]. Although | Defining a method for automatically determining whether |  |  |
| these methods and procedures have made it possible to detect | a vulnerability has been exploited is another challenge when |  |  |
| vulnerabilities, it is frequently necessary for security analysts to | generating automatic exploits for Android. Garcia et al. [18] |  |  |
| decide manually whether those flaws are actually exploitable, | proposed an approach called Letterbomb for automatically gen- |  |  |
| possibly with the aid of dynamics tools such as Drozer [15], | erating exploits for Android apps. | Letterbomb relies on two |  |
| Inspeckage [16], and Objection [17]. However, such a manual | phases. The first phase leverages combined path-sensitive sym- |  |  |
| task is laborious and slow. | A method should ideally be able | bolic execution-based static analysis. During the second phase, |  |

the tool tries to exploit the statically discovered vulnerabilities

| Email addresses: | andrea.romdhana@dibris.unige.it | (Andrea | by generating an Intent and sending it to the analyzed app. The |
| --- | --- | --- | --- |
| Romdhana), | alessio.merlo@unige.it | (Alessio Merlo), | focus of Letterbomb is ICC vulnerabilities. Specifically, it fo- |
| mariano.ceccato@univr.it | (Mariano Ceccato), | cuses on three types: 1) inter-process denial of service, 2) cross- |  |

paolo.tonella@usi.ch (Paolo Tonella)

Preprint submitted to Elsevier May 2022

---

## Page 3

application scripting, 3) and Fragment injection. However, Let- compared with existing and baseline techniques.

terbomb stimulates an app only by directly triggering Intents,

ignoring the possible internal usage of Intents triggered by GUI

2. Background

events [19]. Due to this, Letterbomb misses specific possible

true positives, which can only be exposed by a proper sequence This section introduces the basics of RL as well as the tar-

of GUI events. Moreover, the exploitability of a vulnerabil- geted ICC vulnerabilities in detail.

ity at a particular statement depends on the di ff erent program

| paths that may lead to reaching that statement. A specific path | 2.1. Reinforcement Learning |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| may reach a statement without exploiting the vulnerability, but | Reinforcement learning’s [20] objective is to teach an agent |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| there may be more paths that reach the same statement in the | how to interact with a specific environment to achieve a particu- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| program, and only some of them may exploit the vulnerable | lar goal. The agent determines the environment’s present state, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| statement. Hence, when we modify the payload of an Intent to | takes actions that possibly a | ff | ect the environment, and receives |  |  |  |  |  |  |  |  |  |  |  |  |
| exploit a vulnerability, its execution along a specific path may | a positive, neutral or negative reward. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| or may not trigger the vulnerability, depending on the chosen | At each time step | t | , the agent takes an action | a | t | , according to |  |  |  |  |  |  |  |  |  |
| path. Letterbomb includes path-sensitive analyses for path se- | an observation | x | t | , which may be a partial or full representation |  |  |  |  |  |  |  |  |  |  |  |
| lection but faces path explosion problem as the program grows | of the environment state | s | t | . The action | a | t | causes the transition |  |  |  |  |  |  |  |  |
| due to the potentially exponential number of program paths to | of the environment from state | s | t | to state | s | t | + | 1 | , and its quality is |  |  |  |  |  |  |
| be analyzed. Another related challenge is the generation of the | measured by the reward function | R | ( | x | t | , | a | t | , | x | t | + | 1 | ). A | Markov Deci- |
| parameter values for the Intent. Letterbomb uses a Satisfiabil- | sion Process (MDP) | formally describes the agent environment. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ity Modulo Theory (SMT) solver to generate parameters for the | An MDP is 5-tuple, | ⟨ | S | , | A | , | R | , | P | , ρ | 0 | ⟩ | , where: | S | is the set of states, |
| Intent. The drawback of such an approach is that it loses e | ffi | - | A | is the set of actions, | R | the reward function, | P | the transition |  |  |  |  |  |  |  |
| ciency when dealing with an increasing number of parameters. | probability function, and | ρ | 0 | ⊆ | S | is the set of initial states. The |  |  |  |  |  |  |  |  |  |
| At last, it becomes inapplicable when the constraints to reach | goal in RL is to learn a policy | π | , i.e., a rule for deciding which |  |  |  |  |  |  |  |  |  |  |  |  |
| a certain path within the app are too di | ffi | cult to handle for an | action to take, based on the perceived state | s | t | . The learned pol- |  |  |  |  |  |  |  |  |  |
| SMT solver. | icy must maximize the so-called | expected return | . Earlier RL al- |  |  |  |  |  |  |  |  |  |  |  |  |
| We propose a di | ff | erent approach to exploit generation, which | gorithms approximate states and actions using tables that store |  |  |  |  |  |  |  |  |  |  |  |  |
| we call RONIN, based on Deep Reinforcement Learning. Deep | discrete values. As it may be impractical to describe all possi- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Reinforcement Learning (Deep RL) is a machine learning tech- | ble states and actions in a table, these tabular techniques cannot |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| nique that does not require a labeled training set as input since | learn appropriate policies in vast or unbounded discrete spaces |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the learning process is guided by the positive or negative reward | (e.g., programs with numerous inputs, constraints, and states |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| experienced during the tentative execution of a task. Hence, it | to be modeled)[21]. Deep Reinforcement Learning is a novel |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| can be used to dynamically learn how to build an Intent that | technique that has emerged due to the advent of Deep Learn- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| exposes a specific vulnerability based on the feedback obtained | ing, which relies on the sophisticated function approximation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| during past successful or unsuccessful attempts. More specifi- | capabilities of Deep Neural Networks [21] to learn an optimal |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cally, RONIN manipulates the parameters of the Intents by ap- | policy even in the presence of large state and action spaces. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

plying a sequence of actions to them. Each action receives pos-

| itive feedback if we move closer to the target statement (i.e., | 2.2. Android Background |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| the vulnerable statement) upon execution of the Intent; neu- | The Android Software Development Kit (SDK) o | ff | ers pro- |  |  |  |
| tral (zero) feedback if the minimum distance between the state- | grammers a collection of communication components for build- |  |  |  |  |  |
| ments that we reached and the target statement does not change; | ing mobile applications. | Activities | , | Services | , | Broad- |
| negative feedback if we increase the distance from the target | cast Receivers | , and | Content Providers | are the four |  |  |
| concerning the last Intent execution. RONIN uses a Deep Neu- | Android’s pre-defined components. All such components (ex- |  |  |  |  |  |
| ral Network (DNN) to generate (initially random) actions dur- | cept dynamically registered Broadcast Receivers) are declared |  |  |  |  |  |
| ing the training phase and observes their outcome (i.e., states | in the app’s manifest file ( | AndroidManifest.xml | ). |  |  |  |
| and rewards). Then, RONIN leverages the collected informa- | An | Activity | is a GUI that an app displays to a user and |  |  |  |
| tion and iteratively trains the DNN to take a given action when | that the user can interact with. | A | Service | manages back- |  |  |
| in a given state. Our paper gives the following major contribu- | ground tasks for an app. | A | Content Provider | manages |  |  |
| tions to the state of the art: | access to a central repository of data primarily intended to be |  |  |  |  |  |

used by other applications, allowing secure access. A Broad-

| • | The first Deep RL approach to Android security testing | cast Receiver | receives Intents that are broadcast by other |  |  |
| --- | --- | --- | --- | --- | --- |
| focused on ICC vulnerabilities. | This approach applies | apps or the Android framework (for example, informing the |  |  |  |
| to a wide range of Android apps by relying on feedback | user that the battery is low). | Intents can be exchanged be- |  |  |  |
| provided through dedicated instrumentation. | tween Activities, Services, and Broadcast Receivers. Activities |  |  |  |  |
| • | RONIN, an open source tool, whose code is available at | might be made up of Fragments, each of which could be a user- |  |  |  |
| the url: | https://github.com/H2SO4T/RONIN | . | viewable portion or a full screen. | Fragments | introduce mod- |

ularity and reusability into the activity’s UI by allowing devel-

• An empirical study shows our approach’s e ff ectiveness opers to divide the UI into smaller, more manageable discrete

2

---

## Page 4

| pieces. Moreover, fragments support the dynamic composition | and wrap them into a single native app that can render HTM- |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| of a GUI, allowing developers to add and remove fragments | L | / | CSS content and execute JavaScript. This enables di | ff | erent |  |  |
| (and the layouts therein) dynamically and programmatically. | forms of attack, including: | 1) UI defacing | / | rewriting to trig- |  |  |  |
| Android apps execute in a sandboxed environment to pre- | ger phishing attacks, 2) access to sensitive information, and |  |  |  |  |  |  |
| vent malware from infecting the system, and the hosted appli- | 3) run native code via JavaScript. | A concrete entry point for |  |  |  |  |  |
| cations [22]. The Android sandbox utilizes the isolation capa- | XAS attacks is the WebView class, which renders HTML con- |  |  |  |  |  |  |
| bilities of the Linux kernel. Although sandboxing is an essen- | tent within a mobile app. | The main method of WebView is |  |  |  |  |  |
| tial security feature, interoperability is negatively a | ff | ected as a | loadUrl | . If a malicious app can control the current URL, all |  |  |  |
| result. | Apps need to be able to interact in a variety of ways. | the attacks above become potential threats. To exploit an XAS |  |  |  |  |  |
| For instance, if the user points to the Google Play website, the | vulnerability, an attacker can inject JavaScript code using ei- |  |  |  |  |  |  |
| browser app should be able to launch the Google Play app. | ther the JavaScript URI scheme or the file scheme. The attacker |  |  |  |  |  |  |
| To support interoperability, Android supplies high-level ICC | creates a malicious HTML file and directs the target WebView |  |  |  |  |  |  |
| mechanisms via the | Binder | class, implemented as a driver in | object to load that file via an Intent. |  |  |  |  |
| the Linux kernel. ICC is achieved via | Messages | and | Intents | . | Fragment injection | . The static | instantiate(Context |
| Intents | are messaging objects that contain both the payload | ctx, String fname, Bundle args) | method of class |  |  |  |  |
| and the target application component. Intents can either be im- | Fragment accepts as | fname | the name of the Fragment sub- |  |  |  |  |
| plicit, which means that the target is not specified, or explicit, | class to load reflectively. An attacker can leverage this to ar- |  |  |  |  |  |  |
| which means that a specific target is provided. Intents can be | bitrary load code obtainable through the class loader of | ctx | . |  |  |  |  |
| broadcast to Broadcast Receivers, invoke activities, or launch a | A successful Fragment injection attack can result in loading an |  |  |  |  |  |  |
| Service. External parties can invoke an application component | attacker-selected class into the context of the vulnerable app, |  |  |  |  |  |  |
| via an Intent if the manifest file allows that. The manifest also | which grants that class the same privileges and access rights as |  |  |  |  |  |  |
| defines the permissions that the external party must possess. | its host app. Otherwise, an exception is thrown, but before that, |  |  |  |  |  |  |
| According to the Android documentation [23], Intents con- | the class’ static initializer and default constructor are executed, |  |  |  |  |  |  |
| tain actions, categories, and supplementary data that an app | creating another attack vector. | Another alternative is to load |  |  |  |  |  |
| utilizes to decide how to carry out activities based on it. The | a Fragment already defined by the application or Android | / | Java |  |  |  |  |
| attribute known as an Intent’s action denotes the general ac- | framework but inject malicious initialization data into the Frag- |  |  |  |  |  |  |
| tion to be taken in response to an Intent (e.g., deliver data to | ment. Fragments that are normally loaded by private Activities |  |  |  |  |  |  |
| some agent). The categories of Intent o | ff | er more details about | are more likely to trust rather than validate their initialization |  |  |  |  |
| how the Intent’s action should be carried out by the app. | A | arguments, which renders them more exploitable to Fragment |  |  |  |  |  |
| developer can declare categories in the application manifest, | manipulation attacks. |  |  |  |  |  |  |
| allowing the system to know if the application can handle a | Unhandled Exceptions (Denial of Service) | . | Programming |  |  |  |  |
| specific Intent category. | For example, by putting the CATE- | errors that trigger unchecked exceptions (like null dereference) |  |  |  |  |  |
| GORY BROWSABLE category, an app specifies that a specific | will usually cause the target app to crash if the exception is |  |  |  |  |  |  |
| activity can be invoked through intent by a browser. | missed. This presents an opportunity for Denial-of-Service (DoS) |  |  |  |  |  |  |

attacks and can generally drive the application into an unex-

| 2.3. Vulnerabilities related to ICC Channels | pected state. |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| We can refer to an Android component as | public | if 1) it is | Running Example | . The code in Listing 1 illustrates the dif- |  |  |
| exported via Intent filters, either explicitly or implicitly; 2) it | ferent ways incoming ICC messages are processed. An attacker |  |  |  |  |  |
| requires neither signed nor system permissions; or 3) unsani- | can take advantage of an ICC-based vulnerability in an Android |  |  |  |  |  |
| tized data originating from a public component flows into it. | app by including actions, categories, or additional data with ma- |  |  |  |  |  |
| The presence of public components leaves a hole in the An- | licious payloads or by deleting these parameters. | getExtra- |  |  |  |  |
| droid sandbox. They expose themselves to incoming data from | String | retrieves the value of the custom string field of an |  |  |  |  |
| malicious parties, which might lead to vulnerabilities if the data | Intent. | The Activity contains two exploitable vulnerabilities |  |  |  |  |
| is not sanitized or validated. Fragments are also potentially vul- | that are reachable from the app’s ICC interface. If the Activ- |  |  |  |  |  |
| nerable, as they can access incoming ICC data via their enclos- | ity receives an Intent whose | ExtraString s1 | contains the |  |  |  |
| ing Activity and its initiating Intent. Malicious parties can be | string | URL | (line 20) the | WebView | of the Activity will load |  |
| both local and remote. Malware is highly prevalent in Android | the string associated to | ExtraString s2 | (line 22). | This |  |  |
| and can interact directly with the public ICC interfaces through | leads to a first XAS vulnerability. When | ExtraString | s1 |  |  |  |
| explicit Intents without special permissions [24]. Unsafe han- | does not contain | URL | , the app performs a string comparison |  |  |  |
| dling of incoming ICC data can result in di | ff | erent forms of at- | between | ExtraString s2 | and a hardcoded string (line 27). |  |
| tack. | Below we list three of the main threats that we aim to | If | ExtraString s2 | is a null object, a | Null | Pointer |
| discover. | Exception | will be thrown, which results in the app crash- |  |  |  |  |
| Cross-Application Scripting (XAS) | . Similarly to Cross-Site | ing as the thrown exception is not caught. A malicious app can |  |  |  |  |
| Scripting (XSS) in the Web landscape, XAS [24] arises when | leverage this vulnerability to perform an | inter-process denial- |  |  |  |  |
| script content (mostly JavaScript code) is injected into the HTML | of-service (IDOS) | attack on the MainActivity by periodically |  |  |  |  |
| UI of a hybrid mobile application. Hybrid apps allow develop- | sending an Intent with no | ExtraString s2 | . The function |  |  |  |
| ers to write code based on platform-neutral web technologies | getFragmentInstance | contains a Fragment injection (FI) |  |  |  |  |

3

---

## Page 5

vulnerability [24], which occurs because within getFragmentInstance

an incoming Intent with a string of extra data containing the key

fname can be exploited by supplying as its value the name of a

Fragment that resides in the corresponding app. This Fragment

is then instantiated and loaded into the app (line 39).

1 public class MainActivity extends AppCompatActivity {

| 2 | @Override |  |  |  |
| --- | --- | --- | --- | --- |
| 3 | protected | void | onCreate | (Bundle savedInstanceState) { |
| 4 | // | ... |  |  |
| 5 | } |  |  |  |

6

| 7 | @Override |  |  |  |
| --- | --- | --- | --- | --- |
| 8 | protected | void | onResume(){ |  |
| 9 | super.onResume(); |  |  |  |
| 10 | Button | button | = | (Button) findViewById(R.id.get): |
| 11 | WebView | webView | = | (WebView) findViewById(R.id.webView1) : |
| 12 | button.setonClickListener(new View.OnClickListener() { |  |  |  |

13

| 14 | @override |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 15 | public | void | onclick(View v) { |  |  |
| 16 | TextView | textView | = (TextView) findViewById(R.id.concat); |  |  |
| 17 | Intent | intent | = | getIntent(): |  |
| 18 | String | a | = | intent.getStringExtra("s1"); |  |
| 19 | if | ("URL".equals(a)) { |  |  |  |
| 20 | /* | If | s2 | contains a malicious site it will be loaded by the | WebView |

*/

| 21 | webView.LoadUrl(intent.getstringExtra("s2")); |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 22 | } | else | { |  |  |
| 23 | String | b | = | intent.getStringExtra("s2"); |  |
| 24 | /* | If | String | b is null the app will crash | */ |
| 25 | if | (b.equals | ("www.test.com")) |  |  |
| 26 | webView.LoadUrl(intent.getStringExtra("s2")); |  |  |  |  |
| 27 | } |  |  |  |  |
| 28 | } |  |  |  |  |
| 29 | }); |  |  |  |  |

30 }

31

32 // ...

33

34 public static void getFragmentInstance(Intent my_intent){

| 35 | /* | If | fame | is | not | checked | we can have a Fragment Injection | */ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 36 | String | fname | = | my_intent.getStringExtra("fname"); |  |  |  |  |
| 37 | return | Fragment.instantiate(this, fname) ; |  |  |  |  |  |  |
| 38 | } |  |  |  |  |  |  |  |

39 }

Listing 1: RONIN: An example app that contains ICC vulnerabilities

security testiNg of INter-app communication), our approach

to automatic generation of Inter-App Communication exploits.

Figure 1 shows an overview of the approach. RONIN takes

as input an app, and starts the Vulnerability Identifier . This

analysis outputs all the statically identified vulnerable state-

ments within the app. Moreover, the Vulnerability Identifier

constructs a dictionary of the possible parameters that can be

used as payloads in the Intents and the taint graph that leads

to each identified vulnerability. According to the information

coming from the taint graph, the Oracle Instrumenter injects

code lines within the app to let RONIN’s dynamic analysis ver-

ify its distance to the vulnerability during the exploitation of the

app. The Oracle Instrumenter produces as output many instru-

mented APKs, one for each identified vulnerability. At last, the

Dynamic Exploiter leverages the information collected during

The Vulnerability Identifier analyzes an APK in search for

ICC vulnerabilities. At first, it searches for a possible entry

point. An entry point consists of an Intent function that can

lead to an ICC vulnerability (an Intent function is any function

Figure 1: The RONIN workflow. At first RONIN analyzes the APK using static

APK to verify whether a vulnerability has been reached or not. At last, RONIN

exploit a vulnerability.

that retrieves the parameters of Intents, such as getString-

Extra ). Once an entry point is found, Vulnerability Identifier

taints the related Intent variable (e.g., variable Intent at line

18 in Listing 1). Subsequently, Vulnerability Identifier analyzes

the taint graph in search for possible improper usages of the

tainted variables. If so, RONIN produces: 1) a file that con-

tains the vulnerable statements, 2) a dictionary of parameters

related to the possible payloads of the Intent, and 3) the inter-

components taint graph. To identify the vulnerable statements

we rely on the SEBASTiAn tool [25].

3.2. Static Phase: Oracle Instrumenter

previously produced by the Vulnerability Identifier to instru-

instruments the app for the three aforementioned vulnerability

types. We only need to introduce the instrumentation once per

identified vulnerability. After such one-time instrumentation,

we can reuse it to detect multiple successful exploitations.

4

| 3. RONIN: Approach | analysis and collects potential vulnerabilities. | Then RONIN instruments the |  |  |  |
| --- | --- | --- | --- | --- | --- |
| This section describes | RONIN | (ReinfOrcement learning for | leverages Intent generation through DeepRL and GUI stimulation to e | ff | ectively |
| the static phase and dynamically stimulates each instrumented | To detect whether a generated Intent successfully exploits |  |  |  |  |
| APK with random GUI events and Intents crafted through Deep | a vulnerability, RONIN instruments the app. | The | Oracle In- |  |  |
| RL. | strumenter | leverages the vulnerable statements and taint graphs |  |  |  |
| 3.1. Static Phase: Vulnerability Identifier | ment the original APK. We describe how Oracle Instrumenter |  |  |  |  |

---

## Page 6

To instrument apps vulnerable to an IDOS attack, for each

vulnerable statement RONIN adds a log instruction to record

that the vulnerable statement has been executed. Additionally,

RONIN instruments the statements can help the exploration dur-

ing the dynamic phase, i.e., the statements that connect the In-

tent function to the vulnerability.

XAS instrumentation requires to instrument each statement

where a URL is loaded. Instrumentation must ascertain the

URL loaded after the WebView’s page has finished loading to

verify whether the malicious URL injection was successful. To

that end, RONIN logs the current HTML page loaded from the

URL of a WebView once its page has finished loading.

For the FI instrumentation, RONIN injects logging state-

ments to check for three conditions that together indicate a suc-

cessful FI: (1) the target Activity has received the FI Intent, (2)

the injected Fragment was instantiated successfully, and (3) the

Activity is running without throwing any exception.

3.3. Dynamic Phase: Overview

This section describes the dynamic phase of RONIN, which Figure 2: The dynamic phase workflow.

leverages Deep RL to generate Intents for the app under test

| and uses a random algorithm to generate GUI events. Figure | Algorithm 1 | : The Dynamic Phase |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 shows the workflow of this phase. | The RL environment is | Input | : Instrumented apks, Dictionary of Intent parameters, |  |  |  |  |  |  |
| represented by an app under analysis, which is subject to seve- | Taint Graphs |  |  |  |  |  |  |  |  |
| ral interaction steps. The objective is to successfully exploit the | for | apk | ∈ | Instrumented apks | do |  |  |  |  |
| vulnerabilities discovered during the static phase. At each time | for | vulnerability | ∈ | apk | do |  |  |  |  |
| step, RONIN observes the app state, computes the state | s | t | , and | Start App Testing |  |  |  |  |  |
| chooses an action | a | t | which modifies the current Intent. Then, | Intent | = | EmptyIntent |  |  |  |
| it launches the Intent and it optionally generates random GUI | while | not Timer Expired | do |  |  |  |  |  |  |
| events. | Subsequently, it iterates, receiving the new state | s | t | + | 1 | mutateIntent | ( | Intent | ) |
| and the reward | r | t | + | 1 | (not shown in Figure 2). | Launch Intent |  |  |  |
| Intuitively, if RONIN comes closer to the vulnerability, the | LogTrace | = | CollectLogTrace() |  |  |  |  |  |  |
| reward is positive; it is neutral if the distance remains the same. | if | LogTrace is empty | then |  |  |  |  |  |  |
| Otherwise, the reward is negative if the distance from the vul- | GenerateRandomGuiEvent() |  |  |  |  |  |  |  |  |
| nerability increases. | LogTrace | = | CollectLogTrace() |  |  |  |  |  |  |
| The reward is used to update the neural network, which | end if |  |  |  |  |  |  |  |  |
| learns how to guide the Deep RL algorithm to generate Intents | Distance | = | DistanceFromVulnerability() |  |  |  |  |  |  |
| that exploit the app’s vulnerabilities. The actual update strategy | Reward | = | ComputeReward(Distance) |  |  |  |  |  |  |
| depends on the selected Deep RL algorithm. | if | Distance | = | 0 & |  |  |  |  |  |

LogTrace = Vulnerability-Exploited then

| 3.4. Dynamic Phase: Deep RL and GUI Events | Store Intent and Actions to Take |  |
| --- | --- | --- |
| The Dynamic Analysis of RONIN relies on Deep RL and | end if |  |
| random GUI events generation. | Algorithm 1 represents the | trainDeepRLAlgorithm(Distance, Reward) |
| logic of the dynamic phase. The algorithm takes as input the in- | end while |  |
| strumented APKs, the dictionary of the Intent parameters, and | end for |  |
| the taint graphs. The algorithm iterates on each vulnerability | end for |  |

of each APK and tries to exploit it within a maximum time

(10 minutes in our scenario) by mutating a default Intent and

| eventually generating a random GUI event. The GUI event is | 3.5. Dynamic Phase: Deep RL |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| generated only if the Intent does not produce any log trace. At | To apply RL, we have to map the problem of generating |  |  |  |  |  |  |  |  |  |  |  |  |
| last, the algorithm computes the distance from the target vul- | Android Intents to the standard mathematical formalization of |  |  |  |  |  |  |  |  |  |  |  |  |
| nerability and the reward used to train the DeepRL algorithm. | RL: an MDP, defined by the 5-tuple, | ⟨ | S | , | A | , | R | , | P | , ρ | 0 | ⟩ | . |
| This process iterates until the timer expires, and the algorithm | State Representation. | The state | s | t | ∈ | S | is defined as a com- |  |  |  |  |  |  |
| returns all the exploits generated during the execution. | bined state ( | a | 0 | , ... | a | n | , | node | 0 | , ... | node | m | ). The first part of the state |

a 0 , ... a n is a one-hot encoding of the current activity, i.e., a i is

equal to 1 only if the currently displayed activity is the i -th ac-

5

---

## Page 7

| tivity, it is equal to 0 for all the other activities. The second part | analysis leverages the plugin that extracts ICC vulnerabilities |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| of the state vector, | node | 0 | , ... | node | m | represents all the nodes of | in the SEBASTiAn tool [25], by extracting the vulnerable state- |  |  |  |  |  |  |  |
| the paths that lead to a specific vulnerability. When a specific | ments and the taint graph. Moreover, we added a method to the |  |  |  |  |  |  |  |  |  |  |  |  |  |
| node is traversed by the last action generated by RONIN we set | plugin to search and extract the parameters associated with the |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the corresponding node flag to 1; un-executed nodes have their | Intent functions. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| flag set to 0. | Afterwards, if any vulnerability is present, RONIN starts |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Action Representation. | Each time RONIN takes an action, | the instrumentation phase. | The Oracle Instrumenter is based |  |  |  |  |  |  |  |  |  |  |  |
| it manipulates a previously generated Intent. RONIN mutates | on SOOT [27] and it uses the taint graph to decide where to |  |  |  |  |  |  |  |  |  |  |  |  |  |
| an Intent by adding, removing, or modifying one of its parame- | inject log statements. Listing 2 shows an example of injected |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ters. Hence, an action | a | = | ⟨ | a | 0 | , | a | 1 | , | a | 2 | ⟩ | is 3-dimensional: the first | logs: each node that can potentially lead to the vulnerability is |
| component | a | 0 | specifies which type of action RONIN will apply | logged during the execution of the code. |  |  |  |  |  |  |  |  |  |  |
| to one of the Intent parameters. If zero, RONIN will remove a | RONIN generates as output many instrumented APKs, one |  |  |  |  |  |  |  |  |  |  |  |  |  |
| parameter from the Intent. Otherwise, if one, it will add | / | mod- | per identified vulnerability. Then, RONIN starts the dynamic |  |  |  |  |  |  |  |  |  |  |  |
| ify the corresponding parameter. The second component | a | 1 | en- | analysis on the instrumented APKs, leveraging the informa- |  |  |  |  |  |  |  |  |  |  |
| codes the index of the parameter to be manipulated. The third | tion collected during the static analysis: it builds the dictionary |  |  |  |  |  |  |  |  |  |  |  |  |  |
| component | a | 2 | specifies which payload is associated with the pa- | of values to use during Intent mutation, it instantiates a cus- |  |  |  |  |  |  |  |  |  |  |
| rameter selected by the previous action component. For exam- | tom environment to interact with the application, and it starts |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ple, RONIN can associate to a boolean parameter the payloads | the search for exploitations (Algorithm 1). At each time step, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| True | or | False | . | Transition Probability Function. | The transition | RONIN takes an action (i.e., it modifies the Intent) according to |  |  |  |  |  |  |  |  |
| function | P | determines which state the application can transit to | the current policy of the Deep RL algorithm. The action con- |  |  |  |  |  |  |  |  |  |  |  |
| after RONIN has taken an action. This is decided solely by the | sists of crafting and launching the Intent, and possibly generat- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| app’s execution: RONIN observes the process passively, col- | ing random GUI events on the target app. To generate random |  |  |  |  |  |  |  |  |  |  |  |  |  |
| lecting the new state after the transition has occurred. | GUI events, we used the ARES tool [28]. Once the action has |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Reward Function. | The RL algorithm used by RONIN re- | been fully processed, RONIN elaborates the log information, |  |  |  |  |  |  |  |  |  |  |  |  |
| ceives a reward | r | t | ∈ | R | every time it executes an action | a | t | . We | from which it computes observation and reward for the algo- |  |  |  |  |  |
| define the following reward function: | rithm. | RONIN arranges the whole testing session into finite- |  |  |  |  |  |  |  |  |  |  |  |  |

    Γ 1 if dist f rom vuln () t = 0

     Γ 0 if dist f rom vuln () t − dist f rom vuln () t − 1 = 0 1

2

(1) 3

4

with Γ 1 ≫ Γ 2 ≫ Γ 0 (in our implementation Γ 0 = 0, Γ 1 = 10,

5

7

At time t , the reward r t is positive ( Γ 1 ) if RONIN was able 8

vulnerability is zero. When an action takes RONIN closer to the

vulnerability without triggering it with respect to the previous

execution, the reward is slightly positive ( Γ 2 ). The reward is

RONIN features a custom environment based on the Ope-

nAI Gym[26] interface, which is a de-facto standard in the RL

field. OpenAI Gym is a toolset with a number of built-in en-

vironments for building and comparing RL algorithms. It also

includes instructions for defining custom environments. Our

custom environment interacts with an Android app.

6

length episodes, the goal being to maximize the total reward

public void onClick(View v){

TextView textView = (TextView) findViewById(R.id.concat);

Intent intent = getIntent();

Log.v("{’method’: ’onClick()’, ’unit’: ’intent.getStringExtra(..’, ’id’:

’24503’}");

String example = intent.getStringExtra("example");

textView.setText("total length: " + Integer.toString(example.length()));

}

4.2. ICC Environment

ration file) , is the initialization of the class. The addi-

nary containing the app to be analyzed and its setup. The sec-

ond function is the step(a) function, which takes an action

a as input and returns a list of objects, including observation

(code coverage state) and reward.

4.3. Algorithm Implementation

RONIN leverages Stable Baselines [29], a modular library

|  | received in each episode. Every episode lasts 100 time steps. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Once an episode comes to an end, RONIN resets the Intent to |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Γ | 2 | if | dist f rom vuln | () | t | − | dist f rom vuln | () | t | − | 1 | < | 0 | the default value, and then it uses the acquired knowledge to |  |  |  |  |
| r | t | = |  |  |  |  | − | Γ | 2 | if | dist f rom vuln | () | t | − | dist f rom vuln | () | t | − | 1 | > | 0 | reach the target node of the app in the next episode. |
| Γ | 2 | = | 1). | 6 | Log.v("{’method’: | ’onClick()’, | ’unit’: | ’textView.setText(..’, | ’id’: | ’24504’}"); |  |  |  |  |  |  |  |  |  |  |  |  |
| to trigger the selected vulnerability, i.e., the distance from the | Listing 2: An example of instrumentation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| negative ( | − | Γ | 2 | ) when the action taken does not reach the target | The ICC environment is responsible for handling the ac- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and decreases the distance from the vulnerability with respect to | tions to interact with the app. Since the environment follows |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the last execution. If the distance from the vulnerability remains | the guidelines of the Gym interface, it is structured as a class |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the same as in the last execution, the reward is neutral ( | Γ | 0 | = | 0). | with two key functions. The first function, | init(configu- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4. Implementation | tional parameter | configuration file | consists of a dictio- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4.1. Tool Overview | that adopts a plugin architecture to integrate the Deep RL al- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| As soon as it is launched, RONIN starts the static analysis | gorithm to use. | Currently, one Deep RL exploration strategy |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| on the target app in search for ICC vulnerabilities. The static | is integrated into RONIN: Soft Actor Critic (SAC) [30]. SAC |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 8

| represents one of the state-of-the-art algorithms at the time of | 5.2. Evaluation Procedure |  |  |
| --- | --- | --- | --- |
| writing [31]. Its implementation comes from the Python library | With | RQ1 | , we evaluated RONIN in terms of: 1) How many |
| Stable Baselines. RONIN also implements a second exploration | apps coming from Google Play Store are vulnerable; 2) How |  |  |
| strategy, considered as a baseline in our empirical evaluation: | many exploits can RONIN generate; 3) how many of them are |  |  |
| random exploration, where the algorithm interacts with the tar- | unique exploits. |  |  |
| get app by randomly selecting a mutation to perform on the | In | RQ2 | , we compare RONIN to Letterbomb on three apps |
| Intent. | from the Ghera dataset. | These apps contain four vulnerabili- |  |
| RONIN is publicly available as open source software at the | ties (i.e., 3 IDOS, 1 FI). The objective is to successfully detect |  |  |
| url: | https://github.com/H2SO4T/RONIN | . | and then exploit the vulnerabilities within the apps, obtaining a |

We seek to address the following research questions:

• RQ2 How does RONIN compare with the state-of-the-art

on a vulnerability benchmark? We aim to evaluate the

performance of RONIN in comparison with one baseline,

Letterbomb. To the best of our knowledge, Letterbomb

represents the state-of-the-art, and produces a diversified

set of exploits capable of triggering a vulnerability. We

evaluate the two tools on a benchmark to understand the

key di ff erences between them.

• RQ3 How does RONIN compare with the state-of-the-art

on apps obtained from the wild? We aim to evaluate the

performance of RONIN and Letterbomb in detecting the

three considered vulnerabilities in the wild, considering

a set of apps coming from Google Play Store.

• RQ5 How does RONIN behave when Deep RL is sub-

stituted with a random algorithm? We aim to evaluate

RONIN’s performance in detecting the three considered

vulnerabilities when it generates Intents using a random

algorithm (ablation study).

among the 20k most downloaded apps. Such apps are the top

free Android apps ranked by the number of installations accord-

ing to Androidrank [21], and have been downloaded from the

Google Play Store between Dec. 2021 and Jan. 2022.

7

correct sequence of actions that fulfill exploitation of the vul-

successes of both tools being compared.

In RQ3 , we compare RONIN to Letterbomb on the num-

In RQ5 , we evaluate RONIN’s performance (number of ex-

ploits and number of unique exploits) when generates Intents

randomly. We also compare the Deep RL and random algorithm

on the time necessary to generate the first exploit in each of

the exploited vulnerabilities. To account for non-determinism,

we applied the Wilcoxon non-parametric statistical test to draw

conclusions on the di ff erence between Deep RL and random

algorithm, adopting the conventional p-value threshold at α =

0.05.

6. Experimental Results

6.1. RQ1: Exploit Generation

Table 1 (top) shows the results of RQ1, split by each of

generated an exploit (Expl. Apps), followed by the number of

successfully generated exploits and the number of unique ex-

ploits , where an exploit is unique if it either reaches a unique

vulnerable statement or, in the case of FI, it successfully injects

a unique Fragment.

RONIN successfully exploited 25 apps containing IDOS

number of exploits .

| 5. Evaluation | nerability. We investigate the reasons behind failures and the |  |  |  |
| --- | --- | --- | --- | --- |
| • | RQ1 | To what extent can RONIN identify exploits for the | ber of generated exploits and unique exploits. | Moreover, we |
| three types of vulnerabilities described? | Exploit genera- | evaluate whether the exploits generated by the two tools di | ff | er |
| tion is the ultimate goal of RONIN. We evaluate RONIN’s | among them or belong mostly to the same set. |  |  |  |
| exploit generation capability by considering both exploits | In | RQ4 | , we disable GUI events generation in RONIN to |  |
| and unique exploits. | We aim to evaluate the ability of | evaluate their impact on the overall performance (number of |  |  |
| RONIN to generate multiple di | ff | erent exploits. | exploits and number of unique exploits). |  |
| • | RQ4 | How does RONIN behave when the generation of | the three considered vulnerability types (i.e., IDOS, XAS, and |  |
| GUI events is disabled? | We aim to evaluate RONIN’s | FI). In Column 2, we report the number of Google Play Store |  |  |
| performance in detecting the three considered vulnera- | apps for which RONIN statically detected a vulnerability, fol- |  |  |  |
| bilities when GUI event generation is disabled (ablation | lowed by the number of detected vulnerabilities. In Column 4, |  |  |  |
| study). | we report the number of apps for which RONIN successfully |  |  |  |
| 5.1. Evaluation Design | vulnerabilities, ten apps containing XAS vulnerabilities, and |  |  |  |
| To evaluate the proposed approach, we used the software | one with an FI vulnerability. RONIN obtained 46 unique ex- |  |  |  |
| subjects from the Ghera dataset [19] and the Google Play Store. | ploits and 180 total exploits for IDOS, 10 unique and 18 total |  |  |  |

Ghera contains benign apps with vulnerabilities related to Crypto, exploits for XAS, two unique and six total exploits for FI. It

| ICC, Networking, NonAPI, Permission, Storage, System, and | should be noticed that a vulnerable statement may be exploited |  |
| --- | --- | --- |
| Web APIs. | From the Ghera dataset, we used three ICC apps | from more than one program path, resulting in multiple non- |
| that contain four vulnerabilities related to IDOS, XAS, and FI. | unique exploits for the same vulnerable statement. | These re- |
| From the Google Play Store, we randomly selected 1500 apps | sults indicate that | RONIN is capable of producing a sizeable |

---

## Page 9

RONIN just one vulnerability, but it can not exploit it.

| Vuln. Type | Apps | Vulnerabilities | Expl. Apps | Exploits | Unique Expl. |
| --- | --- | --- | --- | --- | --- |
| FragmentInjec. | IDOS | ✗ | ✗ | D | D |
| FI | ✗ | ✗ | D | D |  |
| UnhandledExc. | IDOS | D | ✗ | D | D |
| UnprotectedBroad. | IDOS | ✗ | ✗ | D | D |

6.2. RQ2: Comparison with Letterbomb on Ghera

| 2 | @Override |  |  |  |
| --- | --- | --- | --- | --- |
| 4 | if (intent.getAction() | != null && intent.getAction().equals("edu.ksu.cs. |  |  |
| 5 | String | number | = | intent.getStringExtra("number"); |
| 7 | SmsManager | smsManager | = SmsManager.getDefault(); |  |
| 9 | Log.d("benign", | "Message sent"); |  |  |
| 11 | } |  |  |  |

Listing 3: IDOS vulnerability occurring when either of the extra strings at lines

Let us consider the exploited vulnerabilities (Columns 4

and 6 in Table 2). RONIN successfully exploited all the stati-

1

cally detected vulnerabilities, while Letterbomb fails in exploit- 2

3

ing the single IDOS it was able to detect statically. The latter 4

5

7

that the vulnerability at line 12 in the app UnhandledException- 9

10

12

pressed. Once pressed, the button consumes the Intent (line 9), 13

14

then extracts the extra values (lines 10-11), and at last calls the 15

16

function length on both extra values. Suppose one of the ex-

ploit such a vulnerability, firstly sending the correct Intent and

secondly clicking on the button that uses the payload coming

from the Intent.

In summary, RONIN can detect and exploit all vulnera-

bilities in the Ghera benchmark, while Letterbomb can detect

| Button | button | = | (Button) | findViewById(R.id.get); | 4 |  |
| --- | --- | --- | --- | --- | --- | --- |
| public | void | onclick(View | v) | { | 7 |  |
| Intent | intent | = | MainActivity.this.getIntent(); | 10 |  |  |
| String | a | = | intent.getStringExtra("s1"); | 11 |  |  |
| textView.setText("total | length:" | + | Integer.toString(a.Length() | + | b.Length | 13 |

()));

} 14

Listing 4: IDOS vulnerability occurring when the button instantiated at line 3

is pressed

RONIN is the only approach that generates exploits in the

wild for all the three types of vulnerabilities that both tools tar-

get. Table 1 (top vs bottom) shows the results of RONIN’s vul-

code.

IDOS / XAS exploits than Letterbomb and can generate FI ex-

ploits that are missed by Letterbomb .

call.setOnClickListener(new View.OnClickListener(){

@override

public void onClick(View view) {

Intent intent = getIntent();

String emergency_number = intent.getStringExtra("emergency_number");

Manifest.permission.CALL_PHONE) != PackageManager.PERMISSION_GRANTED) {

permission.CALL_PHONE}, REQUEST_CALL);

} else {

if (emergency_number.length() = 10) {

startActivity(new Intent(Intent.ACTION_CALL, Uri.parse(dial)));

}

}

}

});

onClick

8

| IDOS | 537 | 867 | 25 | 180 | 46 | 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XAS | 158 | 134 | 10 | 18 | 10 | public | void | onResume() | { | 2 |
| FI | 28 | 31 | 1 | 6 | 2 | super.onResume(); | 3 |  |  |  |
| Letterbomb | button.setOnClickListener(new | View.OnClickListener(){ | 5 |  |  |  |  |  |  |  |
| IDOS | 1232 | 1523 | 12 | 74 | 15 | @Override | 6 |  |  |  |
| XAS | 174 | 231 | 3 | 10 | 3 | TextView | textView | = | (TextView); | 8 |
| FI | 84 | 119 | 0 | 0 | 0 | MainActivitv.this.findViewById(R.id.concat); | 9 |  |  |  |
| Table 1: Detected vulnerabilities and generated exploits | String | b | = | intent.getstringExtra("s2") | ; | 12 |  |  |  |  |
| Bench. App | Vuln. | Letterbomb | RONIN | }); | 15 |  |  |  |  |  |
| Detected | Exploited | Detected | Exploited | } | 16 |  |  |  |  |  |
| Table 2: Comparison between RONIN and Letterbomb on Ghera | 6.3. RQ3: Comparison with Letterbomb in the Wild |  |  |  |  |  |  |  |  |  |
| Table 2 shows the comparison between RONIN and Letter- | nerability comparison with Letterbomb in the wild. For IDOS |  |  |  |  |  |  |  |  |  |
| bomb on the apps from the Ghera dataset. RONIN detects the | and XAS, RONIN generates three times more unique exploits |  |  |  |  |  |  |  |  |  |
| known ICC vulnerabilities in all the apps, while Letterbomb | than Letterbomb. For FI, Letterbomb can not generate any ex- |  |  |  |  |  |  |  |  |  |
| only in one. In most cases of false negatives, Letterbomb fails | ploit, while RONIN generates two exploits. |  |  |  |  |  |  |  |  |  |
| to detect the lack of null checks when executing backward data- | We also compared the two sets of vulnerabilities exploited |  |  |  |  |  |  |  |  |  |
| flow analysis along the use-def chains. | Listing 3 shows the | by the two tools and found that 93% of the vulnerabilities ex- |  |  |  |  |  |  |  |  |
| IDOS vulnerability of app | UnprotectedBroadcastRecv-PrivEsca- | ploited by Letterbomb are also triggered by RONIN. The re- |  |  |  |  |  |  |  |  |
| lation-Lean | at line 8. This vulnerability can be exposed when | maining 7% of vulnerabilities are not covered by RONIN be- |  |  |  |  |  |  |  |  |
| the Intent provided to the | BroadcastReceiver | does not contain | cause its static analysis does not detect them. Moreover, 12% |  |  |  |  |  |  |  |
| one of the extra strings at lines 5-6. RONIN successfully de- | of the vulnerabilities that RONIN has exploited are related to |  |  |  |  |  |  |  |  |  |
| tects the IDOS, while Letterbomb can not identify the function | GUI events that Letterbomb can not manage. |  |  |  |  |  |  |  |  |  |
| sendTextMessage | as a possible cause of a crash. | Listing 5 shows an example of vulnerability that Letter- |  |  |  |  |  |  |  |  |
| 1 | public class | MyReceiver | extends BroadcastReceiver { | bomb does not exploit. This vulnerability is similar to the one |  |  |  |  |  |  |
| 3 | public | void | onReceive | (Context context, Intent intent) { | presented for RQ2. | At line 12, we have an IDOS vulnera- |  |  |  |  |
| benign.myrecv")){ | bility contained within the function attached to a button. | If |  |  |  |  |  |  |  |  |
| 6 | String | text | = | intent.getStringExtra("text"); | RONIN sends an Intent that does not contain the extra param- |  |  |  |  |  |
| 8 | smsManager. | sendTextMessage(number, null, "Benign: " + text, null, | null); | eter | emergency number | , the if condition at line 12 will gen- |  |  |  |  |
| 10 | } | erate a crash, raising a | NullPointerException | . Letterbomb misses |  |  |  |  |  |  |
| 12 | } | it because it does not generate GUI events to reach vulnerable |  |  |  |  |  |  |  |  |
| 5-6 is not supplied | In summary, | RONIN can generate three times more unique |  |  |  |  |  |  |  |  |
| failure happened because Letterbomb does not generate GUI | 6 | if | (ContextCompat.checkSelfPermission(getcontext(), |  |  |  |  |  |  |  |
| events when trying to exploit a vulnerability. Listing 4 shows | 8 | ActivityCompat.requestPermissions(getActivity(), | new | String[]{Manifest. |  |  |  |  |  |  |
| DOS-Lean | is triggered when the button instantiated at line 3 is | 11 | String | dial | = | "tel:" | + | emergency_number; |  |  |
| tra values is unavailable: then, the app crashes. RONIN can ex- | Listing 5: | IDOS vulnerability occurring when the button attached to the |  |  |  |  |  |  |  |  |

---

## Page 10

6.4. RQ4: Disabling GUI Events RONIN Random

found by RONIN decreases by 7, 6 IDOS, and 1 XAS, respec-

also decreases, specifically by five apps (for IDOS). These re-

sults confirm that adding GUI event generation is extremely

useful for covering a broader range of vulnerabilities .

RONIN Without GUI Events

| Vuln. Type | Expl. Apps | Exploits | Unique Expl. |
| --- | --- | --- | --- |
| IDOS | 20 (-20%) | 162 (-10%) | 40 (-13%) |
| XAS | 10 | 14 (-22%) | 9 (-10%) |
| FI | 1 | 6 | 2 |

Table 3: RONIN’s reduced performance when GUI Events are disabled

6.5. RQ5: DeepRL vs Random

Table 4 shows the vulnerabilities exploited by RONIN when

using random Intent generation instead of Deep RL. The two

approaches perform similarly regarding the number of exploited

apps and unique exploits. RONIN with the random method only

misses two vulnerabilities and one app. We can appreciate the

di ff erence between the two methods when looking at the to-

tal number of generated exploits. Actually, RONIN with Deep

RL generates 48 more exploits than RONIN with the random

method.

Let us now consider the time required by either version of

RONIN to generate an exploit. Figure 3 shows the comparison

between Deep RL and Random on one of the analyzed apps.

When the point lies on the x − axis ( y = 0), the action did not

generate any exploit at the corresponding time step. When y

equals 1, one of the two algorithms generates a valid exploit for

the analyzed app. The Deep RL approach remains more con-

sistent than Random in generating exploits after generating the

first one and it generates the first exploit earlier than random.

The reason is that once the Deep RL algorithm generates the

first exploit, it is encouraged to generate new exploits similar

to the previous one, leveraging the knowledge acquired so far.

On the contrary, the random method does not have any memory

of the past actions, resulting in poor performance compared to

Deep RL.

needed to generate the first exploit for each of the apps under

analysis. The Deep RL approach employs fewer time steps to

generate the first exploit, driven by the negative or the posi-

tive reward it receives. Instead, the random approach could not

| Vuln. Type | Expl. Apps | Exploits | Unique Expl. |
| --- | --- | --- | --- |
| XAS | 10 | 14 (-22%) | 10 |

adopted and Deep RL is disabled

Figure 3: Time required by Deep RL vs Random to generate an exploit

generate the first exploit

7. Related Works

9

| Table 3 shows the di | ff | erence of behaviors when we disable | IDOS | 24 (-4%) | 137 (- 24%) | 44 (-5%) |
| --- | --- | --- | --- | --- | --- | --- |
| GUI events in RONIN. The overall number of unique exploits | FI | 1 | 5 (-17%) | 2 |  |  |
| tively (see Column 4 in Table 3). The number of exploited apps | Table 4: | RONIN’s reduced performance when random Intent generation is |  |  |  |  |
| Figure 4 shows the distribution of the number of time steps | Figure 4: Distribution of the time steps required by Deep RL vs Random to |  |  |  |  |  |
| leverage any information collected during the dynamic phase, | Several approaches have been developed to identify vulner- |  |  |  |  |  |
| so the occurrence of the first exploit is unpredictable and is not | abilities in Android apps [32]. ComDroid [33] was one of the |  |  |  |  |  |
| consistent across runs. Moreover, the Wilcoxon non-parametric | first significant works to target ICC-based vulnerabilities in de- |  |  |  |  |  |
| statistical test demonstrates that the di | ff | erence between the al- | tail, Epicc [34] and IC3 [35] extracted information about Intents |  |  |  |
| gorithms is statistically significant ( | p | -value | < α | ). | in a flow-sensitive manner. IccTA [36] and COVERT [37] iden- |  |
| In summary, | while RONIN with random Intent generation | tified vulnerabilities involving interaction between apps rather |  |  |  |  |
| can still generate almost the same number of unique exploits | than only individual apps. | FlowDroid [38] performs a static |  |  |  |  |
| as RONIN with Deep RL, the latter generates the first exploit | taint analysis to identify flows and privacy leakages from An- |  |  |  |  |  |
| much earlier than Random and it then continues to generate | droid API sources to sinks. Amandroid [7] is a static analysis |  |  |  |  |  |
| valid exploits much more consistently than Random | . | approach based on Soot [27] that performs inter-component, |  |  |  |  |

---

## Page 11

| and intra-component data flow point-to-point analysis. | This | app. | However, Letterbomb only stimulates an app using the |  |
| --- | --- | --- | --- | --- |
| methodology combines FlowDroid and IccTA approaches, re- | Intents, but Intent usage can also be triggered by other events |  |  |  |
| sulting in more precise results with respect to both. DroidPa- | coming from the GUI, which may result in missed vulnerabil- |  |  |  |
| trol [8] identifies a list of potential vulnerabilities and proposes | ities for Letterbomb. Moreover, Letterbomb becomes inappli- |  |  |  |
| quick fixes. MobSf [9] executes a plethora of security evalua- | cable when the constraints to reach a certain path within the |  |  |  |
| tions. However, none of these approaches can determine pro- | app are too di | ffi | cult to traverse. | RONIN overcomes the lim- |
| gram paths and the Intents needed to execute them. | itations of Letterbomb by automatically triggering GUI events |  |  |  |
| Another set of approaches relies solely on dynamic anal- | and by adopting a Deep RL algorithm to generate valid exploits. |  |  |  |
| ysis to discover vulnerabilities. | Buzzer [39] fuzzes Android | Our empirical evaluation showed the superiority of our new ap- |  |  |
| system services to find flaws. Stowaway [40] detects permis- | proach w.r.t. Letterbomb. |  |  |  |

sion overprivileged dynamically. Mutchler et al. [41] look for

vulnerabilities in Android web apps. IntentDroid [24] dynami-

cally stimulates an app’s Intent interface to find flaws. None of

tent Provider of another app without the necessary permissions

or authorization. To avoid privilege escalation threats, IPC In-

spection [43] is an OS-based security mechanism that evaluates

dit [14] is primarily concerned with discovering privacy leak-

[2]

and dynamic analysis and the ability to establish data leak poli-

source tools to extract high-level behaviors, API calls, and crit-

[5]

source and sink functions during its execution, and finally eval-

of dynamic taint analysis and is reported to the user. Schindler

[10]

delegation vulnerabilities. To the best of our knowledge, Letter-

symbolic execution-based static analysis. During the second

phase, the tool tries to exploit the statically discovered vulner-

abilities by generating an Intent and sending it to the analyzed

10

8. Conclusion

References

2027 (2022).

StatCounter, Mobile operating system market share worldwide (2022).

mobile/worldwide

quarter 2015 to 2nd quarter 2022 (2022).

URL https://www.statista.com/statistics/289418/

P. Bhattacharya, L. Ulanova, I. Neamtiu, S. C. Koduru, An empirical anal-

ysis of bug reports and bug fixing in open source android apps, in: 2013

tive comparison of program analysis techniques for security assessment

apps, ACM Transactions on Privacy and Security (TOPS) 21 (3) (2018)

1–32.

tions conference (COMPSAC), Vol. 1, IEEE, 2019, pp. 565–569.

M. K. Alzaylaee, S. Y. Yerima, S. Sezer, Dynalog: An automated dynamic

analysis framework for characterizing android applications, in: 2016 In-

android third-party libraries, Journal of Information Security and Appli-

cations 46 (2019) 259–270.

| these strategies use static analysis, preventing them from find- | This paper introduces RONIN, an approach for generating |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ing many potential ICC-based program paths that may lead to a | exploits for Android ICC vulnerabilities through static analy- |  |  |  |  |  |
| vulnerability. | sis, Deep Reinforcement Learning-based dynamic analysis and |  |  |  |  |  |
| A variety of approaches rely upon the conjunction of static | software instrumentation. RONIN, achieves better results than |  |  |  |  |  |
| and dynamic analysis to detect vulnerabilities. | ContentScope | state-of-the-art and baseline tools, improving the number of ex- |  |  |  |  |
| [42] examines Android app Content Providers to identify in- | ploited vulnerabilities. RONIN can generate three times more |  |  |  |  |  |
| stances when data from those components leaked or was con- | unique IDOS | / | XAS exploits than Letterbomb and can generate |  |  |  |
| taminated. This happens when one app manipulates the Con- | FI exploits that are missed by Letterbomb. |  |  |  |  |  |
| an app’s privileges as it gets requests from other apps. AppAu- | [1] | Statista, Number of smartphone subscriptions worldwide from 2016 to |  |  |  |  |
| age vulnerabilities. However, it only conducts minimal Intent | URL | https://www.statista.com/statistics/330695/ |  |  |  |  |
| analysis (e.g., failing to account for various Intent attributes). | number-of-smartphone-users-worldwide/ |  |  |  |  |  |
| AppCaulk [44] detects and stops data breaches through static | URL | https://gs.statcounter.com/os-market-share/ |  |  |  |  |
| cies. | The DynaLog [10] framework leverages existing open- | [3] | Statista, Number of available apps in the google play store from 2nd |  |  |  |
| ical events that can be used to examine an application. He et | number-of-available-apps-in-the-google-play-store-quarte |  |  |  |  |  |
| al. [11] developed a tool that can first identify the third-party | [4] | W. Enck, D. Octeau, P. D. McDaniel, S. Chaudhuri, A study of android |  |  |  |  |
| libraries inside apps, then extracts call chains of the privacy | application security., in: USENIX security symposium, Vol. 2, 2011. |  |  |  |  |  |
| uates the risks of privacy leaks of the third-party libraries ac- | 17th European Conference on Software Maintenance and Reengineering, |  |  |  |  |  |
| cording to the privacy leakage paths. | 2013, pp. 133–143. | doi:10.1109/CSMR.2013.23 | . |  |  |  |
| Methods such as [12] [13] also detect vulnerabilities by | [6] | A. Sadeghi, H. Bagheri, J. Garcia, S. Malek, A taxonomy and qualita- |  |  |  |  |
| combining static and dynamic analysis. Chao et al. [13] pro- | of android software, IEEE Transactions on Software Engineering 43 (6) |  |  |  |  |  |
| pose an approach that uses a static analysis method to obtain | (2017) 492–530. | doi:10.1109/TSE.2016.2615307 | . |  |  |  |
| some basic vulnerability analysis results for the application. | [7] | F. Wei, | S. Roy, | X. Ou, | Amandroid: | A precise and general inter- |
| Then, the application security vulnerability is verified by means | component data flow analysis framework for security vetting of android |  |  |  |  |  |
| et al. [12] combine free open-source tools to support developers | [8] | M. A. I. Talukder, H. Shahriar, K. Qian, M. Rahman, S. Ahamed, F. Wu, |  |  |  |  |
| in checking that their application does not introduce security is- | E. Agu, Droidpatrol: a static analysis plugin for secure mobile software |  |  |  |  |  |
| sues by using third-party libraries. None of these methods are | development, in: 2019 IEEE 43rd annual computer software and applica- |  |  |  |  |  |
| thought to generate exploits. In [45, 46] Demissie et al. present | [9] | MobSF, Mobile security framework (mobsf) (2022). |  |  |  |  |
| an approach based on static analysis and automated test case | URL | https://github.com/MobSF/ |  |  |  |  |
| generation to generate exploits that target the Permission Re- | Mobile-Security-Framework-MobSF |  |  |  |  |  |
| bomb [18] is the only tool that automatically generates exploits | ternational Conference On Cyber Security And Protection Of Digital Ser- |  |  |  |  |  |
| for IDOS, XAS, and FI vulnerabilities. | Letterbomb relies on | vices (Cyber Security), IEEE, 2016, pp. 1–8. |  |  |  |  |
| two phases. The first phase leverages combined path-sensitive | [11] | Y. He, X. Yang, B. Hu, W. Wang, Dynamic privacy leakage analysis of |  |  |  |  |

---

## Page 12

| [12] | C. Schindler, M. Atas, T. Strametz, J. Feiner, R. Hofer, Privacy leak iden- | maximum entropy deep reinforcement learning with a stochastic actor |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tification in third-party android libraries, in: 2022 Seventh International | (2018). | doi:10.48550/ARXIV.1801.01290 | . |  |  |  |  |  |  |  |  |  |
| Conference On Mobile And Secure Services (MobiSecServ), IEEE, 2022, | URL | https://arxiv.org/abs/1801.01290 |  |  |  |  |  |  |  |  |  |  |
| pp. 1–6. | [31] | A. Hill, A. Ra | ffi | n, M. Ernestus, A. Gleave, A. Kanervisto, R. Traore, |  |  |  |  |  |  |  |  |
| [13] | W. Chao, L. Qun, W. XiaoHu, R. TianYu, D. JiaHan, G. GuangXin, S. En- | P. | Dhariwal, | C. | Hesse, | O. | Klimov, | A. | Nichol, | M. | Plappert, |  |
| Jie, An android application vulnerability mining method based on static | A. | Radford, | J. | Schulman, | S. | Sidor, | Y. | Wu, | Stable | baselines | al- |  |
| and dynamic analysis, in: 2020 IEEE 5th Information Technology and | gorithms, | https://stable-baselines3.readthedocs.io/ |  |  |  |  |  |  |  |  |  |  |
| Mechatronics Engineering Conference (ITOEC), IEEE, 2020, pp. 599– | en/master/guide/algos.html | (2018). |  |  |  |  |  |  |  |  |  |  |
| 603. | [32] | A. Sadeghi, H. Bagheri, J. Garcia, S. Malek, A taxonomy and qualita- |  |  |  |  |  |  |  |  |  |  |
| [14] | M. Xia, L. Gong, Y. Lyu, Z. Qi, X. Liu, E | ff | ective real-time android ap- | tive comparison of program analysis techniques for security assessment |  |  |  |  |  |  |  |  |
| plication auditing, in: 2015 IEEE Symposium on Security and Privacy, | of android software, IEEE Transactions on Software Engineering 43 (6) |  |  |  |  |  |  |  |  |  |  |  |
| IEEE, 2015, pp. 899–914. | (2016) 492–530. |  |  |  |  |  |  |  |  |  |  |  |
| [15] | M. InfoSecurity, Drozer (2022). | [33] | E. Chin, | A. P. Felt, | K. Greenwood, | D. Wagner, | Analyzing inter- |  |  |  |  |  |
| URL | https://github.com/WithSecureLabs/drozer | application communication in android, in: Proceedings of the 9th inter- |  |  |  |  |  |  |  |  |  |  |
| [16] | ac pm, Inspeckage (2022). | national conference on Mobile systems, applications, and services, 2011, |  |  |  |  |  |  |  |  |  |  |
| URL | https://github.com/ac-pm/Inspeckage | pp. 239–252. |  |  |  |  |  |  |  |  |  |  |
| [17] | sensepost, Objection (2022). | [34] | D. Octeau, | P. McDaniel, | S. Jha, | A. Bartel, | E. Bodden, | J. Klein, |  |  |  |  |
| URL | https://github.com/sensepost/objection | Y. Le Traon, E | ff | ective | { | Inter-Component | } | communication mapping in |  |  |  |  |
| [18] | J. Garcia, M. Hammad, N. Ghorbani, S. Malek, Automatic generation | android: An essential step towards holistic security analysis, in: 22nd |  |  |  |  |  |  |  |  |  |  |
| of inter-component communication exploits for android applications, in: | USENIX Security Symposium (USENIX Security 13), 2013, pp. 543– |  |  |  |  |  |  |  |  |  |  |  |
| Proceedings of the 2017 11th Joint Meeting on Foundations of Software | 558. |  |  |  |  |  |  |  |  |  |  |  |
| Engineering, 2017, pp. 661–671. | [35] | D. Octeau, D. Luchaup, M. Dering, S. Jha, P. McDaniel, Composite con- |  |  |  |  |  |  |  |  |  |  |
| [19] | J. Mitra, V.-P. Ranganath, Ghera: A repository of android app vulner- | stant propagation: Application to android inter-component communica- |  |  |  |  |  |  |  |  |  |  |
| ability benchmarks, in: | Proceedings of the 13th International Confer- | tion analysis, in: 2015 IEEE | / | ACM 37th IEEE International Conference |  |  |  |  |  |  |  |  |
| ence on Predictive Models and Data Analytics in Software Engineering, | on Software Engineering, Vol. 1, IEEE, 2015, pp. 77–88. |  |  |  |  |  |  |  |  |  |  |  |
| PROMISE, Association for Computing Machinery, New York, NY, USA, | [36] | L. Li, A. Bartel, T. F. Bissyand´ | e, J. Klein, Y. Le Traon, S. Arzt, |  |  |  |  |  |  |  |  |  |
| 2017, p. 43–52. | doi:10.1145/3127005.3127010 | . | S. Rasthofer, E. Bodden, D. Octeau, P. McDaniel, Iccta: Detecting inter- |  |  |  |  |  |  |  |  |  |
| URL | https://doi.org/10.1145/3127005.3127010 | component privacy leaks in android apps, in: 2015 IEEE | / | ACM 37th IEEE |  |  |  |  |  |  |  |  |
| [20] | Sutton, Reinforcement Learning: An Introduction, MIT Press, 2014. | International Conference on Software Engineering, Vol. 1, IEEE, 2015, |  |  |  |  |  |  |  |  |  |  |
| [21] | V. Mnih, K. Kavukcuoglu, D. Silver, A. Graves, I. Antonoglou, D. Wier- | pp. 280–291. |  |  |  |  |  |  |  |  |  |  |
| stra, M. Riedmiller, Playing atari with deep reinforcement learning, arXiv | [37] | H. Bagheri, A. Sadeghi, J. Garcia, S. Malek, Covert: Compositional anal- |  |  |  |  |  |  |  |  |  |  |
| preprint arXiv:1312.5602 (2013). | ysis of android inter-app permission leakage, IEEE transactions on Soft- |  |  |  |  |  |  |  |  |  |  |  |
| [22] | W. Enck, M. Ongtang, P. McDaniel, Understanding android security, | ware Engineering 41 (9) (2015) 866–886. |  |  |  |  |  |  |  |  |  |  |
| IEEE security & privacy 7 (1) (2009) 50–57. | [38] | S. Arzt, S. Rasthofer, C. Fritz, E. Bodden, A. Bartel, J. Klein, Y. Le Traon, |  |  |  |  |  |  |  |  |  |  |
| [23] | Google, Intent (2022). | D. Octeau, P. McDaniel, Flowdroid: Precise context, flow, field, object- |  |  |  |  |  |  |  |  |  |  |
| URL | https://developer.android.com/reference/ | sensitive and lifecycle-aware taint analysis for android apps, Acm Sigplan |  |  |  |  |  |  |  |  |  |  |
| android/content/Intent | Notices 49 (6) (2014) 259–269. |  |  |  |  |  |  |  |  |  |  |  |
| [24] | R. Hay, O. Tripp, M. Pistoia, Dynamic detection of inter-application com- | [39] | C. Cao, N. Gao, P. Liu, J. Xiang, Towards analyzing the input validation |  |  |  |  |  |  |  |  |  |
| munication vulnerabilities in android, in: Proceedings of the 2015 Inter- | vulnerabilities associated with android system services, in: Proceedings |  |  |  |  |  |  |  |  |  |  |  |
| national Symposium on Software Testing and Analysis, 2015, pp. 118– | of the 31st Annual Computer Security Applications Conference, 2015, |  |  |  |  |  |  |  |  |  |  |  |
| 128. | pp. 361–370. |  |  |  |  |  |  |  |  |  |  |  |
| [25] | F. | Pagano, | A. | Romdhana, | D. | Caputo, | L. | Verderame, | A. | Merlo, | [40] | A. P. Felt, E. Chin, S. Hanna, D. Song, D. Wagner, Android permissions |
| SEBASTiAn: | a | Static | and | Extensible | Black-box | Application | Se- | demystified, in: Proceedings of the 18th ACM conference on Computer |  |  |  |  |
| curity | Testing | tool | for | iOS | and | Android | applications | (10 | 2022). | and communications security, 2011, pp. 627–638. |  |  |
| doi:10.36227/techrxiv.21261573.v1 | . | [41] | P. Mutchler, A. Doup´ | e, J. Mitchell, C. Kruegel, G. Vigna, A large-scale |  |  |  |  |  |  |  |  |
| URL | https://www.techrxiv.org/articles/preprint/ | study of mobile web app security, in: Proceedings of the Mobile Security |  |  |  |  |  |  |  |  |  |  |
| SEBASTiAn_a_Static_and_Extensible_Black-box_ | Technologies Workshop (MoST), Vol. 50, 2015. |  |  |  |  |  |  |  |  |  |  |  |
| Application_Security_Testing_tool_for_iOS_and_ | [42] | Y. Z. X. Jiang, Detecting passive content leaks and pollution in android |  |  |  |  |  |  |  |  |  |  |
| Android_applications/21261573 | applications, in: Proceedings of the 20th Network and Distributed System |  |  |  |  |  |  |  |  |  |  |  |
| [26] | G. Brockman, V. Cheung, L. Pettersson, J. Schneider, J. Schulman, | Security Symposium (NDSS), 2013. |  |  |  |  |  |  |  |  |  |  |
| J. Tang, W. Zaremba, Openai gym, arXiv preprint arXiv:1606.01540 | [43] | A. P. Felt, H. J. Wang, A. Moshchuk, S. Hanna, E. Chin, Permission |  |  |  |  |  |  |  |  |  |  |
| (2016). | re-delegation: Attacks and defenses., in: USENIX security symposium, |  |  |  |  |  |  |  |  |  |  |  |
| [27] | S. R. Group, Soot - a framework for analyzing and transforming java and | Vol. 30, 2011, p. 88. |  |  |  |  |  |  |  |  |  |  |
| android applications (2022). | [44] | J. Schutte, D. Titze, J. M. De Fuentes, Appcaulk: Data leak prevention |  |  |  |  |  |  |  |  |  |  |
| URL | http://soot-oss.github.io/soot/ | by injecting targeted taint tracking into android apps, in: 2014 IEEE 13th |  |  |  |  |  |  |  |  |  |  |
| [28] | A. Romdhana, A. Merlo, M. Ceccato, P. Tonella, Deep reinforcement | International Conference on Trust, Security and Privacy in Computing |  |  |  |  |  |  |  |  |  |  |
| learning for black-box testing of android apps, ACM Transactions on | and Communications, IEEE, 2014, pp. 370–379. |  |  |  |  |  |  |  |  |  |  |  |
| Software Engineering and Methodology (2022). | [45] | B. F. Demissie, M. Ceccato, Security testing of second order permis- |  |  |  |  |  |  |  |  |  |  |
| [29] | A. Hill, A. Ra | ffi | n, M. Ernestus, A. Gleave, A. Kanervisto, R. Traore, | sion re-delegation vulnerabilities in android apps, in: Proceedings of the |  |  |  |  |  |  |  |  |
| P. Dhariwal, C. Hesse, O. Klimov, A. Nichol, M. Plappert, A. Radford, | IEEE | / | ACM 7th International Conference on Mobile Software Engineer- |  |  |  |  |  |  |  |  |  |
| J. Schulman, S. Sidor, Y. Wu, Stable baselines, | https://github. | ing and Systems, 2020, pp. 1–11. |  |  |  |  |  |  |  |  |  |  |
| com/hill-a/stable-baselines | (2018). | [46] | B. F. Demissie, M. Ceccato, L. K. Shar, Security analysis of permission |  |  |  |  |  |  |  |  |  |
| [30] | T. Haarnoja, A. Zhou, P. Abbeel, S. Levine, Soft actor-critic: O | ff | -policy | re-delegation vulnerabilities in android apps, Empirical Software Engi- |  |  |  |  |  |  |  |  |

neering 25 (6) (2020) 5084–5136.

11
