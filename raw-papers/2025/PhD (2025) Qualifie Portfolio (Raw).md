---
title: "PhD Qualifie Portfolio"
creator: "Microsoft® PowerPoint® for Microsoft 365"
pages: 37
---

# PhD Qualifie Portfolio

> **總頁數**：37 頁

---

## Page 1

MALintent

Coverage Guided Intent Fuzzing

Framework for Android

Ammar Askar, Fabian Fleischer ,

Christopher Kruegel, Giovanni Vigna,

Taesoo Kim

---

## Page 2

MALintent: Coverage Guided Android Intent Fuzzing

Android IPC-related CVEs

40

App isolation turns IPC into 35

30

a key attack vector on

25

Android

20

15

Increasing number of IPC- 10

# IPC-related CVEs

related CVEs in Android 5

0

apps

Year

2

---

## Page 3

MALintent: Coverage Guided Android Intent Fuzzing

Motivation

TracingControllerAndroidImpl

IPC

Cookies

Browser State

Visual Dump

3

---

## Page 4

MALintent: Coverage Guided Android Intent Fuzzing

Android Intents

Primary Inter Process Communication method in Android.

Intent

ACTION_SHARE

EXTRA_IMAGE:

4

*[Image: Page 4 Image]*

---

## Page 5

MALintent: Coverage Guided Android Intent Fuzzing

Android Intents

An object sent across app boundaries. Android apps are isolated and cannot

directly access each other’s data or special permissions.

Intent

Actions: ACTION_VIEW (view an image)

ACTION_DIAL (dial a number)

ACTION_SEND (send an email)

Metadata

EXTRA_EMAIL (email address to send to)

5

---

## Page 6

MALintent: Coverage Guided Android Intent Fuzzing

Android Intents

Apps can trigger intents to launch other applications.

6

---

## Page 7

MALintent: Coverage Guided Android Intent Fuzzing

Android Intents

Intents are ideal for fuzzing. They contained well-structured data and can

be sent by apps without any privilege to attack other apps.

EmailComposeActivity

ACTION_SEND

mailto:AAAAA ��

7

---

## Page 8

MALintent: Coverage Guided Android Intent Fuzzing

Overall Design

8

---

## Page 9

MALintent: Coverage Guided Android Intent Fuzzing

Design: Static Analysis

Start with the application to determine what intents can be sent to it.

AndroidManifest

Application .apk Intent Specification

App Code

9

---

## Page 10

MALintent: Coverage Guided Android Intent Fuzzing

Design: Static Analysis

AndroidManifest

10

---

## Page 11

MALintent: Coverage Guided Android Intent Fuzzing

Design: Static Analysis

Intent Specification

11

---

## Page 12

MALintent: Coverage Guided Android Intent Fuzzing

Overall Design

12

---

## Page 13

MALintent: Coverage Guided Android Intent Fuzzing

Overall Design

13

---

## Page 14

MALintent: Coverage Guided Android Intent Fuzzing

Android Native Code

There are a wealth of libraries in C/C++ that app developers use

14

---

## Page 15

MALintent: Coverage Guided Android Intent Fuzzing

Android Native Code

Interfacing with these libraries done with JNI (Java Native Interface)

Java C

15

---

## Page 16

MALintent: Coverage Guided Android Intent Fuzzing

JNI Bug Finding

Basic fuzzing loop works but it is slow for JNI bugs.

JNI Native Code

16

---

## Page 17

MALintent: Coverage Guided Android Intent Fuzzing

JNI Bug Finding

Native

Calls

17

---

## Page 18

MALintent: Coverage Guided Android Intent Fuzzing

JNI Bug Finding

Dynamic traces from real intents invoking native code

give us data-flow information

JNI Native Code

18

---

## Page 19

MALintent: Coverage Guided Android Intent Fuzzing

JNI Bug Finding

With the data and control flow information, we can generate a libFuzzer

harness

19

---

## Page 20

MALintent: Coverage Guided Android Intent Fuzzing

JNI Bug Finding

Example bug found in the

Facebook Fresco image

library.

20

---

## Page 21

MALintent: Coverage Guided Android Intent Fuzzing

Privacy Violations

Improper intent handling may introduce vulnerabilities

Intent

VIDEO_CAPTURE

EXTRA_PATH:

/data/local/tmp/...

| Access | Save tmp file |
| --- | --- |
| file | to shared |

storage

21

---

## Page 22

MALintent: Coverage Guided Android Intent Fuzzing

Privacy Violations: Attack Scenarios

| Data leak through | Permission | Call without user |
| --- | --- | --- |
| file system | escalation | interaction |

Intent

Intent

| TAKE_PIC | Intent |  |
| --- | --- | --- |
| No camera | Camera | No user |
| permission | permission | interaction |

necessary

Data flow analysis to detect privacy violations

22

*[Image: Page 22 Image]*

---

## Page 23

MALintent: Coverage Guided Android Intent Fuzzing

Privacy Violations: Attack Scenarios

| Data leak through | Permission | Call without user |
| --- | --- | --- |
| file system | escalation | interaction |

Intent

Intent

| TAKE_PIC | Intent |  |
| --- | --- | --- |
| No camera | Camera | No user |
| permission | permission | interaction |

necessary

23

---

## Page 24

MALintent: Coverage Guided Android Intent Fuzzing

Privacy Violations

Dynamic taint analysis to identify leaking resources

Private Data Sources Intent Data

CameraDevice.

location.

CreateCapture

getLatitude() Extras

Session()

SQLiteDatabase

... URI

.query()

Sinks

Filesystem Network Call

24

---

## Page 25

MALintent: Coverage Guided Android Intent Fuzzing

Evaluation

Ran against 500 F- Droid and Google Play Store’s top -50 and top-50 productivity apps.

F-Droid Google Play 16 hours of

Store

Fuzzing / App

25

---

## Page 26

MALintent: Coverage Guided Android Intent Fuzzing

Evaluation Results

9 49 1

Privacy

| Crashes | Memory |
| --- | --- |
| Violations | Safety |

26

---

## Page 27

MALintent : Coverage Guided Intent

Fuzzing Framework for Android

| • | Framework for fuzzing Intent handlers in Android apps |
| --- | --- |
| • | Includes oracles for bug detection |

→ Privacy violations, memory safety, crashes

| • | Found 49 crashes, 9 privacy violations, and 1 memory safety bug |
| --- | --- |
| • | Open-source implementation available |

Ammar Askar, Fabian Fleischer , Christopher Kruegel, Giovanni Vigna, Taesoo Kim

Network and Distributed System Security (NDSS) Symposium 2025. San Diego, CA.

aaskar@gatech.edu, fleischer@gatech.edu

Paper

27

*[Image: Page 27 Image]*

---

## Page 28

MALintent: Coverage Guided Android Intent Fuzzing

Design: Static Analysis

App Code

28

---

## Page 29

MALintent: Coverage Guided Android Intent Fuzzing

Android Native Code

Since it’s native code, it’s subject to memory -safety issues.

29

---

## Page 30

MALintent: Coverage Guided Android Intent Fuzzing

Android Native Code

and… Intent handlers can

and do invoke native code

30

---

## Page 31

MALintent: Coverage Guided Android Intent Fuzzing

Android Native Code

JNI allows access to Java data from C/C++ land

31

---

## Page 32

MALintent: Coverage Guided Android Intent Fuzzing

JNI Bug Finding

Key is to isolate this portion and run it as fast as possible

JNI Native Code

32

---

## Page 33

MALintent: Coverage Guided Android Intent Fuzzing

JNI Bug Finding

Generate fuzzing harnesses from how the Java code uses native

libraries, and then directly fuzz the library.

Harness

JNI Native Code

JNI Native Code

33

---

## Page 34

MALintent: Coverage Guided Android Intent Fuzzing

JNI Bug Finding

Challenge: data

flow and method

| invocations to | jni_funcA |
| --- | --- |
| native code | long this.ptr; |

return struct_ptr

// ...

this.ptr = jni_funcA (…) jni_funcB

jni_funcB(this.ptr , …) struct_t ptr = …;

ptr->field_a;

JNI Native Code

34

---

## Page 35

MALintent: Coverage Guided Android Intent Fuzzing

Evaluation

System Coverage Bug Types

Instrumentation

| MALintent | Yes | Crashes, Privacy, Memory |  |
| --- | --- | --- | --- |
| IccDroid | Only with Source Code | Crashes |  |
| Intents of Death | Only with Source Code | Crashes |  |
| DroidFuzzer | No | Crashes |  |
| Demissie | et al. | No | Privacy |
| AndroidIntentFuzzer | No | Crashes |  |
| MindMacIntentFuzzer | No | Crashes |  |

34

---

## Page 36

MALintent: Coverage Guided Android Intent Fuzzing

Evaluation

Coverage comparison

between MALintent and

IccDroid (previous state-of-

the-art)

IccDroid does not support

coverage instrumentation

without source code.

34

---

## Page 37

MALintent: Coverage Guided Android Intent Fuzzing

Bugs Found

| App | Component | Oracle | Description |  |  |
| --- | --- | --- | --- | --- | --- |
| Instagram | libnative-filters.so | Memory Safety | Out-of-bounds write in Fresco GUI library. |  |  |
| Chrome | TracingController | Privacy | Exposed profiler leaks private browser data. |  |  |
| WhatsApp | CameraActivity | Privacy | Sending an intent with | add_more_images | causes image |

to be taken without interaction.

TextNow DialerActivity Privacy Intent with answer_call and phone_number causes app to

dial number and pick up automatically.

AndroODB GPS GpsProvider Privacy GPSProvider leaks location data in the form of an intent

result.

Rethink DNS HomeScreenActivity Privacy Allows restoring configs from backup, can set a malicious

DNS server and intercept all traffic.

OpenGPX CacheListActivity Privacy App accepts arbitrary URI when copying gpx map file. Allows

leak of all app data.

…

34
