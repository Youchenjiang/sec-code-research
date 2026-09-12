---
title: "Sapienz: Multi-objective Automated Testing for Android Applications"
creator: "TeX"
pages: 12
---

# X_M_Mao_Sapienz

> **總頁數**：12 頁

---

## Page 1

Sapienz: Multi-objective Automated Testing

for Android Applications

Ke Mao Mark Harman Yue Jia

CREST Centre, University College London, Malet Place, London, WC1E 6BT, UK

k.mao@cs.ucl.ac.uk, mark.harman@ucl.ac.uk, yue.jia@ucl.ac.uk

| ABSTRACT | Where | test | automation | does | occur, | it | typically | uses |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| We introduce | Sapienz | , | an approach to Android testing | Google’s Android Monkey tool [36], which is currently inte- |  |  |  |  |
| that uses multi-objective search-based testing to automati- | grated with the Android system. Since this tool is so widely |  |  |  |  |  |  |  |
| cally explore and optimise test sequences, minimising length, | available and distributed, it is regarded as the current state- |  |  |  |  |  |  |  |
| while simultaneously maximising coverage and fault revela- | of-practice for automated software testing [53]. | Although |  |  |  |  |  |  |
| tion. | Sapienz | combines random fuzzing, systematic and | Monkey automates testing, it does so in a relatively unintel- |  |  |  |  |  |
| search-based exploration, exploiting seeding and multi-level | ligent manner: generating sequences of events at random in |  |  |  |  |  |  |  |
| instrumentation. | Sapienz | significantly outperforms (with | the hope of exploring the app under test and revealing fail- |  |  |  |  |  |
| large effect size) both the state-of-the-art technique Dyno- | ures. | It uses a standard, simple-but-effective, default test |  |  |  |  |  |  |
| droid and the widely-used tool, Android Monkey, in 7/10 | oracle [22] that regards any input that reveals a crash to be |  |  |  |  |  |  |  |
| experiments for coverage, 7/10 for fault detection and 10/10 | a fault-revealing test sequence. |  |  |  |  |  |  |  |
| for fault-revealing sequence length. When applied to the top | Automated testing clearly needs to find such faults, but |  |  |  |  |  |  |  |
| 1,000 Google Play apps, | Sapienz | found 558 unique, previ- | it is no good if it does so with exceptionally long test se- |  |  |  |  |  |
| ously unknown crashes. | So far we have managed to make | quences. | Developers may reject longer sequences as being |  |  |  |  |  |
| contact with the developers of 27 crashing apps. Of these, | impractical for debugging and also unlikely to occur in prac- |  |  |  |  |  |  |  |
| 14 have confirmed that the crashes are caused by real faults. | tice; the longer the generated test sequence, the less likely |  |  |  |  |  |  |  |
| Of those 14, six already have developer-confirmed fixes. | it is to occur in practice. Therefore, a critical goal for auto- |  |  |  |  |  |  |  |

mated testing is to find faults with the shortest possible test

sequences, thereby making fault revelation more actionable

| CCS Concepts | to developers. |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| • | Software | and | its | engineering | → | Software | testing | Exploratory testing is “simultaneous learning, test design, |
| and debugging; | Search-based software engineering; | and test execution” [11], that can be cost-effective and is |  |  |  |  |  |  |

widely used by industrial practitioners [21, 43, 46] for test-

Keywords ing in general. However, it is particularly underdeveloped

for mobile app testing [41, 42]. Although there exist several

Android; Test generation; Search-based software testing test automation frameworks such as Robotium [10] and Ap-

pium [3], they require human-implemented scripts, thereby

| 1. | INTRODUCTION | inhibiting full automation. |  |
| --- | --- | --- | --- |
| There are over 1.8 million apps available from the Google | We introduce | Sapienz | , the first approach offering multi- |
| Play marketplace, as of January 2016 [9]. | For developed | objective automated Android app exploratory testing that |  |
| internet markets such as the US, UK and Canada, mobile | seeks to maximise code coverage and fault revelation, while |  |  |
| app usage now dominates traditional desktop software us- | minimising the length of fault-revealing test sequences. Our |  |  |
| age [29]. Unfortunately, testing technology has yet to catch | goal is to produce an entirely automated approach that max- |  |  |
| up, and software testers are faced with additional problems | imises fault revelation with short test sequences. | The key |  |
| due to device fragmentation [2], which increases test effort | insight in our approach is that minimising test sequence |  |  |
| due to the number of devices that must be considered. Ac- | length and maximising other objectives can be combined in |  |  |
| cording to a study on mobile app development [45], mobile | a Pareto-optimal multi-objective search-based approach to |  |  |
| app testing still relies heavily on manual testing, while the | Android testing. By using Pareto optimality, we do not sac- |  |  |
| use of automated techniques remains rare [48]. | rifice longer test sequences, when they are the only ones that |  |  |

find faults, nor where they are necessary to achieve higher

code coverage. Nevertheless, through its use of Pareto opti-

mality, Sapienz progressively replaces such longer sequences

with shorter test sequences when equally good. The paper

makes the following primary contributions:

1) The Sapienz approach: the paper introduces the first

Pareto multi-objective approach to Android testing, combin-

ing techniques used for traditional automated testing, adapt-

ing and extending them for Android testing. The approach

---

## Page 2

Table 1: At a glance: summary of existing tools and techniques for automated Android app testing (‘OSS’

and ‘CSS’ refer to Open-Source and Closed-Source Software used as evaluation subjects respectively).

| Technique | Venue | Publicly | Emulator / | Eval. Subjects Size |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Available | Box | Approach | Crash | Replay |  |  |  |  |  |  |  |  |
| Report | Scripts | Real Device | Type | OSS | CSS |  |  |  |  |  |  |  |
| Monkey [36] | N/A | Yes | Black | Random-based | Text | No | Both | N/A | N/A | N/A |  |  |
| AndroidRipper [15] | ASE’12 | Yes | Black | Model-based | Text | No | Emulator | OSS | 1 | 0 |  |  |
| ACTEve [16] | FSE’12 | Yes | White | Program analysis | N/A | Yes | Emulator | OSS | 5 | 0 |  |  |
| A | 3 | E [20] | OOPSLA’13 | Partially | Grey | Model-based | N/A | Yes | Real device | CSS | 0 | 25 |
| SwiftHand [27] | OOPSLA’13 | Yes | Black | Model-based | N/A | No | Both | OSS | 10 | 0 |  |  |
| ORBIT [61] | FASE’13 | No | Grey | Model-based | N/A | No | Emulator | OSS | 8 | 0 |  |  |
| Dynodroid [52] | FSE’13 | Yes | Black | Random-based | Text, Image | Yes | Emulator | Both | 50 | 1,000 |  |  |
| PUMA [37] | MobiSys’14 | Yes | Black | Model-based | Text | Yes | Both | CSS | 0 | 3,600 |  |  |
| EvoDroid [53] | FSE’14 | No | White | Search-based | N/A | No | Emulator | OSS | 10 | 0 |  |  |
| SPAG-C [50] | TSE’15 | No | Black | Record-replay | N/A | Yes | Real device | Both | 3 | 2 |  |  |
| MonkeyLab [51] | MSR’15 | No | Black | Trace mining | N/A | Yes | Both | OSS | 5 | 0 |  |  |
| Thor [12] | ISSTA’15 | Yes | Black | Adverse conditions | Text, Image | Yes | Emulator | OSS | 4 | 0 |  |  |
| TrimDroid [54] | ICSE’16 | Yes | White | Program analysis | Text | Yes | Both | OSS | 14 | 0 |  |  |
| CrashScope [57] | ICST’16 | No | Black | Combination | Text, Image | Yes | Both | OSS | 61 | 0 |  |  |
| Sapienz | ISSTA’16 | Yes | Grey | Search-based | Text, Video | Yes | Both | Both | 78 | 1,000 |  |  |
| combines random fuzzing, systematic and search-based ex- | models to guide the computational search process. Unfortu- |  |  |  |  |  |  |  |  |  |  |  |
| ploration, string seeding and multi-level instrumentation, all | nately, its implementation is no longer publicly available. |  |  |  |  |  |  |  |  |  |  |  |
| of which have been extended to cater for, not only traditional | Several previous approaches are based on random testing |  |  |  |  |  |  |  |  |  |  |  |
| white box coverage (which we term ‘skeletal coverage’), but | (fuzz testing), which inject arbitrary or contextual events |  |  |  |  |  |  |  |  |  |  |  |
| also Android user interface coverage (which we term ‘skin | into the apps. | Monkey [36] is Google’s official testing tool |  |  |  |  |  |  |  |  |  |  |
| coverage’). | for Android apps, which is built into the Android platform, |  |  |  |  |  |  |  |  |  |  |  |
| 2) Experimental results: | we present the results of two | and therefore likely to be more widely used than any other |  |  |  |  |  |  |  |  |  |  |
| systematic experimental studies on open-source real-world | automated testing tool for Android apps. Monkey generates |  |  |  |  |  |  |  |  |  |  |  |
| Android apps. The first uses the 68 apps from an Android | (pseudo) random input events, which include both User In- |  |  |  |  |  |  |  |  |  |  |  |
| benchmark suite [28], while the second uses a controlled | terface (UI) events, such as clicks and gestures, and system |  |  |  |  |  |  |  |  |  |  |  |
| random sample of 10 apps from the entire F-Droid suite, | events such as screen-shot capture and volume-adjustment. |  |  |  |  |  |  |  |  |  |  |  |
| for which | Sapienz | always outperforms both Dynodroid and | Dynodroid [52] is a publicly available and open-source tool |  |  |  |  |  |  |  |  |  |
| Monkey, statistically significantly and with large effect size | that extends pure random testing with two feedback di- |  |  |  |  |  |  |  |  |  |  |  |
| in 24 out of 30 cases. | rected biases: | BiasedRandom | , which uses context adjusted |  |  |  |  |  |  |  |  |  |
| 3) The tool, Sapienz: | a practical Android testing tool | weights for each event, and | Frequency | , which has a bias |  |  |  |  |  |  |  |  |
| Sapienz | , which we make publicly available | 1 | . | towards least recently used events. The implementation sup- |  |  |  |  |  |  |  |  |
| 4) Demonstration of usefulness: | an empirical study of | ports the generation of both UI and novel system events. |  |  |  |  |  |  |  |  |  |  |
| the practical usefulness of the technique on the top 1,000 | GUI and model-based approaches are popular for testing |  |  |  |  |  |  |  |  |  |  |  |
| Google play apps. | Sapienz | found 558 unique crashes. The | Android apps [14,15,20,27,37,61]. App event sequences can |  |  |  |  |  |  |  |  |  |
| crashing behaviour has been verified on real Android devices | be generated from models, either manually constructed, or |  |  |  |  |  |  |  |  |  |  |  |
| (as well as Android emulators). At the time of writing, we | obtained from project artefacts, such as code or XML con- |  |  |  |  |  |  |  |  |  |  |  |
| have started reporting these to the developers, and 14 have | figuration files and UI execution states. | For example, An- |  |  |  |  |  |  |  |  |  |  |
| been confirmed to be genuine, previously undetected, faults, | droidRipper [15] (subsequently MobiGUITAR [14]) builds |  |  |  |  |  |  |  |  |  |  |  |
| 6 of which have already been confirmed as fixed by their | a model using a depth-first search over the user interface. |  |  |  |  |  |  |  |  |  |  |  |
| developers. | Since these are the most popular apps in cur- | Its implementation is publicly available however not open- |  |  |  |  |  |  |  |  |  |  |
| rent use, they will likely have been thoroughly tested, not | sourced. A | 3 | E [20] consists of two app exploration strategies, |  |  |  |  |  |  |  |  |  |
| merely by their developers, but also by their many (hun- | the DFS strategy (like AndroidRipper) and a taint-targeted |  |  |  |  |  |  |  |  |  |  |  |
| dreds of thousands of) users. These results demonstrate that | strategy which constructs a static activity transition graph. |  |  |  |  |  |  |  |  |  |  |  |
| Sapienz | is a practical tool for Android developers as well as | Although the tool is publicly available, the version does not |  |  |  |  |  |  |  |  |  |  |
| for researchers. This paper is the first Android app testing | support taint targeting. SwiftHand [27] dynamically builds |  |  |  |  |  |  |  |  |  |  |  |
| work to report a large-scale evaluation on popular Google | a finite state machine model of the GUI, seeking to reduce |  |  |  |  |  |  |  |  |  |  |  |
| Play apps with developer-confirmed real-world faults. | restart time, while improving test coverage. | ORBIT [61] |  |  |  |  |  |  |  |  |  |  |

is based on a combination of dynamic GUI crawling and

static code analysis, using analysis to avoid generation of

| 2. | RELATED WORK AND MOTIVATION | irrelevant UI events. PUMA [37] is a flexible framework for |  |
| --- | --- | --- | --- |
| Table 1 presents a brief survey of the characteristics of ex- | implementing various state-based test strategies. |  |  |
| isting Android testing techniques and tools, which we briefly | Prior Android testing work also employs several other ap- |  |  |
| describe below. | proaches, such as those that are program-analysis-based or |  |  |
| The most closely related work employs search-based meth- | reuse-based. | ACTEve [16] is based on symbolic execution |  |
| ods. | Mahmood et al. | introduced EvoDroid [53], the first | and concolic testing and supports the generation of both UI |
| search-based framework for Android testing. EvoDroid ex- | and system events. | CrashScope [57] uses a combination of |  |
| tracts the interface model (based on static analysis of man- | static and dynamic analyses to generate natural language |  |  |
| ifest and XML configuration files) and a call graph model | crash descriptions with replicable test scripts. SPAG-C [50] |  |  |
| (based on code analysis by using MoDisco [8]). It uses these | implements a capture-reply based on image comparison of |  |  |

screen-shots to provide reusable and accurate test oracles,

1 http://github.com/Rhapsod/sapienz

---

## Page 3

SRC/APK

S APIENZ

M OTIF C ORE Fitness Extractor Report Crash Report Coverage

Video Replay

Atomic Genes Select GA

Initialiser (Test Suites)

Collectively, these techniques cover several important test

these competing objectives simultaneously nor provides a

set of optimal tradeoff solutions like Sapienz . Furthermore,

many of these previously proposed techniques require de-

tailed app information, such as source code [16, 53], general

gorithm. The exploration strategy and app analysers of

Sapienz are described in Sections 3.2 and 3.3 respectively.

Sapienz ’ overall workflow is depicted in Figure 1.

level (white box). By contrast, should it turn out that

at method-level (grey box). However, where the developers

which can always be measured (black box).

Sapienz extracts statically-defined string constants by re-

verse-engineering the APK. These strings are used as inputs

for seeding realistic strings into the app, which has been

found to improve the performance of search-based software

Algorithm 1: Overall algorithm of Sapienz .

max generation g

generation g ← 0;

boot up devices D ; . prepare app exerciser

inject MotifCore into D ; . for hybrid exploration (see § 3.2)

instrument and install A ;

initialise population P ; . hybrid of random and motif genes

while g < g max and ¬ timeout(t) do

g ← g+1;

evaluate Q with MotifCore and update ( M , P F , C );

F ← ∅ ; . non-dominated fronts

F ← sortN onDominated ( P ∪ Q, | P | );

for each front F in F do

P ′ ← P ′ ∪ f ;

return ( M , P F , C );

Debugging Bridge (ADB). The States Logger monitors the

execution states (e.g., covered activities, crashes) of the App

of the search.

3.1 Multi-objective Search Based Testing

approach [38, 39].

∀ i = 1 , 2 , ..., n, f

(1)

A Pareto-optimal set consists of all Pareto-optimal solu-

tions (belonging to all solutions X t ), which is defined as:

∗

P , { x ~ ∗ | @ ~ x ∈ X t , ~ x ≺ x ~ ∗ } (2)

| Instrumented APK | Multi-level Instrumenter | Decompiler | Static Strings | Input | : AUT | A | , crossover probability p, mutation probability q, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AUT | max | , execution time | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Android | Output | : UI model | M | , Pareto front | P F | , test reports | C |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Device | States Logger | DB | Report Generator | M | ← | K | 0 | ; | P F | ← ∅ | ; | C | ← ∅ | ; | . | initialisation |  |  |  |  |
| Gene Interpreter | Test Replayer | Evaluate | static analysis on | A | ; | . | for string seeding (see | § | 3.3) |  |  |  |  |  |  |  |  |  |  |  |
| Motif Genes | Test Generator | Vary | Solutions | evaluate | P | with | MotifCore | and update ( | M | , | P F | , | C | ); |  |  |  |  |  |  |
| Figure 1: Sapienz workflow. | Q | ← | wholeT estSuiteV ariation | ( | P, p, q | ); | . | see Algorithm 2 |  |  |  |  |  |  |  |  |  |  |  |  |
| while Thor [12] makes use of existing test suites, seeking to | P | ′ | ← ∅ | ; | . | non-dominated individuals |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| expose them to adverse conditions. TrimDroid [54] is backed | if | \| | P | ′ | \| | ≥ | \| | P | \| | then | break; |  |  |  |  |  |  |  |  |  |
| with program analysis by extracting interface activity tran- | calculate crowding distance for | F | ; |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| sition and dependency models. | for | each individual | f | in | F | do |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| objectives, such as coverage, test sequence length, execu- | P | ′ | ← | sorted | ( | P | ′ | , | ≺ | c | ); | . | see equation 3 for operator | ≺ | c |  |  |  |  |  |
| tion time, readability and replicablity, yet none optimises | P | ← | P | ′ | [0 : | \| | P | \| | ]; | . | new population |  |  |  |  |  |  |  |  |  |
| UI models [44] and interface and/or activity transition mod- | but has not previously been used in Android testing. | Test |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| els [20, 53, 54, 55]. | While any such additional information | sequences are generated and executed by the | MotifCore |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| can help to guide test data generation, this additional in- | component, which combines random fuzzing and systematic |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| formation requirement can be an impediment to easy and | exploration, which corresponds to two types of genes: | the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| widely-applicable automation. | Given the pressing need for | low-level | atomic genes | and the high-level | motif genes | . |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| fully | automated Android testing, we designed the | Sapienz | Sapienz | ’ multi-objective search algorithm initialises the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| approach to require only the binary executable. Of the pub- | initial population via | MotifCore | ’s | Test Generator | . | Dur- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| licly available tools, Dynodroid and Monkey were found to | ing the genetic evolution process, genetic individuals are as- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| perform best in the recent comprehensive study by Choud- | signed to the | Test Replayer | when evaluating individual fit- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| hary, Gorla and Orso [28]. | Therefore, we regard these as | nesses. The individual test scripts are further decoded into |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| denoting the state-of-the-art and state-of-current-practice, | executable Android events by the | Gene Interpreter | , which |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| which we seek to improve by the introduction of | Sapienz | . | communicates with the the Android device via the Android |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3. | THE SAPIENZ APPROACH | Under Test (AUT) and produces measurement data for the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| We first outline the workflow used by our approach. Then | Fitness Extractor | to calculate the fitnesses. A set of Pareto- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| we provide component summaries of our evolutionary al- | optimal solutions and test reports are generated at the end |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sapienz | starts by instrumenting the app under test, which | Algorithm | 1 | presents | Sapienz | ’ | top-level | algorithm. |  |  |  |  |  |  |  |  |  |  |  |  |
| can be achieved in a white box, grey box or black box man- | Sapienz | optimises for three objectives: | code coverage, se- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ner as follows: | When the app’s source code is available, | quence length and the number of crashes found, using a |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sapienz | uses fine-grained instrumentation at the statement- | Pareto-optimal Search Based Software Engineering (SBSE) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| only the binary APK file is available (as is often the case | Each executable test suite | ~ | x | for the AUT is termed as |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| in real-world, industrial-strength Android testing scenarios), | a | solution | and a | solution | x | ~ | a | is | dominated | by solution | x | ~ | b |  |  |  |  |  |  |  |
| Sapienz | uses undexing and repacking to instrument the app | ( | x | ~ | a | ≺ | x | ~ | b | ) according to a fitness function if and only if: |  |  |  |  |  |  |  |  |  |  |
| disallow repackaging (as is common for commercial apps), | i | ( | x | ~ | a | ) | ≤ | f | j | ( | x | ~ | b | ) | ∧ |  |  |  |  |  |
| Sapienz | uses a non-invasive activity-level ‘skin’ coverage, | ∃ | j | = 1 | , | 2 | , ..., n, f | j | ( | x | ~ | a | ) | < f | j | ( | x | ~ | b | ) |
| testing techniques for web based testing [13], and traditional | Sapienz | ’ search-based approach uses NSGA-II to build |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| application testing [32], and also to improve realism [23], | successively-improved | Pareto-optimal | sets, | seeking | new |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

*[Image: Page 3 Image]*

---

## Page 4

Fitness

| Chromosome 2 | MotifGene 2 | Atomic Event 1 |  |
| --- | --- | --- | --- |
| … | AtomGene 3 | Atomic Event 2 | Alleles |
| … | … |  |  |
| Chromosome n | } |  |  |
| MotifGene m | Atomic Event p |  |  |

Figure 2: Genetic individual representation.

In addition to the Pareto-optimal solution, Sapienz also

an archive operator which stores any crashes found during

SBSE representation: Sapienz performs the whole test

a test suite. The representation of an individual test suite

generated by Sapienz is illustrated in Figure 2. Sapienz

generates a set of these individual test suites, which cor-

responds to a population of individuals in the evolution-

ation is achieved by using a uniform set element crossover

operate on new GUI widgets not exercised by any initial

Algorithm 2: The whole test suite variation operator.

probability q

Output : Offspring Q

Q ← ∅ ;

for i in range (0 , | P | ) do

generate r ∼ U (0 , 1);

if r < p then . apply crossover

x ′

1 , x ′

2 ← unif ormCrossover ( x 1 , x 2 );

Q ← Q ∪ x ′

1

else if r < p + q then . apply mutation

. vary test cases within the test suite x 1

if r < q then

for i in range (0 , | x | ) do

if r < q then

Q ← Q ∪ x

return Q ;

Choudhary et al. [28].

This is achieved by pre-defining patterns to capture

| Chromosome 1 | AtomGene 1 | Atomic Event | Input | : Population | P | , crossover probability | p | , mutation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Individual (Test Suite) | Chromosome (Test Case) | Gene (Test Event) | randomly select parent individuals | x | 1 | , | x | 2 | ; |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| dominating test vectors. NSGA-II is a widely-used multiob- | randomly select individual | x | 1 | ; |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| jective evolutionary search algorithm, popular in SBSE re- | x | ← | shuf f leIndexes | ( | x | 1 | ); |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| search [39], the details of which can be found elsewhere [30]. | for | i | in | range | (1 | , | \| | x | \| | , step | 2) | do |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| At the end of search, testers can choose any test suites of | generate | r | ∼ | U | (0 | , | 1); |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| interest from the Pareto-optimal set generated by | Sapienz | . | x | [ | i | − | 1] | , x | [ | i | ] | ← | oneP ointCrossover | ( | x | [ | i | − | 1] | , x | [ | i | ]); |  |  |  |
| produces an all-crash-test-suite with a set of videos for each | . | vary test events within the test case | x | [ | i | ] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| crashing scenario. | This crashing test suite is generated by | generate | r | ∼ | U | (0 | , | 1) ; |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the search process. | x | [ | i | ] | ← | shuf f leIndexes | ( | x | [ | i | ]); |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| suite evolution [13, 33] thus each individual corresponds to | else | Q | ← | Q | ∪ | (randomly selected | x | 1 | ); | . | apply reproduction |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ary algorithm. | Each individual consists of several chromo- | This selection favours test sequences with smaller non- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| somes (test sequences | 〈 | T | 1 | , T | 2 | , ..., T | m | 〉 | ) and each chromosome | domination rank and, when the rank is equal, it favours the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| contains multiple genes (test events | 〈 | E | 1 | , E | 2 | , ..., E | n | 〉 | ), which | one with greater crowding distance (less dense region). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| consist of a random combination of | atomic | and | motif genes | . | SBSE fitness evaluation: | The fitness value is recorded as |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| An | atomic gene | triggers an atomic event | e | that cannot be | a triple for each of the objectives: | coverage, length of the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| further decomposed, e.g., press down a key, while a | mo- | test and number of revealed crashes. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tif gene | is interpreted as a series of | alleles | (atomic events | SBSE Fitness evaluation can be time-consuming, but it |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 〈 | e | 1 | , e | 2 | , ..., e | p | 〉 | ). | is fortunately also embarrassingly parallel [19, 25, 56, 62]. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SBSE variation operator: | We define a | whole test suite | Therefore, in order to achieve time-efficient search, | Sapienz |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| variation operator | to manipulate individuals. The operator | supports parallel fitness evaluation, assigning individuals to |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| is depicted in Algorithm 2: It applies one of the finer-grained | multiple fitness evaluators, which may run on distributed de- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| crossover | , | mutation | and | reproduction | operators on each in- | vices (a single multicore machine was used in our evaluation, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| dividual (at test suite level). | Sapienz | ’ inter-individual vari- | when comparing | Sapienz | with other techniques). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| among individuals (test suites). The inner-individual varia- | 3.2 | Exploration Strategy |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tion is manipulated by a more complex | mutation | operator. | Android apps can have complex interactions between the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Since each individual is a test suite containing several test | events triggerable from the UI, and the states reachable |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cases, the operator first randomly shuffles test case orders | and consequent coverage achieved. | In manual testing, the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and then performs a single-point crossover on two neigh- | testers’ knowledge can be deployed to explore such com- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| bouring test cases with probability | q | , where the prior shuffle | plex interactions [42]. However, for automated testing, some |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| operation aims to improve crossover diversity. Subsequently, | other way to handle complex interactions has to be found. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the more fine-grained test case mutation operator shuffles | Simple approaches to automated Android testing use only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the test events within each test case with probability | q | , by | atomic events. Even with combinations of such events, the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| randomly swapping event positions. Although atomic events | lack of state and context awareness, makes it difficult to dis- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| include (mutable) parameters, we choose instead to mutate | cover complex interactions. | This may be one reason why |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the execution order of the events, thereby reducing the com- | many research tools were found to under-perform by com- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| plexity of the variation operator. | Mutants are possible to | parison with Monkey in the benchmark study conducted by |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| test case, because the timing of the operations are mutated. | To address this issue, | Sapienz | uses | motif patterns | , which |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The | reproduction | operator simply leaves a randomly chosen | collect together patterns of lower level events, found to be |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| individual unchanged. | good at achieving higher coverage. | Motif genes | are based |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SBSE selection: | We use the | select | operator from NSGA- | on the UI information available in the current view, which |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| II [30], which defines a crowding-distance-based comparison | is widget-based for Android apps. | Motif genes | work together |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| operator | ≺ | c | . For two test sequences | ~ | a | , and | ~ | b | . We say | ~ | a | ≺ | c | ~ | b | to perform behavioural usage patterns on the app, e.g, fill |  |  |  |  |  |  |  |  |  |  |
| if and only if: | all input fields in the current view and submit. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ~ | a | rank | < | ~ | b | rank | ∨ | ( | ~ | a | rank | = | ~ | b | rank | ∧ | ~ | a | dist | > | ~ | b | dist | ) | (3) | testers’ experience regarding complex interactions with the |

---

## Page 5

| Random Exploration | Systematic Exploration | Hybrid Exploration |
| --- | --- | --- |
| Compound | Compound | Compound |
| Event | Event | Event |

A DNA motif is a short sequence pattern that has a biolog-

tion. In our case, our motif genes seek to achieve high-level

atomic genes to achieve higher test coverage. As we explain

below, in Section 3.4, our evaluation of Sapienz relies solely

upon a single obvious, default, generic motif gene , to avoid

any risk of experimenter bias. However, in future work, we

may learn motifs from captured human-led test activities.

Hybrid exploration: Atomic genes and motif genes are

complementary (see Figure 3), so Sapienz combines them to

form hybrid sequences of test events. Random exploration

may (randomly) manage to cover unplanned UI states for

compound events (of which consists of a random combina-

tion of atomic events), but may generally achieve low overall

coverage. Systematic exploration may achieve good coverage

within planned UI state regions, but can be blocked by un-

planned compounds. The hybrid strategy used by Sapienz

is shown in Algorithm 3.

Sapienz performs two types of analysis: static analysis

for string seeding and dynamic analysis for multi-level in-

strumentation. These two features provide necessary infor-

mation for Sapienz to generate realistic test inputs and to

guide the search toward optimal test suites with high test

coverages.

String seeding: In order to extract statically de-

fined strings, Sapienz first reverse-engineers the APK file.

Sapienz obtains a list of globally applicable strings from

the decompiled XML resource files. These natural lan-

guage strings are randomly seeded into the text fields by the

MotifCore component, when performing its hybrid explo-

ration. We found this seeding to be particularly useful when

testing apps that require a lot of user-generated content, e.g.,

Facebook, because it enables Sapienz to post and comment

in an apparently more human-meaningful way. When the

APK file cannot be reverse-engineered successfully, which

is a common case for commercial apps, predefined dummy

strings 2 will replace the extracted strings from the app.

Multi-level instrumentation for skeleton and skin

coverage: In order to be practical and useful, an auto-

mated Android testing technique needs to be applicable to

both open and closed-source apps. To achieve this, Sapienz

uses multi-level instrumentation at one or all of the three

levels of applicable instrumentation granularity. The coars-

Algorithm 3: The MotifCore exploration strategy.

Input : AUT A , test sequence T = 〈 E 1 , E 2 , ..., E n 〉 , random

event list R , motif event list O , static strings S existing

UI Model M and test reports C

Output : Updated ( M, C )

for each event E in T do

if E ∈ R then . handle atomic gene

execute atomic event E and update M ;

if E ∈ O then . handle motif gene

currentActivity ← extractCurrentActivity ( A )

for each element w in uiElementSet do

if w is EditText widget then

else

update M ;

if captured crash c then

return ( M, C );

est instrumentation granularity is always possible, and is

performed through activity/screen interactions to achieve

black box testing or ‘skin coverage’ as we call it, because

it only interacts with the ‘surface’ UI and system actions

of the app. Carino and Andrews also use a similar met-

ric based on the change of GUI widgets [26]. We use the

term ‘skeletal coverage’ for the more fine-grained coverages,

achieved by grey and white box instrumentation. In some

cases, even when source code is unavailable, a finer-grained,

grey box coverage is possible at the method level, which

we term ‘backbone’ skeletal coverage. This backbone cov-

erage can be achieved by undexing the APK file, insert-

where source code is available, we can and do use traditional

statement coverage (which we term ‘full skeletal coverage’).

For such systems we can cover both the ‘skeleton and the

skin’; white box statement level coverage and black box user

interface/activity coverage.

3.4 Implementation

We have implemented the Sapienz tool on top of the

Deap framework [31] for multi-objective test suite evolution.

Sapienz achieves full skeletal coverage (statement coverage)

using EMMA [6] and backbone coverage (method coverage)

using ELLA [5]. It calculates skin coverage (activity cover-

age) by calling Android’s own ActivityManager for extract-

ing activity/screen information.

For atomic genes , the evaluation version of Sapienz sup-

ports 10 types of atomic events that originate from Android

system source, including Touch , Motion , Rotation , Track-

ball , PinchZoom , Flip , Nav (navigation key), MajorNav ,

AppSwitch , SysOp (system operations such as ‘volume mute’

and ‘end call’). Regarding motif genes , of course, there is a

wide range of choices for motif patterns, and we distinguish

between those that are generic (applicable to all apps) and

those that are bespoke (applicable to only a small homoge-

neous set of apps). For our evaluation purposes, we resisted

the temptation to have any bespoke motif genes , since these

would require human intuition and intelligence. Further-

| Simple Event | Compound Event | Visited States | uiElementSet | ← | extractU iElement | ( | currentActivity | ) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Figure 3: Hybrid exploration strategy. | seed string | s | ∈ S | into | w | ; |  |  |  |
| app. The | motif gene | is inspired by how a DNA motif works: | exercise | w | according to motif patterns in | E | ; |  |  |
| ical function. | Motifs are combined with atomic sequences | ( | a, m, s | ) | ← | get covered activities, methods, statements; |  |  |  |
| so that, together, they can express the overall DNA func- | C | ← | C | ∪ | ( | a, m, s | ); | . | update coverage reports |
| functions (by defining patterns) and to work together with | C | ← | C | ∪ | c | ; | . | update crash reports |  |
| 3.3 | Static and Dynamic Analysis | ing probes and then repackaging the binary file. Of course, |  |  |  |  |  |  |  |
| 2 | In our particular implementation, a single string of ‘0’ is | more, we imbued our evaluation version of the | Sapienz | tool |  |  |  |  |  |
| used to ensure that no fields is empty. | with only a single (intuitively obvious) generic | motif gene |  |  |  |  |  |  |  |

---

## Page 6

| that systematically exercises text fields and clickable UI wid- | achieve higher coverage, but we need to provide short se- |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| gets under the corresponding view, which is applicable to all | quences to testers for debugging purposes [17]. Intuitively, |  |  |  |  |
| apps. | It first seeds strings into all text fields and then at- | shorter sequences are more likely to be attractive and ac- |  |  |  |
| tempts to exercise each clickable widget to transfer to the | tionable to developers [34, 49]. This motivates RQ3. |  |  |  |  |
| next view. Such a motif pattern might perform appropriate | RQ3 (Sequence length): | How does | Sapienz | compare |  |
| actions in scenarios such as filling in and submitting a form. | to the state-of-the-art and the state-of-practice in terms of |  |  |  |  |
| We used this simple-minded approach for the evaluation ver- | the length of the fault-revealing test sequences it returns? |  |  |  |  |
| sion of | Sapienz | , to avoid risking any experimenter bias that | We wish to go further in our empirical analysis, because |  |  |
| might otherwise introduce human ingenuity into the | motif | the Choudhary et al. benchmark suite set [28], although an |  |  |  |
| gene | construction process. As a result, the findings reported | excellent starting point, consists of only 68 apps, whereas |  |  |  |
| in the following section can be regarded as lower bounds on | there are, in total (at the time of writing) 1,112 apps in the |  |  |  |  |
| the performance of our approach; with a smarter selection of | overall F-Droid community [7]. There could potentially be |  |  |  |  |
| generic motif patterns, results will improve, and would fur- | some sampling or other biases if we restrict ourselves solely |  |  |  |  |
| ther improve with the construction of bespoke | motif genes | to the benchmark apps. | Furthermore, since | Sapienz | and |
| for particular apps. | the other techniques use randomised algorithms, it is widely |  |  |  |  |
| The | Sapienz | tool generates a set of artefacts for reuse, | regarded as best practice to perform an inferential statistical |  |  |
| including reusable | test suites | , detailed | coverage reports | and | analysis of the performance of each algorithm, reporting sta- |
| crash reports | (with corresponding fault-revealing test cases | tistical significance and effect size [18, 40]. Therefore, RQ4 |  |  |  |
| and automatically captured crash videos as witnesses for the | investigates the findings that can be reported using statisti- |  |  |  |  |
| failures induced by test cases). | cal significance and effect size on multiple runs of the tools, |  |  |  |  |

We evaluate the Sapienz approach by conducting three

empirical studies on both open-source and popular closed-

source Android apps. We investigate whether Sapienz can

optimise multiple objectives and find previously unknown

real faults, within limited (30 minutes per app) execution

time on real-world production hardware.

As a sanity check, we first want to establish that we have

a reliable experimental infrastructure. This is because there

are a number of settings and parameter choices that could

affect the results and, as been widely noted in other areas of

empirical software engineering [58, 60], the choice of param-

eter tuning options can have a dramatic effect on results. To

ensure reliability, we check that our infrastructure replicates

the results previously reported by Choudhary et al. [28].

RQ0 (Reliable replication): Does our experimental

infrastructure reliably replicate the results from the recent

thorough study by Choudhary et al. [28]?

We call this RQ0 (rather than RQ1) since it merely estab-

lishes that our experimental infrastructure replicates recent

results, suggesting that it is reliable for answering the sub-

each applied to a random sample of apps from the 1,112

RQ4 (Statistical significance and effect size): How

does Sapienz perform, compare to the state-of-the-art and

the state-of-practice, on randomly selected apps, with infer-

ential statistical testing?

Finally, we want to investigate the usefulness of the

Sapienz technique on real-world commercial apps. There-

fore, we follow the practice adopted by some previous au-

thors [37, 52] of applying the technique to a large number

of popular apps in Google Play. This avoids the potential

bias of applying the technique only to apps chosen from F-

Droid, which does not contain any of the most popular apps

in current use. Since we do not have access to the source

code of these popular commercial apps, it also tests the ef-

fectiveness of the technique when used in ‘black box mode’,

where it has least available information to guide the test

generation process, and only high level, non-invasive, ‘skin

coverage’ instrumentation is possible.

RQ5 (Usefulness): Can Sapienz find any real bugs on

popular closed-source real-world apps?

| 4. | EVALUATION | F-Droid apps publicly available: |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sequent (novel) questions. | A natural question to ask for | 4.1 | Experimental Setup |  |  |  |  |
| RQ1, once we have established replication of Choudhary | We conduct three studies to answer the above research |  |  |  |  |  |  |
| et al. | in RQ0, is one that is asked by many other stud- | questions: | Study 1 addresses RQ0 to RQ3, Study 2 ad- |  |  |  |  |
| ies [20, 27, 51, 52, 53, 54, 61]: | ‘what coverage is achieved by | dresses RQ4 and Study 3 addresses RQ5. Study 1 and Study |  |  |  |  |  |
| the newly proposed technique?’ | 2 are based on the execution of the testing approaches under |  |  |  |  |  |  |
| RQ1 (Code coverage): | How does the coverage achieved | evaluation on a single PC. Study 3 augments this, by using |  |  |  |  |  |
| by | Sapienz | compare to the state-of-the-art and the state- | real-world physical (Samsung and Google) devices to demon- |  |  |  |  |
| of-practice? | strate the practicality of | Sapienz | . For all these studies, we |  |  |  |  |
| Coverage is one useful indicator, simply because failure to | evaluate on Android KitKat version (API 19) because it is |  |  |  |  |  |  |
| achieve coverage leaves aspects of the app untested. | Nev- | the most widely-used version [1] at the time of writing. All |  |  |  |  |  |
| ertheless, there is evidence that coverage alone, cannot be | techniques under evaluation are fully automated. We choose |  |  |  |  |  |  |
| relied upon to indicate test effectiveness [57]. | Therefore, | not to provide manual assistance (e.g., logins) in testing the |  |  |  |  |  |
| our second question focuses on fault detection; regardless | subjects, because we aim for an unbiased and rigorous as- |  |  |  |  |  |  |
| of coverage achieved, the effectiveness of any software test- | sessment of what can be achieved entirely automatically. |  |  |  |  |  |  |
| ing technique should also be assessed by its ability to reveal | Since Dynodroid itself manipulates the emulator and de- |  |  |  |  |  |  |
| faults. | pends on its own customised Android system image, we fol- |  |  |  |  |  |  |
| RQ2 (Fault revelation): | How do the faults found by | low its user guide [4] and use its own image file to execute the |  |  |  |  |  |
| Sapienz | compare to those found by the state-of-the-art and | tool. For all the approaches under evaluation, we limit only |  |  |  |  |  |
| the state-of-practice? | the execution time and the assigned hardware resource, so |  |  |  |  |  |  |
| Sapienz | targets coverage, fault revelation and length of | that our comparison is direct head-to-head test effectiveness |  |  |  |  |  |
| fault-revealing | test | cases. | Longer | test | sequences | might | achieved in a certain amount of elapsed wall-clock time. This |

---

## Page 7

setting is consistent with the benchmark study conducted by

Choudhary et al. [28], which allows us to perform a direct

the  A ˆ 12 effect size exceeds 0.56, 0.64, and 0.71, respectively.

We repeat each experiment 20 times to provide a sample

statistical evaluation requires 25 days of execution time.

Since Study 3 concerns the evaluation of Sapienz on 1,000

apps, it is inherently time-consuming. Fortunately, since we

are interested in the usefulness of the technique, we want

to investigate whether it can find faults quickly. Therefore,

we restrict the wall-clock execution time for this study to 30

minutes per app per setting. Furthermore, since emulators

may not reflect real device behaviour perfectly, we conduct

this study under three device settings: on a PC with emu-

lators, on a smart mobile device ( Samsung Note II ) and on

a small cluster of 10 tablets ( Google Nexus 7 ). The entire

computation time of the experiment, on all 1,000 apps un-

der three settings, to answer RQ5 is 1,050 hours (nearly 44

days); 500 hours on emulators, 500 hours on the Samsung

Note II and 500/10 hours on the Google Nexus 7 tablets.

In this study, we use only the non-invasive ‘skin coverage’

to guide Sapienz , so the results are a lower bound on the

performance that would be observed by a developer, who

could have access to source code and could therefore exploit

the finer granularity levels of coverage.

Table 2: Results on the 68 benchmark apps.

| Subject | Coverage | #Crashes | Length |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a2dp | 43 | 29 | 46 | 0 | 1 | 3 | - | 315 | 148 |
| aLogCat | 68 | 49 | 71 | 0 | 0 | 2 | - | - | 114 |
| AnyCut | 63 | 65 | 66 | 0 | 0 | 1 | - | - | 103 |
| Book-Catalogue | 46 | 27 | 33 | 1 | 0 | 1 | 1941 | - | 177 |
| battery | 76 | 68 | 79 | 0 | 0 | 4 | - | - | 198 |
| alarmclock | 72 | 51 | 77 | 4 | 1 | 5 | 1716 | 170 | 144 |
| mileage | 40 | 25 | 54 | 2 | 1 | 4 | 878 | 390 | 153 |
| hndroid | 4 | 6 | 10 | 2 | 1 | 2 | 206 | - | 117 |
| worldclock | 93 | 94 | 94 | 0 | 0 | 1 | - | - | 98 |
| jamendo | 62 | 3 | 72 | 0 | 0 | 2 | - | - | 191 |
| yahtzee | 62 | 51 | 58 | 2 | 0 | 0 | 31767 | - | - |
| CountdownTimer | 60 | 62 | 62 | 0 | 0 | 0 | - | - | - |
| dalvik-explorer | 69 | * | 73 | 2 | * | 4 | 3720 | * | 165 |
| dialer2 | 38 | 55 | 42 | 0 | 0 | 0 | - | - | - |
| gestures | 36 | 48 | 52 | 0 | 0 | 0 | - | - | - |
| adsdroid | 23 | 36 | 38 | 2 | 1 | 1 | 356 | 48 | 128 |
| lockpatterngenerator | 78 | 79 | 81 | 0 | 0 | 0 | - | - | - |
| aGrep | * | 38 | * | * | 0 | * | * | - | * |
| MunchLife | 70 | 73 | 76 | 0 | 0 | 0 | - | - | - |
| LNM | 58 | 66 | 60 | 1 | 0 | 1 | 51621 | - | 48 |
| bomber | 76 | 70 | 73 | 0 | 0 | 0 | - | - | - |
| fantastischmemo | 36 | 9 | 60 | 1 | 0 | 6 | 25375 | - | 156 |
| zooborns | 35 | 38 | 36 | 0 | 0 | 0 | - | - | - |
| wikipedia | 36 | 32 | 32 | 0 | 0 | 5 | - | - | 232 |
| Photostream | 16 | 23 | 38 | 1 | 1 | 2 | 317 | 29 | 125 |
| RandomMusicPlayer | 58 | 82 | 59 | 0 | 0 | 0 | - | - | - |
| soundboard | 42 | 60 | 53 | 0 | 0 | 0 | - | - | - |
| SpriteText | 59 | 57 | 62 | 0 | 0 | 0 | - | - | - |
| tippy | 83 | 48 | 83 | 0 | 0 | 0 | - | - | - |
| Triangle | 76 | 69 | 79 | 0 | 0 | 0 | - | - | - |
| whohasmystuff | 74 | * | 80 | 0 | * | 0 | - | * | - |

According to the thorough empirical study by Choudhary

et al. [28], existing techniques fail to outperform the stan-

dard Monkey Android testing tool in ‘continuous mode’. In

this mode, each testing tool is given one hour execution

time and the same hardware configuration. We therefore

chose to evaluate in the same way, comparing against Mon-

key and Dynodroid, which Choudhary et al. found to per-

form best among the research prototype techniques (beating

recently proposed techniques including black box based An-

droidRipper [15], A 3 E [20], PUMA [37] and white-box based

ACTEve [16]). Monkey and Dynodroid also performed

best in a slightly more recent study [57], and, therefore, if

Sapienz outperforms both Monkey and Dynodroid, we will

also have reasonable evidence to conclude that it is likely

to outperform AndroidRipper [15], A 3 E [20], PUMA [37]

and ACTEve [16]. Note that Sapienz also yields a Pareto

front at the end of its execution, which might be a useful

by-product. However, we choose to evaluate Sapienz only

in the ‘continuous mode’, for a fair comparison with Monkey

and Dynodroid, which do not yield Pareto fronts.

| comparison with the results in that previous study. | M | D | S | M | D | S | M | D | S |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| We set | Sapienz | ’s crossover and mutation probability to | aarddict | 14 | 46 | 18 | 0 | 0 | 0 | - | - | - |  |
| 0.7 and 0.3 respectively. | The maximum generation is set | Amazed | 66 | 63 | 69 | 1 | 0 | 1 | 1429 | - | 96 |  |  |
| to 100 with the population size of 50 and each individual | baterrydog | 64 | 66 | 67 | 0 | 1 | 1 | - | 81 | 173 |  |  |  |
| contains 5 test cases. | None of the parameters available to | swiftp | 13 | 13 | 14 | 0 | 0 | 0 | - | - | - |  |  |
| Sapienz | are tuned; all remain set at the same value through- | bites | 38 | 25 | 41 | 1 | 0 | 1 | 19124 | - | 116 |  |  |
| out all our experiments. | We adopt this approach in order | addi | 16 | 26 | 20 | 2 | 1 | 2 | 1367 | 315 | 129 |  |  |
| to ensure that the comparison is strictly fair; results for | manpages | 64 | 68 | 75 | 0 | 0 | 3 | - | - | 120 |  |  |  |
| Sapienz | might be improved by tuning, but this might also | autoanswer | 13 | 24 | 16 | 0 | 0 | 0 | - | - | - |  |  |
| introduce bias and unfairness in the experimentation. | We | multismssender | 43 | 49 | 61 | 0 | 0 | 0 | - | - | - |  |  |
| conducted Study 1 and Study 2 on a PC with a single hexa- | Nectroid | 69 | 46 | 76 | 1 | 0 | 2 | 416 | - | 118 |  |  |  |
| core 3.50GHz CPU and 16GB RAM on Ubuntu 14.04. For | acal | 15 | 15 | 29 | 1 | 0 | 5 | 62717 | - | 177 |  |  |  |
| Study 3, we also use a mobile device | Samsung Galaxy Note | aka | 79 | 76 | 84 | 1 | 0 | 7 | 42804 | - | 136 |  |  |
| II | and a cluster of 10 | Google Nexus 7 | (2013 version) tablets. | aagtl | 30 | 29 | 31 | 4 | 0 | 5 | 1756 | - | 188 |
| For Study 1, we test each subject for one hour by us- | sanity | 32 | 1 | 19 | 2 | 1 | 2 | 8377 | 12 | 90 |  |  |  |
| ing each tools under evaluation. | We record their achieved | Mirrored | 69 | 68 | 64 | 0 | 0 | 1 | - | - | 147 |  |  |
| coverage every 5 minutes. When comparing fault-revealing | DivideAndConquer | 85 | 72 | 83 | 0 | 0 | 2 | - | - | 186 |  |  |  |
| test sequence lengths, we need to be careful to normalise | fileexplorer | 40 | 56 | 50 | 0 | 0 | 0 | - | - | - |  |  |  |
| the results: | each technique might find a different number | hotdeath | 78 | 3 | 79 | 1 | 0 | 3 | 63975 | - | 152 |  |  |
| of faults, so measuring the total length of fault-revealing | myLock | 28 | 33 | 31 | 0 | 0 | 0 | - | - | - |  |  |  |
| test sequences would be unfair. | Rather, we compare the | mnv | 49 | * | 67 | 2 | * | 4 | 30381 | * | 150 |  |  |
| mean length of the fault-revealing test sequences returned by | k9mail | 7 | 5 | 7 | 0 | 0 | 1 | - | - | 238 |  |  |  |
| each approach. We count an atomic event as one event and | LolcatBuilder | 24 | 23 | 31 | 0 | 0 | 0 | - | - | - |  |  |  |
| decompose our high-level | motif genes | into multiple atomic | MyExpenses | 51 | 25 | 65 | 0 | 1 | 2 | - | 67 | 150 |  |
| events for a fair comparison. | netcounter | 44 | 63 | 77 | 0 | 0 | 2 | - | - | 156 |  |  |  |
| For Study 2, we use random selection to identify 10 sub- | frozenbubble | * | 63 | * | * | 0 | * | * | - | * |  |  |  |
| jects from the 1,112 apps in the overall F-Droid set. | We | blokish | 50 | 50 | 52 | 1 | 1 | 2 | 2512 | 252 | 194 |  |  |
| conduct an inferential statistical analysis of the performance | importcontacts | 41 | 43 | 42 | 0 | 0 | 0 | - | - | - |  |  |  |
| of each of the Android testing techniques applied to these | PasswordMaker | 63 | 53 | 64 | 3 | 0 | 1 | 3406 | - | 180 |  |  |  |
| randomly selected apps. Details of the 10 randomly selected | passwordmanager | 11 | 7 | 16 | 0 | 0 | 0 | - | - | - |  |  |  |
| apps can be found in the left-hand columns of Table 5. Since | QuickSettings | 50 | 33 | 50 | 0 | 0 | 1 | - | - | 134 |  |  |  |
| we cannot rely on Gaussian (aka ‘Normal’) distribution of | Ringdroid | 26 | * | 29 | 1 | * | 2 | 550 | * | 161 |  |  |  |
| test results, we use a non-parametric multiple comparison | SpriteMethodTest | 82 | 37 | 83 | 0 | 0 | 0 | - | - | - |  |  |  |
| inferential statistical significance test, | the Kruskal-Wallis | SyncMyPix | 21 | 20 | 22 | 0 | 0 | 4 | - | - | 187 |  |  |
| test [24] (at the 0.05 alpha level) with the Bonferroni cor- | tomdroid | 55 | 43 | 58 | 0 | 1 | 1 | - | 165 | 91 |  |  |  |
| rection, and the Vargha-Delaney effect size measure [59], as | Translate | 48 | 45 | 49 | 0 | 0 | 0 | - | - | - |  |  |  |
| widely recommended [18, 40]. | The differences between ap- | weight-chart | 58 | 57 | 77 | 2 | 1 | 4 | 10588 | 236 | 186 |  |  |
| proaches are characterised as small, medium and large when | Wordpress | 4 | * | 7 | 0 | * | 1 | - | * | 137 |  |  |  |
| of runs for statistical analysis. In total, this more rigorous | 4.2 | State of the Art and Practice |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 8

Figure 6: Pairwise comparison on found crashes.

| Figure 4: Progressive coverage on benchmark apps. | Table 3: Statistics on found crashes. |  |  |
| --- | --- | --- | --- |
| App Crashes | Monkey | Dynodroid | Sapienz |
| # App Crashed | 24 | 13 | 41 |
| # Unique Crashes | 41 | 13 | 104 |
| # Total Crashes | 1,196 | 125 | 6,866 |

Dynodroid from the 10 th minute onwards, finally achiev-

ing the highest overall statement coverage at the end of the

hour’s experimental time allowed for each of the 68 subjects.

To further investigate these results, Figure 5 presents the

boxplots (for which a circle indicates the mean) of the final

coverage results for apps grouped by size-of-app. This analy-

Figure 5: Code coverage on the 68 benchmark apps. sis reveals that Sapienz achieved the highest mean coverage

across all four app size groups. We conclude that there is

evidence from the 68 benchmark apps that Sapienz can at-

4.3 Results

tain and maintain superior coverage after approximately 10

minutes of execution on a standard equipment.

4.3.1 Study 1: Benchmark Subjects

RQ2 (Fault revelation). In answering RQ2, we re-

| The detailed experimental results on each subject for | port not only on the number of crashes found by each tech- |  |  |  |
| --- | --- | --- | --- | --- |
| Study 1 are given in Table 2, | where ‘Coverage’ reports | nique, but also the overlap between the crashes found by |  |  |
| statement coverage achieved by each of the three tools, | each technique. | This allows us to investigate whether the |  |  |
| ‘#Crashes’ indicates the number of unique crashes detected | techniques are complementary, or whether one subsumes an- |  |  |  |
| by each and ‘Length’ reports the fault-revealing test se- | other, as well as reporting on the overall effectiveness (in |  |  |  |
| quence length for each. The column headings ‘M’, ‘D’ and | terms of number of crashes found). Of course a crash may |  |  |  |
| ‘S’ refer to the three tools we compare; Monkey, Dynodroid | be triggered by different test sequences, so we report | unique |  |  |
| and | Sapienz | . The entry ‘*’ indicates the tool cannot start | crashes, considering a crash to be unique when its stack trace |  |
| the corresponding app, while the entry ‘-’ indicates that the | differs from all others. We excluded those crashes caused by |  |  |  |
| fault-revealing length is undefined, because no faults were | the Android system or the test harness itself, which were not |  |  |  |
| found. | caused by the faults from the subjects. Such crashes can be |  |  |  |
| RQ0 (Experimental replication). | We first evaluate | identified by checking the corresponding stack traces. A re- |  |  |
| Monkey and Dynodroid to check that our experiment in- | cent study [57] has highlighted this issue and pointed out |  |  |  |
| frastructure replicates the results reported by Choudhary et | that these crashes are, essentially false positives, so should |  |  |  |
| al. [28]. We calculated progressive average coverages across | not be counted. |  |  |  |
| all 68 subjects every 5 minutes for each of the three tech- | As shown in Table 3, | Sapienz | revealed the largest num- |  |
| niques and report the direct comparison on the final cov- | ber of both unique and total crashes in 41 of the 68 apps. |  |  |  |
| erages achieved. The progressive coverages of Monkey and | Sapienz | also found 30 unique crashes in 14 apps for which |  |  |
| Dynodroid are shown in Figure 4. The shape of the growth | neither Monkey nor Dynodroid found any crashes. We also |  |  |  |
| in coverage over time very closely resembles the results re- | provide a pairwise comparison of the unique crashes found |  |  |  |
| ported by Choudhary et al. [28]. However, the final coverage | in Figure 6 (where the black bars show common crashes; |  |  |  |
| values achieved by these two tools are slightly higher than | those revealed by both techniques): Across the 68 subjects, |  |  |  |
| those reported by Choudhary et al. This may be caused by | Sapienz | found 72 and 99 unique crashes, undetected by |  |  |
| the hardware setting: Choudhary et al. ran the experiments | Monkey and Dynodroid respectively, while it missed only 9 |  |  |  |
| on virtual machines while we conducted our experiments | crashes found by Monkey and 8 by Dynodroid. We conclude |  |  |  |
| on a physical PC which may be faster. | Since the overall | that there is strong evidence from the 68 benchmark apps |  |  |
| growth trend closely resembles the results of Choudhary et | that | Sapienz | outperforms both Monkey and Dynodroid in |  |
| al., and given that better performance only raises the bar | terms of fault revelation, as measured by the number of |  |  |  |
| that | Sapienz | must clear in order to outperform them, we | crashes found. |  |
| believe these results indicate we have a firm foundation on | RQ3 | (Sequence | length). | Table 4 shows the mean |
| which to perform our subsequent experiments. | length of fault-revealing test sequences of the three tools, |  |  |  |
| RQ1 (Code coverage). | We used an identical evalua- | grouped by various subject size ranges (where the group sizes |  |  |
| tion approach for | Sapienz | as that used in the replication | are given in the brackets). On all subject groups except ‘3K- |  |
| study reported in RQ0 for Monkey and Dynodroid. As can | 30K’, | Sapienz | generated the shortest fault-revealing test se- |  |
| be seen from Figure 4, | Sapienz | outperformed Monkey and | quences. On the ‘3K-30K’ subject group, Dynodroid gener- |  |

---

## Page 9

Table 4: Fault-revealing test sequence length.

Monkey Dynodroid Sapienz

| < | 3K (31) | 13,843 | 186 | 132 |
| --- | --- | --- | --- | --- |
| Size | 3K-30K (30) | 14,775 | 77 | 153 |
| > | 30K ( 7) | 21,501 | 276 | 169 |
| Overall (68) | 15,305 | 161 | 149 |  |

ated the shortest fault-revealing test sequences (although its

code coverage and number of found crashes are lower than

Sapienz ). We conclude that there is strong evidence from

the 68 benchmark apps that Sapienz outperforms the fault-

revealing test sequence length of Monkey, and that on larger

subjects it also outperforms Dynodroid.

4.3.2 Study 2: Inferential Statistical Analysis

RQ4 (Statistical significance and effect size). For

all 10 randomly sampled F-Droid programs, and for all three

criteria of interest, Sapienz outperformed both Monkey and

Dynodroid. However, in this study, we are concerned with

the statistical significance in effect size of these results. We

first present the boxplots of the performance comparison on

10 F-Droid subjects, as shown in Figure 7.

Table 5 shows Vargha-Delaney A ˆ 12 effect size for the

three objectives, coverage, the number of crashes found and

fault-revealing sequence length. For each objective, the

columns contain the effect size comparisons for Sapienz -

Monkey (S-M), Sapienz -Dynodroid (S-D), and, for com- Figure 7: Performance comparison on 10 F-Droid

pleteness, Monkey-Dynodroid (M-D), where the result is subjects. (Boxplots grouped by subject.)

significant. As shown in the table, Sapienz significantly

| outperforms Monkey with large effect size on 7/10 subjects | one might in an open-source environment, but we were able |  |  |  |
| --- | --- | --- | --- | --- |
| for coverage, 8/10 for crashes, and 10/10 for length (with | to contact only the associated customer support team. We |  |  |  |
| large effect size). | Sapienz | significantly outperforms Dyn- | got 58 replies in total, excluding those that were automatic |  |
| odroid, with large effect size on 9/10 subjects for coverage, | generated. For such a ‘cold call’ outreach activity, 58 from |  |  |  |
| 9/10 for crashes and 10/10 for length. | We also replicated | 175 emails is relatively high [35, 47]. |  |  |
| the finding of Choudhary et al. [28] that Monkey tends to | Of these 58 replies, in 27 cases we got feedback from the |  |  |  |
| outperform Dynodroid, but further note that it does so less | app developers (after our email was redirected by their cus- |  |  |  |
| conclusively than | Sapienz | does. The overall results suggest | tomer support teams). | Furthermore, 14 developer teams |
| that | Sapienz | outperforms both the state-of-the-art and the | confirmed that the crashes resulted from real faults in their |  |
| state-of-practice approaches on all three objectives. | apps, and 6 of them have already fixed the reported crashes. |  |  |  |

Among the 13 unconfirmed crashes out of 27 developer

| 4.3.3 | Study 3: Top 1,000 Popular Apps | replies, 6 indicated that our reports were helpful or that the |  |  |  |
| --- | --- | --- | --- | --- | --- |
| RQ5 (Usefulness). | In total, | Sapienz | found 558 unique | developers were working on the issue. | A further 6 respon- |
| crashes in 329 of the 1,000 Google Play apps to which it | dents seek additional information. One of the 13 responded |  |  |  |  |
| was applied. In the previous study of Dynodroid [52], it also | that they could not identify the cause of the crash. |  |  |  |  |
| tested top 1,000 apps, however the budget used and total | We list the anonymised details | 4 | of these 14 faults con- |  |  |
| number of found unique crashes are not mentioned. | The | firmed by developers in Table 6: These 14 apps vary greatly |  |  |  |
| authors found 6 bugs (that led to non-native crashes) in 5 | in categories and install numbers, with at least 148 mil- |  |  |  |  |
| out of 1,000 apps tested. Our found 558 unique crashes were | lion installs in total. | The 6 confirmed faults, with further |  |  |  |
| caused by 22 types of errors/exceptions. | The distribution | fixes from their developers are labelled as ‘Confirmed’ in |  |  |  |
| of the most common crash types (those with more than 4 | the ‘Fixed’ column. | For the remaining 8 apps, we found |  |  |  |
| crashes each) is shown in Figure 8, revealing that most were | that 7 of the confirmed crashes can no longer be observed |  |  |  |  |
| caused by ‘native’ crashes, indicating that the crash occurred | when testing their most recent versions. However since we |  |  |  |  |
| outside the Android Java Virtual Machine, while executing | have not received confirmation from developers that these |  |  |  |  |
| the app’s native code. | Another common class of crashes | faults are definitely fixed, we label them as ‘Unconfirmed’ in |  |  |  |
| found were those due to null pointers. | the ‘Fixed’ column. We observed only one of the confirmed |  |  |  |  |
| We reported the non-native crashes to the app provider, | faults was not fixed (still crashes). |  |  |  |  |

giving a stack trace for each crash type. In total, we reported

| 175 crashes | 3 | . Unfortunately, since these apps are commer- | 4.4 | Threats to Validity |
| --- | --- | --- | --- | --- |
| cial apps, we do not have direct access to the developers, as | Like any empirical study, there are potential threats to |  |  |  |
| 3 | For each app, we reported the first found crash that cor- | validity of our experimental results: |  |  |
| responds to each non-native crash type. We did not report | Internal validity | : | Threats to internal validity concern |  |

native crashes because their stack traces do not explicitly

point to the source lines of the potential faults. 4 App versions are omitted for anonymity.

---

## Page 10

Table 5: Vargha-Delaney effect size (‘-’ indicates a statistically insignificant result).

Subject Description Ver. Date SLOC Coverage #Crash Length

S-M S-D M-D S-M S-D M-D S-M S-D M-D

| Arity | Scientific calculator | 1.27 | 2012-02-11 | 2,821 | - | 1.00 | 1.00 | - | 1.00 | 0.98 | 1.00 | 1.00 | - |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BabyCare | Timer for when to feed baby | 1.5 | 2012-08-23 | 8,561 | 1.00 | 1.00 | - | 0.84 | 0.92 | - | 1.00 | 1.00 | - |
| BookWorm | Book collection manager | 1.0.18 | 2011-05-04 | 7,589 | 0.96 | 1.00 | - | 0.97 | 1.00 | - | 1.00 | 0.95 | - |
| DroidSat | Satellite viewer | 2.52 | 2015-01-11 | 15,149 | - | - | - | 1.00 | 1.00 | - | 0.90 | 0.90 | - |
| FillUp | Calculate fuel mileage | 1.7.2 | 2015-03-10 | 10,400 | - | 1.00 | 1.00 | 0.73 | 0.73 | - | 0.95 | 0.80 | 0.23 |
| Hydrate | Set targets for water intake | 1.5 | 2013-12-09 | 2,728 | 0.85 | 1.00 | 0.92 | 0.95 | - | 0.23 | 0.73 | 0.73 | - |
| JustSit | Meditation timer | 0.3.3 | 2012-07-26 | 728 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | 1.00 | 1.00 | 1.00 |
| Kanji | Character recognition | 1.0 | 2012-10-30 | 200,154 | 1.00 | 1.00 | 0.84 | - | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 |
| L9Droid | Interactive fiction | 0.6 | 2015-01-06 | 18,040 | 1.00 | 1.00 | 0.99 | 0.89 | 0.90 | - | 0.94 | 0.91 | - |
| Maniana | User-friendly todo list | 1.26 | 2013-06-28 | 20,263 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - |

Table 6: Confirmed app faults identified by Sapienz.

| App | Category | Installs | Caused By | Device | Description | Fixed |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P* | Photography | 10M-50M | NullPointer | Nexus 7 | Unable to start activity from a customer support SDK. | Unconfirmed |  |  |  |
| K* | Simulation | 10M-50M | NullPointer | Nexus 7 | Concurrent error while executing | doInBackground() | Unconfirmed |  |  |
| B* | Business | 10K-50K | NullPointer | Nexus 7 | Null object reference in a third party SDK | No |  |  |  |
| D* | Education | 500K-1M | NullPointer | Emulator | Exception from event handler | onOptionsItemSelected() | Confirmed |  |  |
| T* | Simulation | 10K-50K | NullPointer | Emulator | Exception from | onAnimationEnd() | in | FlipGameActivity | Confirmed |
| T* | Lifestyle | 500K-1M | NullPointer | Emulator | Error when | CameraUpdateFactory | is not initialized | Confirmed |  |
| T* | Transport | 1M-5M | NullPointer | Emulator | Exception from | onClick() | in | StationInfoFragment | Confirmed |
| S* | Education | 1M-5M | NullPointer | Emulator | Unable to start a third party activity | Unconfirmed |  |  |  |
| T* | Weather | 10M-50M | NullPointer | Emulator | Error when | CameraUpdateFactory | is not initialized | Unconfirmed |  |
| W* | Weather | 10K-50K | OutOfMemory | Note II | Error inflating class on binary XML file | Unconfirmed |  |  |  |
| S* | Puzzle | 5M-10M | ActivityNotFound | Note II | No Activity found to handle | SHARE_GOOGLE | Intent. | Unconfirmed |  |
| F* | Photography | 10M-50M | NullPointer | Note II | Exception from | onGlobalLayout() | in | ViewUtil | Confirmed |
| T* | Music&Audio | 100M-500M | NullPointer | Note II | Unable to start the activity of | PlayerActivity | Unconfirmed |  |  |
| P* | Music&Audio | 5K-10K | ActivityNotFound | Note II | No Activity found to handle a | View | Intent | Confirmed |  |

it promising that the technique applies, out of the box, to so

many different apps, none of which have been ‘cherry picked’

(nor in any other way ‘chosen’ by the experimenters them-

selves). It is possible, of course, that the 1,000 most popular

apps, and the F-Droid open-source apps, have peculiar char-

acteristics not shared by other classes of apps, for which the

performance of the three techniques we studied in this paper

may differ. We also only evaluated our approach on a single

version of the Android platform. Although the most widely-

used version, the rapid evolution of the Android system,

Figure 8: Main crash types on Google Play subjects. means that the performance of three evaluated techniques

may vary as subsequent versions become available.

factors in our experimental methodology that may affect our

5. CONCLUSIONS

results. For Study 1, 50 of the 68 ASE benchmark subjects

| originate in a single article [52], which might have resulted | This paper has introduced a novel multi-objective search- |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| in selection bias. To mitigate this issue, we conducted Study | based software testing technique and tool | Sapienz | for auto- |  |  |  |
| 2 on 10 open-source apps, selected using unbiased random | mated Android app testing. | Sapienz | supports multi-level |  |  |  |
| sampling. | Regarding the particular | Sapienz | implementa- | instrumentation and remains applicable, even when only |  |  |
| tion, we implemented only a single motif pattern to exercise | app’s APK file (and nothing else) is available. Its evolution- |  |  |  |  |  |
| all text fields and clickable UI widgets under the correspond- | ary algorithm continuously optimises for coverage, sequence |  |  |  |  |  |
| ing view, which is applicable to all apps. | Performance of | length and the number of crashes found, seeking to reveal |  |  |  |  |
| Sapienz | may improve when considering different motif pat- | as many crashes as possible, while minimising the length of |  |  |  |  |
| terns, but could not be worse, since this single option will | test sequences. |  |  |  |  |  |
| always be available. | Also, the choice of parameter setting | Our evaluation results on open-source apps have shown |  |  |  |  |
| for each of the three tools may affect their performance sig- | that | Sapienz | outperforms | the | state-of-the-art | technique |
| nificantly. | To reduce this threat, we followed the default | Dynodroid and the widely-used tool, Android Monkey, on all |  |  |  |  |
| configurations for Monkey and Dynodroid, as used in the | three objectives for almost all subjects. The only exception |  |  |  |  |  |
| previous thorough benchmark assessment study Choudhary | is the relatively small (3K-30K lines of code) F-Droid open- |  |  |  |  |  |
| et al. [28] and we resisted any temptation to tune | Sapienz | . | source apps in the benchmark suite, for which Dynodroid |  |  |  |
| External | validity | : | Threats to external validity arise | produced shorter fault-revealing test sequences, although it |  |  |
| when the experimental results cannot be generalised. | Like | achieved less coverage and revealed fewer crashes. |  |  |  |  |
| all empirical studies, we are limited in the number of sub- | We also believe that | Sapienz | is a practical and useful |  |  |  |
| ject systems to which we can apply our tools and techniques. | testing tool, since it was able to find 558 unique crashes in |  |  |  |  |  |
| Our results will not necessarily generalise beyond the 1,078 | the top 1,000 most popular Android apps, 14 of which have |  |  |  |  |  |
| apps to which we have applied | Sapienz | . However, we think | already been confirmed as caused by real faults. |  |  |  |

---

## Page 11

6. REFERENCES [23] M. Bozkurt and M. Harman. Automatically

[1] Android dashboards. http://developer.android.com/

about/dashboards/index.html.

[2] Android fragmentation visualized. http://opensignal.

com/reports/2015/08/android-fragmentation.

[3] Appium: Automation for iOS and Android apps.

http://appium.io.

[4] Dynodroid user guide.

http://code.google.com/p/dyno-droid.

[5] ELLA: A tool for binary instrumentation of Android

apps. http://github.com/saswatanand/ella.

http://emma.sourceforge.net.

[9] Number of Android applications. http:

Proc. of ASE’12 , pages 258–261, 2012.

Proc. of ESEC/FSE’12 , pages 59:1–59:11, 2012.

Engineering , 38(3):497–519, May 2012.

pages 153–162, 2010.

41(5):507–525, May 2015.

generating realistic test input from web services. In

Proc. of SOSE’11 , pages 13–24, 2011.

[24] N. Breslow. A generalized Kruskal-Wallis test for

comparing K samples subject to unequal patterns of

censorship. Biometrika , 57(3):579–594, 1970.

[25] E. Cant´ u-Paz and D. E. Goldberg. Efficient parallel

genetic algorithms: theory and practice. Computer

Methods in Applied Mechanics and Engineering ,

186(2–4):221–238, 2000.

[26] S. Carino and J. H. Andrews. Dynamically testing

GUIs using ant colony optimization. In Proc. of

[27] W. Choi, G. Necula, and K. Sen. Guided GUI testing

623–640, 2013.

39(2):276–291, 2013.

147–158, 2010.

[36] Google. Android Monkey.

pages 342–357, 2007.

| [6] EMMA: A free Java code coverage tool. | ASE’15 | , pages 138–148, 2015. |  |  |  |
| --- | --- | --- | --- | --- | --- |
| [7] F-Droid. http://f-droid.org. | of Android apps with minimal restart and |  |  |  |  |
| [8] Modisco. http://www.eclipse.org/modisco. | approximate learning. In | Proc. of OOPSLA’13 | , pages |  |  |
| //www.appbrain.com/stats/number-of-android-apps. | [28] S. R. Choudhary, A. Gorla, and A. Orso. Automated |  |  |  |  |
| [10] Robotium: User scenario testing for Android. | test input generation for Android: Are we there yet? |  |  |  |  |
| https://github.com/RobotiumTech/robotium. | In | Proc. of ASE’15 | , pages 429–440, 2015. |  |  |
| [11] A. Abran, J. W. Moore, et al. Guide to the software | [29] com | Score | . The global mobile report. |  |  |
| engineering body of knowledge (SWEBOK | © | R | ). In | 2004 | http://comscore.com/Insights/ |
| Version, IEEE CS Professional Practices Committee | , | Presentations-and-Whitepapers/2015/ |  |  |  |
| 2004. | The-Global-Mobile-Report, 2015. |  |  |  |  |
| [12] C. Q. Adamsen, G. Mezzetti, and A. Møller. | [30] K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan. A |  |  |  |  |
| Systematic execution of Android test suites in adverse | fast and elitist multiobjective genetic algorithm: |  |  |  |  |
| conditions. In | Proc. of ISSTA’15 | , pages 83–93, 2015. | NSGA-II. | IEEE Transactions on Evolutionary |  |
| [13] N. Alshahwan and M. Harman. Automated Web | Computation | , 6(2):182–197, 2002. |  |  |  |
| application testing using search based software | [31] F.-A. Fortin, F.-M. De Rainville, M.-A. Gardner, |  |  |  |  |
| engineering. In | Proc. of ASE’11 | , pages 3–12, 2011. | M. Parizeau, and C. Gagn´ | e. DEAP: Evolutionary |  |
| [14] D. Amalfitano, A. Fasolino, P. Tramontana, B. Ta, | algorithms made easy. | Journal of Machine Learning |  |  |  |
| and A. Memon. MobiGUITAR: Automated | Research | , 13:2171–2175, July 2012. |  |  |  |
| model-based testing of mobile apps. | IEEE Software | , | [32] G. Fraser and A. Arcuri. The seed is strong: Seeding |  |  |
| 32(5):53–59, 2015. | strategies in search-based software testing. In | Proc. of |  |  |  |
| [15] D. Amalfitano, A. R. Fasolino, P. Tramontana, | ICTS’12 | , pages 121–130, 2012. |  |  |  |
| S. De Carmine, and A. M. Memon. Using GUI ripping | [33] G. Fraser and A. Arcuri. Whole test suite generation. |  |  |  |  |
| for automated testing of Android applications. In | IEEE Transactions on Software Engineering | , |  |  |  |
| [16] S. Anand, M. Naik, M. J. Harrold, and H. Yang. | [34] G. Fraser and A. Zeller. Mutation-driven generation of |  |  |  |  |
| Automated concolic testing of smartphone apps. In | unit tests and oracles. In | Proc. of ISSTA’10 | , pages |  |  |
| [17] A. Arcuri. A theoretical and empirical analysis of the | [35] M. T. Frohlich. Techniques for improving response |  |  |  |  |
| role of test sequence length in software testing for | rates in OM survey research. | Journal of Operations |  |  |  |
| structural coverage. | IEEE Transactions on Software | Management | , 20(1):53–62, 2002. |  |  |
| [18] A. Arcuri and L. Briand. A practical guide for using | http://developer.android.com/tools/help/monkey.html. |  |  |  |  |
| statistical tests to assess randomized algorithms in | [37] S. Hao, B. Liu, S. Nath, W. G. Halfond, and |  |  |  |  |
| software engineering. In | Proc. of ICSE’11 | , pages 1–10, | R. Govindan. PUMA: Programmable UI-automation |  |  |
| 2011. | for large-scale dynamic analysis of mobile apps. In |  |  |  |  |
| [19] F. Asadi, G. Antoniol, and Y. Gu´ | eh´ | eneuc. Concept | Proc. of MobiSys’14 | , pages 204–217, 2014. |  |
| location with genetic algorithms: A comparison of | [38] M. Harman. The current state and future of search |  |  |  |  |
| four distributed architectures. In | Proc. of SSBSE’10 | , | based software engineering. In | Proc. of FOSE’07 | , |
| [20] T. Azim and I. Neamtiu. Targeted and depth-first | [39] M. Harman, A. Mansouri, and Y. Zhang. Search based |  |  |  |  |
| exploration for systematic testing of Android apps. In | software engineering: Trends, techniques and |  |  |  |  |
| Proc. of OOPSLA’13 | , pages 641–660, 2013. | applications. | ACM Computing Surveys | , |  |
| [21] J. Bach. Exploratory testing. In | The Testing | 45(1):11:1–11:61, November 2012. |  |  |  |
| Practitioner | , pages 253–265, 2004. | [40] M. Harman, P. McMinn, J. Souza, and S. Yoo. Search |  |  |  |
| [22] E. T. Barr, M. Harman, P. McMinn, M. Shahbaz, and | based software engineering: Techniques, taxonomy, |  |  |  |  |
| S. Yoo. The oracle problem in software testing: A | tutorial. In B. Meyer and M. Nordio, editors, |  |  |  |  |
| survey. | IEEE Transactions on Software Engineering | , | Empirical software engineering and verification: |  |  |

---

## Page 12

| LASER 2009-2010 | , pages 1–59. 2012. LNCS 7007. | Segmented evolutionary testing of Android apps. In |  |  |  |
| --- | --- | --- | --- | --- | --- |
| [41] J. Itkonen, M. V. Mantyla, and C. Lassenius. How do | Proc. of ESEC/FSE’14 | , pages 599–609, 2014. |  |  |  |
| testers do it? an exploratory study on manual testing | [54] N. Mirzaei, J. Garcia, H. Bagheri, A. Sadeghi, and |  |  |  |  |
| practices. In | Proc. of ESEM’09 | , pages 494–497, 2009. | S. Malek. Reducing combinatorics in gui testing of |  |  |
| [42] J. Itkonen, M. V. Mantyla, and C. Lassenius. The role | android applications. In | Proc. of ICSE’16 | , 2016. To |  |  |
| of the tester’s knowledge in exploratory software | appear. |  |  |  |  |
| testing. | IEEE Transactions on Software Engineering | , | [55] N. Mirzaei, S. Malek, C. S. P˘ | as˘ | areanu, N. Esfahani, |
| 39(5):707–724, 2013. | and R. Mahmood. Testing Android apps through |  |  |  |  |
| [43] J. Itkonen and K. Rautiainen. Exploratory testing: A | symbolic execution. | SIGSOFT Software Engineering |  |  |  |
| multiple case study. In | Proc. of ESEM’05 | , pages | Notes | , 37(6):1–5, 2012. |  |
| 84–93, 2005. | [56] B. S. Mitchell, M. Traverso, and S. Mancoridis. An |  |  |  |  |
| [44] C. S. Jensen, M. R. Prasad, and A. Møller. | architecture for distributing the computation of |  |  |  |  |
| Automated testing with targeted event sequence | software clustering algorithms. In | Proc. of WICSA’01 | , |  |  |
| generation. In | Proc. of ISSTA’13 | , pages 67–77, 2013. | pages 181–190, 2001. |  |  |
| [45] M. E. Joorabchi, A. Mesbah, and P. Kruchten. Real | [57] K. Moran, M. Linares-V´ | asquez, C. Bernal-C´ | ardenas, |  |  |
| challenges in mobile app development. In | Proc. of | C. Vendome, and D. Poshyvanyk. Automatically |  |  |  |
| ESEM’13 | , pages 15–24, 2013. | discovering, reporting and reproducing Android |  |  |  |
| [46] C. Kaner, J. Bach, and B. Pettichord. | Lessons learned | application crashes. In | Proc. of ICST’16 | , 2016. To |  |
| in software testing | . 2008. | appear. |  |  |  |
| [47] M. D. Kaplowitz, T. D. Hadlock, and R. Levine. A | [58] C. Tantithamthavorn, S. McIntosh, A. E. Hassan, and |  |  |  |  |
| comparison of web and mail survey response rates. | K. Matsumoto. Automated parameter optimization of |  |  |  |  |
| Public Opinion Quarterly | , 68(1):94–101, 2004. | classification techniques for defect prediction models. |  |  |  |
| [48] P. S. Kochhar, F. Thung, N. Nagappan, and | In | Proc. of ICSE’16 | , 2016. To appear. |  |  |
| T. Zimmermann. Understanding the test automation | [59] A. Vargha and H. D. Delaney. A critique and |  |  |  |  |
| culture of app developers. In | Proc. of ICST’15 | , pages | improvement of the CL common language effect size |  |  |
| 1–10, 2015. | statistics of mcgraw and wong. | Journal of Educational |  |  |  |
| [49] A. Leitner, M. Oriol, A. Zeller, I. Ciupa, and | and Behavioral Statistics | , 25(2):101–132, 2000. |  |  |  |
| B. Meyer. Efficient unit test case minimization. In | [60] T. Wang, M. Harman, Y. Jia, and J. Krinke. |  |  |  |  |
| Proc. of ASE’07 | , pages 417–420, 2007. | Searching for better configurations: a rigorous |  |  |  |
| [50] Y.-D. Lin, J. Rojas, E.-H. Chu, and Y.-C. Lai. On the | approach to clone evaluation. In | Proc. of |  |  |  |
| accuracy, efficiency, and reusability of automated test | ESEC/FSE’13 | , pages 455–465, August 2013. |  |  |  |
| oracles for Android devices. | IEEE Transactions on | [61] W. Yang, M. R. Prasad, and T. Xie. A grey-box |  |  |  |
| Software Engineering | , 40(10):957–970, October 2014. | approach for automated GUI-model generation of |  |  |  |
| [51] M. Linares-V´ | asquez, M. White, C. Bernal-C´ | ardenas, | mobile applications. In | Proc. of FASE’13 | , pages |
| K. Moran, and D. Poshyvanyk. Mining Android app | 250–265, 2013. |  |  |  |  |
| usages for generating actionable GUI-based execution | [62] S. Yoo, M. Harman, and S. Ur. GPGPU test suite |  |  |  |  |
| scenarios. In | Proc. of MSR’15 | , pages 111–122, 2015. | minimisation: search based software engineering |  |  |
| [52] A. Machiry, R. Tahiliani, and M. Naik. Dynodroid: | performance improvement using graphics cards. |  |  |  |  |
| An input generation system for Android apps. In | Journal of Empirical Software Engineering | , |  |  |  |
| Proc. of ESEC/FSE’13 | , pages 224–234, 2013. | 18(3):550–593, June 2013. |  |  |  |

[53] R. Mahmood, N. Mirzaei, and S. Malek. EvoDroid:
