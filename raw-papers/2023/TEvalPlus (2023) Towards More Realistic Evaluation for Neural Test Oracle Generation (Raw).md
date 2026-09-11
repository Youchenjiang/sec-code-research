# Towards More Realistic Evaluation for Neural Test Oracle Generation

- **Venue**: ISSTA 2023 (ACM SIGSOFT International Symposium on Software Testing and Analysis)
- **Authors**: Songqiang Chen, Shing-Chi Cheung (HKUST)
- **Pages**: 12

---

## Page 1

Towards More Realistic Evaluation for Neural Test Oracle
Generation

Zhongxin Liu
Zhejiang University
China
liu_zx@zju.edu.cn

Xin Xia
Huawei
China
xin.xia@acm.org

arXiv:2305.17047v1  [cs.SE]  26 May 2023

ABSTRACT

Unit testing has become an essential practice during software de-
velopment and maintenance. Effective unit tests can help guard and
improve software quality but require a substantial amount of time
and effort to write and maintain. A unit test consists of a test prefix
and a test oracle. Synthesizing test oracles, especially functional
oracles, is a well-known challenging problem. Recent studies pro-
posed to leverage neural models to generate test oracles, i.e., neural
test oracle generation (NTOG), and obtained promising results.
However, after a systematic inspection, we find there are some
inappropriate settings in existing evaluation methods for NTOG.
These settings could mislead the understanding of existing NTOG
approaches’ performance. We summarize them as ①generating
test prefixes from bug-fixed program versions, ②evaluating with
an unrealistic metric, and ③lacking a straightforward baseline.
In this paper, we first investigate the impacts of these settings
on evaluating and understanding the performance of NTOG ap-
proaches. We find that ❶unrealistically generating test prefixes
from bug-fixed program versions inflates the number of bugs found
by the state-of-the-art NTOG approach TOGA by 61.8%, ❷FPR
(False Positive Rate) is not a realistic evaluation metric and the
Precision of TOGA is only 0.38%, and ❸a straightforward base-
line NoException, which simply expects no exception should be
raised, can find 61% of the bugs found by TOGA with twice the
Precision. Furthermore, we introduce an additional ranking step
to existing evaluation methods and propose an evaluation metric
named Found@K to better measure the cost-effectiveness of NTOG
approaches in terms of bug-finding. We propose a novel unsuper-
vised ranking method to instantiate this ranking step, significantly
improving the cost-effectiveness of TOGA. Eventually, based on our
experimental results and observations, we propose a more realistic

∗Corresponding author.

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
ISSTA ’23, July 17–21, 2023, Seattle, WA, United States
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0221-1/23/07...$15.00
https://doi.org/10.1145/3597926.3598080

Kui Liu∗

Huawei
China
brucekuiliu@gmail.com

Xiaohu Yang
Zhejiang University
China
yangxh@zju.edu.cn

evaluation method TEval+ for NTOG and summarize seven rules
of thumb to boost NTOG approaches into their practical usages.

CCS CONCEPTS

• Software and its engineering →Software testing and debug-
ging.

KEYWORDS

Test Oracle Generation, Neural Network, Realistic Evaluation.

ACM Reference Format:
Zhongxin Liu, Kui Liu, Xin Xia, and Xiaohu Yang. 2023. Towards More
Realistic Evaluation for Neural Test Oracle Generation. In Proceedings of
the 32nd ACM SIGSOFT International Symposium on Software Testing and
Analysis (ISSTA ’23), July 17–21, 2023, Seattle, WA, United States. ACM, New
York, NY, USA, 12 pages. https://doi.org/10.1145/3597926.3598080

1
INTRODUCTION

Unit testing has become an accepted and even mandatory prac-
tice during software development. For a component (a method,
class, or module), its unit tests check whether its implemented func-
tionality can match its intended functionality and document its
intended usage. Developers leverage unit tests to find bugs, identify
regressions, and facilitate the understanding and usage of the corre-
sponding components. Therefore, effective unit tests can guard and
improve software quality as well as reduce the costs of software
failures [17, 36].
However, writing high-quality unit tests is non-trivial and time-
consuming. Prior work has shown that developers spend more than
15% of their time in writing tests [11]. To address this challenge,
some tools are proposed to automate unit test generation [14, 27, 33].
A unit test consists of a test prefix, which is a sequence of statements
driving the unit under test into a specific state [12], and a test
oracle, which specifies the condition that should be satisfied in
such state [12]. For example, in the unit test presented in Figure 1,
lines 3-6 are the test prefix, which creates a KeyedValues object,
inserts an item into the object, and then removes the item. Line
7 specifies the oracle, i.e., the object should contain no item after
executing the test prefix. Automated unit test generation tools aim
at generating both test prefixes and oracles [14, 33]. However, since
these tools are unknown of the intended behavior of a generated test
prefix, they either generate regression oracles [46], i.e., regarding
the observed behavior as the oracle, or use implicit oracles [4], such


---

## Page 2

ISSTA ’23, July 17–21, 2023, Seattle, WA, United States
Zhongxin Liu, Kui Liu, Xin Xia, and Xiaohu Yang

1 @Test
2 public void test14()
throws Throwable
{
3
KeyedValues KeyedValues0 = new KeyedValues();
4
Integer integer0 = new Integer(233);
5
KeyedValues0.setValue((Comparable) integer0, 0.0);
6
KeyedValues0.removeValue((Comparable) integer0);
7
assertEquals(0, KeyedValues0.getItemCount());
8 }

Figure 1: Example of a unit test case.

as “program crashes are usually undesirable”. Regression oracles
cannot reveal functional bugs in the project versions where they
are generated. Implicit oracles are not always correct and hence
are neither sufficient nor accurate to find the violations of intended
functionality. To sum up, these automated unit test generation tools
still can not replace manual test writing.
To tackle the oracle problem [4] and complement unit test gen-
eration tools, researchers proposed several approaches to automat-
ically generate test oracles and achieved promising results [6, 12,
16, 34, 39, 42, 44, 48]. Recently, a popular and effective category
of approaches trains neural networks on developer-written unit
tests to learn to generate test oracles [12, 42, 44], namely neural
test oracle generation (NTOG) approaches. Given a focal unit and
a test prefix, NTOG approaches leverage the trained neural net-
works to either generate an oracle from scratch or select an oracle
from several candidates that are pre-generated based on templates.
NTOG approaches are flexible since they do not rely on natural
language patterns and manual-crafted rules. The state-of-the-art
NTOG approach is TOGA proposed by Dinella et al. [12], which is
shown to outperform existing test oracle generation tools in terms
of bug-finding. Given a test prefix and its focal context (including
the focal method and the focal docstring), TOGA first generates a
set of possible oracles based on several empirically summarized tem-
plates and the type-based constraints inferred from the test prefix,
and then fine-tunes two CodeBERT models to rank the generated
candidates and outputs the oracle ranking first.
A fundamental goal of test oracle generation is to uncover bugs.
To evaluate the bug-finding performance of NTOG approaches, two
evaluation methods are widely adopted by prior work. The first one
is to evaluate the target approach in a held-out set of developer-
written unit tests collected from real-world projects [12, 30, 44].
This is a common evaluation method for neural methods and is
also used in other code-related tasks, such as code comment gen-
eration [18, 19] and neural patch generation [9, 43]. This method
can reflect whether one NTOG approach is better than other ones
in terms of learning ability. However, it assumes the existence of
developer-written test prefixes, which is usually not the case in
practice, and thus cannot explicitly demonstrate the effectiveness
of NTOG approaches in uncovering real-world bugs. Another eval-
uation method is proposed in the TOGA paper [12] and we refer
to it as TEval for convenience. TEval first leverages a unit test
generation tool, such as EvoSuite [14], to generate test prefixes for
NTOG approaches, then combines the oracles generated by NTOG
approaches with the corresponding test prefixes to construct com-
plete test cases, and finally checks whether the generated oracles
can find bugs by compiling and executing such test cases. Because

TEval does not require developer-written test prefixes, it is more
realistic than the first evaluation method and can measure the per-
formance of NTOG approaches in uncovering real-world bugs.
Using TEval, Dinella et al. [12] presented that TOGA can find 57
out of 835 bugs in the Defects4J benchmark [22] with a False Positive
Rate (FPR) of 25%. After a systematic inspection, we find that even
TEval is not realistic enough and could not accurately assess the
real-world performance of NTOG approaches. Because some of its
settings are inappropriate and could mislead the understanding of
existing NTOG approaches’ performance. We summarize them into
three aspects below:
❶Generating test prefixes from bug-fixed program ver-
sions. Existing NTOG approaches take as input test prefixes and
focal context (e.g., focal methods and their docstrings). To generate
test prefixes for a bug, TEval runs EvoSuite on the corresponding
bug-fixed program version. However, when applying NTOG tools
in practice, we expect them to find bugs in the current buggy pro-
gram version, and the bug-fixed program version is not available
at that time. Therefore, to be consistent with the real-world usage
scenario, test prefixes should be generated on the buggy program
version instead of the bug-fixed program version. Also, considering
that EvoSuite is guided by branch coverage, the test prefixes gener-
ated by EvoSuite on the bug-fixed program version may implicitly
contain some information related to the patch of the bug, which
should be unknown during bug finding. Therefore, using such test
prefixes as input may result in information leakage and inflate the
performance metrics.
❷Evaluating with an unrealistic metric. TEval uses FPR
(False Positive Rate) to assess and compare against different NTOG
approaches. FPR is calculated by #𝐹𝑃/(#𝐹𝑃+#𝑇𝑁), where FP (False
Positive) refers to the generated oracle that fails on both the buggy
and the bug-fixed program versions, TN (True Negative) refers to
the generated oracle that passes on both versions, and #FP and #TN
denote the number of FPs and TNs, respectively. However, when
using bug-finding tools, developers care more about the Precision,
i.e., how many FPs they need to inspect to find a bug, and usually
have few interests in using a tool with a low Precision [5, 21].
Therefore, we argue that the FPR metric is not consistent with
developers’ concerns and may not accurately reflect the real-world
performance of NTOG approaches.
❸Lacking a straightforward baseline. According to TOGA’s
evaluation results [12], the observed behaviors of 39 out of the 57
bugs (68.4%) found by TOGA are “Exception Raised”. The oracles of
these bugs, i.e., no exception raised, are straightforward and do not
need to be explicitly specified by generating an assert statement.
Considering this, we construct a straightforward oracle generation
approach named NoException, which expects that every test prefix
does not raise exceptions and does not explicitly generate assert
statements. Comparing NTOG approaches with NoException on
bug benchmarks can help practitioners understand how much they
can gain from neural models compared to implicit oracles. However,
prior work has not explored this straightforward baseline yet.
To boost neural test oracle generation (NTOG) towards more
realistic evaluation, in this paper, we first investigate the effects of
the inappropriate settings in TEval on evaluating and understanding
the performance of NTOG approaches. Specifically, we conduct a
case study using TOGA [12], the latest and state-of-the-art NTOG


---

## Page 3

Towards More Realistic Evaluation for Neural Test Oracle Generation
ISSTA ’23, July 17–21, 2023, Seattle, WA, United States

approach. We address the three inappropriate settings in TEval
one by one and re-evaluate TOGA on the Defects4j benchmark
using the improved TEval. We observe that: ①Generating test
prefixes from the bug-fixed program versions significantly inflates
the performance metrics. On average, it improves the number of
bugs found by TOGA from 64.4 to 104.2 and enhances FPR from
22.1% to 19.7% (the lower, the better). ②The Precision of TOGA is
only 0.38%, which means developers need to check over 260 test
cases that fail on the buggy program version to find a bug-revealing
one. ③On average, 61% of the bugs found by TOGA can be found by
the straightforward baseline NoException with twice the Precision,
and on average 4.7 bugs found by NoException cannot be found by
TOGA.
Considering the limited development resources, we argue that
when applying an NTOG approach, it is impractical to ask devel-
opers to check all the generated test cases that fail if most of them
cannot reveal bugs. The bug-finding performance of NTOG ap-
proaches should be measured in a cost-effective way. Therefore, we
further enhance TEval by introducing an additional ranking step
and evaluating NTOG approaches’ performance by counting the
number of bugs that can be found if developers only check the top-k
ranked test cases for each bug, i.e., Found@K. In addition, we pro-
pose a novel unsupervised ranking method, which leverages a set
of features designed for this task and an outlier detection algorithm,
to instantiate this ranking step. Experimental results show that ①
our ranking method can significantly improve random ranking in
terms of Found@K, and ②TOGA can be more cost-effective than
NoException with proper ranking.
Finally, we propose a more realistic evaluation method named
TEval+ for NTOG by incorporating all our improvements with
TEval, and further summarize seven rules of thumb to boost NTOG
approaches towards their practical usage.
Our main contributions are summarized as follows:

• We point out several inappropriate settings in existing eval-
uation methods for NTOG and investigate their effects on
measuring and understanding the bug-finding performance
of the state-of-the-art NTOG approach TOGA.
• We propose an evaluation method named TEval+ for NTOG,
which enhances TOGA’s evaluation method by addressing its
inappropriate settings, reducing duplicates and noise during
evaluation, and introducing an additional ranking step to
rank failed test cases. We believe TEval+ is more realistic
than existing evaluation methods and can better reflect the
bug-finding performance of NTOG approaches.
• We proposed a novel unsupervised method to instantiate the
ranking step of TEval+. Experimental results show that it
can significantly improve the cost-effectiveness of NTOG
approaches.
• We summarize seven rules of thumb to help practitioners
conduct more realistic evaluations for NTOG approaches.
• Our replication package can be found at [2].

The remainder of this paper is organized as follows: Section 2 in-
troduces the Defects4J benchmark and existing evaluation methods
for NTOG. Section 3 investigates the effects of inappropriate evalu-
ation settings on evaluating and understanding the performance
of NTOG approaches. We elaborate on our unsupervised ranking

algorithm and its evaluation results in Section 4. Section 5 describes
our enhanced evaluation method TEval+ and our summarized rules
of thumb for NTOG. In Section 6, we present TOGA’s performance
on different types of oracles and discuss the threats to validity. After
reviewing the related work in Section 7, we conclude and point out
future work in Section 8.

2
BACKGROUND

This section briefly introduces the Defects4J benchmark [22] and
existing evaluation methods for NTOG.

2.1
The Defects4J Benchmark

Defects4J [22] is a widely-used bug benchmark containing 835 bugs
from 17 real-world Java projects. TEval uses Defects4J to evaluate
the bug-finding performance of NTOG approaches. Each bug col-
lected by Defects4J is recorded in the corresponding issue tracker, is
fixed in a single commit by modifying the source code, and includes
a buggy and a bug-fixed program versions. Each bug-fixed pro-
gram version is based on a manually minimized patch and passes
all test cases, while each buggy program version fails at least one
test case and such test cases are deterministic. Defects4J also pro-
vides a supporting framework to evaluate a test suite on a specific
buggy/bug-fixed program version. Because the only difference be-
tween a buggy program version and its corresponding bug-fixed
program version is a minimal patch fixing the bug, a test case that
fails on the buggy version and passes on the bug-fixed version
must trigger the specific bug. This property can be used to deter-
mine whether a generated test case is a bug-finding one. Following
Dinella et al. [12], we also use Defects4J 2.0.0 in this work.

2.2
Evaluation Methods for Neural Test Oracle
Generation

Existing NTOG approaches take as input a test prefix and the corre-
sponding focal context (e.g., the focal method and/or its docstring
comment) and output an assert statement, i.e., an oracle. A common
way to evaluate NTOG approaches is to execute them on a held-out
test set collected from developer-written unit tests. In detail, for
each test sample, such evaluation method extracts its test prefix and
focal context as input, uses the target NTOG approach to generate
an oracle, and regards the corresponding developer-written ora-
cle as ground truth to measure the generation accuracy. However,
when applying NTOG approaches in practice, developer-written
test prefixes are usually not available, and writing high-quality or
bug-reaching test prefixes is usually not easier or even more diffi-
cult and time-consuming than writing test oracles for developers.
Therefore, it is impractical and somehow unrealistic to assume the
existence of developer-written test prefixes when evaluating NTOG
approaches. Thus, such evaluation method can hardly reflect the
real-world bug-finding performance of NTOG approaches.
Tufano et al. [42] proposed to evaluate NTOG approaches by
generating additional assert statements for the test cases generated
by EvoSuite, inserting such asserts as the last statements of the test
cases, and calculating the differences in code coverage before and
after the insertion. However, their evaluation only chose one bug
from Defects4J, required to manually select the focal methods, the


---

## Page 4

ISSTA ’23, July 17–21, 2023, Seattle, WA, United States
Zhongxin Liu, Kui Liu, Xin Xia, and Xiaohu Yang

generated test cases and the generated asserts, and did not measure
the bug-finding performance of NTOG approaches.
Recently, an evaluation method is proposed by Dinella et al. [12]
to assess the real-world bug-finding performance of NTOG ap-
proaches. We refer to it as TEval (TOGA’s Evaluation method).
TEval does not assume the existence of developer-written test pre-
fixes. Instead, it generates test prefixes using an automated unit
test generation tool named EvoSuite [14]. Therefore, it is more real-
istic than the first evaluation method. Specifically, TEval first uses
EvoSuite with branch coverage as the criterion on the bug-fixed
program versions to generate regression tests. Then, it extracts the
test prefix and the corresponding focal context of each generated
test case and feeds them into an NTOG approach for oracle gen-
eration. Each generated oracle is appended to its corresponding
test prefix to construct a complete test case. Finally, it executes
each generated test case on the corresponding buggy and bug-fixed
program versions. If a test case fails on the buggy version but passes
on the bug-fixed one, it is regarded as a bug-finding test.
Following the definitions in the TOGA paper [12] and based on
the execution results of the generated tests, the generated tests can
be divided into four groups: True Positive (TP), True Negative (TN),
False Positive (FP) and False Negative (FN). Positive and Negative
mean that the generated test case fails and passes on the corre-
sponding buggy program version, respectively. True/False denotes
that the generated test passes/fails on the corresponding bug-fixed
program version. Based on these definitions, a bug-finding test is a
TP sample. To measure the bug-finding performance, TEval uses
two metrics, i.e., BugFound and FPR (False Positive Rate). BugFound
refers to the number of bugs that can be uncovered by TP samples.
FPR is calculated by #𝐹𝑃/(#𝐹𝑃+ #𝑇𝑁). The experimental results of
using TEval on TOGA show that TOGA, the state-of-the-art NTOG
approach, can find 57 bugs on Defects4J with an FPR of 25%, which
is impressive and outperforms all baseline approaches, including
seq2seq [42] and JDoctor [6], by substantial margins.

3
THE IMPACT OF INAPPROPRIATE
SETTINGS IN TEVAL

TEval is currently the state-of-the-art method for evaluating the
bug-finding performance of NTOG approaches. However, after a
systematic inspection, we find that TEval also has several inappro-
priate settings, which may introduce significant gaps between the
reported evaluation results and the real-world bug-finding perfor-
mance of NTOG approaches. As described in Section 1, we summa-
rize these inappropriate settings as: ❶generating test prefixes
from bug-fixed program versions, ❷evaluating with an un-
realistic metric, and ❸lacking a straightforward baseline. In
this section, we briefly review each inappropriate setting and inves-
tigate its impact on evaluating and understanding the bug-finding
performance of an NTOG approach. We use the state-of-the-art
NTOG approach TOGA as the evaluation subject, and aim to answer
the following research questions (RQs):

• RQ1: What is the impact of generating test prefixes from
bug-fixed program version on TOGA’s performance?
• RQ2: How effective is TOGA when we use more realistic
evaluation metrics?

• RQ3: How effective is TOGA when compared with a straight-
forward baseline?

3.1
Experimental Setup

Following TEval [12], we use EvoSuite with branch coverage as
the criterion to generate test prefixes for TOGA. Specifically, we
leverage the gen_tests.pl script provided by Defects4J to auto-
mate such generation. We run EvoSuite for 3 minutes per tested
program.
In our experiments, we do not need or construct explicit ground
truth. Because TP, FP, TN and FN are not identified by comparing
the generated test oracles with explicit ground truth. Instead, for
each generated test oracle, we combine it with its test prefix to
construct a complete test case and execute this test case on both
the buggy and the bug-fixed program versions. TP, FP, TN and FN
are then identified strictly based on their definitions (described in
Section 2.2) and the execution results. For example, if a test case
fails on the buggy program version and passes on the bug-fixed
program version, its oracle will be regarded as TP.
In addition, the original TEval used in the TOGA paper [12] only
runs EvoSuite once for each bug, which may introduce bias since
EvoSuite is based on randomized algorithms [14]. To reduce the
potential bias, in this work, we run EvoSuite for each bug 10 times
with different random seeds and report the mean value of each
evaluation metric as the result.

3.2
RQ1: Generating Test Prefixes from Buggy
Versions

According to the TOGA paper, TEval generates test prefixes “by
running EvoSuite with default settings (i.e., coverage-guided) on
the fixed program versions” [12]. As discussed in Section 1, this is
unrealistic and may result in information leakage and inflate the
performance metrics. In this RQ, we aim to investigate the impact
of this unrealistic setting on evaluating TOGA’s bug-finding per-
formance and figure out whether it is necessary to fix this setting.
In addition, we find two implementation problems in the official
implementation of TEval [1]. The first problem is called the over-
filtering problem by us. Specifically, to speed up the execution of
test cases, the official implementation aggregates all the test cases
generated for a focal class into one test class. When a test case
generated from a buggy/bug-fixed program version is executed
on the corresponding bug-fixed/buggy version, it may encounter
compilation errors, e.g., using undeclared methods. If one test case
has compilation errors, TEval’s official implementation will filter
out the whole test class, which could reduce the number of bugs that
can be found by an oracle generation approach and underestimate
its bug-finding performance.
The other problem is referred to as the duplication problem by
us. In detail, if a test case generated by EvoSuite contains multiple
assertions at its end, TEval’s official implementation will extract
the same test prefix multiple times. Consequently, the target oracle
generation approach will generate duplicate oracles and TEval will
construct duplicate test cases. However, TEval’s official implemen-
tation does not deduplicate the constructed test cases, which could
increase the numbers of TP, FP, TN and FN to varying degrees and
therefore bias the evaluation results.


---

## Page 5

Towards More Realistic Evaluation for Neural Test Oracle Generation
ISSTA ’23, July 17–21, 2023, Seattle, WA, United States

Table 1: The performance of TOGA with different evaluation
methods.

Evaluation Method
BugFound
FPR

TEval*
57
25%

TEval
96.4
17.0%
TEval@fixed
104.2
19.7%
TEval@buggy
64.4
22.1%

The row of TEval* presents the evaluation results re-
ported in the TOGA paper [12].

Approach: We address the over-filtering problem by identify-
ing and collecting all test cases with compilation errors, removing
them from their test classes, and re-executing these test classes to
collect execution results. To solve the duplication problem, for each
bug, we deduplicate the constructed test cases before calculating
evaluation metrics. Hereon, we use TEval to refer to our replica-
tion of TEval that addresses the duplication problem and keeps
other settings the same as the official implementation of TEval. We
refer to the variant of TEval that addresses the two implementa-
tion problems and generates test prefixes from bug-fixed program
versions as TEval@fixed, and the variant which addresses the
two problems but generates test prefixes from buggy program ver-
sions as TEval@buggy. All three methods remove duplicate test
cases since we regard deduplication as a must-do. Please note that
TEval@fixed and TEval@buggy all run EvoSuite 10 times for each
bug to generate test prefixes and TEval uses the same test prefixes
as TEval@fixed.
To answer this research question, we evaluate TOGA with TEval,
TEval@fixed and TEval@buggy. We illustrate the impact of gener-
ating test prefixes from bug-fixed program versions by comparing
TEval@fixed with TEval@buggy, and highlight the impact of the
over-filtering problem by comparing TEval and TEval@fixed. In
addition, Wilcoxon signed-rank test [45] at the confidence level of
95% is used to show whether the more realistic setting significantly
affects the evaluation results. Cliff’s delta [10] is used to measure
the effect sizes of the performance differences.
Results: Table 1 presents our experimental results. The row
of TEval* refers to the evaluation results reported by the TOGA
paper [12]. We can see that our replication of TEval finds 96.4 bugs
and achieves an FPR of 17.0% on average. Such results are much
better than those of TEval*. Even the experiment with the worst
performance can find 86 bugs. Considering that duplicate test cases
cannot help find more bugs, we infer the reason behind the perfor-
mance gap between TEval and TEval* could be that our hardware
environment is quite different from that of TEval* and we generate
test prefixes of higher quality. Comparing TEval with TEval@fixed,
we can see that on average TEval@fixed finds more bugs than
TEval, which means TEval mistakenly deletes some bug-finding
test cases due to the over-filtering problem. Our statistical analysis
shows that the performance differences in terms of BugFound and
FPR between TEval and TEval@fixed are significant. These results
indicate that it is necessary to fix the over-filtering problem.
According to Table 1, the evaluation results using TEval@fixed
are much better than those using TEval@buggy. TEval@fixed can
find about 61.8% (39.8) more bugs and reduce the FPR by 2.4%,

although the underlying NTOG approach is the same one. In ad-
dition, our statistical analysis shows that the p-value in terms of
BugFound is less than 0.005 and the corresponding effect size is
large (i.e., >0.474). As for FPR, the p-value is less than 0.05 and the
effect size is also large. These results indicate that the differences be-
tween the evaluation results using TEval@buggy and TEval@fixed
are significant. Based on such significant differences and consider-
ing that only buggy program versions are available in practice, we
suggest practitioners use TEval@buggy instead of TEval@fixed for
evaluating NTOG approaches.

In summary, we find that ①fixing the over-filtering prob-
lem can help obtain more accurate evaluation results, and ②
generating test prefixes from bug-fixed program versions can
significantly inflate the performance metrics. Considering the
practical scenarios of NTOG tools, we believe TEval@buggy
can better reflect the real-world performance of NTOG ap-
proaches than Teval@fixed.

3.3
RQ2: Evaluating with More Realistic Metrics

TEval uses two metrics, i.e., BugFound and FPR, to measure the ef-
fectiveness of NTOG approaches in terms of bug finding. BugFound
refers to the total number of bugs that can be revealed by the gen-
erated test oracles, which is good for measuring the upper bound
(or recall) of an oracle generation approach in terms of bug finding.
FPR is calculated by #𝐹𝑃/(#𝐹𝑃+ #𝑇𝑁), as described in Section 2.2.
Dinella et al. claimed that a high FPR rate implies a developer needs
to validate many tests of no use and FPR is a good metric for a
bug-finding tool [12]. However, when using oracle generation tools
in practice, developers only manually check the generated test cases
failing on the program, i.e., the positive sample. TN samples are
usually ignored because they pass on the buggy program version
and cannot help uncover the hidden bugs. According to this and
the definition of FPR, we argue that FPR cannot reflect the rate of
useless test cases that developers need to manually validate, and is not
a realistic metric for measuring the bug-finding effectiveness of oracle
generation tools. In this RQ, we aim to better understand TOGA’s
bug-finding performance with a more realistic evaluation metric.
Approach: Intuitively, when using oracle generation tools or
other bug-finding tools in practice, developers really care about how
many FP samples they need to check before finding a TP sample. In
other words, developers value Precision more [5, 21]. Therefore, we
propose to measure the effectiveness and practicability of an NTOG
approach by calculating its Precision instead of FPR. Precision is
denoted as #𝑇𝑃/(#𝐹𝑃+ #𝑇𝑃), i.e., the ratio of the generated test
cases that can indeed find bugs to all the generated test cases failing
on the program. The higher a tool’s precision is, the less effort it
takes for a developer to validate the generated test cases that is
useless. Like RQ1, we also conduct Wilcoxon signed-rank test [45]
and use Cliff’s delta [10] to show whether TEval@fixed significantly
outperforms TEval@buggy in terms of Precision.
Result: Table 2 presents the experimental results. It is worth
mentioning for each evaluation method, the BugFound is smaller
than the #TP, which is expected. Because for each bug, EvoSuite
generates many different test prefixes. Different test cases can be
generated based on such test prefixes, and there can be more than


---

## Page 6

ISSTA ’23, July 17–21, 2023, Seattle, WA, United States
Zhongxin Liu, Kui Liu, Xin Xia, and Xiaohu Yang

Table 2: The Performance of TOGA in terms of Precision.

Evaluation Method
BugFound
Precision
#TP
#FP

TEval@fixed
104.2
1.13%
288.0
25237.6
TEval@buggy
64.4
0.38%
110.7
29099.4

@Test
public void test1() throws Throwable {
Fraction fraction0 = new Fraction((double) 105, 105);
}

@Test
public void test2() throws Throwable {
Fraction fraction0 = new Fraction((double) (-290), 542)
;
}

Figure 2: Two test cases that can both trigger the bug Math1.

one test case triggering this bug. For example, the bug Math1 in
Defects4J can be triggered by the two different test cases shown
in Figure 2. If an approach generates the two test cases for Math1,
its #TP and BugFound will be increased by 2 and 1, respectively.
Therefore, #TP can be larger than BugFound.
Surprisingly, the Precision of TOGA using TEval@buggy is only
0.38% on average, which means that to find a bug-finding test case,
developers need to manually check over 260 failed test cases gener-
ated by EvoSuite and TOGA. Even if we unrealistically generate test
prefixes from bug-fixed program versions, i.e., using TEval@fixed,
TOGA’s Precision is still quite low (1.13%). Considering the im-
portance of high precision for bug-finding tools, we think there
is still a long way to go before directly applying existing NTOG
tools in practice. We also calculate the p-value and the effect size
of TEval@buggy compared to TEval@fixed in terms of Precision,
which turn out to be less than 0.001 and large. These results indicate
that the Precision of TOGA using TEval@buggy is also significantly
worse than that using TEval@fixed, consistent with our findings in
RQ1.

In summary, we find that when using TEval@buggy,
TOGA’s Precision is only 0.38%. This calls for more efforts on
improving existing NTOG approaches before applying them
in practice.

3.4
RQ3: Comparing with a Straightforward
Baseline

When investigating RQ1 and RQ2, we also manually inspect the
generated test oracles to better understand TOGA’s effectiveness
and practicability. We find that for the generated test oracles which
can find bugs, over 60% of them simply expect no exception raised.
A similar phenomenon was also observed by Dinella et al. [12].
This inspires us that a straightforward baseline, which simply pre-
dicts all oracles as no exception raised, may achieve comparable
performance. We refer to this baseline as NoException. Specifically,
NoException does not explicitly generate any assert statement, it
directly regards the test prefixes generated by EvoSuite as the gen-
erated test cases. If such a test case throws any exception during
execution, NoException regards it as a failed test case. Comparing

Table 3: Comparison of NoException and TOGA in BugFound
and Precision using TEval@buggy.

Approach
BugFound
Precision
#TP
#FP

NoException
44.4
0.77%
73.5
9415.9
TOGA
64.4
0.38%
110.7
29099.4

NoException with NTOG approaches can help practitioners better
understand the benefits they can gain from neural models compared
to implicit oracles. However, to the best of our knowledge, no prior
work has explicitly compared existing NTOG approaches with this
baseline. Therefore, this RQ aims to fill this gap.
Approach: We use TEval@buggy, which is more realistic than
the original TEval, to evaluate NoException and TOGA, and com-
pare their performance in terms of BugFound and Precision. Also,
Wilcoxon signed-rank test [45] and Cliff’s delta [10] are used for
statistical analysis.
Result: Table 3 presents the evaluation results of NoException
and TOGA. We observe that NoException can find 44.4 bugs with a
Precision of 0.77% on average. Although NoException finds 31.1%
(20) fewer bugs than TOGA, its Precision is twice TOGA’s Preci-
sion. The statistical analysis also show that NoException’s better
performance in terms of Precision is significant (p-value < 0.001)
with a large effect size. In addition, we calculate the intersection
of the bugs found by NoException and TOGA, and find it contains
39.7 bugs on average. This means NoException can also find sev-
eral bugs that cannot be found by TOGA. These results may imply
that the practicability and effectiveness of TOGA require further
investigation and discussion.

In summary, we find that simply generating the oracle that
no exception should be thrown can achieve 68.9% of TOGA’s
performance in terms of BugFound and twice TOGA’s Preci-
sion.

4
AN ADDITIONAL RANKING STEP

As presented in Section 3.3, even for the state-of-the-art NTOG
approach TOGA, to find a bug-finding test case, developers need to
manually check over 260 failed test cases on average. This is usually
impractical and even unacceptable for developers due to limited
development resources in practice. A more realistic usage scenario
is that after an NTOG tool generates many failed test cases for a
component, developers only have time to manually check a few
of them. Therefore, an evaluation method for NTOG should also
assess the bug-finding performance in a cost-effective way to help
practitioners better understand NTOG approaches’ practicability.
Motivated by this observation, we first introduce an additional
ranking step in TEval@buggy after all generated test cases are
executed. For each bug, before presenting all of its failed test cases
to developers, this step ranks these test cases according to their
probability of triggering bugs. Developers can check the top-ranked
test cases based on the amount of their available time. Then, we
introduce a new evaluation metric named Found@K, which counts
how many bugs can be found if developers only check the top-
k recommended test cases for each bug. It is formally defined as


---

## Page 7

Towards More Realistic Evaluation for Neural Test Oracle Generation
ISSTA ’23, July 17–21, 2023, Seattle, WA, United States

Test Prefixes

NTOG I/O

Features

Focal Context

0.5

Execution Output

Ranked Failed

Model Predictions

0.3

Features

Test Cases

-0.1

Failed Test Cases

Test Similarity

Extract
Features

Isolation

Scores

Execution Traces

Features

Forest

Figure 3: The procedure of our ranking method.

follows:

𝐹𝑜𝑢𝑛𝑑@𝐾=
Í𝑛
𝑖=1 𝜎(𝑟𝑖≤𝐾)

𝑛
where 𝑟𝑖refers to the rank of the first bug-finding test case for bug
𝑖, 𝜎denotes the indicator function, which returns 1 if 𝑟𝑖≤𝐾or
0 otherwise, and 𝑛is the number of bugs. If no bug-finding test
case is generated for bug 𝑖, 𝑟𝑖is set to infinite. This metric can help
measure the cost-effectiveness of NTOG approaches in terms of
bug finding,

4.1
An Unsupervised Ranking Method

To instantiate this ranking step, we propose a novel unsupervised
ranking method. Our ranking method is inspired by the following
observations: First, according to the evaluation results in Section 3.3,
bug-finding test cases (i.e., TPs) are usually rare in all the failed
test cases. Second, bug-finding test cases usually share different
characteristics from other failed test cases (i.e., FPs). For example,
when inspecting the evaluation results in Section 3.3, we find that
bug-finding test cases are more likely to throw exceptions that are
rarely or never thrown by FPs, and they are more likely to call a
method that is rarely or never called by FPs. One possible reason
for this is that bugs are usually related to exceptional or corner
cases instead of normal cases, and are rare compared to correctly
implemented features. Based on these observations, FPs and TPs
can be regarded as normal samples and outliers, respectively, and
the ranking problem can be converted into an outlier detection
problem. With this intuition, we build our ranking method based
on outlier detection algorithms.
Figure 3 presents the procedure of our ranking method. Specifi-
cally, given a bug and the failed test cases generated by an NTOG
approach for this bug, our ranking method first collects inputs from
multiple sources, including the inputs of the NTOG approach, the
predictions of the approach’s neural model, the source code and
the stack traces of the failed test cases. Next, it extracts three di-
mensions of features for each failed test case. Then, based on such
features, the Isolation Forest [24] algorithm is adopted to detect
outliers from all the failed test cases and calculate the anomaly
score of each failed test. Finally, we rank the failed test cases based
on their anomaly scores. The more likely a test case is to be an
outlier, the higher its rank is. Based on these ranked test cases,
Found@K can be easily calculated.

4.2
Features of Generated Test Cases

Based on the characteristics of this ranking task, we manually craft
three dimensions of features to help outlier detectors distinguish
TPs and FPs, as shown in Table 4:
NTOG I/O: This dimension of features is extracted from the
input and output of the NTOG approach. For each failed test case,
focal_method_name_count and test_distinct_code_line mea-
sure its uniqueness and rareness. If this test case checks a focal

1 org.jfree.data.KeyedObjects2D_ESTest::test131
2 junit.framework.AssertionFailedError: expected:<1> but was:
<2>
3
at org.junit.Assert.fail(Assert.java:88)
4
org.junit.Assert.failNotEquals(Assert.java:743)
5
org.junit.Assert.assertEquals(Assert.java:118)
6
......

Figure 4: The stack trace of a failed test case.

method that is not checked by others or contains distinct code lines,
it is rarer and more unique, and therefore is more likely to be a TP.
is_exception and is_no_exception are used to indicate the type
of the generated oracle.
Execution Output: Before ranking the failed test cases, we have
already obtained their stack traces. Figure 4 presents the stack trace
of a failed test case. We can see that a stack trace contains the
qualified name of the test case (the first line), the exception line (the
second line) and the execution stack (other lines). The exception line
consists of the raised exception, e.g., “junit.framework.Assertio
nFailedError”, and its message, e.g., “expected:<1> but was:<2>”.
We refer to such raised exception as the trace exception and denote
the last item of the trace exception, e.g., “AssertionFailedError” in
Figure 4, as the trace exception name. test_prefix_exception can
help identify the source of the trace exception. For each failed test
case, we extract this feature by parsing its test prefix and checking
whether there is any catch clause. trace_exception_count and
trace_exception_msg_count can reflect the uniqueness of this
trace exception. If the trace exception is an AssertionFailError, or
its name appears in the focal method or the focal docstring, we
regard the trace exception as an expected trace exception. Because
it is common and usually expected that a failed test is caused by
assertion fails and that a generated test case throws an exception
recording in the focal method or the focal docstring. Intuitively, the
more surprising the trace exception is, the more likely the test case
reaches some unspecified or buggy behaviors. Therefore, we use
is_exp_trace_exception to indicate whether the trace exception
is expected and leverage unexp_trace_e_count to measure the
uniqueness of an unexpected trace exception among all the unex-
pected trace exceptions of this bug. focal_unexp_trace_e_count
further refines the measurement of such uniqueness by additionally
considering the focal method for counting.
Text Similarity: test_doc_sim measures the textual similarity
between the test case and the focal docstring. Since the focal doc-
string may contain the informal specification of the focal method,
a failed test case that is more similar to the focal docstring may be
more likely to reveal bugs. To calculate such similarity, we convert
the focal method and the test case into TF-IDF vectors and calculate
their cosine similarity.
In summary, because these features are crafted for outlier detec-
tion techniques, they either provide the basic information of each
test case, e.g., is_exception and is_no_exception, or try to measure
the unexpectedness and rareness of each test case.
We would like to claim our ranking method should not be re-
garded as preferring exception oracles. Although seven out of the
eleven features seem related to exceptions, five out of the seven
features focus on trace exceptions, which are obtained from the


---

## Page 8

ISSTA ’23, July 17–21, 2023, Seattle, WA, United States
Zhongxin Liu, Kui Liu, Xin Xia, and Xiaohu Yang

Table 4: The features crafted for our ranking method
Feature Group
Features
Description

focal_method_name_count
The number of the test cases of which the focal method name is the same as that of
this testj.
test_distinct_code_line
The number of the code lines in this test case that do not appear in other tests.
is_exception
The generated oracle expects an exception.
is_no_exception
The generated oracle expects no exception.

NTOG I/O

test_prefix_exception
Whether the regression behavior of the test prefix is throwing an exception.
trace_exception_count
The number of the test cases that have the same trace exception as this test case.
trace_exception_msg_count
The number of the test cases of which the stack traces contain the same exception
message as this test case.
is_exp_trace_exception
Whether the trace exception is expected. The trace exception is regarded as expected
if it is an AssertionFailError or its name appears in the focal method or the focal
docstring.
unexp_trace_e_count
This feature is set to 0 if this trace exception is expected, and to the number of the test
cases of which the trace exceptions are unexpected and the same as this exception if
this trace exception is unexpected.
focal_unexp_trace_e_count
This feature is set to 0 if the trace exception is expected. If this trace exception is
unexpected, this feature is set to the number of the test cases of which the trace
exceptions are unexpected and the focal methods as well as the trace exceptions are
the same as those of this test case.
Text Similarity
test_doc_sim
The textual similarity between the test case and the focal docstring.

Execution Output

execution results instead of the source code of test cases. Our rank-
ing method aims to rank failed test cases. Each failed test case, no
matter whether its oracle is an exception or assertion oracle, has
a stack trace and a stack exception. Therefore, our method has
no inherent preference for exception oracles. In addition, all the
features can be extracted from the inputs and outputs of an NTOG
approach and are independent of NTOG approaches.

4.3
The Adoption of Isolation Forest

Our ranking method uses Isolation Forest to calculate anomaly
scores. Isolation Forest is a widely-used unsupervised technique
for outlier detection. It has a linear time complexity that has exhib-
ited high accuracy over a variety of datasets [25]. We implement
Isolation Forest using the scikit-learn [35] toolkit with default pa-
rameters. Since Isolation Forest is based on random partitioning
of features, for each bug, we run iForest 10 times with different
random states and report the mean value of each metric as the
result of one experiment.

4.4
Evaluation of Our Ranking Method

To assess the effectiveness of our proposed ranking method and
measure TOGA’s bug-finding performance in a cost-effective way,
we evaluate TOGA and NoException using TEval@buggy plus our
ranking method and compare the evaluation results with those
obtained by using TEval@buggy plus random ranking. Similar to
our ranking method, the random ranking method is also run 10
times with different random states in one experiment to reduce
bias. Found@K metrics with k=1, 3, 5, and 10 are reported to show
whether our proposed ranking method can improve the practica-
bility of TOGA. Wilcoxon signed-rank tests [45] at the confidence
level of 95% and Cliff’s deleta [10] are also conducted.

Table 5: The evaluation results of our ranking method.

Approach
Ranking
F@1
F@3
F@5
F@10

NoException
Random
11.81
22.91
27.76
35.93
NoException
Ours
13.74
26.38
30.07
37.52

TOGA
Random
9.89
20.85
27.61
39.09
TOGA
Ours
15.19
29.59
36.31
45.30

All experiments uses TEval@buggy. F@K refers to Found@K.

The evaluation results are shown in Table 5. We can observe that
for both NoException and TOGA, our ranking method can improve
their bug-finding performance in terms of Found@K, especially
when K is small. In detail, when using TOGA, our ranking method
can help developers find 5.3 (53.6%), 8.74 (41.9%) and 8.70 (31.5%)
more bugs if developers only check the recommended top-1, 3 and
5 failed test cases of each bug. The statistical analysis shows that
the performance improvements of NoException after using our
ranking method are significant in terms of all Found@K with at
least medium effect sizes. Our ranking method also significantly
improves the Found@K of TOGA with large effect sizes. These
results indicate that our ranking method can effectively improve
the practicability of both NoException and TOGA.
According to Table 5 and our statistical analysis, we surprisingly
observe that NoException+Random significantly performs better
than TOGA+Random in terms of Found@1, and Found@3 with
at least medium effect size, which means the cost-effectiveness of
NoException is better than that of TOGA if developers only ran-
domly check one or three failed tests cases to find a bug. But NoEx-
ception+Random does not significantly outperform TOGA+Random
in terms of Found@5 and performs significantly worse in terms of
Found@10. This is reasonable because as presented in Section 3.4,
TOGA can generate more bug-finding test cases for more bugs, and


---

## Page 9

Towards More Realistic Evaluation for Neural Test Oracle Generation
ISSTA ’23, July 17–21, 2023, Seattle, WA, United States

if the search space is enlarged, it would be more likely to find a
bug-finding test case generated by TOGA.
It is interesting that when using our ranking method, TOGA
achieves better Found@K than NoException for all Ks. All the p-
values are less than 0.05, indicating significant performance differ-
ences. These results demonstrate that when using a proper ranking
method, TOGA can indeed be more practical than NoException, and
also highlight the importance of ranking methods for evaluating
NTOG approaches.

5
TOWARDS MORE REALISTIC EVALUATION

In this section, we incorporate all the enhancements we made on
TEval with TEval, and propose a more realistic evaluation method
named TEval+ for NTOG. Figure 5 presents the overall procedure
of TEval+, which is similar to the procedure of TEval described in
Section 2.2. However, TEval+ makes several enhancements over
TEval, which we summarize as seven rules of thumb to boost NTOG
approaches towards their practical usages:

• Be cautious to avoid data leakage. Some information con-
tained in a bug benchmark is not available when applying NTOG
approaches in practice, e.g., the patch fixing the target bug. There-
fore, we should be careful not to use such information when
constructing inputs for NTOG approaches. Following this rule,
TEval+ uses EvoSuite to generate test prefixes on the buggy
program versions instead of the bug-fixed program versions.
• Reduce random noise. During the evaluation, the techniques
relying on randomized algorithms should be run multiple times
to reduce noise. In fact, this rule has been proposed by prior
work [3], but not all NTOG work respects it. Following this
rule, TEval+ runs EvoSuite 10 times and accordingly conducts
experiments 10 times to reduce the bias. In addition, for our
proposed ranking method, we also run Isolation Forest 10 times
because it is also a randomized technique.
• Be careful about duplicate data. Duplicate test cases may
introduce bias. It is necessary to avoid feeding duplicate inputs to
NTOG approaches and to deduplicate test cases before execution.
Following this rule, TEval+ explicitly deduplicates the generated
test cases before executing them.
• Handle compilation errors properly. When encountering
compilation errors, an evaluation method should carefully fil-
ter the corresponding test cases or try to fix such errors, and
should avoid affecting other test cases with no errors. Based on
this rule, TEval+ fixes the over-filtering problem in the original
implementation of TEval.
• Keep real-world usage scenarios in mind. The goal of evalua-
tion methods is to measure the real-world performance of NTOG
approaches. Therefore, evaluation methods for NTOG should
always keep real-world usage scenarios in mind. Based on this
rule, TEval+ does not generate test prefixes from the bug-fixed
program versions, introduces an additional ranking step to mimic
the usage scenario, and proposes the Found@K metric to measure
the bug-finding performance of NTOG approaches practically.
• Compare NTOG approaches with simple and straightfor-
ward baselines. Potential users of NTOG approaches also care
about the benefits and Return on Investment (ROI) of neural

Table 6: TOGA’s performance on different oracle types using
TEval@buggy.

Oracle Type
BugFound
Precision
#TP
#FP

expect_no_exception
39.7
0.92%
64.3
6889.9
expect_exception
10.3
0.39%
20.8
5323.9
assertion
18.2
0.16%
25.6
16885.6

all
64.4
0.38%
110.7 29099.4

Table 7: TOGA’s performance on different oracle types using
TEval+.

Approach
Ranking
F@1
F@3
F@5
F@10

expect_no_exception
Ours
15.62
25.47
29.69
34.94
expect_exception
Ours
4.59
5.81
6.38
8.16
assertion
Ours
3.48
7.94
9.98
12.30

all
Ours
15.19
29.59
36.31
45.30

models, which can be demonstrated by comparing NTOG ap-
proaches with simple and straightforward baselines. Following
this rule, TEval+ introduces a naive baseline named NoException
and explicitly compares NTOG approaches with this baseline.
• Pay attention to post-processing. Besides generating oracles,
how to make use of the generated oracles in practice is also
an important question. To demonstrate this, TEval+ proposes a
novel unsupervised ranking method to rank the failed test cases
and significantly improves the practicability of the underlying
NTOG approaches.

6
DISCUSSION
6.1
TOGA’s performance on different oracle
types

The oracles generated by TOGA can be divided into three types:
expect_no_exception, expect_exception and assertion. Following
Dinella et al. [12], we break down TOGA’s performance on the three
types of oracles for a deeper investigation. For TEval@buggy, we
split the constructed test cases into three groups based on their ora-
cle types and calculate the BugFound and Precision for each group,
as shown in Table 6. Please note that some bugs can be triggered by
different types of oracles. Thus, the sum of the first three BugFound
values in Table 6 is greater than the number of the bugs found by
TOGA (i.e., 64.4). For TEval+, we also split the ranked failed test
cases into three groups and calculate the Found@K metrics for
each group, as shown in Table 7. From Table 6 and Table 7, we can
see that TOGA’s performance is quite different on the three types
of oracles. Best performance is achieved on expect_no_exception
oracles, which strengthens the motivation of using NoException
as a baseline. There are substantial margins between the perfor-
mance on expect_no_exception oracles and the performance on the
other two types of oracles, calling for more efforts on improving
the generation of expect_exception and assertion oracles.
A variant of TOGA, which only outputs the expect_no_exception
oracles generated by TOGA, seems similar to NoException. How-
ever, the TOGA paper does not provide explicit and comprehensive
comparison between TOGA and this variant. NoException also


---

## Page 10

ISSTA ’23, July 17–21, 2023, Seattle, WA, United States
Zhongxin Liu, Kui Liu, Xin Xia, and Xiaohu Yang

Automated Test
Generation Tool

Test Prefixes

Focal Context

Buggy
Program

Neural Oracle
Generation Tool

BugFound

compare

Ranked Failed

Tests Cases

Found@K

NoException

Evaluate

Figure 5: The procedure of TEval+.

provides additional benefits: First, it is independent of other NTOG
approaches, does not use neural models, and thus is simpler and
easier to use. Second, NoException can find more bugs than this
variant (44.4 v.s. 39.7). Therefore, we suggest practitioners explic-
itly consider NoException as a baseline to better evaluate NTOG
approaches.

6.2
Threats to Validity

The first threat to the validity of this study is that EvoSuite and
Isolation Forest are randomized algorithms and are affected by
chance. To cope with this threat, we run EvoSuite 10 times with
different random states for each bug, run Isolation Forest 10 times
with different random states in each experiment, and report the
mean value of each evaluation metric as the result. In addition, we
also conduct statistical analysis to demonstrate the significance of
our observed performance differences.
Second, there may be errors and biases in our experiments. To
mitigate this threat, we re-use the trained model of TOGA provided
by its authors, build TEval+ based on the official implementation
of TEval, and follow the settings used by TOGA unless explicitly
stated. In addition, We have double-checked our code and data, and
released them in our replication package [2].
Another threat to validity is the potentially hidden gaps that are
not realized by us between TEval+ and real-world usage scenarios.
A potential gap is that for each bug, both TEval and TEval+ use
EvoSuite to generate test prefixes only for the classes that will
be patched to fix this bug. However, bug locations are unknown
when developers use NTOG approaches to find bugs. Therefore,
this setting is potentially unrealistic. We do not investigate this
setting’s impact in this work, because: First, considering there are
at least tens and hundreds of focal classes in a real-world project,
generating test prefixes and oracles for all of them is expensive and
time-consuming. Second, there do exist some situations in practice
where we only need to generate oracles for a limited number of
classes or even methods. For example, when using NTOG tools after
a code commit, developers only need to generate test prefixes for the
classes or even the methods that have been changed in this commit.
It would be interesting for future work to further investigate the
impact of this setting on the bug-finding performance of NTOG
approaches and to find and fill other gaps between the evaluation
methods for NTOG and the real-world usage scenarios.

Test Oracles

Test Cases

Deduplicate Filter Errors

Failed Test

Cases

Execute
Rank

7
RELATED WORK
This section discusses the related work concerning automated test
generation and test oracle generation.

7.1
Unit Test Generation

TEval leverages unit test generation tools to generate test prefixes
for NTOG approaches. Researchers have proposed many tools for
automated unit test generation [14, 26, 28, 32, 38, 41, 50]. For exam-
ple, EvoSuite [13, 14] is a typical and widely used search-based test
generation tool, which leverages genetic algorithms to optimize the
coverage and the length of a whole test suite. Randoop [32] is a ran-
dom test generation tool, which generates unit tests by randomly
selecting a method call to apply and finding the arguments for the
call from previously-constructed objects. Zhang et al. [49] proposed
a tool name Palus, which enhances a random test generator with
the information collected using static and dynamic analysis. Sym-
stra [47] is a constraint-based tool, which uses symbolic execution
to explore the object states of an object-oriented system and gen-
erate tests. DART [15], CUTE [38] and Pex [40] combine symbolic
and concrete execution, i.e., use concolic execution, to enumerate
feasible execution paths and synthesize test inputs. Evacon [20]
serially combines symbolic execution and search-based techniques
to generate test cases with higher branch coverage. Malburg and
Fraser [28] proposed to use a constraint solver to help search-based
techniques avoid being stuck in local optima. Lukasczyk et al. [26]
proposed a test generation tool named Pynguin, which adapts the
techniques behind EvoSuite and Randoop for Python projects. In
addition, fuzzers [31, 50] generates test inputs based on grammars
or valid corpus, i.e., generation-based fuzzing, or by mutating seed
inputs, i.e., mutation-based fuzzing. Recently, Tufano et al. [41] pro-
posed a learning-based generation tool named AthenaTest which
pre-trains a BART model [23] using English and Code corpora, and
fine-tunes this model to generate test cases with the corresponding
focal context.
Different from the above-mentioned work, this work focuses on
test oracle generation instead of unit test generation, and targets
studying and improving existing evaluation methods for neural test
oracle generation.

7.2
Test Oracle Generation

Although unit test generation tools are powerful, they still face
the oracle problem [4] and cannot generate test cases that reveal
functional bugs in the current program version. To fill the gap,


---

## Page 11

Towards More Realistic Evaluation for Neural Test Oracle Generation
ISSTA ’23, July 17–21, 2023, Seattle, WA, United States

researchers have proposed some approaches to automatically gen-
erate test oracles that can capture functional bugs. One type of them
assumes that the intended behavior of a Unit Under Test (UUT)
is informally described in its documentation, and synthesizes test
oracles from the documentation based on natural language pro-
cessing (NLP) techniques, manually-summarized rules or patterns,
and search-based techniques [6, 7, 16, 34, 39, 48]. For example,
Goffi et al. [16] proposed Toradocu to generate exceptional ora-
cles. Toradocu first leverages NLP techniques to extract exceptions
and their subjects and predicates from Javadoc, then creates condi-
tional expressions based on pattern and lexical matching, and finally
generates test oracles using run-time instrumentation. JDoctor [6]
enhances Toradocu by using not only pattern and lexical matching,
but also semantic matching, and extends the crafted rules to gener-
ate preconditions, assertion oracles and exceptional oracles. Blasi
et al. [7] proposed Memo, which automatically derives metamor-
phic equivalence relations from natural language documentation.
The above-mentioned tools rely on specific patterns or rules and
can hardly handle the flexibility and diversity of real-world code
documentation. C2S [48] aligns words in comments and tokens
in specifications and leverages a search-based technique to syn-
thesize JML specifications [8] based on such alignment. C2S does
not rely on patterns but requires developer-written test prefixes to
filter invalid specifications. Moreover, prior work [12] showed that
these tools struggle to infer bug-finding oracles for the Defects4J
benchmark.
Recently, researchers proposed to leverage deep neural networks
to generate test oracles by learning from developer-written test
cases [12, 29, 30, 42, 44], i.e., neural test oracle generation (NTOG).
Watson et al. [44] proposed Atlas, which leverages a neural encoder-
decoder model with copy network to generate assert statements
based on developer-written test prefixes and focal methods. Mas-
tropaolo et al. [29, 30] pre-trained a T5 model [37] using massive
raw source code, abstracted source code and code comments, and
fine-tuned this model for multiple code-related tasks including as-
sert statement generation. Tufano et al. [42] proposed to pre-trained
a BART model [23] on large English and code corpora, and fine-
tuned the pre-trained model to generate assert statements. Recently,
Dinella et al. [12] proposed an NTOG tool named TOGA, which is
shown to achieve state-of-the-art bug-finding performance.
In this work, we conduct our case study using TOGA. Different
from existing studies, this work focuses on how to better evaluate
the bug-finding performance of NTOG tools, instead of proposing a
new test oracle generation approach. Therefore, it is complementary
to existing test oracle generation approaches and can inspire more
realistic evaluation methods for this research field.

8
CONCLUSION AND FUTURE WORK

This work focuses on the realistic evaluation for neural test oracle
generation (NTOG). We first point out three inappropriate settings
in existing evaluation methods and comprehensively investigate
their impacts on evaluating and understanding the bug-finding
performance of NTOG approaches. Our experimental results show
that all three settings have negative impacts on measuring or un-
derstanding the performance of NTOG approaches, and even the

state-of-the-art NTOG approach TOGA suffers from limited pre-
cision. Next, we introduce a ranking step in existing evaluation
methods and propose a more realistic evaluation metric Found@K
to help measure the practicability of NTOG approaches. Then, we
instantiate this ranking step with a novel unsupervised ranking
method, which is based on three dimensions of features specifically
designed for this task and an outlier detector. Our ranking method
can significantly improve the cost-effectiveness of TOGA. Finally,
we incorporate all our enhancements with existing evaluation meth-
ods to construct a more realistic evaluation method named TEval+
and summarize seven rules of thumb to help practitioners better
evaluate and understand the performance of NTOG approaches.
In the future, we plan to extend this work to consider more test
prefix generation techniques, such as Randoop and EvoSuite with
different fitness functions, and more neural test oracle generation
approaches.

ACKNOWLEDGMENTS

This research/project is supported by the National Natural Sci-
ence Foundation of China (No. 62202420, No. 62172214 and No.
U20A20173) and the Natural Science Foundation of Jiangsu Province,
China (No. BK20210279). Zhongxin Liu gratefully acknowledges
the support of Zhejiang University Education Foundation Qizhen
Scholar Foundation.

REFERENCES

[1] 2022. TOGA Artifact. https://github.com/microsoft/toga.
[2] 2023. Our Replication Package. https://github.com/Tbabm/TEval-plus.
[3] Andrea Arcuri and Lionel Briand. 2011. A Practical Guide for Using Statistical
Tests to Assess Randomized Algorithms in Software Engineering. In Proceedings
of the 33rd International Conference on Software Engineering. ACM, 1–10. https:
//doi.org/10.1145/1985793.1985795
[4] Earl T. Barr, Mark Harman, Phil McMinn, Muzammil Shahbaz, and Shin Yoo. 2014.
The Oracle Problem in Software Testing: A Survey. IEEE transactions on software
engineering 41, 5 (2014), 507–525. https://doi.org/10.1109/TSE.2014.2372785
[5] Al Bessey, Ken Block, Ben Chelf, Andy Chou, Bryan Fulton, Seth Hallem, Charles
Henri-Gros, Asya Kamsky, Scott McPeak, and Dawson Engler. 2010. A Few
Billion Lines of Code Later: Using Static Analysis to Find Bugs in the Real World.
Commun. ACM 53, 2 (2010), 66–75.
[6] Arianna Blasi, Alberto Goffi, Konstantin Kuznetsov, Alessandra Gorla, Michael D.
Ernst, Mauro Pezzè, and Sergio Delgado Castellanos. 2018. Translating Code
Comments to Procedure Specifications. In Proceedings of the 27th ACM SIGSOFT
International Symposium on Software Testing and Analysis. 242–253. https://doi.
org/10.1145/1646353.1646374
[7] Arianna Blasi, Alessandra Gorla, Michael D. Ernst, Mauro Pezzè, and Antonio
Carzaniga. 2021. MeMo: Automatically Identifying Metamorphic Relations in
Javadoc Comments for Test Automation. Journal of Systems and Software 181
(2021), 111041. https://doi.org/10.1016/j.jss.2021.111041
[8] Lilian Burdy, Yoonsik Cheon, David R. Cok, Michael D. Ernst, Joseph R. Kiniry,
Gary T. Leavens, K. Rustan M. Leino, and Erik Poll. 2005. An Overview of JML
Tools and Applications. International journal on software tools for technology
transfer 7, 3 (2005), 212–232. https://doi.org/10.1007/s10009-004-0167-4
[9] Zimin Chen, Steve Kommrusch, Michele Tufano, Louis-Noël Pouchet, Denys
Poshyvanyk, and Martin Monperrus. 2021. SequenceR: Sequence-to-Sequence
Learning for End-to-End Program Repair. IEEE Transactions on Software Engi-
neering 47, 9 (2021), 1943–1959. https://doi.org/10.1109/TSE.2019.2940179
[10] Norman Cliff. 2014. Ordinal Methods for Behavioral Data Analysis. Psychology
Press.
[11] Ermira Daka and Gordon Fraser. 2014. A Survey on Unit Testing Practices and
Problems. In Proceedings of the 25th IEEE International Symposium on Software
Reliability Engineering. IEEE Computer Society, 201–211. https://doi.org/10.1109/
ISSRE.2014.11
[12] Elizabeth Dinella, Gabriel Ryan, Todd Mytkowicz, and Shuvendu K. Lahiri. 2022.
TOGA: A Neural Method for Test Oracle Generation. In Proceedings of the 44th
IEEE/ACM International Conference on Software Engineering. ACM, 2130–2141.
https://doi.org/10.1145/3510003.3510141
[13] Gordon Fraser and Andrea Arcuri. 2011. EvoSuite: automatic test suite generation
for object-oriented software. In Proceedings of the 19th ACM SIGSOFT symposium


---

## Page 12

ISSTA ’23, July 17–21, 2023, Seattle, WA, United States
Zhongxin Liu, Kui Liu, Xin Xia, and Xiaohu Yang

and the 13th European conference on Foundations of software engineering. ACM,
416–419. https://doi.org/10.1145/2025113.2025179
[14] Gordon Fraser and Andrea Arcuri. 2012. Whole Test Suite Generation. IEEE
Transactions on Software Engineering 39, 2 (2012), 276–291. https://doi.org/10.
1109/TSE.2012.14
[15] Patrice Godefroid, Nils Klarlund, and Koushik Sen. 2005.
DART: Directed
Automated Random Testing. In Proceedings of the 2005 ACM SIGPLAN Con-
ference on Programming Language Design and Implementation. ACM, 213–223.
https://doi.org/10.1145/1065010.1065036
[16] Alberto Goffi, Alessandra Gorla, Michael D. Ernst, and Mauro Pezzè. 2016. Au-
tomatic Generation of Oracles for Exceptional Behaviors. In Proceedings of the
25th International Symposium on Software Testing and Analysis. ACM, 213–224.
https://doi.org/10.1145/2931037.2931061
[17] Alan Hartman. 2002. Is ISSTA Research Relevant to Industry? ACM SIGSOFT
Software Engineering Notes 27, 4 (2002), 205–206. https://doi.org/10.1145/566172.
566207
[18] Xing Hu, Ge Li, Xin Xia, David Lo, and Zhi Jin. 2018. Deep Code Comment
Generation. In Proceedings of the 26th Conference on Program Comprehension.
ACM, 200–210. https://doi.org/10.1145/3196321.3196334
[19] Xing Hu, Ge Li, Xin Xia, David Lo, and Zhi Jin. 2019. Deep Code Comment
Generation with Hybrid Lexical and Syntactical Information. Empirical Software
Engineering (2019), 1–39. https://doi.org/10.1007/s10664-019-09730-9
[20] Kobi Inkumsah and Tao Xie. 2008. Improving Structural Testing of Object-
Oriented Programs via Integrating Evolutionary Testing and Symbolic Execution.
In Proceedings of the 23rd IEEE/ACM International Conference on Automated Soft-
ware Engineering. IEEE, 297–306. https://doi.org/10.1109/ASE.2008.40
[21] Brittany Johnson, Yoonki Song, Emerson Murphy-Hill, and Robert Bowdidge.
2013. Why Don’t Software Developers Use Static Analysis Tools to Find Bugs?.
In Proceedings of the 35th International Conference on Software Engineering. IEEE,
672–681. https://doi.org/10.1109/ICSE.2013.6606613
[22] René Just, Darioush Jalali, and Michael D. Ernst. 2014. Defects4J: A Database
of Existing Faults to Enable Controlled Testing Studies for Java Programs. In
Proceedings of the 2014 International Symposium on Software Testing and Analysis.
ACM, 437–440. https://doi.org/10.1145/2610384.2628055
[23] Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman
Mohamed, Omer Levy, Veselin Stoyanov, and Luke Zettlemoyer. 2020. BART:
Denoising Sequence-to-Sequence Pre-training for Natural Language Generation,
Translation, and Comprehension. In Proceedings of the 58th Annual Meeting of
the Association for Computational Linguistics. Association for Computational
Linguistics, 7871–7880. https://doi.org/10.18653/v1/2020.acl-main.703
[24] Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. 2008. Isolation Forest. In
Proceedings of the 8th IEEE International Conference on Data Mining. IEEE, 413–
422. https://doi.org/10.1109/ICDM.2008.17
[25] Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. 2012. Isolation-Based Anomaly
Detection. ACM Transactions on Knowledge Discovery from Data 6, 1 (2012), 1–39.
https://doi.org/10.1145/2133360.2133363
[26] Stephan Lukasczyk and Gordon Fraser. 2022. Pynguin: Automated Unit Test
Generation for Python. (2022), 168–172. https://doi.org/10.1145/3510454.3516829
[27] Stephan Lukasczyk, Florian Kroiß, and Gordon Fraser. 2020. Automated Unit Test
Generation for Python. In Proceedings of the 12th International Symposium on
Search Based Software Engineering. Springer, 9–24. https://doi.org/10.1007/978-
3-030-59762-7_2
[28] Jan Malburg and Gordon Fraser. 2011. Combining Search-Based and Constraint-
Based Testing. In Proceedings of the 26th IEEE/ACM International Conference on
Automated Software Engineering. IEEE, 436–439. https://doi.org/10.1109/ASE.
2011.6100092
[29] Antonio Mastropaolo, Nathan Cooper, David Nader-Palacio, Simone Scalabrino,
Denys Poshyvanyk, Rocco Oliveto, and Gabriele Bavota. 2023. Using Transfer
Learning for Code-Related Tasks. IEEE Transactions on Software Engineering 49,
4 (2023), 1580–1598. https://doi.org/10.1109/TSE.2022.3183297
[30] Antonio Mastropaolo, Simone Scalabrino, Nathan Cooper, David Nader Palacio,
Denys Poshyvanyk, Rocco Oliveto, and Gabriele Bavota. 2021. Studying the
Usage of Text-To-Text Transfer Transformer to Support Code-Related Tasks. In
Proceedings of the 43rd IEEE/ACM International Conference on Software Engineering.
336–347. https://doi.org/10.1109/ICSE43902.2021.00041
[31] Barton P. Miller, Lars Fredriksen, and Bryan So. 1990. An Empirical Study of
the Reliability of UNIX Utilities. Commun. ACM 33, 12 (1990), 32–44.
https:
//doi.org/10.1145/96267.96279
[32] Carlos Pacheco and Michael D. Ernst. 2007. Randoop: Feedback-Directed Random
Testing for Java. In Companion to the 22nd ACM SIGPLAN Conference on Object-
oriented Programming Systems and Applications Companion. ACM, 815–816. https:
//doi.org/10.1145/1297846.1297902

[33] Carlos Pacheco, Shuvendu K. Lahiri, Michael D. Ernst, and Thomas Ball. 2007.
Feedback-Directed Random Test Generation. In Proceedings of the 29th Inter-
national Conference on Software Engineering. IEEE Computer Society, 75–84.
https://doi.org/10.1109/ICSE.2007.37
[34] Rahul Pandita, Xusheng Xiao, Hao Zhong, Tao Xie, Stephen Oney, and Amit
Paradkar. 2012. Inferring Method Specifications from Natural Language API
Descriptions. In Proceedings of the 34th International Conference on Software
Engineering. IEEE, 815–825. https://doi.org/10.1109/ICSE.2012.6227137
[35] Fabian Pedregosa, Gaël Varoquaux, Alexandre Gramfort, Vincent Michel,
Bertrand Thirion, Olivier Grisel, Mathieu Blondel, Peter Prettenhofer, Ron Weiss,
and Vincent Dubourg. 2011. Scikit-Learn: Machine Learning in Python. the
Journal of machine Learning research 12 (2011), 2825–2830. https://doi.org/10.
5555/1953048.2078195
[36] Strategic Planning. 2002. The Economic Impacts of Inadequate Infrastructure for
Software Testing. National Institute of Standards and Technology (2002), 1.
[37] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang,
Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. 2020. Exploring the limits of
transfer learning with a unified text-to-text transformer. The Journal of Machine
Learning Research 21, 1 (2020), 5485–5551.
[38] Koushik Sen, Darko Marinov, and Gul Agha. 2005. CUTE: a concolic unit testing
engine for C. In Proceedings of the 10th European Software Engineering Conference
held jointly with the 13th ACM SIGSOFT International Symposium on Foundations
of Software Engineering. ACM, 263–272. https://doi.org/10.1145/1081706.1081750
[39] Shin Hwei Tan, Darko Marinov, Lin Tan, and Gary T. Leavens. 2012. @ Tcom-
ment: Testing Javadoc Comments to Detect Comment-Code Inconsistencies. In
Proceedings of the 5th International Conference on Software Testing, Verification
and Validation. 260–269. https://doi.org/10.1109/ICST.2012.106
[40] Nikolai Tillmann and Jonathan de Halleux. 2008. Pex-White Box Test Generation
for .NET. In Proceedings of the 2nd International Conference on Tests and Proofs.
Springer, 134–153. https://doi.org/10.1007/978-3-540-79124-9_10
[41] Michele Tufano, Dawn Drain, Alexey Svyatkovskiy, Shao Kun Deng, and Neel
Sundaresan. 2020. Unit test case generation with transformers and focal context.
arXiv preprint arXiv:2009.05617 (2020). https://doi.org/10.48550/arXiv.2009.05617
[42] Michele Tufano, Dawn Drain, Alexey Svyatkovskiy, and Neel Sundaresan. 2022.
Generating Accurate Assert Statements for Unit Test Cases Using Pretrained
Transformers. In Proceedings of the 3rd ACM/IEEE International Conference on
Automation of Software Test. Association for Computing Machinery, 54–64. https:
//doi.org/10.1145/3524481.3527220
[43] Michele Tufano, Jevgenija Pantiuchina, Cody Watson, Gabriele Bavota, and
Denys Poshyvanyk. 2019. On Learning Meaningful Code Changes via Neural Ma-
chine Translation. In Proceedings of the 41st International Conference on Software
Engineering. IEEE/ACM, 25–36. https://doi.org/10.1109/ICSE.2019.00021
[44] Cody Watson, Michele Tufano, Kevin Moran, Gabriele Bavota, and Denys Poshy-
vanyk. 2020. On Learning Meaningful Assert Statements for Unit Test Cases. In
Proceedings of the 42nd International Conference on Software Engineering. ACM,
1398–1409. https://doi.org/10.1145/3377811.3380429
[45] Frank Wilcoxon. 1992. Individual Comparisons by Ranking Methods. In Break-
throughs in Statistics. Springer, 196–202.
[46] Tao Xie. 2006. Augmenting Automatically Generated Unit-Test Suites with
Regression Oracle Checking. In Proceedings of the 20th European Conference
on Object-Oriented Programming. Springer, 380–403.
https://doi.org/10.1007/
11785477_23
[47] Tao Xie, Darko Marinov, Wolfram Schulte, and David Notkin. 2005. Symstra: A
Framework for Generating Object-Oriented Unit Tests Using Symbolic Execution.
In Proceedings of the 11th International Conference on Tools and Algorithms for the
Construction and Analysis of Systems. Springer, 365–381. https://doi.org/10.1007/
978-3-540-31980-1_24
[48] Juan Zhai, Yu Shi, Minxue Pan, Guian Zhou, Yongxiang Liu, Chunrong Fang,
Shiqing Ma, Lin Tan, and Xiangyu Zhang. 2020.
C2S: Translating Natural
Language Comments to Formal Program Specifications. In Proceedings of the
28th ACM Joint Meeting on European Software Engineering Conference and
Symposium on the Foundations of Software Engineering. ACM, 25–37.
https:
//doi.org/10.1145/3368089.3409716
[49] Sai Zhang, David Saff, Yingyi Bu, and Michael D. Ernst. 2011. Combined Static
and Dynamic Automated Test Generation. In Proceedings of the 20th International
Symposium on Software Testing and Analysis. ACM, 353–363. https://doi.org/10.
1145/2001420.2001463
[50] Xiaogang Zhu, Sheng Wen, Seyit Camtepe, and Yang Xiang. 2022. Fuzzing: A
Survey for Roadmap. Comput. Surveys 54, 11s (2022), 1–36. https://doi.org/10.
1145/3512345

Received 2023-02-16; accepted 2023-05-03


---

