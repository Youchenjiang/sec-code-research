# The Oracle Problem in Software Testing: A Survey

- **Venue**: IEEE Transactions on Software Engineering (TSE 2015)
- **Authors**: Earl T. Barr, Mark Harman, Phil McMinn, Muzammil Shahbaz, Shin Yoo
- **Pages**: 31

---

## Page 1

The Oracle Problem in Software Testing:
A Survey

Earl T. Barr, Mark Harman, Phil McMinn, Muzammil Shahbaz and Shin Yoo

Abstract—Testing involves examining the behaviour of a system in order to discover potential faults. Given an
input for a system, the challenge of distinguishing the corresponding desired, correct behaviour from potentially
incorrect behavior is called the “test oracle problem”. Test oracle automation is important to remove a current
bottleneck that inhibits greater overall test automation. Without test oracle automation, the human has to
determine whether observed behaviour is correct. The literature on test oracles has introduced techniques for
oracle automation, including modelling, speciﬁcations, contract-driven development and metamorphic testing.
When none of these is completely adequate, the ﬁnal source of test oracle information remains the human,
who may be aware of informal speciﬁcations, expectations, norms and domain speciﬁc information that provide
informal oracle guidance. All forms of test oracles, even the humble human, involve challenges of reducing cost
and increasing beneﬁt. This paper provides a comprehensive survey of current approaches to the test oracle
problem and an analysis of trends in this important area of software testing research and practice.

Index Terms—Test oracle; Automatic testing; Testing formalism.

✦

1
INTRODUCTION

Much work on software testing seeks to auto-
mate as much of the test process as practical
and desirable, to make testing faster, cheaper,
and more reliable. To this end, we need a test
oracle, a procedure that distinguishes between
the correct and incorrect behaviors of the Sys-
tem Under Test (SUT).
However, compared to many aspects of test
automation, the problem of automating the
test oracle has received signiﬁcantly less at-
tention, and remains comparatively less well-
solved. This current open problem represents a
signiﬁcant bottleneck that inhibits greater test
automation and uptake of automated testing
methods and tools more widely. For instance,
the problem of automatically generating test
inputs has been the subject of research interest
for nearly four decades [46], [108]. It involves
ﬁnding inputs that cause execution to reveal
faults, if they are present, and to give conﬁ-
dence in their absence, if none are found. Au-

1

tomated test input generation been the subject
of many signiﬁcant advances in both Search-
Based Testing [3], [5], [83], [127], [129] and
Dynamic Symbolic Execution [75], [109], [162];
yet none of these advances address the issue
of checking generated inputs with respect to
expected behaviours—that is, providing an au-
tomated solution to the test oracle problem.
Of course, one might hope that the SUT
has been developed under excellent design-
for-test principles, so that there might be a
detailed, and possibly formal, speciﬁcation of
intended behaviour. One might also hope that
the code itself contains pre- and post- condi-
tions that implement well-understood contract-
driven development approaches [136]. In these
situations, the test oracle cost problem is ame-
liorated by the presence of an automatable test
oracle to which a testing tool can refer to check
outputs, free from the need for costly human
intervention.
Where no full speciﬁcation of the properties
of the SUT exists, one may hope to construct a


---

## Page 2

partial test oracle that can answer questions for
some inputs. Such partial test oracles can be
constructed using metamorphic testing (built
from known relationships between desired be-
haviour) or by deriving oracular information
from execution or documentation.
For many systems and most testing as cur-
rently practiced in industry, however, the tester
does not have the luxury of formal speciﬁca-
tions or assertions, or automated partial test
oracles [91], [92]. The tester therefore faces
the daunting task of manually checking the
system’s behaviour for all test cases. In such
cases, automated software testing approaches
must address the human oracle cost problem
[1], [82], [131].
To achieve greater test automation and wider
uptake of automated testing, we therefore need
a concerted effort to ﬁnd ways to address the
test oracle problem and to integrate automated
and partially automated test oracle solutions
into testing techniques. This paper seeks to
help address this challenge by providing a
comprehensive review and analysis of the ex-
isting literature of the test oracle problem.
Four partial surveys of topics relating to test
oracles precede this one. However, none has
provided a comprehensive survey of trends
and results. In 2001, Baresi and Young [17] pre-
sented a partial survey that covered four topics
prevalent at the time the paper was published:
assertions, speciﬁcations, state-based confor-
mance testing, and log ﬁle analysis. While
these topics remain important, they capture
only a part of the overall landscape of research
in test oracles, which the present paper covers.
Another early work was the initial motivation
for considering the test oracle problem con-
tained in Binder’s textbook on software testing
[23], published in 2000. More recently, in 2009,
Shahamiri et al. [165] compared six techniques
from the speciﬁc category of derived test or-
acles. In 2011, Staats et al. [174] proposed a
theoretical analysis that included test oracles
in a revisitation of the fundamentals of testing.
Most recently, in 2014, Pezz`e et al. focus on

2

automated test oracles for functional proper-
ties [151].
Despite this work, research into the test or-
acle problem remains an activity undertaken
in a fragmented community of researchers and
practitioners. The role of the present paper is to
overcome this fragmentation in this important
area of software testing by providing the ﬁrst
comprehensive analysis and review of work on
the test oracle problem.
The rest of the paper is organised as follows:
Section 2 sets out the deﬁnitions relating to test
oracles that we use to compare and contrast the
techniques in the literature. Section 3 relates
a historical analysis of developments in the
area. Here we identify key milestones and track
the volume of past publications. Based on this
data, we plot growth trends for four broad cat-
egories of solution to the test oracle problem,
which we survey in Sections 4–7. These four
categories comprise approaches to the oracle
problem where:

• test oracles can be speciﬁed (Section 4);

• test oracles can be derived (Section 5);

• test oracles can be built from implicit in-
formation (Section 6); and

• no automatable oracle is available, yet
it is still possible to reduce human effort
(Section 7)
Finally, Section 8 concludes with closing re-
marks.

2
DEFINITIONS

This section presents deﬁnitions to establish a
lingua franca in which to examine the literature
on oracles. These deﬁnitions are formalised to
avoid ambiguity, but the reader should ﬁnd
that it is also possible to read the paper using
only the informal descriptions that accompany
these formal deﬁnitions. We use the theory to
clarify the relationship between algebraic spec-
iﬁcation, pseudo oracles, and metamorphic re-
lations in Section 5.
To begin, we deﬁne a test activity as a stim-
ulus or response, then test activity sequences


---

## Page 3

R
S

f(i)
I
O
i
o

Fig. 1. Stimulus and observations: S is anything
that can change the observable behavior of the
SUT f; R is anything that can be observed
about the system’s behavior; I includes f’s ex-
plicit inputs; O is its explicit outputs; everything
not in S ∪R neither affects nor is affected by f.

that incorporate constraints over stimuli and
responses. Test oracles accept or reject test
activity sequences, ﬁrst deterministically then
probabilistically. We then deﬁne notions of
soundness and completeness of test oracles.

2.1
Test Activities

To test is to stimulate a system and observe
its response. A stimulus and a response both
have values, which may coincide, as when
the stimulus value and the response are both
reals. A system has a set of components C. A
stimulus and its response target a subset of
components. For instance, a common pattern
for constructing test oracles is to compare the
output of distinct components on the same
stimulus value. Thus, stimuli and responses
are values that target components. Collectively,
stimuli and responses are test activities:

Deﬁnition 2.1 (Test Activities). For the SUT p,
S is the set of stimuli that trigger or constrain p’s
computation and R is the set of observable responses
to a stimulus of p. S and R are disjoint. Test
activities form the set A = S ⊎R.

The use of disjoint union implicitly labels the
elements of A, which we can ﬂatten to the tuple
L × C × V , where L = {stimulus, response} is

3

the set of activities labels, C is the set of com-
ponents, and V is an arbitrary set of values.
To model those aspects of the world that are
independent of any component, like a clock,
we set an activity’s target to the empty set.
We use the terms “stimulus” and “observa-
tion” in the broadest sense possible to cater
to various testing scenarios, functional and
nonfunctional. As shown in Figure 1, a stim-
ulus can be either an explicit test input from
the tester, I ⊂S, or an environmental factor
that can affect the testing, S \ I. Similarly, an
observation ranges from an output of the SUT,
O ⊂R, to a nonfunctional execution proﬁle,
like execution time in R \ O.
For example, stimuli include the conﬁgu-
ration and platform settings, database table
contents, device states, resource constraints,
preconditions, typed values at an input device,
inputs on a channel from another system, sen-
sor inputs and so on. Notably, resetting a SUT
to an initial state is a stimulus and stimulating
the SUT with an input runs it. Observations
include anything that can be discerned and
ascribed a meaning signiﬁcant to the purpose
of testing — including values that appear on an
output device, database state, temporal prop-
erties of the execution, heat dissipated during
execution, power consumed, or any other mea-
surable attributes of its execution. Stimuli and
observations are members of different sets of
test activities, but we combine them into test
activities.

2.2
Test Activity Sequence

Testing is a sequence of stimuli and response
observations. The relationship between stimuli
and responses can often be captured formally;
consider a simple SUT that squares its input. To
compactly represent inﬁnite relations between
stimulus and response values such as (i, o =
i2), we introduce a compact notation for set
comprehensions:

x:[φ] = {x | φ},


---

## Page 4

where x is a dummy variable over an arbitrary
set.

Deﬁnition 2.2 (Test Activity Sequence). A test
activity sequence is an element of TA = {w |
T
∗→w} over the grammar

T ::= A ′:[′ φ ′]′ T | AT | ǫ

where A is the test activity alphabet.

Under Deﬁnition 2.2, the testing activity se-
quence io:[o = i2] denotes the stimulus of in-
voking f on i, then observing the response out-
put. It further speciﬁes valid responses obeying
o = i2. Thus, it compactly represents the inﬁ-
nite set of test activity sequences i1o1, i2o2, · · ·
where ok = i2
k.
For practical purposes, a test activity se-
quence will almost always have to satisfy
constraints in order to be useful. Under our
formalism, these constraints differentiate the
approaches to test oracle we survey. As an
initial illustration, we constrain a test activity
sequence to obtain a practical test sequence:

Deﬁnition 2.3 (Practical Test Sequence). A
practical test sequence is any test activity se-
quence w that satisﬁes

w = TsTrT, for s ∈S, r ∈R.

Thus, the test activity sequence, w, is practical
iff w contains at least one stimulus followed by
at least one observation.
This notion of a test sequence is nothing
more than a very general notion of what it
means to test; we must do something to the
system (the stimulus) and subsequently ob-
serve some behaviour of the system (the obser-
vation) so that we have something to check (the
observation) and something upon which this
observed behaviour depends (the stimulus).
A reliable reset (p, r)
∈
S is a special
stimulus that returns the SUT’s component
p to its start state. The test activity se-
quence (stimulus, p, r)(stimulus, p, i) is there-
fore equivalent to the conventional application
notation p(i). To extract the value of an activity,

4

we write v(a); to extract its target component,
we write c(a). To specify two invocations of a
single component on the different values, we
must write r1i1r2, i2 : [r1, i1, r2, i2 ∈S, c(r1) =
c(i1) = c(r2) = c(i2) ∧v(i1) ̸= v(i2)]. In the
sequel, we often compare different executions
of a single SUT or compare the output of in-
dependently implemented components of the
SUT on the same input value. For clarity, we
introduce syntactic sugar to express constraints
on stimulus values and components. We let
f(x) denote ri:[c(i) = f ∧v(i) = x], for f ∈C.
A test oracle is a predicate that determines
whether a given test activity sequence is an
acceptable behaviour of the SUT or not. We
ﬁrst deﬁne a “test oracle”, and then relax this
deﬁnition to “probabilistic test oracle”.

Deﬁnition 2.4 (Test Oracle). A test oracle D :
TA 7→B is a partial1 function from a test activity
sequence to true or false.

When a test oracle is deﬁned for a test
activity, it either accepts the test activity or
not. Concatenation in a test activity sequence
denotes sequential activities; the test oracle
D permits parallel activities when it accepts
different permutations of the same stimuli and
response observations. We use D to distinguish
a deterministic test oracle from probabilistic
ones. Test oracles are typically computationally
expensive, so probabilistic approaches to the
provision of oracle information may be desir-
able even where a deterministic test oracle is
possible [125].

Deﬁnition 2.5 (Probabilistic Test Oracle). A
probabilistic test oracle ˜D : TA
7→[0, 1] maps
a test activity sequence into the interval [0, 1] ∈R.

A probabilistic test oracle returns a real num-
ber in the closed interval [0, 1]. As with test
oracles, we do not require a probabilistic test
oracle to be a total function. A probabilistic test

1. Recall that a function is implicitly total: it maps every
element of its domain to a single element of its range. The
partial function f : X 7→Y is the total function f′ : X′ →
Y , where X′ ⊆X.


---

## Page 5

oracle can model the case where the test oracle
is only able to efﬁciently offer a probability
that the test case is acceptable, or for other
situations where some degree of imprecision
can be tolerated in the test oracle’s response.
Our
formalism
combines
a
language-
theoretic
view
of
stimulus
and
response
activities
with
constraints
over
those
activities; these constraints explicitly capture
speciﬁcations. The high-level language view
imposes a temporal order on the activities.
Thus, our formalism is inherently temporal.
The formalism of Staats et al. captures any
temporal exercising of the SUT’s behavior
in tests, which are atomic black boxes for
them [174]. Indeed, practitioners write test
plans and activities, they do not often write
speciﬁcations at all, let alone a formal one. This
fact and the expressivity of our formalism, as
evident in our capture of existing test oracle
approaches, is evidence that our formalism is
a good ﬁt with practice.

2.3
Soundness and Completeness

We conclude this section by deﬁning sound-
ness and completeness of test oracles.
In order to deﬁne soundness and complete-
ness of a test oracle, we need to deﬁne a
concept of the “ground truth”, G. The ground
truth is another form of oracle, a conceptual
oracle, that always gives the “right answer”.
Of course, it cannot be known in all but the
most trivial cases, but it is a useful deﬁnition
that bounds test oracle behaviour.

Deﬁnition 2.6 (Ground Truth). The ground
truth oracle, G, is a total test oracle that always
gives the “right answer”.

We can now deﬁne soundness and complete-
ness of a test oracle with respect to G.

Deﬁnition 2.7 (Soundness). The test oracle D is
sound iff

D(a) ⇒G(a)

5

Deﬁnition 2.8 (Completeness). The test oracle
D is complete iff

G(a) ⇒D(a)

While test oracles cannot, in general, be both
sound and complete, we can, nevertheless,
deﬁne and use partially correct test oracles.
Further, one could argue, from a purely philo-
sophical point of view, that human oracles
can be sound and complete, or correct. In this
view, correctness becomes a subjective human
assessment. The foregoing deﬁnitions allow for
this case.
We relax our deﬁnition of soundness to cater
for probabilistic test oracles:

Deﬁnition 2.9 (Probablistic Soundness and
Completeness). A probabilistic test oracle ˜D is
probabilistically sound iff

P( ˜D(w) = 1) > 1

2 + ǫ ⇒G(w)

and ˜D is probabilistically complete iff

G(w) ⇒P( ˜D(w) = 1) > 1

2 + ǫ

where ǫ is non-negligible.

The non-negligible advantage ǫ requires ˜D
to do sufﬁciently better than ﬂipping a fair
coin, which for a binary classiﬁer maximizes
entropy, that we can achieve arbitrary conﬁ-
dence in whether the test sequence w is valid
by repeatedly sampling ˜D on w.

3
TEST ORACLE RESEARCH TRENDS

The term “test oracle” ﬁrst appeared in William
Howden’s seminal work in 1978 [99]. In this
section, we analyze the research on test oracles,
and its related areas, conducted since 1978.
We begin with a synopsis of the volume of
publications, classiﬁed into speciﬁed, derived,
implicit, and lack of automated test oracles. We
then discuss when key concepts in test oracles
were ﬁrst introduced.


---

## Page 6

!"#"$%&'''()%$*++"

45)106)7*8-&1%)3*
!"#"$%&'()*%+,-*"

,-"#"$%.//))"

!"##$%&'()**+$#,)-**".**/$,%01&'"23*

+0$"

+$$"

)0$"

)$$"

&0$"

&$$"

0$"

$"

&.'&"

&.'0"

&.'*"

&.''"

&.'."

&..&"

&..0"

&..*"

&..'"

&..."

)$$&"

)$$0"

)$$*"

)$$'"

)$$."

)$&&"

&.'$"

&.')"

&.'+"

&.'/"

&.'1"

&..$"

&..)"

&..+"

&../"

&..1"

)$$$"

)$$)"

)$$+"

)$$/"

)$$1"

)$&$"

)$&)"

4#5%0106*7-&1%)3*
y = 0.2997x1.4727

!"#"$%&'()*'%+,-'"

!"##$%&'()**+$#,)-**".**/$,%01&'"23*

./"#"$%)(-&+"

)$"

($"

+$"

,$"

0$"

-$"

&$"

'$"

$"

'1))"

'1)1"

'11'"

'11,"

'11("

'11)"

'111"

&$$'"

&$$,"

&$$("

&$$)"

&$$1"

&$''"

'11$"

'11&"

'11-"

'110"

'11+"

&$$$"

&$$&"

&$$-"

&$$0"

&$$+"

&$'$"

&$'&"

Fig. 2. Cumulative number of publications from 1978 to 2012 and research trend analysis for each
type of test oracle. The x-axis represents years and y-axis the cumulative number of publications.
We use a power regression model to perform the trend analysis. The regression equation and
the coefﬁcient of determination (R2) indicate a upward future trend, a sign of a healthy research
community.

3.1
Volume of Publications

We constructed a repository of 694 publica-
tions on test oracles and its related areas from
1978 to 2012 by conducting web searches for
research articles on Google Scholar and Microsoft
Academic Search using the queries “software +
test + oracle” and “software + test oracle”2,
for each year. Although some of the queries
generated in this fashion may be similar, dif-
ferent responses are obtained, with particular
differences around more lowly-ranked results.
We classify work on test oracles into four
categories: speciﬁed test oracles (317), derived
test oracles (245), implicit test oracles (76), and
no test oracle (56), which handles the lack of a

2. We use + to separate the keywords in a query; a
phrase, not internally separated by +, like “test oracle”,
is a compound keyword, quoted when given to the search
engine.

6

4)-0()5*6-&1%)3*

!"##$%&'()**+$#,)-**".**/$,%01&'"23*

./"#"$%0$*1'"

&$$"

'-$"

'$$"

*-$"

*$$"

-$"

$"

*01*"

*01-"

*01,"

*011"

*010"

*00*"

*00-"

*00,"

*001"

*000"

'$$*"

'$$-"

'$$,"

'$$1"

'$$0"

'$**"

*01$"

*01'"

*01&"

*01("

*01+"

*00$"

*00'"

*00&"

*00("

*00+"

'$$$"

'$$'"

'$$&"

'$$("

'$$+"

'$*$"

'$*'"

Handling the lack of oracles

R² = 0.8871

Commula've  Number  of  Publica'ons

60

50

40

30

20

10

0

1991

1995

1997

1998

1999

2001

2005

2007

2008

2009

2011

1990

1992

1993

1994

1996

2000

2002

2003

2004

2006

2010

2012

test oracle.

Speciﬁed test oracles, discussed in detail in
Section 4, judge all behavioural aspects of a
system with respect to a given formal speciﬁ-
cation. For speciﬁed test oracles we searched
for
related
articles
using
queries
“formal
+ speciﬁcation”, “state-based speciﬁcation”,
“model-based
languages”,
“transition-based
languages”, “assertion-based languages”, “al-
gebraic speciﬁcation” and “formal + confor-
mance testing”. For all queries, we appended
the keywords with “test oracle” to ﬁlter the
results for test oracles.

Derived test oracles (see Section 5) in-
volve artefacts from which a test oracle may
be derived — for instance, a previous ver-
sion of the system. For derived test oracles,
we searched for additional articles using the
queries “speciﬁcation inference”, “speciﬁcation


---

## Page 7

mining”, “API mining”, “metamorphic test-
ing”, “regression testing” and “program doc-
umentation”.
An implicit oracle (see Section 6) refers to
the detection of “obvious” faults such as a pro-
gram crash. For implicit test oracles we applied
the queries “implicit oracle”, “null pointer +
detection”, “null reference + detection”, “dead-
lock + livelock + race + detection”, “memory
leaks + detection”, “crash + detection”, “per-
formance + load testing”, “non-functional +
error detection”, “fuzzing + test oracle” and
“anomaly detection”.
There have also been papers researching
strategies for handling the lack of an auto-
mated test oracle (see Section 7). Here, we
applied the queries “human oracle”, “test mini-
mization”, “test suite reduction” and “test data
+ generation + realistic + valid”.
Each of the above queries were appended
by the keywords “software testing”. The re-
sults were ﬁltered, removing articles that were
found to have no relation to software testing
and test oracles. Figure 2 shows the cumulative
number of publications on each type of test
oracle from 1978 onwards. We analyzed the
research trend on this data by applying differ-
ent regression models. The trend line, shown
in Figure 2, is ﬁtted using a power model.
The high values for the four coefﬁcients of
determination (R2), one for each of the four
types of test oracle, conﬁrm that our models are
good ﬁts to the trend data. The trends observed
suggest a healthy growth in research volumes
in these topics related to the test oracle problem
in the future.

3.2
The Advent of Test Oracle Techniques

We classiﬁed the collected publications by tech-
niques or concepts they proposed to (partially)
solve a test oracle problem; for example, Model
Checking [35] and Metamorphic Testing
[36]
fall into the derived test oracle and DAISTIS
[69] is an algebraic speciﬁcation system that
addresses the speciﬁed test oracle problem.

7

For each type of test oracle and the advent of
a technique or a concept, we plotted a timeline
in chronological order of publications to study
research trends. Figure 3 shows the timeline
starting from 1978 when the term “test oracle”
was ﬁrst coined. Each vertical bar presents the
technique or concept used to solve the problem
labeled with the year of its ﬁrst publication.
The timeline shows only the work that is
explicit on the issue of test oracles. For exam-
ple, the work on test generation using ﬁnite
state machines (FSM) can be traced back to as
early as 1950s. But the explicit use of ﬁnite
state machines to generate test oracles can
be traced back to Jard and Bochmann [103]
and Howden in 1986 [98]. We record, in the
timeline, the earliest available publication for a
given technique or concept. We consider only
published work in journals, the proceedings
of conferences and workshops, or magazines.
We excluded all other types of documentation,
such as technical reports and manuals.
Figure 3 shows a few techniques and con-
cepts that predate 1978. Although not explicitly
on test oracles, they identify and address issues
for which test oracles were later developed. For
example, work on detecting concurrency issues
(deadlock, livelock, and races) can be traced
back to the 1960s. Since these issues require
no speciﬁcation, implicit test oracles can and
have been built that detect them on arbitrary
systems. Similarly, Regression Testing detects
problems in the functionality a new version of
a system shares with its predecessors and is a
precursor of derived test oracles.
The trend analysis suggests that propos-
als for new techniques and concepts for the
formal speciﬁcation of test oracles peaked in
1990s, and has gradually diminished in the last
decade. However, it remains an area of much
research activity, as can be judged from the
number of publications for each year in Fig-
ure 2. For derived test oracles, many solutions
have been proposed throughout this period.
Initially, these solutions were primarily theoret-
ical, such as Partial/Pseudo-Oracles [196] and


---

## Page 8

Handling the Lack of Test Oracles  
93

pre-78

Test Size Reduction

Partition Testing

88 
 Implicit Test Oracles

pre-78 
98 
06

90

Concurrency Issues Detection

Memory Leaks Detection

Exception Checking

Load Testing

Fuzzing

Test Oracle

pre-78 
99 
02 
07 
09 10 
 Derived Test Oracles

82 83 
86 
94 
98

Pseudo, Partial Oracle

Regression Testing

Spec Inference

N-Versions

88 
92 
01 
81 
89 
96 
94 
93 
97 98 99 00 
04 
07 
09 
 Specified Test Oracles  
83

ASTOOT, GIL, TOAS, Z, 
Lustre

IORL, PROSPER, SDL

Design-by-Contract

ANNA, LARCH

MSC, VDM

DAISTS

FSM

1980 
1985 
1990 
1995 
2000 
2005 
2010

1978

Fig. 3. Chronological introduction of test oracles techniques and concepts.

Speciﬁcation Inference [194]; empirical studies
however followed in late 1990s.

For implicit test oracles, research into the so-
lutions established before 1978 has continued,
but at a slower pace than the other types of test
oracles. For handling the lack of an automated
test oracle, Partition Testing is a well-known
technique that helps a human test oracle select
tests. The trend line suggests that only recently
have new techniques and concepts for tackling
this problem started to emerge, with an explicit
focus on the human oracle cost problem.

8

00 
05 
11 12

02

Input Classification

Realistic Test Data

Machine Learning

Delta Debugging

Usage Mining

08

Mining for Concurrency Issues

Robustness Checking

Anomaly Detection

Spec Mining, N Networks

Log File Analysis, 
Metamorphic Testing

Invariant Detection

Semi-Formal Docs

Code Comments

Mutant-based

API Docs

95

02

08

ASML, Alloy, RESOLVE

H Statecharts, Object-Z

DAISTISH, Temporal 
Logic, Model Checking

CASCAT

TTCN-3

LETO

IOCO

CASL

LOFT

UML

OCL

JML

4
SPECIFIED TEST ORACLES

Speciﬁcation is fundamental to computer sci-
ence, so it is not surprising that a vast body of
research has explored its use as a source of test
oracle information. This topic could merit an
entire survey on its own right. In this section,
we provide an overview of this work. We also
include here partial speciﬁcations of system
behaviour such as assertions and models.
A speciﬁcation deﬁnes, if possible using
mathematical logic, the test oracle for partic-
ular domain. Thus, a speciﬁcation language
is a notation for deﬁning a speciﬁed test oracle
D, which judges whether the behaviour of a


---

## Page 9

system conforms to a formal speciﬁcation. Our
formalism, deﬁned in Section 2, is, itself, a
speciﬁcation language for specifying test ora-
cles.
Over the last 30 years, many methods and
formalisms for testing based on formal spec-
iﬁcation have been developed. They fall into
four broad categories: model-based speciﬁca-
tion languages, state transition systems, asser-
tions and contracts, and algebraic speciﬁca-
tions. Model-based languages deﬁne models
and a syntax that deﬁnes desired behavior in
terms of its effect on the model. State transition
systems focus on modeling the reaction of a
system to stimuli, referred to as “transitions”
in this particular formalism. Assertions and
contracts are fragments of a speciﬁcation lan-
guage that are interleaved with statements of
the implementation language and checked at
runtime. Algebraic speciﬁcations deﬁne equa-
tions over a program’s operations that hold
when the program is correct.

4.1
Speciﬁcation Languages

Speciﬁcation languages deﬁne a mathemati-
cal model of a system’s behaviour, and are
equipped with a formal semantics that deﬁnes
the meaning of each language construct in
terms of the model. When used for testing,
models do not usually fully specify the sys-
tem, but seek to capture salient properties of a
system so that test cases can be generated from
or checked against them.

4.1.1
Model-Based Speciﬁcation Languages

Model-based speciﬁcation languages model a
system as a collection of states and operations
to alter these states, and are therefore also
referred to as “state-based speciﬁcations” in
the literature [101], [110], [182], [183]. Precon-
ditions and postconditions constrain the sys-
tem’s operations. An operation’s precondition
imposes a necessary condition over the input
states that must hold in a correct application
of the operation; a postcondition deﬁnes the

9

(usually strongest) effect the operation has on
program state [110].
A variety of model-based speciﬁcation lan-
guages
exist,
including
Z
[172],
B
[111],
UML/OCL
[31],
VDM/VDM-SL
[62],
Al-
loy
[102],
and
the
LARCH
family
[71],
which
includes
an
algebraic
speciﬁcation
sub-language. Broadly, these languages have
evolved toward being more concrete, closer
to the implementation languages programmers
use to solve problems. Two reasons explain
this phenomenon: the ﬁrst is the effort to in-
crease their adoption in industry by making
them more familiar to practitioners and the
second is to establish synergies between spec-
iﬁcation and implementation that facilitate de-
velopment as iterative reﬁnement. For instance,
Z models disparate entities, like predicates,
sets, state properties, and operations, through
a single structuring mechanism, its schema
construct; the B method, Z’s successor, pro-
vides a richer array of less abstract language
constructs.
B¨orger discusses how to use the abstract
state machine formalism, a very general set-
theoretic speciﬁcation language geared toward
the deﬁnition of functions, to deﬁne high level
test oracles [29]. The models underlying speci-
ﬁcation languages can be very abstract, quite
far from concrete execution output. For in-
stance, it may be difﬁcult to compute whether
a model’s postcondition for a function permits
an observed concrete output. If this impedance
mismatch can be overcome, by abstracting a
system’s concrete output or by concretizing a
speciﬁcation model’s output, and if a speciﬁca-
tion’s postconditions can be evaluated in ﬁnite
time, they can serve as a test oracle [4].
Model-based speciﬁcation languages, such
as VDM, Z, and B can express invariants,
which can drive testing. Any test case that
causes a program to violate an invariant has
discovered an incorrect behavior; therefore,
these invariants are partial test oracles.
In search of a model-based speciﬁcation lan-
guage accessible to domain experts, Parnas


---

## Page 10

et al. proposed TOG (Test Oracles Genera-
tor) from program documentation [143], [146],
[149]. In their method, the documentation is
written in fully formal tabular expressions in
which the method signature, the external vari-
ables, and relation between its start and end
states are speciﬁed [105]. Thus, test oracles can
be automatically generated to check the out-
puts against the speciﬁed states of a program.
The work by Parnas et al. has been developed
over a considerable period of more than two
decades [48], [59], [60], [145], [150], [190], [191].

4.1.2
State Transition Systems
State transition systems often present a graph-
ical
syntax,
and
focus
on
transitions
be-
tween different states of the system. Here,
states typically abstract sets of concrete state
of the modeled system. State transition sys-
tems have been referred as visual languages
in the literature [197]. A wide variety of
state transition systems exist, including Fi-
nite State Machines [112], Mealy/Moore ma-
chines [112], I/O Automata [118], Labeled
Transition Systems [180], SDL [54], Harel Stat-
echarts [81], UML state machines [28], X-
Machines [95], [96], Simulink/Stateﬂow [179]
and PROMELA [97]. Mouchawrab et al. con-
ducted a rigorous empirical evaluation of test
oracle construction techniques using state tran-
sition systems [70], [138].
An important class of state transition sys-
tems have a ﬁnite set of states and are therefore
particularly well-suited for automated reason-
ing about systems whose behaviour can be
abstracted into states deﬁned by a ﬁnite set
of values [93]. State transition systems cap-
ture the behavior of a system under test as
a set of states3, with transitions representing
stimuli that cause the system to change state.
State transition systems model the output of

3. Unfortunately, the term ‘state’ has different interpre-
tation in the context of test oracles. Often, it refers to a
‘snapshot’ of the conﬁguration of a system at some point
during its execution; in context of state transition systems,
however, ‘state’ typically refers to an abstraction of a set
of conﬁgurations, as noted above.

10

a system they abstract either as a property of
the states (the ﬁnal state in the case of Moore
machines) or the transitions traversed (as with
Mealy machines).
Models approximate a SUT, so behavioral
differences between the two are inevitable.
Some divergences, however, are spurious and
falsely report testing failure. State-transition
models are especially susceptible to this prob-
lem when modeling embedded systems, for
which time of occurrence is critical. Recent
work model tolerates spurious differences in
time by “steering” model’s evaluation: when
the SUT and its model differ, the model is back-
tracked, and a steering action, like modifying
timer value or changing inputs, is applied to
reduce the distance, under a similarity mea-
sure [74].
Protocol conformance testing [72] and, later,
model-based testing [183] motivated much of
the work applying state transition systems to
testing. Given a speciﬁcation F as a state tran-
sition system, e.g. a ﬁnite state machine, a
test case can be extracted from sequences of
transitions in F. The transition labels of such
a sequence deﬁne an input. A test oracle can
then be constructed from F as follows: if F
accepts the sequence and outputs some value,
then so should the system under test; if F does
not accept the input, then neither should the
system under test.
Challenges remain, however, as the deﬁni-
tion of conformity comes in different ﬂavours,
depending on whether the model is determin-
istic or non-deterministic and whether the be-
haviour of the system under test on a given test
case is observable and can be interpreted at the
same level of abstraction as the model’s. The
resulting ﬂavours of conformity have been cap-
tured in alternate notions, in terms of whether
the system under test is isomorphic to, equiv-
alent to, or quasi-equivalent to F. These no-
tions of conformity were deﬁned in the mid-
1990s in the famous survey paper by Lee and
Yannakakis [112] among other notable papers,
including those by Bochmann et al. [26] and


---

## Page 11

Tretmans [180].

4.2
Assertions and Contracts

An assertion is a boolean expression that is
placed at a certain point in a program to check
its behaviour at runtime. When an assertion
evaluates to true, the program’s behaviour is
regarded “as intended” at the point of the
assertion, for that particular execution; when
an assertion evaluates to false, an error has
been found in the program for that particular
execution. It is obvious to see how assertions
can be used as a test oracle.
The fact that assertions are embedded in an
implementation language has two implications
that differentiate them from speciﬁcation lan-
guages. First, assertions can directly reference
and deﬁne relations over program variables,
reducing the impedance mismatch between
speciﬁcation and implementation, for the prop-
erties an assertion can express and check. In
this sense, assertions are a natural consequence
of the evolution of speciﬁcation languages to-
ward supporting development through iter-
ative reﬁnement. Second, they are typically
written along with the code whose runtime
behavior they check, as opposed to preced-
ing implementation as speciﬁcation languages
tend to do.
Assertions have a long pedigree dating back
to Turing [181], who ﬁrst identiﬁed the need
to separate the tester from the developer and
suggested that they should communicate by
means of assertions: the developer writing
them and the tester checking them. Asser-
tions gained signiﬁcant attention as a means
of capturing language semantics in the semi-
nal work of Floyd
[64] and Hoare [94] and
subsequently were championed as a means
of increasing code quality in the development
of the contract-based programming approach,
notably in the language Eiffel [136].
Widely used programming languages now
routinely provide assertion constructs; for in-
stance, C, C++, and Java provide a construct
called assert and C# provides a Debug.Assert

11

method. Moreover, a variety of systems have
been independently developed for embedding
assertions into a host programming languages,
such as Anna [117] for Ada, APP [156] and
Nana [120] for C languages.
In practice, assertion approaches can check
only a limited set of properties at a certain
point in a program [49]. Languages based on
design by contract principles extend the ex-
pressivity of assertions by providing means
to check contracts between client and supplier
objects in the form of method pre- and post-
conditions and class invariants. Eiffel was the
ﬁrst language to offer design by contract [136],
a language feature that has since found its way
into other languages, such as Java in the form
of Java modeling language (JML) [140].
Cheon and Leavens showed how to con-
struct an assertion-based test oracle on top
of JML [45]. For more on assertion-based test
oracles, see Coppit and Haddox-Schatz’s eval-
uation [49], and, later, a method proposed by
Cheon [44]. Both assertions and contracts are
enforced observation activity that are embed-
ded into the code. Araujo et al. provide a
systematic evaluation of design by contract on
a large industrial system [9] and using JML in
particular [8]; Briand et al. showed how to sup-
port testing by instrumenting contracts [33].

4.3
Algebraic Speciﬁcation Languages

Algebraic speciﬁcation languages deﬁne a soft-
ware module in terms of its interface, a sig-
nature consisting of sorts and operation sym-
bols. Equational axioms specify the required
properties of the operations; their equivalence
is often computed using term rewriting [15].
Structuring facilities, which group sorts and
operations, allow the composition of interfaces.
Typically, these languages employ ﬁrst-order
logic to prove properties of the speciﬁcation,
like the correctness of reﬁnements. Abstract
data types (ADT), which combine data and
operations over that data, are well-suited to
algebraic speciﬁcation.


---

## Page 12

One of the earliest algebraic speciﬁcation
systems, for implementing, specifying and test-
ing ADTs, is DAISTS [69]. In this system,
equational axioms generally equate a term-
rewriting expression in a restricted dialect of
ALGOL 60 against a function composition in
the implementation language. For example,
consider this axiom used in DAISTS:

Pop2(Stack S, EltType I) :
Pop(Push(S, I)) = if Depth(S) = Limit

then Pop(S)

else S;

This axiom is taken from a speciﬁcation that
differentiates the accessor Top, which returns
the top element of a stake without modifying
the stack, and the mutator Pop, which returns a
new stack lacking the previous top element. A
test oracle simply executes both this axiom and
its corresponding composition of implemented
functions against a test suite: if they disagree, a
failure has been found in the implementation
or in the axiom; if they agree, we gain some
assurance of their correctness.
Gaudel and her colleagues [19], [20], [72],
[73] were the ﬁrst to provide a general test-
ing theory founded on algebraic speciﬁcation.
Their idea is that an exhaustive test suite
composed only of ground terms, i.e., terms
with no free variables, would be sufﬁcient
to judge program correctness. This approach
faces an immediate problem: the domain of
each variable in a ground term might be in-
ﬁnite and generate an inﬁnite number of test
cases. Test suites, however, must be ﬁnite, a
practical limitation to which all forms of testing
are subject. The workaround is, of course, to
abandon exhaustive coverage of all bindings
of values to ground terms and select a ﬁnite
subset of test cases [20].
Gaudel’s theory focuses on observational
equivalence. Observational inequivalence is,
however, equally important [210]. For this rea-
son, Frankl and Doong extended Gaudel’s the-
ory to express inequality as well an equal-

12

ity [52]. They proposed a notation that is suit-
able for object-oriented programs and devel-
oped an algebraic speciﬁcation language called
LOBAS and a test harness called ASTOOT. In
addition to handling object-orientation, Frankl
and Doong require classes to implement the
testing method EQN that ASTOOT uses to
check the equivalence or inequivalence of two
instances of a given class. From the vantage
point of an observer, an object has observable
and unobservable, or hidden, state. Typically,
the observable state of an object is its public
ﬁelds and method return values. EQN enhances
the testability of code and enables ASTOOT
to approximate the observational equivalence
of two objects on a sequence of messages,
or method calls. When ASTOOT checks the
equivalence of an object and a speciﬁcation in
LOBAS, it realizes a speciﬁed test oracle.
Expanding upon ASTOOT, Chen et al. [40]
[41] built TACCLE, a tool that employs a white-
box heuristic to generate a relevant, ﬁnite
number of test cases. Their heuristic builds a
data relevance graph that connects two ﬁelds
of a class if one affects the other. They use
this graph to consider only that can affect
an observable attributes of a class when con-
sidering the (in)equivalence of two instances.
Algebraic speciﬁcation has been a fruitful line
of research; many algebraic speciﬁcation lan-
guages and tools exist, including Daistish [100],
LOFT [123], CASL [11], CASCAT [205]. The
projects have been evolving toward testing a
wider array of entities, from ADTS, to classes,
and most recently, components; they also differ
in their degree of automation of test case gen-
eration and test harness creation. Bochmann et
al. used LOTOS to realise test oracle functions
from algebraic speciﬁcations [184]; most re-
cently, Zhu also considered the use of algebraic
speciﬁcations as test oracles [210].

4.3.1
Speciﬁed Test Oracle Challenges

Three challenges must be overcome to build
speciﬁed test oracles. The ﬁrst is the lack of a
formal speciﬁcation. Indeed, the other classes


---

## Page 13

of test oracles, discussed in this survey, all
address the problem of test oracle construction
in the absence of a formal speciﬁcation. Formal
speciﬁcations models necessarily rely on ab-
straction that can lead to the second problem:
imprecision, models that include infeasible be-
havior or that do not capture all the behav-
ior relevant to checking a speciﬁcation [68].
Finally, one must contend with the problem of
interpreting model output and equating it to
concrete program output.
Speciﬁed results are usually quite abstract,
and the concrete test results of a program’s ex-
ecutions may not be represented in a form that
makes checking their equivalence to the speci-
ﬁed result straightforward. Moreover, speciﬁed
results can be partially represented or over-
simpliﬁed. This is why Gaudel remarked that
the existence of a formal speciﬁcation does
not guarantee the existence of a successful test
driver [72]. Formulating concrete equivalence
functions may be necessary to correctly inter-
pret results [119]. In short, solutions to this
problem of equivalence across abstraction lev-
els depend largely on the degree of abstraction
and, to a lesser extent, on the implementation
of the system under test.

5
DERIVED TEST ORACLES

A derived test oracle distinguishes a system’s
correct from incorrect behavior based on in-
formation derived from various artefacts (e.g.
documentation, system executions) or proper-
ties of the system under test, or other versions
of it. Testers resort to derived test oracles when
speciﬁed test oracles are unavailable, which
is often the case, since speciﬁcations rapidly
fall out of date when they exist at all. Of
course, the derived test oracle might become
a partial “speciﬁed test oracle”, so that test
oracles derived by the methods discussed in
this section could migrate, over time, to be-
come, those considered to be the “speciﬁed test
oracles” of the previous section. For example,
JWalk incrementally learns algebraic properties

13

of the class under test [170]. It allows interac-
tive conﬁrmation from the tester, ensuring that
the human is in the “’learning loop”.
The following sections discuss research on
deriving test oracles from development arte-
facts, beginning in Section 5.1 with pseudo-
oracles and N-version programming, which
focus on agreement among independent imple-
mentations. Section 5.2 then introduces meta-
morphic relations which focuses on relations
that must hold among distinct executions of
a single implementation. Regression testing,
Section 5.3, focuses on relations that should
hold across different versions of the SUT.
Approaches for inferring models from sys-
tem executions, including invariant inference
and speciﬁcation mining, are described in Sec-
tion 5.4. Section 5.5 closes with a discussion of
research into extracting test oracle information
from textual documentation, like comments,
speciﬁcations, and requirements.

5.1
Pseudo-Oracles

One of the earliest versions of a derived test
oracle is the concept of a pseudo-oracle, intro-
duced by Davis and Weyuker [50], as a means
of addressing so-called non-testable programs:
“Programs which were written in or-
der to determine the answer in the
ﬁrst place. There would be no need
to write such programs, if the correct
answer were known.” [196].
A pseudo-oracle is an alternative version of
the program produced independently, e.g. by
a different programming team or written in
an entirely different programming language.
In our formalism (Section 2), a pseudo-oracle
is a test oracle D that accepts test activity
sequences of the form

f1(x)o1f2(x)o2 :[f1 ̸= f2 ∧o1 = o2],
(1)

where f1, f2 ∈C, the components of the SUT
(Section 2), are alternative, independently pro-
duced, versions of the SUT on the same value.
We draw the reader’s attention to the similarity


---

## Page 14

between pseudo-oracles and algebraic speci-
ﬁcation systems (Section 4.3), like DIASTIS,
where the function composition expression in
the implementation language and the term-
rewriting expression are distinct implementa-
tions whose output must agree and form a
pseudo-oracle.
A similar idea exists in fault-tolerant com-
puting, referred to as multi- or N-version pro-
gramming [13], [14], where the software is
implemented in multiple ways and executed
in parallel. Where results differ at run-time, a
“voting” mechanism decides which output to
use. In our formalism, an N-version test oracle
accepts test activities of the following form:

f1(x)o1f2(x)o2 · · · fk(x)ok :
[∀i, j ∈[1..k], i ̸= j ⇒fi ̸= fj
∧arg max
oi
m(oi) ≥t]
(2)

In Equation 2, the outputs form a multiset
and m is the multiplicity, or number of repeti-
tions of an element in the multiset. The arg max
operator ﬁnds the argument that maximizes a
function’s output, here an output with greatest
multiplicity. Finally, the maximum multiplicity
is compared against the threshold t. We can
now deﬁne a N-version test oracle as Dnv(w, x)
where w obeys Equation 2 with t bound to x.
Then Dmaj(w) = Dnv(w, ⌈k

2⌉) is an N-version
oracle that requires a majority of the outputs
to agree and Dpso(w) = Dnv(w, k) generalizes
pseudo oracles to agreement across k imple-
mentations.
More recently, Feldt [58] investigated the
possibility of automatically producing differ-
ent versions using genetic programming, and
McMinn [128] explored the idea of producing
different software versions for testing through
program transformation and the swapping of
different software elements with those of a
similar speciﬁcation.

5.2
Metamorphic Relations

For the SUT p that implements the function f,
a metamorphic relation is a relation over applica-

14

tions of f that we expect to hold across multiple
executions of p. Suppose f(x)
=
ex, then
eae−a = 1 is a metamorphic relation. Under
this metamorphic relation, p(0.3) * p(-0.3)
= 1 will hold if p is correct [43]. The key idea
is that reasoning about the properties of f will
lead us to relations that its implementation p
must obey.
Metamorphic testing is a process of exploiting
metamorphic relations to generate partial test
oracles for follow-up test cases: it checks im-
portant properties of the SUT after certain test
cases are executed [36]. Although metamorphic
relations are properties of the ground truth, the
correct phenomenon (f in the example above)
that a SUT seeks to implement and could be
considered a mechanism for creating speciﬁed
test oracles. We have placed them with derived
test oracles, because, in practice, metamorphic
relations are usually manually inferred from a
white-box inspection of a SUT.
Metamorphic relations differ from algebraic
speciﬁcations in that a metamorphic relation
relates different executions, not necessarily on
the same input, of the same implementation
relative to its speciﬁcation, while algebraic
speciﬁcations equates two distinct implementa-
tions of the speciﬁcation, one written in an im-
plementation language and the other written
in formalism free of implementation details,
usually term rewriting [15].
Under the formalism of Section 2, a meta-
morphic relation is

f(x1)o1f(x2)o2 · · · f(ik)ok :[expr ∧k ≥2],

where expr is a constraint, usually arithmetic,
over the inputs xi and ox. This deﬁnition
makes clear that a metamorphic relation is
a constraint on the values of stimulating the
single SUT f at least twice, observing the
responses, and imposing a constraint on how
they interrelate. In contrast, algebraic speciﬁ-
cation is a type of pseudo-oracle, as speciﬁed
in Equation 1, which stimulates two distinct
implementations on the same value, requiring
their output to be equivalent.


---

## Page 15

It is often thought that metamorphic rela-
tions need to concern numerical properties that
can be captured by arithmetic equations, but
metamorphic testing is, in fact, more general.
For example, Zhou et al. [209] used meta-
morphic testing to test search engines such
as Google and Yahoo!, where the relations
considered are clearly non-numeric. Zhou et
al. build metamorphic relations in terms of
the consistency of search results. A motivating
example they give is of searching for a paper
in the ACM digital library: two attempts, the
second quoted, using advanced search fail, but
a general search identical to the ﬁrst succeeds.
Using this insight, the authors build metamor-
phic relations, like ROR : A1 = (A2 ∪A3) ⇒
|A2| ≤|A1|, where the Ai are sets of web pages
returned by queries. Metamorphic testing is
also means of testing Weyuker’s “non-testable
programs”, introduced in the last section.
When the SUT is nondeterministic, such as
a classiﬁer whose exact output varies from run
to run, deﬁning metamorphic relations solely
in terms of output equality is usually insufﬁ-
cient during metamorphic testing. Murphy et
al. [139], [140] investigate relations other than
equality, like set intersection, to relate the out-
put of stochastic machine learning algorithms,
such as classiﬁers. Guderlei and Mayer intro-
duced statistical metamorphic testing, where
the relations for test output are checked us-
ing statistical analysis [80], a technique later
exploited to apply metamorphic testing to
stochastic optimisation algorithms [203].
The biggest challenge in metamorphic test-
ing is automating the discovery of metamor-
phic relations. Some of those in the literature
are mathematical [36], [37], [42] or combina-
torial [139], [140], [161], [203]. Work on the
discovery of algebraic speciﬁcations [88] and
JWalk’s lazy systematic unit testing, in which
the speciﬁcation is lazily, and incrementally,
learned through interactions between JWalk
and the developer [170] might be suitable for
adaptation to the discovery metamorphic re-
lations. For instance, the programmer’s devel-

15

opment environment might track relationships
among the output of test cases run during de-
velopment, and propose ones that hold across
many runs to the developer as possible meta-
morphic relations. Work has already begun
that exploits domain knowledge to formulate
metamorphic relations [38], but it is still at an
early stage and not yet automated.

5.3
Regression Test Suites

Regression testing aims to detect whether
the modiﬁcations made to the new version
of a SUT have disrupted existing functional-
ity [204]. It rests on the implicit assumption
that the previous version can serve as an oracle
for existing functionality.
For corrective modiﬁcations, desired func-
tionality remains the same so the test oracle
for version i, Di, can serve as the next ver-
sion’s test oracle, Di+1. Corrective modiﬁca-
tions may fail to correct the problem they seek
to address or disrupt existing functionality; test
oracles may be constructed for these issues
by symbolically comparing the execution of
the faulty version against the newer, allegedly
ﬁxed version [79]. Orstra generates assertion-
based test oracles by observing the program
states of the previous version while executing
the regression test suite [199]. The regression
test suite, now augmented with assertions, is
then applied to the newer version. Similarly,
spectra-based approaches use the program and
value spectra obtained from the original ver-
sion to detect regression faults in the newer
versions [86], [200].
For perfective modiﬁcations, those that add
new features to the SUT, Di must be modi-
ﬁed to cater for newly added behaviours, i.e.
Di+1 = Di ∪∆D. Test suite augmentation tech-
niques specialise in identifying and generating
∆D [6], [132], [202]. However, more work is
required to develop these augmentation tech-
niques so that they augment, not merely the
test input, but also the expected output. In this
way, test suite augmentation could be extended


---

## Page 16

to augment the existing oracles as well as the
test data.
Changes
in
the
speciﬁcation,
which
is
deemed to fail to meet requirements per-
haps because the requirements have them-
selves changed, drives another class of modiﬁ-
cations. These changes are generally regarded
as “perfective” maintenance in the literature
but no distinction is made between perfections
that add new functionality to code (without
changing requirements) and those changes that
arise due to changed requirements (or incorrect
speciﬁcations).
Our formalisation of test oracles in Section 2
forces a distinction of these two categories
of perfective maintenance, since the two have
profoundly different consequences for test or-
acles. We therefore refer to this new category
of perfective maintenance as “changed require-
ments”. Recall that, for the function f : X →Y ,
dom(f) = X. For changed requirements:

∃α · Di+1(α) ̸= Di(α),

which
implies,
of
course,
dom(Di+1) ∩
dom(Di) ̸= ∅and the new test oracle cannot
simply union the new behavior with the old
test oracle. Instead, we have

(
∆D
if α ∈dom(∆D)
Di
otherwise.

Di+1 =

5.4
System Executions

A system execution trace can be exploited to
derive test oracles or to reduce the cost of
a human test oracle by aligning an incorrect
execution against the expected execution, as
expressed in temporal logic [51]. This section
discusses the two main techniques for deriv-
ing test oracles from traces — invariant de-
tection and speciﬁcation mining. Derived test
oracles can be built on both techniques to au-
tomatically check expected behaviour similar
to assertion-based speciﬁcation, discussed in
Section 4.2.

16

5.4.1
Invariant Detection

Program
behaviours
can
be
automatically
checked against invariants. Thus, invariants
can serve as test oracles to help determine the
correct and incorrect outputs.
When invariants are not available for a pro-
gram in advance, they can be learned from the
program (semi-) automatically. A well-known
technique proposed by Ernst et al. [56], imple-
mented in the Daikon tool [55], is to execute a
program on a collection of inputs (test cases)
against a collection of potential invariants. The
invariants are instantiated by binding their
variables to the program’s variables. Daikon
then dynamically infers likely invariants from
those invariants not violated during the pro-
gram executions over the inputs. The inferred
invariants capture program behaviours, and
thus can be used to check program correct-
ness. For example, in regression testing, invari-
ants inferred from the previous version can be
checked as to whether they still hold in the
new version.
In our formalism, Daikon invariant detec-
tion can deﬁne an unsound test oracle that
gathers likely invariants from the preﬁx of a
testing activity sequence, then enforces those
invariants over its sufﬁx. Let Ij be the set of
likely invariants at observation j; I0 are the
initial invariants; for the test activity sequence
r1r2 · · · rn, In = {x ∈I | ∀i ∈[1..n], ri |=
x}, where |= is logical entailment. Thus, we
take an observation to deﬁne a binding of the
variables in the world under which a likely
invariant either holds or does not: only those
likely invariants remain that no observation
invalidates. In the sufﬁx rn+1rn+2 · · · rm, the
test oracle then changes gear and accepts only
those activities whose response observations
obey In, i.e. ri :[ri |= In], i > n.
Invariant detection can be computationally
expensive, so incremental [22], [171] and light
weight static analyses [39], [63] have been
brought to bear. A technical report summarises
various dynamic analysis techniques [158].
Model inference [90], [187] could also be re-


---

## Page 17

garded as a form of invariant generation in
which the invariant is expressed as a model
(typically as an FSM). Ratcliff et al. used
Search-Based Software Engineering (SBSE) [84]
to search for invariants, guided by mutation
testing [154].
The accuracy of inferred invariants depends
in part on the quality and completeness of the
test cases; additional test cases might provide
new data from which more accurate invariants
can be inferred [56]. Nevertheless, inferring
“perfect” invariants is almost impossible with
the current state of the art, which tends to fre-
quently infer incorrect or irrelevant invariants
[152]. Wei et al. recently leveraged existing con-
tracts in Eiffel code to infer postconditions on
commands (as opposed to queries) involving
quantiﬁcation or implications whose premises
are conjunctions of formulae [192], [193].
Human intervention can, of course, be used
to ﬁlter the resulting invariants, i.e., retaining
the correct ones and discarding the rest. How-
ever, manual ﬁltering is error-prone and the
misclassiﬁcation of invariants is frequent. In a
recent empirical study, Staats et al. found that
half of the incorrect invariants Daikon inferred
from a set of Java programs were misclassi-
ﬁed [175]. Despite these issues, research on the
dynamic inference of program invariants has
exhibited strong momentum in the recent past
with the primary focus on its application to test
generation [10], [142], [207].

5.4.2
Speciﬁcation Mining

Speciﬁcation mining or inference infers a for-
mal model of program behaviour from a set
of observations. In terms of our formalism, a
test oracle can enforce these formal models
over test activities. In her seminal work on
using inference to assess test data adequacy,
Weyuker connected inference and testing as in-
verse processes [194]. The testing process starts
with a program, and looks for I/O pairs that
characterise every aspect of both the intended
and actual behaviours, while inference starts
with a set of I/O pairs, and derives a program

17

to ﬁt the given behaviour. Weyuker deﬁned
this relation for assessing test adequacy which
can be stated informally as follows.
A set of I/O pairs T is an inference adequate
test set for the program P intended to fulﬁl
speciﬁcation S iff the program IT inferred from
T (using some inference procedure) is equiva-
lent to both P and S. Any difference would
imply that the inferred program is not equiva-
lent to the actual program and, therefore, that
the test set T used to infer the program P is
inadequate.
This inference procedure mainly depends
upon the set of I/O pairs used to infer be-
haviours. These pairs can be obtained from
system executions either passively, e.g., by run-
time monitoring, or actively, e.g., by querying
the system [106]. However, equivalence check-
ing is undecidable in general, and therefore
inference is only possible for programs in a
restricted class, such as those whose behaviour
can be modelled by ﬁnite state machines [194].
With this, equivalence can be accomplished by
experiment [89]. Nevertheless, serious practical
limitations are associated with such experi-
ments (see the survey by Lee and Yannakakis
[112] for complete discussion).
The marriage between inference and testing
has produced wealth of techniques, especially
in the context of “black-box” systems, when
source code/behavioural models are unavail-
able. Most work has applied L∗, a well-known
learning algorithm, to learn a black-box sys-
tem B as a ﬁnite state machine (FSM) with
n states [7]. The algorithm infers an FSM by
iteratively querying B and observing the cor-
responding outputs. A string distinguishes two
FSMs when only one of the two machines ends
in a ﬁnal state upon consuming the string. At
each iteration, an inferred model Mi with i < n
states is given. Then, the model is reﬁned with
the help of a string that distinguishes B and
Mi to produce a new model, until the number
of states reaches n.
Lee and Yannakakis [112] showed how to
use L∗for conformance testing of B with a


---

## Page 18

speciﬁcation S. Suppose L∗starts by inferring
a model Mi, then we compute a string that
distinguishes Mi from S and reﬁne Mi through
the algorithm. If, for i = n, Mn is S, then we
declare B to be correct, otherwise faulty.
Apart from conformance testing, inference
techniques have been used to guide test gen-
eration to focus on particular system behavior
and to reduce the scope of analysis. For exam-
ple, Li et al. applied L∗to the integration test-
ing of a system of black-box components [114].
Their analysis architecture derives a test oracle
from a test suite by using L∗to infer a model
of the systems from dynamically observing
system’s behavior; this model is then searched
to ﬁnd incorrect behaviors, such as deadlocks,
and used to verify the system’s behaviour un-
der fuzz testing (Section 6).
To ﬁnd concurrency issues in asynchronous
black-box systems, Groz et al. proposed an
approach that extracts behavioural models
from systems through active learning tech-
niques [78] and then performs reachability
analysis on the models [27] to detect issues,
notably races.
Further work in this context has been com-
piled by Shahbaz [166] with industrial ap-
plications. Similar applications of inference
can be found in system analysis [21], [78],
[135], [188], [189], component interaction test-
ing [115], [122], regression testing [200], se-
curity testing [168] and veriﬁcation [53], [77],
[148].
Zheng et al. [208] extract item sets from web
search queries and their results, then apply
association rule mining to infer rules. From
these rules, they construct derived test ora-
cles for web search engines, which had been
thought to be untestable. Image segmentation
delineates objects of interest in an image; im-
plementing segmentation programs is a te-
dious, iterative process. Frouchni et al. success-
fully apply semi-supervised machine learning
to create test oracles for image segmentation
programs [67]. Memon et al. [133], [134], [198]
introduced and developed the GUITAR tool,

18

which has been evaluated by treating the cur-
rent version of the SUT as correct, inferring the
speciﬁcation, and then executing the generated
test inputs. Artiﬁcial Neural Networks have
also been applied to learn system behaviour
and detect deviations from it [163], [164].
The majority of speciﬁcation mining tech-
niques adopt Finite State Machines as the out-
put format to capture the functional behaviour
of the SUT [21], [27], [53], [77], [78], [89], [112],
[114], [135], [148], [166], [168], [189], some-
times extended with temporal constraints [188]
or data constraints [115], [122] which are, in
turn, inferred by Daikon [56]. B¨uchi automata
have been used to check properties against
black-box systems [148]. Annotated call trees
have been used to represent the program be-
haviour of different versions in the regression
testing context [200]. GUI widgets have been
directly modelled with objects and properties
for testing [133], [134], [198]. Artiﬁcial Neu-
ral Nets and machine learning classiﬁers have
been used to learn the expected behaviour of
SUT [67], [163], [164]. For dynamic and fuzzy
behaviours such as the result of web search
engine queries, association rules between in-
put (query) and output (search result strings)
have been used as the format of an inferred
oracle [208].

5.5
Textual Documentation

Textual documentation ranges from natural
language descriptions of requirements to struc-
tured documents detailing the functionalities
of APIs. These documents describe the func-
tionalities expected from the SUT to varying
degrees, and can therefore serve as a basis
for generating test oracles. They are usually
informal, intended for other humans, not to
support formal logical or mathematical rea-
soning. Thus, they are often partial and am-
biguous, in contrast to speciﬁcation languages.
Their importance for test oracle construction
rests on the fact that developers are more likely
to write them than formal speciﬁcations. In
other words, the documentation deﬁnes the


---

## Page 19

constraints that the test oracle D, as deﬁned
in Section 2, enforces over testing activities.
At ﬁrst sight, it may seem impossible to
derive test oracles automatically because nat-
ural languages are inherently ambiguous and
textual documentation is often imprecise and
inconsistent. The use of textual documentation
has often been limited to humans in practical
testing applications [144]. However, some par-
tial automation can assist the human in testing
using documentation as a source of test oracle
information.
Two approaches have been explored. The
ﬁrst category builds techniques to construct a
formal speciﬁcation out of an informal, tex-
tual artefact, such as an informal textual spec-
iﬁcation, user and developer documentation,
and even source code comments. The second
restricts a natural language to a semi-formal
fragment amenable to automatic processing.
Next, we present representative examples of
each approach.

5.5.1
Converting Text into Speciﬁcations
Prowell and Poore [153] introduced a se-
quential enumeration method for developing
a formal speciﬁcation from an informal one.
The method systematically enumerates all se-
quences from the input domain and maps the
corresponding outputs to produce an arguably
complete, consistent, and correct speciﬁcation.
However, it can suffer from an exponential
explosion in the number of input/output se-
quences. Prowell and Poore employ abstraction
techniques to control this explosion. The end
result is a formal speciﬁcation that can be
transferred into a number of notations, e.g.,
state transition systems. A notable beneﬁt of
this approach is that it tends to discover many
inconsistent and missing requirements, making
the speciﬁcation more complete and precise.

5.5.2
Restricting Natural Language
Restrictions on a natural language reduce com-
plexities in its grammar and lexicon and allow
the expression of requirements in a concise

19

vocabulary with minimal ambiguity. This, in
turn, eases the interpretation of documents and
makes the automatic derivation of test oracles
possible. The researchers who have proposed
speciﬁcation languages based on (semi-) formal
subsets of a natural language are motivated
by the fact that model-based speciﬁcation lan-
guages have not seen wide-spread adoption,
and believe the reason is the inaccessibility
their formalism and set-theoretic underpin-
nings to the average programmer.
Schwitter
introduced
a
computer-
processable,
restricted
natural
language
called PENG [160]. It covers a strict subset of
standard English with a restricted grammar
and a domain speciﬁc lexicon for content
words
and
predeﬁned
function
words.
Documents written in PENG can be translated
deterministically
into
ﬁrst-order
predicate
logic. Schwitter et al. [30] provided guidelines
for writing test scenarios in PENG that can
automatically judge the correctness of program
behaviours.

6
IMPLICIT TEST ORACLES

An implicit test oracle is one that relies on
general, implicit knowledge to distinguish be-
tween a system’s correct and incorrect be-
haviour. This generally true implicit knowl-
edge includes such facts as “buffer overﬂows
and segfaults are nearly always errors”. The
critical aspect of an implicit test oracle is that it
requires neither domain knowledge nor a for-
mal speciﬁcation to implement, and it applies
to nearly all programs.
Implicit test oracle can be built on any proce-
dure that detects anomalies such as abnormal
termination due to a crash or an execution fail-
ure [34], [167]. This is because such anomalies
are blatant faults; that is, no more information
is required to ascertain whether the program
behaved correctly or not. Under our formalism,
an implicit oracle deﬁnes a subset of stimulus
and response relations as guaranteed failures,
in some context.


---

## Page 20

Implicit test oracles are not universal. Be-
haviours abnormal for one system in one con-
text may be normal for that system in a dif-
ferent context or normal for a different system.
Even crashing may be considered acceptable, or
even desired behaviour, as in systems designed
to ﬁnd crashes.
Research on implicit oracles is evident from
early work in software engineering. The very
ﬁrst work in this context was related to dead-
lock, livelock and race detection to counter
system concurrency issues [24] [107] [185]
[16] [169]. Similarly, research on testing non-
functional attributes have garnered much at-
tention since the advent of the object-oriented
paradigm.
In
performance
testing,
system
throughput metrics can highlight degradation
errors [121], [124], as when a server fails to
respond when a number of requests are sent
simultaneously. A case study by Weyuker and
Vokolos showed how a process with excessive
CPU usage caused service delays and disrup-
tions [195]. Similarly, test oracles for memory
leaks can be built on a proﬁling technique that
detects dangling references during the run of
a program [12], [57], [87], [211]. For example,
Xie and Aiken proposed a boolean constraint
system to represent the dynamically allocated
objects in a program [201]. Their system raises
an alarm when an object becomes unreachable
but has not yet been deallocated.
Fuzzing is an effective way to ﬁnd implicit
anomalies, such a crashes [137]. The main idea
is to generate random, or “fuzz”, inputs and
feed them to the system to ﬁnd anomalies.
This works because the implicit speciﬁcation
usually holds over all inputs, unlike explicit
speciﬁcations which tend to relate subsets of
inputs to outputs. If an anomaly is detected,
the fuzz tester reports it along with the input
that triggers it. Fuzzing is commonly used to
detect security vulnerabilities, such as buffer
overﬂows, memory leaks, unhandled excep-
tions, denial of service, etc. [18], [177].
Other work has focused on developing pat-
terns to detect anomalies. For instance, Ricca

20

and Tonella [155] considered a subset of the
anomalies that Web applications can harbor,
such as navigation problems, hyperlink incon-
sistencies, etc. In their empirical study, 60% of
the Web applications exhibited anomalies and
execution failures.

7
THE HUMAN ORACLE PROBLEM

The above sections give solutions to the test
oracle problem when some artefact exists that
can serve as the foundation for either a full or
partial test oracle. In many cases, however, no
such artefact exists so a human tester must ver-
ify whether software behaviour is correct given
some stimuli. Despite the lack of an automated
test oracle, software engineering research can
still play a key role: ﬁnding ways to reduce
the effort that the human tester has to expend
in directly creating, or in being, the test oracle.
This effort is referred to as the Human Oracle
Cost [126]. It aims to reduce the cost of human
involvement along two dimensions: 1) writing
test oracles and 2) evaluating test outcomes.
Concerning the ﬁrst dimension, the work of
Staats et al. is a representative. They seek to
reduce the human oracle cost by guiding hu-
man testers to those parts of the code they need
to focus on when writing test oracles [173].
This reduces the cost of test oracle construc-
tion, rather than reducing the cost of a human
involvement in testing in the absence of an au-
tomated test oracle. Additional recent work on
test oracle construction includes Dodona, a tool
that suggests oracle data to a human who then
decides whether to use it to deﬁne a test oracle
realized as a Java unit test [116]. Dodona infers
relations among program variables during ex-
ecution, using network centrality analysis and
data ﬂow.
Research that seeks to reduce the human
oracle cost broadly focuses on ﬁnding a quan-
titative reduction in the amount of work the
tester has to do for the same amount of test
coverage or ﬁnding a qualitative reduction in
the work needed to understand and evaluate
test cases.


---

## Page 21

7.1
Quantitative Human Oracle Cost

Test suites can be unnecessarily large, covering
few test goals in each individual test case.
Additionally, the test cases themselves may be
unnecessarily long — for example containing
large numbers of method calls, many of which
do not contribute to the overall test case. The
goal of quantitative human oracle cost reduction
is to reduce test suite and test case size so
as to maximise the beneﬁt of each test case
and each component of that test case. This
consequently reduces the amount of manual
checking effort that is required on behalf of
a human tester performing the role of a test
oracle. Cast in terms of our formalism, quan-
titative reduction aims to partition the set of
test activity sequences so the human need only
consider representative sequences, while test
case reduction aims to shorten test activity
sequences.

7.1.1
Test Suite Reduction

Traditionally, test suite reduction has been ap-
plied as a post-processing step to an existing
test suite, e.g. the work of Harrold et al, [85],
Offutt et al. [141] and Rothermel et al. [157]. Re-
cent work in the search-based testing literature
has sought to combine test input generation
and test suite reduction into one phase to
produce smaller test suites.
Harman et al. proposed a technique for gen-
erating test cases that penetrate the deepest
levels of the control dependence graph for
the program, in order to create test cases that
exercise as many elements of the program as
possible [82]. Ferrer et al. [61] attack a multi-
objective version of the problem in which they
sought to simultaneously maximize branch
coverage and minimize test suite size; their
focus was not this problem per se, but its use
to compare a number of multi-objective opti-
misation algorithms, including the well-known
Non-dominated Sorting Genetic Algorithm II
(NSGA-II), Strength Pareto EA 2 (SPEA2), and
MOCell. On a series of randomly-generated

21

programs and small benchmarks, they found
MOCell performed best.
Taylor et al. [178] use an inferred model as
a semantic test oracle to shrink a test suite.
Fraser and Arcuri [65] generate test suites for
Java using their EvoSuite tool. By generating
the entire suite at once, they are able to simulta-
neously maximize coverage and minimize test
suite size, thereby aiding human oracles and
alleviating the human oracle cost problem.

7.1.2
Test Case Reduction

When using randomised algorithms for gen-
erating test cases for object-oriented systems,
individual test cases can generate very long
traces very quickly — consisting of a large
number of method calls that do not actually
contribute to a speciﬁc test goal (e.g. the cov-
erage of a particular branch). Such method
calls unnecessarily increase test oracle cost,
so Leitner et al. remove such calls [113] us-
ing Zeller’s and Hildebrandt’s Delta Debug-
ging [206]. JWalk simpliﬁes test sequences by
removing side-effect free functions from them,
thereby reducing test oracle costs where the
human is the test oracle [170]. Quick tests
seek to efﬁciently spend a small test budget
by building test suites whose execution is fast
enough for it to be run after compilations [76].
These quick tests must be likely to trigger bugs
and therefore generate short traces, which, as
a result, are easier for humans to comprehend.

7.2
Qualitative Human Oracle Cost

Human oracle costs may also be minimised
from a qualitative perspective. That is, the
extent to which test cases, more generally test-
ing activities, may be easily understood and
processed by a human. The input proﬁle of
a SUT is the distribution of inputs it actually
processes when running in its operational en-
vironment. Learning an input proﬁle requires
domain knowledge. If such domain knowledge
is not built into the test data generation pro-
cess, machine-generated test data tend to be


---

## Page 22

drawn from a different distribution over the
SUT’s inputs than its input proﬁle. While this
may be beneﬁcial for trapping certain types
of faults, the utility of the approach decreases
when test oracle costs are taken into account,
since the tester must invest time comprehending
the scenario represented by test data in order to
correctly evaluate the corresponding program
output. Arbitrary inputs are much harder to
understand than recognisable pieces of data,
thus adding time to the checking process.
All approaches to qualitatively alleviating
the human oracle cost problem incorporate
human knowledge to improve the understand-
ability of test cases. The three approaches we
cover are 1) augmenting test suites designed by
the developers; 2) computing “realistic” inputs
from web pages, web services, and natural
language; and 3) mining usage patterns to
replicate them in the test cases.
In
order
to
improve
the
readability
of
automatically-generated test cases, McMinn et
al. propose the incorporation of human knowl-
edge into the test data generation process [126].
With search-based approaches, they proposed
injecting this knowledge by “seeding” the algo-
rithm with test cases that may have originated
from a human source such as a “sanity check”
performed by the programmer, an already ex-
isting, partial test suite, or input–output ex-
amples generated by programming paradigms
that involve the developer in computation, like
prorogued programming [2].
The generation of string test data is par-
ticularly problematic for automatic test data
generators, which tend to generate nonsensi-
cal strings. These nonsensical strings are, of
course, a form of fuzz testing (Section 6) and
good for exploring uncommon, shallow code
paths and ﬁnding corner cases, but they are
unlikely to exercise functionality deeper in a
program’s control ﬂow. This is because string
comparisons in control expressions are usually
stronger than numerical comparisons, making
one of a control point’s branches much less
likely to traverse via uniform fuzzing. We see

22

here the seminal computer science trade-off be-
tween breadth ﬁrst and depth ﬁrst search in the
choice between fuzz testing with nonsensical
inputs and testing with realistic inputs.
Bozkurt and Harman, introduced the idea of
mining web services for realistic test inputs,
using the outputs of known and trusted test
services as more realistic inputs to the service
under test [32]. The idea is that realistic test
cases are more likely to reveal faults that de-
velopers care about and yield test cases that
are more readily understood. McMinn et al.
also mine the web for realistic test cases. They
proposed mining strings from the web to assist
in the test generation process [130]. Since web
page content is generally the result of human
effort, the strings contained therein tend to be
real words or phrases with high degrees of
semantic and domain relevant context that can
thus be used as sources of realistic test data.
Afshan et al. [1] combine a natural language
model and metahueristics, strategies that guide
a search process [25], to help generate read-
able strings. The language model scores how
likely a string is to belong to a language based
on the character combinations. Incorporating
this probability score into a ﬁtness function,
a metaheuristic search can not only cover test
goals, but generate string inputs that are more
comprehensible than the arbitrary strings gen-
erated by the previous state of the art. Over
a number of case studies, Afshan et al. found
that human oracles more accurately and more
quickly evaluated their test strings.
Fraser and Zeller [66] improve the familiarity
of test cases by mining the software under test
for common usage patterns of APIs. They then
seek to replicate these patterns in generated
test cases. In this way, the scenarios generated
are more likely to be realistic and represent
actual usages of the software under test.

7.3
Crowdsourcing the Test Oracle

A recent approach to handling the lack of a
test oracle is to outsource the problem to an


---

## Page 23

online service to which large numbers of peo-
ple can provide answers — i.e., through crowd-
sourcing. Pastore et al. [147] demonstrated the
feasibility of the approach but noted problems
in presenting the test problem to the crowd
such that it could be easily understood, and the
need to provide sufﬁcient code documentation
so that the crowd could determine correct out-
puts from incorrect ones. In these experiments,
crowdsourcing was performed by submitting
tasks to a generic crowdsourcing platform —
Amazon’s Mechanical Turk4. However, some
dedicated crowdsourcing services now exist
for the testing of mobile applications. They
speciﬁcally address the problem of the explod-
ing number of devices on which a mobile
application may run, and which the developer
or tester may not own, but which may be
possessed by the crowd at large. Examples
of these services include Mob4Hire5, MobTest6

and uTest7.

8
FUTURE DIRECTIONS
AND CON-
CLUSION

This paper has provided a comprehensive sur-
vey of test oracles, covering speciﬁed, derived
and implicit oracles and techniques that cater
for the absence of test oracles. The paper has
also analyzed publication trends in the test ora-
cle domain. This paper has necessarily focused
on the traditional approaches to the test oracle
problem. Much work on test oracles remains to
be done. In addition to research deepening and
interconnecting these approaches, test oracle
problem is open to new research directions.
We close with a discussion of two of these that
we ﬁnd noteworthy and promising: test oracle
reuse and test oracle metrics.
As this survey has shown, test oracles are
difﬁcult to construct. Oracle reuse is therefore
an important problem that merits attention.

4. http://www.mturk.com
5. http://www.mob4hire.com
6. http://www.mobtest.com
7. http://www.utest.com/

23

Two promising approaches to oracle reuse are
generalizations of reliable reset and the sharing
of oracular data across software product lines
(SPLs). Generalizing reliable reset to arbitrary
states allows the interconnection of different
versions of a program, so we can build test
oracles that based on older versions of a pro-
gram, using generalized reliable reset to ignore
or handle new inputs and functionality. SPLs
are sets of related versions of a system [47].
A product line can be thought of as a tree of
related software products in which branches
contain new alternative versions of the system,
each of which shares some core functionality
enjoyed by a base version. Research on test
oracles should seek to leverage these SPL trees
to deﬁne trees of test oracles that share oracular
data where possible.
Work has already begun on using test ora-
cle as the measure of how well the program
has been tested (a kind of test oracle cover-
age) [104], [176], [186] and measures of oracles
such as assessing the quality of assertions [159].
More work is needed. “Oracle metrics” is a
challenge to, and an opportunity for, the “soft-
ware metrics” community. In a world in which
test oracles become more prevalent, it will be
important for testers to be able to assess the
features offered by alternative test oracles.
A repository of papers on test oracles accom-
panies this paper at nemo@utopia.com8.

9
ACKNOWLEDGEMENTS
We would like to thank Bob Binder for helpful
information and discussions when we began
work on this paper. We would also like thank
all who attended the CREST Open Workshop
on the Test Oracle Problem (21–22 May 2012) at
University College London, and gave feedback
on an early presentation of the work. We are
further indebted to the very many responses
to our emails from authors cited in this survey,
who provided several useful comments on an
earlier draft of our paper.

8. This repository will be made public when paper is
accepted.


---

## Page 24

REFERENCES

[1]
Sheeva Afshan, Phil McMinn, and Mark Stevenson.
Evolving readable string test inputs using a natural
language model to reduce human oracle cost. In In-
ternational Conference on Software Testing, Veriﬁcation
and Validation (ICST 2013). IEEE, March 2013.
[2]
Mehrdad Afshari, Earl T. Barr, and Zhendong Su.
Liberating the programmer with prorogued pro-
gramming.
In Proceedings of the ACM international
symposium on New ideas, new paradigms, and reﬂections
on programming and software, Onward! ’12, pages 11–
26, New York, NY, USA, 2012. ACM.
Track at
OOPSLA/SPLASH’12.
[3]
Wasif Afzal, Richard Torkar, and Robert Feldt.
A
systematic review of search-based testing for non-
functional system properties.
Information and Soft-
ware Technology, 51(6):957–976, 2009.
[4]
Bernhard K. Aichernig. Automated black-box testing
with abstract VDM oracles. In SAFECOMP, pages
250–259. Springer-Verlag, 1999.
[5]
Shaukat Ali, Lionel C. Briand, Hadi Hemmati, and
Rajwinder Kaur Panesar-Walawege.
A systematic
review of the application and empirical investigation
of search-based test-case generation. IEEE Transac-
tions on Software Engineering, pages 742–762, 2010.
[6]
Nadia Alshahwan and Mark Harman. Automated
session data repair for web application regression
testing. In Proceedings of 2008 International Conference
on Software Testing, Veriﬁcation, and Validation, pages
298–307. IEEE Computer Society, 2008.
[7]
Dana Angluin. Learning regular sets from queries
and counterexamples.
Inf. Comput., 75(2):87–106,
1987.
[8]
W. Araujo, L.C. Briand, and Y. Labiche.
Enabling
the runtime assertion checking of concurrent con-
tracts for the java modeling language. In Software
Engineering (ICSE), 2011 33rd International Conference
on, pages 786–795, 2011.
[9]
W. Araujo, L.C. Briand, and Y. Labiche.
On the
effectiveness of contracts as test oracles in the detec-
tion and diagnosis of race conditions and deadlocks
in concurrent object-oriented software. In Empirical
Software Engineering and Measurement (ESEM), 2011
International Symposium on, pages 10–19, 2011.
[10]
Shay Artzi, Michael D. Ernst, Adam Kie˙zun, Carlos
Pacheco, and Jeff H. Perkins. Finding the needles
in the haystack: Generating legal test inputs for
object-oriented programs. In 1st Workshop on Model-
Based Testing and Object-Oriented Systems (M-TOOS),
Portland, OR, October 23, 2006.
[11]
Egidio Astesiano, Michel Bidoit, H´el`ene Kirchner,
Bernd Krieg-Br¨uckner, Peter D. Mosses, Donald San-
nella, and Andrzej Tarlecki.
CASL: the common
algebraic speciﬁcation language. Theor. Comput. Sci.,
286(2):153–196, 2002.
[12]
Todd M. Austin, Scott E. Breach, and Gurindar S.
Sohi.
Efﬁcient detection of all pointer and array
access errors. In PLDI, pages 290–301. ACM, 1994.
[13]
A. Avizienis.
The N-version approach to fault-

24

tolerant software. IEEE Transactions on Software En-
gineering, 11:1491–1501, 1985.
[14]
A. Avizienis and L. Chen. On the implementation of
N-version programming for software fault-tolerance
during execution.
In Proceedings of the First Inter-
national Computer Software and Application Conference
(COMPSAC ’77), pages 149–155, 1977.
[15]
Franz Baader and Tobias Nipkow.
Term Rewriting
and All That. Cambridge University Press, New York,
NY, USA, 1998.
[16]
A. F. Babich.
Proving total correctness of parallel
programs.
IEEE Trans. Softw. Eng., 5(6):558–574,
November 1979.
[17]
Luciano Baresi and Michal Young. Test oracles. Tech-
nical Report CIS-TR-01-02, University of Oregon,
Dept. of Computer and Information Science, August
2001. http://www.cs.uoregon.edu/∼michal/pubs/
oracles.html.
[18]
Soﬁa Bekrar, Chaouki Bekrar, Roland Groz, and
Laurent Mounier.
Finding software vulnerabilities
by smart fuzzing. In ICST, pages 427–430, 2011.
[19]
Gilles Bernot. Testing against formal speciﬁcations:
a theoretical view. In Proceedings of the International
Joint Conference on Theory and Practice of Software
Development on Advances in Distributed Computing
(ADC) and Colloquium on Combining Paradigms for
Software Development (CCPSD): Vol. 2, TAPSOFT ’91,
pages 99–119, New York, NY, USA, 1991. Springer-
Verlag New York, Inc.
[20]
Gilles Bernot, Marie Claude Gaudel, and Bruno
Marre. Software testing based on formal speciﬁca-
tions: a theory and a tool. Softw. Eng. J., 6(6):387–405,
November 1991.
[21]
Antonia Bertolino, Paola Inverardi, Patrizio Pellic-
cione, and Massimo Tivoli. Automatic synthesis of
behavior protocols for composable web-services. In
Proceedings of ESEC/SIGSOFT FSE, ESEC/FSE 2009,
pages 141–150, 2009.
[22]
D. Beyer, T. Henzinger, R. Jhala, and R. Majumdar.
Checking memory safety with Blast. In M. Cerioli,
editor, Fundamental Approaches to Software Engineer-
ing, 8th International Conference, FASE 2005, Held as
Part of the Joint European Conferences on Theory and
Practice of Software, ETAPS 2005, Edinburgh, UK, April
4-8, 2005, Proceedings, volume 3442 of Lecture Notes
in Computer Science, pages 2–18. Springer, 2005.
[23]
R. Binder.
Testing Object-Oriented Systems: Models,
Patterns, and Tools. Addison-Wesley, 2000.
[24]
A. Blikle.
Proving programs by sets of compu-
tations.
In Mathematical Foundations of Computer
Science, pages 333–358. Springer, 1975.
[25]
Christian Blum and Andrea Roli. Metaheuristics in
combinatorial optimization: Overview and concep-
tual comparison. ACM Computing Surveys (CSUR),
35(3):268–308, 2003.
[26]
Gregor V. Bochmann and Alexandre Petrenko. Pro-
tocol testing: review of methods and relevance for
software testing.
In Proceedings of the 1994 ACM
SIGSOFT international symposium on Software testing
and analysis, ISSTA ’94, pages 109–124. ACM, 1994.
[27]
G.V. Bochmann. Finite state description of commu-


---

## Page 25

nication protocols. Computer Networks, 2(4):361–372,
1978.
[28]
E. B¨orger, A. Cavarra, and E. Riccobene. Modeling
the dynamics of UML state machines.
In Abstract
State Machines-Theory and Applications, pages 167–
186. Springer, 2000.
[29]
Egon B¨orger. High level system design and analysis
using abstract state machines. In Proceedings of the
International Workshop on Current Trends in Applied
Formal Method: Applied Formal Methods, FM-Trends
98, pages 1–43, London, UK, UK, 1999. Springer-
Verlag.
[30]
Kathrin B¨ottger, Rolf Schwitter, Diego Moll´a, and
Debbie Richards. Towards reconciling use cases via
controlled language and graphical models. In INAP,
pages 115–128, Berlin, Heidelberg, 2003. Springer-
Verlag.
[31]
F. Bouquet, C. Grandpierre, B. Legeard, F. Peureux,
N. Vacelet, and M. Utting.
A subset of precise
UML for model-based testing. In Proceedings of the
3rd International Workshop on Advances in Model-Based
Testing, A-MOST ’07, pages 95–104, New York, NY,
USA, 2007. ACM.
[32]
Mustafa Bozkurt and Mark Harman. Automatically
generating realistic test input from web services. In
IEEE 6th International Symposium on Service Oriented
System Engineering (SOSE), pages 13–24, 2011.
[33]
L. C. Briand, Y. Labiche, and H. Sun. Investigating
the use of analysis contracts to improve the testa-
bility of object-oriented code.
Softw. Pract. Exper.,
33(7):637–672, June 2003.
[34]
Cristian Cadar, Vijay Ganesh, Peter M. Pawlowski,
David L. Dill, and Dawson R. Engler. EXE: Auto-
matically generating inputs of death.
ACM Trans.
Inf. Syst. Secur., 12(2):10:1–10:38, December 2008.
[35]
J. Callahan, F. Schneider, S. Easterbrook, et al. Au-
tomated software testing using model-checking. In
Proceedings 1996 SPIN workshop, volume 353. Cite-
seer, 1996.
[36]
F. T. Chan, T. Y. Chen, S. C. Cheung, M. F. Lau,
and S. M. Yiu. Application of metamorphic testing
in numerical analysis. In Proceedings of the IASTED
International Conference on Software Engineering, pages
191–197, 1998.
[37]
W.K. Chan, S.C. Cheung, and Karl R.P.H. Leung.
A metamorphic testing approach for online testing of
service-oriented software applications, chapter 7, pages
2894–2914. IGI Global, 2009.
[38]
W.K. Chan, S.C. Cheung, and K.R.P.H. Leung.
Towards a metamorphic testing methodology for
service-oriented software applications.
In QSIC,
pages 470–476, September 2005.
[39]
F. Chen, N. Tillmann, and W. Schulte. Discovering
speciﬁcations.
Technical Report MSR-TR-2005-146,
Microsoft Research, October 2005.
[40]
Huo Yan Chen, T. H. Tse, F. T. Chan, and T. Y.
Chen. In black and white: an integrated approach to
class-level testing of object-oriented programs. ACM
Trans. Softw. Eng. Methodol., 7:250–295, July 1998.
[41]
Huo Yan Chen, T. H. Tse, and T. Y. Chen. TACCLE: a
methodology for object-oriented software testing at

25

the class and cluster levels. ACM Trans. Softw. Eng.
Methodol., 10(1):56–109, January 2001.
[42]
T. Y. Chen, F.-C. Kuo, T. H. Tse, and Zhi Quan Zhou.
Metamorphic testing and beyond.
In Proceedings
of the International Workshop on Software Technology
and Engineering Practice (STEP 2003), pages 94–100,
September 2004.
[43]
Tsong Chen, Dehao Huang, Haito Huang, Tsun-
Him Tse, Zong Yang, and Zhi Zhou. Metamorphic
testing and its applications. In Proceedings of the 8th
International Symposium on Future Software Technology,
ISFST 2004, pages 310–319, 2004.
[44]
Yoonsik Cheon. Abstraction in assertion-based test
oracles.
In Proceedings of the Seventh International
Conference on Quality Software, pages 410–414, Wash-
ington, DC, USA, 2007. IEEE Computer Society.
[45]
Yoonsik Cheon and Gary T. Leavens. A simple and
practical approach to unit testing: The JML and JUnit
way. In Proceedings of the 16th European Conference on
Object-Oriented Programming, ECOOP ’02, pages 231–
255, London, UK, 2002. Springer-Verlag.
[46]
L.A. Clarke.
A system to generate test data and
symbolically execute programs. Software Engineering,
IEEE Transactions on, SE-2(3):215 – 222, sept. 1976.
[47]
Paul C. Clements. Managing variability for software
product lines: Working with variability mechanisms.
In 10th International Conference on Software Product
Lines (SPLC 2006), pages 207–208, Baltimore, Mary-
land, USA, 2006. IEEE Computer Society.
[48]
Markus Clermont and David Parnas. Using informa-
tion about functions in selecting test cases. In Pro-
ceedings of the 1st international workshop on Advances
in model-based testing, A-MOST ’05, pages 1–7, New
York, NY, USA, 2005. ACM.
[49]
David Coppit and Jennifer M. Haddox-Schatz. On
the use of speciﬁcation-based assertions as test ora-
cles.
In Proceedings of the 29th Annual IEEE/NASA
on Software Engineering Workshop, pages 305–314,
Washington, DC, USA, 2005. IEEE Computer Society.
[50]
M. Davies and E. Weyuker. Pseudo-oracles for non-
testable programs.
In Proceedings of the ACM ’81
Conference, pages 254–257, 1981.
[51]
Laura K. Dillon. Automated support for testing and
debugging of real-time programs using oracles. SIG-
SOFT Softw. Eng. Notes, 25(1):45–46, January 2000.
[52]
Roong-Ko Doong and Phyllis G. Frankl.
The AS-
TOOT approach to testing object-oriented programs.
ACM Trans. Softw. Eng. Methodol., 3:101–130, April
1994.
[53]
Edith Elkind, Blaise Genest, Doron Peled, and
Hongyang Qu. Grey-box checking. In FORTE, pages
420–435, 2006.
[54]
J. Ellsberger, D. Hogrefe, and A. Sarma. SDL: for-
mal object-oriented language for communicating systems.
Prentice Hall, 1997.
[55]
M.D. Ernst, J.H. Perkins, P.J. Guo, S. McCamant,
C. Pacheco, M.S. Tschantz, and C. Xiao. The Daikon
system for dynamic detection of likely invariants.
Science of Computer Programming, 69(1):35–45, 2007.
[56]
Michael D. Ernst, Jake Cockrell, William G. Gris-
wold, and David Notkin. Dynamically discovering


---

## Page 26

likely program invariants to support program evo-
lution. IEEE Trans. Software Eng., 27(2):99–123, 2001.
[57]
R.A. Eyre-Todd. The detection of dangling references
in C++ programs. ACM Letters on Programming Lan-
guages and Systems (LOPLAS), 2(1-4):127–134, 1993.
[58]
R. Feldt. Generating diverse software versions with
genetic programming: an experimental study. Soft-
ware, IEE Proceedings, 145, December 1998.
[59]
Xin Feng, David Lorge Parnas, T. H. Tse, and Tony
O’Callaghan. A comparison of tabular expression-
based testing strategies.
IEEE Trans. Softw. Eng.,
37(5):616–634, September 2011.
[60]
Xin Feng, David Lorge Parnas, and T.H. Tse. Tabular
expression-based testing strategies: A comparison.
Testing: Academic and Industrial Conference Practice and
Research Techniques - MUTATION, 0:134, 2007.
[61]
J. Ferrer, F. Chicano, and E. Alba.
Evolutionary
algorithms for the multi-objective test data gen-
eration problem.
Software: Practice and Experience,
42(11):1331–1362, 2011.
[62]
John S. Fitzgerald and Peter Gorm Larsen. Modelling
Systems - Practical Tools and Techniques in Software
Development (2. ed.).
Cambridge University Press,
2009.
[63]
C. Flanagan and K. R. M. Leino.
Houdini, an
annotation assistant for ESC/Java. Lecture Notes in
Computer Science, 2021:500–517, 2001.
[64]
Robert W. Floyd. Assigning meanings to programs.
In J. T. Schwartz, editor, Mathematical Aspects of
Computer Science, volume 19 of Symposia in Applied
Mathematics, pages 19–32. American Mathematical
Society, Providence, RI, 1967.
[65]
Gordon Fraser and Andrea Arcuri. Whole test suite
generation. IEEE Transactions on Software Engineering,
39(2):276–291, 2013.
[66]
Gordon Fraser and Andreas Zeller. Exploiting com-
mon object usage in test case generation. In Proceed-
ings of the 2011 Fourth IEEE International Conference
on Software Testing, Veriﬁcation and Validation, ICST
’11, pages 80–89. IEEE Computer Society, 2011.
[67]
Kambiz Frounchi, Lionel C. Briand, Leo Grady, Yvan
Labiche, and Rajesh Subramanyan.
Automating
image segmentation veriﬁcation and validation by
learning test oracles. Information and Software Tech-
nology, 53(12):1337–1348, 2011.
[68]
Pascale Gall and Agns Arnould. Formal speciﬁca-
tions and test: Correctness and oracle.
In Magne
Haveraaen, Olaf Owe, and Ole-Johan Dahl, editors,
Recent Trends in Data Type Speciﬁcation, volume 1130
of Lecture Notes in Computer Science, pages 342–358.
Springer Berlin Heidelberg, 1996.
[69]
J. Gannon, P. McMullin, and R. Hamlet. Data ab-
straction, implementation, speciﬁcation, and testing.
ACM Transactions on Programming Languages and Sys-
tems (TOPLAS), 3(3):211–223, 1981.
[70]
Angelo Gargantini and Elvinia Riccobene.
ASM-
based testing: Coverage criteria and automatic test
sequence.
Journal of Universal Computer Science,
7(11):1050–1067, nov 2001.
[71]
Stephen J. Garland, John V. Guttag, and James J.
Horning.
An overview of Larch.
In Functional

26

Programming, Concurrency, Simulation and Automated
Reasoning, pages 329–348, 1993.
[72]
Marie-Claude Gaudel. Testing from formal speciﬁ-
cations, a generic approach. In Proceedings of the 6th
Ade-Europe International Conference Leuven on Reliable
Software Technologies, Ada Europe ’01, pages 35–48,
London, UK, 2001. Springer-Verlag.
[73]
Marie-Claude Gaudel and Perry R. James. Testing
algebraic data types and processes: A unifying the-
ory. Formal Asp. Comput., 10(5-6):436–451, 1998.
[74]
Gregory Gay, Sanjai Rayadurgam, and Mats Heim-
dah.
Improving the accuracy of oracle verdicts
through automated model steering.
In Automated
Software Engineering (ASE 2014). ACM Press, 2014.
[75]
Patrice Godefroid, Nils Klarlund, and Koushik Sen.
DART: directed automated random testing. In PLDI,
pages 213–223. ACM, 2005.
[76]
Alex Groce, Mohammad Amin Alipour, Chaoqiang
Zhang, Yang Chen, and John Regehr. Cause reduc-
tion for quick testing. In ICST, pages 243–252, 2014.
[77]
Alex Groce, Doron Peled, and Mihalis Yannakakis.
Amc: An adaptive model checker.
In CAV, pages
521–525, 2002.
[78]
Roland Groz, Keqin Li, Alexandre Petrenko, and
Muzammil Shahbaz.
Modular system veriﬁcation
by inference, testing and reachability analysis.
In
TestCom/FATES, pages 216–233, 2008.
[79]
Zhongxian Gu, Earl T. Barr, David J. Hamilton, and
Zhendong Su. Has the bug really been ﬁxed? In Pro-
ceedings of the 2010 International Conference on Software
Engineering (ICSE’10). IEEE Computer Society, 2010.
[80]
R. Guderlei and J. Mayer. Statistical metamorphic
testing testing programs with random output by
means of statistical hypothesis tests and metamor-
phic testing. In QSIC, pages 404–409, October 2007.
[81]
D. Harel.
Statecharts: A visual formalism for
complex systems. Science of computer programming,
8(3):231–274, 1987.
[82]
Mark Harman, Sung Gon Kim, Kiran Lakhotia, Phil
McMinn, and Shin Yoo. Optimizing for the num-
ber of tests generated in search based test data
generation with an application to the oracle cost
problem.
In International Workshop on Search-Based
Software Testing (SBST 2010), pages 182–191. IEEE, 6
April 2010.
[83]
Mark Harman, Afshin Mansouri, and Yuanyuan
Zhang. Search based software engineering: A com-
prehensive analysis and review of trends techniques
and applications. Technical Report TR-09-03, Depart-
ment of Computer Science, King’s College London,
April 2009.
[84]
Mark Harman, Phil McMinn, Jerffeson Teixeira de
Souza, and Shin Yoo. Search based software engi-
neering: Techniques, taxonomy, tutorial. In Bertrand
Meyer and Martin Nordio, editors, Empirical software
engineering and veriﬁcation: LASER 2009-2010, pages
1–59. Springer, 2012. LNCS 7007.
[85]
M. Jean Harrold, Rajiv Gupta, and Mary Lou Soffa.
A methodology for controlling the size of a test suite.
ACM Trans. Softw. Eng. Methodol., 2(3):270–285, July
1993.


---

## Page 27

[86]
Mary Jean Harrold, Gregg Rothermel, Kent Sayre,
Rui Wu, and Liu Yi.
An empirical investigation
of the relationship between spectra differences and
regression faults.
Software Testing, Veriﬁcation, and
Reliability, 10(3):171–194, 2000.
[87]
David L. Heine and Monica S. Lam. A practical ﬂow-
sensitive and context-sensitive C and C++ memory
leak detector. In PLDI, pages 168–181. ACM, 2003.
[88]
J. Henkel and A. Diwan.
Discovering algebraic
speciﬁcations from Java classes.
Lecture Notes in
Computer Science, 2743:431–456, 2003.
[89]
F.C. Hennie. Finite-state models for logical machines.
Wiley, 1968.
[90]
MarijnJ.H. Heule and Sicco Verwer. Software model
synthesis using satisﬁability solvers. Empirical Soft-
ware Engineering, pages 1–32, 2012.
[91]
R.M. Hierons. Oracles for distributed testing. Soft-
ware Engineering, IEEE Transactions on, 38(3):629–641,
2012.
[92]
Robert M. Hierons. Verdict functions in testing with
a fault domain or test hypotheses. ACM Trans. Softw.
Eng. Methodol., 18(4):14:1–14:19, July 2009.
[93]
Robert M. Hierons, Kirill Bogdanov, Jonathan P.
Bowen, Rance Cleaveland, John Derrick, Jeremy
Dick, Marian Gheorghe, Mark Harman, Kalpesh
Kapoor, Paul Krause, Gerald L¨uttgen, Anthony J. H.
Simons, Sergiy Vilkomir, Martin R. Woodward, and
Hussein Zedan.
Using formal speciﬁcations to
support testing.
ACM Comput. Surv., 41:9:1–9:76,
February 2009.
[94]
Charles Anthony Richard Hoare.
An Axiomatic
Basis of Computer Programming.
Communications
of the ACM, 12:576–580, 1969.
[95]
M. Holcombe. X-machines as a basis for dynamic
system speciﬁcation.
Software Engineering Journal,
3(2):69–76, 1988.
[96]
Mike Holcombe and Florentin Ipate.
Correct sys-
tems: building a business process solution. Software
Testing Veriﬁcation and Reliability, 9(1):76–77, 1999.
[97]
Gerard J. Holzmann. The model checker SPIN. IEEE
Trans. Softw. Eng., 23(5):279–295, May 1997.
[98]
W E Howden.
A functional approach to pro-
gram testing and analysis. IEEE Trans. Softw. Eng.,
12(10):997–1005, October 1986.
[99]
W.E. Howden.
Theoretical and empirical studies
of program testing.
IEEE Transactions on Software
Engineering, 4(4):293–298, July 1978.
[100] Merlin Hughes and David Stotts.
Daistish: sys-
tematic algebraic testing for OO programs in the
presence of side-effects. SIGSOFT Softw. Eng. Notes,
21(3):53–61, May 1996.
[101] Daniel Jackson. Software Abstractions: Logic, Language,
and Analysis. The MIT Press, 2006.
[102] Daniel Jackson. Software Abstractions: Logic, Language,
and Analysis. The MIT Press, 2006.
[103] Claude Jard and Gregor v. Bochmann. An approach
to testing speciﬁcations. Journal of Systems and Soft-
ware, 3(4):315 – 323, 1983.
[104] D. Jeffrey and R. Gupta.
Test case prioritization
using relevant slices. In Computer Software and Appli-

27

cations Conference, 2006. COMPSAC ’06. 30th Annual
International, volume 1, pages 411–420, 2006.
[105] Ying Jin and David Lorge Parnas.
Deﬁning the
meaning of tabular mathematical expressions. Sci.
Comput. Program., 75(11):980–1000, November 2010.
[106] M.J. Kearns and U.V. Vazirani.
An Introduction to
Computational Learning Theory. MIT Press, 1994.
[107] R.M. Keller. Formal veriﬁcation of parallel programs.
Communications of the ACM, 19(7):371–384, 1976.
[108] James C. King.
Symbolic execution and program
testing. Communications of the ACM, 19(7):385–394,
July 1976.
[109] Kiran Lakhotia, Phil McMinn, and Mark Harman.
An empirical investigation into branch coverage for
C programs using CUTE and AUSTIN.
Journal of
Systems and Software, 83(12):2379–2391, 2010.
[110] Axel van Lamsweerde.
Formal speciﬁcation: a
roadmap.
In Proceedings of the Conference on The
Future of Software Engineering, ICSE ’00, pages 147–
159, New York, NY, USA, 2000. ACM.
[111] K. Lano and H. Haughton.
Speciﬁcation in B: An
Introduction Using the B Toolkit.
Imperial College
Press, 1996.
[112] D. Lee and M. Yannakakis. Principles and methods
of testing ﬁnite state machines—a survey. Proceedings
of the IEEE, 84(8):1090–1123, aug 1996.
[113] A. Leitner, M. Oriol, A Zeller, I. Ciupa, and B. Meyer.
Efﬁcient unit test case minimization. In Automated
Software Engineering (ASE 2007), pages 417–420, At-
lanta, Georgia, USA, 2007. ACM Press.
[114] Keqin Li, Roland Groz, and Muzammil Shahbaz.
Integration testing of components guided by incre-
mental state machine learning. In TAIC PART, pages
59–70, 2006.
[115] D. Lorenzoli, L. Mariani, and M. Pezz`e. Automatic
generation of software behavioral models.
In pro-
ceedings of the 30th International Conference on Software
Engineering (ICSE), 2008.
[116] Pablo Loyola, Matthew Staats, In-Young Ko, and
Gregg Rothermel. Dodona: Automated oracle data
set selection. In International Symposium on Software
Testing and Analysis 2014, ISSTA’04, 2014.
[117] D. Luckham and F.W. Henke.
An overview of
ANNA-a speciﬁcation language for ADA. Technical
report, Stanford University, 1984.
[118] Nancy A. Lynch and Mark R. Tuttle. An introduction
to input/output automata. CWI Quarterly, 2:219–246,
1989.
[119] Patr´ıcia D. L. Machado.
On oracles for interpret-
ing test results against algebraic speciﬁcations.
In
AMAST, pages 502–518. Springer-Verlag, 1999.
[120] Phil Maker.
GNU Nana: improved support for
assertion checking and logging in GNU C/C++,
1998. http://gnu.cs.pu.edu.tw/software/nana/.
[121] Haroon Malik, Hadi Hemmati, and Ahmed E. Has-
san. Automatic detection of performance deviations
in the load testing of large scale systems. In Proceed-
ings of International Conference on Software Engineering
- Software Engineering in Practice Track, ICSE 2013,
page to appear, 2013.


---

## Page 28

[122] L. Mariani, F. Pastore, and M. Pezz`e.
Dynamic
analysis for diagnosing integration faults.
IEEE
Transactions on Software Engineering, 37(4):486–508,
2011.
[123] Bruno Marre.
Loft: A tool for assisting selection
of test data sets from algebraic speciﬁcations.
In
TAPSOFT, pages 799–800. Springer-Verlag, 1995.
[124] A.P. Mathur. Performance, effectiveness, and relia-
bility issues in software testing. In COMPSAC, pages
604–605. IEEE, 1991.
[125] Johannes Mayer, Ralph Guderlei, Abteilung Angew,
Te Informationsverarbeitung, Abteilung Stochastik,
and Universitt Ulm.
Test oracles using statistical
methods. In In: Proceedings of the First International
Workshop on Software Quality, Lecture Notes in Infor-
matics P-58, Kllen Druck+Verlag GmbH, pages 179–
189. Springer, 2004.
[126] P. McMinn, M. Stevenson, and M. Harman. Reduc-
ing qualitative human oracle costs associated with
automatically generated test data. In 1st International
Workshop on Software Test Output Validation (STOV
2010), Trento, Italy, 13th July 2010, pages 1–4, 2010.
[127] Phil McMinn. Search-based software test data gen-
eration: a survey. Softw. Test. Verif. Reliab., 14(2):105–
156, June 2004.
[128] Phil McMinn.
Search-based failure discovery us-
ing testability transformations to generate pseudo-
oracles.
In Genetic and Evolutionary Computation
Conference (GECCO 2009), pages 1689–1696. ACM
Press, 8-12 July 2009.
[129] Phil McMinn. Search-based software testing: Past,
present and future.
In International Workshop on
Search-Based Software Testing (SBST 2011), pages 153–
163. IEEE, 21 March 2011.
[130] Phil
McMinn,
Muzammil
Shahbaz,
and
Mark
Stevenson.
Search-based test input generation for
string data types using the results of web queries.
In ICST, pages 141–150, 2012.
[131] Phil McMinn, Mark Stevenson, and Mark Harman.
Reducing qualitative human oracle costs associated
with automatically generated test data.
In Inter-
national Workshop on Software Test Output Validation
(STOV 2010), pages 1–4. ACM, 13 July 2010.
[132] Atif M. Memon.
Automatically repairing event
sequence-based GUI test suites for regression test-
ing.
ACM Transactions on Software Engineering
Methodology, 18(2):1–36, 2008.
[133] Atif M. Memon, Martha E. Pollack, and Mary Lou
Soffa. Automated test oracles for GUIs. In SIGSOFT
’00/FSE-8: Proceedings of the 8th ACM SIGSOFT inter-
national symposium on Foundations of software engineer-
ing, pages 30–39, New York, NY, USA, 2000. ACM
Press.
[134] Atif M. Memon and Qing Xie.
Using tran-
sient/persistent errors to develop automated test
oracles for event-driven software. In ASE ’04: Pro-
ceedings of the 19th IEEE international conference on
Automated software engineering, pages 186–195, Wash-
ington, DC, USA, 2004. IEEE Computer Society.
[135] Maik Merten, Falk Howar, Bernhard Steffen, Pa-
trizio Pellicione, and Massimo Tivoli.
Automated

28

inference of models for black box systems based
on interface descriptions.
In Proceedings of the 5th
international conference on Leveraging Applications of
Formal Methods, Veriﬁcation and Validation: technologies
for mastering change - Volume Part I, ISoLA’12, pages
79–96. Springer-Verlag, 2012.
[136] Bertrand Meyer. Eiffel: A language and environment
for software engineering. The Journal of Systems and
Software, 8(3):199–246, June 1988.
[137] B.P. Miller, L. Fredriksen, and B. So. An empirical
study of the reliability of UNIX utilities. Communi-
cations of the ACM, 33(12):32–44, 1990.
[138] S.
Mouchawrab,
L.C.
Briand,
Y.
Labiche,
and
M. Di Penta. Assessing, comparing, and combining
state machine-based testing and structural testing:
A series of experiments. Software Engineering, IEEE
Transactions on, 37(2):161–187, 2011.
[139] Christian Murphy, Kuang Shen, and Gail Kaiser.
Automatic system testing of programs without test
oracles. In ISSTA, pages 189–200. ACM Press, 2009.
[140] Christian Murphy, Kuang Shen, and Gail Kaiser.
Using JML runtime assertion checking to automate
metamorphic testing in applications without test or-
acles. 2009 International Conference on Software Testing
Veriﬁcation and Validation, pages 436–445, 2009.
[141] A. J. Offutt, J. Pan, and J. M. Voas. Procedures for
reducing the size of coverage-based test sets.
In
International Conference on Testing Computer Software,
pages 111–123, 1995.
[142] C. Pacheco and M. Ernst. Eclat: Automatic genera-
tion and classiﬁcation of test inputs. ECOOP 2005-
Object-Oriented Programming, pages 734–734, 2005.
[143] D L Parnas, J Madey, and M Iglewski.
Precise
documentation of well-structured programs.
IEEE
Transactions on Software Engineering, 20(12):948–976,
1994.
[144] David Lorge Parnas.
Document based rational
software development.
Journal of Knowledge Based
Systems, 22:132–141, April 2009.
[145] David Lorge Parnas.
Precise documentation: The
key to better software.
In Sebastian Nanz, editor,
The Future of Software Engineering, pages 125–148.
Springer Berlin Heidelberg, 2011.
[146] David Lorge Parnas and Jan Madey. Functional doc-
uments for computer systems. Sci. Comput. Program.,
25(1):41–61, October 1995.
[147] F. Pastore, L. Mariani, and G. Fraser. Crowdoracles:
Can the crowd solve the oracle problem? In Proceed-
ings of the International Conference on Software Testing,
Veriﬁcation and Validation (ICST), 2013.
[148] Doron Peled, Moshe Y. Vardi, and Mihalis Yan-
nakakis.
Black box checking.
Journal of Automata,
Languages and Combinatorics, 7(2), 2002.
[149] D K Peters and D L Parnas. Using test oracles gen-
erated from program documentation. IEEE Transac-
tions on Software Engineering, 24(3):161–173, 1998.
[150] Dennis
K.
Peters
and
David
Lorge
Parnas.
Requirements-based monitors for real-time systems.
IEEE Trans. Softw. Eng., 28(2):146–158, February
2002.


---

## Page 29

[151] Mauro Pezz`e and Cheng Zhang.
Automated test
oracles: A survey. In Ali Hurson and Atif Memon,
editors, Advances in Computers, volume 95, pages 1–
48. Elsevier Ltd., 2014.
[152] Nadia Polikarpova, Ilinca Ciupa, and Bertrand
Meyer. A comparative study of programmer-written
and automatically inferred contracts.
In ISSTA,
pages 93–104. ACM, 2009.
[153] S.J.
Prowell
and
J.H.
Poore.
Foundations
of
sequence-based software speciﬁcation. Software En-
gineering, IEEE Transactions on, 29(5):417–429, 2003.
[154] Sam Ratcliff, David R. White, and John A. Clark.
Searching for invariants using genetic programming
and mutation testing. In Proceedings of the 13th annual
conference on Genetic and evolutionary computation,
GECCO ’11, pages 1907–1914, New York, NY, USA,
2011. ACM.
[155] F. Ricca and P. Tonella. Detecting anomaly and fail-
ure in web applications. MultiMedia, IEEE, 13(2):44
– 51, april-june 2006.
[156] D.S. Rosenblum. A practical approach to program-
ming with assertions.
Software Engineering, IEEE
Transactions on, 21(1):19–31, 1995.
[157] G. Rothermel, M. J. Harrold, J. von Ronne, and
C. Hong. Empirical studies of test-suite reduction.
Software Testing, Veriﬁcation and Reliability, 12:219—
249, 2002.
[158] N. Walkinshaw S. Ali, K. Bogdanov. A comparative
study of methods for dynamic reverse-engineering
of state models.
Technical Report CS-07-16, The
University of Shefﬁeld, Department of Computer
Science, October 2007. http://www.dcs.shef.ac.uk/
intranet/research/resmes/CS0716.pdf.
[159] David Schuler and Andreas Zeller. Assessing oracle
quality with checked coverage. In Proceedings of the
2011 Fourth IEEE International Conference on Software
Testing, Veriﬁcation and Validation, ICST ’11, pages
90–99, Washington, DC, USA, 2011. IEEE Computer
Society.
[160] R. Schwitter.
English as a formal speciﬁcation
language.
In Database and Expert Systems Applica-
tions, 2002. Proceedings. 13th International Workshop
on, pages 228–232, sept. 2002.
[161] Sergio Segura, Robert M. Hierons, David Benavides,
and Antonio Ruiz-Cort´es. Automated metamorphic
testing on the analyses of feature models. Information
and Software Technology, 53(3):245 – 258, 2011.
[162] Koushik Sen, Darko Marinov, and Gul Agha. CUTE:
a concolic unit testing engine for C. In ESEC/FSE,
pages 263–272. ACM, 2005.
[163] Seyed Shahamiri, Wan Wan-Kadir, Suhaimi Ibrahim,
and Siti Hashim. Artiﬁcial neural networks as multi-
networks automated test oracle. Automated Software
Engineering, 19(3):303–334, 2012.
[164] Seyed Reza Shahamiri, Wan Mohd Nasir Wan Kadir,
Suhaimi Ibrahim, and Siti Zaiton Mohd Hashim.
An automated framework for software test oracle.
Information and Software Technology, 53(7):774 – 788,
2011.
[165] Seyed Reza Shahamiri, Wan Mohd Nasir Wan-Kadir,
and Siti Zaiton Mohd Hashim. A comparative study

29

on automated software test oracle methods.
In
ICSEA, pages 140–145, 2009.
[166] M. Shahbaz. Reverse Engineering and Testing of Black-
Box Software Components.
LAP Lambert Academic
Publishing, 2012.
[167] K. Shrestha and M.J. Rutherford.
An empirical
evaluation of assertions as oracles. In ICST, pages
110–119. IEEE, 2011.
[168] Guoqiang Shu, Yating Hsu, and David Lee.
De-
tecting communication protocol security ﬂaws by
formal fuzz testing and machine learning. In FORTE,
pages 299–304, 2008.
[169] J. Sifakis. Deadlocks and livelocks in transition sys-
tems. Mathematical Foundations of Computer Science
1980, pages 587–600, 1980.
[170] A. J. H. Simons. JWalk: a tool for lazy systematic
testing of java classes by design introspection and
user interaction.
Automated Software Engineering,
14(4):369–418, December 2007.
[171] Rishabh Singh, Dimitra Giannakopoulou, and Co-
rina S. Pasareanu.
Learning component interfaces
with may and must abstractions. In Tayssir Touili,
Byron Cook, and Paul Jackson, editors, Computer
Aided Veriﬁcation, 22nd International Conference, CAV
2010, Edinburgh, UK, July 15-19, 2010. Proceedings,
volume 6174 of Lecture Notes in Computer Science,
pages 527–542. Springer, 2010.
[172] J. Michael Spivey. Z Notation - a reference manual (2.
ed.). Prentice Hall International Series in Computer
Science. Prentice Hall, 1992.
[173] M. Staats, G. Gay, and M. P. E. Heimdahl.
Auto-
mated oracle creation support, or: How I learned to
stop worrying about fault propagation and love mu-
tation testing. In Proceedings of the 34th International
Conference on Software Engineering, ICSE 2012, pages
870–880, 2012.
[174] M. Staats, M.W. Whalen, and M.P.E. Heimdahl. Pro-
grams, tests, and oracles: the foundations of testing
revisited. In ICSE, pages 391–400. IEEE, 2011.
[175] Matt Staats, Shin Hong, Moonzoo Kim, and Gregg
Rothermel. Understanding user understanding: de-
termining correctness of generated program invari-
ants. In ISSTA, pages 188–198. ACM, 2012.
[176] Matt Staats, Pablo Loyola, and Gregg Rothermel.
Oracle-centric test case prioritization. In Proceedings
of the 23rd International Symposium on Software Relia-
bility Engineering, ISSRE 2012, pages 311–320, 2012.
[177] Ari Takanen, Jared DeMott, and Charlie Miller.
Fuzzing for Software Security Testing and Quality As-
surance. Artech House, Inc., Norwood, MA, USA, 1
edition, 2008.
[178] Ramsay Taylor, Mathew Hall, Kirill Bogdanov, and
John Derrick. Using behaviour inference to optimise
regression test sets.
In Brian Nielsen and Carsten
Weise, editors, Testing Software and Systems - 24th IFIP
WG 6.1 International Conference, ICTSS 2012, Aalborg,
Denmark, November 19-21, 2012. Proceedings, volume
7641 of Lecture Notes in Computer Science, pages 184–
199. Springer, 2012.
[179] A. Tiwari. Formal semantics and analysis methods
for Simulink Stateﬂow models. Technical report, SRI


---

## Page 30

International, 2002. http://www.csl.sri.com/users/
tiwari/html/stateﬂow.html.
[180] Jan Tretmans. Test generation with inputs, outputs
and repetitive quiescence.
Software - Concepts and
Tools, 17(3):103–120, 1996.
[181] Alan M. Turing. Checking a large routine. In Report
of a Conference on High Speed Automatic Calculating
Machines, pages 67–69, Cambridge, England, June
1949. University Mathematical Laboratory.
[182] Mark Utting and Bruno Legeard.
Practical Model-
Based Testing: A Tools Approach. Morgan Kaufmann
Publishers Inc., San Francisco, CA, USA, 2007.
[183] Mark Utting, Alexander Pretschner, and Bruno Leg-
eard.
A taxonomy of model-based testing ap-
proaches.
Softw. Test. Verif. Reliab., 22(5):297–312,
August 2012.
[184] G. v. Bochmann, C. He, and D. Ouimet.
Protocol
testing using automatic trace analysis.
In Proceed-
ings of Canadian Conference on Electrical and Computer
Engineering, pages 814–820, 1989.
[185] A. van Lamsweerde and M. Sintzoff. Formal deriva-
tion of strongly correct concurrent programs. Acta
Informatica, 12(1):1–31, 1979.
[186] J.M. Voas. PIE: a dynamic failure-based technique.
Software Engineering, IEEE Transactions on, 18(8):717–
727, 1992.
[187] N. Walkinshaw, K. Bogdanov, J. Derrick, and J. Paris.
Increasing functional coverage by inductive testing:
A case study.
In Alexandre Petrenko, Adenilso
da Silva Sim˜ao, and Jos´e Carlos Maldonado, edi-
tors, Testing Software and Systems - 22nd IFIP WG
6.1 International Conference, ICTSS 2010, Natal, Brazil,
November 8-10, 2010. Proceedings, volume 6435 of
Lecture Notes in Computer Science, pages 126–141.
Springer, 2010.
[188] Neil Walkinshaw and Kirill Bogdanov.
Inferring
ﬁnite-state models with temporal constraints.
In
ASE, pages 248–257, 2008.
[189] Neil Walkinshaw, John Derrick, and Qiang Guo.
Iterative reﬁnement of reverse-engineered models by
model-based testing. In FM, pages 305–320, 2009.
[190] Yabo Wang and DavidLorge Parnas. Trace rewriting
systems.
In Micha¨el Rusinowitch and Jean-Luc
R´emy, editors, Conditional Term Rewriting Systems,
volume 656 of Lecture Notes in Computer Science,
pages 343–356. Springer Berlin Heidelberg, 1993.
[191] Yabo Wang and D.L. Parnas.
Simulating the be-
haviour of software modules by trace rewriting. In
Software Engineering, 1993. Proceedings., 15th Interna-
tional Conference on, pages 14–23, 1993.
[192] Yi Wei, Carlo A. Furia, Nikolay Kazmin, and
Bertrand Meyer. Inferring better contracts. In Pro-
ceedings of the 33rd International Conference on Software
Engineering, ICSE ’11, pages 191–200, New York, NY,
USA, 2011. ACM.
[193] Yi Wei, H. Roth, C.A. Furia, Yu Pei, A. Horton,
M. Steindorfer, M. Nordio, and B. Meyer. Stateful
testing: Finding more errors in code and contracts.
In Automated Software Engineering (ASE), 2011 26th
IEEE/ACM International Conference on, pages 440–443,
2011.

30

[194] E.J. Weyuker. Assessing test data adequacy through
program inference.
ACM Transactions on Program-
ming Languages and Systems (TOPLAS), 5(4):641–655,
1983.
[195] E.J. Weyuker and F.I. Vokolos.
Experience with
performance testing of software systems: issues, an
approach, and case study. Software Engineering, IEEE
Transactions on, 26(12):1147–1156, 2000.
[196] Elaine J. Weyuker. On testing non-testable programs.
The Computer Journal, 25(4):465–470, November 1982.
[197] Jeannette M. Wing.
A speciﬁer’s introduction to
formal methods. IEEE Computer, 23(9):8–24, 1990.
[198] Qing Xie and Atif M. Memon.
Designing and
comparing automated test oracles for GUI-based
software applications. ACM Transactions on Software
Engineering and Methodology, 16(1):4, 2007.
[199] Tao Xie. Augmenting automatically generated unit-
test suites with regression oracle checking. In Proc.
20th European Conference on Object-Oriented Program-
ming (ECOOP 2006), pages 380–403, July 2006.
[200] Tao Xie and David Notkin. Checking inside the black
box: Regression testing by comparing value spectra.
IEEE Transactions on Software Engineering, 31(10):869–
883, October 2005.
[201] Yichen Xie and Alex Aiken.
Context-and path-
sensitive memory leak detection.
ACM SIGSOFT
Software Engineering Notes, 30(5):115–125, 2005.
[202] Zhihong Xu, Yunho Kim, Moonzoo Kim, Gregg
Rothermel, and Myra B. Cohen. Directed test suite
augmentation: techniques and tradeoffs.
In Pro-
ceedings of the eighteenth ACM SIGSOFT international
symposium on Foundations of software engineering, FSE
’10, pages 257–266, New York, NY, USA, 2010. ACM.
[203] Shin Yoo. Metamorphic testing of stochastic optimi-
sation. In Proceedings of the 2010 Third International
Conference on Software Testing, Veriﬁcation, and Vali-
dation Workshops, ICSTW ’10, pages 192–201. IEEE
Computer Society, 2010.
[204] Shin Yoo and Mark Harman.
Regression testing
minimisation, selection and prioritisation: A survey.
Software Testing, Veriﬁcation, and Reliability, 22(2):67–
120, March 2012.
[205] Bo Yu, Liang Kong, Yufeng Zhang, and Hong Zhu.
Testing Java components based on algebraic speciﬁ-
cations. Software Testing, Veriﬁcation, and Validation,
2008 International Conference on, 0:190–199, 2008.
[206] A. Zeller and R Hildebrandt. Simplifying and iso-
lating failure-inducing input.
IEEE Transactions on
Software Engineering, 28(2):183–200, 2002.
[207] S. Zhang, D. Saff, Y. Bu, and M.D. Ernst. Combined
static and dynamic automated test generation.
In
ISSTA, volume 11, pages 353–363, 2011.
[208] Wujie Zheng, Hao Ma, Michael R. Lyu, Tao Xie,
and Irwin King. Mining test oracles of web search
engines. In Proc. 26th IEEE/ACM International Con-
ference on Automated Software Engineering (ASE 2011),
Short Paper, ASE 2011, pages 408–411, 2011.
[209] Zhi Quan Zhou, ShuJia Zhang, Markus Hagenbuch-
ner, T. H. Tse, Fei-Ching Kuo, and T. Y. Chen. Au-
tomated functional testing of online search services.


---

## Page 31

Software Testing, Veriﬁcation and Reliability, 22(4):221–
243, 2012.
[210] Hong Zhu.
A note on test oracles and semantics
of algebraic speciﬁcations.
In Proceedings of the
3rd International Conference on Quality Software, QSIC
2003, pages 91–98, 2003.
[211] B. Zorn and P. Hilﬁnger.
A memory allocation
proﬁler for C and Lisp programs. In Proceedings of
the Summer USENIX Conference, pages 223–237, 1988.

31


---

