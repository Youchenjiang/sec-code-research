---
title: "AugmenTest: Enhancing Tests with LLM-Driven Oracles"
year: 2025
author: "Research Team"
source_pdf: "AugmenTest (2025) Enhancing Tests with LLM-Driven Oracles.pdf"
---

<!-- Page 1 -->

AugmenTest: Enhancing Tests with LLM-Driven
Oracles
Shaker Mahmud Khandaker
Software Engineering Unit
Fondazione Bruno Kessler
Trento, Italy
skhandaker@fbk.eu
Fitsum Kifetew
Software Engineering Unit
Fondazione Bruno Kessler
Trento, Italy
kifetew@fbk.eu
Davide Prandi
Software Engineering Unit
Fondazione Bruno Kessler
Trento, Italy
prandi@fbk.eu
Angelo Susi
Software Engineering Unit
Fondazione Bruno Kessler
Trento, Italy
susi@fbk.eu
Abstract—Automated test generation is crucial for ensuring the
reliability and robustness of software applications while at the
same time reducing the effort needed. While significant progress
has been made in test generation research, generating valid test
oracles still remains an open problem.
To address this challenge, we present AugmenTest, an ap-
proach leveraging Large Language Models (LLMs) to infer
correct test oracles based on available documentation of the
software under test. Unlike most existing methods that rely on
code, AugmenTest utilizes the semantic capabilities of LLMs to
infer the intended behavior of a method from documentation and
developer comments, without looking at the code. AugmenTest
includes four variants: Simple Prompt, Extended Prompt, RAG
with a generic prompt (without the context of class or method
under test), and RAG with Simple Prompt, each offering different
levels of contextual information to the LLMs.
To evaluate our work, we selected 142 Java classes and gen-
erated multiple mutants for each. We then generated tests from
these mutants, focusing only on tests that passed on the mutant
but failed on the original class, to ensure that the tests effectively
captured bugs. This resulted in 203 unique tests with distinct
bugs, which were then used to evaluate AugmenTest. Results show
that in the most conservative scenario, AugmenTest’s Extended
Prompt consistently outperformed the Simple Prompt, achieving
a success rate of 30% for generating correct assertions. In
comparison, the state-of-the-art TOGA approach achieved 8.2%.
Contrary to our expectations, the RAG-based approaches did not
lead to improvements, with performance of 18.2% success rate
for the most conservative scenario.
Our study demonstrates the potential of LLMs in improving
the reliability of automated test generation tools, while also
highlighting areas for future enhancement.
Index Terms—Test Oracles, Large Language Models, Assertion
Generation, Context-Aware Testing, Software Testing, Retrieval-
Augmented Generation
I. I NTRODUCTION
In modern software development, ensuring the reliability
and robustness of applications is a critical challenge, often
addressed through comprehensive testing. However, automat-
ing test generation, while essential for keeping pace with
rapidly evolving codebases, faces a persistent issue related
to generating valid oracles [1]. This problem arises when
automated tools incorrectly interpret unintended behavior as
correct, leading to unreliable tests. Traditional test generation
tools, such as EvoSuite, rely on the code of the system
under test to generate assertions [2]. Such assertions are useful
as regression oracles for identifying eventual regression bugs
in successive releases by capturing deviations with respect to
the previous implementation. On the other hand, however, they
are not able to capture bugs due to implementations deviating
from expected behavior.
Large Language Models, trained on vast amounts of natural
language and code data, present a promising solution to this
issue. By understanding both code and its associated docu-
mentation, LLMs can potentially infer the intended behavior
of software, offering a more robust approach to test oracle
generation. This shift from code-centric to context-aware test
oracle generation could address the limitations of conventional
approaches and significantly improve the usefulness of auto-
mated tests in exposing bugs.
In this paper, we introduce AugmenTest, an approach that
harnesses the semantic capabilities of LLMs [3] to generate
correct test oracles by leveraging code documentation and
developer comments, rather than depending on the code it-
self. AugmenTest offers also the possibility to use Retrieval-
Augmented Generation (RAG) which can be effective when
dealing with richer contexts. AugmenTest has four distinct
variants, each providing different levels of contextual infor-
mation to the LLMs: Simple Prompt, Extended Prompt, RAG
with a generic prompt, and RAG with Simple Prompt.
We evaluated our approach on a dataset of 203 unique test
cases for 142 Java classes, specifically selected for their ability
to expose bugs. We performed experiments across multiple
replications and adopted a threshold-based methodology, en-
suring that consistent results were generated across different
runs. We considered three thresholds, namely 60%, 80%,
and 100%, which reflect varying levels of result consistency
across replications. These thresholds provide a measure of the
reliability of the generated assertions, as explained in detail in
Section IV.
The results show that AugmenTest’s Extended Prompt vari-
ant significantly outperforms the other variants. Results also
show that the Extended Prompt variant outperforms the state-
of-the-art TOGA [4] approach, achieving a 30% success rate
in the most conservative 100% threshold scenario, compared
to TOGA’s 8.2%. However, contrary to our expectations, the
RAG-based variants did not perform as well, highlighting the
need for a refinement of their integration in oracle generation.
arXiv:2501.17461v1  [cs.SE]  29 Jan 2025

<!-- Page 2 -->

Overall, our study demonstrates the potential of LLMs to
overcome the Oracle problem in software testing, offering
substantial improvements over existing methods. However, the
mixed results for RAG-based variants highlight opportunities
for future work, particularly in improving how structured data
is integrated into the generation process. By exploring the
capabilities and limitations of LLMs in test oracle generation,
this paper highlights the potential for these models to over-
come key challenges in automated testing, paving the way for
more reliable and efficient test generation tools.
The main contributions of this study are as follows:
Contribution 1: Empirical Study and Benchmarking
with Mutants: We conducted a comprehensive evaluation
of AugmenTest across test cases from 142 Java classes,
analyzing its performance in generating accurate test oracles
by leveraging large language models. This study uniquely
benchmarks AugmenTest’s ability to infer correct assertions by
using mutants (buggy versions of the classes), ensuring that the
inferred oracles pass on the original class and fail on the buggy
class. This empirical evaluation provides a robust framework
for assessing the accuracy and effectiveness of LLM-driven
oracle generation.
Contribution 2: Comparison of Prompt Variants: We
explored multiple prompt variants, including Simple Prompts,
Extended Prompts, and Retrieval-Augmented Generation, to
investigate the impact of context-rich prompts on assertion
inference. Our results demonstrate that while providing ex-
tended context can improve oracle generation, using RAG-
based approaches does not enhance performance as expected.
Contribution 3: Flexible Framework for LLM Oracle
Inference: Unlike previous studies, such as TOGA, which
trains models to infer test oracles, AugmenTest presents a
more flexible, model-agnostic framework. Our approach can
be applied to any LLM, making it adaptable to evolving
models and new developments in AI.
Contribution 4: Dataset: We are making our dataset
publicly available [5] to support future research on LLM-based
test oracle generation. The dataset includes 203 test cases from
142 Java classes, each with at least 30 characters of developer
comments per method, ensuring sufficient context for LLM-
based inference. We also include the generated mutants (buggy
versions of the classes), which were used to benchmark the
performance of AugmenTest in inferring correct assertions.
The remainder of this paper is organized as follows: Sec-
tion II discusses closely related works in the area of LLMs for
assertion generation and test generation in general. Section III
presents details of the AugmenTest approach. A discussion of
the experiment we performed to evaluate the effectiveness of
AugmenTest, the results obtained, and the relevant threats to
validity are presented in Section IV. Finally in Section V we
present concluding remarks and outline potential directions for
future work.
II. R ELATED WORK
We conducted a literature review focusing on the intersec-
tion of software testing and large language models (LLMs).
Using a broad search query in the Scopus database [6],
we initially identified 191 studies. After manually filtering
out irrelevant papers and artifacts, we narrowed the set to
8 studies based on specific selection criteria. The selection
criteria involved including studies that defined or experimented
with software testing using large language models (LLMs),
presented empirical findings, applied LLMs throughout the
testing lifecycle, underwent peer review, and were written in
English; conversely, papers were excluded if they did not focus
on software testing tasks, lacked active use of LLMs, only
mentioned LLMs in future contexts, were published before
2015, were secondary studies, or were unavailable as full text.
Finally, using a snowballing approach, we reviewed references
and added 3 more studies, resulting in 11 key papers relevant
to our research.
Our related work is divided into two key areas: Oracle
Generation and Unit Test Generation. Below is a summary
of the most relevant studies within these categories.
A. Oracle Generation
Gabriel Ryan et al. introduce TOGA [4], a transformer-
based framework for test oracle generation. TOGA integrates
EvoSuite and utilizes an oracle classifier and assertion
ranker, significantly improving the inference of assertions
and exceptional behaviors. It has demonstrated superior bug-
finding accuracy compared to other tools. However, Liu et
al. [7] highlight limitations in TOGA’s evaluation methods,
proposing TEval+ as a more realistic metric, revealing that
TOGA’s precision in detecting bugs is much lower when
evaluated under realistic conditions.
Tufano et al. [8] leverage pretrained transformers for assert
statement generation, achieving substantial improvements over
ATLAS, including an 80% boost in top-1 accuracy. Nie et
al. [9] introduce TECO, which applies code semantics for
oracle generation, outperforming TOGA by 82% in exact-
match accuracy. They also highlight the impact of execution
re-ranking in enhancing prediction accuracy.
Other approaches, like the Information Retrieval (IR)-based
method by Yu et al. [10], show that combining IR and deep
learning techniques outperforms purely deep learning-based
solutions such as ATLAS in assertion generation tasks. Deep
learning-based approaches, such as those analyzed by Shin
et al. [11] provide an extensive analysis of Neural Oracle
Generation (NOG) models, highlighting the lack of correlation
between textual similarity metrics (e.g., BLEU, ROUGE) and
test adequacy metrics (e.g., code coverage, mutation score),
emphasizing the need for more effective evaluation methods
in oracle generation.
B. Unit Test Generation
In the domain of unit test generation, Sch ¨afer et al. present
TESTPILOT [12], a system that uses LLMs for end-to-end test
generation, achieving high statement coverage and effective
assertion generation. Tufano et al. propose an approach [13],
a model fine-tuned on real-world developer-written test cases,

<!-- Page 3 -->

outperforming GPT-3 and achieving test coverage comparable
to EvoSuite.
Tang et al. [14] explore ChatGPT’s ability to generate
unit test suites, finding that while it struggles with coverage
compared to EvoSuite, it excels in readability and usability.
Yuan et al. [15] take this further with CHATTESTER, a tool
that improves ChatGPT-generated tests by reducing compila-
tion errors and enhancing assertion accuracy.
Xie et al. introduce ChatUniTest [16], another ChatGPT-
based tool that surpasses AthenaTest and EvoSuite in sev-
eral key test generation metrics, emphasizing the efficiency of
ChatGPT-based repair mechanisms.
These studies underscore the significant advancements made
in both oracle and unit test generation, showcasing the evolv-
ing role of LLMs in improving automated testing workflows.
While most approaches focus on pretrained models, our work
distinguishes itself by incorporating context from code doc-
umentation and developer comments, ensuring more targeted
and efficient test oracle generation.
III. A UGMEN TEST : A FRAMEWORK FOR LLM- BASED
ORACLE INFERENCE
In this section, we present AugmenTest, our approach for
generating test oracles using LLMs. AugmenTest tackles the
problem of generating valid test oracles by leveraging the
semantic understanding capabilities of LLMs to infer correct
behavior based on context extracted from the Class Under Test
and Method Under Test. This context includes documentation,
metadata, and developer comments. AugmenTest also exploits
Retrieval-Augmented Generation (RAG) for structured knowl-
edge retrieval.
Overview of AugmenTest. The overall workflow of Aug-
menTest is illustrated in Figure 1. AugmenTest consists of
two main phases: the preprocessing phase , where relevant
information from the source code is extracted and prepared,
and the assertion generation phase, where LLMs are consulted
to generate assertions based on different levels of contextual
information. These two phases are presented in Algorithm 1
and described below.
A. Phase 1: Preprocessing and Metadata Extraction
In this phase, AugmenTest analyzes the source code and
extracts essential metadata about the class and method under
test, building a structured knowledge base that is used later
to provide context for assertion generation (lines 1-2 in Algo-
rithm 1). Specifically, this step includes:
• Parsing each class in the project to extract metadata such
as method signatures, return types, class variables, de-
pendencies, developer comments, and relationships (e.g.,
inheritance or interfaces).
• Storing the extracted metadata in a structured or semi-
structured format, which can later be used for generat-
ing contextual prompts for the LLM. For instance, in
our current implementation, we store the information in
JSON format, while in principle any other format could
be adopted.
• For variants using RAG (i.e., RAG and RAG SP ), this
information is converted into vector embeddings using a
suitable embedding model. This allows efficient retrieval
of relevant information during the assertion generation
phase.
The result of this phase is a knowledge base containing the
necessary metadata about the classes and methods in the
project, along with vectorized embeddings for RAG-based
retrieval when applicable.
B. Phase 2: Assertion Generation with LLMs
In this phase, AugmenTest uses LLMs to generate test
assertions based on different variants of contextual information
(lines 3-24 in Algorithm 1). This phase involves performing
different tasks, as outlined below.
Test Case Preprocessing. For each test case, AugmenTest
first identifies the focal methods (the method which is the
subject of the specific test case under consideration) in the
test case and strips the assertions, leaving a test prefix . The
test prefix is prepared by keeping only the non-assertion
statements in the test case and leaving a placeholder for
the final assertion to be generated. Note that here we are
assuming the test generation tool (e.g., EvoSuite) generates
one or more assertions together with the test cases, in which
case AugmenTest removes them and replaces them with a
placeholder which will be replaced by an assertion using the
LLM. However, the preprocessing process should be equally
applicable also in scenarios where the test generation tool does
not generate assertions.
Contextual Prompt Generation. Our prompt design prior-
itizes concise and deterministic outputs tailored specifically
for generating JUnit assertions. Unlike traditional prompt
engineering techniques such as role-playing or structured
examples, which are better suited for open-ended tasks, our
approach focuses on providing clear and task-relevant context
(e.g., method details, developer comments) while minimizing
response noise. Explicit formatting instructions (e.g., ”Your
statement should end with a semicolon” ) ensure compatibility
with automated post-processing and downstream validation
steps. This design choice optimizes efficiency and reduces
ambiguity, particularly for procedural tasks, while accommo-
dating the token and computational constraints of both closed-
source APIs and local, quantized models.
Once the test case is preprocessed with a placeholder for the
eventual assertion to be inserted, the next step is to formulate
an appropriate prompt to be sent to the LLM requesting for an
assertion that replaces the placeholder previously inserted. The
key aspects in this phase are the level of information used for
constructing the context for the prompt, which are organized
into four variants as follows:
1) Simple Prompt (SP): Basic information about
the class such as: class name , fields and
method under test details such as: focal method
name, signature, parameters, dependencies,
return type , developer comments are ex-
tracted from the stored structured data and are replaced

<!-- Page 4 -->

Fig. 1. Overview of AugmenTest approach. Each test case is processed to remove existing assertions, if any, and produce a test prefix with a placeholder for
the eventual assertion to be generated. Then a prompt is crafted and sent to the LLM. The returned assertion is incorporated into the test prefix, then compiled
and executed . If successful the test cases is saved as a candidate, otherwise the LLM is prompted again.
A Java project includes a class called <class_name>
with following fields: <fields> and it has the
following method details as JSON string:
<focal_method_details>.
We need a test oracle for a JUnit test case based on
the above information and <DEVELOPER COMMENTS> of the
method to test its functionality.
In the following test case, replace the
<assertion_placeholder> with an appropriate assertion:
<test_method_code>
Just write the assertion statement for the
placeholder, not the whole test. No explanation or
markdown formatting/tick needed.
Listing 1. Simple Prompt Template
A Java project includes a class called <class_name>
with following fields: <fields> and it has the
following Focal method details as JSON string:
<focal_method_details>.
The class has other methods with developer comments as
JSON string: <class_method_details>.
We need a test oracle for a JUnit test case based on
the above information and <DEVELOPER COMMENTS> of the
method to test its functionality.
In the following the test case, replace the
<assertion_placeholder> with an appropriate assertion:
<test_method_code>
Just write the assertion statement for the
placeholder, not the whole test. No explanation or
markdown formatting/tick needed.
Listing 2. Extended Prompt Template
in the simple prompt template along with the test
prefix with assertion placeholder as shown
in Listing 1.
2) Extended Prompt (EP): In addition to the information
added in Simple Prompt, detail about all methods in
A Java project includes a class called <class_name>.
We need a test oracle for a JUnit test case based on
the information you can find in the provided files and
developer comments of the method to test its
functionality.
In the following the test case, replace the
<assertion_placeholder> with an appropriate and
correct assertion:
<test_method_code>
Just write the assertion statement for the
placeholder, not the whole test. Your statement
should end with a semicolon. No explanation or
markdown formatting/tick needed.
Listing 3. RAG Generic Prompt Template
the class under test are added to the context to replace
in the extended prompt template as shown in Listing 2.
3) RAG with Generic Prompt (RAG): No context about
class or method under test is added in the prompt. In-
stead, retrieval-augmented generation is used to retrieve
relevant information of the class from the structured data
store to generate assertions as shown in Listing 3.
4) RAG with Simple Prompt (RAG SP): Combines
the Simple Prompt and RAG with the database of
class/method information as shown in Listing 4.
Assertion Generation with LLM Interface: Once the
contextual prompt is prepared, AugmenTest uses the LLM
Interface, a core component responsible for interacting with
any chosen LLM to generate assertions. It is designed with
flexibility and modularity in mind, enabling developers to
integrate different LLMs into the test oracle generation pro-
cess seamlessly. This interface abstracts the underlying model
selection, ensuring that AugmenTest can work with a wide

<!-- Page 5 -->

A Java project includes a class called <class_name>
with following fields: <fields> and it has the
following method details as JSON string:
<focal_method_details>.
We need a test oracle for a JUnit test case based on
the above information and <DEVELOPER COMMENTS> of the
method along with any other relevant information you
can find in the provided vector store files to test
its functionality.
In the following the test case, replace the
<assertion_placeholder> with an appropriate assertion:
<test_method_code>
Just write the assertion statement for the
placeholder, not the whole test. Your statement should
end with a semicolon. No explanation or markdown
formatting/tick needed.
Listing 4. RAG Simple Prompt Template
range of LLMs — whether they are open-source, closed-
source, large, or quantized models. By decoupling the oracle
generation process from specific LLM implementations, the
interface ensures that our system remains versatile and future-
proof as new LLMs are developed. When the selected LLM
is prompted to generate an appropriate assertion for the test
case, it returns a response with potential assertion based on the
context provided, which is later extracted and inserted into the
test prefix to complete the test case.
Validation and Execution. After generating an assertion
and completing the test case prefix, AugmenTest checks the
syntactic correctness of the test case and attempts to compile
and execute it (lines 18-22 in Algorithm 1). If the test
case compiles successfully and executes without any errors
(regardless of whether it passes or fails), the test is considered
a valid candidate. If the test fails to compile or executes with
errors, the assertion generation process is re-tried for a fixed
number of attempts within a predefined budget until either a
valid candidate is found or the budget is exhausted.
Test Selection and Candidate Generation. Once a valid
test case is generated (i.e., it compiles and runs successfully),
it is added to the pool of candidate test cases. This process
is repeated for each test case in the project, with the LLM
generating assertions tailored to each focal method.
In summary, the process in AugmenTest begins by extract-
ing metadata from the project repository, preparing context
for the test cases, formulating a suitable prompt for the LLM,
and prompting the LLM to generate assertions based on the
selected variant (SP, EP, RAG, or RAG SP). The generated
assertions are validated by compiling and executing the test
cases. Successful test cases are added to the candidate pool,
while failed attempts are re-tried within a limited budget.
IV. E VALUATION
To evaluate our approach, we conducted a set of experiments
to answer the following research questions:
RQ1: Can AugmenTest infer correct test oracles?
With this question, we aim to evaluate the ability of Aug-
menTest to generate meaningful and accurate assertions for
test cases where the original assertions, if any, are replaced
with placeholders. The focus is on assessing whether the
Algorithm 1: Oracle Generation with AugmenTest
Input : Project repository/source code, Test cases (auto-generated or manual),
LLM model, Variants: SP, EP, RAG, RAG SP
Output: Candidate test cases with inferred assertions
1 metadata ← ExtractMetadata(source code );
2 embeddings ← ConvertToVectors(metadata);
3 foreach test ∈ test casesdo
4 f ocalM ethods← IdentifyFocalMethods(test);
5 testP ref ix← PrepareTestPrefix(test);
6 if variant == SP then
7 context ← Basic context of CUT and MUT;
8 if variant == EP then
9 context ← Basic context + all methods in CUT;
10 if variant == RAG then
11 context ← Retrieved structured JSON embeddings with no
specific CUT/MUT context;
12 if variant == RAGSP then
13 context ← Simple prompt context + structured JSON
embeddings;
14 success ← F alse;
15 attempts ← 0;
16 while not success and attempts < budgetdo
17 assertion ← GenerateAssertion(context);
18 if CompileAndRun(testP ref ix, assertion) then
19 success ← T rue;
20 candidateTests.append(testP ref ix+ assertion);
21 else
22 attempts += 1;
23 if success then
24 candidateTests.append(testP ref ix+ assertion);
25 return candidateTests;
generated assertions are consistent with the expected behavior
of the class and method under test, as described in the relevant
documentation such as developer comments.
RQ2: Does providing additional context improve asser-
tion generation?
With this question, we aim to explore whether enhancing
the context for LLM-based assertion generation by integrating
additional information, such as class information, method
data, and developer comments, improves the accuracy of the
inferred test oracles. Different levels of context information are
provided through LLM prompt variants, and the effectiveness
of each variant is measured.
A. Prototype
We have implemented the AugmenTest approach in a proto-
type using Python 3.10 , incorporating various open-source
tools and libraries to enhance its modularity and flexibility.
The prototype integrates two types of LLMs: a closed-source
API and open-source models. For closed-source, we utilize
the OpenAI API for GPT-4o1. For open-source, we employ
quantized models like Meta-Llama-3-8B-Instruct2
and Nous-Hermes-Llama2-13b3 using the GPT4All4
(v2.7.0) framework, enabling the models to run locally and pri-
vately without relying on external servers. For our prototype,
1https://openai.com/index/hello-gpt-4o/
2https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
3https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b
4https://www.nomic.ai/gpt4all/

<!-- Page 6 -->

subject models do not include LLMs for code and we only con-
sidered general purpose LLMs. The choice to utilize general
purpose LLMs rather than code-specific LLMs was intentional
and based on the nature of the problem domain. While LLMs
for code, such as Codex5, excels at generating syntactically
correct code and understanding programming constructs due
to their specialized training on code corpora, our primary
focus lies in understanding and leveraging textual descriptions,
such as developer comments. These descriptions provide high-
level guidance on test oracle construction, which requires
advanced natural language understanding — a strength of
general purpose LLMs trained on broader datasets that include
both code and natural language. Moreover, the generated code
in our context is minimal, typically limited to expressions for
assertions or oracles, where the key challenge is correctly
interpreting the semantic intent conveyed in the comments.
Although integrating code-specific LLMs could be explored
as part of future work, our current approach prioritizes the
linguistic interpretive capabilities of general purpose LLMs to
align with the requirements of our methodology.
For test generation, the prototype uses EvoSuite6
(v1.2.0), an automated Java unit test generation tool.
Tree-sitter7 (v0.20.1) is employed to parse Java code and
extract metadata such as method names, classes, comments,
etc. The Jinja2 (v3.1.2) template engine is utilized to
dynamically create prompts tailored for each class and method
under test. LangChain8 serves as the framework to manage
interactions between the code context and LLMs.
In our prototype, we employed OpenAI’s File Search
Assistant9 tool to implement the RAG variants. This tool
utilizes the text-embedding-3-large model with 256
dimensions for embedding, a chunk size of 800 tokens with a
400-token overlap, and incorporates up to 20 chunks into the
context.
Additionally, the prototype uses JUnit (v4.12) for compil-
ing and executing tests, and the Major Mutation Framework 10
(v3.0.1) for generating mutants. The prototype was used for
the experimental evaluation discussed in this section and is
publicly available at: https://github.com/se-fbk/augmentest.
B. Evaluation Setup
Dataset. The evaluation is based on Java classes sampled
from a dataset published in a recent study [17] consisting of
418 Java projects with more than 27,000 classes. From this
dataset, we selected all 142 Java classes in which every method
contains developer comments of at least 30 characters (see
Table I for the characteristics of the selected classes). A class
was included only if all its methods met this criterion, ensuring
that the comments provided meaningful information rather
than automatically generated parameter names. To evaluate
5https://openai.com/index/openai-codex/
6https://www.evosuite.org/
7https://tree-sitter.github.io/tree-sitter/
8https://www.langchain.com/framework/
9https://platform.openai.com/docs/assistants/tools/file-search
10https://mutation-testing.org/
n. Classes n. Loc n. Methods CCN
All classes 27,161 63 9 2.3
Selected classes 142 99 13 3.0
TABLE I
CHARACTERISTICS OF THE SELECTED CLASSES AND OF ALL THE CLASSES
IN GRUBER ET AL . [17]. n. Loc, n. Methods, CCN REPRESENT AVERAGE
LINES OF CODE , NUMBER OF METHODS , AND CYCLOMATIC COMPLEXITY
RESPECTIVEY .
our approach, we generated multiple mutants using the Major
Mutation Framework for these selected classes to introduce
potential bugs. Using EvoSuite, we generated test cases for
these mutants. From these generated tests, we selected those
that passed on the mutant but failed on the original class,
ensuring that they accurately captured the bugs introduced by
the mutation. This resulted in 203 unique test cases. Among
these, 93 contained Exception Oracles , which ensure
that expected exceptions occur or unexpected ones are avoided,
and 110 contained Assertion Oracles [4], which verify
the correctness of specific program outputs by checking con-
ditions such as equality. The projects span various domains,
including real-world examples, making the evaluation robust
and potentially generalizable to actual development scenarios.
The RAG variants of AugmenTest rely on a structured JSON
file to provide detailed metadata for Java projects. Each JSON
entry corresponds to a Java class and encapsulates class-level
and method-level details. Listing 5 shows an example.
{
"projectName": "ExampleProject",
"classes": [
{
"className": "ExampleClass",
"filePath": "src/main/java/ExampleClass.java",
"signature": "public class ExampleClass extends BaseClass implements
InterfaceA",
"superClass": "BaseClass",
"interfaces": ["InterfaceA"],
"package": "com.example",
"imports": ["java.util.List", "java.io.File"],
"methods": [
{
"methodName": "exampleMethod",
"signature": "public String exampleMethod(int param1, String param2)",
"returnType": "String",
"visibility": "public",
"parameters": [
{"name": "param1", "type" : "int"},
{"name": "param2", "type" : "String"}
],
"comments": "This method performs example functionality."
}
]
}
]
}
Listing 5. Example JSON structure for RAG input
The JSON file includes:
• Class-level Metadata: Includes the class name, file path,
signature, superclass, implemented interfaces, package,
and imported libraries.
• Method-level Metadata: Covers method names, signa-
tures, return types, visibility, parameters (name and type),
and developer comments.
AugmenTest Variants. As stated earlier we have four
different variants of AugmenTest each using different levels
of context information in their prompts (Section III-B). Fur-
thermore, different kinds of models are used for the actual

<!-- Page 7 -->

assertion inference, overall resulting in the following 9 con-
figurations of AugmenTest to be evaluated:
• GPT4o SP Simple Prompt variant using OpenAI’s
GPT4o model
• GPT4o EP Extended Prompt variant using OpenAI’s
GPT4o model
• LLAMA SP Simple Prompt variant using the quantized
version of Meta-Llama-3-8B-Instruct model
• LLAMA EP Extended Prompt variant using the quantized
version of Meta-Llama-3-8B-Instruct model
• HERMES SP Simple Prompt variant using the quantized
version of Nous-Hermes-Llama2-13b model
• HERMES EP Extended Prompt variant using the quan-
tized version of Nous-Hermes-Llama2-13b model
• RAG Gen RAG with generic prompt using OpenAI’s
GPT4o model
• RAG SP RAG with Simple Prompt using OpenAI’s
GPT4o model
• RAG EP RAG with Extended Prompt using OpenAI’s
GPT4o model
Baseline. As a baseline for comparison, we consider TOGA.
TOGA ranks assertions based on a combination of its classi-
fication accuracy and confidence levels [4]. It uses specific
thresholds for various assertion types, such as assertTrue
and assertEquals, to determine the minimum confidence
required, which restricts its ability to produce useful assertions
when the confidence is low. This often results in correctly
classified test prefixes yielding no output [18]. To mitigate this
issue, we use two variants of TOGA. The first variant ( TOGA
WT) is the default TOGA tool with default configurations
as publicly available. The second variant ( TOGA UN ) is a
variant where we relaxed its settings by disregarding the
confidence thresholds to allow the generation of assertions
even at lower confidence levels. This approach enabled a more
comprehensive evaluation of TOGA’s capabilities and ensured
that potentially valuable assertions were not excluded from
consideration, thus facilitating a more balanced comparison
with AugmenTest.
AugmenTest’s performance is compared to the TOGA ap-
proach which uses custom trained neural networks [4] to
infer oracles. While TOGA evaluates on datasets such as
Defects4J [19] and Methods2Test [20], which are datasets
most probably seen by most recent LLMs, potential data
leakage is very likely (a concern with TOGA’s reliance on
previously trained datasets). By constructing a new dataset of
bugs, we evaluate AugmenTest’s performance in a setting in
which the system under test’s code is unseen by the LLMs.
Evaluation Metrics. To evaluate the effectiveness of a
variant in generating a correct test oracle, we compile and
execute the test case augmented with the assertion generated
by the variant against the mutant (buggy) and original class
from which the test case was generated. If the test passes
on the original class but fails on the buggy we consider the
assertion to be a correct one (a true positive ). There are
other combinations of pass and fail resulting in three other
outcomes. In particular, the test with the generated assertion
could compile correctly but fails on both original and buggy
code ( false positive ); could pass on both original and buggy
(true negative); and could fail on the original but pass on the
buggy (false negative). This way of categorizing the outcomes
is similar to the one adopted by Gabriel Ryan et al. for
evaluating TOGA [4].
To account for the inherent variability in the responses
produced by LLMs, we repeat the assertion generation for
every test case 10 times. This results in situations where some
assertions are correct while others are not. Hence, we adopted
a threshold-based evaluation mechanism to measure the con-
sistency and reliability of the generated test oracles across
multiple runs. Specifically, we ran 10 replications of each
experiment and considered three thresholds: 60%, 80%, and
100%, which represent varying levels of consistency across the
replications. The thresholds indicate the minimum percentage
of replications that must generate the same assertion for a
given test case to be considered successful. For example, the
100% threshold is the most conservative, meaning that the test
case is only considered valid if all 10 replications generate the
correct assertions, whereas the 60% threshold is more lenient,
requiring correctness in only 6 out of the 10 runs.
Additionally, during each run, if the tool fails to generate
or extract an assertion from the LLM, it retries up to three
times before marking the attempt as unsuccessful. This retry
mechanism ensures that minor failures or inconsistencies in the
LLM’s response do not disproportionately affect the evaluation
outcomes.
Test Generation. For test generation during the dataset
preparation process described above, we used EvoSuite
version 1.2, to generate tests for both the original and mutated
classes. We generated these tests from the buggy class and tests
that passed on the buggy class but failed on the original class
were selected as candidate test cases for assertion generation.
The LLM used for assertion inference was prompted with
context data formatted as JSON, and assertions were replaced
in the test cases accordingly.
Execution Environment. We present here some details
regarding the software and hardware used in our experiment
to facilitate future replication studies. The evaluation was
conducted on two platforms: the TOGA ( TOGA UN , TOGA
WT) and API based experiments ( GPT4o SP , GPT4o SP ,
RAG Gen ) are executed on a machine with an Intel Core
i7 processor, 32GB RAM, and Ubuntu 22.04 OS. The ex-
periments using quantized local LLM installations ( LLAMA
SP, LLAMA EP , HERMES SP , HERMES EP ) are executed
on nodes in a cluster environment with AMD EPYC 7413
24-Core Processor and 0.5TB RAM.
C. Results
In this section, we present the results of the experiment
along with the two research questions we outlined earlier.
RQ1: Can AugmenTest infer correct oracles?: To answer
RQ1, we analyzed the correctness of the assertions generated
by the different AugmenTest variants as well as by the baseline

<!-- Page 8 -->

Acceptance threshold Variant TP % FP % TN % FN % Failures %
60%
GPT4o EP 45.5 26.4 19.1 1.8 7.2
GPT4o SP 37.3 32.7 15.5 2.7 11.8
RAG Gen 28.2 46.4 17.3 4.5 3.6
LLAMA SP 10.0 35.5 13.6 0.9 40.0
LLAMA EP 10.9 25.5 15.5 0.0 48.1
HERMES SP 9.1 20.0 8.2 2.7 60.0
HERMES EP 6.4 22.7 2.7 1.8 66.4
TOGA WT 5.5 4.5 9.1 0.0 80.9
TOGA UN 8.2 13.6 25.5 0.0 52.7
80%
GPT4o EP 36.4 20.0 16.4 0.9 26.3
GPT4o SP 34.5 30.9 13.6 1.8 19.2
RAG Gen 25.5 40.9 13.6 2.7 17.3
LLAMA SP 7.3 30.9 10.9 0.9 50.0
LLAMA EP 7.3 17.3 10.9 0.0 64.5
HERMES SP 6.4 8.2 2.7 1.8 80.9
HERMES EP 1.8 3.6 0.9 0.9 92.8
TOGA WT 5.5 4.5 9.1 0.0 80.9
TOGA UN 8.2 13.6 25.5 0.0 52.7
100%
GPT4o EP 30.0 15.5 11.8 0.9 41.8
GPT4o SP 29.1 27.3 11.8 0.9 30.9
RAG Gen 18.2 21.8 7.3 0.9 51.8
LLAMA SP 6.4 25.5 8.2 0.9 59.0
LLAMA EP 7.3 14.5 10.9 0.0 67.3
HERMES SP 3.6 5.5 0.0 1.8 89.1
HERMES EP 0.9 0.0 0.0 0.9 98.2
TOGA WT 5.5 4.5 9.1 0.0 80.9
TOGA UN 8.2 13.6 25.5 0.0 52.7
TABLE II
SUMMARY OF THE PERFORMANCES OF THE DIFFERENT VARIANTS . T RUE POSITIVE (TP) ARE CASES WHERE THE TEST PASSES ON THE ORIGINAL CODE
BUT FAILS ON THE MUTATED . FALSE POSITIVE (FP) INCLUDES TESTS THAT FAIL ON BOTH ORIGINAL AND MUTATED CODE . T RUE NEGATIVE (TN) ARE
THOSE TESTS THAT PASS ON BOTH ORIGINAL AND BUGGY CODE . FALSE NEGATIVE (FN) TESTS FAIL ON THE ORIGINAL CODE AND PASS ON THE
MUTATED . T HE ACCEPTANCE THRESHOLD INDICATES THE FRACTION OF REPLICAS THAT HAVE TO SHOW CONCORDANT RESULTS (SECTION IV).
FAILURES GROUP ALL THE CASES IN WHICH THE GENERATED TESTS DO NOT COMPILE OR THE REPLICAS EXHIBIT DISCORDANT BEHAVIOR .
(TOGA). The primary metric for correctness was the ability of
the newly generated assertion to pass on the original class and
fail on the buggy class (true positives). This ensures that the
assertion reflects the intended behavior of the method under
test with respect to the test statements in the specific test case.
In Table II we present the results of our experimental runs
on the dataset of 203 tests. We also graphically show the
success rates of the various variants in Figure 2. We note here
that we do not report results for two of the variants described
above ( RAG SP and RAG EP ) as we excluded them from
the experimentation based on the results of RAG Gen where
the results were not as promising while the experiments are
quite time consuming and expensive. Hence, in the interest
of saving time and resources, we decided to exclude them
from the experiment. We also further note that for similar
reasons we ran the experiment with the RAG variant ( RAG
Gen) only 5 times per test case, while for all the other variants
we performed 10 repetitions.
The results demonstrate that AugmenTest can indeed infer
correct assertions, with the GPT-4 model performing sig-
nificantly better than LLAMA and HERMES in terms of
overall success rates. The use of Extended Prompts (EP)
led to higher success rates than the Simple Prompt (SP),
suggesting that providing more information improves assertion
inference. Specifically, the GPT4o EP variant gives the best
performance out of the variants.
Considering the baseline variants ( TOGA UN and TOGA
WT) which employ specialized neural models, the results show
that three of AugmenTest’s variants (GPT4o EP , GPT4o SP ,
and RAG Gen ) perform consistently better than the baseline
variants in all three levels of threshold. The baseline variants
achieve low success rates as can be seen from Table II. In
particular the baseline with the default settings ( TOGA WT )
achieves low success rates, while relaxing some of the settings
(as discussed earlier in Section IV) appears to have improved
the success rate where the TOGA UN variant achieves 3
percentage points improvement over the default variant (TOGA
WT) for all the threshold values considered. We note here that
in our dataset there were a number of test cases (as generated
by EvoSuite) that involve exception handling assertions. In
these cases, none of the variants experimented with were able
to infer the correct assertion. Hence, the results presented here
are only for those test cases involving non-exception assertions
(more on this in the Discussion Section IV-D).
RQ2: Does enhancing the context improve assertion gener-
ation?: For RQ2, we focus on the different prompt variants of
AugmenTest to evaluate their relative effectiveness. As can be
seen in Table II and Figure 2, at 60% threshold, AugmenTest’s
Extended Prompt (EP) achieved the highest success rate of
45.5%, compared to the Simple Prompt (SP) at 37.3%. When
we increase the threshold to 80%, EP still outperformed other
variants with 36.4%, while SP achieved 34.5%. In the most
conservative scenario, where 100% consistency is required
across all replications, the success rates drop, but EP continues
to lead at 30%, with SP at 29.1%. Interestingly, the RAG-based
approaches consistently underperformed across all thresholds,

<!-- Page 9 -->

Th=60% Th=80% Th=100%
TOGA WT
HERMES EP
TOGA UN
HERMES SPLLAMA SPLLAMA EPGPT4o RAGGPT4o SPGPT4o EPTOGA WT
HERMES EP
TOGA UN
HERMES SPLLAMA SPLLAMA EPGPT4o RAGGPT4o SPGPT4o EPTOGA WT
HERMES EP
TOGA UN
HERMES SPLLAMA SPLLAMA EPGPT4o RAGGPT4o SPGPT4o EP
0%
10%
20%
30%
40%
Experiment configuration
Success rate
Fig. 2. Performance of the different variants with three values of consistency thresholds (Th).
suggesting that while enriching the LLMs with additional
structured data holds potential, it requires further refinement
to realize its full benefits. We also notice that the difference
between the EP and SP variants diminishes as the threshold
level is increased.
These results suggest that while AugmenTest can infer
correct assertions, the introduction of RAG did not yield
the expected improvements. In fact, the RAG Gen variant
underperformed compared to both the Simple and Extended
Prompts. The success rate for GPT4o EP , though marginally
higher than GPT4o SP , indicates that additional context does
help but not substantially.
We also note from the results in Table II that there are
several cases of failure (Failures column) where the assertion
generation did not produce candidates, mainly because the
generated assertions did not compile/run successfully. This
also shows an inherent issue with using LLMs, at least in
their current state, which does not necessarily guarantee a valid
response. Further studies are required to understand how much
of this problem could be mitigated by improving the prompting
mechanism, of course besides improving the performances of
the models themselves.
To facilitate replication of the work reported in this paper
and further experimentation we make all data and results
publicly available online [5].
D. Discussion
The experimental results demonstrate that AugmenTest ef-
fectively infers correct test oracles across various scenarios.
As shown in Table II, the True Positive (TP) column
highlights the percentage of successfully inferred assertion
oracles, where AugmenTest was able to correctly identify
assertions in 110 test cases. Notably, however, none of the vari-
ants was successful in inferring any Exception Oracles ,
which is an unexpected outcome. While TOGA is typically
capable of classifying both assertion and exception oracles,
its failure to infer exceptions in this case is surprising, espe-
cially given its training on Exception Oracles. This indicates
potential limitations in TOGA’s ability to generalize beyond
its training data in practical scenarios. This finding also in-
dicates that AugmenTest approach requires further refinement
in future work for handling oracles involving exceptions.
The evaluation reveals a notable performance disparity
among various models in inferring correct test oracles. The
GPT-4o model from OpenAI API consistently outperforms
all other variants, demonstrating superior effectiveness in this
task. However, its reliance on cloud-based processing may
raise significant privacy concerns, as sensitive data may be
exposed during model interaction. On the other hand, quan-
tized models like Hermes and Llama, while not achieving
comparable performance levels, provide the advantage of be-
ing run entirely locally. This eliminates privacy risks, making
them suitable for environments where data confidentiality is
paramount.
One of the key finding is that providing more detailed and
structured information via RAG did not lead to better oracle
inference. The RAG variants underperformed compared to
the simpler prompts, contradicting our expectation that more
context would result in more accurate assertions. This could
suggest that the LLM has limitations in effectively integrat-
ing complex structured data in this setting. It also suggests
that, while LLMs like GPT-4o benefit from richer natural
language context (as seen in the improvement from SP to
EP), they may not gain from structured data unless integrated
in a more intuitive or specialized way. While RAG shows
reasonable performance, it comes at a higher operational cost
compared to other variants. This highlights the trade-off users
must consider: choosing between superior model performance
and privacy assurance or managing costs while potentially
sacrificing some effectiveness.

<!-- Page 10 -->

An interesting observation from our results is that the
model occasionally generates natural language descriptions
of assertions instead of source code—though unintended, this
highlights the potential of LLMs for interpreting and explain-
ing code, warranting further exploration of such capabilities.
These findings underscore the need for developers and
organizations to carefully evaluate their priorities, whether
they lean towards performance, privacy, or cost-efficiency, in
selecting the most appropriate model for their software testing
needs. The flexibility of AugmenTest is aimed at supporting
developers in such situations.
E. Threats to Validity
Data Leakage. A potential threat to internal validity is the
possibility of data leakage, particularly with respect to the
LLMs used in our study. LLMs may have been pre-trained on
similar datasets, potentially leading to over-optimistic results
when generating test oracles. However, to mitigate this risk, we
carefully selected Java projects based on a different benchmark
and generated unique mutants that are unlikely to have been
seen by the model during pre-training. While this reduces the
chances of data leakage, it is impossible to entirely rule out
the influence of pre-training data on the results.
Mutant Generation Bias. Our evaluation relies on auto-
matically generated mutants to benchmark the correctness of
inferred assertions. These mutants, while useful for simulating
bugs, may not fully represent real-world software faults. This
introduces a potential bias in evaluating AugmenTest’s effec-
tiveness in real-world scenarios. Future work could involve
using a wider variety of bug benchmarks or real-world defects
to strengthen the internal validity of the approach.
Generalization. The external validity of our study is pri-
marily limited by the scope of the dataset, which consists
exclusively of Java projects. While our results demonstrate
AugmenTest’s ability to infer correct test oracles in this
context, it is unclear how well the approach would general-
ize to other programming languages or frameworks. Future
research should aim to evaluate AugmenTest on projects from
additional programming ecosystems, such as Python, C#, or
JavaScript, to assess the generalizability of the approach.
LLM Dependency. Another factor affecting generalizability
is the reliance on specific large language models, such as
GPT-4, used for assertion inference. The performance of
AugmenTest may vary across different LLMs, particularly
those with different architectures or training data. As new
models emerge, it will be important to assess whether the
observed performance improvements hold across a wider range
of LLMs and domains.
Evaluation Metrics. The success of our approach is primar-
ily measured by the accuracy of inferred assertions in passing
on the original class and failing on the mutant. While this is a
strong indicator of correctness, it does not fully capture other
aspects of a test’s effectiveness, such as the ability to detect
subtle, real-world bugs or maintainability of the generated
tests. Future work could focus on broadening the evaluation
metrics.
V. C ONCLUSION AND FUTURE WORK
In this paper we presented AugmenTest, an approach for
generating test oracles using large language models. Our
method demonstrates the effectiveness of leveraging context-
rich prompts to guide the LLM in generating assertions for au-
tomated tests. We evaluated our approach across four variants:
Simple Prompt, Extended Prompt, RAG with Generic Prompt,
and RAG with Simple Prompt. The results indicate that the Ex-
tended Prompt (EP) variant outperformed the Simple Prompt
(SP) variant, achieving an assertion correctness rate of 30%,
compared to 29.1% for SP considering the most conservative
scenario. However, the use of RAG (both RAG and RAG SP)
did not lead to the anticipated performance improvements,
with RAG yielding a lower correctness rate of 18.2%. This
suggests that while adding more contextual information im-
proves the quality of generated assertions, the retrieval-based
augmentation in RAG may require further optimization to
fully realize its potential. The results demonstrate the potential
of LLM-based test oracle generation in augmenting software
testing practices, reducing manual effort in writing assertions,
and improving the quality of automatically generated test
cases.
Despite these promising results, several areas for future
improvement remain. First, our method relies on syntactic
correctness and successful compilation to validate assertions
but lacks a formal assurance mechanism to verify the semantic
correctness of the generated oracles. Approaches like Assured
LLM-Based Software Engineering have explored assurance
layers to rigorously filter and validate LLM outputs before
they are accepted [21]. Incorporating a similar assurance
layer could improve the reliability of generated assertions,
ensuring they truly reflect the intended behavior of the system
under test. Moreover, we currently lack an assertion ranking
mechanism to prioritize more accurate or optimal assertions,
which has been explored in related works [4]. Developing such
a mechanism could further enhance the quality of generated
test cases. Moreover, our evaluation focused on Java projects,
and future work should explore applying the approach to
other programming languages and software domains. This
would allow us to assess the generalizability and scalability
of AugmenTest across diverse systems and testing scenarios.
Finally, future work could investigate the role of AI-generated
comments as a supplement to developer-written comments, as-
sessing how they influence the quality of generated assertions
and the overall performance of the approach. By analyzing
the synergy or redundancy between these comment types,
we could gain insights into optimizing prompt engineering
and improving the contextual understanding of large language
models in software testing.
ACKNOWLEDGMENT
We acknowledge the support of the PNRR project FAIR
- Future AI Research (PE00000013), under the NRRP MUR
program funded by the NextGenerationEU.

<!-- Page 11 -->

## References

[1] E. T. Barr, M. Harman, P. McMinn, M. Shahbaz, and S. Yoo, “The
oracle problem in software testing: A survey,” IEEE Transactions on
Software Engineering, vol. 41, no. 5, pp. 507–525, 2015.
[2] G. Fraser and A. Zeller, “Mutation-driven generation of unit tests
and oracles,” in Proceedings of the 19th international symposium on
Software testing and analysis , 2010, pp. 147–158.
[3] S. Yang, F. Chen, Y . Yang, and Z. Zhu, “A study on semantic
understanding of large language models from the perspective of
ambiguity resolution,” in Proceedings of the 2023 International Joint
Conference on Robotics and Artificial Intelligence , ser. JCRAI ’23.
New York, NY , USA: Association for Computing Machinery, 2024, p.
165–170. [Online]. Available: https://doi.org/10.1145/3632971.3632973
[4] E. Dinella, G. Ryan, T. Mytkowicz, and S. K. Lahiri, “Toga: a
neural method for test oracle generation,” in Proceedings of the 44th
International Conference on Software Engineering , ser. ICSE ’22.
New York, NY , USA: Association for Computing Machinery, 2022,
p. 2130–2141. [Online]. Available: https://doi.org/10.1145/3510003.
3510141
[5] S. M. Khandaker, F. Kifetew, D. Prandi, and A. Susi, “Augmentest:
Enhancing tests with llm-driven oracles - replication package,” 2024.
[Online]. Available: https://doi.org/10.5281/zenodo.13881826
[6] Elsevier, “Scopus.” [Online]. Available: https://www.elsevier.com/en-in/
solutions/scopus
[7] Z. Liu, K. Liu, X. Xia, and X. Yang, “Towards more realistic
evaluation for neural test oracle generation,” in Proceedings of the
32nd ACM SIGSOFT International Symposium on Software Testing
and Analysis , ser. ISSTA 2023. New York, NY , USA: Association
for Computing Machinery, 2023, p. 589–600. [Online]. Available:
https://doi.org/10.1145/3597926.3598080
[8] M. Tufano, D. Drain, A. Svyatkovskiy, and N. Sundaresan, “Generating
accurate assert statements for unit test cases using pretrained
transformers,” in Proceedings of the 3rd ACM/IEEE International
Conference on Automation of Software Test, ser. AST ’22. Association
for Computing Machinery, 2022, pp. 54–64. [Online]. Available:
https://dl.acm.org/doi/10.1145/3524481.3527220
[9] P. Nie, R. Banerjee, J. J. Li, R. J. Mooney, and M. Gligoric,
“Learning deep semantics for test completion,” in Proceedings of
the 45th International Conference on Software Engineering , ser.
ICSE ’23. IEEE Press, 2023, p. 2111–2123. [Online]. Available:
https://doi.org/10.1109/ICSE48619.2023.00178
[10] H. Yu, Y . Lou, K. Sun, D. Ran, T. Xie, D. Hao, Y . Li, G. Li, and
Q. Wang, “Automated assertion generation via information retrieval
and its integration with deep learning,” in Proceedings of the 44th
International Conference on Software Engineering , ser. ICSE ’22.
Association for Computing Machinery, 2022, pp. 163–174. [Online].
Available: https://dl.acm.org/doi/10.1145/3510003.3510149
[11] J. Shin, H. Hemmati, M. Wei, and S. Wang, “ Assessing Evaluation
Metrics for Neural Test Oracle Generation ,” IEEE Transactions
on Software Engineering , vol. 50, no. 09, pp. 2337–2349, Sep.
2024. [Online]. Available: https://doi.ieeecomputersociety.org/10.1109/
TSE.2024.3433463
[12] M. Sch ¨afer, S. Nadi, A. Eghbali, and F. Tip, “An empirical evaluation of
using large language models for automated unit test generation,” IEEE
Transactions on Software Engineering, vol. 50, no. 1, pp. 85–105, 2024.
[13] M. Tufano, D. Drain, A. Svyatkovskiy, and N. Sundaresan, “Generating
accurate assert statements for unit test cases using pretrained
transformers,” in Proceedings of the 3rd ACM/IEEE International
Conference on Automation of Software Test , ser. AST ’22. New York,
NY , USA: Association for Computing Machinery, 2022, p. 54–64.
[Online]. Available: https://doi.org/10.1145/3524481.3527220
[14] Y . Tang, Z. Liu, Z. Zhou, and X. Luo, “Chatgpt vs sbst: A
comparative assessment of unit test suite generation,” IEEE Trans.
Softw. Eng. , vol. 50, no. 6, p. 1340–1359, Mar. 2024. [Online].
Available: https://doi.org/10.1109/TSE.2024.3382365
[15] Z. Yuan, M. Liu, S. Ding, K. Wang, Y . Chen, X. Peng, and Y . Lou,
“Evaluating and improving chatgpt for unit test generation,” Proc.
ACM Softw. Eng. , vol. 1, no. FSE, Jul. 2024. [Online]. Available:
https://doi.org/10.1145/3660783
[16] Y . Chen, Z. Hu, C. Zhi, J. Han, S. Deng, and J. Yin, “Chatunitest: A
framework for llm-based test generation,” in Companion Proceedings
of the 32nd ACM International Conference on the Foundations
of Software Engineering , ser. FSE 2024. New York, NY , USA:
Association for Computing Machinery, 2024, p. 572–576. [Online].
Available: https://doi.org/10.1145/3663529.3663801
[17] M. Gruber, M. F. Roslan, O. Parry, F. Scharnb ¨ock, P. McMinn,
and G. Fraser, “Do automatic test generation tools generate flaky
tests?” in Proceedings of the IEEE/ACM 46th International Conference
on Software Engineering , ser. ICSE ’24. New York, NY , USA:
Association for Computing Machinery, 2024. [Online]. Available:
https://doi.org/10.1145/3597503.3608138
[18] S. B. Hossain, A. Filieri, M. B. Dwyer, S. Elbaum, and W. Visser,
“Neural-based test oracle generation: A large-scale evaluation and
lessons learned,” in Proceedings of the 31st ACM Joint European
Software Engineering Conference and Symposium on the Foundations
of Software Engineering , ser. ESEC/FSE 2023. New York, NY , USA:
Association for Computing Machinery, 2023, p. 120–132. [Online].
Available: https://doi.org/10.1145/3611643.3616265
[19] R. Just, D. Jalali, and M. D. Ernst, “Defects4j: a database of existing
faults to enable controlled testing studies for java programs,” in
Proceedings of the 2014 International Symposium on Software Testing
and Analysis , ser. ISSTA 2014. New York, NY , USA: Association
for Computing Machinery, 2014, p. 437–440. [Online]. Available:
https://doi.org/10.1145/2610384.2628055
[20] M. Tufano, S. K. Deng, N. Sundaresan, and A. Svyatkovskiy,
“Methods2test: a dataset of focal methods mapped to test cases,” in
Proceedings of the 19th International Conference on Mining Software
Repositories, ser. MSR ’22. New York, NY , USA: Association
for Computing Machinery, 2022, p. 299–303. [Online]. Available:
https://doi.org/10.1145/3524842.3528009
[21] N. Alshahwan, M. Harman, I. Harper, A. Marginean, S. Sengupta,
and E. Wang, “Assured offline llm-based software engineering,”
in Proceedings of the ACM/IEEE 2nd International Workshop on
Interpretability, Robustness, and Benchmarking in Neural Software
Engineering, ser. InteNSE ’24. New York, NY , USA: Association
for Computing Machinery, 2024, p. 7–12. [Online]. Available:
https://doi.org/10.1145/3643661.3643953
