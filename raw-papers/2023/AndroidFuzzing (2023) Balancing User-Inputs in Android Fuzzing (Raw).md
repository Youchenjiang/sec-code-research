---
title: "Android Fuzzing: Balancing User-Inputs and Intents"
pages: 14
---

# Android Fuzzing: Balancing User-Inputs and Intents

## Page 1

Android Fuzzing: Balancing User-Inputs and Intents

Michael Auer
University of Passau

Andreas Stahlbauer

CQSE GmbH
Munich, Germany

Passau, Germany

Abstract—Android apps can be effectively tested by randomly
generating inputs and triggering corresponding events. Most
test generators focus on user-triggered events, such as button
clicks. However, the state of an app is not only determined by the
interactions with a user, but also inputs from the system and other
apps, which are called intents in Android. Intent fuzzing, that is,
the automated generation of randomized intents as test inputs, has
been demonstrated to be an effective means for identifying crashes
in apps. However, the behavior of intent handlers is inﬂuenced by
the state of the app, which may depend on the user’s interactions
with the app that triggers corresponding events. Recent test
generators have therefore started integrating some of both types
of events, leaving open questions about the best way to combine
and balance UI inputs and intents. In this paper, we describe
a general framework for integrating user events and intents for
testing Android apps. We study empirically how to best combine
these two types of events, and evaluate the effectiveness of the
combination. Our experiments suggest that combining UI inputs
and intents reveals substantially higher code coverage as well as
more unique crashes (844 on 500 F-Droid apps) than sending only
user-events (762) or only intents (511): The combined approach
achieves a magnitude higher activity coverage (78.07%) than using
only user inputs (70.45%) and sending only intents (58.23%).
Furthermore, 121 unique crashes were found only through the
combination of UI inputs and intents. Although intent crashes and
UI crashes result from similar exception types, they are distinct,
which is relevant when comparing test generators.

Index Terms—Test Generation, Fuzzing, Intents, Android

I. INTRODUCTION

A popular approach for ﬁnding bugs in Android apps is to
generate user inputs randomly or guided by a search algorithm,
and to send these inputs to an app running in an emulator or
on an actual device. Many test generation tools based on this
principle have been introduced in recent years [1]–[3], each
improving on the number of crashes they can detect. These
tools mostly focus on producing user inputs such as button
clicks, thus simulating users interacting with the apps. User
inputs, however, represent only a subset of the inputs that an
Android app typically handles: Besides user inputs, Android
apps also handle inter-process communication with the concept
of intents, which are means for describing operations to be
performed by an app through its event handlers.

Generating intents automatically (i.e., intent fuzzing) has been
shown to be an effective way to test apps, and has been reported
to reveal many crashes [4]–[8]. However, which intents an app
can process and which event handlers are activated depends
on the state of the app. This state is not only determined by
intents, but also by user inputs. Thus, testing only via intents
or only via UI inputs may miss out the possibility of triggering

44

Gordon Fraser
University of Passau

Passau, Germany

relevant crashes in Android apps. While most Android test
generators either focus on triggering UI events or on fuzzing
with intents only, there have been attempts to combine these
two types of testing, such as Dynodroid [9] and Stoat [6].

However, it remains unclear to what extent the use of
intents is instrumental in achieving improvements, and how
speciﬁcally the different input types should be combined in a
test sequence for maximum effectiveness. In fact, Android has
more than 100 system-level events, such as user actions (e.g.,
screen rotation) and broadcast intents (e.g., connection to
network) [6]; even though apps cannot handle all intents
available, investigating how frequently the test generator should
produce either UI or system-level events could help tuning
testing tools to achieve better results. Furthermore, there is
the question whether intent-induced crashes are different from
crashes produced by user inputs. For example, apps may not
be programmed to expect invalid (e.g., null-valued) intent
parameters and crash due to lack of defensive programming.

In this paper, we describe a general framework for combining
UI events with intents during test generation. We extend
the Android test generator MATE [10] to implement this
framework, such that it uses a pre-determined probability for
deciding whether to send an intent or a user input to the App
Under Test (AUT) next; intents are generated randomly using a
valid structure of information statically derived from the app’s
conﬁguration and bytecode. We empirically investigate how to
best combine user-input generation and intent generation, the
improvements achieved by using this hybrid approach, and the
types of crashes found by the improved approach. In detail,
the contributions of this paper are as follows:

• A general framework and implementation for combining
user-inputs and intents when testing Android apps.

• An empirical comparison of fuzzing UI events vs. intents
and the resulting coverage and crashes on 500 apps.

• An empirical investigation of the combination of UI event
and intent fuzzing and the resulting coverage and crashes.
Our results show that fuzzing both, intents and user inputs,
leads to higher code coverage and reveals more unique
crashes (844 on the 500 F-Droid apps) than sending only user
inputs (762) or only intents (511). The combined approach
achieves a magnitude higher activity coverage (78.07%) than
using only user inputs (70.45%) and sending only intents
(58.23%). Furthermore, 121 of the unique crashes found only
through the combination of UI inputs and intents were never
triggered by sending only one type of event, suggesting that
there are synergetic effects resulting from this combination.


---

## Page 2

System

Intents

Broadcast
Receivers
Services
App

Activities
Content
Providers

UI Input

User

Fig. 1: Architecture of an Android application.

II. ANDROID BACKGROUND

Android applications (apps) consist of activities, services,
content providers, and broadcast receivers (Figure 1). Android
follows an event-driven programming model and the compo-
nents may handle events triggered by either the system or by
user interactions. Except for user inputs, events are typically
triggered by sending intents, which pass information between
apps and between the components within an app. Typically,
intents describe operations that should be carried out by the
target component. In addition, they hold values that serve as
the parameters to the operations that are to be performed.

A. Components of Android Apps

The components and the communication structure of an
Android app are declared in the app’s manifest description—
for full details we refer to the Android Developer Docs. An app
is composed of one or more of the following components [11]:

Activities:
Activity
are
windows
containing
widgets (e.g., buttons, text boxes), and different activities
exist for logically separate functionalities of the user interface.
Users can interact with the widgets, and the user’s inputs
trigger event handlers such as onClick or onTouch. Activities
also provide handlers for phases of the Android activity
lifecycle [12]; e.g., the onCreate method is invoked when an
activity is created.

Services: Services execute long-running tasks that run in
the background, e.g., remote database queries. Consequently,
services do not produce a graphical interface with which an
user can interact. There are two types of services: unbound
and bound services. The former type is not coupled to other
components and can run indeﬁnitely, while the latter is bound
to some component and exists only as the component.

Content Providers: Content providers expose interfaces for
accessing data, e.g., contacts or calendars. Custom access
policies can restrict whether data is shared among different
apps or only the hosting application can access them.

Broadcast Receivers: Broadcast receivers handle notiﬁca-
tions about system events such as reaching a speciﬁc battery
level. Information about these events is wrapped into intents and
sent by the system. Broadcast receivers can also receive intents
from other apps or components. Broadcast receivers are either

registered statically in the application’s central conﬁguration
(the manifest ﬁle, c.f. Section II-C) or dynamically at runtime.

B. Intents: Android Messaging Objects

Intents describe operations to be performed; they are the
basic units of communication between the components of an
app or between different apps. They are used to invoke other
components (for example, to launch an activity), and to inform
other components about events (for example, an incoming text
message). Intents can be classiﬁed as either explicit or implicit:
Explicit intents specify which component will receive the intent.
Implicit intents declare a general action to be performed, so
that all components (including components of other apps) may
handle this intent. For instance, opening a web page might be
carried out by one of multiple web browsers.

An intent is a tuple (a, d, c, t, m, e) ∈I, from the set of
intents I, with the following properties [13]:

1) An action a is the most essential part of an intent and
describes what operation should be performed upon receiving
the intent. For example, the action ACTION_VIEW would
request to show some data to the user. The set of all possible
actions is not limited to the predeﬁned Android actions, but
custom actions can also be deﬁned.

2) The data ﬁeld d contains a uniform resource identi-
ﬁer (URI) that refers to some data the action is supposed
to operate on. An URI is a string that is composed of four
parts: a scheme, host, port, and path.

3) The set of categories c is an optional attribute classifying
the speciﬁed action. It is possible to specify multiple categories.

4) The ﬁeld type t speciﬁes the MIME type for the supplied
data, for example, image/jpeg. Its usage is optional, if not set,
the type is automatically derived from the ﬁlename.

5) The ﬁeld component m stores the target component that is
supposed to handle the intent. If it is set, we refer to the intent
as an explicit intent, otherwise we call it an implicit intent. If
unspeciﬁed, the target component is derived from the remaining
attributes, potentially enabling multiple components to handle
the intent (in this case, the user can select the appropriate app).

6) The optional ﬁeld extras e may contain an optional data
object called bundle consisting of key-value pairs. This ﬁeld
is primarily used to hold further application data, for example,
the phone number of the callee.

C. Conﬁguring Components and Event Handlers

The manifest of an app is a ﬁle that describes, among
other things, its components and how they communicate.
Listing 2 shows an excerpt of such a ﬁle adapted from the
F-Droid application BMI Calculator. Required permissions
are speciﬁed with the uses-permission tags, for example the
permission SEND_SMS is needed to send an SMS. Each
component may additionally specify multiple intent-ﬁlter tags to
declare which intents it can process. These specify the implicit
intents that a service, an activity, or a broadcast receiver can
handle. For example, in Figure 2 the broadcast receiver named
StartUpBootReceiver can handle intents specifying the action
BOOT_COMPLETED. This means the StartUpBootReceiver is

45


---

## Page 3

<manifest package="com.zola.bmi">
...
<uses-permission android:name="android.permission.SEND_SMS"/>
...
<activity android:name="com.zola.bmi.FileViewer">

<intent-filter>

<action android:name="android.intent.action.VIEW"/>
<category android:name="android.intent.category.LAUNCHER"/>
<data android:scheme="file" />
<data android:mimeType="text/plain" />
</intent-filter>
</activity>
<service android:name="com.zola.bmi.AuthenticationService"

android:exported="false">
</service>
<receiver android:name="com.zola.bmi.StartUpBootReceiver">

<intent-filter>

<action android:name="android.intent.action.BOOT_COMPLETED" />
</intent-filter>
</receiver>
...
</manifest>

Fig. 2: Excerpt of an AndroidManifest.xml.

{ act=android.intent.action.VIEW cat=[android.intent.category.LAUNCHER]

dat=file:///storage/0/emulated/Downloads/test.txt
typ=text/plain cmp=com.zola.bmi/.FileViewer }

Fig. 3: An intent that triggers the FileViewer activity.

notiﬁed when the boot process has been completed. The content
of such a ﬁlter (with tag intent-ﬁlter) is generally described by
its action, category and data. The Android framework ﬁnds
the intent’s receiver(s) by matching the content of the intent
with the intent ﬁlters declared by the apps’ components. When
several components are applicable for handling the intent, the
user can pick an appropriate app in a system dialog.

When explicit intents are sent with a target component
speciﬁed, any intent ﬁlters declared by this component are
ignored: It is possible to invoke a component with an arbitrary
intent as long as the name of the target component is known
and the component is marked as exported. This is often
misunderstood and can lead to security issues [14]. The
exported attribute decides whether a component is accessible
from the outside, by other apps. If the attribute is set to false,
only components belonging to the same app can communicate
with this component. If the component speciﬁes any non-empty
intent ﬁlters, the component is assumed to be exported.

Finally, it is possible to declare aliases for activities with the
activity-alias tag. Similar to other component tags, the activity-
alias tag can specify additional intent ﬁlters and attributes,
which are not already listed for the actual activity. These ﬁlters
and attributes take the same role as in the original activity.

Listing 3 shows an example intent for the intent ﬁlter of the
com.zola.bmi.FileViewer activity described in Listing 2: The
manifest speciﬁes that this component can process VIEW actions
that receive text ﬁles as data. The intent has its components
set to valid values as per the manifest, and the data is set to
an existing text ﬁle. When the component receives this intent,
it will trigger the action to view the ﬁle test.txt.

D. Android Testing and Android Fuzzing

Typically, Android developers will test their apps in two
different ways: They can test different parts of their application
independently from the other parts and without the need to
execute them inside an emulator or on a physical Android
device; i.e., they can apply unit testing. Secondly, they can
test the entire application running inside an emulator or on a
physical device using automated UI tests that can assert whether

46

predeﬁned states of the app are reached during execution. The
latter type are generated automatically by fuzzers, a research
topic that has been widely explored recently [2], [3], [15].
Testing approaches typically generate user inputs—for example,
clicks, long-clicks, swipes—to exercise the GUI, or intents to
exercise inter-component or inter-app communication. In both
cases, most approaches aim to ﬁnd issues regarding runtime
crashes, exceptions, security, performance, or energy-efﬁciency.

When it comes to generating user inputs, most approaches
are based on dynamic analysis and repeat the following steps
until a stopping criterion (e.g., a time budget) is met: (1) eligible
relevant events—e.g., button click, input text—are extracted
from the GUI; (2) one relevant event is selected and executed;
and (3) the effects of the event execution are evaluated—crash,
moved to new state, code coverage. A dynamic model of the
AUT is sometimes built during this process to support test
generation. The next event to be executed is selected either by
using systematic (e.g., depth or breadth ﬁrst search) or random
strategies (e.g., [16]–[24]). Some approaches additionally
collect information from the source code to improve test
generation, e.g., [5], [25]–[32]. Access to the source code
enables testing strategies such as search-based testing [5], [27],
[31], [33] or symbolic execution [30], [31], [34].

Intent fuzzing is another approach to test apps: Most recent
intent fuzzer tools (e.g., [4], [14], [35], [36], apply static
analysis to retrieve information about the attributes of intents
from the manifest. In addition, most tools, e.g., [7], [36], [37],
also extract (string) constants from the bytecode that are passed
as input to the generation of the extras. Similarly, information
about the key and type of extras is either retrieved statically [37],
[38] or dynamically [14], [36] by instrumenting certain API
calls. Some tools [7], [36] provide predeﬁned ﬁles for the most
common data types, except DroidFuzzer [35], which derives an
initial block of data from the speciﬁcation of the MIME type,
and then modiﬁes it using its variation engine. Some approaches
start with empty intents that are then ﬁlled iteratively [4],
[14] using different strategies, sometimes using invalid data
for certain attributes. Alternative approaches include deriving
intents from hand-crafted intent speciﬁcations [8] or inter-
component communication graphs [39].

The effectiveness of the many different Android test gen-
erators is a much debated topic, in particular in the light of
the good performance of the basic Android Monkey tool [1].
However, recent approaches have been demonstrated to be
more effective at revealing crashes, and some of these, such
as Stoat [6], provide a combination of user events and intents.
Our aim in this paper is to investigate the relation of user-input
based and intent-based test generation in more detail.

III. FUZZING INTENT AND UI INPUTS

We now describe a general framework for combining user-
inputs and intents when testing Android apps. In particular, we
examine how to combine sending UI inputs and intents for an
effective test execution. This involves mining the manifest and
a static analysis of the DALVIK bytecode.


---

## Page 4

Algorithm 1 testLoopρ

Input: Intent probability ρ ∈[0, 1]

1: while not stopCondition do
2:
(test, stacktrace) ←runTest(p)
3:
if |stacktrace| > 0 then
4:
log(test, stacktrace)
5:
restartApp()

Algorithm 2 runTestρ

Input: Intent probability ρ ∈[0, 1]
Output: Pair (test, stacktrace) of a sequence of test inputs and a stack trace

1: test ←ïð
2: for i = 1 to getMaxNumInputs() do
3:
if getRandom(0, 1) > p then
4:
e ←generateUserInput()
5:
else
6:
c ←chooseTargetComponent()
7:
e ←generateIntent(c)
8:
test ←test ◦ïeð
9:
stacktrace ←stimulateApp(e)
10:
if |stacktrace| > 0 then
11:
return (test, stacktrace)
12: return (test, ïð)

A. Test Generation Strategy

The main loop of the testing procedure is described by
Algorithm 1. Until a stopping condition is satisﬁed (e.g., a
time budget is exhausted), tests are generated and executed
successively. The algorithm is parameterized implicitly with
the parameter ρ, which deﬁnes the probability for sending an
intent instead of performing a UI input. If a test produces
a crash, information about that crash—the sequence of test
inputs that caused it and its stack trace—are stored. After each
execution of a test case the AUT is reset, which ensures a
clean starting state at the beginning of each test case.

The functionality of runTest(p) in line 2 is described by
Algorithm 2. First, an empty test is initialized, which is ﬁlled
within a loop (line 2–11) with either a UI input or an intent each
iteration until the maximum number of subsequent inputs (line
2) is reached or a crash has been discovered (line 10). The type
of the input e depends on the probability ρ. In line 9 the AUT
is stimulated with the input. In case of a crash a stack trace is
produced and the function returns immediately (line 10–11).
Otherwise, a graceful return is performed after reaching the
maximum number of inputs (line 12).

The selection of a target component is managed by the
procedure chooseTargetComponent(): Initially, the relative
numbers of components of each type are determined, e.g.,
how many activities are present in comparison to the total
number of components. Next, these values are directly mapped
to probabilities informing a probabilistic choice of component
type. Finally, a component is randomly chosen from the elected
component type. There is one minor exception to this rule. If
an activity is picked, the procedure uniformly chooses between
targeting the current activity or an arbitrary one. This rule was
employed to trigger the onNewIntent method of an activity and
requires the current activity to be active. If the current activity
does not deﬁne such a method, the procedure picks another
activity at random. Note that content providers do not receive
intents [36] and hence are ignored.

B. UI Input Generation

The generation of a UI input is done in a semi random
fashion [40]. First, a list of eligible widgets is identiﬁed based
on the current state of the app (i.e., the current screen state),
where on each widget a couple of actions can be performed, e.g.,
a button can be clicked. Then, a widget and one of the possible
actions that can be performed on that widget is chosen from
this list at random and returned by generateUserInput(). Note
that we do not enforce any timeouts between two consecutive
actions unless a progress bar is detected. In addition to the
list of actions that can be performed on widgets, the random
choice also considers a list of UI inputs that are not directly
linked to a widget such as press back, press menu, open quick
drawer, and more. A further category of user events—only
included by some tools such as STOAT [6]—includes actions
like toggle landscape mode, sleep and wake up.

C. Intent Generation

The construction of an effective intent requires a preliminary
static analysis of the manifest and the DALVIK bytecode. The
manifest provides essential information about attributes that
are expected for a speciﬁc intent. In particular, the intent
ﬁlters that are declared in the manifest provide information for
each component in terms of the possible values for the action,
category, and data attributes. The information extracted from
the manifest may not be complete, as, for example, broadcast
receivers can be registered dynamically at runtime.

Further information about the keys and types of values that
can be speciﬁed in a bundle object for an intent can be extracted
from the bytecode of the application. For example, instances
of the form Intent.get*Extra(key : String) reveal which keys
require values to be set. Here, * is a placeholder for a default
Java data type, for example, String, int, or double—see [13]
for a complete list of supported types. This analysis yields
tuples of the following form (<key>, <type>), for example,
("phone-number", String). Note that the target component is
given by the class invoking one of these calls. Thus, we know
to which component the bundle belongs to. We also extract
string constants from the bytecode and feed them as inputs
to our intents. In particular, we collect the string constants
deﬁned in each component’s class ﬁle. These serve as values
for extras of type String. If no string constants were deﬁned,
we fall back on a list of pre-deﬁned strings. In addition to the
components obtained from the manifest, we extract declared
dynamic broadcast receivers from the bytecode by backtracking
calls to Context.registerReceiver(). Our current implementation
supports tracking of action and category tags.

The actual generation of intents is implemented in the method
generateIntent() and operates as follows: i) An empty intent
is initialized. ii) An action is randomly chosen from the list
of extracted actions and attached to the intent. iii) A category
is randomly selected from the list of extracted categories and
attached to the intent. If multiple categories are available, we
add further categories with decreasing probability. iv) A data
URI is randomly constructed from the list of extracted data
tags and attached to the intent. For most basic MIME types

47


---

## Page 5

we provide predeﬁned ﬁles that are used if possible. v) The
intent is made explicit by specifying the name of the target
component. This ensures that the target component is the sole
receiver of the intent. There is one minor exception to this rule:
Dynamic receivers cannot receive explicit intents. In this case,
we specify the app’s package name, which in turn restricts
the receiver of the intent to be a component of the app. vi) If
the target component expects a bundle object, we proceed
as follows: First an empty bundle object is constructed. This
object is iteratively ﬁlled with key-value pairs where the key
and its corresponding type is retrieved from the result of the
analysis of the bytecode. The corresponding value is chosen
randomly from a predeﬁned pool of values of the different data
types. Recall that keys with the associated type String reuse
string constants extracted from the bytecode if possible.
Unlike simple fuzzing of intents, our intents are by construction
not discarded by the system and solely target a dedicated
component. Moreover, similar to STOAT [6], we support intents
conveying system event notiﬁcations like BOOT_COMPLETED.

IV. EMPIRICAL STUDY

Based on the general framework for combining user inputs
with intents, we aim to answer the following research questions:

RQ1: What is the best way to combine UI events and intents?
RQ2: What are the effects of testing with UI events and intents?

A. Implementation

We used the Android test generation tool MATE [10] for
experiments, which implements state of the art test generation
for Android and is available as open source. We extended
MATE with the functionality to send intents as described
in Section III. We conducted the experiments on a compute
cluster, where each node is equipped with two Intel Xeon
E5-2620v4 CPUs (16 cores) with 2.10 GHz and 256 GB of
RAM, and runs Debian GNU/Linux 11 with Java 11. We
limit each execution of MATE to four cores and 60 GB
of RAM, where the emulator (Nexus 5) runs a x86 image
with API level 25 (Android 7.1.1) and is limited to 4 GB of
RAM with a VM heap size of 576 MB. We make the imple-
mentation including the study subjects publicly available at
https://ﬁgshare.com/articles/dataset/replication_zip/21378780.

B. Study Subjects

To empirically answer the stated research questions, we sam-
pled two data sets consisting of 40 and 500 apps, respectively:

TUNING dataset: This data set consists of 40 apps
sampled from previous studies [33], [41], [42], where we
excluded apps that could not be successfully instrumented.
We use this dataset for determining the best value for the
parameter ρ. Table I enumerates these apps along with some
measures on their size and structure.

EVALUATION dataset: The second data set comprises
500 applications sampled from FDroid. During sampling, we
discarded apps belonging to the Game category and those that
could not be successfully instrumented. This data set serves to
evaluate testing with UI events and intents (RQ2).

48

TABLE I: Characteristics of TUNING case study.

Component distribution by app in terms of total and exposed components.

App Name
Activities
Services
Broadcast Receivers

Static
Dyn.
Total
Exp.
Total
Exp.
Total
Exp.

com.liato.bankdroid
17
3
3
0
7
4
0
com.willianveiga.countdowntimer
3
1
0
0
1
0
0
com.pvcodes.debtcalc
5
0
0
0
2
0
0
org.tomdroid
8
4
0
0
0
0
0
net.sf.andbatdog.batterydog
2
1
1
0
1
0
0
org.jtb.alogcat
3
1
2
0
2
2
0
net.fercanet.LNM
4
4
0
0
0
0
0
pt.lighthouselabs.obd.reader
9
1
2
0
1
0
0
me.anon.grow
20
2
1
0
5
1
0
com.ichi2.anki
28
1
3
0
13
2
7
de.freewarepoint.whohasmystuff
2
1
0
0
0
0
0
com.woefe.shoppinglist
4
1
1
0
0
0
0
org.quantumbadger.redreader
19
3
1
0
6
1
1
jp.gr.java_conf.hatalab.mnv
8
2
0
0
0
0
0
org.schabi.newpipe
11
4
1
0
4
0
0
de.smasi.tickmate
7
1
0
0
1
0
0
bander.notepad
7
4
0
0
0
0
0
org.billthefarmer.specie
5
0
0
0
1
0
0
protect.rentalcalc
12
1
0
0
1
0
0
com.olam
2
1
0
0
1
0
0
com.smorgasbork.hotdeath
3
1
0
0
0
0
0
com.orpheusdroid.screenrecorder
7
1
3
1
2
0
0
de.rampro.activitydiary
12
2
2
0
2
0
0
org.liberty.android.fantastischmemo
24
3
4
0
11
2
0
hu.vsza.adsdroid
3
1
0
0
2
1
0
com.ringdroid
3
2
0
0
0
0
0
com.oriondev.moneywallet
38
2
7
0
26
1
0
de.retujo.bierverkostung
13
1
0
0
1
0
0
de.arnowelzel.android.periodical
8
1
0
0
0
0
0
cri.sanity
28
2
5
0
11
6
2
org.beide.bomber
2
1
0
0
0
0
0
com.gmail.altakey.effy
3
1
1
0
0
0
0
org.y20k.transistor
6
1
2
0
9
0
1
de.tap.easy_xkcd
12
2
3
0
5
2
1
ch.ﬁxme.cowsay
1
1
0
0
0
0
0
caldwell.ben.bites
5
1
0
0
1
0
0
org.jessies.dalvikexplorer
17
1
0
0
1
1
0
net.gsantner.markor
10
3
1
0
2
1
0
com.rigid.birthdroid
4
1
1
0
1
1
0
de.drhoffmannsoftware
10
1
0
0
0
0
0

Average:
9.62
1.62
1.10
0.03
3.00
0.62
0.30

C. Experiment Procedure

RQ1: To determine how UI events and intents should be
combined to reveal many faults while exploring as much as
possible code of the AUT, we ran MATE on the TUNING
dataset conﬁgured with a varying intent probability ρ ∈
{0%, 10%, . . . , 100%} for one hour each. To compensate for
randomness we repeated each conﬁguration 10 times. To
determine the overall best conﬁguration using this data we use
tournament ranking: For each pair of conﬁgurations (c1, c2)
we statistically compare the two conﬁgurations for each of the
apps in terms of the number of unique crashes found and the
resulting activity and line coverage using a Wilcoxon-Mann-
Whitney U test, with a 95% conﬁdence level. If a statistical
difference is observed, we use the Vargha-Delaney ˆA12 effect
size [43] to determine which of the two conﬁgurations is better,
and the score for this conﬁguration is increased by one. At the
end, the conﬁguration with the highest score is the overall best
conﬁguration. We consider two crashes as identical if (1) their
exception types match, and (2) they share the same stack trace.
We do not compare the exception messages, as they often vary
in terms of object references or user inputs included.


---

## Page 6

RQ2: We would like to evaluate whether a combination
of UI events and intents does not only reveal more crashes
and increases coverage, but also whether it exposes distinct
crashes. We ran MATE with three different conﬁgurations for
ρ: ρ = 0.0 (Only UI), ρ = 0.1 (best conﬁguration according to
RQ1) and ρ = 1.0 (Only Intent), on the EVALUATION dataset.
We are interested in the number and type of crashes as well as
the activity and line coverage. To determine whether the crashes
are distinct, we compare the union of Only UI and Only Intent
with the best conﬁguration. In addition, to ensure our results
based on MATE are representative we compare with the state-
of-the-art testing tools MONKEY [44] and STOAT [6], each
conﬁgured to explore each app of the EVALUATION dataset
for one hour and report activity and line coverage as well as
the number of unique crashes. These two tools both include
UI events as well as intents, and in particular for STOAT the
question arises to what extent its reported good performance
is due to the inclusion of system events. For MONKEY we set
a reasonable delay of 500ms between two consecutive actions.
For STOAT we speciﬁed a timeout of 30 minutes for both
model construction and Gibbs sampling. We had to adjust
STOAT to use the same coverage tool as MATE to enable a
consistent comparison among reported coverage values.

D. Threats to Validity

Threats to external validity may arise from our sample of
subject apps, and results may not generalize beyond the tested
apps. To counteract selection bias, we picked the apps for the
tuning study from three different sources, while the 500 apps
for the evaluation study have been chosen randomly. There
may also be some implicit bias, e.g., the apps on F-Droid
might be simpler than those on Google PlayStore. We also
stuck to one speciﬁc emulator conﬁguration and one concrete
API level, but results may differ on other versions.

Threats to internal validity may arise from bugs in MATE
or our analysis scripts. To mitigate this risk, we manually
reviewed the results, and tested and reviewed all code. To
reduce the risk of favoring one research tool over the other, we
used default parameters suggested by the tool authors. Lastly,
to allow for a fair comparison between the reported coverage
values, we adopted in STOAT the same coverage mechanism
as in MATE.

Threats to construct validity may result from our choice
of metrics, in particular coverage and crashes. Results may
differ when considering non-crashing functional bugs, and
even though our heuristic to decide when crashes are unique
is commonly used, it may be imprecise.

E. RQ1 Results

Table II lists the different conﬁgurations together with the
number of unique crashes, activity and line coverage. The last
three columns contain the scores of the tournament ranking. We
generally note that both coverage and the number of crashes
go down with higher probabilities of fuzzing intents. However,
not using intents at all (ρ = 0.0) also appears to be missing out
on certain coverage and crashes. Therefore, the conﬁguration

TABLE II: Evaluation of conﬁgurations on TUNING dataset.

Number of unique crashes, activity and line coverage as well as a score based
on tournament ranking, where ρ = 0.1 appears to be the best conﬁguration.

Conf.
Crashes
Coverage
Scores
AC
LC
Crashes
AC
LC

ρ=0.0
24.48
64.48
50.58
88
140.00
257.00
ρ=0.1
26.75
67.52
50.91
115
165.00
292.00
ρ=0.2
26.10
65.35
48.85
107
135.00
260.00
ρ=0.3
23.95
64.01
46.93
87
121.00
232.00
ρ=0.4
21.27
62.70
45.39
62
113.00
200.00
ρ=0.5
19.27
61.07
43.85
49
93.00
169.00
ρ=0.6
16.10
58.39
41.67
44
77.00
131.00
ρ=0.7
13.72
56.74
39.64
29
60.00
102.00
ρ=0.8
12.07
53.92
37.34
31
42.00
75.00
ρ=0.9
10.07
48.84
33.69
23
22.00
43.00
ρ=1.0
8.20
34.54
18.32
18
1.00
2.00

Average:
18.36
57.96
41.56
-
-
-

ρ = 0.1 produces the best results with respect to all three
criteria, both in terms of average values as well as tournament
ranking scores. This also implies that combining UI events
with intents makes sense, since both the number of unique
crashes and coverage can be increased.

A possible conjecture why a low probability of ρ = 0.1 is
better than higher probabilities could be that intent handling
code only represents a small share of the code compared to UI
input processing, and ρ = 0.1 might be relatively proportional
to this. While certain code parts may only be reached through
a complex series of UI inputs, a single intent can potentially
explore the dependent code directly. It may also be possible
that automatically generated intents achieve coverage mainly
by exercising input validation code, but struggle more to reach
“deeper” aspects of functionality, such that sending more intents

overall is counterproductive in terms of coverage.

On the other hand, a non-zero probability of ρ = 0.1 being
better than ρ = 0.0 may be due to UI inputs simply not covering
intent handling code, or not reaching intent-dependent activities.

Summary (RQ1): The best results in terms of coverage and
crashes is achieved by fuzzing intents with a low probability
of 10%, and fuzzing the UI with 90% probability.

F. RQ2 Results

We ﬁrst verify how the best conﬁguration according to the
tuning study performs on the EVALUATION dataset. In Table III
one can observe for the conﬁgurations Only UI, Best and Only
Intent the total number of unique crashes separated into UI and
intent crashes as well as the average activity and line coverage.
The Best conﬁguration still appears to represent the best trade
off between UI and intent crashes, while outperforming the
conﬁgurations Only UI and Only Intent in terms of coverage.
In total, the Best conﬁguration discovers 82 unique crashes
more than Only UI and even 333 in contrast to Only Intent.

To get a better picture on the differences in coverage, Figure 4
and Figure 5 show the distribution of activity and line coverage,
respectively for the three conﬁgurations. At the right side

49


---

## Page 7

TABLE III: Evaluation on EVALUATION dataset.

Number of unique crashes separated in UI and intent crashes as well as activity
and line coverage for the conﬁgurations Only UI, Best and Only Intent.

Conﬁguration
Unique Crashes
Coverage
UI
Intent
Total
AC
LC

ρ=0.0
762.00
0.00
762.00
70.45
42.50
ρ=0.1
655.00
196.00
844.00
78.07
45.32
ρ=1.0
0.00
511.00
511.00
58.23
24.72

Average:
472.33
235.67
705.67
68.92
37.51

100

Activity Coverage

75

50

25

0

Only UI
Best
Only Intent
Monkey
Stoat

Fig. 4: Activity coverage on the EVALUATION dataset.
Compares the activity coverage distribution for the conﬁgurations Only UI,
Best, Only Intent, Monkey and Stoat.

of each plot, we show in addition the coverage distribution
for MONKEY and STOAT. Considering Figure 4, there is a
clear dominance of the Best conﬁguration regarding activity
coverage in comparison to the conﬁgurations Only UI, Only
Intent and MONKEY. The median is 100%, while Only UI is
below 80%, Only Intent around 50% and MONKEY achieves
a bit less than 70%. We ﬁnd a statistical signiﬁcance for the
Best conﬁguration in comparison to the conﬁgurations Only UI,
Only Intent and MONKEY with p < 0.0001 and effect-sizes of
0.57, 0.66 and 0.61, respectively. In fact, the Best conﬁguration
can also compete with STOAT, which also has a median of
100%, although there is a statistically signiﬁcant difference
(p = 0.03) with a small effect-size of 0.46 in favor of STOAT.

The difference at the line coverage level is not so signiﬁcant
anymore, at least between the Best conﬁguration and Only
UI, while the median for Only Intent is roughly the half.
The difference to the exploration with MONKEY is also
smaller. In fact, there is no statistical signiﬁcance between
the conﬁgurations Best and Only UI (p = 0.08), while we
still have a statistical signiﬁcance of the Best conﬁguration in
comparison to the conﬁgurations Only Intent and MONKEY
with p = 0.008 and effect sizes of 0.74 and 0.56, respectively.
We cannot state a statistical signiﬁcance in comparison to

STOAT (p = 0.59). Nevertheless, the Best conﬁguration
achieves the highest median among all conﬁgurations.

We can perform the same comparison also regarding the
distribution of the unique crashes, shown in Figure 6. Since
many apps did not result in any crashes, we removed the
outliers in the plot to get a better view on the core distribution.
The green rectangles denote the means of each distribution.
While all conﬁgurations report a median of 0, the Best
conﬁguration achieves the highest mean (1.69). Moreover, the
Best conﬁguration reports a statistically signiﬁcant difference
in comparison to the conﬁgurations Only UI, Only Intent and

50

100

Line Coverage

75

50

25

0

Only UI
Best
Only Intent
Monkey
Stoat

Fig. 5: Line coverage on the EVALUATION dataset.
Compares the line coverage distribution for the conﬁgurations Only UI, Best,
Only Intent, Monkey and Stoat.

2.0

Unique Crashes

1.5

1.0

0.5

0.0

Only UI
Best
Only Intent
Monkey
Stoat

Fig. 6: Unique crashes on the EVALUATION dataset.
Compares the unique crashes distribution for the conﬁgurations Only UI, Best,
Only Intent, Monkey and Stoat.

MONKEY with p < 0.0001 and effect sizes of 0.56, 0.61 and
0.58, respectively. Overall, the Best conﬁguration is likely to
produce more unique crashes, on par with STOAT (p = 0.67).

To classify whether the crashes triggered by a UI input
are different from those produced by an intent, we consider
Table IV, which shows the exception types appearing in
both conﬁgurations and states how often each exception was
triggered by Only UI and Only Intent, respectively. The
last column indicates how many exceptions of a speciﬁc
exception type could be triggered by both conﬁgurations. In
fact, almost none of the listed exceptions was produced by
both Only UI and Only Intent, and we only see an overlap
in IllegalArgumentExceptions. This indicates that the set of
exceptions produced by only UI inputs is extremely disjoint to
the set of exceptions triggered by only intents, which in turn
strengthens our hypothesis that a solid combination of both
input types is required to explore an app thoroughly.

To evaluate whether the Best conﬁguration (a combination
using both UI inputs and intents) results in a different
distribution regarding the exception types, we can consult
Table V. It lists the exception types, together with the number
of unique occurrences and which type of action triggered
the exception how often. The numbers indicate that certain
exceptions types are more likely to be triggered by one type of
action, e.g., NumberFormatExceptions are almost only triggered
by UI inputs, likely referring to textual data entered by the
test generator into text ﬁelds that expected numeric input. On
the other hand, ClassCastExceptions can be revealed primarily
by intents, and is mainly due invalid bundles attached to the
intents, and lack of input validation code in the app.

To further classify whether certain exceptions can be only
triggered by a combination of UI inputs and intents, consider
Table VI: It shows for the exception types appearing in Only


---

## Page 8

TABLE IV: Crashes found by Only UI vs Only Intent.

Lists the exception types appearing in the conﬁgurations Only UI and Only
Intent. For each exception type the number of unique occurrences in each
conﬁguration is given alongside a similarity measure.

Exception Type
Unique Crashes
Similarity
UI
Intent

NumberFormatException
347
5
0.00%
IllegalStateException
66
180
0.00%
OutOfMemoryError
2
152
0.00%
IllegalArgumentException
92
24
0.86%
NullPointerException
55
52
0.00%
ActivityNotFoundException
71
24
0.00%
RuntimeException
39
1
0.00%
URISyntaxException
39
0
0.00%
ClassCastException
2
24
0.00%
ClassNotFoundException
4
16
0.00%
IndexOutOfBoundsException
6
7
0.00%
NoSuchMethodException
9
0
0.00%
StringIndexOutOfBoundsException
8
0
0.00%
JSONException
1
6
0.00%
UnsupportedOperationException
4
2
0.00%
Resources$NotFoundException
1
4
0.00%
FileUriExposedException
2
1
0.00%
InsufﬁcientAccessException
2
0
0.00%
StackOverﬂowError
2
0
0.00%
ArrayIndexOutOfBoundsException
2
0
0.00%
ViewRootImpl$CalledFromWrongThreadException
2
0
0.00%
CursorIndexOutOfBoundsException
1
1
0.00%
FileNotFoundException
0
2
0.00%
NotImplementedError
0
2
0.00%
JavascriptException
1
0
0.00%
NoClassDefFoundError
1
0
0.00%
ZipException
1
0
0.00%
a
1
0
0.00%
NoSuchMethodError
1
0
0.00%
JsonDecodingException
0
1
0.00%
TypeCastException
0
1
0.00%
ArithmeticException
0
1
0.00%
b
0
1
0.00%
CursorWindowAllocationException
0
1
0.00%
g0$e
0
1
0.00%
UninitializedPropertyAccessException
0
1
0.00%
RejectedExecutionException
0
1
0.00%

UI, Best and Only Intent how many unique crashes could
be discovered by the respective conﬁgurations. The numbers
in parentheses indicate how many of the crashes were also
revealed by the Best conﬁguration. Overall, 565 out of the 762
Only UI crashes and 161 out of the 511 Only Intent crashes
were also reproduced by the Best conﬁguration.

The similarity column indicates how many unique crashes of
the Best conﬁguration appear also in the union of Only UI and
Only Intent expressed as a percentage. On average, the Best
conﬁguration can reproduce roughly 57% of the crashes found
by either Only UI or Only Intent. Since the Best conﬁguration
found the most unique crashes according to Table III, this
indicates that there must be crashes only discovered by the
Best conﬁguration. As the last column of Table VI conﬁrms,
the Best conﬁguration can reveal 121 unique crashes that could
not be discovered by Only UI or Only Intent in isolation.

Summary (RQ2): The combination of UI and intent fuzzing
can not only ﬁnd more crashes, but also distinct ones: Out of
844 unique crashes discovered by the Best conﬁguration, 121
were neither found using only UI inputs or intents. Similarly,
the combined approach achieves higher activity coverage
(78.07%) than Only UI (70.45%) and Only Intent (58.23%).

TABLE V: Exceptions types for Best conﬁguration.

Lists the exception types for the Best conﬁguration alongside stats about the
frequency and the action type that caused the exception.

Exception types
Unique
Caused By
Occ.
UI Input
Intent

NumberFormatException
290.00
288.00
2.00
NullPointerException
118.00
61.00
61.00
IllegalStateException
97.00
68.00
30.00
IllegalArgumentException
82.00
61.00
21.00
ActivityNotFoundException
64.00
59.00
5.00
URISyntaxException
34.00
34.00
0.00
RuntimeException
32.00
29.00
3.00
ClassCastException
27.00
2.00
26.00
OutOfMemoryError
14.00
6.00
8.00
IndexOutOfBoundsException
13.00
6.00
7.00
NoSuchMethodException
11.00
11.00
0.00
ClassNotFoundException
6.00
3.00
3.00
FileNotFoundException
5.00
3.00
2.00
StringIndexOutOfBoundsException
5.00
5.00
0.00
JSONException
5.00
1.00
4.00
SecurityException
4.00
0.00
4.00
NotSerializableException
4.00
0.00
4.00
FileUriExposedException
4.00
3.00
1.00
Resources$NotFoundException
3.00
1.00
2.00
UnsupportedOperationException
3.00
1.00
2.00
JavascriptException
3.00
3.00
0.00
NotImplementedError
2.00
0.00
2.00
CursorIndexOutOfBoundsException
2.00
1.00
1.00
ArrayIndexOutOfBoundsException
2.00
2.00
0.00
WriteError
1.00
1.00
0.00
ArithmeticException
1.00
1.00
1.00
ServiceSpeciﬁcException
1.00
0.00
1.00
UninitializedPropertyAccessException
1.00
0.00
1.00
SQLiteConstraintException
1.00
0.00
1.00
SQLiteException
1.00
1.00
0.00
ViewRootImpl$CalledFromWrongThreadException
1.00
1.00
0.00
GlideException
1.00
1.00
0.00
TypeCastException
1.00
0.00
1.00
a
1.00
1.00
0.00
ZipException
1.00
1.00
0.00
g0$e
1.00
0.00
1.00
b
1.00
0.00
1.00
JsonDecodingException
1.00
0.00
1.00

Total:
844
655
196

G. Discussion

We observed that combining UI and intent fuzzing can
signiﬁcantly increase activity coverage, while there is only a
slight increase in line coverage (Figure 4 and Figure 5). This
is at least true for the Best conﬁguration and STOAT, while
MONKEY covers signiﬁcantly fewer activities. We believe that
the employed static analysis in MATE and STOAT helps in
targeting new activities, e.g., we can construct valid data URIs
backed by sample ﬁles, MONKEY cannot. The fact that random
exploration with a combined approach on MATE achieves a
similar performance as STOAT also suggests that the success
of STOAT is inﬂuenced more by the combination of UI events
and intents than the exploration algorithm. Although we can
likely explore more activities by sending intents, it seems like
we cannot dive deeper in these code parts. This may be due
to immediate crashes after entering a new activity, or simply
triggering the intent in the wrong app state.

Another drawback of a random driven exploration is that
we likely re-explore the same app states again and again,
hence ending up with the same crashes. Although we did

51


---

## Page 9

TABLE VI: Exceptions of Best conﬁguration compared to Only
UI and Only Intent.

Number of unique exceptions, where the number in parentheses indicates how
many exceptions are also covered by the Best conﬁguration. A similarity score
between the conﬁgurations is provided, which measures how many unique
exceptions lie in the intersection. The last column refers to the number of
unique exceptions exclusively appearing in the Best conﬁguration.

Exception Type
Unique Crashes
Similarity
New
Best
UI
Intent

NumberFormatException
290
347 (276)
5 (0)
79.08%
14
NullPointerException
118
55 (40)
52 (49)
83.18%
29
IllegalStateException
97
66 (42)
180 (25)
67.68%
30
IllegalArgumentException
82
92 (61)
24 (21)
78.22%
3
ActivityNotFoundException
64
71 (57)
24 (4)
83.56%
3
URISyntaxException
34
39 (34)
0 (0)
87.18%
0
RuntimeException
32
39 (26)
1 (1)
67.5%
5
ClassCastException
27
2 (1)
24 (23)
92.31%
3
OutOfMemoryError
14
2 (2)
152 (8)
166.67%
4
IndexOutOfBoundsException
13
6 (2)
7 (7)
100.0%
4
NoSuchMethodException
11
9 (8)
0 (0)
88.89%
3
ClassNotFoundException
6
4 (3)
16 (3)
85.71%
0
FileNotFoundException
5
0 (0)
2 (2)
100.0%
3
JSONException
5
1 (1)
6 (4)
166.67%
0
StringIndexOutOfBoundsException
5
8 (1)
0 (0)
12.5%
4
SecurityException
4
0 (0)
0 (0)
0.0%
4
FileUriExposedException
4
2 (3)
1 (1)
133.33%
0
NotSerializableException
4
0 (0)
0 (0)
0.0%
4
Resources$NotFoundException
3
1 (1)
4 (2)
150.0%
0
JavascriptException
3
1 (1)
0 (0)
100.0%
2
UnsupportedOperationException
3
4 (1)
2 (2)
50.0%
0
ArrayIndexOutOfBoundsException
2
2 (2)
0 (0)
100.0%
0
CursorIndexOutOfBoundsException
2
1 (1)
1 (1)
100.0%
0
NotImplementedError
2
0 (0)
2 (2)
100.0%
0
GlideException
1
0 (0)
0 (0)
0.0%
1
ServiceSpeciﬁcException
1
0 (0)
0 (0)
0.0%
1
JsonDecodingException
1
0 (0)
1 (1)
100.0%
0
TypeCastException
1
0 (0)
1 (1)
100.0%
0
ArithmeticException
1
0 (0)
1 (1)
100.0%
0
WriteError
1
0 (0)
0 (0)
0.0%
1
b
1
0 (0)
1 (1)
100.0%
0
g0$e
1
0 (0)
1 (1)
100.0%
0
SQLiteConstraintException
1
0 (0)
0 (0)
0.0%
1
ZipException
1
1 (1)
0 (0)
100.0%
0
SQLiteException
1
0 (0)
0 (0)
0.0%
1
ViewRootImpl$CalledFromWrongThreadException
1
2 (1)
0 (0)
50.0%
0
UninitializedPropertyAccessException
1
0 (0)
1 (1)
100.0%
0
a
1
1 (0)
0 (0)
0.0%
1
InsufﬁcientAccessException
0
2 (0)
0 (0)
0.0%
0
StackOverﬂowError
0
2 (0)
0 (0)
0.0%
0
NoClassDefFoundError
0
1 (0)
0 (0)
0.0%
0
NoSuchMethodError
0
1 (0)
0 (0)
0.0%
0
CursorWindowAllocationException
0
0 (0)
1 (0)
0.0%
0
RejectedExecutionException
0
0 (0)
1 (0)
0.0%
0

Total:
844
762 (565)
511 (161)
57.03%
121

not state the total numbers of exceptions explicitly, those
are a magnitude higher than the unique exceptions. Thus, it
appears that without any guidance the exploration gets stuck.
We suggest combining UI inputs and intents with a search-
based exploration or reinforcement learning based approaches.

One might speculate that UI crashes are more “realistic”
since they represent interactions with a user, while intents
are generated by other programs. For example, a fundamental
difference is that most UI events are discrete events without
parameters: a click on a widget may occur or not occur, and
only few events take parameters such as text input. In contrast,
intents are assembled programmatically, possibly including
values that may later cause problems while being processed.

To better understand what types of faults our intent fuzzer
could reveal, consider the different ways in which an intent ob-
ject may lead to crashes. An intent consists of six components:
Action, data, categories, type, component, and extras. Table VII
enumerates for these components possible value types as well
as potential faults and failures, respectively. Most faults are
already prevented by intent ﬁlters (assuming implicit intents) or

52

TABLE VII: Possible failures caused by generated intents.

Intent attribute, possible values, potential fault, and possible resulting failures.

Intent component
Value type
Potential fault
Potential Failure

Action
Missing
Prevented by MATE and intent ﬁlter
Action
Invalid
Prevented by MATE and intent ﬁlter
Action
Valid
Program logic
Any
Categories
Missing
Prevented by MATE and intent ﬁlter
Categories
Invalid
Prevented by MATE and intent ﬁlter
Categories
Valid
Program logic
Any
Data
Missing
Missing check
NPE (explicit intent)
Data
Missing
Prevented by intent ﬁlter (implicit intent)
Data
Invalid URI
Prevented by MATE and intent ﬁlter
Data
Valid URI, missing ﬁle
Missing check
FileNotFoundException
Data
Valid URI, invalid ﬁle
Missing check
Any
Data
Valid
Program logic
Any
Type
Omitted
Missing check
NPE (explicit intent)
Type
Omitted
Prevented by intent ﬁlter (implicit intent)
Type
Wrong
Prevented by MATE and intent ﬁlter
Type
Valid
Unlikely to cause a problem
Component
Missing
Prevented by MATE
Component
Non-existent
Prevented by MATE
Component
Wrong
Prevented by MATE
Extra
Missing key
Missing check
NullPointerException
Extra
Wrong type
Prevented by MATE
Extra
Valid type
Program logic
Any

by MATE’s intent generation strategy. For instance, a missing
action is prevented in both ways: Implicit intents without action
would not get past the intent ﬁlter, and MATE’s intent generator
prevents sending explicit intents with missing actions. It is still
possible to trigger a failure if the implemented program logic
handles a valid action incorrectly. A similar behavior can be
observed for the categories of an intent. In contrast, assuming
that we sent an explicit intent without a URI although one
was expected, then this could lead to a NullPointerException
if no check was applied. If the same intent would have been
sent implicitly, the corresponding intent ﬁlter would deny the
intent. A typical fault constitutes a valid URI, which refers
to a non-existent or invalid ﬁle. As our intent generator omits
the type attribute, the target component could crash with a
NullPointerException if no check is applied. This is only the case
for an explicit intent, otherwise the intent ﬁlter would complain.
However, this is typically not the case, since the mime type is
mostly derived from the URI and either not speciﬁed in the
intent ﬁlter at all or left untouched. The component attribute is
only relevant for explicit intents. Our intent generator prevents
the misuse of a non-existent, missing or wrong component
attribute. Lastly, extras missing keys or deﬁning unexpected
types may cause crashes, while correct values for expected
keys may cause any behavior in the program logic.

Overall, we could treat all generated intents as implicit ones
and almost all would pass the corresponding intent ﬁlters,
thus reaching the target component. Consequently, all crashes
observed in our experiments are “real” crashes, in the sense that
the app may crash in the wild under the same circumstances.
Although we cannot conﬁrm the causes for all AUTs manually,
it is nevertheless likely that many observed crashes are due to
missing checks in the intent handling code (Table VII) rather
than deeper nested in the code. However, this is precisely one
of the objectives of fuzzing—since the AUT deﬁnes a matching
intent-ﬁlter it should be able to handle all valid intents.


---

## Page 10

V. RELATED WORK

In this paper we described and evaluated a general framework
for Android fuzzing using UI inputs and intents. Several other
Android testing tools have combined different types of events.

ANDROID MONKEY [44] is a built-in tool of the Android
SDK and has been widely used by mobile developers. It
generates (pseudo) random input events and allows users to
adjust the percentage of types of events generated. Monkey
can also trigger system key events and send intents to start
activities. However, it is neither possible to target services or
broadcast receivers, nor to control how the intents look like
apart from specifying a set of categories for the activities.

ACTEVE++ [31] adopts a similar strategy to Monkey: It
generates user inputs and leverages information collected during
static analysis to produce intents that start different activities
within the AUT. It can handle broadcast receivers by hooking
speciﬁc framework methods; this also includes dynamic broad-
cast registers that are programmatically deﬁned. In contrast,
we extract information about all types of components including
dynamic receivers via static analysis of the manifest and the
bytecode. Also, ACTEve++ lacks the support to target services.

DYNODROID [9] analyzes information on the GUI and the
source code to identify relevant user inputs and system inputs,
and can generate both by setting ﬁxed priorities for each event
type. In our approach, the probability of selecting a system
or UI event can be tuned. DYNODROID modiﬁes the Android
SDK for retrieving information about services and broadcast
receivers, while we only apply static analysis to the APK ﬁle.

SAPIENZ [5] generates test sequences based on random
fuzzing, systematic and search-based exploration. For generat-
ing user inputs, Sapienz uses atomic events (e.g., click, pinch
zoom, system events) and motif patterns that combine different
atomic events. Unlike our approach, it does not target activities,
services or broadcast receivers by intents.

CRASHSCOPE [32] is primarily used to reveal crashes
and provide in such a case detailed bug reports including
screenshots and replayable scripts. It leverages static and
dynamic analyses to guide the systematic exploration. Although
it does not support intents, CRASHSCOPE can test contextual
features, e.g., the screen rotation. Our approach can also change
the orientation of the screen by using system events and similar
to CRASHSCOPE, we only require the APK ﬁle as input.

STOAT [6] uses dynamic analysis to construct a stochastic
ﬁnite state machine based on only UI events, for which a
probability is assigned and updated based on their execution
frequency. Next, it generates test sequences with only UI events
and then randomly injects system-level events. In contrast, our
approach deﬁnes different probabilities for selecting either a
UI-level or a system-level event to create a test sequence;
STOAT injects system events in predeﬁned UI test sequences.

Although many of these approaches combining the automatic
generation of user and system events have been shown to be
effective, it remains unclear what is the contribution of system
events, in particular intents, in terms of crashes revealed, and
how to balance these aspects during test generation.

VI. CONCLUSIONS

Automated testing of Android apps is a thoroughly studied
ﬁeld of research, with countless tools and prototypes available.
Most of these tools focus on sending user inputs to the AUT,
although some of the approaches also integrate system events
in terms of intents. In this paper, we took a closer look at how
to combine user-inputs and intents, and what the effects are.

Our experiments show that Android fuzzing is better done
with a combination of different types of inputs. This can
increase the number of identiﬁed distinct crashes considerably:
In our experiments on 500 apps from F-Droid, the combined
approach found a total of 844 unique crashes, whereas sending
only user-inputs revealed only 762, and sending only intents
revealed 511 crashes. The combined approach also achieves a
higher activity coverage (78.07%) than using only user inputs
(70.45%) and sending only intents (58.23%).

Although we provide a general framework for combining UI
inputs and intents, there is potential to improve our intent
generation implementation: For example, as we statically
extract the dynamic receivers, we cannot guarantee they are still
registered at the moment they are targeted with intents. This
could be overcome by monitoring registration by instrumenting
the AUT. A general limitation lies in the pool of ﬁles for various
common data types, which can be extended to generate more
valid URIs [35]. In our current prototype the broadcasting of a
system event notiﬁcation is purely random, however sending for
instance a BOOT_COMPLETED message should only happen
right after the boot process has been completed. In that sense,
we do not consider system event constraints. We do not enforce
a timeout between two consecutive actions, except when a
progress bar is detected. This may affect test effectiveness [16]
although the discussion of how to deﬁne such timeouts and
their effects is quite controversial [45]. Different types of inputs
may require different timeouts, requiring further research.

When combining user-inputs and intents, it is important to
balance the two carefully: Our experiments show that sending
too many or too few intents can be harmful; future work should
investigate how this result is inﬂuenced by other optimizations
to Android testing—for example, use of meta-heuristic search
algorithms. An aspect of interest for further investigation is
the observed difference in the crashes resulting from sending
intents vs. sending user inputs: Intents are prone to causing
crashes that reveal weaknesses in how event handlers process
intents, since developers may make assumptions about the
validity of the intents. This also suggests that future research
on Android testing should maybe not blindly count the number
of crashes, but also report in more detail on the types of crashes.

To
make
our
results
convenient
to
reproduce,
we
provide
a
replication
package
that
contains
all
case
studies,
the
tool
implementation,
and
the
raw
results
of
our
study.
The
replication
package
can
be
found
on
our
supplementary
Web
page
at https://ﬁgshare.com/articles/dataset/replication_zip/21378780.

ACKNOWLEDGEMENTS

This work is supported by DFG project FR2955/4-1 “STUNT:
Improving Software Testing Using Novelty”. 53


---

## Page 11

REFERENCES

[1] S. R. Choudhary, A. Gorla, and A. Orso, “Automated test input generation

for android: Are we there yet? (e),” in 2015 30th IEEE/ACM International
Conference on Automated Software Engineering (ASE), Nov 2015, pp.
429–440.
[2] P. Tramontana, D. Amalﬁtano, N. Amatucci, and A. R. Fasolino,

“Automated functional testing of mobile applications: a systematic

mapping study,” Software Quality Journal, vol. 27, no. 1, pp.
149–201,
Mar 2019.
[Online].
Available: https://doi.org/10.1007/
s11219-018-9418-6
[3] P. Kong, L. Li, J. Gao, K. Liu, T. F. Bissyandé, and J. Klein,

“Automated testing of android apps: A systematic literature review,” IEEE

Transactions on Reliability, vol. 68, no. 1, pp. 45–66, March 2019.
[4] A. K. Maji, F. A. Arshad, S. Bagchi, and J. S. Rellermeyer, “An empirical

study of the robustness of inter-component communication in android,”
in IEEE/IFIP International Conference on Dependable Systems and
Networks (DSN 2012), June 2012, pp. 1–12.
[5] K. Mao, M. Harman, and Y. Jia, “Sapienz: Multi-objective automated

testing for android applications,” in Proceedings of the 25th International
Symposium on Software Testing and Analysis, ser. ISSTA 2016.
New York, NY, USA: ACM, 2016, pp. 94–105. [Online]. Available:
http://doi.acm.org/10.1145/2931037.2931054
[6] T. Su, G. Meng, Y. Chen, K. Wu, W. Yang, Y. Yao, G. Pu,

Y. Liu, and Z. Su, “Guided, stochastic model-based gui testing of
android apps,” in Proceedings of the 2017 11th Joint Meeting on
Foundations of Software Engineering, ser. ESEC/FSE 2017.
New
York, NY, USA: ACM, 2017, pp. 245–256. [Online]. Available:
http://doi.acm.org/10.1145/3106237.3106298
[7] S. Rasthofer, S. Arzt, S. Triller, and M. Pradel, “Making malory behave

maliciously: Targeted fuzzing of android execution environments,” in
2017 IEEE/ACM 39th International Conference on Software Engineering
(ICSE), 2017, pp. 300–311.
[8] K. Choi, M. Ko, and B. Chang, “A practical intent fuzzing tool for

robustness of inter-component communication in android apps,” TIIS,
vol. 12, no. 9, pp. 4248–4270, 2018.
[9] A. Machiry, R. Tahiliani, and M. Naik, “Dynodroid: An input generation

system for android apps,” in Proceedings of the 2013 9th Joint
Meeting on Foundations of Software Engineering, ser. ESEC/FSE 2013.
New York, NY, USA: ACM, 2013, pp. 224–234. [Online]. Available:
http://doi.acm.org/10.1145/2491411.2491450
[10] M. M. Eler, J. M. Rojas, Y. Ge, and G. Fraser, “Automated accessibility

testing of mobile apps,” in ICST.
IEEE Computer Society, 2018, pp.
116–126.
[11] A. D. Docs. App components. [Online]. Available: https://developer.

android.com/guide/components/fundamentals#Components
[12] ——. Understand the activity lifecycle. [Online]. Available: https:

//developer.android.com/guide/components/activities/activity-lifecycle
[13] ——. Intent. [Online]. Available: https://developer.android.com/reference/

android/content/Intent
[14] R. Hay, O. Tripp, and M. Pistoia, “Dynamic detection of inter-application

communication vulnerabilities in android,” in Proceedings of the 2015
International Symposium on Software Testing and Analysis, ser. ISSTA
2015.
New York, NY, USA: ACM, 2015, pp. 118–128. [Online].
Available: http://doi.acm.org/10.1145/2771783.2771800
[15] S.
Zein,
N.
Salleh,
and
J.
Grundy,
“A
systematic
mapping
study of mobile application testing techniques,” J. Syst. Softw.,
vol. 117, no. C, pp. 334–356, Jul. 2016. [Online]. Available:
https://doi.org/10.1016/j.jss.2016.03.065
[16] D. Amalﬁtano, A. Fasolino, P. Tramontana, S. Carmine, and A. Memon,

“Using gui ripping for automated testing of android applications,”

2012 27th IEEE/ACM International Conference on Automated Software
Engineering, ASE 2012 - Proceedings, 09 2012.
[17] A. Machiry, R. Tahiliani, and M. Naik, “Dynodroid: An input generation

system for android apps,” in Proceedings of the 2013 9th Joint
Meeting on Foundations of Software Engineering, ser. ESEC/FSE 2013.
New York, NY, USA: ACM, 2013, pp. 224–234. [Online]. Available:
http://doi.acm.org/10.1145/2491411.2491450
[18] D. Amalﬁtano, A. R. Fasolino, P. Tramontana, B. D. Ta, and

A. M. Memon, “Mobiguitar: Automated model-based testing of mobile
apps.” IEEE Software, vol. 32, no. 5, pp. 53–59, 2015. [Online].
Available: http://dblp.uni-trier.de/db/journals/software/software32.html#
AmalﬁtanoFTTM15
[19] Y. Li, Z. Yang, Y. Guo, and X. Chen, “Droidbot: a lightweight

ui-guided test input generator for android.” in ICSE (Companion

54

Volume), S. Uchitel, A. Orso, and M. P. Robillard, Eds.
IEEE
Computer
Society,
2017,
pp.
23–26.
[Online].
Available:
http:
//dblp.uni-trier.de/db/conf/icse/icse2017c.html#LiYGC17
[20] T. Azim and I. Neamtiu, “Targeted and depth-ﬁrst exploration for

systematic testing of android apps,” SIGPLAN Not., vol. 48, no. 10,
pp. 641–660, Oct. 2013. [Online]. Available: http://doi.acm.org/10.1145/
2544173.2509549
[21] C. Sun, Z. Zhang, B. Jiang, and W. K. Chan, “Facilitating monkey test

by detecting operable regions in rendered gui of mobile game apps,” in
2016 IEEE International Conference on Software Quality, Reliability
and Security (QRS), Aug 2016, pp. 298–306.
[22] W. Choi, G. Necula, and K. Sen, “Guided gui testing of android

apps with minimal restart and approximate learning,” SIGPLAN
Not., vol. 48, no. 10, pp. 623–640, Oct. 2013. [Online]. Available:
http://doi.acm.org/10.1145/2544173.2509552
[23] N. P. B. Jr., J. Hotzkow, and A. Zeller, “Droidmate-2: a platform

for android test generation,” in Proceedings of the 33rd ACM/IEEE
International Conference on Automated Software Engineering, ASE
2018, Montpellier, France, September 3-7, 2018, 2018, pp. 916–919.
[Online]. Available: https://doi.org/10.1145/3238147.3240479
[24] S. Hao, B. Liu, S. Nath, W. G. Halfond, and R. Govindan, “Puma:

Programmable ui-automation for large-scale dynamic analysis of mobile
apps,” in Proceedings of the 12th Annual International Conference
on Mobile Systems, Applications, and Services, ser. MobiSys ’14.
New York, NY, USA: ACM, 2014, pp. 204–217. [Online]. Available:
http://doi.acm.org/10.1145/2594368.2594390
[25] N. Mirzaei, J. Garcia, H. Bagheri, A. Sadeghi, and S. Malek, “Reducing

combinatorics in gui testing of android applications,” in Proceedings
of the 38th International Conference on Software Engineering, ser.
ICSE ’16.
New York, NY, USA: ACM, 2016, pp. 559–570. [Online].
Available: http://doi.acm.org/10.1145/2884781.2884853
[26] Z. Shan, T. Azim, and I. Neamtiu, “Finding resume and restart

errors in android applications,” in Proceedings of the 2016 ACM
SIGPLAN International Conference on Object-Oriented Programming,
Systems, Languages, and Applications, ser. OOPSLA 2016.
New
York, NY, USA: ACM, 2016, pp. 864–880. [Online]. Available:
http://doi.acm.org/10.1145/2983990.2984011
[27] R. Mahmood, N. Mirzaei, and S. Malek, “Evodroid: Segmented evolu-

tionary testing of android apps,” in 22nd ACM SIGSOFT International
Symposium on the Foundations of Software Engineering (FSE 2014),
Hong Kong, China, November 2014, pp. 599–609.
[28] W. Song, X. Qian, and J. Huang, “Ehbdroid: Beyond gui testing

for android applications,” in Proceedings of the 32Nd IEEE/ACM
International Conference on Automated Software Engineering, ser. ASE
2017.
Piscataway, NJ, USA: IEEE Press, 2017, pp. 27–37. [Online].
Available: http://dl.acm.org/citation.cfm?id=3155562.3155570
[29] Y. Lu, M. Pan, J. Zhai, T. Zhang, and X. Li, “Preference-wise testing

for android applications,” in Proceedings of the 2019 27th ACM Joint
Meeting on European Software Engineering Conference and Symposium
on the Foundations of Software Engineering, ser. ESEC/FSE 2019.
New York, NY, USA: ACM, 2019, pp. 268–278. [Online]. Available:
http://doi.acm.org/10.1145/3338906.3338980
[30] S. Anand, M. Naik, M. J. Harrold, and H. Yang, “Automated concolic

testing of smartphone apps,” in Proceedings of the ACM SIGSOFT 20th
International Symposium on the Foundations of Software Engineering,
ser. FSE ’12.
New York, NY, USA: ACM, 2012, pp. 59:1–59:11.
[Online]. Available: http://doi.acm.org/10.1145/2393596.2393666
[31] J. Qin, H. Zhang, S. Wang, Z. Geng, and T. Chen, “Acteve++: An

improved android application automatic tester based on acteve,” IEEE
Access, vol. 7, pp. 31 358–31 363, 2019.
[32] K. Moran, M. Linares-Vásquez, C. Bernal-Cárdenas, C. Vendome, and

D. Poshyvanyk, “Crashscope: A practical tool for automated testing
of android applications,” in Proceedings of the 39th International
Conference on Software Engineering Companion, ser. ICSE-C ’17.
Piscataway, NJ, USA: IEEE Press, 2017, pp. 15–18. [Online]. Available:
https://doi.org/10.1109/ICSE-C.2017.16
[33] L. Sell, M. Auer, C. Frädrich, M. Gruber, P. Werli, and G. Fraser, “An

empirical evaluation of search algorithms for app testing,” in ICTSS, ser.
Lecture Notes in Computer Science, vol. 11812.
Springer, 2019, pp.
123–139.
[34] H. van der Merwe, B. van der Merwe, and W. Visser, “Verifying

android applications using java pathﬁnder,” SIGSOFT Softw. Eng.
Notes, vol. 37, no. 6, pp. 1–5, Nov. 2012. [Online]. Available:
http://doi.acm.org/10.1145/2382756.2382797


---

## Page 12

[35] H. Ye, S. Cheng, L. Zhang, and F. Jiang, “Droidfuzzer: Fuzzing the

android apps with intent-ﬁlter tag,” in Proceedings of International
Conference on Advances in Mobile Computing &#38; Multimedia, ser.
MoMM ’13.
New York, NY, USA: ACM, 2013, pp. 68:68–68:74.
[Online]. Available: http://doi.acm.org/10.1145/2536853.2536881
[36] K. Yang, J. Zhuge, Y. Wang, L. Zhou, and H. Duan, “Intentfuzzer:

Detecting capability leaks of android applications,” in Proceedings of the
9th ACM Symposium on Information, Computer and Communications
Security, ser. ASIA CCS ’14. New York, NY, USA: ACM, 2014, pp. 531–
536. [Online]. Available: http://doi.acm.org/10.1145/2590296.2590316
[37] T. Wu and Y. Yang, “Crafting intents to detect icc vulnerabilities of

android apps,” in 2016 12th International Conference on Computational
Intelligence and Security (CIS), Dec 2016, pp. 557–560.
[38] R. Sasnauskas and J. Regehr, “Intent fuzzer: Crafting intents of

death,” in Proceedings of the 2014 Joint International Workshop on
Dynamic Analysis (WODA) and Software and System Performance
Testing, Debugging, and Analytics (PERTEA), ser. WODA+PERTEA
2014.
New York, NY, USA: ACM, 2014, pp. 1–5. [Online]. Available:
http://doi.acm.org/10.1145/2632168.2632169
[39] A. K. Jha, S. Lee, and W. J. Lee, “Modeling and test case generation

of inter-component communication in android,” in Proceedings of
the Second ACM International Conference on Mobile Software
Engineering
and
Systems,
ser.
MOBILESoft
’15.
Piscataway,
NJ, USA: IEEE Press, 2015, pp. 113–116. [Online]. Available:

http://dl.acm.org/citation.cfm?id=2825041.2825061
[40] L. V. Haoyin, “Automatic android application gui testing—a random walk

approach,” in 2017 International Conference on Wireless Communications,
Signal Processing and Networking (WiSPNET), 2017, pp. 72–76.
[41] T. Su, L. Fan, S. Chen, Y. Liu, L. Xu, G. Pu, and Z. Su, “Why my app

crashes? understanding and benchmarking framework-speciﬁc exceptions
of android apps,” IEEE Transactions on Software Engineering, vol. 48,
no. 4, pp. 1115–1137, 2022.
[42] T. Su, J. Wang, and Z. Su, “Benchmarking automated gui testing for

android against real-world bugs,” in Proceedings of the 29th ACM Joint
Meeting on European Software Engineering Conference and Symposium
on the Foundations of Software Engineering, ser. ESEC/FSE 2021.
New York, NY, USA: Association for Computing Machinery, 2021, p.
119–130. [Online]. Available: https://doi.org/10.1145/3468264.3468620
[43] A. Vargha and H. D. Delaney, “A critique and improvement of the cl

common language effect size statistics of mcgraw and wong,” Journal
of Educational and Behavioral Statistics, vol. 25, no. 2, pp. 101–132,
2000.
[44] A. D. Docs. Ui/application exerciser monkey. [Online]. Available:

https://developer.android.com/studio/test/monkey
[45] B. Jiang, Y. Zhang, W. K. Chan, and Z. Zhang, “A systematic study on

factors impacting gui traversal-based test case generation techniques for
android applications,” IEEE Transactions on Reliability, vol. 68, no. 3,
pp. 913–926, 2019.

55


---

## Page 13


---

## Page 14

6 Exploring Android Apps Using Motif
Actions

Michael Auer and Gordon Fraser.
‘Exploring Android Apps Using Motif Actions’.
In: International Conference on Automated Software Engineering Workshops (ASEW).
Kirchberg, Luxembourg: IEEE, Sept. 2023, pp. 135–142. doi: 10.1109/ASEW60602.
2023.00023

Conceptualization

Formal analysis

Methodology

Investigation

Validation

Authors

Software

Writing - Review & Editing

Writing - Original Draft

Project administration

Funding acquisition

Data Curation

Visualization

Supervision

Resources

57

Table 6.1 enumerates for each author the contributions according to the Contributor
Roles Taxonomy.

Tabelle 6.1: Contributions of each author according to the Contributor Roles Taxonomy.

Michael Auer
X
X
X
X
X
X
X
X
X
X
X
X
X
Gordon Fraser
X
X
X
X
X
X


---
