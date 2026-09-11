# 09 AutoOracle2026 AutoOracle High Quality C Test Oracle

- **Source File**: [`09_AutoOracle2026_AutoOracle_High_Quality_C_Test_Oracle.pdf`](file:///c:/Users/g1014/Documents/GitHub/Youchen/code-security-research/papers/09_AutoOracle2026_AutoOracle_High_Quality_C_Test_Oracle.pdf)
- **Total Pages**: 12

---

<!-- Page 1 -->

AutoOracle: High-Quality C++ Test Oracle Generation via Data
Quality-Driven and Filtering-Enabled LLMs
Cong Li
Samsung R&D Institute Xi’an
Xi’an, China
cong109.li@samsung.com
Jong-In Jang
Samsung Electronics
Hwaseong, Republic of Korea
jji.jang@samsung.com
Yuqi Zhang
Samsung R&D Institute Xi’an
Xi’an, China
yuqi1.zhang@samsung.com
Nakwon Lee
Samsung Electronics
Hwaseong, Republic of Korea
nakwon.lee@samsung.com
Bin Wang
Samsung R&D Institute Xi’an
Xi’an, China
bin01.wang@samsung.com
Yinghua Zhang
Samsung R&D Institute Xi’an
Xi’an, China
yingh.zhang@samsung.com
Chanwook Kim
Samsung Electronics
Hwaseong, Republic of Korea
chanwook.kim@samsung.com
Jia Zhang
Samsung R&D Institute Xi’an
Xi’an, China
jia2.zhang@samsung.com
HyunSeok Kim
Samsung Electronics
Hwaseong, Republic of Korea
hs0926.kim@samsung.com
Xing He
Samsung R&D Institute Xi’an
Xi’an, China
xing84.he@samsung.com
Kangho Roh
Samsung Electronics
Hwaseong, Republic of Korea
kangho.roh@samsung.com
Seongjun Ahn
Samsung Electronics
Hwaseong, Republic of Korea
seongjun.ahn@samsung.com

## Abstract

Test oracles (assertions used to verify program behavior) serve as
a validation benchmark in software testing by comparing the ac-
tual outputs with expected results. However, manually building
test oracles is time-consuming, and the existing AI-driven test ora-
cle generation schemes often suffer from noisy training data and
unreliable inference outputs. To this end, this paper proposes Au-
toOracle, a novel framework that leverages large language models
(LLMs)forautomatedtestoraclegenerationinC++. Itautomatically
constructs the first large-scale, high-quality C++ training dataset
through Code De-Differentiation Method and Data Quality Scoring
and Filtering Mechanism, fine-tunes the first domain-specific LLM
forC++testoraclegeneration, andimprovesthereliabilityofgener-
ated oracles via a Suspicious Oracle Filtering Framework. We have
evaluated our approach in terms of oracle quality and practicality.
Experimentalresultsonopen-sourceC++projectsdemonstratethat
AutoOracle improves accuracy by 2.13 times and reduces the error
rate by 52.3% compared with the state-of-the-art (SOTA) method.
In practice, on an embedded C++ solid state drive firmware project
at Samsung Electronics, AutoOracle generated test oracles with
higher compile/runtime success rates and received better feedback
in a survey of 19 practitioners, compared with the SOTA method.
These results indicate that AutoOracle can generate high-quality
test oracles, thereby significantly boosting test efficiency.
This work is licensed under a Creative Commons Attribution 4.0 International License.
ICSE-SEIP ’26, Rio de Janeiro, Brazil
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2426-8/26/04
https://doi.org/10.1145/3786583.3786868
CCS Concepts
• Software and its engineering→ Software testing and debug-
ging.
Keywords
Test oracle generation, Large Language models, C++ Testing, AI-
driven testing
ACM Reference Format:
Cong Li, Jong-In Jang, Yuqi Zhang, Nakwon Lee, Bin Wang, Yinghua
Zhang, Chanwook Kim, Jia Zhang, HyunSeok Kim, Xing He, Kangho Roh,
and Seongjun Ahn. 2026. AutoOracle: High-Quality C++ Test Oracle
Generation via Data Quality-Driven and Filtering-Enabled LLMs. In2026
IEEE/ACM 48th International Conference on Software Engineering (ICSE-SEIP
’26), April 12–18, 2026, Rio de Janeiro, Brazil. ACM, New York, NY, USA,
12 pages. https://doi.org/10.1145/3786583.3786868

## 1 Introduction

Testing,akeypartofthesoftwaredevelopmentlifecycle,isessential
for ensuring product quality [2]. A test case specifies the input
conditions, expected outcomes, and execution constraints for a
given software feature. Among the core components of a test
case, test oracles, such asassertEqual(a, nullptr), act as validation
mechanisms that compare the program’s actual output with the
expected results [28]. This comparison is crucial for identifying
software defects and verifying conformance to requirements and
design specifications.
However, manually developing test oracles, particularly by
adding assertion statements with expected outputs to automati-
cally generated test cases, imposes a significant burden for embed-
ded software such as solid state drive (SSD) firmware developed
at Samsung Electronics. In such firmware, data flow is difficult to
236

<!-- Page 2 -->

ICSE-SEIP ’26, April 12–18, 2026, Rio de Janeiro, Brazil Cong Li et al.
analyze due to constraints of the programming language (e.g., C++)
and architectural designs optimized to limited runtime resources,
making manual oracle construction even more challenging. There-
fore, automated test oracle generation is essential to fully leverage
the benefits of automated test case generation in the embedded
software domain.
Prior studies, such as Atlas [25], Tufano et al. [24], and TOGLL
[8] adopt AI-driven methods to automatically generate test oracles
for Java programs. These methods extract Test-Assert Pairs (TAPs)
from publicly available open-source projects as training data. As
shown in Figure 1, each TAP consists of a test prefix, a focal method
(i.e., the method under test), and a corresponding test oracle. The
extracted TAPs are then used to fine-tune a pre-trained model to
enhance its test oracle generation capability. Nevertheless, these
methods still face four major challenges in generating high-quality
test oracles, especially for commercial embedded software testing.
• Inconsistent coding styles.Variations in syntax and in-
dividual coding habits result in various test oracle coding
styles in the extracted dataset, hindering effective model
training.
• Focal method mismatches in TAPs.Since test oracles are
designed to verify the behavior triggered by a focal method,
it is crucial to accurately identify the focal method for au-
tomatic TAP extraction. Most existing methods [8, 24, 25]
assume that the focal method is the last method invoked im-
mediately before the test oracle within a test case. However,
this assumption does not always hold in practice, leading to
mismatched TAPs. Such mismatches introduce noise into
the training data and ultimately degrade model accuracy.
• Unreliable oracle outputs.A significant portion of the
generated oracles are incorrect, making them unreliable in
practice. Consequently, developers must manually inspect
and fix these oracles, resulting in substantial verification
costs.
• Lack of attention to C++.Existing methods mainly focus
on test oracle generation for Java, and there is no publicly
available TAP dataset for training and evaluating test oracle
generation models for C++. As one of the most widely used
languages, particularly in embedded software, C++ deserves
greater attention in this research area.
To address these issues, we propose AutoOracle, a novel C++ test
oraclegenerationapproach. AutoOracleconstructsahigher-quality
TAP dataset and leverages LLM-based self-inspection to generate
more accurate test oracles. Our evaluation on open-source C++
projects shows that, compared with the state-of-the-art (SOTA)
method TOGLL [8], AutoOracle improves oracle accuracy by 2.13
times and reduces the error rate of test oracles delivered to develop-
ers by 52.3%. In an industrial setting, AutoOracle also significantly
improves both compile and runtime success rates in a Samsung SSD
firmware project. Furthermore, a user study with 19 participants
indicates that the oracles generated by AutoOracle are perceived as
moreusefulreferencesforwritingassertions. Thekeycontributions
of this work are as follows:
• We propose anOracle De-Differentiation Methodthat
transforms diverse test oracle expressions into a unified rep-
resentation based on logical equivalence. By normalizing
logically equivalent oracles, this method eliminates stylistic
variations and reduces niche syntactic forms, making test
oracles more consistent and easier for LLMs to learn and
interpret.
• We develop aTAP Quality Scoring and Filtering Mecha-
nism to construct a high-quality TAP dataset. Specifically,
we evaluate the correlation of each test oracle and its can-
didate focal methods across multiple dimensions, select the
most strongly correlated focal method, and filter out samples
that still exhibit low correlation. This mechanism reduces
mismatched TAPs and provides a reliable data foundation
for model training.
• To reduce the manual effort required to verify incorrect ora-
cles, we propose an automaticSuspicious Oracle Filtering
Framework based on LLM self-inspection. It identifies po-
tentially incorrect oracles and filters them out before they
are presented to developers, thereby significantly reducing
verification cost.
• To facilitate future research in C++ test oracle generation,
we collect and publicly release the first large-scale C++ TAP
dataset for training and evaluating test oracle generation
models, consisting of 79,496 samples from 666 open-source
projects. Itisavailableathttps://github.com/samsungDS/Au-
toOracleDataset.

## 2 Related Work and Motivation

Recent advances in large language models (LLMs) have shown
strong capabilities in automated test oracle generation [11, 16].
Most existing approaches [8, 24, 25] follow a two-step scheme:
(1) extract TAPs from open-source projects; and (2) fine-tune a
pre-trained LLM to generate test oracles from test contexts. Atlas
[25] trained a recurrent neural network (RNN) [7] encoder-decoder
model from scratch based on the Java TAP dataset they collected.
Tufanoetal. [ 24]introducedthemoreadvancedBARTTransformer
model to replace RNN-based model. With the breakthrough of LLM
in code generation, TOGLL [8] significantly improved the test or-
acle generation accuracy by fine-tuning the pre-trained LLM. In
contrast, ChatAssert [6] takes a different approach by leveraging
prompt engineering [15] with a general-purpose LLM, without re-
quiring fine-tuning for test oracle generation. Note that all these
methods focus on generating test oracles for Java. In this study, we
focus on how to construct a high-quality C++ TAP dataset for LLM
fine-tuning and how to provide more reliable test oracles to devel-
opers. In industrial settings, such as ours, security and compliance
constraints make it difficult to rely on proprietary closed-source
LLMs. Therefore,open-sourceLLMsareoftentheonlyviableoption,
which naturally enables and encourages fine-tuning for domain
adaptation.
2.1 Challenges in TAPs Extraction
A TAP typically consists of a test context and a corresponding test
oracle, where the test context includes the test prefix and the focal
method under test [24, 25]. The test prefix handles test behaviors,
such as parameter initialization and method invocation, to produce
the result that will be verified by the test oracle. Figure 1 shows an
237

<!-- Page 3 -->

AutoOracle: High-Quality C++ Test Oracle Generation via Data Quality-Driven and Filtering-Enabled LLMs ICSE-SEIP ’26, April 12–18, 2026, Rio de Janeiro, Brazil
example of a TAP. The focal methodfactorial() computes the facto-
rial of a given integer n. The test casetestFactorial() validates this
behavior using the test oracleassertEquals(1, ret), which compares
the actual result ret with the expected value 1. In this scenario,
existing approaches construct a TAP by combining the test context,
consisting of the definitions oftestFactorial() and factorial(), with
the corresponding test oracleassertEquals(1, ret). However, existing
TAP extraction approaches suffer from several limitations.
Figure 1: A Java TAP sample
Limitation 1: various test oracle coding styles in TAP
dataset. Test oracles written by different developers exhibit syn-
tactic variations, which makes it difficult for LLMs to learn their un-
derlyinggrammars and logic. In particular, niche syntactic patterns,
which appear infrequently in the dataset, pose greater challenges
to the model due to insufficient samples for the model to learn from.
Many of these niche patterns are semantically equivalent to more
common expressions. As illustrated in Figure 2, the oracles on the
left use different patterns to verify the same condition (i.e., whether
A equals B), while the right examples use the same oracle type
but differ in how the input is expressed, either via an intermediate
variable or a direct method call. Although these stylistic differ-
ences do not affect program semantics, they introduce unnecessary
variability that complicates the model’s learning process.
Figure 2: Various test oracle coding styles in public projects
Idea 1: code de-differentiation in TAP extraction.Based
on our analysis, many code structures look distinct syntactically
but are semantically equivalent. Therefore, we suggest applying
code transformation based on logical equivalence during the TAP
sample extraction process. Through code de-differentiation, the
syntactic patterns of test oracles are normalized, reducing niche
grammars and thus making it easier for the model to learn.
Limitation 2: mismatched focal methods in TAP dataset.
Existing methods [8, 24, 25] identify the focal method using sim-
ple heuristics, most commonly selecting the last method invoked
before the test oracle, which can be incorrect. As a result, some
extracted TAPs of previous work pair a test oracle with the wrong
focal method, introducing noise that can degrade LLM fine-tuning.
For example, Figure 3 shows a C++ test case intended to verify
vector::push_back(). The test checks the vector size after the opera-
tion by callingsize(), storing it in an intermediate variablelen, and
asserting on len. Becausesize() appears closer to the oracle than
push_back(), the most common heuristics would selectsize() as the
focal method, erroneously.
Figure 3: Mismatched focal method
Idea 2: focal method identification quality scoring and
score-based TAP filtering. To improve the accuracy of focal
method identification, we suggest combining multiple factors, such
asthetestcasename,filename,anddataflowtoestimatethedegree
of matching between a test case and its candidate focal methods.
Furthermore, for test cases where the matching score is still low,
we remove them from the training set to reduce the impact of these
possible noise samples on LLM fine-tuning.
2.2 Challenges in LLM Fine-tuning and
Inference
OnceaTAPdatasetisextracted,manystudies[ 3,8,11,24]fine-tune
pre-trainedmodelswithcodeunderstandingcapabilitiestoimprove
test oracle generation performance. In this setting, the test context
(i.e., test prefix and focal method) is provided as input to the model,
and the corresponding test oracle is used as the target output. The
fine-tuned model is then applied to generate test oracles for unseen
test contexts during inference.
Limitation 3: unreliable oracles generated by LLMs.Ex-
isting approaches use fine-tuned LLM to infer test oracles, but a
substantial portion of the generated oracles are incorrect. Conse-
quently, developers must manually inspect and validate each oracle
before use, which introduces significant verification overhead. This
manual effort limits the practical adoption of automated test oracle
generation in real-world software development.
Idea 3: Automatic suspicious oracles filtering.To reduce
the manual verification burden on developers, we leverage the self-
inspection capability of LLMs. We design dedicated prompts during
fine-tuning to enhance the model’s ability to assess its own out-
puts. During inference, the model estimates the confidence of each
generated test oracle and filters out those deemed suspicious. By
withholding low-confidence oracles from developers, this approach
reduces manual verification effort.
238

<!-- Page 4 -->

ICSE-SEIP ’26, April 12–18, 2026, Rio de Janeiro, Brazil Cong Li et al.
Figure 4: Architecture of AutoOracle

## 3 Design

The overall architecture of the proposed AutoOracle is shown in
Figure 4. Based on our motivations and ideas outlined in Section 2,
we develop the following three modules to address the limitations
of existing schemes. (1)Oracle De-Differentiation Method.To
eliminate syntactic variations in test oracles, we normalize seman-
tically equivalent oracles into a standardized format. This ensures
semantic consistency and minimizes variations across TAPs in the
dataset, improving the accuracy and robustness of test oracle gen-
eration. (2) TAP Quality Scoring and Filtering Mechanism.
This method extracts TAPs based on the multi-view correlation
between test oracles and their candidate focal methods, and elim-
inates TAPs that fail to identify a highly correlated focal method
from the training set, thereby yielding a high-quality dataset for
model fine-tuning. (3)Suspicious Oracle Filtering Framework.
We design a novel framework that automatically filters out test
oracles suspected to be incorrect by enhancing the self-inspection
capability of LLMs. Specifically, we first activate and enhance the
LLM’s self-inspection ability during the fine-tuning phase with
explicitly designed samples. During inference, we let LLM verify
the correctness of the generated test oracle. The final correctness
of a test oracle is estimated based on both the LLM’s confidence
in generating the test oracle and its confidence that the oracle is
correct.
3.1 Oracle De-Differentiation Method
To address syntactic diversity in test oracles, we propose the Or-
acle De-Differentiation (ODD) method to transform semantically
equivalent but syntactically distinct test oracles into a unified form.
It mainly involves three stages: triple extraction, logical simplifica-
tion, and oracle normalization, as described in Algorithm 1
In Algorithm1, the ExtractTriples function is used to extract
triples. Ittakes a rawtest oracle stringas input andreturnsa logical
triple (S, L, P), where S denotes the equivalent logical operator of
assertion macro (e.g., EXPECT_TRUE), L represents the logical
operator (e.g., “==” in(!A == TRUE)), and P is a list of parameters
(e.g., “A” and “B” in(A, B)) or logical operands (e.g., “!A” and “TRUE”
in (!A == TRUE)). The process proceeds as follows: First, tree-
sitter [22] is used to parse the test oracle, extracting the macros
and their associated parameter lists. Second, a mapping table (see
Table 1) is employed to translate the extracted macro strings into
their corresponding logical operators. Next, if only one parameter
contains logical operators, a regular expression is applied to split
it into logical operands and logical operator; in other cases, the
argument list is extracted. This design ensures that the resulting
triple(S,L,P)containsonlylogicaloperandsandoperators, offering
a clear and consistent input for subsequent logical processing. For
example, given the input test oracleEXPECT_TRUE(!A == TRUE),
the extracted triple is(TRUE, ==, [!A, TRUE]).
To simplify the extracted logical triple (S, L, P), we introduce
the SimplifyLogic function. It outputs a simplified (L, P), where L
represents the reduced logical operator and P is the list of logical
operands. The function first merges the logic of S and L using
logical operations to generate an equivalent logical expression.
It then further simplifies L and the potentially embedded logical
operators within the operands in P. For instance,(TRUE, ==, [!A,
TRUE]) is first simplified to(==, [!A, TRUE]) by merging S and L,
and then to(TRUE, [!A]) by merging logic operators in L and P.
Finally, unnecessary negations in P are removed via a negation
operation (as defined in the operator negation column of Table 1),
transforming (TRUE, [!A])into (FALSE, [A]).Thislogicsimplification
process guarantees that the final logic is semantically equivalent to
the original expression, but with a more concise form.
Table 1: The mapping of macro to Logical Operator and oper-
ator negation
Macro Operator Operator
negation
EXPECT_EQ == !=
EXPECT_NE ! = ==
EXPECT_LT < > =
EXPECT_LE < = >
EXPECT_GT > < =
EXPECT_GE > = <
EXPECT_TRUE TRUE FALSE
EXPECT_FALSE FALSE TRUE
239

<!-- Page 5 -->

AutoOracle: High-Quality C++ Test Oracle Generation via Data Quality-Driven and Filtering-Enabled LLMs ICSE-SEIP ’26, April 12–18, 2026, Rio de Janeiro, Brazil
Furthermore, we design theNormalizeOracle function to convert
the simplified (L, P) into a normalized test oracle. This function first
utilizes the mapping table (Table 1) to map the logical operators
back to their corresponding assertion macros. For example,EX-
PECT_TRUE(!A == TRUE) is simplified to(FALSE, [A]) in Simplify-
Logic, and then converted toEXPECT_FALSE(A)in NormalizeOracle.
If P is not an expression (e.g., function call and arithmetic opera-
tions), the conversion ends; otherwise, the complex expressions in
the operands are assigned to temporary variables. For example, if
A is a function callfunc(a), thenEXPECT_FALSE(func(a)) will be
converted to “auto temp = func(a); EXPECT_FALSE(temp)”.
In summary, the ODD method transforms the test oracles into
a unified and normalized form through three stages: triple extrac-
tion, logical simplification, and oracle normalization. This method
addresses the syntactic diversity issue and provides a structured
and standardized format, which is easier for the model to interpret.
3.2 TAP Quality Scoring and Filtering
Mechanism
Automatically identifying the focal method associated with a given
test oracle is a critical yet challenging task when multiple candidate
methods exist in test code. To address this issue, we propose a TAP
Quality Scoring and Filtering (TQSF) mechanism.
3.2.1 Scoring Mechanism for TAP Quality. We observe that test
intent can often be inferred from the naming conventions of cor-
responding test cases. In the widely used GoogleTest framework
[29], test functions (e.g.,TEST() and TEST_F()) follow a naming
convention where the names specified in the macro parameters
reflect the test intent. For instance, a test name,test_push_back,
typically corresponds to a focal method namedpush_back. In ad-
dition, test files and source files typically follow a mirrored path
structure [19, 21, 26], where the directory hierarchy of test code
closely aligns with that of the source code. For example, a source
file may be located atproject/src/math/add.cpp, while the test file is
located atproject/test/math/add_test.cpp, with a “_test” suffix. These
naming conventions convey the structure of a project and help
to map test oracles to their focal methods. Yet, such conventions
are not mandatory, and there are a lot of non-standard names in
practice. Accordingly, for the test names, file names, and file paths
corresponding to the test case and candidate focal methods, we
adopt the Longest Common Subsequence (LCS) algorithm [10] to
perform fuzzy matching on them. The equation is as follows.
𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦 = 𝐿𝐶𝑆 𝐿𝑒𝑛𝑔𝑡ℎ (𝑡𝑒𝑠𝑡, 𝑓 𝑜𝑐𝑎𝑙 )
𝑚𝑎𝑥 (𝐿𝑒𝑛𝑔𝑡ℎ (𝑡𝑒𝑠𝑡 ) , 𝐿𝑒𝑛𝑔𝑡ℎ (𝑓 𝑜𝑐𝑎𝑙)) (1)
In addition to test intent, code structure features also play a
crucial role in identifying the correct focal method and they are de-
rived from the syntactic characteristics of the test code. First, data
flow dependencies between the test oracle and the focal method
indicate their logical connection. In practice, test oracles are com-
monly constructed based on the post-conditions of an execution
(e.g., outputs, internal states, etc.) of the focal method. Second,
while previous approaches consider that the method closest to the
test oracle is the focal method, we also observe that the test oracle
is usually close to the focal method, although not always the closest.
Basedontheseobservations, weextracttwocodestructurefeatures,
Algorithm 1Oracle De-Differentiation (ODD)
Input: Test oracle string (e.g., EXPECT_TRUE(A==B))
Output: Normalized test oracle string (e.g., EXPECT_EQ(A, B))
Step 1:(S, L, P)← ExtractTriples(input_oracle)
Step 2:(L, P)← SimplifyLogic(S, L, P)
Step 3:normalized_oracle ← NormalizeOracle(L, P)
Procedure ExtractTriples(input_oracle):
ast ← TreeSitter.parse(input_oracle)
macro_node ← ast.get_child(“identifier”)
args_node ← ast.get_child(“argument_list”)
macro_op ← LogicalMapping.get(macro_node.text)
if len(args_node.children) == 1 then child ← args_node.child
if child.type is “binary_expression”then
e, l, r← child.text, child.left.text, child.right.text
operator ← extractOperator(e, l, r)
if operator ∈ LogicalOperator then
return (macro_op, operator, [l, r])
return (macro_op, None, [child.text])
if len(args_node.children) == 2 then
l, r← child.left.text, child.right.text
return (macro_op, None, [l, r])
Procedure SimplifyLogic(S, L, P):
/* S1: Combine the logic of S and L */#
if L is Nonethen L ← S
else
if S is “TRUE”then L ← L
if S is “FALSE”then L ← OperatorNegationMapping(L)
/* S2: Combine the logic of L and P */
if len(P) == 1 then return (L, P)
if len(P) == 2 then
if “TRUE” in Pthen P.remove(“TRUE”)
if L is “==” then L ← “TRUE”
if L is “!=” then L ← “FALSE”
if “FALSE” in Pthen P.remove(“FALSE”)
if L is “==” then L ← “FALSE”
if L is “!=” then L ← “TRUE”
/* S3: remove negations */
if len(P) == 1 and “!” in Pthen
L ← OperatorNegationMapping(L)
P ← !P
return (L, P)
Procedure NormalizeOracle(L, P):
macro ← LogicalOperatorToMacroMapping.get(L)
params ← []
temp_declarations ← []
for param in Pdo
ast ← TreeSitter.parse(param)
if “expression” in ast.typethen
temp_var ← “temp_” + str(temp_count)
temp_declarations.append(“auto ” + temp_var + “= ”
+ param + “;”)
params.append(temp_var)
else
params.append(param)
oracle ← macro + “(” + “, ”.join(params) + “)”
return “\n”.join(temp_declarations) + “\n” +oracle
240

<!-- Page 6 -->

ICSE-SEIP ’26, April 12–18, 2026, Rio de Janeiro, Brazil Cong Li et al.
data flow proximity and line proximity. For data flow proximity,
we re-represent the data flow relationships by tracking variables
with tree-sitter [22] and then quantify the dependency strength by
measuring the lengths of the paths between variables. As defined
in Equation (2), it captures the intensity of these dependencies.
𝐷𝑎𝑡𝑎 𝑓 𝑙𝑜𝑤 𝑝𝑟𝑜𝑥𝑖𝑚𝑖𝑡𝑦 = 1
𝑃 𝑎𝑡ℎ 𝐿𝑒𝑛𝑔𝑡ℎ + 1 (2)
Path length is the number of variables or statements involved in
the shortest data flow path from a candidate method to an oracle.
Higher data flow proximity means the connection between the
candidate focal method and the test oracle is closer.
For line proximity, we consider the line distance in the code be-
tween a test oracle and the invocation of a candidate focal method.
Since the number of lines of code may be large, we apply a loga-
rithmic normalization on the line distance and then calculate the
line proximity by Equation (3).
𝐿𝑖𝑛𝑒 𝑝𝑟𝑜𝑥𝑖𝑚𝑖𝑡𝑦 = 1 − 𝑙𝑛 (𝐿𝑖𝑛𝑒 𝐷𝑖𝑠𝑡𝑎𝑛𝑐𝑒 + 1 )
𝑙𝑛 (𝑇 𝑜𝑡𝑎𝑙 𝐿𝑖𝑛𝑒 𝐷𝑖𝑠𝑡𝑎𝑛𝑐𝑒 + 1 ) (3)
Total line distancedenotesthetotalnumberoflinesinthecurrent
testcase, and line distance representsthenumberoflinesseparating
the test oracle and the candidate method invocation.
Based on the five features defined above, three from test intent
and two from code structure (i.e., name similarity, file name simi-
larity, file path similarity, data flow proximity, and line proximity),
we calculate the average value of these five features as the quality
score. This scoring mechanism provides a fair and comprehensive
evaluation of the match between a test oracle and a candidate fo-
cal method with the highest quality score as final focal method to
construct the TAP.
3.2.2 Filtering Mechanism for Low-Quality TAP Samples. Although
we combine multiple factors to identify focal method, some mis-
matched cases still remain in automatic TAP extraction, and these
cases typically fail to yield a focal method with a high-quality score.
Therefore, based on the quality scores of each TAP, we introduce a
filtering strategy to remove samples with low quality scores. Specif-
ically, through statistical analysis of the quality scores, we set a
threshold r to remove the bottomr% of samples from the training
set (r defaults to 35 in this study). The threshold is chosen to strike
a balance between discarding low-quality samples and retaining a
sufficiently large training set, ultimately improving the reliability
of the training data.
In summary, the TQSF mechanism provides a multi-perspective
approach to identifying focal methods and removing low-quality
TAP samples based on quality scores. It establishes a reliable and
high-quality data foundation for LLM fine-tuning.
3.3 Suspicious Oracle Filtering Framework
Suspicious Oracle Filtering (SOF) framework is designed to auto-
matically filter out suspicious test oracles generated by LLMs. It
enhances the self-inspection ability of LLMs that have test oracle
generation capability, enabling them to automatically detect and
discard potentially incorrect test oracles. As a result, in practice,
SOF improves the reliability and usability of AutoOracle’s outputs
and reduces the burden of manual verification.
Figure 5: Prompt generation and fine-tuning in SOF
In the fine-tuning stage, we design SOF prompts (as shown in
Figure5)andincorporateSOFsampletoenhancethemodel’sability
of detecting incorrect test oracles. In particular, we first fine-tune
the LLM on the original training samples, and then use the fine-
tuned model to generate test oracles on a held-out TAP set. By
comparing the generated oracles with the ground-truth oracles,
we derive SOF samples. Each SOF sample consists of test context,
the generated test oracle, and a SOF question for assessing its
correctness as input. The corresponding label is either “yes” or “no”,
depending on whether the generated oracle matches the ground-
truth oracle. The LLM is then fine-tuned with these SOF samples
to better distinguish correct oracles.
During inference, for a generated test oracle, we first prompt the
LLMwiththeSOFquestion(i.e., “Isthisanswercorrect?”) totrigger
its self-inspection. We then estimate the correctness of a gener-
ated oracle using two confidence measures: the LLM’s confidence
during oracle generation (generation confidence,CONF_GEN) and
its confidence in the oracle’s correctness (inspection confidence,
CONF_INS). When generating each token, LLMs typically produce
aprobabilitydistributionovereachwordinthevocabulary, wherea
higher probability indicates that the LLM considers the word more
likely to be correct. We extract the probabilities of all tokens in
the generated test oracle and compute their average asCONF_GEN.
Next, we collect the probability of the LLM answering “yes” to the
SOF question asCONF_INS. Given that we include SOF samples
during fine-tuning, the sum of the probabilities for “yes” and “no”
responses to SOF question is approximately 1. Therefore, the “yes”
probability can serve as a reliable indicator of the LLM’s judgment
on the oracle’s correctness. Instead of relying on the binary de-
cision, we use the probability of the “yes” token to quantify the
model’s confidence in its self-inspection result.
Finally, we calculate the average ofCONF_GEN and CONF_INS
to obtain an overall confidence score,CONF_OA, which is used
to estimate the correctness of the generated test oracle. Based on
CONF_OA, we set a thresholdp to filter out low-confidence test
oracles. Oracles with aCONF_OA below p are not presented to
developers in practice to reduce the burden of manual review. In
this study,p is set to 0.15 by default, and the impact of different
settings is discussed in Section 4.4.
241

<!-- Page 7 -->

AutoOracle: High-Quality C++ Test Oracle Generation via Data Quality-Driven and Filtering-Enabled LLMs ICSE-SEIP ’26, April 12–18, 2026, Rio de Janeiro, Brazil

## 4 Evaluation

This section evaluates the effectiveness of AutoOracle in automati-
cally generating test oracles for C++ code. The research questions
(RQs) are as follows:
RQ1: Does AutoOracle outperform SOTA techniques in gener-
ating accurate C++ test oracles?
RQ2: Do the ODD and TQSF provide a high-quality data foun-
dation in fine-tuning phase?
RQ3: Does the SOF framework improve the quality of generated
test oracles in the inference phase?
RQ4: Does AutoOracle perform effectively in real-world unit
testing scenario, particularly in Samsung SSD firmware projects?
4.1 Evaluation Setup
4.1.1 TAP Dataset Configuration. C++ is a widely used high-level
programming language for system-level and embedded software
development,yetresearchontestoraclegenerationforC++remains
limited. To bridge this gap, based on the ODD and TQSF methods
described in Section 3, we construct the first C++ TAP dataset
for model fine-tuning and evaluation. The dataset contains 79,496
TAPs, collected from 666 open-source C++ projects on GitHub that
with GoogleTest [29] test cases and have more than 45 stars. It is
split into 90% for model fine-tuning and 10% for testing.
4.1.2 Evaluation metrics. We adopt the following evaluation met-
rics, as commonly used in prior work [6, 8, 18, 23–25]. In terms of
test oracle quality, we use ACC to measure the exact match accu-
racy between the generated oracles and the ground-truth oracles,
Error Rate to indicate the proportion of mismatched oracles, and
CodeBLEU [20] to evaluate their semantic and structural similarity.
We also evaluated the effectiveness of AutoOracle in practice on
a Samsung SSD firmware project, and the evaluation metrics are
introduced separately in Section 4.5.
4.1.3 Baseline model. We compare AutoOracle with TOGLL [8],
a SOTA approach based on LLM fine-tuning, and ChatAssert [6],
which relies on prompt engineering. Both approaches are adapted
to C++. TOGLL provides multiple test context extraction strategies,
and we adopt the best-performing one (Prompt 5) as reported in
the original paper. In this strategy, the test context consists of a
test prefix and a focal method, which is consistent with the test
context structure of AutoOracle. ChatAssert incorporates a prompt
engineering-based test oracle correction mechanism that leverages
both compilation and runtime results. In our adaptation, we im-
plement the compilation-based correction using Clang [12, 14], but
omit the runtime-based correction. Although runtime-based cor-
rection can improve accuracy, it may also discard oracles that could
detect defects due to runtime failures, which is unacceptable in
practical testing.
All three methods use the open-source Qwen3-32B model [1, 27]
with strong code generation capability as the base model to ensure
a fair comparison. AutoOracle and TOGLL use the Qwen3-32B
model as their pre-trained model and apply LoRA [9] technique
for parameter-efficient fine-tuning. The fine-tuned model is finally
used to generate test oracles. In contrast, ChatAssert directly uses
the original Qwen3-32B model and combines prompt engineering
to generate test oracles.
4.1.4 Experimental environment. We conducted the experiments
on a server with an Intel Xeon Platinum 8380 CPU, 314 GB DDR4
RAM, and an NVIDIA A100 GPU.
4.2 RQ 1: Does AutoOracle outperform SOTA
techniques in generating accurate C++ test
oracles?
We compare AutoOracle with TOGLL and ChatAssert on the col-
lected C++ TAP. As shown in Table 2, AutoOracle significantly
outperforms existing methods across all oracle quality metrics. It
achieves an ACC of 64.5%, which is 2.13 times higher than TOGLL
(30.3%) and 2.37 times higher than ChatAssert (27.2%). The error
rate is reduced from 69.7% and 72.8% to 20.5%, substantially lower-
ing the generation of invalid or incorrect oracles and reducing the
manual correction effort required. Moreover, AutoOracle attains
a CodeBLEU score of 0.55, compared to 0.44 for TOGLL and 0.40
for ChatAssert, suggesting that AutoOracle generates oracles that
more closely resemble manually written ones in both structure and
semantics. These improvements can be attributed to our use of
the ODD and TQSF strategies during training, as well as the SOF
framework during inference, which are discussed in detail in the
following sections.
4.3 RQ 2: Do the ODD and TQSF provide a
high-quality data foundation in fine-tuning
phase?
To evaluate whether the ODD and TQSF strategies improve the
quality of the dataset for test oracle generation, we conducted an
ablation study. We compared TOGLL, AutoOracle-ODD (TOGLL
augmented with the ODD module), and AutoOracle-TQSF (TOGLL
augmented with both the ODD and TQSF modules). As shown in
Table 3, compared to the baseline, AutoOracle-ODD improves ACC
from30.3%to45.8%. Codede-differentiationprovidesamoreunified
testoracleformat,makingiteasierforthemodeltolearn. Byfurther
incorporating multiple factors for focal method identification and
applying low-quality TAP filtering, AutoOracle-TQSF achieves an
ACC of 65.2%, an error rate of 34.8%, and a CodeBLEU score of
0.50. These results demonstrate that the ODD and TQSF strategies
significantly improve the consistency and overall quality of the
dataset, thereby enhancing the effectiveness of LLM fine-tuning for
test oracle generation.
4.4 RQ 3: Does the SOF framework improve the
quality of the generated test oracles in the
inference phase?
In this section, we evaluate the effectiveness of the SOF module.
The core idea of SOF is to apply a thresholdp to the confidence
score to filter out low-quality test oracles while minimizing the
impact on correct ones, thereby improving the reliability and us-
ability of the final output. Figure 6 presents the impact of SOF
under different values of p. We report three metrics: (1) Delivered
Oracles, the number of oracles that pass the SOF filtering among
total 7,133 generated oracles; (2) Accuracy (ACC), the proportion of
correct oracles among the delivered ones relative to the total 7,133
242

<!-- Page 8 -->

ICSE-SEIP ’26, April 12–18, 2026, Rio de Janeiro, Brazil Cong Li et al.
Table 2: Performance Comparison of AutoOracle against ChatAssert and TOGLL
Model ACC Error Rate CodeBLEU
ChatAssert [1] 27.2% 72.8% 0.4
TOGLL [2] 30.3% 69.7% 0.44
AutoOracle 64.5% 20.5% 0.55
Table 3: Ablation Study of AutoOracle Modules
Model ACC Error Rate Code BLEU
TOGLL [2] 30.3% 69.7% 0.44
AutoOracle-ODD 45.8% 54.2% 0.46
AutoOracle-TQSF 65.2% 34.8% 0.50
Figure 6: Evaluation of SOF across different p values
oracles; (3) Error Rate, the proportion of incorrect oracles among
the delivered ones relative to the same total.
As p increases, the error rate consistently decreases, reflecting a
lower verification cost for developers handling incorrect oracles.
However, the marginal reduction in error rate diminishes asp
grows, while both accuracy and the number of delivered oracles
decrease, suggesting that some correct oracles are also filtered out.
Therefore, the choice ofp is a balance between reducing incorrect
oracles through stricter filtering and preserving correct oracles by
keeping more ou6tputs. In this work,p is set to 0.15 by default. As
shown in Figure 6, compared with AutoOracle-TQSF without SOF
(p=0), setting p=0.15 reduces the error rate from 34.8% to 20.5%,
meaning that 41.1% of incorrect oracles are successfully removed.
Meanwhile, accuracy decreases only slightly from 65.2% to 64.5%,
indicating that most correct oracles are preserved.
Overall, these results demonstrate that SOF effectively filters out
suspicious oracles during inference, greatly improving the reliabil-
ity and practical usability of the generated test oracles. Therefore,
developers can focus on higher-quality oracles, reducing effort
required for manual inspection and debugging.
4.5 RQ 4: Does AutoOracle perform effectively
in real-world unit testing scenario,
particularly in Samsung SSD firmware
projects?
To evaluate AutoOracle’s utility in real-world commercial software
development, we conducted a case study on unit testing in an
SSD firmware project P. Project P actively promotes unit testing
automation and recently piloted an in-house concolic testing tool
that generates test harnesses and inputs but not oracles. Given its
scale, we focused on module F, the first to adopt automated testing.
We applied the tool to all C++ source files in the module to generate
test prefixes without oracles, and the TAP extraction tool extracted
3,265 valid test contexts, forming the SSD TAP dataset.
In open-source TAP datasets, most assertions compare return
values to concrete expected outputs. However, many focal methods
in SSD firmware are void-type due to their stateful nature, where
behavior is often expressed through NAND states and contextual
metadata rather than explicit return values. For such methods,
correctness is validated by checking whether the program’s inter-
nal state transitions to the intended state after execution, which
requires assertions over implicit post-conditions. Since this differs
fromthetaskAutoOraclewasprimarilytrainedon, weprovideeval-
uation results on the full SSD TAP dataset (3,265 test contexts) and
a subset of the dataset (1,205 test contexts) that excludes void-type
focal methods.
In this case study, we limit our comparison to AutoOracle and
TOGLL, excluding ChatAssert for two reasons. First, as discussed
in Section 4.2, ChatAssert demonstrated lower performance than
TOGLL in our evaluation on open-source TAP dataset. Secondly,
ChatAssert exhibited significantly higher latency per oracle gener-
ation due to its compilation- and runtime-based oracle correction
mechanism, while our intended unit testing scenario requires near
real-time turnaround per pull request, making it impractical for
production use.
Similar to prior work [17], Table 4 reports immediate practicality
using two metrics: %Compile (the proportion of oracles that com-
pile successfully when attached to the target test prefix) and %Run
(the proportion of oracles that compile and execute to completion
without exceptions). As shown in Table 4, Autooracle consistently
outperforms TOGLL in both compilation and runtime success. On
the full SSD TAP dataset, AutoOracle achieves 47.3% %Compile and
47.1% %Run, compared to TOGLL’s 33.1% and 33.0%. The perfor-
mance gap becomes even larger for the 1,205 test contexts with
non-voidfocalmethods,whereAutoOraclereaches82.0%%Compile
and 81.8% %Run, while TOGLL achieves 67.4% and 66.9%, respec-
tively.
243

<!-- Page 9 -->

AutoOracle: High-Quality C++ Test Oracle Generation via Data Quality-Driven and Filtering-Enabled LLMs ICSE-SEIP ’26, April 12–18, 2026, Rio de Janeiro, Brazil
Table 4: Compile and Run Rates of the Generated Oracles
Focal Method Model %Compile %Run
All TOGLL 33.1% 33.0%
AutoOracle 47.3% 47.1%
Non-Void TOGLL 67.4% 66.9%
AutoOracle 82.0% 81.8%
We also conducted a questionnaire-based survey of develop-
ers and test engineers in project P to qualitatively evaluate the
perceived quality and usefulness of the generated oracles. Since
project P currently contains only a limited number of developer-
written unit tests with complete assertions, collecting sufficient
ground-truth oracles for a large-scale accuracy evaluation, akin to
our open-source experiments, was not feasible at this stage. There-
fore, we relied on a developer survey as a practical alternative until
a larger set of developer-written ground-truth oracles becomes
available. The survey compared AutoOracle and TOGLL under
two usage scenarios: (1) in fully automated unit testing, where
reviewers were asked to decide whether to approve or decline a
pull request with the oracle added to an assertion-less test prefix;
and (2) in a unit testing assistant tool, where declined oracles were
evaluated for their usefulness as reference suggestions when devel-
opers manually wrote their own assertions. All test prefixes used
here were produced by the in-house concolic testing tool.
To construct the survey items, we selected six classes in mod-
ule F that had newly added or modified developer-written unit
tests merged during the week prior to survey design. This selec-
tion was independent of any oracle generation technique and was
solely based on recent developer activity, which indicates stabilized
functionality and reliable implementation of the target code un-
der test. With this criterion, we could minimize ambiguity about
code intent and reduce unnecessary cognitive load for survey par-
ticipants, thereby enabling a more accurate assessment of oracle
quality. We then applied the concolic testing tool to all methods
in the selected classes, yielding 156 test prefixes, of which TAP
extraction succeeded for 66. Among them, AutoOracle and TOGLL
generated distinct oracles for 49 test prefixes. The remaining 17
cases, where the two techniques produced identical oracles, were
excluded, as they were unsuitable for a comparative survey. When
we executed these 49 test prefixes without attaching any oracle,
only 17 reached the oracle location without raising any exceptions.
We then attached both techniques’ oracles to these 17 test prefixes
and observed that 12 compiled and ran successfully in both cases.
These 12 test cases including the oracles formed the initial candi-
date set for the qualitative study. Restricting the set to test cases
that compile and run without exceptions mimics a practical use
case and provides minimal quality control prior to exposing them
to developers.
We manually analyzed 24 generated oracles (12 per technique).
AutoOracle produced three correct and nine incorrect oracles;
TOGLL produced four correct and eight incorrect. Both approaches
primarily used macros such as EXPECT_EQ, where correctness
depends on selecting an appropriate target variable and predicting
a correct expected value. All nine incorrect AutoOracle assertions
involved incorrect expected values. Of the eight incorrect TOGLL
assertions, three had incorrect expected values and five used wrong
target variables. Including all 12 test contexts and 24 oracles in the
questionnaire would have resulted in an overly long survey and
risked low response rates [4]. We therefore excluded five trivial
test contexts where oracle correctness was obvious even without
understanding the code intent. For these cases, AutoOracle yielded
twocorrectandthreeincorrectoracles,allduetoincorrectexpected
values, while TOGLL also yielded two correct and three incorrect
oracles, with two incorrect expected values and one wrong tar-
get variable. We also excluded two highly complex test contexts
whose focal methods have cyclomatic complexities of 19 and 20,
respectively, to avoid excessive cognitive load that could lead to
participant attrition during the survey. In these cases, AutoOra-
cle produced incorrect oracles for both due to incorrect expected
values, whereas TOGLL produced one correct and one incorrect
oracle, with the latter failing due to a wrong target variable. After
these exclusions, five test contexts and ten oracles remained for
the questionnaire. Notably, all selection and filtering criteria up
to this point were applied uniformly to both techniques, thereby
avoiding any systematic bias toward either approach. To ensure
transparency, we detail each filtering step, including the applied
criteria and the numbers of removed test cases and oracles (both
correct and incorrect) for each technique.
The focal methods of the five selected test contexts exhibit dis-
tinct characteristics that affect oracle generation. Methods A (un-
signed int) and B (bool) return values that differ across branches,
but since the branch conditions are simple, the difficulty of oracle
generation is low. Method C (enum) also has diverse return values,
but its more complex branch conditions result in medium oracle
generation difficulty. Method D (unsigned long long) produces the
same return value across branches, but computing this value in-
volves multiple steps of complex arithmetic, which we also classify
as medium difficulty. Method E is a void focal method with no
explicit return value, but its execution induces a clear state change,
requiring developers to identify an appropriate state variable as
the assertion target, which makes oracle generation highly difficult.
Table 6 summarizes the return type and oracle generation difficulty
of each focal method, along with the correctness and error types of
incorrect oracles generated by AutoOracle and TOGLL.
The questionnaire begins with an introduction to the research
team, the study’s objective, and a brief description of the target
code. We explicitly clarified that the survey focuses solely on eval-
uating the quality of generated test oracles, rather than the overall
effectiveness of unit test automation, and asked respondents to
concentrate exclusively on oracle quality. Each survey item cor-
responds to one of the five selected test contexts and presents the
test prefix and focal method code, together with the test case’s line
coverage. For each item, two anonymized candidate oracles, one
from each technique, are presented in random order, along with the
observed execution outcome (pass or fail, including error messages
if any) when each oracle is attached to the test prefix. Subsequently,
the first question asked whether the respondent would approve or
decline the pull request that adds the oracle to the test prefix. For
oracles that were declined, a second question assessed the useful-
ness of the oracle as a reference, assuming the respondent would
need to write the assertion themselves, using a five-point Likert
244

<!-- Page 10 -->

ICSE-SEIP ’26, April 12–18, 2026, Rio de Janeiro, Brazil Cong Li et al.
Table 5: Industry Experience of the Respondents
Industry
Experience
Total Developers Test
Engineers
1-5 years 6 2 4
6-10 years 5 3 2
11-15 years 5 1 4
16-20 years 3 1 2
Total 19 7 12
scale [13]: very helpful, helpful, not helpful, distracting, or very
distracting. For oracles rated as distracting or very distracting, a
third question asked respondents to specify the reason. Finally, an
open-ended question invited additional comments or suggestions.
All questionnaires were administered in Korean.
We distributed the survey to all 30 members of project P who are
familiar with module F and are actively involved in unit test devel-
opment and review, including 13 developers and 17 test engineers.
Rather than sampling a larger but less relevant population, we in-
tentionally employed a judgment sampling strategy [4], targeting
the complete set of practitioners with direct domain knowledge of
the study subject. As a result, the selected participants represent
the full pool of relevant experts for module F and unit testing, en-
suring that the feedback reflects informed and practical judgments
on test oracle quality. Over a one-week response window, 19 par-
ticipants responded (63.3% response rate; 7 developers and 12 test
engineers). This response rate exceeds the average response rate
reported for survey studies in computer science field (56.55%) [5],
indicating strong engagement from the target population. Thus,
these 19 responses represent the best attainable outcome in our
setting. Table 5 summarizes the industry experience distribution of
the respondents.
Table6summarizesthesurveyresponses,reportingapprovaland
decline percentages for each technique, as well as the helpfulness
of declined oracles. Helpfulness is measured by the average Likert
score (very distracting being 1 and very helpful being 5) and the
ratio of non-negative responses (i.e., excluding distracting and very
distracting). As shown in Table 6, AutoOracle outperforms TOGLL
in overall approval rate, average helpfulness, and non-negative
response ratio.
When stratified by correctness, the approval rate for correct
oracles was 52.6% (20/38), twice the approval rate for incorrect
oracles (26.3%, 40/152). It shows that improving the accuracy of
Table 6: Survey Results
Focal Methods Metrics AutoOracle TOGLL
Method A
Type: unsigned int
Difficulty: low
Correctness X (value) X (variable)
Approve 31.6% (6/19) 36.8% (7/19)
Decline 68.4% (13/19) 63.2% (12/19)
Avg. Helpfulness 3.69 2.08
Non-negative 92.3% (12/13) 41.7% (5/12)
Method B
Type: bool
Difficulty: low
Correctness X (value) O
Approve 15.8% (3/19) 42.1% (8/19)
Decline 84.2% (16/19) 57.9% (11/19)
Avg. Helpfulness 2.88 2.91
Non-negative 75.0% (12/16) 72.7% (8/11)
Method C
Type: enum
Difficulty: medium
Correctness O X (variable)
Approve 63.2% (12/19) 26.3% (5/19)
Decline 36.8% (7/19) 73.7% (14/19)
Avg. Helpfulness 3.14 3.36
Non-negative 85.7% (6/7) 85.7% (12/14)
Method D
Type: unsigned
long long
Difficulty: medium
Correctness X (value) X (variable)
Approve 26.3% (5/19) 10.5% (2/19)
Decline 73.7% (14/19) 89.5% (17/19)
Avg. Helpfulness 3.21 2.29
Non-negative 85.7% (12/14) 47.1% (8/17)
Method E
Type: void
Difficulty: high
Correctness X (value) X (value)
Approve 26.3% (5/19) 36.8% (7/19)
Decline 73.7% (14/19) 63.2% (12/19)
Avg. Helpfulness 2.86 2.75
Non-negative 57.1% (8/14) 50.0% (6/12)
Overall Approve 32.6% (31/95) 30.5% (29/95)
Decline 67.4% (64/95) 69.5% (66/95)
Avg. Helpfulness 3.14 2.67
Non-negative 78.1% (50/64) 59.1% (39/66)
245

<!-- Page 11 -->

AutoOracle: High-Quality C++ Test Oracle Generation via Data Quality-Driven and Filtering-Enabled LLMs ICSE-SEIP ’26, April 12–18, 2026, Rio de Janeiro, Brazil
oracle generation is essential for practical acceptance, especially
in fully automated unit testing. This provides evidence that the
high accuracy of AutoOracle demonstrated in our open-source
TAP dataset experiments translates into tangible practicality in an
industrial setting.
Among the 8 incorrect oracles, those with wrong target vari-
ables had an average helpfulness score of 2.58 and a non-negative
response ratio of 58.1% (25/43), whereas those with incorrect ex-
pected values scored 3.07 with a ratio of 72.5% (50/69). Developers
generally considered incorrect expected values relatively easy to
fix and not particularly harmful, but wrong target variables often
confused the interpretation of test case behavior and hindered the
assertion writing. Notably, in the 12 candidate test contexts used
for survey construction, all of AutoOracle’s incorrect oracles were
of the incorrect expected value type, while TOGLL exhibited both
error types, including five wrong target variables. Hence, although
AutoOracle produce incorrect oracles under current limitations,
the errors did not fall into the type most detrimental to developer
productivity.
In the final open-ended question, many participants noted that
concolic test generation targeting branch coverage often obscures
the intent of generated test cases, making it difficult to craft appro-
priate assertions. Several also remarked that, at the current stage,
automatically generated oracles may be more useful as references
than as assertions to be merged automatically, and some preferred
not to receive low-confidence oracles at all. These observations
point to one promising research direction and one practical impli-
cation. First, for test cases whose intent is not self-evident from
test case names, variable names, or comments, a pre-processing
step could be introduced to infer the test’s purpose and expected
post-conditions, for example by leveraging an LLM. This inferred
information can then be incorporated into the oracle generation
prompt, enabling the generated oracles to better capture the in-
tended verification goal. Second, our SOF framework, which filters
out low-confidence oracles instead of presenting them to develop-
ers, may be particularly beneficial in industrial practice.

## 5 Conclusion

We propose AutoOracle, the first LLM-driven test oracle generation
approach designed for C++ projects, along with the first publicly
released large-scale C++ TAP dataset. By constructing high-quality
training data and automatically discarding low-confidence outputs,
AutoOracle outperforms previous approaches on both open-source
C++ projects and a Samsung’s commercial SSD firmware project.
The evaluations demonstrate AutoOracle achieves up to 2.13 times
higher oracle accuracy and 52.3% reduction in error rate. Practi-
tioner feedback further confirms that the test oracle generated by
AutoOracle are more useful for embedded software testing in prac-
tice. Consequently, AutoOracle provides a reproducible research
foundation and a deployable solution, promoting both academic
study and industrial productivity in C++ testing.

## References

[1] Alibaba Model Studio. 2025. Qwen3-32B. Retrieved from https://huggingface.co/
Qwen/Qwen3-32B
[2] Ermira Daka and Gordon Fraser. 2014. A Survey on Unit Testing Practices and
Problems. In 2014 IEEE 25th International Symposium on Software Reliability
Engineering, 2014. 201–211. https://doi.org/10.1109/ISSRE.2014.11
[3] Elizabeth Dinella, Gabriel Ryan, Todd Mytkowicz, and Shuvendu K Lahiri. 2022.
Toga: A neural method for test oracle generation. In Proceedings of the 44th
International Conference on Software Engineering, 2022. ACM, 2130–2141. https:
//doi.org/10.1145/3510003.351014
[4] AhmadNaumanGhazi,KaiPetersen,SriSaiVijayRajReddy,andHariniNekkanti.
2019. Survey Research in Software Engineering: Problems and Mitigation Strate-
gies. IEEE Access 7, (2019), 24703–24718. https://doi.org/10.1109/ACCESS.2018.
2881041
[5] Hamed Taherdoost and Mitra Madanchian. 2025. The Impact of Survey Response
Rates on Research Validity and Reliability. In Design and Validation of Research
Tools and Methodologies. 183–212. https://doi.org/10.4018/979-8-3693-1135-6.
ch009
[6] Ishrak Hayet, Adam Scott, and Marcelo d’Amorim. 2025. ChatAssert: LLM-Based
Test Oracle Generation With External Tools Assistance. IEEE Transactions on
Software Engineering 51, 1 (2025), 305–319. https://doi.org/10.1109/TSE.2024.
3519159
[7] Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long Short-Term Memory. Neu-
ralComputation9,8(1997),1735–1780.https://doi.org/10.1162/neco.1997.9.8.1735
[8] Soneya Binta Hossain and Matthew B. Dwyer. 2025. TOGLL: Correct and Strong
Test Oracle Generation with LLMS. In 2025 IEEE/ACM 47th International Confer-
ence on Software Engineering (ICSE), 2025. IEEE Press, Ottawa, Ontario, Canada,
1475–1487. https://doi.org/10.1109/ICSE55347.2025.00098
[9] Edward J. Hu, yelong shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean
Wang, Lu Wang, and Weizhu Chen. 2022. LoRA: Low-Rank Adaptation of Large
Language Models. In International Conference on Learning Representations,
2022. . Retrieved from https://openreview.net/forum?id$=$nZeVKeeFYf9
[10] James W. Hunt and Thomas G. Szymanski. 1977. A fast algorithm for computing
longest common subsequences. Commun. ACM 20, 5 (May 1977), 350–353. https:
//doi.org/10.1145/359581.359603
[11] Shaker Mahmud Khandaker, Fitsum Kifetew, Davide Prandi, and Angelo Susi.
2025. AugmenTest: Enhancing Tests with LLM-Driven Oracles. In 2025 IEEE
ConferenceonSoftwareTesting,VerificationandValidation(ICST),2025.279–289.
https://doi.org/10.1109/ICST62969.2025.10988926
[12] C. Lattner and V. Adve. 2004. LLVM: a compilation framework for lifelong pro-
gramanalysis&transformation.InInternationalSymposiumonCodeGeneration
and Optimization, 2004. CGO 2004., 2004. 75–86. https://doi.org/10.1109/CGO.
2004.1281665
[13] Rensis Likert. 1932. A technique for the measurement of attitudes. Archives of
psychology (1932).
[14] LLVM Foundation. 2024. Clang: a C language family frontend for LLVM. Re-
trieved from https://clang.llvm.org/
[15] Ggaliwango Marvin, Nakayiza Hellen, Daudi Jjingo, and Joyce Nakatumba-
Nabende. 2024. Prompt Engineering in Large Language Models. In Data Intelli-
gence and Cognitive Informatics, 2024. Springer Nature Singapore, Singapore,
387–402.
[16] Facundo Molina, Alessandra Gorla, and Marcelo d’Amorim. 2025. Test Oracle
Automation in the era of LLMs. ACM Transactions on Software Engineering and
Methodology 34, 5 (2025), 1–24. https://doi.org/10.1145/3715107
[17] Pengyu Nie, Rahul Banerjee, Junyi Jessy Li, Raymond J. Mooney, and Milos
Gligoric. 2023. Learning Deep Semantics for Test Completion. In 2023 IEEE/ACM
45th International Conference on Software Engineering (ICSE), 2023. 2111–2123.
https://doi.org/10.1109/ICSE48619.2023.00178
[18] Carlos Pacheco and Michael D. Ernst. 2007. Randoop: feedback-directed random
testing for Java. In Companion to the 22nd ACM SIGPLAN Conference on Object-
Oriented Programming Systems and Applications Companion (OOPSLA ’07),
2007. Association for Computing Machinery, New York, NY, USA, 815–816. https:
//doi.org/10.1145/1297846.1297902
[19] Reza Meimandi Parizi, Sai Peck Lee, and Mohammad Dabbagh. 2014. Achieve-
ments and Challenges in State-of-the-Art Software Traceability Between Test
and Code Artifacts. IEEE Transactions on Reliability 63, 4 (2014), 913–926.
https://doi.org/10.1109/TR.2014.2338254
[20] Shuo Ren, Daya Guo, Shuai Lu, Long Zhou, Shujie Liu, Duyu Tang, Neel Sun-
daresan, Ming Zhou, Ambrosio Blanco, and Shuai Ma. 2020. CodeBLEU: a
Method for Automatic Evaluation of Code Synthesis. (2020). Retrieved from
https://arxiv.org/abs/2009.10297
[21] Bart Van Rompaey and Serge Demeyer. 2009. Establishing Traceability Links
between Unit Test Cases and Units under Test. In 2009 13th European Conference
on Software Maintenance and Reengineering, 2009. 209–218. https://doi.org/10.
1109/CSMR.2009.39
[22] The Tree-sitter Contributors. 2024. Tree-sitter. Retrieved October 25, 2024 from
https://github.com/tree-sitter/tree-sitter
[23] Michele Tufano, Shao Kun Deng, Neel Sundaresan, and Alexey Svyatkovskiy.
2022. Methods2Test: a dataset of focal methods mapped to test cases. In Proceed-
ings of the 19th International Conference on Mining Software Repositories (MSR
’22), 2022. Association for Computing Machinery, New York, NY, USA, 299–303.
https://doi.org/10.1145/3524842.3528009
246

<!-- Page 12 -->

ICSE-SEIP ’26, April 12–18, 2026, Rio de Janeiro, Brazil Cong Li et al.
[24] Michele Tufano, Dawn Drain, Alexey Svyatkovskiy, and Neel Sundaresan. 2022.
Generating accurate assert statements for unit test cases using pretrained trans-
formers. In Proceedings of the 3rd ACM/IEEE International Conference on Au-
tomation of Software Test, 2022. Association for Computing Machinery, New
York, NY, United States, 54–64. https://doi.org/10.1145/3524481.3527220
[25] Cody Watson, Michele Tufano, Kevin Moran, Gabriele Bavota, and Denys Poshy-
vanyk. 2020. On learning meaningful assert statements for unit test cases. In
Proceedings of the ACM/IEEE 42nd International Conference on Software Engi-
neering (ICSE ’20), 2020. Association for Computing Machinery, New York, NY,
USA, 1398–1409. https://doi.org/10.1145/3377811.3380429
[26] Robert White, Jens Krinke, and Raymond Tan. 2020. Establishing multilevel test-
to-code traceability links. In Proceedings of the ACM/IEEE 42nd International
Conference on Software Engineering (ICSE ’20), 2020. Association for Comput-
ing Machinery, New York, NY, USA, 861–872. https://doi.org/10.1145/3377811.
3380921
[27] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng,
Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng
Liu, Fan Zhou, Fei Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong
Tang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jing Zhou,
Jingren Zhou, Junyang Lin, Kai Dang, Keqin Bao, Kexin Yang, Le Yu, Lianghao
Deng, Mei Li, Mingfeng Xue, Mingze Li, Pei Zhang, Peng Wang, Qin Zhu, Rui
Men, Ruize Gao, Shixuan Liu, Shuang Luo, Tianhao Li, Tianyi Tang, Wenbiao Yin,
Xingzhang Ren, Xinyu Wang, Xinyu Zhang, Xuancheng Ren, Yang Fan, Yang Su,
Yichang Zhang, Yinger Zhang, Yu Wan, Yuqiong Liu, Zekun Wang, Zeyu Cui,
Zhenru Zhang, Zhipeng Zhou, and Zihan Qiu. 2025. Qwen3 Technical Report.
(2025). Retrieved from https://arxiv.org/abs/2505.09388
[28] 2012. Module (Unit) Testing. In The Art of Software Testing. John Wiley & Sons,
Ltd, 85–111. https://doi.org/10.1002/9781119202486.ch5
[29] 2024. Google Test Framework. Retrieved from https://github.com/google/
googletest
247

