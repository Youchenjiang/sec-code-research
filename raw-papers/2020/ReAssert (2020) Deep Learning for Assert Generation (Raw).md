# 24 ReAssert2020 ReAssert  Learning to Repair Broken Test

- **Source File**: [`24_ReAssert2020_ReAssert__Learning_to_Repair_Broken_Test.pdf`](file:///c:/Users/g1014/Documents/GitHub/Youchen/code-security-research/papers/24_ReAssert2020_ReAssert__Learning_to_Repair_Broken_Test.pdf)
- **Total Pages**: 12

---

<!-- Page 1 -->

REASSERT : Deep Learning for Assert Generation
Robert White
University College London
robert.white.13@ucl.ac.uk
Jens Krinke
University College London
j.krinke@ucl.ac.uk
Abstract—The automated generation of test code can reduce
the time and effort required to build software while increasing
its correctness and robustness. In this paper, we present R E-
ASSERT , an approach for the automated generation of JUnit test
asserts which produces more accurate asserts than previous work
with fewer constraints. This is achieved by targeting projects
individually, using precise code-to-test traceability for learning
and by generating assert statements from the method-under-test
directly without the need to write an assert-less test ﬁrst. We also
utilise Reformer, a state-of-the-art deep learning model, along
with two models from previous work to evaluate R EASSERT and
an existing approach, known as A TLAS , using lexical accuracy,
uniqueness, and dynamic analysis. Our evaluation of R EASSERT
shows up to 44% of generated asserts for a single project match
exactly with the ground truth, increasing to 51% for generated
asserts that compile. We also improve on the A TLAS results
through our use of Reformer with 28% of generated asserts
matching exactly with the ground truth. Reformer also produces
the greatest proportion of unique asserts (71%), giving further
evidence that Reformer produces the most useful asserts.
Index Terms—software engineering, software testing, test gen-
eration, machine learning
I. I NTRODUCTION
The process of creating and maintaining unit tests is time-
consuming, error-prone, and often disliked by developers,
frequently resulting in software that has a low level of test
coverage. Previous work has shown that to maintain a high
level of unit test coverage, the tests must be created at the
same time as the tested code as retroactively creating unit tests
is rarely done and only partially successful when attempted [1].
Therefore, by automating parts of the unit test creation process
we hope to improve the efﬁciency of the software engineering
process and the robustness of the resulting software. To achieve
this, we present REASSERT , an approach for generating JUnit
assert statements using deep learning.
Test suite generation tools such as EvoSuite [2], Randoop [3],
and AgitarOne [4] employ techniques that primarily focus on
generating high-coverage tests rather than meaningful asserts
and, therefore, the asserts they generate are often weak and lack
speciﬁcity. This problem contributes to the deﬁciencies these
tools show when attempting to revealing real-world faults [5],
[6].
To overcome the issues that existing test generation tech-
niques have with generating asserts, we turn to deep learning.
Previous work [7] investigated generating JUnit tests using a
sequence to sequence recurrent neural network (RNN) trained
on individual projects in an approach named TEST NMT. After
this, Watson et al. [8] used a similar RNN model in their ATLAS
approach, trained on a general corpus mined from GitHub for
generating just the assert statements for JUnit tests. These
previous works have demonstrated that this type of deep neural
network is capable of generating useful test code, however,
in the case of TEST NMT , the generated candidate tests need
some manual transformation before being usable and, in the
case in case of ATLAS , only 17% of the generated asserts were
exact matches with the ground truth when using the raw dataset
and the test (minus the asserts) was required to already been
written. In addition, only a single assert could be generated
for a given method and no analysis beyond lexical accuracy
was performed to assess the usefulness of the asserts.
Our approach, called REASSERT , builds on the previous
work by focusing on generating JUnit asserts, similar to Watson
et al. [8], but utilises a project-based approach that does not
require the (assert-less) test to be written before asserts can
be generated and allows for the generation of more than one
assert per tested method. REASSERT can use three different
models and includes the new Reformer model [9] in addition
to the two RNN models used in TEST NMT [7] and ATLAS [8].
Reformer utilises a state-of-the-art deep learning architecture
and may push the accuracy and usefulness of the generated
asserts beyond that of the previous models. All three models
are applied to both REASSERT and a re-implementation of
ATLAS , and we also expand the evaluation in two other ways to
focus more on real-world usefulness and applicability. Firstly,
we perform an extended lexical accuracy evaluation (how close
is the text of the generated asserts to the ground truth from
the test set) and an analysis of the uniqueness of the generated
asserts, which gives further evidence as to their usefulness.
Secondly, for REASSERT , we go beyond the static lexical
accuracy analysis, to use a dynamic analysis which determines
how many generated asserts compile and how many pass when
inserted into existing tests. By evaluating all three models
for both REASSERT and ATLAS with the uniqueness and
dynamic evaluation, along with the typical lexical evaluation,
we demonstrate which approach and model combinations are
the most useful in a real-world setting. The main contributions
of this paper are:
• REASSERT , a project-based deep learning approach for
the generation of unit test asserts implemented for JUnit.
• An evaluation of REASSERT using lexical accuracy and
dynamic analysis with Reformer, a new state-of-the-art
transformer-based model and two RNN-based models from
previous work.
arXiv:2011.09784v1  [cs.SE]  19 Nov 2020

<!-- Page 2 -->

• An extended comparative evaluation of all three models
using lexical accuracy and uniqueness on a previous
approach, ATLAS .
• Takeaway messages for researchers and practitioners
concerning the construction of data sets when applying
sequence to sequence learning for code generation.
II. B ACKGROUND
Test assert generation has previously been the domain of
test suite generation tools, such as EvoSuite [2], Randoop [3],
and AgitarOne [4]. However, these tools primarily generate
tests through methods that optimise for coverage, such as
genetic programming and random testing. Therefore, these
tools produce tests that aim primarily to achieve high coverage
rather than include meaningful assert statements, resulting in a
deﬁciency in the ability of these generated tests to detect real
faults. This was quantiﬁed in a study [5] which discovered that
neither EvoSuite, Randoop, or AgitarOne were able to detect
more than 40.6% of faults in the Defects4J [10] database. As
63.3% of the undetected faults were covered, this indicates
weaknesses in the asserts of the generated test cases.
With the advent of deep learning and the successful appli-
cation of deep learning techniques to tasks that require the
processing of sequential data, especially language-based tasks
such as machine translation [11]–[13], an opportunity to apply
these methods to source code was created. These deep learning
models have been applied to a wide range of software engineer-
ing problems such as code summarisation [14]–[16], program
comprehension [17], clone detection [18], code similarity [19],
method name generation [20], comment generation [21],
traceability [22], and type inference [23]. However, for the
task of code generation, deep learning models initially were
only applied to the generation of implementation code [24],
not test code. TEST NMT [7] applied these techniques to test
generation by utilising a sequence to sequence RNN-based
neural network, adapted from a model that had previously been
used for neural machine translation and applied it to translate
from Java methods to JUnit tests. TEST NMT demonstrated
that, when applied to large individual projects, this technique
is capable of generating some tests that only require a small
amount of manual effort on the part of the developers to turn
into useful tests. However, many tests still required a large
amount of effort to be converted and the approach was not
effective when using a single multi-project data set to train a
general model that works for any project. After TEST NMT ,
ATLAS [8] applied the same type of model to the problem of
generating test code, however, instead of attempting to generate
whole tests, ATLAS attempts only to generate the asserts for
JUnit test cases. This removes the issue of developers having to
expend a lot of effort to transform the output of the model into
usable code and also allows the training of a single network on
a corpus of general Java code to apply to any project. However,
unlike TEST NMT [7], ATLAS only uses tests with a single
assert statement and the test code (minus the assert) is included
in the source sequence, requiring that a developer writes a test
before using ATLAS , which can then only generate a single
assert. The model used by TEST NMT [7] and the model used
by ATLAS [8] are utilised in this work for a comparative
evaluation with R EASSERT and the Reformer model.
III. A PPROACH
The REASSERT approach, illustrated in Figure 1, facilitates
the generation of assert statements for a given method by
using deep neural network models trained on pairs of assert
statements and tested methods, extracted from existing test-to-
tested-method pairs. To train the model, we start by gathering
the test-to-tested-method pairs from a target project via test-to-
code traceability links [25]. Then, for each test-to-tested-method
pair, we extract the assert statements from the test method and
concatenate them to produce the string of assert statements
associated with the tested method. The tested method and
assert strings are then processed into input and output token
sequences, known as method sequences and assert sequences
respectively. These sequences are used to train the model.
Once trained, the model can be used to generate an assert
sequence, given a method sequence as input. The generated
assert sequences are then processed into syntactically correct
code that can be directly inserted into a test for that method.
Figure 2 illustrates an example from Stanford CoreNLP for how
REASSERT generates asserts for a new method by processing
the method into an input sequence, inferring over the trained
model, and processing the output sequence into syntactically
correct asserts. As the example shows, the generated assert
statements can easily be expanded into a test.
We speciﬁcally target our work more toward applicability
than previous work by ensuring that we do not apply any
ﬁltering or abstraction and we do not use any prediction
techniques that generate multiple outputs, such as beam search.
We also only use the training set to create the vocabulary
that is used when generating the method sequences and assert
sequences. This is to ensure, ﬁrstly, that we are evaluating in a
scenario that is true to real-world development and, secondly,
that we minimise the amount of work that a developer has to do
to utilise the produced assert statements in their code. Also, in
contrast to ATLAS , REASSERT does not include the test code
in the source sequence as this would require the developer
to have already written the test case (except for the assert
statements) before using REASSERT to generate asserts. As
we believe that the generated asserts should help the developer
to write the rest of the test, this is an important improvement
over prior work. Our use of tests which have multiple assert
statements is another improvement over ATLAS which only
uses tests that contain a single assert statement. We believe
this further increases R EASSERT ’s applicability.
A. Test-to-code Traceability Establishment
Given the code for a project, we ﬁrst need to extract the
test-to-code traceability links in order to build our training
and testing data sets. Establishing test-to-code traceability
links is an open research problem in software engineering
for which multiple different techniques have been developed.
Each technique has its own strengths and weaknesses, resulting

<!-- Page 3 -->

Project Source
Test Tested
MethodApply Relaxed NC
traceability
Tokenisation,
Assert extraction,
and OOV
replacement
Untested Method
Tokenisation and
OOV replacementUntested
Method
Sequence
Train
Asserts
Sequence
Generated
Assert Statements
Lexical processing
Training Inference
Model
Tested
Method
Sequence
Assert
Sequence
Tested
Method
Sequence
Assert
Sequence
Developer
Test-to-code traceability links Input/Output Training Examples
Test Tested
Method
Write Method
Fig. 1: Overview of the R EASSERT approach.
Tokenisation and OOV replacement
Developer
public List<Sentence> sentences(Properties props) {
return this.sentences(props, props == EMPTY_PROPS ?
defaultTokenize :
getOrCreate(Annotator.STANFORD_TOKENIZE, props,
() -> backend.tokenizer(props)).get());
}
assert Equals ( 2 , sentences . size ( ) ) ; assert Equals ( " the quick brown fox jumped over the lazy dog .
" , sentences . get ( 0 ) . text ( ) ) ; assert Equals ( " The lazy dog was not impressed . " , sentences . get (
1 ) . text ( ) ) ;
public List < Sentence > sentences ( Properties props ) { return this . sentences ( props , props = =
EMPTY _ <unk> ? default <unk> : get Or Create ( Annotator . STANFORD _ <unk> , props , ( ) - >
backend . tokenizer ( props ) ) . get ( ) ) ; }
Write method
Trained Model
Provide input sequence
Lexical processing
assertEquals(2, sentences.size());
assertEquals("theQuickBrownFoxJumpedOverTheLazyDog.",
sentences.get(0).text());
assertEquals("TheLazyDogWasNotImpressed.",
sentences.get(1).text());
Generate output sequence
@Test
public void testSentences() {
Document doc = new Document(
"the quick brown fox jumped over the lazy dog. The lazy dog
was not impressed.");
List<Sentence> sentences = doc.sentences();
assertEquals(2, sentences.size());
assertEquals("the quick brown fox jumped over the lazy dog.",
sentences.get(0).text());
assertEquals("The lazy dog was not impressed.",
sentences.get(1).text());
}
Test integration
Fig. 2: Example from the Stanford CoreNLP project demonstrat-
ing the R EASSERT process to generate asserts for a method.
in different balances between precision and recall [25], [26].
Finding the right balance of precision and recall is important
for building a data set for machine learning as if the precision
is too low, the data will have too much noise (incorrect links)
but if the recall is too low the data set will be too small to
effectively train from. In addition, the optimal precision versus
recall trade-off differs depending on which data set we are
constructing. When constructing the training set, we prefer
recall, however, for the validation set (used for conﬁguring
the parameters of the networks) and test set (used for the
evaluation) we prefer precision. This is due to the fact that
when we are training the model we want to ensure we have as
much data as possible, whereas, when we are evaluating the
model using the validation or test set, we want to ensure that
we are not evaluating the model with noisy data.
When training a model, we can tolerate some noise in the
data as we want to maximise the amount of data and, even if a
link is technically incorrect, we may still be able to learn some
useful structure from it. An example of this can be seen when
looking at tests for commonly overridden methods such as
equals or toString. In these cases, even if a link is incorrect, a
link between the test for the equals method of one class to the
equals method of a different but similar class, the network may
still learn some useful information about the general structure
of equals tests because most tests for equals methods tend to be
very similar. However, when we are evaluating the model, we
want to ensure that there are as few incorrect links as possible
as we don’t want to be evaluating the model by asking it
to generate something that is incorrect. Doing so will give
an inaccurate view of how well the model performs, usually
resulting in an underestimation of its accuracy.
Given the above concerns, we ﬁrstly want to ﬁnd a high
precision technique for building the validation and training sets.
Using the recent work by White et al. which compares the
precision and recall of multiple techniques [26], we selected
the naming conventions (NC) technique for building these data
sets as it has a precision of 100%. The naming convention
technique establishes links by taking the fully-qualiﬁed names
(FQNs) of both the tested method and the test method and
comparing them after the word test has been removed from
the test method name. If the names match exactly, the test
method is linked to the tested method. However, given the
very low recall of only 11%, this technique was not suitable
for building the training set so we created a variant of this
technique called “Relaxed NC” (we conversely call the standard
NC “Strict NC”). Relaxed NC utilises the same concept as
Strict NC but instead of performing the matching on the FQN,
the matching is performed only over the tested method and
test method name. Therefore, a link will still be created even
if the class name does not match the test class name. While
this will create some incorrect links, we can often still learn
some useful structure from these links (as described above)
and it gives us much more data to train on, which is critical,
especially for the smaller projects.
B. Data Set Construction
To build the data sets, we start by constructing all the Strict
NC and Relaxed NC links and place all the Relaxed NC links

<!-- Page 4 -->

into the training set. The Strict NC links are then split between
the validation set (used for conﬁguring the parameters of the
networks) and test set (used for the evaluation), up to the
maximum size of 100 links for each set. Any excess Strict NC
links are placed in the training set. As we want to ensure that
we are not unfairly biasing the model, we then ﬁlter out any
links from the training set that appear in either the validation
or the test sets. This ﬁltering can result in a large reduction
of the number of links in the training set, with the number
of links in the validation and test set greatly inﬂuencing the
magnitude of this reduction as the larger the validation and
test sets are, the more links will have to be removed from
the training set. Therefore, it is important to balance the sizes
of the sets so that each set has an adequate amount of links
to perform its function. This is why we limit the number
of links in the test and validation sets to 100. Now that we
have the links for each set we must process the links into
pairs of source sequences (from the tested methods) to target
sequences (from the tests). To do this we ﬁrst tokenise the
source for each artefact, build the vocabularies based on the
tokenised sequences, then replace out-of-vocabulary (OOV)
tokens with UNK. Our tokenisation process consists of stripping
all non-printing and non-alphanumeric characters that are not
used in Java, adding spaces around all programming language
characters, de-camelcasing identiﬁers and adding spaces around
the resulting tokens. This results in a sequence of individual
tokens consisting of the split identiﬁers and programming
language characters. At this stage the tested methods have
been fully tokenised into source sequences, however, for the
tests we want to keep only the assert statements so we add
another stage of processing for the tests where detect which
tokens are part of assert statements by checking for the ”assert”
token, ﬁnding the next opening parenthesis and its partner
closing parenthesis and treating all the tokens in-between as
being part of the assert statement. Any tokens that are not
determined to be part of an assert statement are deleted. This
results in a target sequence that is just the tokenised assert
statements for the test. It is important to note that unlike Watson
et al., we use tests that have multiple assert statements and
we add all of the assert statements in the test to the target
sequence. Once we have applied this process to all the code
snippets for the tested methods and the tests we have our sets
of input-output examples (source sequence to target sequence
pairs). We then build the source and target vocabularies by
collecting all the tokens in all the sequences and taking the
top n most frequent tokens, where n is the desired size of the
vocabulary. The vocabularies are then used to replace OOV
tokens in the sequences by replacing any token which does
not appear in the relevant vocabulary with UNK.
IV. M ODELS
To compare the performance of established and new models,
we selected a set of networks consisting of two that use a
traditional seq-to-seq architecture with recurrent neural network
(RNN) units [7], [8], and a more efﬁcient variant of the newer
Transformer architecture called Reformer [9]. All of these
models utilise the encoder-decoder with attention architecture
type where the encoder encodes the source sequence into
a vector representation which is then decoded into a target
sequence by the decoder. The attention mechanism allows for
modelling of out-of-sequence dependencies by attending over
the whole source sequence. This is the typical architecture
used for sequence to sequence learning tasks, such as neural
machine translation.
A. RNN models
The two RNN type models we use are ATLAS [8] and
TEST NMT [7]. For both of these models, the encoder builds
the vector representation of the source sequence by traversing
the sequence one token at a time converting each token into
a vector embedding via an embedding layer which is then
provided as input to the encoder RNN unit for that time step.
After the source sequence has been fully processed, the ﬁnal
hidden state of the encoder RNN is used to initialise the hidden
state of the decoder RNN. Then, at each time step, the decoder
RNN uses the current hidden state, the previously generated
target sequence token, and the attention mechanism, to generate
a new target sequence token. This continues until the end-of-
sequence token is generated.
The attention mechanism assists in determining the next
token by assigning attention weights to each of the tokens in the
source sequence, computing a context vector representing the
full attention, and combining them with the hidden state of the
decoder to compute the attention vector. The attention weight
αts for a given target token and source token is computed
by performing a normalised comparison between the target
hidden state ht and the source hidden state hs using the score
function:
αts = exp score(ht, hs)∑S
s′=1 exp score(ht, hs′)
These attention scores are used to compute the context vector
ct using a weighted sum ct = ∑
sαtshs and the attention
vector is computed by combining the context vector with the
current decoder hidden state at = tanh(Wc[ct; ht]).
The attention vector is then passed to the softmax layer to
generate the predicted target token. After decoding the target
token for the current step, the attention vector is passed to the
next step in the decoder to ensure that past attention information
is carried forward. This helps to capture contextual and out-of-
sequence dependencies by allowing the network to attend to
the source tokens in differing amounts as the target sequence
is generated.
While the ATLAS and TEST NMT networks both utilise this
same basic architecture, as shown in Figure 3a and Figure 3b,
and both utilise LSTM cells with the tanh activation function,
they do differ in several signiﬁcant ways. One major difference
is that the ATLAS network includes a copy mechanism [27]
that replaces UNK token predictions with a token from the
source sequence. In contrast, the TEST NMT network does not
use an UNK replacement mechanism. Another difference is
that the TEST NMT network uses two unidirectional layers

<!-- Page 5 -->

𝑎𝑡,4𝑎𝑡,2 𝑎𝑡,3𝑎𝑡,1Attention
weights
Context
vector
Attention
vector
𝑥1 𝑥2 𝑥3 </𝑠 > <s> 𝑦1 𝑦2 𝑦3
𝑦1 𝑦2 𝑦3 </𝑠 >
Copy
Mechanism
Copy
Mechanism
Copy
Mechanism
(a) ATLAS /RNN
𝑎𝑡,4𝑎𝑡,2 𝑎𝑡,3𝑎𝑡,1Attention
weights
Context
vector
Attention
vector
𝑥1 𝑥2 𝑥3 </𝑠 > <s> 𝑦1 𝑦2 𝑦3
𝑦1 𝑦2 𝑦3 </𝑠 > (b) T EST NMT /RNN
𝑥1 𝑥2 𝑥3 </𝑠 >
𝑦1 𝑦2 𝑦3 </𝑠 >
Encoder 1
Feed Forward
Encoder 2
Multi-head Self-Attention
Feed Forward
Multi-head Self-Attention
Multi-head Encoder-
Decoder Attention
Feed Forward
Decoder 1
Linear
Softmax
Decoder 2
Multi-head Self-Attention
Multi-head Self-Attention
Multi-head Encoder-
Decoder Attention
Feed Forward (c) Two-layer Transformer (simpliﬁed)
Fig. 3: Architecture of the three models.
in the encoder and two layers in the decoder, whereas the
ATLAS network uses a single bidirectional layer in the encoder
and two layers in the decoder. This difference between the
networks can provide some insight as to the relative effect
of the directionality of layers vs the number of layers. The
networks also differ in the way that attention is calculated.
ATLAS uses Bahdanau’s additive technique [28]:
score(ht, hs) = v⊤
a tanh(W1ht + W2hs)
TEST NMT uses Luong’s multiplicative style [29]:
score(ht, hs) = h⊤
t Whs
B. Reformer model
The Reformer model [9] is a less resource-intensive iteration
of the recently popularised Transformer model [30]. The
Transformer model differs from the RNN based models in
that it relies solely on attention and simple point-wise fully
connected feedforward network layers. The Transformer still
employs encoder-decode attention, however, it also utilises
another form of attention called multi-headed self-attention.
The Transformer architecture is comprised of a series of layers
stacked on top of each other where each layer contains an
encoder and a decoder. The source sequence is fed through each
encoder sequentially and the result is given to each decoder
along with the output from the previous decoder (if one exists).
The encoders and decoders are themselves comprised of sub-
layers with the encoders containing multi-head self-attention
and feedforward sub-layers, while the decoders contain multi-
head self-attention, multi-head encoder-decoder attention, and
feedforward sub-layers. The output from the ﬁnal decoder
passes through a single linear layer and into the softmax to
compute the output token predictions. Figure 3c shows a high-
level example of a two-layer Transformer architecture.
The multi-headed attention mechanism works to improve
performance by allowing the model to attend to information
from multiple different representation subspaces concurrently,
enhancing the model’s ability to focus on different positions.
This is done by projecting the information from the input
vectors h times, where h is the number of heads, performing
the attention calculations over each head, and then combining
the results from all heads. All heads are initialised randomly
Transformer (ResNet) Encoder
Reformer (RevNet) Encoder – Forward pass
𝑥1
Multi-head Self-Attention
⊕
Feed Forward
⊕
𝑦1
𝑦2
𝑥1
Multi-head Self-Attention
Feed Forward
𝑦2
𝑥2
⊕
𝑦1
⊕
Reformer (RevNet) Encoder – Reverse Pass
𝑥1
Multi-head Self-Attention
Feed Forward
𝑦2
𝑥2
⊝
𝑦1
⊝
Fig. 4: Residual Network (ResNet) units (used in Transformer)
vs Reversible Network (RevNet) units (used in Reformer).
and trained with random dropout so that different heads learn
to attend more appropriately over different positions, making
the combination of multiple heads more effective than a single
attention function.
However, although Transformers achieve state-of-the-art per-
formance they can be very resource-intensive due to the extreme
number of parameters and the size of the calculations required
for multi-head attention. Given this limitation, the Reformer
model was created to reduce the resource requirements of
the model while still applying the concepts that make the
Transformer effective. To do this, Reformer targets the three
main sources of resource consumption in the Transformer,
speciﬁcally the large self-attention computation, which is OL2
for sequences of length L, the large numbers of layers, and
that the feedforward layers are often much deeper than the
attention activations. The Reformer deals with the size of the
attention computation by employing Locality Sensitive Hashing
(LSH) attention and deals with the large number and depth of
layers by using a Reversible Residual Network (RevNet) [31]
with chunking. However, as the current implementation of the
Reformer [32] does not use LSH attention for encoder-decoder
sequence to sequence tasks (only decoder-only language
models), we omit discussion of LSH here and focus on RevNet
and chunking.
RevNet improves the memory consumption of the model

<!-- Page 6 -->

TABLE I: Subject project details.
Project Version Set Sizes
Training Validation Test
Apache OpenNLP 1.9.1 2027 66 66
DL4J 1.0.0 2122 67 68
EJML 0.38 26 999 100 100
ND4J 1.0.0 5728 49 50
Stanford CoreNLP 3.9.2 3930 100 100
by replacing the Residual Network (ResNet) units of the
standard Transformer with RevNet units. This reduces memory
consumption as ResNet units need to store all of the activations
for each layer in memory for the backpropagation calculations,
requiring a lot of space when using deep networks. RevNet
units, however, can recover the activations in the nth layer from
the activations in the (n+1)th layer, meaning only the activations
from one layer need to be stored at any time. Figure 4 provides
an example of this by comparing a Transformer encoder with
ResNet units and a Reformer encoder with RevNet units. In
traditional transformers, the self-attention and feedforward sub-
layers are each contained in their own ResNet units and require
that all the activations be stored. However, in the Reformer,
the self-attention and feedforward layers are wrapped together
in a single RevNet unit where the input (activations from the
previous layer) can be recovered from the outputs (activations
from the current layer).
The ﬁnal improvement is using chunking in the feedforward
sub-layers. Improving the efﬁciency of these layers is important
as the dimensionality of the vectors in these layers can reach
4K or higher. Chunking can be used because the computations
are independent across the positions in a sequence, meaning
that the computation can be split into n chunks which are
executed in series, reducing memory requirements.
By using this combination of efﬁciency improvements,
the Reformer can achieve performance on par with that of
traditional large Transformers while being much more memory-
efﬁcient and faster, especially on large sequences.
V. E VALUATION – REASSERT
We evaluate the REASSERT approach using the two RNN-
based models from TEST NMT [7] and ATLAS [8] in addition
to the new Reformer model [9]. The projects that we selected
to perform the evaluation are Apache OpenNLP [33], Deep
Learning for Java (DL4J) [34], Efﬁcient Java Matrix Library
(EJML) [35], ND4J [36], and Stanford CoreNLP [37]. These
projects are well-tested, widely used, and include two natural
language processing libraries (Apache OpenNLP and Stanford
CoreNLP), two linear algebra libraries (EJML and ND4J), and
one deep learning library (DL4J). The details of the data sets
obtained from these projects are given in Table I.
The evaluation of REASSERT is split into two research
questions which collectively evaluate the usefulness of the
generated asserts by performing a lexical accuracy and a
dynamic analysis over individual asserts and the applicability
of these asserts to the test suites of the projects.
A. Research Question 1 (Assert Accuracy)
How many of the generated asserts are exact matches,
passing, and compiling? In RQ1 we examine the effectiveness
of REASSERT at generating individual asserts when paired
with each of the three models. We perform an analysis on the
generated asserts that ﬁrst establishes which are exact matches
(the generated assert exactly matches an assert written by the
developers), then which of the remaining asserts compile and
which of those then pass when used to replace the developer
written asserts in the existing test.
a) Experimental Setup: To evaluate REASSERT , we ﬁrst
take each test-to-tested-method pair from the test set, provide
the tested method as input to the model, get the output sequence,
process the output sequence into syntactically correct assert
statements, and compare those statements to those given in
the test method. Where a generated assert exactly matches any
assert in the test, we mark it as an exact match (and therefore
also as passing and compiling). We can automatically categorise
exact matches in this way as the test suites are fully green
(have no failing tests) for all of the projects. For generated
asserts that are not exact matches, we take the test from the
pair, remove all existing asserts from the test method, insert
the non-matching assert at the end of the test method, attempt
to compile and, if compilation is successful, run the test to see
if it passes. We repeat this process for all test-to-tested-method
pairs in the test sets of all the projects.
b) Findings: The results, presented in Table II, show that,
in general, the three models perform similarly. However, there
are some noticeable trends, such as the TEST NMT model being
slightly higher for F1 score in most projects and the Reformer
model being slightly lower in some projects (precision, recall,
and F1 scores are for exact matches only). Note that in most
cases, there are more asserts that pass than asserts that are
exact matches and there are more asserts that compile than
asserts that pass (i.e., there are some asserts generated that
compile, but where the test fails). A discussion exploring the
implications of these results can be found in Section VII-A.
B. Research Question 2 (Test Applicability)
What percentage of tests contain at least one assert from
the categories? In RQ2 we perform an analysis that uses the
generated asserts from RQ1 where, for each assert category
(exact match, passing, compiling), we determine the percentage
of tests that have at least one generated assert from that category.
This is to give evidence as to how useful the generated asserts
are across a whole test suite.
a) Experimental Setup: To answer this research question,
we use the asserts generated for RQ1 and, for each category,
count the percentage of tests in each project that contains at
least one assert from that category.
b) Findings: The results, presented in Table III, show
that in the best case, using the TEST NMT model, nearly half
of the tests in a project receive a generated assert that at least
compiles (Stanford CoreNLP). On average, a third of tests
receive at least one generated assert that compiles and 28%
receive at least one exact match assert. When comparing models

<!-- Page 7 -->

TABLE II: RQ1 – Exact match, passing, and compiling asserts.
Apache
OpenNLP DL4J EJML ND4J Stanford
CoreNLP
TEST NMT /RNN
Gen. Asserts 173 191 179 118 236
Matches 45 39 51 10 103
Precision (%) 26 20 28 15 44
Recall (%) 21 13 27 5 30
F1 23 16 27 7 35
Passing 47 40 61 10 108
Passing (%) 27 21 34 15 46
Compiling 47 44 69 10 120
Compiling (%) 27 23 39 15 51
ATLAS /RNN
Gen. Asserts 150 111 184 96 197
Matches 47 21 45 9 85
Precision (%) 31 19 24 9 43
Recall (%) 22 7 24 4 25
F1 26 10 24 6 31
Passing 47 21 53 14 87
Passing (%) 31 19 29 22 44
Compiling 47 28 63 14 100
Compiling (%) 31 25 34 22 51
Reformer
Gen. Asserts 192 217 212 132 271
Matches 30 17 38 8 88
Precision (%) 16 8 18 6 32
Recall (%) 15 6 20 4 25
F1 15 7 19 5 29
Passing 30 17 49 9 98
Passing (%) 16 8 23 7 36
Compiling 31 26 61 9 110
Compiling (%) 16 12 29 7 41
TABLE III: RQ2 – Percentage of tests with at least one
generated assert that is an exact match, passing, or compiling.
Apache
OpenNLP DL4J EJML ND4J Stanford
CoreNLP
TEST NMT /RNN
Matched 26% 27% 29% 20% 40%
Passing 27% 28% 32% 20% 44%
Compiling 27% 31% 37% 20% 49%
ATLAS /RNN
Matched 26% 12% 32% 18% 40%
Passing 26% 12% 37% 22% 40%
Compiling 26% 18% 42% 22% 44%
Reformer
Matched 17% 13% 28% 16% 41%
Passing 17% 13% 33% 18% 45%
Compiling 18% 21% 38% 18% 48%
the performance is similar but, like RQ1, the Reformer model
is slightly lower in some projects than the two RNN models
TEST NMT and A TLAS .
VI. E VALUATION – ATLAS
We present our evaluation of the three models using ATLAS
to determine if we can improve over previous results using
the new Reformer model or the TEST NMT model. ATLAS
signiﬁcantly differs from REASSERT in two aspects: (a) ATLAS
uses the tested method and the test method for training and
querying and (b) ATLAS uses a very simple and imprecise test-
to-code traceability technique. However, it has been applied
in a multi-project setting in which the corpus is created from
a large number of projects. To construct the data set, Watson
et al. mined 9,275 projects from GitHub and used the Spoon
library [38] to extract the test methods by looking for the @Test
annotation. However, any test that contained more than one
assert statement or was longer than 1000 tokens was discarded,
leaving 188,154 tests in total.
The traceability technique used by Watson et al. [8] in ATLAS
is a simpliﬁed version of Last Call Before Assert (LCBA) [25].
Instead of using a static or dynamic call graph, ATLAS simply
extracts the name of the last called method before the assert
and then searches the package for methods of the same name.
If no match can be found, ATLAS extends the search to the
whole project. While having the beneﬁt of being able to be used
on a large and diverse corpus, this method for establishing test-
to-code traceability links can result in a lot of noise in the data.
The noise can be especially bad if there are multiple classes
which deﬁne methods with the same names or if there are a
lot of overloaded methods. After establishing the links, ATLAS
processes them into input-output examples by extracting the
asserts from the tests to use as the outputs with their respective
tested methods as the inputs. Further ﬁltering is then performed
on the resulting data set to remove duplicate examples and any
example where the assert contains a token that does not appear
in the vocabulary. The data set provided by Watson et al. is
already ﬁltered, so our evaluation uses the data set directly
without mining or extraction.
The evaluation of the three models using ATLAS is split
into three research questions which collectively evaluate the
usefulness of the generated asserts by looking at the accuracy
(RQ3 and RQ4) and uniqueness (RQ5) of the generated asserts.
A. Research Question 3 (Assert Accuracy)
How many of the generated asserts are exact matches
for developer written asserts? For RQ3 we examine the
effectiveness of our three models at generating exact match
asserts, similar to RQ1, but in the ATLAS setting. The evaluation
is limited to exact matches as performing a dynamic analysis
to discover passing or compiling non-matched asserts is not
possible with Watson et al.’s data set. We do not use beam
search when applying the ATLAS model as it results in multiple
tokens being predicted for the same position in the output
sequence. Therefore, when it is utilised in the same way as
Watson et al. and all of the predicted tokens are used to build
a list of possible outputs, the output of the model is a set of
candidate assert recommendations rather than a single assert.
a) Experimental Setup: To answer RQ3, we use the model
to generate an assert for each test-to-tested-method pair in the
test set and compare the generated assert to the assert from
the test as present in the data set. Where the generated assert
and the test assert match, we count it as an exact match and
use the number of exact matches divided by the total number
of generated asserts to calculate the precision.
b) Findings: The results, as shown in Table IV, reveal
that TEST NMT is the worst-performing model with only 7%
precision. While ATLAS fairs much better than TEST NMT

<!-- Page 8 -->

TABLE IV: RQ3 – Exact match asserts.
TEST NMT /RNN ATLAS /RNN Reformer
Generated Asserts 18 817 18 817 18 817
Matched Asserts 1355 3323 5262
Accuracy 7% 18% 28%
with 17% precision, Reformer is the best by a wide margin
at 28% precision. Note that our results of 3323 exact matches
for our reimplementation of ATLAS is identical to the results
reported by Watson et al. [8], giving us conﬁdence that our
reimplementation is faithful to the original ATLAS . Discussion
regarding these results can be found in Section VII-A.
B. Research Question 4 (Edit Distance Evaluation)
How far from exact matches are non-matched asserts? RQ4
investigates how much transformation, measured in absolute
and relative token-based edit distance, is required to turn non-
exact match asserts into exact matches. These measures give
evidence as to how useful non-matched asserts are to developers
as, intuitively, the easier it is to turn a non-exact match assert
into an exact match, the more useful that assert would be for
developers. We use the relative edit distance as we want to take
the length of the asserts into account to avoid favouring models
that are more likely to produce short asserts. Discussions
relating to the length of generated asserts can be found in
Section VII-B. We also report the count of asserts that are less
than two token changes away from being a matched assert.
This group, therefore, includes asserts that are either exact
matches or only one token change away from an exact match.
Given the ease of changing a single token, we consider these
non-matched asserts to be in the group of asserts which should
be of most use to developers.
a) Experimental Setup: This evaluation is performed
using the asserts generated for RQ5. First, we ﬁnd the edit
distance by computing the Levenshtein distance between the
generated assert and each developer written assert, using tokens
instead of characters as the atomic unit, and take the smallest
distance. The distance is then used to compute the relative
edit distance by dividing it by the number of tokens in the
assert with the most tokens out of the generated assert and the
developer written assert.
b) Findings: The results, as shown in Table VI reveal
that the ATLAS and Reformer models perform essentially
equivalently to each other in edit distance, with the TEST NMT
model trailing behind them. However, when looking at asserts
that are less than 2 token changes away from an exact match,
the Reformer model has a clear advantage.
C. Research Question 5 (Uniqueness Evaluation)
What is the uniqueness of generated asserts? RQ5 investi-
gates how unique the generated asserts are, which is important
as the more unique an assert is, the more useful it is likely to
be. This belief is driven by the fact that, in general, asserts that
are more unique are more likely to encode speciﬁc information
about the task. For example, an assert statement that simply
TABLE V: RQ4 – Exact match edit distance evaluation.
TEST NMT /RNN ATLAS /RNN Reformer
Median Edit Dist. 5 2 2
Mean Edit Dist. 5.07 3.85 4.00
Median Rel. Edit Dist. 0.28 0.15 0.15
Mean Rel. Edit Dist. 0.26 0.18 0.19
Dist. < 2 Count 3375 6984 8180
Dist. < 2 (%) 18% 37% 43%
checks the equality of two generically named variables contains
less speciﬁc information than an assert statement which contains
method calls. We use the asserts generated by each of the three
models only with the Watson et al. data set because this data
set is taken from a large number of projects and, therefore,
demonstrating the ability to generate a diverse and unique
range of asserts is important.
To evaluate uniqueness, we ﬁrst look at the absolute number
of unique asserts the models produce and what percentage
of generated asserts were unique at generation time for all
generated asserts and all matched asserts. This measures how
frequently the models are generating unique asserts. However,
we do not only want to look at unique asserts but also the
distribution of non-unique asserts. We perform this analysis
with a view that a more even distribution, in general, indicates
a greater diversity of asserts and, therefore, greater useful
informational content. This assumption is discussed in more
detail in Section VII-B. To assess the distribution of non-unique
asserts, we compute the absolute number and percentage of
matched asserts that are among the top ﬁve and top ten most
common asserts, essentially showing us how common the
most common asserts are. To demonstrate a good ability to
generate asserts with a high degree of uniqueness, we are
looking for a model to maximise the unique assert percentages
while minimising the most common assert percentages.
a) Experimental Setup: To conduct RQ5, for each model,
we ﬁrst take the list of assert statements generated by the model
and group identical asserts together. The sizes of these groups
give us the count of how many times each assert appears. We
take the number of groups as our count of distinct asserts and
calculate this as a percentage of all the generated asserts. This
is the percentage of asserts that were unique at the time of
generation. The groups are then ordered by their cardinalities
and we take the sum of the cardinalities of the top ﬁve and the
top ten largest groups and use these to calculate the percentage
of generated asserts that are members of these groups.
b) Findings: The results, as shown in Table VI reveal that
Reformer is the best model for uniqueness as it has the highest
percentages of unique asserts and the lowest percentages of
asserts that are among the top 5 and top 10 most common
asserts. These results show Reformer is better for uniqueness
than the next best model, ATLAS , by a sizeable margin in all
measures. The TEST NMT model performs poorly as it rarely
generates unique asserts. Discussion regarding these results
can be found in Section VII-B.

<!-- Page 9 -->

TABLE VI: RQ5 – Assert uniqueness analysis results.
TEST NMT /RNN ATLAS /RNN Reformer
Unique Asserts 470 11 496 13 331
Unique Asserts (%) 2% 62% 71%
Unique matched 97 948 2647
Unique matched (%) 7% 29% 50%
Top 5 matched (%) 59% 25% 16%
Top 10 matched (%) 71% 37% 20%
VII. D ISCUSSION
We discuss the ﬁndings of the research questions and other
subjects relating to our methodology and outcomes. The topics
of assert accuracy (RQ1 – RQ4) and assert uniqueness (RQ5)
are of particular interest as they constitute the primary ways
in which we assess the usefulness of the generated asserts.
In addition, there are important takeaway messages regarding
the practicalities of applying this general approach to code
generation tasks, both in research and in industrial practice.
A. Assert Accuracy
Assessing the accuracy of the generated asserts by comparing
to a ground truth test set is the primary method for evaluating
assert generation techniques as it shows us how similar the
generated asserts are to developer written asserts. Given the
assumption that developers write useful asserts, this gives direct
evidence for the usefulness of the generated asserts.
For RQ1 we use the precision and recall as our measure for
accuracy which shows that the accuracy achieved byREASSERT
is heavily dependant on the project it is applied to. In the best
case of our experiments, using the TEST NMT model with
Stanford CoreNLP, the accuracy is greater than what is achieved
in the best case with ATLAS , using the Reformer model.
However, when using the ND4J project, the accuracy is lower.
Despite this, when taking the RQ2 results into consideration,
we see that even for the worst-performing project, ND4J, we
still have 20% of tests receiving at least one exact match assert.
When using the accuracy to compare models within the
ATLAS approach, in RQ3 we see that the Reformer model with
5262 matched asserts is 58% more accurate than the ATLAS
model with 3323 matched asserts, the next best performing
model, while the TEST NMT model is far behind with only
1355 matched asserts. The poor performance of TEST NMT
is due to its lack of an UNK replacement mechanism which
results in an UNK token appearing in 80% of the asserts
it generates. As any assert which contains an UNK token
cannot be matched, the accuracy of the model is very poor.
This is one of the primary ways in which the ATLAS model
differs from the TEST NMT model in that it implements a
copy mechanism that replaces UNK token predictions with
a token from the source sequence, the effects of which are
seen in these results. RQ1 paints a different picture in terms of
the comparisons between models when using the REASSERT
approach. This that shows that all the models are close to
each other in general but where there are larger differences,
the ordering from RQ1 is typically reversed, with TEST NMT
coming in ﬁrst and Reformer coming in last. The reasons for
TABLE VII: Top 5 most common matched asserts across all
models.
Assert Count
assertEquals(expected, actual) 1288
assertEquals(expResult, result) 419
assertEquals(expected, result) 337
assertTrue(true) 253
assertNotNull(result) 181
TABLE VIII: Top 5 most common matched asserts containing
a method call.
Assert Count
assertEquals(0, result.size()) 172
assertTrue(getNoErrorMsg(), result) 59
assertEquals(0, meldingen.size()) 57
assertEquals(200, response.getStatusCode()) 38
assertEquals(”test”, echo.echo(”test”)) 26
this are two-fold. Firstly, it seems that the accuracy of the
models is ultimately being bottlenecked by the quantity and
diversity of training data. Given that the amount of training
data that can be extracted from a single project is limited, there
are a proportion of asserts appearing in the test set that bare
no resemblance to any assert in the training set and, therefore,
will never be able to be replicated by any model. Given this,
it seems that TEST NMT may be the best model at learning
and recreating a restricted set of asserts that appear frequently,
while Reformer is better at generalising when given a more
diverse data set. This would explain the differences between
these models when comparing the RQ1 and RQ3 results. The
subject of the effect of data sets on the performance of the
models is discussed further in Section VII-C.
The takeaway message from these RQs is that the best
performing model is dependent on the usage scenario. If
generating asserts for a project that has a data set that is
conducive to sequence to sequence learning, REASSERT with
a TEST NMT model is the best performing with up to 44%
precision and the ability to generate at least one matching
assert for up to 40% of tests with the projects we used in the
evaluation. Otherwise, when using the ATLAS approach, the
Reformer model may be the best choice.
B. Assert Uniqueness
In RQ5, we performed a uniqueness evaluation on the
generated asserts to provide more evidence for how useful
the asserts are in practice. This was done as uniqueness is an
indicator of speciﬁcity and the more speciﬁc information an
assert contains, the more useful that assert is likely to be to
in practice. Therefore, we use uniqueness as a partial proxy
for evaluating usefulness. The intuition behind this evaluation
is clear when inspecting the least unique (most commonly
generated) asserts, as shown in Table VII. This demonstrates
how the most common asserts are extremely generic and
provide almost no speciﬁc information to the developers as
they simply compare values of generically named variables. In
the extreme case, as exempliﬁed by the fourth most common

<!-- Page 10 -->

assert, assertTrue(true), the assert is of no use at all and has
been learnt from developers writing a placeholder assert into
their tests (which is considered bad practice). As a comparison,
if we look at the top ﬁve most common generated asserts
that contain a method call, as shown in Table VIII we see
that, while still somewhat generic, these asserts contain more
speciﬁc information for how to test the tested method. This
comparison highlights how uniqueness relates to speciﬁcity,
which in turn relates to practical usefulness. We, therefore,
favour models which generate the greatest diversity of asserts.
Given that Reformer produces more unique asserts and has
a lower percentage of its asserts belonging to the top 5 and
top 10 most common asserts as compared to ATLAS in the
evaluation for RQ5, Reformer is the most desirable model in
this regard. TEST NMT performs poorly in this evaluation for
the same reason as its poor performance in accuracy, namely
that the lack of an UNK replacement mechanism limits the
range of matched asserts that it can produce. The takeaway
message is that the use of a state of the art model like Reformer
can improve the usefulness of the generated asserts due to the
higher uniqueness of the asserts.
C. Data Set Size, Diversity, and Quality
As discussed in Section VII-A, we see a surprising result
when we compare the accuracy between models when using
REASSERT versus when using ATLAS , in that the models
perform much more similarly with REASSERT . This indicates
that some of the projects selected for the REASSERT evaluation
produce data sets that do not allow all the models to generalise
maximally, most likely due to insufﬁcient size, low diversity,
or too much noise. This is an important takeaway for those
wishing to use these code generation techniques in the future
as these properties are determined not just by the size of the
projects from which the data is taken but also by the traceability
technique used to establish the test-to-tested-method links, the
ﬁltering that is applied to the data sets, and the way the code is
written. This diversity of concerns is evident when investigating
the relationship between data set sizes and performance. In
this regard, it’s important to note that the project with the
largest data set (EJML) is only the second-best performing
project in terms of F1 score in RQ1 with the Reformer model
(and third-best with the RNN models), while the project that
performs best for F1 score with all models (Stanford CoreNLP)
has only the third largest data set. This shows that the size,
diversity, and quality of the data set has a large impact and, for
projects of this size, ultimately limits the ability of the models
to generalise. The takeaway message, therefore, is that it is
crucial to select a corpus of software that is large and diverse
and that appropriate techniques which balance data set size
and accuracy must be selected.
VIII. T HREATS TO VALIDITY
The threats to validity are related to the data used for training
and evaluating the models, both in terms of subject selection
and the method of data set collection. An external threat to
validity is the representativeness of the subjects chosen for
the REASSERT evaluation, as we have no strong evidence
that the subjects are representative of the general population
of software. However, the subjects cover a range of project
types, are widely used in research and industry, and are large
enough to demonstrate applicability to complex software. The
second threat comes from the method by which the data was
collected as the traceability techniques used to build the test-to-
tested-method links do not have complete precision and there
is, therefore, some noise in the data. However, as discussed
in Section III-A, we believe that having some noise in the data
does not necessarily signiﬁcantly hamper the training. For the
individual project data sets, we ensure that the validation and
test sets contain minimal noise by using a very high precision
traceability technique for constructing those sets. However,
when using multi-project data sets, such as in the ATLAS
evaluation, the results may vary if using a data set with a
signiﬁcantly different amount of noise in the data sets.
IX. R ELATED WORK
Prior to the application of the machine learning techniques
that are the subject of this paper, assert generation was done
primarily by test suite generation tools. These tools can be split
into several categories depending on the general approach used
for the generation of their tests. Randoop [3], Nighthawk [39],
JCrasher [40], and CarFast [41] are the primary examples
of tools that use approaches based on random generation
while EvoSuite [2] and eToc [42] are examples of meta-
heuristic search-based tools and Symbolic Pathﬁnder [43] and
jCUTE [44] are examples of tools that use dynamic symbolic
execution. However, despite the diversity of approaches to test
generation employed by these tools, they all focus primarily
on things other than the generation of meaningful asserts. The
usual goal for these tools is achieving coverage or exposing
faults in other ways, such as generating exceptions and crashes.
Therefore, even the most well developed and studied examples
of these tools which do have some form of assert generation,
such as EvoSuite and Randoop, the asserts they generate are
often trivial or not meaningful, contributing to the relatively
high rate of missed faults in real-world projects [6].
X. C ONCLUSION
We have presented REASSERT , a project-based deep learning
approach for the generation of JUnit test asserts. We also utilise
the state-of-the-art Reformer model and two RNN-based models
from previous work to evaluate REASSERT and provide an
extended evaluation of ATLAS , allowing us to compare models
and approaches for assert generation. REASSERT improves over
previous work by generating asserts that are, in general, more
accurate and does not require that a test be written before being
able to generate asserts, in addition to being able to generate
multiple asserts for a single function. Also, the Reformer model
is shown to improve the results achievable by the ATLAS
approach [8] generating asserts that are more accurate and
more unique. However, when the Reformer model is used with
REASSERT , the difference in effectiveness between the models
is greatly lessened. This indicates that some of the projects

<!-- Page 11 -->

selected for the REASSERT evaluation produce data sets that
do not allow all the models to generalise maximally, most
likely due to insufﬁcient size, low diversity, or too much noise.
Therefore, researchers and practitioners must be aware of this
limitation and select code corpora and traceability techniques
that provide suitably large, diverse, and clean data sets.

## References

[1] C. Klammer and A. Kern, “Writing unit tests: It’s now or never!”
in 2015 IEEE Eighth International Conference on Software Testing,
Veriﬁcation and Validation Workshops (ICSTW). IEEE, apr 2015, pp.
1–4. [Online]. Available: http://ieeexplore.ieee.org/document/7107469/
[2] G. Fraser and A. Arcuri, “Whole Test Suite Generation,” IEEE
Transactions on Software Engineering , vol. 39, no. 2, pp. 276–291, feb
2013. [Online]. Available: http://ieeexplore.ieee.org/document/6152257/
[3] C. Pacheco and M. D. Ernst, “Randoop: feedback-directed random
testing for Java,” in Companion to the 22nd ACM SIGPLAN conference
on Object oriented programming systems and applications companion
- OOPSLA ’07 , vol. 2. New York, New York, USA: ACM Press,
2007, p. 815. [Online]. Available: http://portal.acm.org/citation.cfm?
doid=1297846.1297902
[4] A. T. P. J. to the Test. Automated JUnit Generation. [Online]. Available:
http://www.agitar.com/solutions/products/agitarone.html
[5] S. Shamshiri, “Automated unit test generation for evolving software,”
2015 10th Joint Meeting of the European Software Engineering Confer-
ence and the ACM SIGSOFT Symposium on the Foundations of Software
Engineering, ESEC/FSE 2015 - Proceedings , pp. 1038–1041, 2015.
[6] S. Shamshiri, R. Just, J. M. Rojas, G. Fraser, P. McMinn, and
A. Arcuri, “Do Automatically Generated Unit Tests Find Real Faults?
An Empirical Study of Effectiveness and Challenges,” in 2015
30th IEEE/ACM International Conference on Automated Software
Engineering (ASE). IEEE, nov 2015, pp. 201–211. [Online]. Available:
http://ieeexplore.ieee.org/document/7372009/
[7] R. White and J. Krinke, “Testnmt: Function-to-test neural machine
translation,” in Proceedings of the 4th ACM SIGSOFT International
Workshop on NLP for Software Engineering , ser. NL4SE 2018. New
York, NY , USA: Association for Computing Machinery, 2018, p. 30–33.
[Online]. Available: https://doi.org/10.1145/3283812.3283823
[8] C. Watson, M. Tufano, K. Moran, G. Bavota, and D. Poshyvanyk, “On
Learning Meaningful Assert Statements for Unit Test Cases,” in 42nd
International Conference on Software Engineering (ICSE ’20), May
23–29, 2020, Seoul, Republic of Korea , 2020.
[9] N. Kitaev, Ł. Kaiser, and A. Levskaya, “Reformer: The efﬁcient
transformer,” arXiv preprint arXiv:2001.04451 , 2020.
[10] R. Just, D. Jalali, and M. D. Ernst, “Defects4J: a database
of existing faults to enable controlled testing studies for Java
programs,” in Proceedings of the 2014 International Symposium on
Software Testing and Analysis - ISSTA 2014 . New York, New
York, USA: ACM Press, 2014, pp. 437–440. [Online]. Available:
http://dl.acm.org/citation.cfm?doid=2610384.2628055
[11] N. Kalchbrenner and P. Blunsom, “Recurrent continuous translation
models,” in Proceedings of the 2013 Conference on Empirical Methods
in Natural Language Processing , 2013, pp. 1700–1709.
[12] I. Sutskever, O. Vinyals, and Q. V . Le, “Sequence to Sequence Learning
with Neural Networks,” Mathematical Programming , vol. 155, no.
1-2, pp. 105–145, sep 2014. [Online]. Available: http://papers.nips.
cc/paper/5346-sequence-to-sequence-learning-with-neuralhttp://link.
springer.com/10.1007/s10107-014-0839-0http://arxiv.org/abs/1409.3215
[13] K. Cho, B. Van Merri ¨enboer, D. Bahdanau, and Y . Bengio, “On the
properties of neural machine translation: Encoder-decoder approaches,”
arXiv preprint arXiv:1409.1259 , 2014.
[14] M. Allamanis, H. Peng, and C. Sutton, “A convolutional attention network
for extreme summarization of source code,” in International conference
on machine learning , 2016, pp. 2091–2100.
[15] U. Alon, S. Brody, O. Levy, and E. Yahav, “code2seq: Generating
sequences from structured representations of code,” arXiv preprint
arXiv:1808.01400, 2018.
[16] S. Iyer, I. Konstas, A. Cheung, and L. Zettlemoyer, “Summarizing source
code using a neural attention model,” in Proceedings of the 54th Annual
Meeting of the Association for Computational Linguistics (Volume 1:
Long Papers), 2016, pp. 2073–2083.
[17] J. Henkel, S. K. Lahiri, B. Liblit, and T. Reps, “Code vectors:
understanding programs through embedded abstracted symbolic traces,”
in Proceedings of the 2018 26th ACM Joint Meeting on European
Software Engineering Conference and Symposium on the Foundations
of Software Engineering - ESEC/FSE 2018 . New York, New
York, USA: ACM Press, 2018, pp. 163–174. [Online]. Available:
http://dl.acm.org/citation.cfm?doid=3236024.3236085
[18] M. White, M. Tufano, C. Vendome, and D. Poshyvanyk, “Deep
learning code fragments for code clone detection,” in Proceedings
of the 31st IEEE/ACM International Conference on Automated
Software Engineering - ASE 2016 . New York, New York,
USA: ACM Press, 2016, pp. 87–98. [Online]. Available: http:
//dl.acm.org/citation.cfm?doid=2970276.2970326
[19] G. Zhao and J. Huang, “DeepSim: deep learning code functional
similarity,” in Proceedings of the 2018 26th ACM Joint Meeting on
European Software Engineering Conference and Symposium on the
Foundations of Software Engineering - ESEC/FSE 2018 . New York,
New York, USA: ACM Press, 2018, pp. 141–151. [Online]. Available:
http://dl.acm.org/citation.cfm?doid=3236024.3236068
[20] U. Alon, M. Zilberstein, O. Levy, and E. Yahav, “code2vec: Learning
distributed representations of code,” Proceedings of the ACM on
Programming Languages, vol. 3, no. POPL, pp. 1–29, 2019.
[21] X. Hu, G. Li, X. Xia, D. Lo, and Z. Jin, “Deep code comment
generation,” in 2018 IEEE/ACM 26th International Conference on
Program Comprehension (ICPC). IEEE, 2018, pp. 200–20 010.
[22] J. Guo, J. Cheng, and J. Cleland-Huang, “Semantically Enhanced
Software Traceability Using Deep Learning Techniques,” in 2017
IEEE/ACM 39th International Conference on Software Engineering
(ICSE). IEEE, may 2017, pp. 3–14. [Online]. Available: http:
//ieeexplore.ieee.org/document/7985645/
[23] V . J. Hellendoorn, C. Bird, E. T. Barr, and M. Allamanis, “Deep
learning type inference,” in Proceedings of the 2018 26th ACM
Joint Meeting on European Software Engineering Conference and
Symposium on the Foundations of Software Engineering - ESEC/FSE
2018, vol. 18. New York, New York, USA: ACM Press, 2018, pp. 152–
162. [Online]. Available: https://doi.org/10.1145/3236024.3236051http:
//dl.acm.org/citation.cfm?doid=3236024.3236051
[24] W. Ling, E. Grefenstette, K. M. Hermann, T. Koˇcisk`y, A. Senior, F. Wang,
and P. Blunsom, “Latent predictor networks for code generation,” arXiv
preprint arXiv:1603.06744, 2016.
[25] B. V . Rompaey and S. Demeyer, “Establishing Traceability Links between
Unit Test Cases and Units under Test,” in2009 13th European Conference
on Software Maintenance and Reengineering, no. ii. IEEE, 2009, pp. 209–
218. [Online]. Available: http://ieeexplore.ieee.org/document/4812754/
[26] R. White, J. Krinke, and R. Tan, “Establishing Multilevel Test-to-Code
Traceability Links,” in 42nd International Conference on Software
Engineering (ICSE ’20) . Seoul, Republic of Korea: ACM, 2020.
[Online]. Available: https://doi.org/10.1145/3377811.3380921
[27] J. Gu, Z. Lu, H. Li, and V . O. Li, “Incorporating Copying Mechanism
in Sequence-to-Sequence Learning,” in Proceedings of the 54th Annual
Meeting of the Association for Computational Linguistics (Volume
1: Long Papers) , vol. 3. Stroudsburg, PA, USA: Association for
Computational Linguistics, 2016, pp. 1631–1640. [Online]. Available:
http://aclweb.org/anthology/P16-1154
[28] D. Bahdanau, K. Cho, and Y . Bengio, “Neural Machine Translation
by Jointly Learning to Align and Translate,” Annual Review of
Neuroscience, vol. 26, no. 1, pp. 105–131, sep 2014. [Online]. Available:
http://arxiv.org/abs/1409.0473
[29] T. Luong, H. Pham, and C. D. Manning, “Effective Approaches to
Attention-based Neural Machine Translation,” in Proceedings of the
2015 Conference on Empirical Methods in Natural Language Processing .
Stroudsburg, PA, USA: Association for Computational Linguistics, 2015,
pp. 1412–1421. [Online]. Available: http://arxiv.org/abs/1508.04025http:
//aclweb.org/anthology/D15-1166
[30] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
L. Kaiser, and I. Polosukhin, “Attention Is All You Need,” Behavioral
and Brain Sciences , vol. 40, no. Nips, p. e253, jun 2017. [Online].
Available: http://papers.nips.cc/paper/7181-attention-is-all-you-need
[31] A. N. Gomez, M. Ren, R. Urtasun, and R. B. Grosse, “The Reversible
Residual Network: Backpropagation Without Storing Activations,”
Advances in Neural Information Processing Systems , vol. 2017-
Decem, no. Nips, pp. 2215–2225, jul 2017. [Online]. Available:
http://arxiv.org/abs/1707.04585

<!-- Page 12 -->

[32] Google, “google/trax,” 2020. [Online]. Available: https://github.com/
google/trax
[33] T. A. O. Team. [Online]. Available: https://opennlp.apache.org/
[34] “Deep learning for java.” [Online]. Available: https://deeplearning4j.org/
[35] [Online]. Available: http://ejml.org/
[36] deeplearning4j, “Nd4j.” [Online]. Available: https://github.com/
deeplearning4j/nd4j
[37] “Stanford corenlp.” [Online]. Available: https://stanfordnlp.github.io/
CoreNLP/
[38] R. Pawlak, M. Monperrus, N. Petitprez, C. Noguera, and L. Seinturier,
“Spoon: A library for implementing analyses and transformations of java
source code,” Software: Practice and Experience , vol. 46, no. 9, pp.
1155–1179, 2016.
[39] J. H. Andrews, F. C. H. Li, and T. Menzies, “Nighthawk:
A Two-Level Genetic-Random Unit Test Data Generator,” in
Proceedings of the twenty-second IEEE/ACM international conference
on Automated software engineering - ASE ’07 . New York,
New York, USA: ACM Press, 2007, p. 144. [Online]. Available:
http://portal.acm.org/citation.cfm?doid=1321631.1321654
[40] C. Csallner and Y . Smaragdakis, “JCrasher: an automatic robustness tester
for Java,” Software: Practice and Experience , vol. 34, no. 11, pp. 1025–
1050, sep 2004. [Online]. Available: http://doi.wiley.com/10.1002/spe.602
[41] S. Park, B. M. M. Hossain, I. Hussain, C. Csallner, M. Grechanik,
K. Taneja, C. Fu, and Q. Xie, “CarFast: Achieving Higher Statement
Coverage Faster Sangmin,” in Proceedings of the ACM SIGSOFT 20th
International Symposium on the Foundations of Software Engineering -
FSE ’12. New York, New York, USA: ACM Press, 2012, p. 1. [Online].
Available: http://dl.acm.org/citation.cfm?doid=2393596.2393636
[42] P. Tonella, “Evolutionary testing of classes,” ACM SIGSOFT Software
Engineering Notes, vol. 29, no. 4, p. 119, jul 2004. [Online]. Available:
http://portal.acm.org/citation.cfm?doid=1013886.1007528
[43] C. S. P ˘as˘areanu and N. Rungta, “Symbolic PathFinder: Symbolic
Execution of Java Bytecode,” in Proceedings of the IEEE/ACM
international conference on Automated software engineering - ASE ’10 ,
vol. 2. New York, New York, USA: ACM Press, 2010, p. 179. [Online].
Available: http://portal.acm.org/citation.cfm?doid=1858996.1859035
[44] K. Sen and G. Agha, “CUTE and jCUTE: Concolic Unit Testing and
Explicit Path Model-Checking Tools,” in Lecture Notes in Computer
Science (including subseries Lecture Notes in Artiﬁcial Intelligence and
Lecture Notes in Bioinformatics) , 2006, vol. 4144 LNCS, pp. 419–423.
[Online]. Available: http://link.springer.com/10.1007/11817963{ }38

