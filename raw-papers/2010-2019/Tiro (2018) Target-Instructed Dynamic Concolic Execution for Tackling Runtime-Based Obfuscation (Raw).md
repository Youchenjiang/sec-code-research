---
title: "20_Wong_&_Lie,_TIRO_Tackling_Runtime-Based_Obfuscation"
creator: "LaTeX with hyperref package"
pages: 17
---

# 20_Wong_&_Lie,_TIRO_Tackling_Runtime-Based_Obfuscation

> **總頁數**：17 頁

---

## Page 1

Tackling runtime-based obfuscation

in Android with T iro

Michelle Y. Wong and David Lie, University of Toronto

https://www.usenix.org/conference/usenixsecurity18/presentation/wong

This paper is included in the Proceedings of the

27th USENIX Security Symposium.

August 15–17, 2018 • Baltimore, MD, USA

ISBN 978-1-939133-04-5

Open access to the Proceedings of the

27th USENIX Security Symposium

is sponsored by USENIX.

*[Image: Page 1 Image]*

*[Image: Page 1 Image]*

---

## Page 2

Tackling runtime-based obfuscation in Android with T IRO

Michelle Y. Wong and David Lie

University of Toronto

Abstract analysis as well for efficiency and greater code cover-

Obfuscation is used in malware to hide malicious activ-

ity from manual or automatic program analysis. On the

Android platform, malware has had a history of using ob-

fuscation techniques such as Java reflection, code pack-

ing and value encryption. However, more recent mal-

ware has turned to employing obfuscation that subverts

the integrity of the Android runtime (ART or Dalvik), a

technique we call runtime-based obfuscation . Once sub-

verted, the runtime no longer follows the normally ex-

pected rules of code execution and method invocation,

raising the difficulty of deobfuscating and analyzing mal-

ware that use these techniques.

In this work, we propose T IRO , a deobfuscation

framework for Android using an approach of T arget-

I nstrument- R un- O bserve. T IRO provides a unified

framework that can deobfuscate malware that use a com-

bination of traditional obfuscation and newer runtime-

based obfuscation techniques. We evaluate and use

T IRO on a dataset of modern Android malware samples

and find that T IRO can automatically detect and reverse

language-based and runtime-based obfuscation. We also

evaluate T IRO on a corpus of 2000 malware samples

from VirusTotal and find that runtime-based obfuscation

techniques are present in 80% of the samples, demon-

strating that runtime-based obfuscation is a significant

tool employed by Android malware authors today.

age [1, 2, 12]. As a result, malware authors have increas-

ingly turned to obfuscation to hide their actions and con-

fuse both static and dynamic analysis tools. The presence

of obfuscation does not indicate malicious intent in and

of itself, as many legitimate applications employ code

obfuscation to protect intellectual property. However, be-

cause of its prevalence among malware, it is crucial that

malware analyzers have the ability to deobfuscate An-

droid applications in order to determine if an application

is indeed malicious or not.

There exist a variety of obfuscation techniques on the

Android platform. Many common techniques, such as

Java reflection, value encryption, dynamically decrypt-

ing and loading code, and calling native methods have

been identified and discussed in the literature [11,22,26].

These techniques have a common property in that they

exploit facilities provided by the Java programming lan-

guage, which is the main development language for An-

droid applications, and thus we call these language-

based obfuscation techniques. In contrast, malware au-

thors may eschew Java and execute entirely in native

code, obfuscating with techniques seen in x86 mal-

ware [3, 8, 17, 20, 24]. We call this technique full-native

code obfuscation .

In this paper, we identify a third option—obfuscation

techniques that subvert ART, the Android RunTime,

which we call runtime-based obfuscation techniques.

These techniques subtly alter the way method invoca-

obfuscation has advantages over both language-based

| 1 | Introduction | tions are resolved and code is executed. Runtime-based |
| --- | --- | --- |
| There are currently an estimated 2.8 million applica- | and full-native code obfuscation. While language-based |  |
| tions on the Google Play store, with thousands being | obfuscation techniques have to occur immediately before |  |
| added and many more existing applications being up- | the obfuscated code is called, runtime-based obfuscation |  |
| dated daily. | A large market with many users naturally | techniques can occur in one place and alter code exe- |
| draws attackers who create and distribute malicious ap- | cution in a seemingly unrelated part of the application. |  |
| plications (i.e. malware) for fun and profit. While dy- | This significantly raises the difficulty of deobfuscating |  |
| namic analyses [10, 27, 28, 34] can be used to detect | code, as code execution no longer follows expected con- |  |
| and analyze malware, anti-malware tools often use static | ventions and analysis can no longer be performed piece- |  |
| USENIX Association | 27th USENIX Security Symposium | 1247 |

---

## Page 3

| meal on an application, but must examine the entire ap- | 2. We present the design and implementation of T | IRO | , |
| --- | --- | --- | --- |
| plication as a whole. Compared to full-native code ob- | a framework for Android-based deobfuscation that |  |  |
| fuscation, runtime-based obfuscation allows a malware | can handle both language-based and runtime-based |  |  |
| developer to still use the convenient Java-based API li- | obfuscation techniques. |  |  |

braries provided by the framework. Malware that use na-

tive code obfuscation will either have to use language- or

runtime-based obfuscation to hide its Android API use,

or risk compatibility loss if it tries to access APIs directly.

Our study of obfuscated malware suggests that authors

almost universally employ language- and runtime-based

methods to hide their use of Android APIs in Java.

To study both language- and runtime-based obfusca-

mine whether obfuscation occurred and if so, produce

the deobfuscated code. T IRO performs these steps itera-

tively until it can no longer detect any new obfuscation.

obfuscation, T IRO can incrementally increase the com-

IntelliDroid improves T IRO ’s efficiency by targeting its

dynamic analysis toward obfuscation code and T IRO im-

proves IntelliDroid’s completeness by incorporating de-

obfuscated information back into its targeting. Succes-

sive iterations allow each to refine the results of the other.

1. We identify and describe a family of runtime-based

obfuscation techniques in ART, including DEX file

hooking, class modification, ArtMethod hooking,

method entry-point hooking and instruction hook-

3. We evaluate T IRO on a corpus of 34 modern mal-

ware samples provided by the Android Malware

team at Google. We also run T IRO on 2000 obfus-

cated malware samples downloaded from VirusTo-

tal to measure the prevalence of various runtime-

based obfuscation techniques in the wild and find

that 80% use a form of runtime-based obfuscation.

2 Background

mance.

Reflection. Java provides the ability to dynamically in-

stantiate and invoke methods using reflection. Because

the target of reflected method invocations is only known

at run-time, this frustrates static analysis and can make

the targets of these calls unresolvable (e.g. by using

cesses.

Value encryption. Key values and strings in an applica-

tion can be encrypted so they are not visible to static anal-

ysis. When executed, code in the application decrypts

| tion in Android malware, we propose T | IRO | , a tool that | We begin by providing background on the Android |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| can handle both types of obfuscation techniques within | runtime and classical language-based obfuscation tech- |  |  |  |  |  |  |  |  |  |  |  |  |
| a single deobfuscation framework. T | IRO | is an acronym | niques in Section 2. | We then introduce and explain |  |  |  |  |  |  |  |  |  |
| for the automated approach taken to defeat obfuscation | runtime-based obfuscation techniques in Section 3. We |  |  |  |  |  |  |  |  |  |  |  |  |
| — | T | arget- | I | nstrument- | R | un- | O | bserve. T | IRO | first analyzes | present T | IRO | , a deobfuscation framework that can han- |
| the application code to target locations where obfusca- | dle both language- and runtime-based obfuscation in |  |  |  |  |  |  |  |  |  |  |  |  |
| tion may occur, and applies instrumentation either in the | Section 4 and provide implementation details in Sec- |  |  |  |  |  |  |  |  |  |  |  |  |
| application or runtime to monitor for obfuscation and | tion 5. | We present an analysis of obfuscated Android |  |  |  |  |  |  |  |  |  |  |  |
| collect run-time information. | T | IRO | then runs the ap- | malware in Section 6 and show how T | IRO | can deobfus- |  |  |  |  |  |  |  |
| plication with specially generated inputs that will trig- | cate these applications. We analyze our findings and our |  |  |  |  |  |  |  |  |  |  |  |  |
| ger the instrumentation. Finally, T | IRO | observes the re- | limitations in Section 7. | Related work is discussed in |  |  |  |  |  |  |  |  |  |
| sults of running the instrumented application to deter- | Section 8. Finally, we conclude in Section 9. |  |  |  |  |  |  |  |  |  |  |  |  |
| This iterative mechanism enables it to work on a variety | Android applications are implemented in Java, compiled |  |  |  |  |  |  |  |  |  |  |  |  |
| of obfuscated applications and techniques. | into DEX bytecode, and executed in either the Dalvik |  |  |  |  |  |  |  |  |  |  |  |  |
| T | IRO | ’s hybrid static-dynamic design is rooted in an | Virtual Machine or the Android Runtime (ART). | 1 | The |  |  |  |  |  |  |  |  |
| integration with IntelliDroid [31], which implements tar- | Dalvik VM, used in Android versions prior to 4.4, inter- |  |  |  |  |  |  |  |  |  |  |  |  |
| geted dynamic execution for Android applications. T | IRO | prets the DEX bytecode and uses just-in-time (JIT) com- |  |  |  |  |  |  |  |  |  |  |  |
| uses this targeting to drive its dynamic analysis to lo- | pilation for frequently executed code segments. ART, a |  |  |  |  |  |  |  |  |  |  |  |  |
| cations of obfuscation, saving it from having to execute | separate runtime introduced in Android 4.4 and set as the |  |  |  |  |  |  |  |  |  |  |  |  |
| unrelated parts of the application. However, IntelliDroid | default in Android 5.0, adds ahead-of-time (AOT) com- |  |  |  |  |  |  |  |  |  |  |  |  |
| uses static analysis and is susceptible to language-based | pilation (using the | dex2oat | tool) to a DEX interpreter. |  |  |  |  |  |  |  |  |  |  |
| and runtime-based obfuscation, which can make its anal- | Starting in Android 7.0, ART also includes profile-based |  |  |  |  |  |  |  |  |  |  |  |  |
| ysis incomplete. By using an iterative design that feeds | smart compilation that uses a mixture of interpretation, |  |  |  |  |  |  |  |  |  |  |  |  |
| dynamic information back into static analysis for de- | JIT, and AOT compilation to boost application perfor- |  |  |  |  |  |  |  |  |  |  |  |  |
| pleteness of this targeting, which further improves its de- | We briefly discuss traditional language-based obfusca- |  |  |  |  |  |  |  |  |  |  |  |  |
| obfuscation capabilities. In this synergistic combination, | tion and full-native code obfuscation techniques: |  |  |  |  |  |  |  |  |  |  |  |  |
| We make three main contributions in this paper: | an encrypted string), thus hiding call edges and data ac- |  |  |  |  |  |  |  |  |  |  |  |  |
| ing/overwriting. | 1 | https://source.android.com/devices/tech/dalvik/ |  |  |  |  |  |  |  |  |  |  |  |
| 1248 | 27th USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 4

| the values, allowing the application to use the plain text | Java code. As a result, applications that use native code |
| --- | --- |
| at run-time. Value encryption is often combined with re- | obfuscation still need obfuscation for Java code if they |
| flection to hide the names of classes or methods targeted | want to be able to make Android API calls reliably. |

by reflected calls.

plication package (APK) can be executed through dy-

tively or in native code, using multiple layers of obfusca-

tion to increase the difficulty of analysis.

Native methods. Java applications may use the Java Na-

tive Interface (JNI) to invoke native methods in the appli-

cation. When used for obfuscation, malicious behavior

and method invocations can be performed in native code.

Unlike Java or DEX bytecode, native code contains no

symbol information—variables are mapped to registers

and many symbols are just addresses. Thus, static anal-

ysis of native code yields significantly less useful results

and the inclusion of native code in an application can

hide malicious activity or sensitive API invocations from

an analyzer.

from Java code without language- or runtime-based ob-

fuscation would expose the APIs calls to standard An-

droid application analysis [2, 12]. On the other hand,

calling these APIs from native code requires the appli-

3.1 DEX file and class loading

In Stage A , DEX files are loaded from disk into mem-

ory, a process that involves instantiating Java and native

objects to represent the loaded DEX file. The Java java.

lang.DexFile object is returned to the application if it

uses the DexFile.loadDex() API; in normal cases, this

object is passed to a class loader so that ART can later

load classes from the new DEX bytecode.

The class loading process, Stage B , is triggered when

a class is first requested (e.g. when it is first instantiated).

The class linker within ART searches the loaded DEX

files (in the order of loading) until it finds a class defi-

loaded class.

3.2 Code execution

| Dynamic loading. | Code located outside the main ap- | 3 | Runtime-based obfuscation |  |
| --- | --- | --- | --- | --- |
| namic code loading. | This is often used in packed ap- | Before we describe runtime-based obfuscation, we first |  |  |
| plications, where the hidden code is stored as an en- | describe how code is loaded and executed in the ART |  |  |  |
| crypted binary file within the APK package and de- | runtime. Figure 1 illustrates three major steps in loading |  |  |  |
| crypted when the application is launched. The decrypted | and invoking code. First, | A | shows how DEX bytecode |  |
| code is stored in a temporary file and loaded into the | must be identified and loaded from disk into the runtime. |  |  |  |
| runtime through the use of the dynamic loading APIs | Second, | B | is triggered when a class is instantiated by |  |
| in the | dalvik.system.DexClassLoader | and | dalvik. | the application and shows how the corresponding byte- |
| system.DexFile | classes. Normally, the temporary files | code within the DEX file is found and incorporated into |  |  |
| holding the decrypted bytecode are deleted after the load- | runtime state. Finally, | C | shows how virtual methods are |  |
| ing process to further hide or obfuscate it from analysis. | dynamically resolved via a virtual method table (vtable) |  |  |  |
| In some cases, the invocation to the dynamic loading API | and execution is directed to the target method code. We |  |  |  |
| may be obfuscated by performing the invocation reflec- | describe these steps in more detail below. |  |  |  |
| Full-native code obfuscation. | Because Android appli- | nition entry ( | class_def_item | ) matching the requested |
| cations can execute code natively, it would also be possi- | class name. | The associated class data is parsed from |  |  |
| ble to implement an entire Android application in native | the DEX file, now loaded in memory, and a | Class | ob- |  |
| code and utilize native code obfuscation techniques. Na- | ject is used to represent this class in ART. In addition, |  |  |  |
| tive code obfuscation has a long history on x86 desktop | data for class members are also parsed, and | ArtField | or |  |
| systems, and can be extremely resistant to analysis [3]. | ArtMethod | objects created to represent them. To handle |  |  |
| The primary drawback to this approach is that access | polymorphism, a vtable is stored for each class and used |  |  |  |
| to Android APIs, which can reveal the user’s location | to resolve virtual method invocations efficiently. The ta- |  |  |  |
| and give access to various databases containing the user’s | ble is initially populated by pointers to | ArtMethod | in- |  |
| contacts, calendar and browsing history, can only be re- | stances from the superclass (i.e. inherited methods). For |  |  |  |
| liably accessed via API stubs in the Java framework li- | overridden methods, their entries in the table are replaced |  |  |  |
| brary provided by the OS. On one hand, calling APIs | with pointers to the | ArtMethod | instances for the current |  |
| cation to correctly guess the Binder message format that | When a non-static virtual invocation is made, marked by |  |  |  |
| the services on the Android system are using. Because | Stage | C | , the target method must be resolved. The res- |  |
| the ecosystem of Android is very fragmented, | 2 | this poses | olution begins by determining the receiver object’s type, |  |
| a challenge for malware that wishes to avoid executing | which references a | Class | object. The method specified |  |
| 2 | https://developer.android.com/about/dashboards/ | in the invocation is used to index into the vtable of this |  |  |
| index.html | class, thereby obtaining the target | ArtMethod | object to |  |
| USENIX Association | 27th USENIX Security Symposium | 1249 |  |  |

---

## Page 5

| disk | DEX file (mmap) | Class |
| --- | --- | --- |
| 011001000110 | <headers> | ... |

010101111000 ...

001000000110

011001101001

class_def_item

...

| A | class_data_item |
| --- | --- |
| java.lang. | ... |

DexFile

method_data_item 3

...

1

| mCookie | ... |
| --- | --- |
| ... | code_item |

code loading and

begin_ X execution

2

pointers/state stored

#

... in ART

Figure 1: ART state for code loading and execution

compiled mode). A set of entry-points are stored with

the ArtMethod to handle each case (see 5 ); each is

vtable_

4 virtual methods table

Parameters

... Target method

B

ArtMethod

...

6

code_item_offset_

...

5

..._entry_point_ Set up

..._entry_point_

Execute code

more detail below:

terpart, the DexFile::mCookie Java field stores point-

ers to the associated native art::DexFile instances that

| 011011000110 | Invocation | C |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0101........ | Receiver |  |  |  |  |  |  |
| art::DexFile | ..._entry_point_ | Trampoline |  |  |  |  |  |
| ... | ..._entry_point_ | function | : |  |  |  |  |
| mapped DEX file ptr | Obtain code ptr |  |  |  |  |  |  |
| invoke (see | 4 | in Figure 1). The actual invocation pro- | runtime from the application). | 4 | - | 6 | indicates runtime |
| cedure depends on the method type (e.g. Java or native) | state that can be subverted to alter the code that a method |  |  |  |  |  |  |
| and the current runtime environment (e.g. interpreter or | invocation resolves to. We describe these techniques in |  |  |  |  |  |  |
| essentially a function pointer/trampoline that performs | 1 | 2 | DEX file hooking. | When loading a DEX |  |  |  |
| any necessary set-up, obtains and executes the method’s | file, the | dalvik.system.DexFile | class is used in Java |  |  |  |  |
| DEX or OAT code, and performs clean-up. While Fig- | code to identify the loaded file; however, the bulk of |  |  |  |  |  |  |
| ure 1 shows only how the DEX code pointer is retrieved | the actual loading is performed by native code in the |  |  |  |  |  |  |
| for a method (see | 6 | ), OAT code pointers for compiled | runtime, using a complementary native | art::DexFile |  |  |  |
| code are obtained in an analogous way. | class. | To reconcile the Java class with its native coun- |  |  |  |  |  |
| 3.3 | Obfuscation techniques | represent this DEX file. When classes are loaded later, |  |  |  |  |  |
| Runtime-based obfuscation redirects method invocations | this Java field is used to access the corresponding na- |  |  |  |  |  |  |
| by subverting runtime state at a number of points during | tive | art::DexFile | instance, which holds a pointer to |  |  |  |  |
| the code loading and execution process outlined above. | the memory address where the DEX file has been load- |  |  |  |  |  |  |
| Because runtime-based obfuscation works by modifying | ed/mapped. Obfuscation techniques can use reflection to |  |  |  |  |  |  |
| the state of the runtime, it must acquire the addresses of | access the private | mCookie | field and redirect it to another |  |  |  |  |
| the runtime objects it needs to modify, which is normally | art::DexFile | object, switching an apparently benign |  |  |  |  |  |
| done using reflection, and modify them using native code | DEX file with one that contains malicious code. In most |  |  |  |  |  |  |
| invoked via JNI (since Java memory management would | cases, the malicious DEX file is loaded using non-API |  |  |  |  |  |  |
| prevent code in Java from modifying ART runtime ob- | methods and classes within native code, or is dynami- |  |  |  |  |  |  |
| jects). | In total, our analysis with T | IRO | has identified | cally generated in memory, further hiding its existence. |  |  |  |
| six different techniques used by malware to obfuscate the | Similarly, instead of modifying the | mCookie | field, the |  |  |  |  |
| targets of method invocations. In Figure 1, | 1 | - | 3 | indi- | obfuscation code can also modify the | begin_ | field |
| cates runtime state that can be modified to hijack the code | within the | art::DexFile | native class and redirect it to |  |  |  |  |
| loading process such that the state is initialized with un- | another DEX file. However, this approach can be more |  |  |  |  |  |  |
| expected data (with respect to the input provided to the | brittle since the obfuscation code must make assump- |  |  |  |  |  |  |
| 1250 | 27th USENIX Security Symposium | USENIX Association |  |  |  |  |  |

---

## Page 6

tions about the location of the begin_ field within the Class objects, reflection via the JNI can be used to ob-

object. tain the Java Method object and through this, the obfus-

3 Class data overwriting. Obfuscation code can

also directly modify the contents of the memory-mapped

DEX file to alter the code to be executed. DEX files

follow a predetermined layout that separates class dec-

Both

the location of the code implementing a method. This

can be done en masse or in a piecemeal fashion, where

each class or method is modified immediately before it

is first used. We note that there are no bounds checks

on the pointers, so while class and method pointers nor-

mally point to definitions and code within the DEX file,

obfuscation code is free to change them to point to ob-

jects (including dynamically created ones) anywhere in

the application’s address space.

4 ArtMethod hooking. After the receiving class of

an invocation is determined, the target method is found

by indexing into the class’s vtable. Obfuscation code

can obtain a handle to a Class object using reflection

and determine the offset at which the vtable is stored.

By modifying entries in this table, the target ArtMethod

object for an invocation can be hooked so that a differ-

ent method is retrieved and executed. The target method

that is actually executed must be an ArtMethod object,

fuscation code or loaded previously from a DEX file. In

5 Method entry-point hooking. Once the target

ArtMethod object has been determined for an invoca-

tion, the method is executed by invoking one of its entry-

points, which are mere function pointers. Similar to

cation code can determine the location of the correspond-

ing ArtMethod object, which is a wrapper/abstraction

around the method. By modifying and hooking the val-

ues of these entry-points, it can change the code that is

executes it.

6 Instruction hooking and overwriting. The final

stage in the method invocation process is to retrieve the

DEX or OAT code pointers for a method and execute

the instructions; this is performed by the method’s entry-

points. These code pointers are stored and retrieved

from the ArtMethod object. Instruction hooking can be

achieved by modifying this pointer such that a different

set of instructions is referenced and executed when the

obfuscation code can essentially execute a completely

different method than what was first loaded into the run-

time. The modification of a method’s instructions can oc-

cur before or after class loading, since the runtime links

directly to the instruction array in ArtMethod objects.

It is even possible to overwrite the instructions multiple

times such that a different set of instructions is executed

every time the method is invoked.

fashion to detect and handle modern obfuscation tech-

niques in Android applications. The input to T IRO is

an APK file that might be distributed or submitted to

an application marketplace. The output is a set of de-

obfuscated information (such as statically unresolvable

| larations, class data, field data, and method data. | 3 | executed when the method is invoked. |  |  |
| --- | --- | --- | --- | --- |
| the class data pointer ( | class_data_item | ), which de- | Although the new entry-point code can be arbitrary na- |  |
| termines where information for a class is stored, and | tive code, there exists a number of method hooking li- |  |  |  |
| method data pointer ( | method_data_item | ), which de- | braries [18, 19, 35] that allow an application developer |  |
| termines where information is stored for a method, are | to specify pairs of hooked and target methods in Java. |  |  |  |
| prime targets for such modification. Modifying the class | They use method entry-point hooking so that a generic |  |  |  |
| data pointer allows the obfuscation code to replace the | look-up method is executed when the hooked methods |  |  |  |
| class definition with a different class while modifying the | are invoked. This look-up method determines the regis- |  |  |  |
| method definition allows the obfuscation code to change | tered target method for a hooked method invocation and |  |  |  |
| Class declarations ( | class_def_item | ) are not normally | method is invoked. Alternatively, instruction overwriting |  |
| modified by obfuscation code since this top level object | can be achieved by accessing the memory referenced by |  |  |  |
| is often read and cached into an in-memory data structure | this pointer and performing in-place modification of the |  |  |  |
| for fast lookup. If the obfuscation code misses the small | code—this normally requires the original instruction ar- |  |  |  |
| window where the DEX file is loaded but this data struc- | ray to be padded with NOPs (or other irrelevant instruc- |  |  |  |
| ture has not yet been populated, any modifications to the | tions) to ensure sufficient room for the newly modified |  |  |  |
| class declarations will not take effect in the runtime. | code. While the invocation target does not change, the |  |  |  |
| which might have been dynamically generated by the ob- | 4 | T | IRO | : A hybrid iterative deobfuscator |
| the latter case, the use of virtual method hooking is to | To address language-based and runtime-based obfusca- |  |  |  |
| hide the invocation and have malicious code appear to | tion techniques, we describe T | IRO | , a deobfuscator that |  |
| be dead. The feasibility of this type of modification for | handles both types of obfuscation. At a high level, T | IRO |  |  |
| obfuscation was established in [6]. | combines static and dynamic techniques in an iterative |  |  |  |
| 3 | https://source.android.com/devices/tech/dalvik/ | run-time values, dynamically loaded code, etc.) that can |  |  |
| dex-format | be passed into existing security analysis tools to increase |  |  |  |
| USENIX Association | 27th USENIX Security Symposium | 1251 |  |  |

---

## Page 7

| their coverage, or used by a human analyst to better un- | build the static analysis portion of T | IRO | on top of Intel- |  |  |
| --- | --- | --- | --- | --- | --- |
| derstand the behaviors of an Android application. | liDroid [31], a tool for targeted execution of Android ap- |  |  |  |  |
| The main design of T | IRO | is an iterative loop that in- | plications. | Given a list of targets (i.e. | locations in the |
| crementally deobfuscates applications in four steps: | code), IntelliDroid automatically extracts call paths to |  |  |  |  |

T arget: We use static analysis to target locations

where obfuscation is likely to occur. For language-

based obfuscation, these are invocations to the meth-

ods used for the obfuscation (e.g. reflection APIs with

non-constant target strings). For runtime-based obfus-

cation, we target native code invocations as these are

necessary to modify the state of the ART runtime.

strumentation reports the dynamic information neces-

R un: We execute the obfuscated code dynamically

and trigger the application to deobfuscate/unpack and

execute the code.

T IRO ’s iterative process allows for deobfuscation of

multiple layers or forms of obfuscation used by an ap-

plication, since the deobfuscation of one form may re-

veal further obfuscation. This is motivated by our find-

ings that obfuscated code often combines several obfus-

contains code that has been obfuscated with a different

4.1 Targeting obfuscation

these targets and generates constraints on the inputs that

trigger these paths. An associated dynamic client solves

these constraints at run-time, assembles the input object

from the solved values, and injects the input objects to

trigger the paths. Using IntelliDroid, T IRO specifies lo-

cations of obfuscation as targets. While recent Android

obfuscators generally automatically unpack application

code at startup (and thus require no special inputs), an

cific circumstances [25].

are visible in static analysis and the targets provided to

IntelliDroid are invocations to reflection APIs, dynamic

loading APIs, and native methods. For runtime-based

obfuscation, while the obfuscated code is executed in the

OnLoad function in the loaded native library). While this

is an over-approximation, targeting native code will en-

sure that any runtime-based obfuscation can be detected

in the instrumentation phase.

ports the values of unresolved variables to logcat , An-

droid’s logging facility. A separate process monitors

the log and keeps a record of the dynamic information

| I nstrument: | We statically instrument the application | added benefit of targeting is that we can use IntelliDroid |  |  |
| --- | --- | --- | --- | --- |
| and the ART runtime to monitor for language-based | to generate inputs to trigger paths in future obfuscated |  |  |  |
| and runtime-based obfuscation, respectively. This in- | code that may only unpack sections of code under spe- |  |  |  |
| sary for deobfuscation. | For language-based obfuscation, obfuscation locations |  |  |  |
| O bserve: | We observe and collect the deobfuscated | runtime (i.e. in Java/DEX bytecode), the actual obfusca- |  |  |
| information reported by the instrumentation during | tion is done in native code as described in Section 3.3. |  |  |  |
| dynamic analysis. | If T | IRO | discovers that the de- | IntelliDroid is currently unable to target locations in- |
| obfuscation reveals more obfuscated code, it iterates | side native code. As a result, we instead target all Java |  |  |  |
| through the above steps on the new code until it has | entry-points into application-provided native code, such |  |  |  |
| executed all targeted locations that could contain ob- | as invocations to native methods and to native code load- |  |  |  |
| fuscation. | ing APIs (e.g. | System.load() | , which calls the | JNI_ |
| cation techniques and that deobfuscated code often itself | 4.2 | Instrumenting obfuscation locations |  |  |
| technique. For instance, an application that dynamically | Once all of the target obfuscation locations have been |  |  |  |
| modifies DEX bytecode in memory often uses reflection | identified, | T | IRO | instruments the application and the |
| to obtain classes and invoke methods in the obfuscated | ART runtime such that any detected obfuscation is re- |  |  |  |
| code. Without supporting both forms of obfuscation, ei- | ported and deobfuscated values/code are extracted. For |  |  |  |
| ther the deobfuscated reflection target is useless without | language-based obfuscation, T | IRO | instruments applica- |  |
| the bytecode for the target method, or the extracted ob- | tion code since that is where the actual obfuscation oc- |  |  |  |
| fuscated code appears dead since the only invocation into | curs. | The instrumented code is inserted immediately |  |  |
| it is reflective. | before the target locations and the instrumentation re- |  |  |  |
| A fundamental part of T | IRO | ’s framework is the abil- | reported. | For example, to deobfuscate a statically un- |
| ity to both detect potential obfuscation (i.e. | targeting) | resolvable reflection invocation, the parameters to the |  |  |
| and to perform deobfuscation (i.e. observation). With- | invocation are logged (as well as the exact location |  |  |  |
| out targeting, T | IRO | would need to instrument and ob- | where invocation occurs, to disambiguate between mul- |  |
| serve all program paths, which could be infinite in num- | tiple uses of reflection). To deobfuscate dynamic load- |  |  |  |
| ber. Targeting enables T | IRO | to only instrument and ob- | ing, part of the instrumentation will store the loaded |  |
| serve the program paths that are involved in deobfuscat- | code in a T | IRO | -specific device location and report this |  |
| ing or unpacking obfuscated code. For this reason, we | location in the log. Native code transitions are also de- |  |  |  |
| 1252 | 27th USENIX Security Symposium | USENIX Association |  |  |

---

## Page 8

obfuscated by instrumenting calls from Java into native 4.3 Running obfuscated code

code and Java methods that can be called from native

| code. This allows T | IRO | to create control-flow connec- | T | IRO | substitutes the original application with its instru- |
| --- | --- | --- | --- | --- | --- |
| tions of the type: | Java caller | → | [native code] | mented code and uses IntelliDroid’s targeting capabili- |  |
| → | Java callee | , which helps shed light into what ac- | ties to compute and inject the appropriate inputs to run |  |  |
| tions are being taken in the native code of an application, | the instrumented obfuscation locations. However, doing |  |  |  |  |
| even though T | IRO | does not perform native code analysis. | this on obfuscated code raises an additional challenge— |  |  |
| For runtime-based obfuscation, T | IRO | instruments the | many instances of obfuscated applications also contain |  |  |
| ART runtime. Since the result of this modification is the | integrity checks that check for tampering of applica- |  |  |  |  |
| execution of unexpected code on a method invocation, | tion code and refuse to run if instrumentation is de- |  |  |  |  |
| one approach might be to record the code that was loaded | tected. | We found that the most robust method for cir- |  |  |  |
| into the runtime for a given method and check whether | cumventing these checks is to return (i.e. | spoof) the |  |  |  |
| this code has been modified at the time of invocation. | original code when classes are accessed by the applica- |  |  |  |  |
| However, this poses a catch-22 situation: to detect the | tion and return instrumented code when accessed by the |  |  |  |  |
| obfuscation, T | IRO | would have to target the obfuscated | runtime for execution. To avoid conflicts with any run- |  |  |
| method but with runtime-based obfuscation, the obfus- | time state modification that may be performed by obfus- |  |  |  |  |
| cation code could modify any class or method in the pro- | cation code, T | IRO | checks if any state modifications tar- |  |  |
| gram. It would be impractical to target every method in | get instrumented code and if so, T | IRO | aborts execution |  |  |
| the program. Instead, we use the fact that runtime-based | of the instrumented code and allows the modifications to |  |  |  |  |
| obfuscation must rely on native code to do the actual state | be performed on the original application code instead. In |  |  |  |  |
| modification. As a result, to detect runtime-based obfus- | the next iteration, after extracting the modified code, the |  |  |  |  |
| cation, T | IRO | instruments transitions between native to | previously obfuscated code will be instrumented and ex- |  |  |
| Java and Java to native code to detect whether runtime | ecuted. |  |  |  |  |

state has been modified while the application was exe-

cuting native code.

The runtime state monitored is specific to the ob- 4.4 Observing deobfuscated results

jects used to load and execute code, as described in

| Section 3.3. | For example, to detect DEX file hook- | T | IRO | observes how the application either resolves and |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ing, T | IRO | finds and monitors the | DexFile::mCookie | runs sections of code (to defeat language-based obfusca- |  |  |
| and | art::DexFile::begin_ | fields of all instantiated | tion), or how the application’s obfuscation code modifies |  |  |  |
| objects for changes before and after native code exe- | the runtime state (for runtime-based obfuscation). | The |  |  |  |  |
| cution. | If modifications are detected, T | IRO | reports the | results of this observation and the information provided |  |  |
| call path which triggered the modification, the element(s) | by T | IRO | ’s instrumentation are reported to the user for |  |  |  |
| that were modified and affected by the modification, and | deobfuscation of the application. |  |  |  |  |  |
| if possible, the code that is actually executed as a result | The iterative approach taken by T | IRO | also relies on |  |  |  |
| of the runtime-based obfuscation. In some cases, there | these observed results to incrementally deobfuscate lay- |  |  |  |  |  |
| are legitimate reasons why runtime state may change be- | ers of obfuscated code. For obfuscation that hides or con- |  |  |  |  |  |
| tween initial code loading and code execution (e.g. lazy | fuses invocation targets (e.g. | reflection, native method |  |  |  |  |
| linking or JIT compilation). We detect these and elimi- | invocations, method hooking), T | IRO | ’s instrumentation |  |  |  |
| nate these cases from T | IRO | ’s detection of runtime-based | reports the caller method, the invocation site, and the ac- |  |  |  |
| obfuscation. | tual method that is executed. This information is used in |  |  |  |  |  |
| Checking all runtime state for modifications can be | the next iteration to generate a synthetic edge in the static |  |  |  |  |  |
| expensive as there can be many classes and methods to | call graph that represents the newly discovered execution |  |  |  |  |  |
| check. | To reduce this cost we: (1) only monitor run- | flow. Often, this turns apparently dead code into reach- |  |  |  |  |
| time state used in the code loading and execution pro- | able code and T | IRO | will target this code on the next iter- |  |  |  |
| cess, and that are retrievable via the dynamic loading | ation. For obfuscation that executes dynamically loaded |  |  |  |  |  |
| or reflection APIs (i.e. | state stored within | DexFile | , | code (e.g. | dynamic loading, DEX file hooking, etc.), |  |
| Class | , and | Method | objects); (2) only monitor the ob- | T | IRO | ’s instrumentation extracts the code that is actually |
| jects for methods and classes used by the application, as | executed into an | extraction file | , and a process monitoring |  |  |  |
| determined by reachability analysis during T | IRO | ’s static | T | IRO | ’s instrumentation log pulls this file from the device. |  |
| phase. | This process relies on T | IRO | ’s iterative design, | The extracted code is then included in the static analysis |  |  |
| since the reachability analysis and subsequent monitor- | in the following iteration. An example of how T | IRO | iter- |  |  |  |
| ing becomes more complete as the application becomes | atively deobfuscates code from the | dexprotector | packer |  |  |  |
| progressively deobfuscated in later iterations. | is given in Appendix A. |  |  |  |  |  |
| USENIX Association | 27th USENIX Security Symposium | 1253 |  |  |  |  |

---

## Page 9

5 Implementation the call graph representing dynamically resolved/deob-

tation that deobfuscates runtime-based obfuscation.

5.1 AOSP modifications

and finally to an Object in 6.0. These changes and other

conventions that the malware relies upon (such as private

method signatures and locations of installed APKs) re-

5.3 Soot modifications

To incorporate deobfuscated values back into the static

portion of T IRO , we made several modifications to

fuscated invocations. Other deobfuscated values/vari-

of Soot.

Some obfuscated applications are armored to prevent

parsing by frameworks such as Soot. For example, there

were several instances of unparseable, invalid instruc-

6 Evaluation

of 22 different Android obfuscation tools. This dataset

and were transferred to us in two batches: one in March

samples from VirusTotal [30]. Finally, we present an

analysis of T IRO ’s performance.

6.1 General findings

| We implemented the static and dynamic portions of T | IRO | ables are tagged in the intermediate representation and |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| on top of IntelliDroid [31] and added the ART instrumen- | can be accessed in the post-call-graph-generation phases |  |  |  |  |  |  |
| The modifications to AOSP are located within the ART | tions in methods that appear to be dead code. | While |  |  |  |  |  |
| runtime code ( | art/runtime | and | libcore/libart | ). | this code is never executed, a static analysis pass would |  |  |
| We have implemented these changes on three different | still attempt to parse these instructions, resulting in er- |  |  |  |  |  |  |
| versions of AOSP: 4.4 (KitKat), 5.1 (Lollipop), and 6.0 | rors that halt the analysis. | In cases where a class def- |  |  |  |  |  |
| (Marshmallow) due to the portability issues of the DEX | inition or method implementation is malformed (which |  |  |  |  |  |  |
| file hooking technique, which is performed by most of | often occurs for applications performing DEX bytecode |  |  |  |  |  |  |
| the malware in our datasets. In order to access the private | modification), we skip these classes/methods and do not |  |  |  |  |  |  |
| DexFile::mCookie | field for DEX file hooking, appli- | produce an instrumented version. If the bytecode is mod- |  |  |  |  |  |
| cations must use reflection or JNI, but the | mCookie | field | ified at run-time, T | IRO | will extract them and instrument |  |  |
| type has changed from an | int | in 4.4, to a | long | in 5.0, | them in the following iteration. |  |  |
| sult in crashes when the applications are not executed on | To evaluate T | IRO | ’s accuracy, | we acquired a labeled |  |  |  |
| their intended Android version. | dataset of 34 malware samples, each obfuscated by one |  |  |  |  |  |  |
| 5.2 | Extending IntelliDroid | was provided by the Android Malware team at Google |  |  |  |  |  |
| T | IRO | uses IntelliDroid’s [31] static analysis to target | 2017 and another in October 2017. The samples in the |  |  |  |  |
| likely locations of obfuscation and its dynamic client to | dataset were chosen for their use of advanced obfusca- |  |  |  |  |  |  |
| compute and inject inputs that trigger these locations. | tion capabilities and difficulty of analysis, and attention |  |  |  |  |  |  |
| The deobfuscated information extracted by T | IRO | is in- | was made to ensure that they represent a wide range of |  |  |  |  |
| corporated into the static analysis prior to the call graph | state-of-the-art obfuscators. Each sample was manually |  |  |  |  |  |  |
| generation phase and the code instrumentation is per- | confirmed as malware and classified by a security ana- |  |  |  |  |  |  |
| formed after the extraction of targeted paths and con- | lyst from Google, independent of our own analysis using |  |  |  |  |  |  |
| straints. | To enable support for ART, which was intro- | T | IRO | . | To evaluate T | IRO | ’s accuracy, we shared the re- |
| duced in Android 4.4, we have ported IntelliDroid from | sults of T | IRO | ’s analysis with Google and they confirmed |  |  |  |  |
| Android 4.3 to Android 6.0. In addition, we have ported | or denied our findings on the samples. |  |  |  |  |  |  |
| IntelliDroid to use the Soot [29] static analysis frame- | In our evaluation, the static portion of T | IRO | was ex- |  |  |  |  |
| work, which provides direct support for instrumenta- | ecuted on an Intel i7-3770 (3.40GHz) machine with |  |  |  |  |  |  |
| tion of DEX bytecode via the smali/dexpler [14] library. | 32 GB of memory, 24 GB of which were provided to |  |  |  |  |  |  |
| Previously, IntelliDroid used the WALA analysis frame- | the static analysis JVM. The dynamic portion was exe- |  |  |  |  |  |  |
| work, which does not have a backend for DEX bytecode. | cuted on a Nexus 5 device running T | IRO | ’s instrumented |  |  |  |  |
| While instrumentation could have been achieved by us- | versions of Android 4.4, Android 5.1, and Android 6.0. |  |  |  |  |  |  |
| ing WALA with Java-to-DEX conversion tools [7, 21], | We begin by evaluating T | IRO | ’s accuracy, as well as de- |  |  |  |  |
| we found that malicious applications and packers often | tailing the findings made by T | IRO | on the labeled dataset. |  |  |  |  |
| use very esoteric aspects of the bytecode specification | Then, to measure the use of obfuscation on malware in |  |  |  |  |  |  |
| that are not always supported by conversion tools. | the wild, we apply T | IRO | to 2000 obfuscated malware |  |  |  |  |
| Soot [29]. Most of these changes were in the call graph | Table 1 summarizes our findings after running T | IRO | on |  |  |  |  |
| generation code, where we tag locations at which deob- | the labeled dataset. The table lists the name of the obfus- |  |  |  |  |  |  |
| fuscated values were obtained and add special edges to | cator, the number of samples from that obfuscator, the |  |  |  |  |  |  |
| 1254 | 27th USENIX Security Symposium | USENIX Association |  |  |  |  |  |

---

## Page 10

Table 1: Deobfuscation results

Obfuscation

| T | IRO | Sensitive |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Language-based | Runtime-based | APIs |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sample | # | Reflection | Dynamic | loading | Native code | DEX file | hooking | Class data | overwriting | ArtMethod | hooking | Instruction | hooking | Instruction | overwriting | Iterations | Before | After |
| aliprotect | 2 | • | n | • | • | • | 3 | 0 | 44 |  |  |  |  |  |  |  |  |  |
| apkprotect | 1 | • | d | • | 2 | 8 | 52 |  |  |  |  |  |  |  |  |  |  |  |
| appguard | 1 | • | • | • | 2 | 0 | 5 |  |  |  |  |  |  |  |  |  |  |  |
| appsolid | 1 | • | n | • | 2 | 0 | 82 |  |  |  |  |  |  |  |  |  |  |  |
| baiduprotect | 1 | • | n | • | • | • | 2 | 1 | 2 |  |  |  |  |  |  |  |  |  |
| bangcle | 1 | • | n | • | 2 | 1 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| dexguard | 3 | • | 2 | 0 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| dexprotector | 3 | • | r | • | 4 | 0 | 80 |  |  |  |  |  |  |  |  |  |  |  |
| dxshield | 2 | • | n | • | • | 2 | 3 | 25 |  |  |  |  |  |  |  |  |  |  |
| ijiamipacker | 2 | • | n | • | • | • | • | • | • | 2 | 1 | 93 |  |  |  |  |  |  |
| liapp | 1 | • | n | • | 2 | 4 | 90 |  |  |  |  |  |  |  |  |  |  |  |
| naga | 1 | • | n | • | • | 2 | 2 | 2 |  |  |  |  |  |  |  |  |  |  |
| naga_pha | 1 | • | n | • | • | • | • | • | • | 2 | 0 | 6 |  |  |  |  |  |  |
| nqprotect | 1 | • | d | • | 2 | 1 | 12 |  |  |  |  |  |  |  |  |  |  |  |
| qihoopacker | 3 | • | n | • | • | 2 | 3 | 217 |  |  |  |  |  |  |  |  |  |  |
| secshell | 2 | • | r | n | • | • | • | 2 | 200 | 287 |  |  |  |  |  |  |  |  |
| secneo | 1 | • | n | • | 3 | 0 | 12 |  |  |  |  |  |  |  |  |  |  |  |
| sqlpacker | 2 | • | d | • | 2 | 1 | 31 |  |  |  |  |  |  |  |  |  |  |  |
| tencentpacker | 2 | • | n | • | • | 3 | 3 | 504 |  |  |  |  |  |  |  |  |  |  |
| unicomsdk | 2 | • | d | • | 2 | 226 | 227 |  |  |  |  |  |  |  |  |  |  |  |
| wjshell | 1 | • | d | • | • | 2 | 8 | 13 |  |  |  |  |  |  |  |  |  |  |
| d | Direct dynamic loading invocation | r | Dynamic loading invoked via reflection | n | Dynamic loading invoked in native code |  |  |  |  |  |  |  |  |  |  |  |  |  |
| obfuscation techniques found by T | IRO | and the number | no case did T | IRO | mistake legitimate state modification |  |  |  |  |  |  |  |  |  |  |  |  |  |
| of iterations T | IRO | used to fully deobfuscate the sample. | performed by ART for an attempt to perform runtime- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| We also show the number of sensitive APIs that are stat- | based obfuscation by the application. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ically visible before and after T | IRO | ’s deobfuscation. For | We make several general observations about the re- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| obfuscation tools where there was more than one sample, | sults. First, all of the malware samples employed basic |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the table shows the results for the sample with the most | language-based obfuscation such as reflection and native |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| sensitive behaviors detected. | code usage, while roughly 53% (18/34) of the samples |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| After sharing our results with the Google Android | also employed the more advanced runtime-based obfus- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Malware team, we confirmed that T | IRO | successfully | cation techniques. | We note that none of the samples |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| found and deobfuscated the known obfuscated code in | in this set employed method entry-point hooking, per- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the applications, with the exception of the two samples | haps owing to their age as these samples are older than |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| packed with | unicomsdk | , and was able to reach and an- | those used in our VirusTotal analysis described in Sec- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| alyze the original applications (i.e. | the bytecode for | tion 6.3. In addition, all used between 2-4 layers of ob- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the underlying application before it was obfuscated or | fuscation, requiring multiple iterations by T | IRO | . These |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| packed). | On closer analysis, we found T | IRO | failed on | findings demonstrate the utility of T | IRO | ’s iterative de- |  |  |  |  |  |  |  |  |  |  |  |  |
| the | unicomsdk | samples because while T | IRO | does trigger | sign and ability to simultaneously handle multiple types |  |  |  |  |  |  |  |  |  |  |  |  |  |
| call paths that invoke dynamic loading, the obfuscation | of obfuscation. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| code tries to retrieve bytecode from a network server that | Second, many of the obfuscators employed tactics to |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| is no longer active. | Our comparison also showed that | make analysis difficult. For example, 21 of the 34 sam- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| T | IRO | did not have any false positives on the dataset—in | ples included code integrity checks that T | IRO | ’s code |  |  |  |  |  |  |  |  |  |  |  |  |  |
| USENIX Association | 27th USENIX Security Symposium | 1255 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 11

| spoofing was able to circumvent. In addition, a common | ponents declared in the manifest. In the dynamic phase, |  |  |
| --- | --- | --- | --- |
| post-loading step in most of the samples was the deletion | instrumentation of dynamic loading and reflection re- |  |  |
| of the decrypted code file after it had been loaded. This | trieved the dynamically loaded code and deobfuscated |  |  |
| made it marginally more difficult to retrieve the code, | the reflection targets. | From the run-time information |  |
| since the unpacked DEX file was unavailable after it was | gathered, T | IRO | reported that a number of class objects |
| loaded; however, since T | IRO | extracts DEX code from | were requested via reflection, but only one was instanti- |
| memory during the loading process, this did not impact | ated via a reflected call to the constructor method. |  |  |

its deobfuscation capabilities.

Finally, in all cases, the obfuscation was used to hide

calls to sensitive APIs in Java, which were used to per-

form malicious activity. The number of sensitive APIs

shown in Table 1 are the number of API calls found by

static analysis before and after running T IRO , where the

set of sensitive APIs were obtained from FlowDroid’s [2]

collection of sources and sinks. On average, T IRO ’s iter-

ative deobfuscation resulted in over 30 new hidden sen-

sitive API uses detected in each sample. The new sen-

sitive behaviors detected after T IRO ’s iterative deobfus-

cation included well-known malware behaviors such as

premium SMS abuse and access to sensitive data, includ-

ing location information and device identifiers.

We now describe in detail some of the interesting behav-

iors and obfuscation techniques T IRO uncovered:

buffer (i.e. outside the DEX file). The application stored

the new non-empty implementations.

In the second iteration, T IRO found that only the class

that was instantiated was actually present in the dynam-

ically loaded code. Further analysis showed that the ap-

plication performed a trial-and-error form of class load-

ing, where it looped through class names app.plg_v#.

Plugin (with # a sequentially increasing integer) until

it found a class object that could actually be retrieved

and instantiated. This form of class loading would have

introduced a great deal of imprecision in static analysis

since the class name was unknown and obscured by the

loop logic; however, with the dynamic information re-

trieved by T IRO , the static analysis in the subsequent iter-

ations was able to precisely identify the loaded and exe-

cuted class. During the static phase, T IRO also found two

methods within the dynamically loaded code that con-

methods did not appear to be invoked but attempting

to load them without patching Soot resulted in crashes

stemming from parsing errors.

ijiamipacker: When first installing this APK, the

| 6.2 | Sample-specific findings | tained invalid instructions and were unparseable. These |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aliprotect: | During | T | IRO | ’s | first | iteration, | we | baiduprotect / naga / naga_pha: | These samples used |
| found | that | the | APK | file | contained | only | one | class | DEX file hooking to load code dynamically but they |
| ( | StubApplication | ) | that | set | up | and | unpacked | the | would also modify the hooked DEX file multiple times |
| application’s code. Static analysis found only one case | in their execution. Each modification would change the |  |  |  |  |  |  |  |  |
| of reflection to instrument and one direct native method | data for one class but also invalidated header values in |  |  |  |  |  |  |  |  |
| invocation via | System.load() | . During dynamic anal- | another; therefore, after the DEX bytecode modification |  |  |  |  |  |  |
| ysis, we found that the sample used DEX file hooking | process had begun, no single snapshot of the DEX code |  |  |  |  |  |  |  |  |
| to load the main application code dynamically. | After | memory buffer would result in a valid DEX file. Since |  |  |  |  |  |  |  |
| loading, the obfuscated DEX file was also overwritten | T | IRO | retrieves modified code in a piecemeal fashion as |  |  |  |  |  |  |
| prior to class loading to change the bytecode defining the | the modification is detected for each class (rather than |  |  |  |  |  |  |  |  |
| application’s main activity. When extracting the modi- | taking a single snapshot of the buffer), it was able to han- |  |  |  |  |  |  |  |  |
| fied DEX bytecode, T | IRO | found that some of the class | dle the multiple code modifications and the subsequent |  |  |  |  |  |  |
| data pointers referred to locations outside the DEX code | mangling of class metadata. |  |  |  |  |  |  |  |  |
| code in separate memory locations and, | via pointer | dexprotector: | This sample highlights how T | IRO | deob- |  |  |  |  |
| arithmetic, modified the DEX class pointers to refer to | fuscates multiple layers of obfuscation and is described |  |  |  |  |  |  |  |  |
| those locations. | In the second iteration, static analysis | in Appendix A. It used a combination of reflection to in- |  |  |  |  |  |  |  |
| showed that most of the methods in the obfuscated (and | voke dynamic loading APIs ( | DexFile.loadClass() | ) |  |  |  |  |  |  |
| now extracted) DEX file were empty—when invoked, | and to invoke methods in the dynamically loaded code. |  |  |  |  |  |  |  |  |
| they would throw a run-time exception. | These empty | The loaded code included another call to | DexFile. |  |  |  |  |  |  |
| methods and classes appeared to be decoys and were | loadDex() | for a second layer of dynamic loading that |  |  |  |  |  |  |  |
| never actually executed by the application. The methods | unpacked the main activity. Further iterations deobfus- |  |  |  |  |  |  |  |  |
| and classes that were executed had undergone DEX | cated the reflected and native method invocations that |  |  |  |  |  |  |  |  |
| bytecode modification, and T | IRO | successfully extracted | formed most of the application’s call graph. |  |  |  |  |  |  |
| apkprotect: | In the first iteration, T | IRO | found several | dex2oat | tool reported a number of verification errors in |  |  |  |  |
| classes in the APK file, none of which were the com- | most of the classes. | T | IRO | ’s static analysis had similar |  |  |  |  |  |
| 1256 | 27th USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |

---

## Page 12

results but within the parseable classes, it detected in- Table 2: Obfuscation in 2000 recent VirusTotal samples

stances of reflection, native methods, and dynamic load-

bytecode for the now-parseable classes and instrumented

new cases of reflection.

qihoopacker: In addition to the DEX file hooking obfus-

cation that this sample employed, we found that it also

invoked art::RegisterNativeMethods() to redefine

the native method DexFile.getClassNameList() .

This is a form of native method hooking, where the na-

tive function attached to a method is swapped for another.

The hooked method getClassNameList() does not ac-

tually play a part in the class loading process nor was it

used by the application; however, it is useful for code

analysis as it returns a list of loaded classes and its redef-

inition made such interactive analysis more difficult.

6.3 Evaluation on VirusTotal dataset

We also use T IRO to measure the types of obfuscation

served, including method entry-point hooking. While

this dataset is larger, we speculate that these differences

and the broader use of runtime-based techniques likely

owe more to the fact that the malware in this dataset are

more recent than those in the previous labeled dataset.

The most frequent form of runtime-based obfusca-

tion found was DEX file hooking, which is likely due

to the ease of implementing the state modification (i.e.

the DexFile::mCookie field) required for the obfus-

cation. Likewise, use of instruction hooking was also

prominent, since the obfuscation required changing just

the DEX code pointer (and possibly the compiled OAT

more well-known language-based techniques.

6.4 Performance

| ing. The dynamic phase showed that some of the classes | Language-based | Runtime-based |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| with DEX verification errors were executed without er- | Reflection | 58.5 % | DEX file hooking | 64.0 % |  |  |  |
| ror due to dynamic modification of the classes’ bytecode. | Dynamic loading | 79.9 % | Class data overwriting | 0.7 % |  |  |  |
| Furthermore, the methods were modified one at a time as | Direct | 52.2 % | ArtMethod hooking | 0.5 % |  |  |  |
| they were loaded by the class loader, which was achieved | Reflected | 0.1 % | Method entry hooking | 0.3 % |  |  |  |
| by hooking a method within the class loader. In the sec- | Native | 49.2 % | Instruction hooking | 33.7 % |  |  |  |
| ond iteration, T | IRO | was able to analyze the extracted | Native code | 96.8 % | Instruction overwriting | 0.1 % |  |
| We also found that this sample suppressed log mes- | T | IRO | was run on this dataset, it exceeded the 3 hour time- |  |  |  |  |
| sages after a certain point in the unpacking process be- | out on the static analysis phase for four of the samples |  |  |  |  |  |  |
| fore the main activity was loaded. | Since T | IRO | ’s feed- | and ran out of memory on two others. Of the remaining |  |  |  |
| back system of relaying dynamic information to static | samples, all proceeded to instrumentation and analysis |  |  |  |  |  |  |
| analysis depends on instrumented log messages, this ini- | by T | IRO | ’s dynamic phase. Table 2 shows the breakdown |  |  |  |  |
| tially posed a problem for deobfuscation. | Fortunately, | of the types of obfuscation found by T | IRO | . |  |  |  |
| this sample did not suppress error logs, so T | IRO | was | On this dataset, a larger proportion (80%) of these |  |  |  |  |
| modified to write to the error log as well. A more robust | applications used runtime-based obfuscation techniques, |  |  |  |  |  |  |
| approach would be to implement a custom deobfuscation | compared to 53% on the labeled dataset. In addition, us- |  |  |  |  |  |  |
| log that only T | IRO | can access and control. | age of all types of runtime-based obfuscation were ob- |  |  |  |  |
| For completeness, we also found two publicly avail- | code pointer) in | ArtMethod | objects. Techniques that re- |  |  |  |  |
| able | method | hooking | libraries: | Legend | [18] | and | quire overwriting larger regions of memory or more pre- |
| YAHFA [19], and used these to create our own applica- | cise determination of a location to modify (e.g. | modi- |  |  |  |  |  |
| tion obfuscated with method hooking. For both libraries, | fying a vtable entry for ArtMethod hooking) were much |  |  |  |  |  |  |
| T | IRO | detected the hooked methods, which contained | less common. | This may be due to the implementation |  |  |  |
| modified method entry-point pointers. | These pointers | effort of these techniques, which require greater knowl- |  |  |  |  |  |
| were redirected to custom trampoline/bridge code that | edge of the runtime objects being modified to ensure that |  |  |  |  |  |  |
| resolved the hooked invocation and invoked the target | any overwriting maintains the expected layout of these |  |  |  |  |  |  |
| method specified by the developer. | T | IRO | heuristically | objects and preserves the stability of the runtime. How- |  |  |  |
| reported the method objects retrieved by the application | ever, we do see instances of these techniques in recent |  |  |  |  |  |  |
| that were likely to serve as target methods for this hook- | malware, and the overall frequency of runtime-based ob- |  |  |  |  |  |  |
| ing, and in the following iterations, correctly constructed | fuscation techniques in our dataset is likely in response |  |  |  |  |  |  |
| call edges between the hooked and target methods. | to advances in analyses that can deal with the simpler and |  |  |  |  |  |  |
| used by malware in the wild. | We searched VirusTotal | We evaluate the performance of the static and dynamic |  |  |  |  |  |
| for malware tagged as obfuscated or packed, and down- | phases in T | IRO | separately. | The run time of the static |  |  |  |
| loaded 2000 randomly selected samples that were sub- | component increases as iterations find and deobfuscate |  |  |  |  |  |  |
| mitted throughout the month of January 2018. | When | more code to analyze. In the first iteration of the static |  |  |  |  |  |
| USENIX Association | 27th USENIX Security Symposium | 1257 |  |  |  |  |  |

---

## Page 13

| component (where the analysis is only targeting obfusca- | formed. | This highlights the main difference between |  |  |  |
| --- | --- | --- | --- | --- | --- |
| tion locations in the original APK file), the average static | the two forms of obfuscation: in runtime-based obfusca- |  |  |  |  |
| analysis time for the samples in Table 1 is 4.3 minutes. | tion, the actual malicious behavior can be implemented |  |  |  |  |
| However, after the last iteration, the static component | in Java. | Whether this is useful to the malware devel- |  |  |  |
| takes an average of 12.2 minutes across our dataset. | oper is dependent on the type of malicious activity they |  |  |  |  |
| T | IRO | ’s instrumentation also incurs overhead in its dy- | wish to execute on a victim’s device and how they want |  |  |
| namic phase. Since the majority of obfuscation occurs | to implement it. | Many state-of-the-art obfuscators are |  |  |  |
| in the application launch phase (i.e. | when the applica- | commercial tools that add wrapper classes to an applica- |  |  |  |
| tion unpacks its main activity and other components), we | tion to pack them into an obfuscated APK and unpack |  |  |  |  |
| compare the launch time of the application when running | them when the application is launched. Runtime-based |  |  |  |  |
| in T | IRO | against the launch time in an unmodified version | obfuscation allows for complex obfuscation while still |  |  |
| of AOSP. On average, there is a 3.3 | × | slowdown, with all | allowing the users of these commercial tools to imple- |  |  |
| of the applications launching in under 11 seconds. The | ment their code in Java, which may be preferable due |  |  |  |  |
| majority of this overhead is due to the checking of ART | to ease of development. | Reusing the existing runtime |  |  |  |
| runtime state before and after native code is executed. | on Android makes it easier for commercial obfuscation |  |  |  |  |
| While this is a noticeable performance impact, we note | tools to reliably support all forms of Android applica- |  |  |  |  |
| that T | IRO | is meant for analysis and not production us- | tions. |  |  |
| age; thus, while the slowdown is large, applications still | In addition, system services are normally accessed |  |  |  |  |
| launch and run in a reasonable amount of time. To fur- | through their RPC interface, which would require a tran- |  |  |  |  |
| ther reduce performance overhead, we believe that we | sition back into the runtime and would be detected by |  |  |  |  |
| can optimize T | IRO | ’s monitoring using hardware support. | T | IRO | ’s monitoring of native-to-Java transitions. To avoid |
| Currently, a full check is performed of all tracked run- | any Java code (i.e. a true fully native application), the ap- |  |  |  |  |
| time state on every native-to-Java transition. By manip- | plication would have to access system services by calling |  |  |  |  |
| ulating memory protections or dirty bits in the hardware | the low-level Binder interface or Unix | ioctl | s directly. |  |  |
| page table to identify modified pages, and tracking which | Since the Binder library is not part of the Android NDK, |  |  |  |  |
| objects are stored on those pages, T | IRO | can reduce the | the application is then sensitive to any changes in imple- |  |  |
| number of objects it must check for modifications. | mentation in the Binder kernel driver or Android service |  |  |  |  |

7 Discussion

From our analysis of obfuscation in recent Android mal-

ware, we identify and classify a type of runtime-based

obfuscation that differs from obfuscation seen in previ-

ous work on x86 and Java. The use of a runtime intro-

full-native code obfuscation. Static analysis of native

code is more imprecise and most existing static malware

analyzers for Android are limited to Java bytecode, so

manager. We believe that this is one of the reasons why

language- and runtime-based obfuscation is so prominent

on Android despite the long history and effectiveness of

native code obfuscation on x86. As a result, for the fore-

seeable future, language- and runtime-based obfuscation

techniques will likely still be relevant techniques for ob-

fuscated code on Android.

that executes a secret bytecode. This is a complemen-

tary technique to runtime-based obfuscation and is also

7.2 Other limitations

| duces another technique of hiding code that we show is | Another form of obfuscation may be to embed a |  |  |
| --- | --- | --- | --- |
| already in use in Android malware. | natively-implemented interpreter within the application |  |  |
| 7.1 | Bypassing the runtime | a method of bypassing the ART runtime, since the inter- |  |
| Unlike language-based obfuscation where the applica- | preter would be fully implemented in native code. Simi- |  |  |
| tion abuses Java language features, runtime-based obfus- | lar to full-native code obfuscation, access to system ser- |  |  |
| cation requires modifying runtime data, which must be | vices would be limited and invocations to framework |  |  |
| done using native code. | A natural question is whether | methods would still require execution in the ART run- |  |
| runtime-based obfuscation is a stepping stone toward | time and would therefore be deobfuscated by T | IRO | . |
| a full native code application would make them ineffec- | Part of T | IRO | ’s deobfuscation focuses on retrieving DEX |
| tive. We argue that runtime-based obfuscation is not su- | bytecode that the application dynamically loads and ex- |  |  |
| perseded by full native code but is a complementary tech- | ecutes. This implicitly assumes that any manipulation of |  |  |
| nique. | the DEX bytecode is reflected in the compiled OAT or |  |  |
| In runtime-based obfuscation, native code is used to | ODEX code, and vice versa. Obfuscation code may vi- |  |  |
| modify the runtime state but the execution inevitably re- | olate this assumption and perform modifications directly |  |  |
| turns to Java code after the modifications have been per- | on the OAT or ODEX bytecode, bypassing the current |  |  |
| 1258 | 27th USENIX Security Symposium | USENIX Association |  |

---

## Page 14

| implementation of T | IRO | . However, in doing this, the ob- | used by existing Android packers and malware. |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fuscation code forgoes portability across devices, as OAT | The work that most closely resembles T | IRO | are exist- |  |  |  |  |  |  |  |
| and ODEX files are device-specific. We did not observe | ing deobfuscation tools for Android. Some focus only on |  |  |  |  |  |  |  |  |  |
| any malware instances that were device-specific in this | language-based obfuscation. | Harvester [22] uses static |  |  |  |  |  |  |  |  |
| way. If direct OAT or ODEX modification were to ex- | code slicing to execute paths leading to specific code lo- |  |  |  |  |  |  |  |  |  |
| ist, it would be straightforward to enhance T | IRO | to de- | cations, such as reflection invocations, and can log deob- |  |  |  |  |  |  |  |
| tect these modifications by monitoring | art::OatFile | fuscated values. However, code slices do not always pro- |  |  |  |  |  |  |  |  |
| objects in the same manner as | art::DexFile | objects. | duce realistic executions and it does not handle runtime- |  |  |  |  |  |  |  |
| While | we | have | identified | a | number | of | forms | of | based obfuscation. | StaDynA [38] uses a hybrid itera- |
| runtime-based obfuscation in Section 3.3, there may be | tive approach similar to T | IRO | to deobfuscate reflection |  |  |  |  |  |  |  |
| others that T | IRO | currently does not monitor, providing | and retrieve dynamically loaded code. | However, it re- |  |  |  |  |  |  |
| avenues for newer malware to avoid detection and deob- | lies on instrumentation of reflection and dynamic load- |  |  |  |  |  |  |  |  |  |
| fuscation. However, the framework proposed in T | IRO | is | ing API invocations. | Some Android unpackers, such |  |  |  |  |  |  |
| general enough to accommodate the monitoring of other | as DexHunter [36] and Android-unpacker [26], handle |  |  |  |  |  |  |  |  |  |
| forms of runtime state as they are identified. A further | certain cases of DEX file and DEX bytecode manipu- |  |  |  |  |  |  |  |  |  |
| limitation is that applications can employ x86 obfusca- | lation, but use special packer-specific values to identify |  |  |  |  |  |  |  |  |  |
| tion and hooking techniques to bypass T | IRO | ’s monitor- | the code that must be extracted. They also do not handle |  |  |  |  |  |  |  |
| ing within the ART runtime. | While we currently can- | any other form of obfuscation, which makes it difficult |  |  |  |  |  |  |  |  |
| not prevent this, due to the shared address space between | to analyze the retrieved code if it is further obfuscated in |  |  |  |  |  |  |  |  |  |
| the application and the runtime environment, future work | another way. Others, such as PackerGrind [33] and App- |  |  |  |  |  |  |  |  |  |
| may explore the separation of application and runtime | Spear [16] have a more general design but their monitor- |  |  |  |  |  |  |  |  |  |
| memory, which would also prevent tampering of runtime | ing for bytecode modification is limited to instrumenta- |  |  |  |  |  |  |  |  |  |
| state and disable runtime-based obfuscation. | tion of specific methods they expect obfuscation code to |  |  |  |  |  |  |  |  |  |
| Since T | IRO | relies on dynamic analysis to report de- | use. While these unpackers identify certain cases of DEX |  |  |  |  |  |  |  |
| obfuscated values, full deobfuscation of an application | bytecode modification, they do not handle other forms |  |  |  |  |  |  |  |  |  |
| would require executing all of its obfuscation code. | of state modification in the code execution process nor |  |  |  |  |  |  |  |  |  |
| Since T | IRO | was implemented on top of IntelliDroid [31], | do they address the wider issue of runtime-based obfus- |  |  |  |  |  |  |  |
| we rely on it to execute targeted obfuscation locations. | cation. DroidUnpack [9] uses full system emulation to |  |  |  |  |  |  |  |  |  |
| However, because its analysis is limited to Java, while | dynamically extract packed code. | While DroidUnpack |  |  |  |  |  |  |  |  |
| it can target native method invocations, it cannot extract | can extract dynamically loaded code and decrypted DEX |  |  |  |  |  |  |  |  |  |
| execution paths within native code. | Since native code | files, they do not discuss or indicate if they can han- |  |  |  |  |  |  |  |  |
| is used extensively by obfuscators, we may miss certain | dle runtime-based obfuscation the way T | IRO | can. | De- |  |  |  |  |  |  |
| paths. In addition, IntelliDroid may not be able to extract | Guard [4] takes a different approach and uses a statisti- |  |  |  |  |  |  |  |  |  |
| all targeted paths and constraints due to static impreci- | cal model to reverse the name obfuscation performed by |  |  |  |  |  |  |  |  |  |
| sion and complex path constraints in the code; T | IRO | nat- | the ProGuard [15] tool included with the Android SDK. |  |  |  |  |  |  |  |
| urally inherits these limitations. T | IRO | can be combined | Since T | IRO | focuses on the actions taken by an applica- |  |  |  |  |  |
| with fuzzers if deobfuscation is required in native code or | tion, we do not deobfuscate class and method names. |  |  |  |  |  |  |  |  |  |
| in execution paths with constraints that cannot be solved. | However, combining the results of T | IRO | and DeGuard |  |  |  |  |  |  |  |

would aid in manual analysis of malware.

8 Related work T IRO is also similar to deobfuscation tools proposed

for general Java applications. TamiFlex [5] deobfuscates

| A variety of security and privacy analyzers have been de- | reflection by instrumenting the reflection classes loaded |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| veloped for Android, including static [2,12] and dynamic | by the Java runtime, but does not handle other forms |  |  |  |  |
| tools [10, 27, 28, 34]. | T | IRO | is a hybrid system similar | of obfuscation. | However, its modification of the class |
| to [22, 23, 31, 32], which use dynamic information to en- | loader in the runtime is similar to the technique used in |  |  |  |  |
| hance static analysis. Tools that perform malware classi- | T | IRO | to load instrumented application classes. Similarly, |  |  |
| fication [1, 12] are often based on application semantics | Ripple [37] also targets reflection but does so through |  |  |  |  |
| and rely on the ability to determine the actions performed | static resolution, which is less precise. | These tools do |  |  |  |
| by an application. While they are effective against unob- | not address runtime-based obfuscation. |  |  |  |  |
| fuscated applications, they cannot handle complex code | Deobfuscation and unpacking tools also exist for x86 |  |  |  |  |
| obfuscation and will likely miss malicious actions that | applications. | Renovo [17] tracks whether previously |  |  |  |
| the malware performs. While some tools have been de- | written memory regions are being executed and can |  |  |  |  |
| signed with obfuscation resilience in mind [13], they of- | handle multiple “hidden layers" of packing. | Polyun- |  |  |  |
| ten cannot handle the complex obfuscation techniques | pack [24] checks whether dynamic instruction sequences |  |  |  |  |
| USENIX Association | 27th USENIX Security Symposium | 1259 |  |  |  |

---

## Page 15

match those in its static model of the application and References

returns new unpacked instruction sequences. Ether [8]

and produce effective results that can be integrated with

existing Android security tools.

niques used on the Android platform, which we name

runtime-based obfuscation . These techniques subvert the

fuscation framework for Android applications that can

ditional techniques such as reflection or native method

strumentation and dynamic information gathering that

that T IRO is able to deobfuscate malware that have been

curity analysis will require deobfuscation of these tech-

produced by T IRO , it is possible for existing security

10 Acknowledgments

Daniel Bali, Jason Woloz, and Monirul Sharif for shar-

The research in this paper was supported by an NSERC

a Google Faculty Research Award.

[1] A RP , D., S PREITZENBARTH , M., H UBNER , M., G ASCON , H.,

P. FlowDroid: precise context, flow, field, object-sensitive and-

cution attacks. In Proceedings of the 32nd Annual Conference on

Computer Security Applications (2016), ACM, pp. 189–200.

[4] B ICHSEL , B., R AYCHEV , V., T SANKOV , P., AND V ECHEV , M.

Statistical deobfuscation of Android applications. In Proceedings

of the 2016 ACM SIGSAC Conference on Computer and Commu-

[5] B ODDEN , E., S EWE , A., S INSCHEK , J., O UESLATI , H., AND

ence of reflection and custom class loaders. In Proceedings of the

33rd International Conference on Software Engineering (2011),

ACM, pp. 241–250.

(IMPS) (2016), 24–32.

Accessed: April 2017.

malware analysis via hardware virtualization extensions. In Pro-

ceedings of the 15th ACM conference on Computer and commu-

[9] D UAN , Y., Z HANG , M., B HASKAR , A. V., Y IN , H., P AN , X.,

Distributed System Security (NDSS) (2018).

M C D ANIEL , P., AND S HETH , A. N. TaintDroid: an information-

flow tracking system for realtime privacy monitoring on smart-

6.

[11] F ELT , A. P., C HIN , E., H ANNA , S., S ONG , D., AND W AG -

NER , D. Android permissions demystified. In Proceedings of the

18th ACM Conference on Computer and Communications Secu-

rity (2011), ACM, pp. 627–638.

K HALIGH , A., AND M ALEK , S. Obfuscation-resilient, efficient,

and accurate detection and family identification of Android mal-

sity, Tech. Rep (2015).

smali , 2017.

| presents a transparent malware analysis tool that handles | R | IECK | , K., | AND | S | IEMENS | , C. DREBIN: Effective and explain- |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| emulator-resistant techniques used by packers to pre- | able detection of Android malware in your pocket. In | Proceed- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| vent reverse engineering. Omniunpack [20] uses an in- | ings of the Annual Symposium on Network and Distributed Sys- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| memory malware detector to determine if malicious code | tem Security (NDSS) | (2014). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| is being unpacked and retrieves this code from memory. | [2] | A | RZT | , S., R | ASTHOFER | , S., F | RITZ | , C., B | ODDEN | , E., B | ARTEL | , |  |  |  |  |  |
| These techniques are more general than those used in | A., K | LEIN | , J., L | E | T | RAON | , Y., O | CTEAU | , D., | AND | M | C | D | ANIEL | , |  |  |
| T | IRO | but would require special support to handle the An- | aware taint analysis for Android apps. In | Proceedings of the 35th |  |  |  |  |  |  |  |  |  |  |  |  |  |
| droid runtime and its code loading processes. By focus- | ACM SIGPLAN Conference on Programming Language Design |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ing on obfuscation for the Android runtime via language- | and Implementation | (2014), p. 29. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| based and runtime-based deobfuscation, we account for | [3] | B | ANESCU | , S., C | OLLBERG | , C., G | ANESH | , V., N | EWSHAM | , Z., |  |  |  |  |  |  |  |
| the environment in which Android applications are run | AND | P | RETSCHNER | , A. Code obfuscation against symbolic exe- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | Conclusion | nications Security | (2016), ACM, pp. 343–355. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| In this paper, we identify a family of obfuscation tech- | M | EZINI | , M. Taming reflection: Aiding static analysis in the pres- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| integrity of the Android runtime to manipulate the code | [6] | C | OSTAMAGNA | , V., | AND | Z | HENG | , C. | ARTDroid: | A virtual- |  |  |  |  |  |  |  |
| loading and execution processes and execute malicious | method hooking framework on Android ART runtime. | Proceed- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| code surreptitiously. We propose T | IRO | , a unified deob- | ings of the 2016 Innovations in Mobile Privacy and Security |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| deobfuscate runtime-based obfuscation as well as tra- | [7] | Dex2jar. | https://github.com/pxb1988/dex2jar | , | 2017. |  |  |  |  |  |  |  |  |  |  |  |  |
| invocation. | Through an iterative process of static in- | [8] | D | INABURG | , A., R | OYAL | , P., S | HARIF | , M., | AND | L | EE | , W. Ether: |  |  |  |  |
| uses | T | arget, | I | nstrument, | R | un and | O | bserve, we show | nications security | (2008), ACM, pp. 51–62. |  |  |  |  |  |  |  |
| packed using state-of-the-art Android obfuscators. | We | L | I | , T., W | ANG | , X., | AND | W | ANG | , X. Things you may not know |  |  |  |  |  |  |  |
| also show that runtime-based obfuscation is prevalent | about Android (Un)Packers: A systematic study based on whole- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| among recent Android malware and that effective se- | system emulation. | In | Proc. of the Symposium on Network and |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| niques. Using the deobfuscated application information | [10] | E | NCK | , W., G | ILBERT | , P., C | HUN | , B.-G., C | OX | , L. P., J | UNG | , J., |  |  |  |  |  |
| analysis tools to achieve more complete analysis and de- | phones. | In | Proceedings of the 2010 Symposium on Operating |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tection of Android malware. | Systems Design and Implementation (OSDI) | (Oct. 2010), pp. 1– |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| We would like to thank Mariana D’Angelo, Peter Sun, | [12] | F | RATANTONIO | , Y., B | IANCHI | , A., R | OBERTSON | , W., K | IRDA | , |  |  |  |  |  |  |  |
| Ivan Pustogarov, James Zhen Huang, Beom Heyn Kim, | E., K | RUEGEL | , C., | AND | V | IGNA | , G. TriggerScope: Towards de- |  |  |  |  |  |  |  |  |  |  |
| Wei Huang, Sukwon Oh, Diego Bravo Velasquez, Vasily | tecting logic bombs in Android applications. In | Security and Pri- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Rudchenko, Shirley Yang, and the anonymous review- | vacy (SP), 2016 IEEE Symposium on | (2016), IEEE, pp. 377–396. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ers for their suggestions and feedback. | We also thank | [13] | G | ARCIA | , | J., | H | AMMAD | , | M., | P | EDROOD | , | B., | B | AGHERI | - |
| ing their expertise in Android malware and obfuscation. | ware. | Department of Computer Science, George Mason Univer- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CGS-D scholarship, a Tier 2 Canada Research Chair, and | [14] | G | RUVER | , B. | smali. | https://github.com/JesusFreke/ |  |  |  |  |  |  |  |  |  |  |  |
| 1260 | 27th USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 16

| [15] | G | UARD | S | QURE | . Proguard. | https://www.guardsquare.com/ | [32] | X | IA | , M., G | ONG | , L., L | YU | , Y., Q | I | , Z., | AND | L | IU | , X. Effective |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| en/proguard | , 2017. | real-time Android application auditing. | In | Proceedings of the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [16] | H | U | , W., | AND | G | U | , D. AppSpear: Bytecode decrypting and dex | 2015 IEEE Symposium on Security and Privacy | (2015), SP ’15, |  |  |  |  |  |  |  |  |  |  |  |
| reassembling for packed Android malware. | In | Research in At- | IEEE Computer Society. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tacks, Intrusions, and Defenses: 18th International Symposium, | [33] | X | UE | , L., L | UO | , X., Y | U | , L., W | ANG | , S., | AND | W | U | , D. Adaptive |  |  |  |  |  |  |
| RAID 2015, Kyoto, Japan, November 2-4, 2015. Proceedings | unpacking of Android apps. | In | Software Engineering (ICSE), |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (2015), vol. 9404, Springer, p. 359. | 2017 IEEE/ACM 39th International Conference on | (2017), IEEE, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

[17] K ANG , M. G., P OOSANKAM , P., AND Y IN , H. Renovo: A

[18] Legend. https://github.com/asLody/legend , 2017.

[19] L IU , R. Yet another hook framework for art (YAHFA). https:

//github.com/rk700/YAHFA , 2017.

Computer Security Applications Conference, 2007. ACSAC 2007.

Twenty-Third Annual (2007), IEEE, pp. 431–441.

[23] R ASTHOFER , S., A RZT , S., T RILLER , S., AND P RADEL , M.

Making malory behave maliciously: Targeted fuzzing of An-

droid execution environments. In Software Engineering (ICSE),

2017 IEEE/ACM 39th International Conference on (2017), IEEE,

pp. 300–311.

L EE , W. PolyUnpack: Automating the hidden-code extraction

tions Conference, 2006. ACSAC’06. 22nd Annual (2006), IEEE,

[25] S HARIF , M. I., L ANZI , A., G IFFIN , J. T., AND L EE , W. Imped-

strazzere/android-unpacker , 2017.

level information-flow tracking system for Android runtime. In

CopperDroid: Automatic reconstruction of Android malware be-

tion framework. In Proceedings of the 1999 conference of the

Centre for Advanced Studies on Collaborative research (1999),

[30] V IRUS T OTAL . Virustotal. https://www.virustotal.com ,

2018.

[31] W ONG , M. Y., AND L IE , D. IntelliDroid: A targeted input gen-

erator for the dynamic analysis of Android malware. In Proceed-

pp. 358–369.

584.

[35] Z HANG , A. ZHookLib. https://github.com/cmzy/

ZHookLib , 2017.

[36] Z HANG , Y., L UO , X., AND Y IN , H. DexHunter: toward extract-

pp. 293–311.

[37] Z HANG , Y., T AN , T., L I , Y., AND X UE , J. Ripple: Reflec-

48.

Appendix

like other API invocations that the malware wishes to

the reflected obfuscation API.

phase executes the instrumented code and reports the

DEX files.

Iteration 2: The static analysis scope is expanded to in-

clude code from these two DEX files. This code in-

| hidden code extractor for packed executables. In | Proceedings of | [34] | Y | AN | , L.-K., | AND | Y | IN | , H. DroidScope: Seamlessly reconstruct- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the 2007 ACM workshop on Recurring malcode | (2007), ACM, | ing the os and dalvik semantic views for dynamic Android mal- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| pp. 46–53. | ware analysis. In | USENIX security symposium | (2012), pp. 569– |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [20] | M | ARTIGNONI | , L., C | HRISTODORESCU | , M., | AND | J | HA | , S. Om- | ing hidden code from packed Android applications. In | European |  |  |  |  |  |  |  |  |  |  |  |  |  |
| niunpack: | Fast, generic, and safe unpacking of malware. | In | Symposium on Research in Computer Security | (2015), Springer, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [21] | O | CTEAU | , D., J | HA | , S., | AND | M | C | D | ANIEL | , P. | Retargeting An- | tion analysis for Android apps in incomplete information envi- |  |  |  |  |  |  |  |  |  |  |  |
| droid applications to java bytecode. In | Proceedings of the ACM | ronments. | In | Proceedings of the Seventh ACM on Conference |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SIGSOFT 20th International Symposium on the Foundations of | on Data and Application Security and Privacy, CODASPY 2017, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Software Engineering | (2012), ACM, p. 6. | Scottsdale, AZ, USA, March 22-24, 2017 | (2017), pp. 281–288. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [22] | R | ASTHOFER | , S., A | RZT | , S., M | ILTENBERGER | , M., | AND | B | OD | - | [38] | Z | HAUNIAROVICH | , | Y., | A | HMAD | , | M., | G | ADYATSKAYA | , | O., |
| DEN | , E. Harvesting runtime values in Android applications that | C | RISPO | , B., | AND | M | ASSACCI | , F. | StaDynA: Addressing the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| feature anti-analysis techniques. | In | Proceedings of the Annual | problem of dynamic code updates in the security analysis of An- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Symposium on Network and Distributed System Security (NDSS) | droid applications. In | Proceedings of the 5th ACM Conference on |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (2016). | Data and Application Security and Privacy | (2015), ACM, pp. 37– |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [24] | R | OYAL | , P., H | ALPIN | , M., D | AGON | , D., E | DMONDS | , R., | AND | A | Iterative deobfuscation in T | IRO |  |  |  |  |  |  |  |  |  |  |  |
| of unpack-executing malware. | In | Computer Security Applica- | Most obfuscators and packers use more than one of the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| pp. 289–300. | obfuscation techniques we have described. For instance, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ing malware analysis using conditional code obfuscation. In | Pro- | hide, dynamic loading invocations may be hidden behind |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ceedings of the Annual Symposium on Network and Distributed | reflection. Deobfuscation in these cases requires multi- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| System Security (NDSS) | (2008). | ple iterations to resolve the reflection target and, if the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [26] | S | TRAZZERE | , T. | android-unpacker. | https://github.com/ | target is used for another form of obfuscation, to resolve |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [27] | S | UN | , M., W | EI | , T., | AND | L | UI | , J. | TaintART: A practical multi- | As an example, Figure 2 shows how T | IRO | iteratively |  |  |  |  |  |  |  |  |  |  |  |
| Proceedings of the 2016 ACM SIGSAC Conference on Computer | applies the T- | I | - | R | - | O | loop to deobfuscate the combination |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and Communications Security | (2016), ACM, pp. 331–342. | of techniques used by the | dexprotector | packer and to ex- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [28] | T | AM | , K., K | HAN | , S. J., F | ATTORI | , A., | AND | C | AVALLARO | , L. | tract a complete application call graph. |  |  |  |  |  |  |  |  |  |  |  |  |
| haviors. In | Proc. of the Symposium on Network and Distributed | Iteration 1: | The scope of the static analysis is limited |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| System Security (NDSS) | (2015). | to code in the application’s APK file. T | IRO | finds loca- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [29] | V | ALLÉE | -R | AI | , R., C | O | , P., G | AGNON | , E., H | ENDREN | , L., L | AM | , | tions of reflected method invocations and instruments |  |  |  |  |  |  |  |  |  |  |
| P., | AND | S | UNDARESAN | , V. | Soot - a Java bytecode optimiza- | them to determine the reflection targets. The dynamic |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CASCON ’99, IBM Press, p. 13. | reflection targets. It also finds two dynamically loaded |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ings of the Annual Symposium on Network and Distributed Sys- | cludes entry-points into the application that were pre- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tem Security (NDSS) | (2016). | viously unknown. | However, the use of reflection in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| USENIX Association | 27th USENIX Security Symposium | 1261 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 17

| Iteration 1 | Iteration 2 | Iteration 3 | Iteration 4 |
| --- | --- | --- | --- |
| Dex 1 | Dex 1 | Dex 1 |  |
| Dex 2 | Dex 2 | Dex 2 |  |
| entry-point | method | dynamically loaded method |  |
| normal invocation | reflected invocation |  |  |

Figure 2: Deobfuscated call graphs produced for an ap-

plication packed with dexprotector

the dynamically loaded code means that the call graph

may miss certain invocation edges. T IRO ’s static anal-

ysis adds new instrumentation for any obfuscation

(namely, reflection) found in the APK code or dynam-

ically loaded code. The dynamic phase will again ex-

ecute the instrumented code to find the reflection tar-

gets.

Iteration 3: Some reflective call edges are resolved

in the static call graph; however, T IRO still sees

seemingly-dead code from the second dynamically

loaded DEX file. The process is repeated until T IRO

encounters no new unresolved obfuscation/reflection.

Iteration 4: The final result is a static call graph that

represents all of the code executed by an applica-

tion and the method invocation relationships. If used

alongside a security analysis tool, malicious actions

performed by the application can then be discovered

by searching the deobfuscated call graph.

1262 27th USENIX Security Symposium USENIX Association
