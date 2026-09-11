---year: 2013

secverify_category: "Legacy"
categories:
  - "[[2A.1-Web與API動態漏洞掃描 (DAST)]]"
  - "[[2B.1-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]"
title: "29_Machiry_et_al.,_Dynodroid_Input_Generation_System"
creator: "TeX"
pages: 11
source: "Dynodroid (2013) Input Generation System for Android Apps.pdf"
---

# Dynodroid (2013) Input Generation System for Android Apps

> **文獻存檔**：[PDF 原文](<../../raw-papers/2010-2019/Dynodroid (2013) Input Generation System for Android Apps.pdf>) | [Markdown 原文](<../../raw-papers/2010-2019/Dynodroid (2013) Input Generation System for Android Apps (Raw).md>)

> **總頁數**：11 頁

---

## Page 1

Dynodroid: An Input Generation System for Android Apps

Aravind Machiry Rohan Tahiliani Mayur Naik

Georgia Institute of Technology, USA

{amachiry, rohan_tahil, naik}@gatech.edu

| ABSTRACT | What-if analyses of programs are broadly classified into |  |  |
| --- | --- | --- | --- |
| We present a system Dynodroid for generating relevant in- | static and dynamic. Static analyses are hindered by features |  |  |
| puts to unmodified Android apps. Dynodroid views an app | commonly used by mobile apps such as code obfuscation, na- |  |  |
| as an event-driven program that interacts with its environ- | tive libraries, and a complex SDK framework. As a result, |  |  |
| ment by means of a sequence of events through the Android | there is growing interest in dynamic analyses of mobile apps |  |  |
| framework. | By instrumenting the framework once and for | (e.g., [1, 12, 13, 25]). | A key challenge to applying dynamic |
| all, Dynodroid monitors the reaction of an app upon each | analysis ahead-of-time, however, is obtaining program in- |  |  |
| event in a lightweight manner, using it to guide the gener- | puts that adequately exercise the program’s functionality. |  |  |
| ation of the next event to the app. | Dynodroid also allows | We set out to build a system for generating inputs to |  |
| interleaving events from machines, which are better at gen- | mobile apps on Android, the dominant mobile app platform, |  |  |
| erating a large number of simple inputs, with events from | and identified five key criteria that we felt such a system |  |  |
| humans, who are better at providing intelligent inputs. | must satisfy in order to be useful: |  |  |

We evaluated Dynodroid on 50 open-source Android apps,

| and compared it with two prevalent approaches: users man- | • | Robust | : Does the system handle real-world apps? |  |
| --- | --- | --- | --- | --- |
| ually exercising apps, and Monkey, a popular fuzzing tool. | • | Black-box | : | Does the system forgo the need for app |
| Dynodroid, humans, and Monkey covered 55%, 60%, and | sources and the ability to decompile app binaries? |  |  |  |
| 53%, respectively, of each app’s Java source code on average. | • | Versatile | : | Is the system capable of exercising impor- |
| Monkey took 20X more events on average than Dynodroid. | tant app functionality? |  |  |  |
| Dynodroid also found 9 bugs in 7 of the 50 apps, and 6 bugs | • | Automated | : Does the system reduce manual effort? |  |

in 5 of the top 1,000 free apps on Google Play.

• Efficient : Does the system generate concise inputs, i.e.,

Categories and Subject Descriptors avoid generating redundant inputs?

D.2.5 [ Software Engineering ]: Testing and Debugging

This paper presents a system Dynodroid that satisfies

General Terms the above criteria. Dynodroid views a mobile app as an

event-driven program that interacts with its environment by

Reliability, Experimentation means of a sequence of events. The main principle under-

Keywords lying Dynodroid is an observe-select-execute cycle, in which

it first observes which events are relevant to the app in the

GUI testing, testing event-driven programs, Android current state, then selects one of those events, and finally

executes the selected event to yield a new state in which

| 1. | INTRODUCTION | it repeats this process. | This cycle is relatively straightfor- |  |
| --- | --- | --- | --- | --- |
| Mobile apps—programs that run on advanced mobile de- | ward for | UI events | —inputs delivered via the program’s user |  |
| vices such as smartphones and tablets—are becoming in- | interface (UI) such as a tap or a gesture on the device’s |  |  |  |
| creasingly prevalent. Unlike traditional enterprise software, | touchscreen. | In the | observer | stage, Dynodroid determines |
| mobile apps serve a wide range of users in heterogeneous and | the layout of widgets on the current screen and what kind |  |  |  |
| demanding conditions. As a result, mobile app developers, | of input each widget expects. | In the | selector | stage, Dyno- |
| testers, marketplace auditors, and ultimately end users can | droid uses a novel randomized algorithm to select a widget |  |  |  |
| benefit greatly from what-if analyses of mobile apps. | in a manner that penalizes frequently selected widgets with- |  |  |  |

out starving any widget indefinitely. Finally, in the executor

stage, Dynodroid exercises the selected widget.

In practice, human intelligence may be needed for exer-

| Permission to make digital or hard copies of all or part of this work for | cising certain app functionality, in terms of generating both |  |
| --- | --- | --- |
| personal or classroom use is granted without fee provided that copies are | individual events (e.g., inputs to text boxes that expect valid |  |
| not made or distributed for profit or commercial advantage and that copies | passwords) and sequences of events (e.g., a strategy for win- |  |
| bear this notice and the full citation on the first page. To copy otherwise, to | ning a game). | For this reason, Dynodroid allows a user to |
| republish, to post on servers or to redistribute to lists, requires prior specific | observe an app reacting to events as it generates them, and |  |

permission and/or a fee.

ESEC/FSE ’13, August 18-26, 2013, Saint Petersburg, Russia lets the user pause the system’s event generation, manually

Copyright 2013 ACM 978-1-4503-2237-9/13/08 ...$15.00. generate arbitrary events, and resume the system’s event

---

## Page 2

| generation. Our overall system thereby combines the bene- | 1. We propose an effective approach for generating in- |  |  |
| --- | --- | --- | --- |
| fits of both the automated and manual approaches. | puts to mobile apps. It is based on a “observe-select- |  |  |
| We discussed how Dynodroid handles UI events, but sig- | execute” principle that efficiently generates a sequence |  |  |
| nificant functionality of mobile apps is controlled by non-UI | of relevant events. | To adequately exercise app func- |  |
| events we call | system events | , such as an incoming SMS mes- | tionality, it generates both UI and system events, and |
| sage, a request by another app for the device’s audio, or a | seamlessly combines events from human and machine. |  |  |
| notification of the device’s battery power running low. Sat- | 2. We show how to observe, select, and execute system |  |  |
| isfying our five desirable criteria in the presence of system | events for Android in a mobile device emulator with- |  |  |
| events is challenging for two reasons. | First, the number of | out modifying the app. | The central insight is to tai- |
| possible system events is very large, and it is impractical to | lor these tasks to the vast common framework against |  |  |
| generate all possible permutations of those events. | For in- | which all apps are written and from which they pri- |  |
| stance, Android supports 108 different broadcast receivers, | marily derive their functionality. |  |  |
| each of which can send notifications called | intents | to an app. | 3. We present extensive empirical evaluation of the sys- |
| Second, many system events have structured data that must | tem, comparing it to the prevalent approaches of man- |  |  |
| be constructed and dispatched correctly to the app along- | ual testing and automated fuzzing, using metrics in- |  |  |
| side an intent. | For example, generating an incoming SMS | cluding code coverage and number of events, for di- |  |
| message event entails constructing and sending a suitable | verse Android apps including both open-source apps |  |  |
| object of class | android.telephony.SmsMessage | . | and top free marketplace apps. |

A distinctive aspect of mobile apps is that all such apps,

Dynodroid addresses the problem of handling a very large

number of system events by using the observation that in

them we call relevant events. An event is relevant to an app

if the app has registered a listener for the event with the

framework. Finding when an app registers (or unregisters)

such a listener does not require modifying the app: it suf-

fices to instrument the framework once and for all. The ob-

server monitors the app’s interaction with the framework via

this instrumentation, and presents the selector only events

that the app has registered to listen. Finally, the executor

constructs any data associated with the selected event and

dispatches it to the app. A salient aspect of Dynodroid con-

cerns how it constructs this data. For instance, the listener

for network connectivity change events expects an object of

class android.net.NetworkInfo describing the new status

of the network interface. Dynodroid cannot arbitrarily cre-

ate such objects; it must obtain them from a pool maintained

by system service android.net.ConnectivityManager . Fi-

nally, whenever an event is executed, any previously relevant

event may become irrelevant and vice versa, for the next

observe-select-execute cycle.

We implemented Dynodroid for the Android platform and

applied it to 50 diverse, real-world, open-source apps. We

compared the performance of Dynodroid in terms of each

app’s Java source code coverage to two prevalent approaches:

one involving expert users manually exercising these apps,

and another using Monkey [7], a popular fuzzing tool. Dyno-

droid, humans, and Monkey covered 55%, 60%, and 53%

code, respectively, on average per app. Dynodroid was able

to cover 83% of the code covered by humans per app on av-

erage, showing its ability to automate testing. Also, Dyno-

droid achieved peak coverage faster than Monkey, with Mon-

key requiring 20X more events on average, showing the ef-

fectiveness of our randomized event selection algorithm. Fi-

nally, Dynodroid found 9 bugs in 7 of the 50 apps. In a

separate experiment, we applied Dynodroid to the top 1,000

free apps in Google Play, and it found 6 bugs in 5 of them.

We summarize the main contributions of our work:

Section 8 concludes.

This section presents the system architecture of Dyno-

droid. Algorithm 1 shows the overall algorithm of Dyno-

droid. It takes as input the number n of events to generate

to an app under test. It produces as output a list L of n

events it generates. The first generated event is to install and

start the app in a mobile device emulator. The remaining

n − 1 events are generated one at a time in an observe-select-

execute cycle. Each of these events constitutes either a UI

input or non-UI input to the app, which we call UI event

and system event , respectively. The two kinds of events are

conceptually alike: each event of either kind has a type and

associated data. We distinguish between them because, as

we explain below, Dynodroid uses different mechanisms to

handle them. The executor executes the current event, de-

noted e , in the current emulator state, denoted s , to yield a

new emulator state that overwrites the current state. Next,

the observer computes which events are relevant in the new

state. We denote the set of relevant events E . Finally, the

selector selects one of the events from E to execute next,

and the process is repeated.

Figure 1 presents a dataflow diagram of Dynodroid that

provides more details about the mechanisms it uses to im-

plement the executor , the observer , and the selector

on the Android platform.

The executor triggers a given event using the appropri-

ate mechanism based on the event kind. It uses the Android

Debug Bridge ( adb ) to send the event to an Android device

emulator that is running the app under test. For UI events,

the ADB host talks to the ADB daemon ( adbd ) on the emu-

lator via the monkeyrunner tool. Note that this tool, which

is used to send events to an emulator via an API, is unre-

lated to the Monkey fuzz testing tool, which runs in an adb

shell directly on the emulator. For system events, the ADB

host talks to the Activity Manager tool ( am ) on the emu-

lator, which can send system events as intents to running

apps. Section 3 describes the executor in further detail.

| regardless of how diverse their functionality, | are written | The rest of the paper is organized as follows. | Section 2 |
| --- | --- | --- | --- |
| against a common framework that implements a significant | describes the overall system. The next three sections present |  |  |
| portion of the app’s functionality. | Dynodroid exploits this | its three main parts: Section 3 the executor, Section 4 the |  |
| aspect pervasively in observing, selecting, and executing sys- | observer, and Section 5 the selector. Section 6 presents our |  |  |
| tem events, as we describe next. | experimental results. | Section 7 surveys related work and |  |
| practice, a mobile app reacts to only a small fraction of | 2. | SYSTEM ARCHITECTURE |  |

---

## Page 3

Ini=al(event( e (((install(and(start(app) %

(

(

(

e (is(system( (

App(under(test(

event(

| event( | ( |  |
| --- | --- | --- |
| Monkey( | ( | ADB(Host( |
| Runner( | ( | ADB(Daemon( |

(

(

Executor( Device(Emulator(

(

(

Figure 1 :

e := event to install and start app under test

append e to L

// Execute event e in current state s to yield updated state.

// Compute set E of all events relevant in current state s .

// Select an event e ∈ E to execute in next iteration.

e := selector ( E )

end for

The observer computes the set of events that are rele-

vant to the app under test in the current emulator state. It

consists of two parts to handle the two kinds of events: the

Hierarchy Viewer tool for UI events, and the instrumented

framework (SDK) for system events. Hierarchy Viewer pro-

vides information about the app’s GUI elements currently

displayed on the device’s screen. The observer computes

the set of relevant UI events E 1 from this information. The

instrumented SDK provides information about broadcast re-

ceivers and system services for which the app is currently

registered. The observer computes the set of relevant sys-

tem events E 2 from this information. It provides the set of

all relevant events E = E 1 ∪ E 2 to the selector . Section 4

provides more details about the observer .

The selector selects an event from E as the next event

to be triggered. Dynodroid implements various selection

strategies that one can choose from upfront, including deter-

ministic vs. randomized, and history dependent vs. history

manual input generation. Figure 2 shows how Dynodroid

allows switching between machine and human. The execu-

Selected(event( e (from( E%

Intercepted( System(

events(

calls(from(

apps(to(SDK( E2%

Selector(

Observer(

Hierarchy(

Viewer( UI(

events(

E1%

Dataflow diagram of Dynodroid for the Android platform.

start% START& human% machine%

console%commands%

events%to%app% final%

allows the human to exercise the app uninterrupted in the

emulator, until a RESUME command is received from the

console. At this point, the executor switches to machine

mode and generates events until the given bound n is reached

or a PAUSE command is received from the console. In the

latter case, the executor switches to human mode again.

Human inputs do not count towards the bound n . Also,

nothing prevents the human from exercising the app in ma-

chine mode as well, along with the machine. Finally, the

STOP command from the console stops Dynodroid.

The executor executes an event, chosen by the selec-

tor , on the emulator via the Android Debug Bridge ( adb ).

It uses separate mechanisms for executing UI events and sys-

tem events. UI events are triggered using the monkeyrunner

tool. This tool is a wrapper around adb that provides an

API to execute UI events. System events are triggered us-

ing the Activity Manager tool ( am ). Broadcast events of any

type can be triggered using this tool provided the correct

arguments are supplied.

4. OBSERVER

goal of the observer is to efficiently compute as small a

4.1 UI Events

| ( | Ac=vity( | Instrumented( | All(relevant( |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ( | Manager( | SDK( | events( |  |  |  |  |  |
| e | (is(UI( | ( | E | (=( | E1 | (U( | E2% |  |
| Algorithm 1 | Overall algorithm of Dynodroid. | RESUME& |  |  |  |  |  |  |
| INPUT: | Number | n > | 0 of events to generate. | emulator% |  |  |  |  |
| OUTPUT: | List | L | of | n | events. | human% | executor% |  |
| L | := empty list | state% | mode% | mode% |  |  |  |  |
| s | := initial program state | console% |  |  |  |  |  |  |
| for | i | from | 1 | to | n | do | state%transi1ons% | PAUSE& |
| s | := | executor | ( | e | , | s | ) | state% |
| E | := | observer | ( | s | ) | Figure 2 | : | State transition diagram of Dynodroid. |
| oblivious strategies. Section 5 describes these strategies and | The | observer | computes the set of relevant events after an |  |  |  |  |  |
| Section 6 evaluates them on a code coverage client for 50 | event is executed. We consider an event | relevant | if triggering |  |  |  |  |  |
| open-source apps. | it may result in executing code that is part of the app. The |  |  |  |  |  |  |  |
| 3. | EXECUTOR | set of relevant events as possible without missing any. This |  |  |  |  |  |  |
| Dynodroid allows both machine and human to generate | section describes how the | observer | computes relevant UI |  |  |  |  |  |
| events in order to combine the benefits of automated and | events (Section 4.1) and relevant system events (Section 4.2). |  |  |  |  |  |  |  |
| tor | listens to commands from a console and starts in | human | These are events generated by the SDK in response to |  |  |  |  |  |
| mode | , in which it does not trigger any events and instead | interaction by users with the device’s input mechanisms. |  |  |  |  |  |  |

![Page 3 Image](data:image/png;base64,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)

![Page 3 Image](data:image/png;base64,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)

![Page 3 Image](data:image/png;base64,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)

![Page 3 Image](data:image/png;base64,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)

![Page 3 Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHAAAABwCAYAAADG4PRLAAAOk0lEQVR4nO2dZ1MbSxOF+16bHCWCEdkEES2yRboYEDljc43v//8jb1F1uupUvzOrlbQooJmq+WCkFWaeOae7Z1czIqGFFlpooTVx+6uCHlqVWxSMv0vsAWoVWjFQn0z/HLPzNcXAhlZGcwGzkFrQW9HbTG83nV/Ta/QzLNgAs4xWDFqLAfUGpUNEOkWkC70bvcfT9fUuXNeJz2gnsBaoC2Zo1HzgLDSG9QajV0T6RKRfRFIikhaRAREZpD6Erv8eQE/jmn58jsK1QF0wA0g0C84HTZXViwFPA8awiHwRkYyIjIrImIiMi8gE+qTpE3h9DO9/u24En6NwU5gUPfi9CpOV6VJlU7Vi4NqhBIWWwuAOY8BHAWNKRL6KyKyIzInIvIhkRWRBRBYdfQE9i/fO4vopAB4D1C8AmnbAbGt2kD5wGtPUHvsJWgbKeRvoGcB6A7EkIisi8k1E1kRkXUQ2RGRTRLYcfRN9A+/PiciqiCwDsEKdxgQZJZgpTKZuAtnaTNbqUp0qTm1S1TaIgRsjaFkAW8Xgv4HYFpHvIrIrInsiciAihyLyD/oRdf3ZId63j2vyIrIDwOuYDMuYIApzHJNoiFTZHaHIDwfRpTq2yh4CN4IBm4YiFNo6gOUx8IcAcywipyJSEJEzETkXkQv0S+r6s3O8r4DrTkTkB+DuYzLsQKU5wMxiEk1ClcME0lrrh4LoU50mJ92wSgU3gZiUxcCtQRl5DK4CKwDEG5grEbkRkVsRuUO/p/6Azj+7w/vfrrsmwGcAeoQJsotJs45JtAhVKsghstYuSnY+hBqjVKd2OQCrHCdwK6S2PShDoV0QsDuAeRSRJ/RnEfkZoz+jP+F6BXxLQBnmPqx6ExbLIDOYgP0OW21YiC54VnVDmMVTsMplgNsBuCNY3Dmg3ZKiGNYvEXlB/9f039Tta3rNL3QF+0gqvcakKcBmD+AGm1DkAibeOCZiGhOzs5Eh+iyzE39cGn/sBOLKImLNtgF3gQG8I2gMzEJ6LaNbwC8emDekymOA/I4Jt4IJOEVq7HNYakNAdMFTy+zDH5ch1a1iNudhlScG3CMGkqFZYH8S6BaqhflEFntJitzHxMthIs4gcx5GbOyB6zDEv+sVog8eW+YYLEdVt4PZfAyrLAbOB+2/CnoUUIbJIG8w0U4x8fLIWpdRo06QpVqIn+pRiRZeK8FLYUaOI/Av449V1RUwq29hlQouClolwEoB6gP5SDHyDGrcQ8a8SpY6gkRN42JdQoxSXori3RzixSb+2B+kunuKcS81AhcHpoL8hYn2gIl3Afs/hKvkkOBMI2QMmOSmrmJiMXiTFO+2YZka61h11iprBS0KJCuSbfUOmXIBrvIdNeyiB2LdJDZx4X0jeKewzDuP6mqpuFJAsho1NqqlHiFErHsg2sSmJhD1l3Kp0IWEZRi2qfB2YC8FzFS1TBvr6hVcMZAvZKk3CA1HWMmxEG1i86kWmSnHvc9U5/URvLkIeJyoNBK4YhB/Gog/oMQ1xERNbNJwqnZHsV81gJxxdsAaBlEqzFLMU3jXBM9lmbUGkiTER6NEhZhFWPkCp+qipKZqmamNex2whAEsjc2gVNiimHf1AeFZkBwXLURNbL4hrEygLu7zJDXvCs9apyYtI/D5RdR5e8g2Pzq8KIhqpwU40TZKqVk41SDFw5ZqqJDhtTriXhZWkYf/X1C2aeHVesDfGyLHxGs40QHq4CWsSI1g8ndVoz60WWc7WSfHvR34/jnqvKcPkLBUAvEZDnSJJUPNTBcQD4eNlb5bQmOtU0sGtc4lzK4DSloemwyeD6IW+xeY3BoP1UoHIAbNShNXoVUfZ51snbuYZRz3tM5rFngWohb7jxQPD5DkLWHyc1b6LgmNL3HJIOtc8VhnM8S9KIAM8Scm9RVZ6Rqy0nFKaNqTTmh86huC+hbg6fsI1GqdP4111npAawmRrfSWSottlFw2oUlUha7Ylyb1rcLTNevkkqGZ4l4UxFdTH2pWukcFfpQKKwYYpb4NqK8Aj9fEpVmts5gKn01Co7WhqrA/yYzULpl1UdHOse8H0uT7YJ2RKvxNCY1VocZCzkgrtlG2T637BvGLsib2BfVFA1SIrEIbCzUjtXVhWckMJy+86vIFv2gZv/jIxL6gPj9ElwpPkJHmUBeO0t0KuzpTtvo4eRnFL8rhF5+Yoj2oLxoix8Jb3AA+xCLIAi1091Zqoz771ORFV13O8B+xmWetB6seu6suvEQOsUPJzBdKZsquCW32ae0zJC/lQ1QV6uqMJjM53AhXGy27JvRln5kY9tnsdV8cgKpCTWZcNjpYSTbqWjoboOxzI9hnIgDZRo/gast49ELvUnSYBe6SAbZT8T6JG7ZbSH8vgn2WBfCPJxvNY2VrxlPUx46DUfFvBUtnetfhIWSfZUF8pfVRvUuxj6LeFQdjr8q46r9+Wn35hvjHC9cvFP9qPTiN0KPi4AatjQ6UUw/6EphRzIw1Wvvk20ZBfeUB1Dh4gbC0hTA1ibBVciLjS2DGTAJzjpkTVl/KB6hx8IHqwW2TyPQ67tSXDNAW8CGBSQYiJzJ6o/e7KehLzkR9KzCcgR6FAj4xgC8xMtGSHjv0lRBTeIZjmwA+AGAo4MsDaDPRUySI+sBTppwlNQXYQgCHAZCX0GwJEQBWDrBAS2oKMFVqLcgAOwigXQO9CktoiQK8JYBcCyYKUO/AHweAiQH8NwBszF4VgO1FLDTEwMoBuixUbytVHAOjkpjLADBRgIknMa47EaGMSBbg74gywt6RKLsOdBXyYSUmWYCuQl6fE+2rpJC3N3N1Ke2Q1kIDwMoA+pbSppNYSlOAaSxmz+NZUHs3PgAsHZ5rMVuf1F5CzjFUyWJ21O2kPXqYN9xOKh9g1O2ksp+LiXNDNx/xQFOtB6cRuu+G7gHd0B0r94auEEB+pMJVC9pSIqgwPkBXBmofLUyV80iFjYOaifJDTeGeYGXw7CP2nMCsOh7ubS31q2ZRd+Xn6Ust9rGKYKPxAdr450tgKnqskOMgf6U6Kg4GFcYDaL8fcZDEA00WoisOTnm+mRRsNB483zOhfCO3ovjnslHXdwPt09nBRuMB9D2V7fqOYEU7ONldmez3I9RGwwO+8eG5Njyw9lnx9yIYYJSNLtG6KD9iGDY38AN8NfuoafaZpwXsTJK7VVgbtdkor8qEZCYanuvLnedYV96i7NN+qaWi/WJc2aiuynx1JDNBhX6AvGuTqo+/Xj1X6epLFES7wZ3d6MClwpCRutVnN/vZMslLotuMSEQyoyq022zdmb1Bm12FvtjH6pt3bHqX6E5Nvo3uxk0sPKGMNNSF/79s9mQ2NnBtePcu2066dqzgXXp1i+VDUxc2c0LjSlx4UwPNPOeqseVksc1e52AFebpL0cxW6tqpkHfu3Ufdt2gyz3fd9NXGwk46I2KK9srep43OXVb60SFaeLpkptb5D+2PNkNnSXS/54av4lFht9m5cIWOGjij7beaCSLHPbtbr1pnjvZGGzKnubzrGRK2LrQJjR728d1s/tosWy9beBz3TpDosXW6zo+oytEDrr2z9aykBdp+2e5c/1Eh/omAd2V2rNcNXvkYnsR36S0G0GelvAE6nx1x+YEh+uBp0sJnRqyaMyOqZp0uiHFOb9lEUhMHYiOCLAZPk5YdKhnsqS01O0/QlZXa85NWUB9GQWzUk1ziKE+P3MlFnJtUNet0AbTxUPcUHaIjV30QHyPODqw1nFLA8Yme9zHgpWp9cpkLousMQR/EY3N6p0JUS61XkH888FynePJRrFk6dq6u4DFEe2Y8HwTJhx/7zs91HXxcL7HRB04t85GOJz9BtrmNmKfKG/GcaF3zI1h9ENuNEseQ2Czh9hOfYH3lsNR6AGnBvRK4n+bY1XM4y745yXoy4jjyuoGnzQdRY+IonSG/RmfI64HIN47TrKt9FPkfj+I0SbGnV19SvNv1nCWfagR4YpIaa6d9yE4ziAdZzNItWOqR4zz5uCArger6DNfZ8b/ILu+M6g4wGfXU6hmEjWGKeXUPT5sPopYYWuxPUFxkNR6jdrpygPxlYDLQKKjF+qsDGlulC9wJVJdHXF+lZGUUk7UPk1cTlrqHx40haomhxX4Ks3MMlqpq3MCAHBJIVeQ9BvHZAZOBWqhRna9hpSm0J7LKa9j8KcDtIVHJQXWzmJQj5rz4Nke2WffwtFmIrSYuDhg1LiJz2zQgCxi8awPzyQH0xYB1dX6fAmOlPUBtN5hArDgFtwb3mCfVDZl419DwtEVZqqpRE5wpBP8lzOxNFMIHiJEnpEqFeQegDwYqdwb0TOp6ImD3pDSFdopy5xAJCoPLwj3GkagMGMvUeNfQ8LRZiC41pmGrDHKRrHUbg8gwCxjoS8TMa6jmluC6+i3ed43rFNgZPleh7WECbWJCqeIU3AhiXT8lKj7VNSw8bQxRl95aKDZ2k60qyElkdFkMXo5g5lFzHQLoDwz+KcCeoZ+bfobXC3j/Ma7/B5+3i4RqE2pbwUSaw10WC64HbvLhVOdrPjWqrXYbRWYQI6cRJxcA8xsGeBNAdwB1FyD2odYDQD6kf+9DXbtQ2DY+Zx2fq9BUbZOYUGqVCo7t8kOqztf+KmKrCrIXMXIQgzcKBUxBmXMAuoRBX4VK1wBjHYrlvo7XcwRrmYDNYrJMIkseQYxOY2JZxbU0g+p8zdqqVWQHZnkPqXIQyhwB0AkM9jSgzgLsPHrW9Hm8Pov3f8WEmACwDCaLQuvHROqOCa5p4GmzamSQLaRKhtmLgVWgQwQ1A7BjEX0U7xsBrGF8ThqKV6UxtDYT45oenKv5QHLCozA7AVSttg9Q+wEhTX0APU2QUnhvH65nYB0GmlVbAFekRamSldnmgKpguXej8886DSwXsChoAVyMZgeMYX5yQFWw3NtM59daqH922GOAlmCzA8lAXWBL6fZzArQqNBfQKLhRgAKwOmrF4ARQoYUWWmihcfsfLcOwSNSwLMYAAAAASUVORK5CYII=)

![Page 3 Image](data:image/png;base64,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)

![Page 3 Image](data:image/png;base64,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)

---

## Page 4

Table 1 : Mapping registered callback methods and location, etc. The SDK provides one of two means by which

overridden methods to relevant UI events. an app can receive each type of system event: broadcast

Relevant Event

Tap Tap Drag Text

(short) (long)

| onTouchEvent | X | X | X |
| --- | --- | --- | --- |
| performLongClick | X |  |  |
| performClick | X |  |  |

are the most common input mechanisms, the mechanisms

we do not support (keyboard, trackball, etc.) are device-

dependent, and there is often redundancy among different

UI inputs, such as an incoming phone call, a change in geo-

receiver and system service . In either case, the app registers

a callback to be called by the SDK when the event occurs.

The app may later unregister it to stop receiving the event.

manually modified to inject the instrumentation. A system

event becomes relevant when an app registers to receive it

not only which system events are relevant, but also what

data to associate with each. Unlike for UI events, however,

tem services (Section 4.2.2).

4.2.1 Broadcast Receiver Events

Object[] p = (Object[]) b.get("pdus");

for (int i = 0; i < pdus.length; i++)

} };

| If app registers callback: | The | observer | uses the same mechanism for extracting |  |
| --- | --- | --- | --- | --- |
| onClickListener | X | relevant system events via broadcast receivers and system |  |  |
| onLongClickListener | X | services: | it instruments the SDK to observe when an app |  |
| onTouchListener | X | X | X | registers (or unregisters) for each type of system event. This |
| onKeyListener | X | instrumented SDK is a file system.img that is loaded on the |  |  |
| onCreateContextMenuListener | X | emulator during bootup. | It is produced once and for all |  |
| If app overrides method: | by compiling Java source code of the original SDK that is |  |  |  |
| onKeyDown | X | and, conversely, it becomes irrelevant when an app unregis- |  |  |
| onKeyUp | X | ters it. As in the case of UI events, the | observer | computes |
| Dynodroid supports two input mechanisms: touchscreen and | this data can be highly-structured SDK objects (instead of |  |  |  |
| navigation buttons (specifically, “back” and “menu” buttons). | primitive-typed data). We next outline how the | observer |  |  |
| We found these sufficient in practice, for three reasons: they | handles specific broadcast receivers (Section 4.2.1) and sys- |  |  |  |
| input mechanisms. | Android provides two ways for apps to register for system |  |  |  |
| The | observer | analyzes the app’s current UI state in order | events via a broadcast receiver, depending on the desired |  |
| to compute relevant UI events. First, it deems clicking each | lifetime: dynamically or statically. In the dynamic case, the |  |  |  |
| navigation button as a relevant UI event, since these buttons | receiver’s lifetime is from when Context.registerReceiver() is |  |  |  |
| are always enabled. Second, it inspects the | view hierarchy | , | called to either until Context.unregisterReceiver() is called |  |
| which is an Android-specific tree representation of the app’s | or until the lifetime of the registering app component. | In |  |  |
| UI currently displayed on the touchscreen. | The SDK pro- | the static case, the receiver is specified in file AndroidMani- |  |  |
| vides two ways by which an app can react to inputs to a UI | fest.xml, and has the same lifetime as the app. In either case, |  |  |  |
| element: by overriding a method of the corresponding View | the receiver defines a callback method overriding Broadcas- |  |  |  |
| object’s class, or by registering a callback with it. | tReceiver.onReceive() that the SDK calls when the event |  |  |  |
| The SDK dispatches each input on the touchscreen to the | occurs (we provide an example below). The | observer | sup- |  |
| root node of the view hierarchy, which in turn depending on | ports both kinds of receivers. |  |  |  |
| the position of the input dispatches it recursively to one of | The Gingerbread SDK version we instrumented has 108 |  |  |  |
| its children, until the view to which the input was intended | different kinds of system events as | intents | for which an app |  |
| executes a callback and returns true, denoting that the in- | may register via a broadcast receiver. | As a proof of con- |  |  |
| put was successfully handled. | The | observer | obtains the | cept, we chose the top 25 receivers used by the top 1,000 |
| view hierarchy from a service called ViewServer that runs | free apps in the Google Play market. Supporting additional |  |  |  |
| on Android devices having debug support. Once it obtains | intents is straightforward: it involves identifying the type of |  |  |  |
| the view hierarchy, it considers only the View objects at leaf | data associated with the intent and providing valid values |  |  |  |
| nodes of the tree as interesting, as these correspond to visi- | for the data. The data includes an optional URI, and a Bun- |  |  |  |
| ble UI elements that users can interact with. It extracts two | dle object which is a key-value map that contains any extra |  |  |  |
| kinds of data from each such object about the correspond- | information. | Finally, for statically registered receivers, we |  |  |
| ing UI element: (a) the set of callback methods registered | also explicitly identify the receiver in the intent, since un- |  |  |  |
| and the set of methods overridden by the app, for listening | like UI events which are dispatched to a single View object, |  |  |  |
| to inputs to this UI element, and (b) the location and size | broadcast intents are by default dispatched to all receivers |  |  |  |
| of the UI element on the touchscreen (the position of its | (possibly from several apps) that register for them. |  |  |  |
| top left corner, its width, height, and scaling factor). | The | Table 3 shows the type and values of the data used by the |  |  |
| native Hierarchy Viewer does not provide all of the above | observer | for our 25 chosen broadcast intents. All the data |  |  |
| data; we modified the Android SDK source to obtain it. The | shown, except those of type URI, are provided in a Bun- |  |  |  |
| observer | uses the data in item (a) to compute which UI | dle object. For instance, an app may register the following |  |  |
| events are relevant, as dictated by Table 1. It supports all | receiver for the | SMS RECEIVED | intent which is broadcast |  |
| common touchscreen inputs: | tap inputs, limited kinds of | upon incoming SMS messages: |  |  |
| gestures, and text inputs. | Finally, the | observer | uses the | public class SmsReceiver extends BroadcastReceiver { |
| data in item (b) to compute the parameters of each such | @Override public void onReceive(Context c, Intent e) { |  |  |  |
| event, as dictated by Table 2. | Bundle b = e.getExtras(); |  |  |  |
| 4.2 | System Events | SmsMessage[] a = new SmsMessage[p.length]; |  |  |
| These are events generated by the SDK in response to non- | a[i] = SmsMessage.createFromPdu((byte[]) p[i]); |  |  |  |

---

## Page 5

Table 2 : User event parameters: l , t , w , h denote left position, top position, width, and height of the

view, respectively. TL, TR, BL, BR, MB, MT, ML, MR denote top left/right, bottom left/right, and mid

bottom/top/left/right points of the view, respectively.

| Event Type | Parameters | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tap | Tap( | l | + | w | /2, | t | + | h | /2) | trigger Tap at center of view |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| LongTap | LongTap( | l | + | w | /2, | t | + | h | /2) | trigger LongTap at center of view |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Drag | random one of: Drag( | l | , | t | , | l | + | w | , | t | + | h | ), Drag( | l | + | w | , | t | + | h | , | l | , | t | ), | randomly trigger one of gestures: |  |  |  |
| Drag( | l | , | t | + | h | , | l | + | w | , | t | ), Drag( | l | + | w | , | t | , | l | , | t | + | h | ), | TL to BR, BR to TL, BL to TR, |  |  |  |  |
| Drag( | l | , | t | + | h | /2, | l | + | w | , | t | + | h | /2), Drag( | l | + | w | , | t | + | h | /2, | l | , | t | + | h | /2), | TR to BL, ML to MR, MR to ML, |
| Drag( | l | + | w | /2, | t | , | l | + | w | /2, | t | + | h | ), Drag( | l | + | w | /2, | t | + | h | , | l | + | w | /2, t) | MT to MB, MB to MT |  |  |
| Text | arbitrary fixed string | trigger arbitrary text input |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| To trigger this event, the | executor | serializes the appro- | Algorithm 2 | Event selection algorithm | BiasedRandom | . |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| priate intent along with a Bundle object that maps a kay | 1: | var | G | : map from (event, set of events) pairs to int |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| named “pdus” to an SmsMessage object array representing | 2: | G | := empty map |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| arbitrary but well-formed phone numbers and message texts. | 3: | INPUT: | Set | E | of relevant events. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

4: OUTPUT: An event in E .

| 4.2.2 | System Service Events | 5: | for each | ( | e | in | E | ) | do |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| System services are a fixed set of processes that provide | 6: | if | (( | e, E | ) is not in domain of | G | ) | then |  |  |  |  |
| abstractions of different functionality of an Android device. | 7: | // Initialize score of event | e | in context | E | . |  |  |  |  |  |  |
| We distinguish services whose offered functionality depends | 8: | G | ( | e, E | ) := init score( | e | ) |  |  |  |  |  |
| on app-provided data from those that are independent of | 9: | end if |  |  |  |  |  |  |  |  |  |  |
| such data. | We call such services | internally | vs. | externally | 10: | end for |  |  |  |  |  |  |
| triggered, as they depend on data internal or external to | 11: | var | L | : map from events to int |  |  |  |  |  |  |  |  |
| the app under test. For instance, the AlarmManager service | 12: | L | := map from each event in | E | to 0 |  |  |  |  |  |  |  |
| is internally triggered, as it depends on the alarm duration | 13: | while | true | do |  |  |  |  |  |  |  |  |
| given by an app, but the LocationManager service is exter- | 14: | e | := event chosen uniformly at random from | E |  |  |  |  |  |  |  |  |
| nally triggered, as it depends on the device’s geo-location. | 15: | if | ( | L | ( | e | ) = | G | ( | e, E | )) | then |
| Dynodroid only controls externally triggered services as the | 16: | // Select | e | this time, but decrease its chance of being |  |  |  |  |  |  |  |  |
| app itself controls internally triggered services. | 17: | // selected in context | E | in future calls to | selector | . |  |  |  |  |  |  |
| Table 4 shows how Dynodroid handles events of each ex- | 18: | G | ( | e, E | ) := | G | ( | e, E | ) + 1 |  |  |  |
| ternally triggered service. | The “Register/Unregister Mech- | 19: | return | e |  |  |  |  |  |  |  |  |
| anism” shows how an app registers or unregisters for the | 20: | else |  |  |  |  |  |  |  |  |  |  |
| service, which the | observer | observes via SDK instrumen- | 21: | // Increase chance of selecting | e | in the next iteration. |  |  |  |  |  |  |
| tation. Since services are global components, the | observer | 22: | L | ( | e | ) := | L | ( | e | ) + 1 |  |  |
| uses the ID of the app under test to filter out observing other | 23: | end if |  |  |  |  |  |  |  |  |  |  |
| apps that may also register or unregister for these services. | 24: | end while |  |  |  |  |  |  |  |  |  |  |
| The “Callback Mechanism” shows how the app specifies the | 25: | procedure | init score( | e | ) : | int |  |  |  |  |  |  |
| callback to handle events by the service. Lastly, the “Trigger | 26: | case | (e) | of |  |  |  |  |  |  |  |  |
| Mechanism” shows how the | executor | triggers the callback, | 27: | Text event: | return | -1 |  |  |  |  |  |  |
| usually via a command sent from the ActivityManager tool | 28: | non-Text UI event: | return | 1 |  |  |  |  |  |  |  |  |
| running on the emulator (see Section 3). | 29: | system event: | return | 2 |  |  |  |  |  |  |  |  |
| The following example showing how an app may use the | 30: | end case |  |  |  |  |  |  |  |  |  |  |

LocationManager service:

GpsStatus.Listener l = new GpsStatus.Listener() {

@Override public void onGpsStatusChanged(int event) {...} 5. SELECTOR

};

| LocationManager lm = getSystemService(LOCATION_SERVICE); | The | selector | selects an event for the | executor | to ex- |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lm.addGpsStatusListener(l); | ecute from the set of relevant events | E | computed by the |  |  |  |  |
| ...; | observer | . We implemented three different selection strate- |  |  |  |  |  |
| lm.removeGpsStatusListener(l); | gies in the | selector | , called | Frequency | , | UniformRandom | , and |

BiasedRandom . This section describes these strategies.

| From the point at which the app registers to listen to GPS | The | Frequency | strategy selects an event from | E | that has |
| --- | --- | --- | --- | --- | --- |
| status changes by calling addGpsStatusListener() to the point | been selected least frequently by it so far. The rationale is |  |  |  |  |
| at which it unregisters by calling removeGpsStatusListener(), | that infrequently selected events have a higher chance of ex- |  |  |  |  |
| the | observer | regards GPS status change as a relevant sys- | ercising new app functionality. A drawback of this strategy |  |  |
| tem event. | If the | selector | described in the next section | is that its deterministic nature leads the app to the same |  |
| selects this event, then the | executor | triggers it by sending | state in repeated runs. In practice, different states might be |  |  |
| telnet command “geo fix | G | ” to the emulator, where | G | is an | reached in different runs because of non-determinism inher- |
| arbitrary geo-location (a triple comprising a latitude, longi- | ent in dynamic analysis of Android apps, due to factors such |  |  |  |  |
| tude, and altitude). This in turn results in invoking callback | as concurrency and asynchrony; however, we cannot rely on |  |  |  |  |
| onGpsStatusChanged() defined by the app. | them to cover much new app functionality. |  |  |  |  |

---

## Page 6

Table 3 : Broadcast receiver events with associated data as implemented in Dynodroid. These implemented

events have no associated data: BATTERY [CHANGED | LOW | OKAY] , ACTION POWER [DIS]CONNECTED ,

ACTION SHUTDOWN , TIME SET , AUDIO BECOMING NOISY , DATE CHANGED , USER PRESENT , ME-

DIA EJECT , and BOOT COMPLETED .

| Action Name | Data Type : Description | Data Value |
| --- | --- | --- |
| APPWIDGET UPDATE | int[] : IDs of App Widgets to update | random (1-10) sized array of random (0-1000) ints |
| android.net.NetworkInfo : status of | random NetworkInfo object from |  |

CONNECTIVITY CHANGE

| the network interface | android.net.ConnectivityManager |  |
| --- | --- | --- |
| int : uid assigned to new package, | uid of random installed package, |  |
| PACKAGE ADDED | bool : true if this follows a ‘removed’ | random bool |

broadcast for the same package

| int : uid previously given to package, | uid of random installed package, |
| --- | --- |
| bool : true if removing entire app, | random bool, |

PACKAGE REMOVED

bool : true if an ‘added’ broadcast random bool

for the same package will follow

PACKAGE REPLACED int : uid assigned to new package uid of random installed package

URI : path to mount point of media, “/mnt/sdcard”,

MEDIA MOUNTED

| bool : true if media is read-only | false |  |
| --- | --- | --- |
| TIMEZONE CHANGED | TimeZone : time-zone representation | America/Los Angeles time-zone |
| android.view.KeyEvent : key event | KeyEvent object with action as ACTION UP and |  |

MEDIA BUTTON

| that caused this broadcast | value as KEYCODE MEDIA PLAY PAUSE |
| --- | --- |
| android.telephony.SmsMessage[] : | array of 1 SmsMessage object with arbitrary |

SMS RECEIVED

array of received SMS messages MSISDN and message

MEDIA UNMOUNTED URI : path to mount point of media “/mnt/sdcard”

int : phone state (idle | ringing | offhook), 1 (ringing),

PHONE STATE

| String : incoming phone number | an arbitrary MSISDN |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MEDIA SCANNER FINISHED | URI | “/mnt/sdcard” |  |  |  |  |  |  |
| NEW OUTGOING CALL | String: outgoing phone number | an arbitrary MSISDN |  |  |  |  |  |  |
| The | UniformRandom | strategy circumvents the above prob- | recorded in global variable | G | that maps each pair ( | e, E | ) to a |  |
| lem by selecting an event from | E | uniformly at random. This | score. The map starts empty and is populated lazily. At any |  |  |  |  |  |
| is essentially the strategy used by the Monkey fuzz testing | instant, the score for a pair ( | e, E | ) in the map is either | − | 1, |  |  |  |
| tool, with three key differences. | First, Monkey can only | meaning event | e | is blacklisted in context | E | (i.e., | e | will never |
| generate UI events, preventing it from covering app func- | be selected in context | E | ), or it is a non-negative integer, |  |  |  |  |  |
| tionality controlled by system events. Second, Monkey does | with higher values denoting lesser chance of selecting event |  |  |  |  |  |  |  |
| not compute relevant events and can send many events that | e | in context | E | in the future. We found it suitable to use the |  |  |  |  |
| are no-ops in the current state, hindering efficiency and con- | set of relevant events | E | as context because it is efficient to |  |  |  |  |  |
| ciseness of the generated event sequence. | Third, Monkey | compute (the | observer | already computes | E | ) and it strikes |  |  |
| does not compute a model of the app’s UI, which has pros | a good balance between factoring too little and too much of |  |  |  |  |  |  |  |
| and cons. On one hand, it prevents Monkey from identifying | the state into the context. |  |  |  |  |  |  |  |
| observationally equivalent | UI events (e.g., taps at different | Each time the | selector | is called using this strategy in an |  |  |  |  |
| points of the same button that have the same effect, of click- | observe-select-execute cycle, it runs the algorithm on lines |  |  |  |  |  |  |  |
| ing the button) and hinders efficiency and conciseness; on | 3-25, taking as input the set of relevant events | E | from the |  |  |  |  |  |
| the other hand, Dynodroid sends mostly fixed inputs (see | observer | and producing as output the selected event | e | ∈ | E |  |  |  |
| Table 2) to a widget, and may fail to adequately exercise | for the | executor | to execute. It starts by mapping, for ev- |  |  |  |  |  |
| custom widgets (e.g., a game that interprets taps at differ- | ery | e | ∈ | E | , the pair ( | e, E | ) to its initial score in global map |  |
| ent points of a widget differently). | G | , unless it already exists in | G | . | We bias the initial score |  |  |  |
| A drawback of the | UniformRandom | strategy is that it does | (lines 26-31) depending on the kind of event. If | e | is a Text |  |  |  |
| not take any domain knowledge into account: | it does not | event, its initial score is | − | 1. | In other words, text inputs |  |  |  |
| distinguish between UI events and system events, nor be- | are blacklisted in all contexts. Intuitively, the reason is that |  |  |  |  |  |  |  |
| tween different contexts in which an event may occur, nor | text inputs are interesting only if they are followed by a non- |  |  |  |  |  |  |  |
| between frequent and infrequent events. | For instance, an | text input, e.g., a button click. | Hence, we forbid selecting |  |  |  |  |  |
| event that is always relevant (e.g., an incoming phone call | text inputs in the | selector | altogether, and instead require |  |  |  |  |  |
| event) stands to be picked much more often than one that | the | executor | to populate all text boxes in the current UI |  |  |  |  |  |
| is relevant only in certain contexts (e.g., only on a certain | before it executes the selected non-Text event. | We distin- |  |  |  |  |  |  |
| screen of the app). As another example, navigation buttons | guish between two kinds of non-Text events: | non-Text UI |  |  |  |  |  |  |
| (“back” and “menu”) are always relevant, but often have dif- | events and system events. | We choose initial score of 1 for |  |  |  |  |  |  |
| ferent behavior on different screens. These observations mo- | the former and 2 for the latter, reducing the relative chance |  |  |  |  |  |  |  |
| tivate our final and default selection strategy | BiasedRandom | . | of selecting system events. This bias stems from our obser- |  |  |  |  |  |
| This strategy is shown in Algorithm 2. Like the | Frequency | vation that system events tend to be relevant over longer |  |  |  |  |  |  |
| strategy, it maintains a history of how often each event has | periods than UI events, with UI events typically being rel- |  |  |  |  |  |  |  |
| been selected in the past, but it does so in a context-sensitive | evant only when a certain screen is displayed. | A hallmark |  |  |  |  |  |  |
| manner: the | context | for an event | e | at a particular instant is | of our algorithm, however, is that it never starves any event |  |  |  |
| the set | E | of all relevant events at that instant. This history is | in any context. | This is ensured by lines 11-25, which re- |  |  |  |  |

---

## Page 7

Table 4 : Handling of events of externally triggerable system services in Dynodroid.

| Service | Register/Unregister Mechanism | Callback Mechanism | Trigger Mechanism |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| registerMediaButtonEventReceiver( | C | ) / | invoke component denoted by | send KeyPress event with keycode of |  |  |
| unregisterMediaButtonEventReceiver() | ComponentName object | C | any | MEDIA BUTTON | via | monkeyrunner |

Audio-

Manager requestAudioFocus( L ) /

abandonAudioFocus()

Location-

Manager

on[Location

onProvider[Enabled

removeUpdates()

requestSingleUpdate() /

auto unregister after update

Telephone- listen( L , S ), with

Manager state S non-zero / zero

Table 5 : Emulator configuration in our evaluation.

| Feature Name | Feature Value |
| --- | --- |
| Device RAM size | 4 GB |
| Emulator hardware features | All except GPU emulation |
| Sdcard size | 1 GB |
| Files on Sdcard | pdf:2, img:2, vcf:11, arr:2, zip:4, |
| (type:count) | 3gp:1, m4v:1, mov:1, mp3:3 |

one satisfies condition L ( e ) = G ( e, E ), in which case it is

returned as the event selected by the current selector call.

chance of picking e in context E in a future selector call.

L is a local map that records the number of times event e

was randomly picked by the above process in the current se-

lector call but passed over for not satisfying the condition.

Thus, fewer the number of times that e has been chosen in

context E in past selector calls, or higher the number of

times that e has been passed over in context E in the current

selector call, the higher the chance that e will be selected

to execute in context E in the current selector call.

| call onAudioFocusChange() in | simulate incoming phone call |  |  |  |
| --- | --- | --- | --- | --- |
| AudioManager.OnAudioFocus- | from a fixed MSIDN | N | via |  |
| ChangeListener object | L | telnet command “gsm call | N | ” |

trigger PendingIntent P

| if LocationListener specified, call | set geo-location twice, via |  |  |  |
| --- | --- | --- | --- | --- |
| \| | Status]Changed() or | commands “geo fix | G |  |
| \| | Disabled](); | “geo fix | G | is random |

2 ”; G 1

| else call PendingIntent or post to | geo-location, | G | 2 | is based on |  |
| --- | --- | --- | --- | --- | --- |
| message queue of given Looper | G | 1 | and registered criteria. |  |  |
| same as above | same as above |  |  |  |  |
| call onDataActivity() or any of | trigger state change via telnet |  |  |  |  |
| several on*Changed() methods | command “gsm | C D | ”; | C | is random gsm |
| on PhoneStateListener object | L | command and | D | is random valid data. |  |

Our first study measures the app source code coverage

that different input generation approaches are able to achieve.

We randomly chose 50 apps from the Android open-source

apps repository F-Droid [3] for this study. These 50 apps

are sufficiently diverse as evidenced in Figure 3. The SLOC

of these apps ranges from 16 to 21.9K, with a mean of 2.7K.

We obtained app coverage metrics by using Emma [2],

a popular Java source code coverage tool. Emma generates

detailed line coverage metrics to the granularity of branches,

and provides coverage reports in different formats that assist

in analysis and gathering statistics.

| addGpsStatusListener( | L | ) / | call onGpsStatusChanged() in | set geo-location to fixed value | G |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| removeGpsStatusListener() | GpsStatus.Listener object | L | via telnet command “geo fix | G | ” |  |  |  |  |  |  |  |
| addNmeaListener( | L | ) / | call onNmeaReceived() in | send fixed NMEA data | S | via |  |  |  |  |  |  |
| removeNmeaListener() | GpsStatus.NmeaListener object | L | telnet command “geo nmea | S | ” |  |  |  |  |  |  |  |
| addProximityAlert( | G | , | P | ) / | set geo-location to registered proximal |  |  |  |  |  |  |  |
| removeProximityAlert() | value | G | via telnet command “geo fix | G | ” |  |  |  |  |  |  |  |
| requestLocationUpdates() / | 1 | ” and |  |  |  |  |  |  |  |  |  |  |
| Sensor- | registerListener( | L | , | S | ) / | call on[Accuracy | \| | Sensor]Changed() | set random values | x, y, z | for sensor | S |
| Manager | unregisterListener() | on SensorEventListener object | L | via telnet command “sensor set | S | x | : | y | : | z | ” |  |
| peatedly pick an event | e | from | E | uniformly at random, until | Figure 3 | : | Distribution of open-source apps. |  |  |  |  |  |
| Just before returning, we increment | G | ( | e, E | ) to reduce the | 6.1 | Study 1: App Source Code Coverage |  |  |  |  |  |  |
| 6. | EMPIRICAL EVALUATION | Evaluated Approaches. | We evaluated the following |  |  |  |  |  |  |  |  |  |
| We evaluated Dynodroid on real-world Android apps, and | five approaches in this study: Dynodroid using each of the |  |  |  |  |  |  |  |  |  |  |  |
| compared it to two state-of-the-art approaches for testing | three selection strategies ( | Frequency | , | UniformRandom | , | Biase- |  |  |  |  |  |  |
| such apps: manual testing and automated fuzzing. All our | dRandom | ); the Monkey fuzz testing tool provided in the An- |  |  |  |  |  |  |  |  |  |  |
| experiments were done on Linux machines with 8GB mem- | droid platform; and manual testing conducted in a study in- |  |  |  |  |  |  |  |  |  |  |  |
| ory and 3.0GHz processors. We used the Gingerbread ver- | volving ten users. Table 6 shows the setup we used for each |  |  |  |  |  |  |  |  |  |  |  |
| sion of Android, which is the most popular version, installed | of these five approaches on each app. | We ran each of the |  |  |  |  |  |  |  |  |  |  |
| on 50% of all devices that recently accessed Google Play [6]. | three variants of Dynodroid for 2,000 events, we ran Monkey |  |  |  |  |  |  |  |  |  |  |  |
| Table 5 shows the emulator configuration that we used in all | for 10,000 events, and we allowed the users in our study to |  |  |  |  |  |  |  |  |  |  |  |
| experiments. For each run, an app was given a freshly cre- | manually generate an unlimited number of events. |  |  |  |  |  |  |  |  |  |  |  |
| ated emulator along with only default system applications | We used different numbers of events for Dynodroid and |  |  |  |  |  |  |  |  |  |  |  |
| and the above configuration. We next describe two studies | Monkey because those are the numbers of events that the |  |  |  |  |  |  |  |  |  |  |  |
| we performed: measuring app source code coverage (Section | two tools were able to generate in roughly the same duration |  |  |  |  |  |  |  |  |  |  |  |
| 6.1) and finding bugs in apps (Section 6.2). | in three hours for each of the 50 apps on average. Dynodroid |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 8

Table 6 : Testing approaches used to test each app. under test, we prevented both Dynodroid and Monkey from

| Dynodroid | Frequency | 2,000 | 1 |
| --- | --- | --- | --- |
| Dynodroid | UniformRandom | 2,000 | 3 |
| Apps Switch | 2% |  |  |
| Others (keyboard/volume/camera buttons) | 16% |  |  |

runs 5X slower than Monkey primarily due to performance

issues with the version of the off-the-shelf Hierarchy Viewer

tool it calls after each event. On the plus side, as we show

below, Dynodroid achieves peak code coverage much faster

than Monkey, requiring far fewer than even the 2,000 events

we generated.

Monkey triggers a large variety of UI events but no system

events. Table 7 summarizes the kinds of UI events it triggers

in its default configuration that we used. These events are

strictly a superset of the kinds of UI events that Dynodroid

can generate (see Section 4.1).

All ten users that we chose in our study are graduate stu-

dents at Georgia Tech who have experience with not only

using Android apps, but also developing and testing them

using Android developer tools. We provided each of them

with each app’s source code, the ability to run the app any

number of times in the Android emulator, and the ability

to inspect app source code coverage reports produced from

those runs. They were allowed to provide any kind of GUI

inputs, including intelligent game inputs and login creden-

tials to websites. They were also allowed to modify the en-

vironment by adding/removing files from the emulator’s Sd-

card, to manually trigger system events via a terminal by

studying the apps’ source code, etc.

We ensured that each app was assigned to at least two

users. Likewise, we ran each automated approach involv-

ing randomization (Monkey, and the UniformRandom and

BiasedRandom strategies in Dynodroid) three times on each

app. We considered the highest coverage that a user or

run achieved for each app. Perhaps surprisingly, for cer-

tain apps, we found fairly significant variation in coverage

achieved across the three runs by any of the random ap-

proaches. Upon closer inspection, we found certain events in

these apps that if not selected in a certain state, irreversibly

prevent exploring entire parts of the app’s state space. Two

possible fixes to this problem are: (i) allowing a relatively

expensive event during testing that removes and re-installs

the app (Dynodroid currently installs the app only once in

a run); and (ii) to simply run the app multiple times and

aggregate their results.

Finally, Android apps may often call other apps such as

a browser, a picture editor, etc. To prevent the automated

approaches in the study from wandering far beyond the app

exercising components not contained in the app under test.

study for the 50 apps are shown in the three plots in Figure 4.

Figure 4a compares the code coverage achieved for each

notes the user who achieved the best coverage of all users

but not the other).

Both Dynodroid and Human cover 4-91% of code per app,

for an average of 51%. Dynodroid exclusively covers 0-26%

of code, for an average of 4%, and Human exclusively cov-

ers 0-43% of code, for an average of 7%. In terms of the

total code covered for each app, Human easily outperforms

Dynodroid, achieving higher coverage for 34 of the 50 apps.

This is not surprising, given that the users in our study were

expert Android users, could provide intelligent text inputs

and event sequences, and most importantly, could inspect

Emma’s coverage reports and attempt to trigger events to

cover any missed code.

But all the ten users in our study also reported tedious-

ness during testing, how easy it was to miss combinations of

events, and that it was especially mundane to click various

options in the settings of apps one by one. Dynodroid could

be used to automate most of the testing effort of Human, as

measured by what we call the automation degree , measured

as the ratio of coverage achieved by the intersection of Dyno-

droid and Human, to the total coverage achieved by Human.

This ratio varies from 8% to 100% across our 50 apps, with

mean 83% and standard deviation 21%. These observations

justify Dynodroid’s vision of synergistically combine human

and machine. It already provides support for intelligent text

inputs, where a user with knowledge of an app can specify

the text that it should use (instead of random text) in the

specific text box widget prior to execution, or can pause

its event generation when it reaches the screen, key in the

input, and let it resume (as described in Section 3).

Figure 4b compares the code coverage achieved for each of

the 50 apps by Dynodroid vs. Monkey. It is analogous to Fig-

ure 4a with Monkey instead of Human. Both Dynodroid and

Monkey cover 4-81% of code per app, for an average of 47%.

Dynodroid exclusively covers 0-46% of code, for an average

of 8%, which is attributed to system events that only Dyno-

droid can trigger. Monkey exclusively covers 0-61% of code,

for an average of 6%, which is attributed to the richer set of

UI events that Monkey can trigger (see Table 2 vs. Table 7).

Another reason is that Dynodroid only generates straight

(Drag) gestures but Monkey combines short sequences of

such gestures to generate more complex (e.g., circular) ges-

tures. Finally, Dynodroid uses fixed parameter values for UI

events whereas Monkey uses random values, giving it supe-

rior ability to exercise custom widgets. In terms of the total

code covered for each app, however, Dynodroid outperforms

Monkey, achieving higher coverage for 30 of the 50 apps.

| Approach | #Events | #Runs | Coverage Results. | The results of our code coverage |
| --- | --- | --- | --- | --- |
| Dynodroid | BiasedRandom | 2,000 | 3 | To enable comparisons for each app across plots, each point |
| Monkey | 10,000 | 3 | on the X axis of all three plots denotes the same app. We |  |
| Humans | no limit | ≥ | 2 | next elaborate upon the results in each of these plots. |
| Table 7 | : | Kinds of UI events triggered by Monkey. | of the 50 apps by Dynodroid vs. Human, where Human de- |  |
| Event Type | Proportion | in our user study for a given app, and Dynodroid uses the |  |  |
| Touch | 15% | BiasedRandom | strategy. | The bar for each app has three |
| Motion | 10% | parts: the bottom red part shows the fraction of code that |  |  |
| Trackball | 15% | both Dynodroid and Human were able to cover (i.e., the in- |  |  |
| Minor Navigation | 25% | tersection of code covered by them). Atop this part are two |  |  |
| Major Navigation | 15% | parts showing the fraction of code that only Dynodroid and |  |  |
| System keys | 2% | only Human were able to cover (i.e., the code covered by one |  |  |

---

## Page 9

100

80

60

40

% App Code Coverage

20

0

(a) Code coverage achieved by Dynodroid (

100

80

60

40

% App Code Coverage

20

0

(b) Code coverage achieved by Dynodroid (

10000

1000

Number of Events

100

(c)

to do so. Note that the Y axis in Figure 4c uses a logarithmic scale.

Dynodroid using each of the selection strategies—to achieve

Monkey for 10,000 events and Dynodroid for 2,000 events).

To strike a good tradeoff between measurement accuracy

and performance, we invoke Emma to aggregate coverage

after every 100 events for each approach on each app, and

hence the minimum number of reported events is 100. It

is evident that all three strategies in Dynodroid require sig-

nificantly fewer events than Monkey; in particular, Monkey

requires 20X more events than BiasedRandom on average.

This is despite Dynodroid considering both system and UI

events at each step. The reason is that Dynodroid only ex-

ercises relevant events at each step and also because it iden-

tifies observationally equivalent events. Finally, of the three

selection strategies in Dynodroid, BiasedRandom performs

common

only Dynodroid

only Human

BiasedRandom ) vs. Human.

common

only Dynodroid

only Monkey

BiasedRandom ) vs. Monkey.

BiasedRandom

UniformRandom

Frequency

Monkey

Minimum number of events needed for peak code coverage by various approaches.

The second study we performed shows that Dynodroid is

an effective bug-finding tool and is also robust. To demon-

strate its robustness, we were able to successfully run Dyno-

droid on the 1,000 most popular free apps from Google Play.

The popularity metric used is a score given to each app by

Google that depends on various factors like number of down-

loads and ratings. These apps are uniformly distributed over

all 31 app categories in Google Play: the minimum, maxi-

mum, mean, and standard deviation of the number of apps

in these categories is 26, 55, 40.3, and 6.3, respectively.

We also found that Dynodroid exposed several bugs in

both the 50 open-source apps we chose from F-Droid and

the 1,000 most popular free apps from Google Play. Table 8

Figure 4 : Results of the app source code coverage study. Each point on the X axis in all three plots denotes

the same app from the 50 open-source apps used in the study. Figure 4a shows that Dynodroid can be used

to automate to a significant degree the tedious testing done by humans. Figure 4b shows that Dynodroid

and Monkey get comparable coverage, but Figure 4c shows that Monkey requires significantly more events

| Figure 4c compares the minimum number of events that | the best, with each of the other two strategies requiring 2X |  |
| --- | --- | --- |
| were needed by each automated approach—Monkey, and | more events than it on average. |  |
| peak code coverage for each of the 50 apps (recall that we ran | 6.2 | Study 2: Bugs Found in Apps |

---

## Page 10

Table 8 : Bugs found by Dynodroid in the 50 open-source apps from F-Droid and the 1,000 top free apps from

Google Play. The two classes of apps are separated by the double line, with all the open-source apps listed

above. NULL PTR denotes a “null pointer dereference” exception and ARRAY IDX an “array index out of

bounds” exception.

| App Name | # Bugs | Kind | Description |
| --- | --- | --- | --- |
| PasswordMakerProForAndroid | 1 | NULL PTR | Improper handling of user data. |
| com.morphoss.acal | 1 | NULL PTR | Dereferencing null returned by an online service. |
| hu.vsza.adsdroid | 2 | NULL PTR | Dereferencing null returned by an online service. |
| cri.sanity | 1 | NULL PTR | Improper handling of user data. |
| com.zoffcc.applications.aagtl | 2 | NULL PTR | Dereferencing null returned by an online service. |
| org.beide.bomber | 1 | ARRAY IDX | Game indexes an array with improper index. |
| com.addi | 1 | NULL PTR | Improper handling of user data. |
| com.ibm.events.android.usopen | 1 | NULL PTR | Null pointer check missed in onCreate() of an activity. |
| com.nullsoft.winamp | 2 | NULL PTR | Improper handling of RSS feeds read from online service. |
| com.almalence.night | 1 | NULL PTR | Null pointer check missed in onCreate() of an activity. |
| com.avast.android.mobilesecurity | 1 | NULL PTR | Receiver callback fails to check for null in optional data. |
| com.aviary.android.feather | 1 | NULL PTR | Receiver callback fails to check for null in optional data. |
| summarizes these bugs. | We mined the Android emulator | using the GUITAR [4] framework. | GUITAR has been ap- |
| logs for any unhandled exceptions that were thrown from | plied to Android apps, IPhone apps, and web apps, among |  |  |
| code in packages of the app under test while Dynodroid ex- | others. | In general, model-based testing requires users to |  |
| ercised the app in the emulator. | To be conservative, we | provide a model of the app’s GUI [24, 27], though auto- |  |
| checked for only | FATAL EXCEPTION | , as this exception is | mated GUI model inference tools tailored to specific GUI |
| the most severe and causes the app to be forcefully termi- | frameworks exist as well [8, 23]. | One such tool in the An- |  |
| nated. We manually ascertained each bug to eliminate any | droid platform, that Dynodroid also uses for observing rele- |  |  |
| false positives reported by this method but found that all the | vant UI events, is Hierarchy Viewer [5]. Model-based testing |  |  |
| bugs were indeed genuine and did cause the app to crash. | harnesses human and framework knowledge to abstract the |  |  |

input space of a program’s GUI, and thus reduce redun-

dancy and improve efficiency, but existing approaches pre-

7. RELATED WORK

dominantly target UI events as opposed to system events.

| There are broadly three kinds of approaches for generating | The EXSYST tool [15] extends model-based testing using a |  |  |
| --- | --- | --- | --- |
| inputs to mobile apps: | fuzz testing | , which generates random | genetic algorithm to continually refine models from run-time |
| inputs to the app; | systematic testing | , which systematically | feedback, with the goal of maximizing the code coverage of |
| tests the app by executing it symbolically; and | model-based | the given app. | It uses guidance based on branch distance |
| testing | , which tests a model of the app. We elaborate upon | measurement and also aims to produce small test suites. |  |

each of these three approaches in this section.

Fuzz Testing. The Android platform includes a fuzz

| testing tool Monkey [7] that generates a sequence of random | 8. | CONCLUSION |
| --- | --- | --- |
| UI events to Android apps in a mobile device emulator. Re- | We presented a practical system Dynodroid for generat- |  |
| cent work has applied Monkey to find GUI bugs [16] and | ing relevant inputs to mobile apps on the dominant Android |  |
| security bugs [19]. Fuzz testing is a black-box approach, is | platform. | It uses a novel “observe-select-execute” princi- |
| easy to implement robustly, is fully automatic, and can effi- | ple to efficiently generate a sequence of such inputs to an |  |
| ciently generate a large number of simple inputs. But it is | app. It operates on unmodified app binaries, it can generate |  |
| not suited for generating inputs that require human intel- | both UI inputs and system inputs, and it allows combin- |  |
| ligence (e.g., playing and winning a game) nor is it suited | ing inputs from human and machine. | We applied it to a |
| for generating highly specific inputs that control the app’s | suite of 50 real-world apps and compared its performance to |  |
| functionality, and it may generate highly redundant inputs. | two state-of-the-art input generation approaches for Android |  |
| Finally, Monkey only generates UI events, not system events. | apps: manual testing done by expert users and fuzz testing |  |
| It is challenging to randomly generate system events due to | using the popular Monkey tool. We showed that Dynodroid |  |
| the large space of possible such events and highly structured | can significantly automate testing tasks that users consider |  |
| data that is associated with them. | tedious, and generates significantly more concise input se- |  |
| Systematic Testing. | Several recent efforts [9, 17, 22] | quences than Monkey. We also showed its robustness by ap- |
| have applied symbolic execution [11, 14, 18] to generate in- | plying it to the top 1,000 free apps on Google Play. Lastly, |  |
| puts to Android apps. | Symbolic execution automatically | it exposed a few bugs in a handful of the apps to which it |
| partitions the domain of inputs such that each partition cor- | was applied. |  |

responds to a unique program behavior (e.g., execution of a

unique program path). Thus, it avoids generating redundant

| inputs and can generate highly specific inputs, but it is dif- | ACKNOWLEDGMENTS |  |
| --- | --- | --- |
| ficult to scale due to the notorious path explosion problem. | We thank the anonymous reviewers for insightful comments. |  |
| Moreover, symbolic execution is not black-box and requires | We thank the ten users in our study for their participation. |  |
| heavily instrumenting the app in addition to the framework. | This research was supported in part by DARPA contract |  |
| Model-based Testing. | Model-based testing has been | #FA8750-12-2-0020, NSF award #1253867, and awards from |
| widely studied in testing GUI-based programs [10,20,21,26] | Google and Microsoft. |  |

---

## Page 11

9. REFERENCES ACM Conf. on Programming Language Design and

testing. http://guitar.sourceforge.net/ .

[6] Historical distribution of Android versions in use.

[8] D. Amalfitano, A. Fasolino, S. Carmine, A. Memon,

and P. Tramontana. Using GUI ripping for automated

testing of Android applications. In Proceedings of 27th

[9] S. Anand, M. Naik, H. Yang, and M. Harrold.

markets. In Proceedings of 2nd Intl. Workshop on

Implementation (PLDI) , 2005.

Test (AST) , 2011.

//www.cs.umd.edu/~jfoster/papers/symdroid.pdf .

automated security testing of Android applications on

the cloud. In Proceedings of 7th IEEE/ACM Workshop

on Automation of Software Test (AST) , 2012.

Foundations of Software Engineering (FSE) , 2000.

Engr. , 37(4), 2011.

| [1] DroidBox: Android application sandbox. | [15] F. Gross, G. Fraser, and A. Zeller. Search-based |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| http://code.google.com/p/droidbox/ | . | system testing: high coverage, no false alarms. In |  |  |  |
| [2] EMMA: a free Java code coverage tool. | Proceedings of the 2012 International Symposium on |  |  |  |  |
| http://emma.sourceforge.net/ | . | Software Testing and Analysis (ISSTA) | , 2012. |  |  |
| [3] Free and Open Source App Repository. | [16] C. Hu and I. Neamtiu. Automating GUI testing for |  |  |  |  |
| https://f-droid.org/ | . | Android applications. In | Proceedings of 6th |  |  |
| [4] GUITAR: A model-based system for automated GUI | IEEE/ACM Workshop on Automation of Software |  |  |  |  |
| [5] Hierarchy Viewer. | http://developer.android.com/ | [17] J. Jeon, K. Micinski, and J. Foster. Symdroid: |  |  |  |
| tools/help/hierarchy-viewer.html | . | Symbolic execution for dalvik bytecode, 2012. | http: |  |  |
| http://developer.android.com/about/dashboards/ | [18] J. King. Symbolic execution and program testing. |  |  |  |  |
| index.html | . | CACM | , 19(7):385–394, 1976. |  |  |
| [7] UI/Application Exerciser Monkey. | http: | [19] R. Mahmood, N. Esfahani, T. Kacem, N. Mirzaei, |  |  |  |
| //developer.android.com/tools/help/monkey.html | . | S. Malek, and A. Stavrou. A whitebox approach for |  |  |  |
| Intl. Conf. on Automated Software Engineering | [20] A. Memon, M. Pollack, and M. Soffa. Automated test |  |  |  |  |
| (ASE) | , 2012. | oracles for GUIs. In | Proceedings of ACM Conf. on |  |  |
| Automated concolic testing of smartphone apps. In | [21] A. Memon and M. Soffa. Regression testing of GUIs. |  |  |  |  |
| Proceedings of ACM Conf. on Foundations of Software | In | Proceedings of ACM Conf. on Foundations of |  |  |  |
| Engineering (FSE) | , 2012. | Software Engineering (FSE) | , 2003. |  |  |
| [10] R. Bryce, S. Sampath, and A. Memon. Developing a | [22] N. Mirzaei, S. Malek, C. Pasareanu, N. Esfahani, and |  |  |  |  |
| single model and test prioritization strategies for | R. Mahmood. Testing Android apps through symbolic |  |  |  |  |
| event-driven software. | Trans. on Soft. Engr. | , 37(1), | execution. In | Java Pathfinder Workshop (JPF) | , 2012. |
| 2011. | [23] T. Takala, M. Katara, and J. Harty. Experiences of |  |  |  |  |
| [11] C. Cadar, D. Dunbar, and D. Engler. KLEE: | system-level model-based GUI testing of an Android |  |  |  |  |
| Unassisted and automatic generation of high-coverage | app. In | Proceedings of 4th Intl. Conf. on Software |  |  |  |
| tests for complex systems programs. In | Proceedings of | Testing, Verification and Validation (ICST) | , 2011. |  |  |
| 8th USENIX Symp. on Operating Systems Design and | [24] L. White and H. Almezen. Generating test cases for |  |  |  |  |
| Implementation (OSDI) | , 2008. | GUI responsibilities using complete interaction |  |  |  |
| [12] W. Enck, P. Gilbert, B.-G. Chun, L. Cox, J. Jung, | sequences. In | Proceedings of 11th IEEE Intl. Symp. on |  |  |  |
| P. McDaniel, and A. Sheth. Taintdroid: An | Software Reliability Engineering (ISSRE) | , 2000. |  |  |  |
| information-flow tracking system for realtime privacy | [25] L. Yan and H. Yin. DroidScope: Seamlessly |  |  |  |  |
| monitoring on smartphones. In | Proceedings of 9th | reconstructing the OS and Dalvik semantic views for |  |  |  |
| USENIX Symp. on Operating Systems Design and | dynamic Android malware analysis. In | Proceedings of |  |  |  |
| Implementation (OSDI) | , 2010. | 21st USENIX Security Symposium | , 2012. |  |  |
| [13] P. Gilbert, B.-G. Chun, L. Cox, and J. Jung. Vision: | [26] X. Yuan, M. Cohen, and A. Memon. GUI interaction |  |  |  |  |
| automated security validation of mobile apps at app | testing: Incorporating event context. | Trans. on Soft. |  |  |  |
| Mobile Cloud Computing and Services (MCS) | , 2011. | [27] X. Yuan and A. Memon. Generating event |  |  |  |
| [14] P. Godefroid, N. Klarlund, and K. Sen. DART: | sequence-based test cases using GUI runtime state |  |  |  |  |
| Directed automated random testing. In | Proceedings of | feedback. | Trans. on Soft. Engr. | , 36(1), 2010. |  |
