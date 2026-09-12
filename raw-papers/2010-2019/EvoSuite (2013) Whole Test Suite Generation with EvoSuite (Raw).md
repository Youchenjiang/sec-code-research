---
title: "Whole Test Suite Generation with EvoSuite"
year: 2013
author: "Research Team"
source_pdf: "EvoSuite (2013) Whole Test Suite Generation with EvoSuite.pdf"
---

<!-- Page 1 -->

Whole Test Suite Generation
Gordon Fraser, Member, IEEE and Andrea Arcuri, Member, IEEE.
✦
Abstract—Not all bugs lead to program crashes, and not always is
there a formal speciﬁcation to check the correctness of a software test’s
outcome. A common scenario in software testing is therefore that test
data is generated, and a tester manually adds test oracles. A s this
is a difﬁcult task, it is important to produce small yet repre sentative
test sets, and this representativeness is typically measur ed using code
coverage. There is, however, a fundamental problem with the common
approach of targeting one coverage goal at a time: Coverage g oals
are not independent, not equally difﬁcult, and sometimes in feasible –
the result of test generation is therefore dependent on the o rder of
coverage goals and how many of them are feasible. To overcome this
problem, we propose a novel paradigm in which whole test suites are
evolved with the aim of covering all coverage goals at the same time,
while keeping the total size as small as possible. This appro ach has
several advantages, as for example its effectiveness is not affected by
the number of infeasible targets in the code. We have implemented this
novel approach in the EVOSUITE tool, and compared it to the common
approach of addressing one goal at a time. Evaluated on open s ource
libraries and an industrial case study for a total of 1,741 cl asses, we
show that EVOSUITE achieved up to 188 times the branch coverage of
a traditional approach targeting single branches, with up to 62% smaller
test suites.
Index Terms—Search based software engineering, length, branch cov-
erage, genetic algorithm, infeasible goal, collateral coverage

## 1 I NTRODUCTION

I
T is widely recognized that software testing is an essential
component of any successful software development process.
A software test consists of an input that executes the progra m
and a deﬁnition of the expected outcome. Many techniques
to automatically produce inputs have been proposed over the
years, and today are able to produce test suites with high cod e
coverage. Yet, the problem of the expected outcome persists ,
and has become known as the oracle problem . Sometimes,
essential properties of programs are formally speciﬁed, or have
to hold universally such that no explicit oracles need to be
deﬁned (e.g., programs should normally not crash). However ,
in the general case one cannot assume the availability of an
automated oracle. This means that, if we produce test inputs ,
then a human tester needs to specify the oracle in terms of
the expected outcome. To make this feasible, test generatio n
needs to aim not only at high code coverage, but also at small
test suites that make oracle generation as easy as possible.
• Gordon Fraser is with Saarland University – Computer Scienc e,
Saarbr¨ucken, Germany, email: fraser@cs.uni-saarland.de. Andre a Arcuri
is with the Certus Software V&V Center at Simula Research Labo ratory,
P .O. Box 134, Lysaker, Norway, email: arcuri@simula.no
1public class Stack{
2 int[] values = new int[3];
3 int size = 0;
4 void push(int x){
5 if (size >= values.length) ⇐ Requires a full stack
6 resize() ;
7 if (size < values.length) ⇐ Else branch is infeasible
8 values[size++] = x;
9 }
10 int pop(){
11 if (size > 0)⇐ May imply coverage in push and resize
12 return values[size−−];
13 else
14 throw new EmptyStackException();
15 }
16 private void resize(){
17 int[] tmp = new int[values.length∗ 2];
18 for(int i = 0; i < values.length; i++)
19 tmp[i] = values[i];
20 values = tmp;
21 }
22}
Fig. 1. Example stack implementation: Some branches
are more difﬁcult to cover than others, some lead to
coverage of further branches, and some can be infeasible.
A common approach in the literature is to generate a
test case for each coverage goal (e.g., branches in branch
coverage), and then to combine them in a single test suite (e.g.,
see [
43]). However, the size of a resulting test suite is difﬁcult
to predict, as a test case generated for one goal may implicit ly
also cover any number of further coverage goals. This is
usually called collateral or serendipitous coverage (e.g. , [
25]).
For example, consider the stack implementation in Figure 1:
Covering the true branch in Line 11 is necessarily preceded
by the true branch in Line 7, and may or may not also be
preceded by the true branch in Line 5. In fact, the order
in which each goal is select can thus play a major role, as
there can be dependencies among goals. Although there have
been attempts to exploit collateral coverage to optimize te st
generation (e.g., [
25]), to the best of our knowledge there is
no conclusive evaluation in the literature of their effectiveness.

<!-- Page 2 -->

Stack stack0 = new Stack();
try {
stack0.pop();
} catch(EmptyStackException e) {
}
Stack stack0 = new Stack();
int int0 = − 510;
stack0.push(int0);
stack0.push(int0);
stack0.push(int0);
stack0.push(int0);
stack0.pop();
Fig. 2. Test suite consisting of two tests, produced by
EVOSUITE for the Stack class shown in Figure 1: All
feasible branches are covered.
There are further issues to the approach of targeting one
test goal at a time: Some targets are more difﬁcult to cover
than others. For example, covering the true branch in Line
5
of the stack example is more difﬁcult than covering the false
branch of the same line, as the true branch requires a Stack
object which has ﬁlled its internal array. Furthermore, coverage
goals can be infeasible, such that there exists no input that
would cover them. For example, in Figure
1 the false branch
of the if condition in Line 7 is infeasible. Even if this
particular infeasible branch may be easy to detect this is no t
true in general (it is, in fact, an undecidable problem [ 23]),
and thus targeting infeasible goals will per deﬁnition fail and
the effort would be wasted. This leads to the question of how
to properly allocate how much of the testing budget (e.g., th e
maximum total time allowed for testing by the user) is used
for each target, and how to redistribute such budget to other
uncovered targets when the current target is covered before its
budget is fully consumed. Although in the literature there h as
been preliminary work based on software metrics to predict
the difﬁculty of coverage goals in procedural code [
31], its
evaluation and usefulness on object-oriented software is s till
an open research question.
In this paper we evaluate a novel approach for test data
generation, which we call whole test suite generation , that
improves upon the current approach of targeting one goal at a
time. We use an evolutionary technique [
1], [ 34] in which,
instead of evolving each test case individually, we evolve
all the test cases in a test suite at the same time, and the
ﬁtness function considers all the testing goals simultaneo usly.
The technique starts with an initial population of randomly
generated test suites, and then uses a Genetic Algorithm to
optimize towards satisfying a chosen coverage criterion, w hile
using the test suite size as a secondary objective. At the end ,
the best resulting test suite is minimized, giving us a test
suite as shown in Figure
2 for the Stack example from
Figure 1. With such an approach, most of the complications
and downsides of the one target at a time approach either
disappear or become signiﬁcantly reduced. The technique is
implemented as part of our testing tool E VOSUITE [
18], which
is freely available online.
This novel approach was ﬁrst described in [ 17], and this
paper extends that work in several directions, by for exampl e
using a much larger and variegated case study, verifying tha t
the presence of infeasible branches has no negative impact
on performance, and by providing theoretical analyses to sh ed
more lights on the properties of the proposed approach. In
particular, we demonstrate the effectiveness of E VOSUITE
by applying it to 1,741 classes coming from open source
libraries and an industrial case study (Section
5); to the best
of our knowledge, this is the largest evaluation of search-
based testing of object-oriented software to date. Because to
effectively address the problem of test suite generation we had
to develop specialized search operators, there would be no
guarantee on the convergence property of the resulting search
algorithm. To cope with this problem, we formally prove the
convergence of our proposed technique.
The results of our experiments show strong statistical evi-
dence that the E VOSUITE approach yields signiﬁcantly better
results (i.e., either higher coverage or, if same coverage, then
smaller test suites) compared to the traditional approach o f
targeting each testing goal independently. In some cases, EVO-
SUITE achieved up to 188 times higher coverage on average,
and test suites that were 62% smaller while maintaining the
same structural coverage. Furthermore, running E VOSUITE
with a constrained budget (one million statement execution s
during the search, up to a maximum 10 minutes timeout)
resulted in an impressive 83% of coverage on average on our
case study.
The paper is organized as follows. Section
2 provides back-
ground information. The novel approach of evolving whole
test suites is described in Section
3, and the details of our
EVOSUITE tool follow in Section 4. The empirical study we
conducted to validate our approach is presented and discuss ed
in Section 5. Convergence is formally proven in Section 6.
Threats to validity of our study are analyzed in Section 7, and
ﬁnally, Section 8 concludes the paper.

## 2 B ACKGROUND

Coverage criteria are commonly used to guide test generatio n.
A coverage criterion represents a ﬁnite set of coverage goal s,
and a common approach is to target one such goal at a time,
generating test inputs either symbolically or with a search -
based approach. The predominant criterion in the literatur e
is branch coverage, but in principle any other coverage cri-
terion or related techniques such as mutation testing [
29] are
amenable to automated test generation.
Solving path constraints generated with symbolic executio n
is a popular approach to generate test data [ 50] or unit
tests [ 51], and dynamic symbolic execution as an extension
can overcome a number of problems by combining concrete
executions with symbolic execution (e.g., [
22], [ 39]). This
idea has been implemented in tools like DART [ 22] and
CUTE [ 39], and is also applied in Microsoft’s parametrized
unit testing tool PEX [ 42] or in the Dsc [ 28] tool.
Meta-heuristic search techniques have been used as an
alternative to symbolic execution based approaches (see [ 1],
[34] for surveys on this topic). The application of search for
test data generation can be traced as back to the 70s [ 35],
where the key concepts of branch distance [30] and approach
level [48] were introduced to help search techniques in gen-
erating the right test data. A promising avenue also seems
to be the combination of evolutionary methods with dynamic
symbolic execution (e.g., [
12], [27], [33]), alleviating some of
the problems both approaches have.

<!-- Page 3 -->

Search-based techniques have also been applied to test
object-oriented software using method sequences [ 21], [ 43]
or strongly typed genetic programming [ 37], [ 47]. When
generating test cases for object-oriented software, since the
early work of Tonella [ 43], authors have tried to deal with the
problem of handling the length of the test sequences, for ex-
ample by penalizing the length directly in the ﬁtness functi on.
However, longer test sequences can lead to achieve higher code
coverage [
5], yet properly handling their growth/reduction
during the search requires special care [ 19].
Most approaches described in the literature aim to generate
test suites that achieve as high as possible branch coverage .
In principle, any other coverage criterion is amenable to
automated test generation. For example, mutation testing [
29]
is often considered a worthwhile test goal, and has been used
in a search-based test generation environment [
21]. When test
cases are sought for individual targets in such coverage bas ed
approaches, it is important to keep track of the accidental
collateral coverage of the remaining targets. Otherwise, i t has
been proven that random testing would fare better under some
scalability models [
10]. Recently, Harman et al. [25] proposed
a search-based multi-objective approach in which, althoug h
each goal is still targeted individually, there is the secon dary
objective of maximizing the number of collateral targets th at
are accidentally covered. However, no particular heuristi c is
used to help covering these other targets.
All approaches mentioned so far target a single test goal
at a time – this is the predominant method. There are some
notable exceptions in search-based software testing. The works
of Arcuri and Yao [
11] and Baresi et al. [ 13] use a single
sequence of function calls to maximize the number of covered
branches while minimizing the length of such a test case. A
drawback of such an approach is that there can be conﬂicting
testing goals, and it might be impossible to cover all of them
with a single test sequence regardless of its length.
Regarding the optimization of an entire test suite in which
all test cases are considered at the same time, we are aware of
only the work of Baudry et al. [
14]. In that work, test suites
are optimized with a search algorithm with respect to mutation
analysis. However, in that work there is the strong limitati on
of having to manually choose and ﬁx the length of the test
cases, which does not change during the search.
In the literature of testing object-oriented software, there are
also techniques that do not directly aim at code coverage, asfor
example implemented in the Randoop [
36] tool. In that work,
sequences of function calls are generated incrementally us ing
an extension of random testing (for details, see [ 36]), and the
goal is to ﬁnd test sequences for which the system under test
(SUT) fails. This, however, is feasible if and only if automated
oracles are available. Once a sequence of function calls is
found for which at least one automated oracle is not passed,
that sequence can be reduced to remove all the unnecessary
function calls to trigger the failure. The software tester w ould
usually get as output only the test cases for which failures a re
triggered. Notice that achieving higher coverage likely le ads
to higher probability of ﬁnding faults, and so recent extens ions
such as Palus [
52] aim to achieve this.
Although targeting for path coverage, tools like DART [ 22]
or CUTE [ 39] have a similar objective, assuming the avail-
ability of an automated oracle (e.g., does the SUT crash?) to
check the generated test cases. This step is essential becau se,
apart from trivial cases, the test suites generated followi ng a
path coverage criterion would be far too large to be manually
evaluated by software testers in real industrial contexts.
The testing problem we address in this paper is very
different from the one considered by tools such as Randoop,
DART, or CUTE: Our goal is to target difﬁcult faults for which
automated oracles are not available – which is a common
situation in practice. Because in these cases the outputs of
the test cases have to be veriﬁed manually, the generated tes t
suites need to be of manageable size. There are two contrasting
objectives: the “quality” of the test suite (e.g., measured in its
ability to trigger failures once manual oracles are provide d)
and its size. The approach we follow in this paper can be
summarized as: Satisfy the chosen coverage criterion (e.g. ,
branch coverage) with the smallest possible test suite.

## 3 T EST SUITE OPTIMIZATION

To evolve test suites that optimize the chosen coverage crit e-
rion, we use a search algorithm, namely a Genetic Algorithm
(GA), that is applied on a population of test suites. In this s ec-
tion, we describe the applied GA, the representation, genet ic
operations, and the ﬁtness function.
3.1 Genetic Algorithms
Genetic Algorithms (GAs) qualify as meta-heuristic search
technique and attempt to imitate the mechanisms of natural
adaptation in computer systems. A population of chromosomes
is evolved using genetics-inspired operations, where each
chromosome represents a possible problem solution.
The GA employed in this paper is depicted in Algorithm
1:
Starting with a random population, evolution is performed u n-
til a solution is found that fulﬁlls the coverage criterion, or the
allocated resources (e.g., time, number of ﬁtness evaluati ons)
have been used up. In each iteration of the evolution, a new
generation is created and initialized with the best individ uals
of the last generation ( elitism). Then, the new generation is
ﬁlled up with individuals produced by rank selection (Line
5),
crossover (Line 7), and mutation (Line 10). Either the offspring
or the parents are added to the new generation, depending on
ﬁtness and length constraints (see Section
3.4).
3.2 Problem Representation
To apply search algorithms to solve an engineering problem,
the ﬁrst step is to deﬁne a representation of the valid soluti ons
for that problem. In our case, a solution is a test suite, which
is represented as a set T of test cases ti. Given|T| =n, we
haveT ={t1,t 2,...,t n}.
In a unit testing scenario, a test case t essentially is a
program that executes the SUT. Consequently, a test case
requires a reasonable subset of the target language (e.g., J ava
in our case) that allows one to encode optimal solutions for
the addressed problem. In this paper, we use a test case
representation similar to what has been used previously [
21],
[43]: A test case is a sequence of statementst =⟨s1,s 2,...,s l⟩

<!-- Page 4 -->

Algorithm 1 The genetic algorithm applied in E VOSUITE
1 current population← generate random population
2 repeat
3 Z← elite of current population
4 while|Z|̸=|current population| do
5 P1,P 2← select two parents with rank selection
6 if crossover probability then
7 O1,O 2← crossoverP1,P 2
8 else
9 O1,O 2← P1,P 2
10 mutate O1 and O2
11 fP =min(fitness (P1),fitness (P2))
12 fO =min(fitness (O1),fitness (O2))
13 lP =length(P1) +length(P2)
14 lO =length(O1) +length(O2)
15 TB = best individual of current population
16 if fO <f P∨ (fO =fP∧lO≤lP ) then
17 forO in{O1,O 2} do
18 if length(O)≤ 2×length(TB) then
19 Z←Z∪{O}
20 else
21 Z←Z∪{P1 orP2}
22 else
23 Z←Z∪{P1,P 2}
24 current population←Z
25 until solution found or maximum resources spent
of length l. The length of a test suite is deﬁned as the sum of
the lengths of its test cases, i.e., length(T ) = ∑
t∈Tlt. Note,
that in this paper we only consider the problem of deriving
test inputs. In practice, a test case usually also contains a test
oracle, e.g., in terms of test assertions; the problem of der iving
such oracles is addressed elsewhere (e.g., [
21].
Each statement in a test case represents one value v(si),
which has a type τ(v(si))∈T , where T is the ﬁnite set of
types. We deﬁne ﬁve different kinds of statements:
Primitive statements represent numeric, Boolean, String,
and enumeration variables, as for exampleint var0 = 54.
Furthermore, primitive statements can also deﬁne arrays of any
type (e.g., Object[] var1 = new Object[10]). The
value and type of the statement are deﬁned by the primitive
variable. In addition, an array deﬁnition also implicitly d eﬁnes
a set of values of the component type of the array, according
to the length of the array.
Constructor statements generate new instances of any
given class; e.g., Stack var2 = new Stack(). Value
and type of the statement are deﬁned by the object constructe d
in the call. Any parameters of the constructor call are assig ned
values out of the set {v(sk)| 0≤k <i}.
Field statements access public member variables of ob-
jects, e.g., int var3 = var2.size. Value and type of
a ﬁeld statement are deﬁned by the member variable. If the
ﬁeld is non-static, then the source object of the ﬁeld has to b e
in the set {v(sk)| 0≤k <i}.
Method statements invoke methods on objects or call
static methods, e.g., int var4 = var2.pop(). Again,
the source object or any of the parameters have to be values
in{v(sk)| 0≤k <i}. Value and type of a method statement
are deﬁned by its return value.
Assignment statements assign values to array indices or to
public member variables of objects, e.g., var1[0] = new
Object() or var2.maxSize = 10. Assignment state-
ments do not deﬁne new values.
For a given SUT, the test cluster [
47] deﬁnes the set of
available classes, their public constructors, methods, and ﬁelds.
Note that the chosen representation has variable size . Not
only the number n of test cases in a test suite can vary
during the GA search, but also the number of statements l
in the test cases. The motivation for having a variable lengt h
representation is that, for a new software to test, we do not
know its optimal number of test cases and their optimal lengt h
a priori – this needs to be searched for.
The entire search space of test suites is composed of all
possible sets of sizes from 1 to N (i.e., n∈ [1,N ]). Each
test case can have a size from 1 to L (i.e., l ∈ [1,L ]).
We need to have these constraints, because in the context
addressed in this paper we are not assuming the presence of
an automated oracle. Therefore, we cannot expect software
testers to manually check the outputs (i.e., writing assert
statements) of thousands of long test cases. For each positi on
in the sequence of statements of a test case, there can be from
Imin toImax possible statements, depending on the SUT and
the position (later statements can reuse objects instantia ted
in previous statements). The search space is hence extremel y
large, although ﬁnite because N, L and Imax are ﬁnite.
3.3 Fitness Function
In this paper, we focus on branch coverage as test criterion,
although the E VOSUITE approach can be generalized to any
test criterion. A program contains control structures such as
if orwhile statements guarded by logical predicates; branch
coverage requires that each of these predicates evaluates to true
and to false. A branch is infeasible if there exists no program
input that evaluates the predicate such that this particula r
branch is executed.
Let B denote the set of branches of the SUT, two for
every control structure. For simplicity, we treat switch/c ase
constructs such that each case is treated like an individual if
condition with a true and false branch. A method without any
control structures consists of only one branch, and therefo re
we require that each method in the set of methods M is
executed at least once.
An optimal solution To is deﬁned as a solution that covers
all the feasible branches/methods and it is minimal in the
total number of statements, i.e., no other test suite with th e
same coverage should exist that has a lower total number of
statements in its test cases. Depending on the chosen test ca se
representation some branches might never be covered, even
though they are potentially reachable if the entire grammar
of the target language was used. As a very simple example,
if the chosen representation allows only to create instance s
of the SUT and none of other classes, then it might not be
possible to reach the branches in the methods of the SUT that
take as input instances of other classes. Because without a

<!-- Page 5 -->

formal proof it is not possible to state that a representatio n is
fully adequate, for sake of simplicity we tag those branches
as infeasible for the given representation.
In order to guide the selection of parents for offspring
generation, we use a ﬁtness function that rewards better cov -
erage. If two test suites have the same coverage, the selecti on
mechanism rewards the test suite with less statements, i.e. , the
shorter one.
For a given test suite T , the ﬁtness value is measured by
executing all tests t ∈ T and keeping track of the set of
executed methodsMT as well as the minimal branch distance
dmin(b,T ) for each branch b ∈ B. The branch distance is
a common heuristic to guide the search for input data to
solve the constraints in the logical predicates of the branc hes
[
30], [ 34]. The branch distance for any given execution of a
predicate can be calculated by applying a recursively deﬁne d
set of rules (see [ 30], [ 34] for details). For example, for
predicatex≥ 10 andx having the value 5, the branch distance
to the true branch is 10− 5 +k, with k >0. In practice, to
determine the branch distance each predicate of the SUT is
instrumented to keep track of the distances for each executi on.
The ﬁtness function estimates how close a test suite is to
covering all branches of a program, therefore it is important to
consider that each predicate has to be executed at least twic e
so that each branch can be taken. Consequently, we deﬁne the
branch distanced(b,T ) for branchb on test suite T as follows:
d(b,T ) =









0 if the branch has been covered,
ν(dmin(b,T )) if the predicate has been
executed at least twice,
1 otherwise.
Here, ν(x) is a normalizing function in [0, 1]; we use the
normalization function [
4]: ν(x) = x/ (x + 1). Notice that
there is a non-trivial reason behind the choice of d(b,T ) =
ν(dmin(b,T )) applied only when the predicate is executed at
least twice [ 11]. For example, assume the case in which it
is always applied. If the predicate is reached, and branch b
is not covered, then we would have d(b,T ) > 0, while the
opposite branchbopp would be covered, and sod(bopp,T ) = 0 .
The search algorithm might be able to follow the gradient
given by d(b,T ) > 0 until b is covered, i.e., d(b,T ) = 0 .
However, in that case bopp would not be covered any more,
and so its branch distance would increase, i.e., d(bopp,T )> 0.
Now, the search would have a gradient to cover bopp but,
if it does cover it, then necessarily b would not be covered
any more (the predicate is reached only once) – and so on.
Forcing a predicate to be evaluated at least twice, before
assigning ν(dmin(b,T )) to the distance of the non-covered
branch, avoids this kind of circular behavior.
Finally, the resulting ﬁtness function to minimize is as
follows:
ﬁtness(T ) =|M|−| MT| +
∑
bk∈B
d(bk,T )
3.4 Bloat Control
A variable size representation could lead to bloat, which
is a problem that is very typical for example in Genetic
Programming [
41]: For instance, after each generation, test
cases can become longer and longer, until all the memory
is consumed, even if shorter sequences are better rewarded.
Notice that bloat is an extremely complex phenomenon in
evolutionary computation, and after many decades of resear ch
it is still an open problem whose dynamics and nature are not
completely understood [
41].
Bloat occurs when small negligible improvements in the
ﬁtness value are obtained with larger solutions. This is ver y
typical in classiﬁcation/regression problems. When in software
testing the ﬁtness function is just the obtained coverage, t hen
we would not expect bloat, because the ﬁtness function would
assume only few possible values. However, when other metrics
are introduced with large domains of possible values (e.g.,
branch distance and also for example mutation impact [
21]),
then bloat might occur.
In previous work [19], we have studied several bloat control
methods from the literature of Genetic Programming [ 41]
applied in the context of testing object-oriented software .
However, our previous study [ 19] covered only the case of
targeting one branch at a time. In E VOSUITE we use the same
methods analyzed in that study [ 19], although further analyses
are required to study whether there are differences in their
application to handle bloat in evolving test suites rather t han
single test cases. The employed bloat control methods are:
• We put a limit N on the maximum number of test cases
and limit L for their maximum length. Even if we expect
the length and number of test cases of an optimal test suite
to have low values, we still need to choose comparatively
larger N and L. In fact, allowing the search process to
employ longer test sequences and then reduce their length
during/after the search can provide staggering improvements
in terms of achieved coverage [
5].
• In our GA we use rank selection [ 49] based on the ﬁtness
function (i.e., the obtained coverage and branch distance
values). In case of ties, we assign better ranks to smaller
test suites. Notice that including the length directly in
the ﬁtness function (as for example done in [
11], [ 13]),
might have side-effects, because we would need to put
together and linearly combine two values of different units
of measure. Furthermore, although we have two distinct
objectives, coverage is more important than size.
• Offspring with non-better coverage are never accepted for
the next generation if they are larger than their parents (fo r
the details, see Algorithm
1).
• We use a dynamic size limit conceptually similar to the
one presented by Silva and Costa [ 41]. If an offspring’s
coverage is not better than that of the best solution TB in
the current entire GA population, then it is not accepted in
the new generations if it is longer than twice the length of
TB (see Line
18 in Algorithm 1).
3.5 Search Operators
The GA code depicted in Algorithm
1 is at high level, and can
be used for many engineering problems in which variable size
representations are used. To adapt it to a speciﬁc engineeri ng
problem, we need to deﬁne search operators that manipulate

<!-- Page 6 -->

a() b() c() d()
x() y() z()
f() g() h() i()
a() b()
x() y() z()
f() g() h()
a()
a() b() c() d()
x() y() z()
a() b()
x() y() z() a()
f() g() h() i() f() h() g()
(a) Test Suite Crossover
a() b() c()
b() x()
b() x() d()
a() b() c()
(b) Test Case Mutation
Fig. 3. Crossover and mutation are the basic operators for
the search using a GA. Crossover is applied at test suite
level; mutation is applied to test cases and test suites.
the chosen solution representation (see Section
3.2). In partic-
ular we need to deﬁne the crossover and mutation operators
for test suites. Furthermore, we need to deﬁne how random
test cases are sampled when we initialize the ﬁrst populatio n
of the GA.
3.5.1 Crossover
The crossover operator (see Figure
3(a)) generates two off-
spring O1 and O2 from two parent test suites P1 and P2. A
random value α is chosen from [0, 1]. On one hand, the ﬁrst
offspring O1 will contain the ﬁrst α|P1| test cases from the
ﬁrst parent, followed by the last (1−α )|P2| test cases from
the second parent. On the other hand, the second offspring O2
will contain the ﬁrst α|P2| test cases from the second parent,
followed by the last (1−α )|P1| test cases from the ﬁrst parent.
Because the test cases are independent among them, this
crossover operator always yields valid offspring test suit es.
Furthermore, it is easy to see that it decreases the differen ce
in the number of test cases between the test suites, i.e.,
abs(|O1|−| O2|)≤abs(|P1|−| P2|). No offspring will have
more test cases than the largest of its parents. However, it i s
possible that the total sum of the length of test cases in an
offspring could increase.
3.5.2 Mutation
The mutation operator for test suites is more complicated th an
that used for crossover, because it works both at test suite a nd
test case levels. When a test suite T is mutated, each of its
test cases is mutated with probability 1/|T|. So, on average,
only one test case is mutated. Then, a number of new random
test cases is added to T : With probability σ, a test case is
added. If it is added, then a second test case is added with
probability σ 2, and so on until the ith test case is not added
(which happens with probability 1−σ i). Test cases are added
only if the limit N has not been reached, i.e., if n<N .
If a test case is mutated (see Figure
3(b)), then three
types of operations are applied in order: remove, change and
insert. Each is applied with probability 1/ 3. Therefore, on
average, only one of them is applied, although with probability
(1/ 3)3 all of them are applied. These three operations work
as follows:
Remove: For a test case t =⟨s1,s 2,...,s l⟩ with length l,
each statement si is deleted with probability 1/l . As the value
v(si) might be used as a parameter in any of the statements
si+1,...,s l, the test case needs to be repaired to remain valid:
For each statement sj, i < j≤ l, if sj refers to v(si), then
this reference is replaced with another value out of the set
{v(sk)| 0≤k <j∧k̸=i} which has the same type as v(si).
If this is not possible, then sj is deleted as well recursively.
Change: For a test case t =⟨s1,s 2,...,s l⟩ with length
l, each statement si is changed with probability 1/l . If si is
a primitive statement, then the numeric value represented b y
si is changed by a random value in [−∆ , ∆] , where ∆ is a
constant. If the primitive value is a string, then the string is
changed by deleting, replacing, or inserting characters in a way
similar to how sequences of method calls are mutated. In the
case of an array, the length is changed by a random value in
[−∆ ′, ∆ ′] such that no accesses to the array are invalidated. In
an assignment statement, either the variable on the left or t he
right hand side of the assignment is replaced with a differen t
variable of the same type. If si is not a primitive statement,
then a method, ﬁeld, or constructor with the same return type
as v(si) and parameters satisﬁable with the values in the set
{v(sk)| 0≤k <i} is randomly chosen out of the test cluster.
Insert: With probability σ ′, a new statement is inserted at
a random position in the test case. If it is added, then a secon d
statement is added with probability σ ′2, and so on until the
ith statement is not inserted. A new statement is added only
if the limit L has not been reached, i.e., if l < L. For each
insertion, with probability 1/ 3 a random call of the class under
test or its member classes is inserted, with probability 1/ 3 a
method call on a value in the set {v(sk)| 0≤ k < i} for
insertion at position i is added, and with probability 1/ 3 a
value{v(sk)| 0≤k <i} is used as a parameter in a call of
the class under test or its member classes. Any parameters of
the selected call are either reused out of the set {v(sk)| 0≤
k <i}, set to null, or randomly generated.
If after applying these mutation operators a test caset has no
statements left (i.e., all have been removed), then t is removed
from T .
To evaluate the ﬁtness of a test suite, it is necessary to
execute all its test cases and collect the branch informatio n.
During the search, on average only one test case is changed in
a test suite for each generation. This means that re-executi ng
all test cases is not necessary, as the coverage information can
be carried over from the previous execution.
3.5.3 Random Test Cases
Random test cases are needed to initialize the ﬁrst generati on
of the GA, and when mutating test suites. Sampling a test case
at random means that each possible test case in the search
space has a non-zero probability of being sampled, and these
probabilities are independent. In other words, the probabi lity
of sampling a speciﬁc test case is constant and it does not
depend on the test cases sampled so far.
When a test case representation is complex and it is of
variable length (as it happens in our case, see Section
3.2),
it is often not possible to sample test cases with uniform
distribution (i.e., each test case having the same probabil ity
of being sampled). Even when it would be possible to use a
uniform distribution, it would be unwise (for more details o n

<!-- Page 7 -->

this problem, see [10]). For example, given a maximum length
L, if each test case was sampled with uniform probability, then
sampling a short sequence would be extremely unlikely. This
is because there are many more test cases with long length
compared to the ones of short length.
In this paper, when we sample a test case at random, we
choose a value r in 1 ≤ r ≤ L with uniform probability.
Then, on an empty sequence we repeatedly apply the insertion
operator described in Section
3.5.2 until the test case has a
length≥r.

## 4 T HE EVOSUITE TOOL

The E VOSUITE tool implements the approach presented in
this paper for generating JUnit test suites for Java code.
EVOSUITE works on the byte-code level and collects all
necessary information for the test cluster from the byte-co de
via Java Reﬂection. This means that it does not require the
source code of the SUT, and in principle is also applicable
to other languages that compile to Java byte-code (such as
Scala or Groovy, for example). Note that we also consider
branch coverage at the byte-code level. Because high level
branch statements in Java (e.g., predicates in loop conditi ons)
are transformed into simpler statements similar to atomic if
statements in the byte-code, E VOSUITE is able to handle all
language constructs. Furthermore, E VOSUITE treats each case
of a switch/case construct like an individualif-condition. The
number of branches at byte-code level is thus usually larger
than at source code level, as complex predicates are compile d
into simpler byte-code instructions.
EVOSUITE instruments the byte-code with additional state-
ments to collect the information necessary to calculate ﬁt-
ness values, and also performs some basic transformations t o
improve testability: To allow optimizations of String valu es,
branches based on String methods like String.equals are
transformed such that they act on the edit distance [
2]. Simi-
larly, comparisons on double, ﬂoat, and long datatypes in byte-
code need transformation to carry a distance measurements t o
the branches.
During test generation, E VOSUITE considers one top-level
class at a time. The class and all its anonymous and member
classes are instrumented at byte-code level to keep track of
called methods and branch distances during execution. To
produce test cases as compilable JUnit source code, E VO-
SUITE accesses only the public interfaces for test generation;
any subclasses are also considered part of the unit under
test to allow testing of abstract classes. To execute the tes ts
during the search, E VOSUITE uses Java Reﬂection. Before
presenting the result to the user, test suites are minimizedusing
a simple minimization algorithm [
5] which attempts to remove
each statement one at a time until all remaining statements
contribute to the coverage; this minimization reduces both
the number of test cases as well as their length, such that
removing any statement in the resulting test suite will redu ce
its coverage.
The search operators for test cases make use of only the type
information in the test cluster, and although type informat ion
is updated during execution difﬁculties can arise when meth od
signatures are imprecise. In particular, this problem exis ts
for all classes using Java Generics, as type erasure removes
much of the useful information during compilation and all
generic parameters look like Object for Java Reﬂection. To
overcome this problem for container classes (and in general for
any class with methods that take as input and return Object
instances), we always put Integer objects into container
classes, such that we can also cast returned Object instances
back to Integer. Currently, container classes need to be
identiﬁed manually, but future versions of E VOSUITE will
determine suitable types automatically.
Test case execution can be slow, and in particular when
generating test cases randomly, inﬁnite recursion can occu r
(e.g., by adding a container to itself and then calling the
hashCode method). Therefore, we chose a timeout of ﬁve
seconds for test case execution. If a test case times out, the n
the test suite with that test case is assigned the maximum
ﬁtness value, which is |M| +|B|, the sum of methods and
branches to be covered.
Test cases are executed in their own threads, but as Java does
not allow to forcefully stop threads it may happen that after the
timeout such a thread survives. To overcome this problem, we
instrument the byte-code with additional statements that y ield
the execution of a test when the thread is interrupted. If thi s
also shows no effect, the thread is given a low priority and
its execution is ignored. Aggregations of such stale thread s
consume memory, and so E VOSUITE uses a client/server
architecture where the client monitors its free memory, and
asks the server for a process restart which resumes at the sam e
point in the search, if it runs out of memory.
EVOSUITE also employs a custom, conﬁgurable security
manager which can be used to control what permissions
are granted during the test execution. For example, it is
usually not desirable to have the tests open random networking
connections or access the ﬁlesystem in random ways. The
use of a custom security manager was an essential feature
for the large empirical study we conduct in this paper. In
fact, thanks to that we were able to select a large number
of SUTs from different sources without needing to worry
whether their behavior was safe under all inputs. However,
this means that E VOSUITE currently can only cover code that
has no environmental dependencies. Furthermore, E VOSUITE
assumes that the code under test is deterministic, such that
executing the same test case twice will yield the same result s.
4.1 Single Branch Strategy
To allow a fair comparison with the traditional single branc h
approach (e.g., [
43]), we implemented this strategy on top
of E VOSUITE . In the single branch strategy, an individual of
the search space is a single test case. The identical mutatio n
operators for test cases can be used as in E VOSUITE , but
crossover needs to be done at the test case level. For this,
we used the approach also applied by Tonella [
43] and Fraser
and Zeller [ 21]: Offspring is generated using the single point
crossover function described in Section 3.5.1, where the ﬁrst
part of the sequence of statements of the ﬁrst parent is merge d
with the second part of the second parent, and vice versa.

<!-- Page 8 -->

Because there are dependencies between statements and values
generated in the test case, this might invalidate the result ing
test case, and we need to repair it: The statements of the second
part are appended one at a time similarly to the insertion
described in Section
3.5.2, except that whenever possible
dependencies are satisﬁed using existing values.
The ﬁtness function in the single branch strategy also needs
to be adapted: We use the traditional approach level [48]
plus normalized branch distance ﬁtness function, which is
commonly used in the literature (e.g., see [
26], [ 34]). The
approach level is used to guide the search toward the target
branch. It is determined as the minimal number of control
dependent edges in the control dependency graph between the
target branch and the control ﬂow represented by the test cas e.
The branch distance is calculated as in E VOSUITE , but taken
for the closest control dependent branch where the control ﬂow
diverges from the target branch.
While implementing this approach, we tried to derive a
faithful representation of current practice, which means t hat
there are some optimizations proposed in the literature whi ch
we did not include:
• New test cases are only generated for branches that have
not already been covered through collateral coverage of
previously created test cases. However, we do not evaluate
the collateral coverage of all individuals during the searc h,
as this would add a signiﬁcant overhead, and it is not clear
what effects this would have given the ﬁxed timeout we
used in our experiments.
• When applying the one target at a time approach, a possible
improvement could be to use a seeding strategy [
48]. During
the search, we could store the test data that have good ﬁtness
values on targets that are not covered yet. These test data
can then be used as starting point (i.e., for seeding the ﬁrst
generation of a GA) in the successive searches for those
uncovered targets. However, we decided not to implement
this, as reference [
48] does not provide sufﬁcient details to
reimplement the technique, and there is no conclusive data
regarding several open questions; for example, potentiall y
a seeding strategy could reduce diversity in the population ,
and so in some cases it might in fact reduce the overall
performance of the search algorithm.
• The order in which coverage goals are selected might also
inﬂuence the result. As in the literature usually no order is
speciﬁed (e.g., [
25], [27], [43]), we selected the branches in
random order. However, in the context of procedural code
approaches to prioritize coverage goals have been proposed,
e.g., based on dynamic information [
48]. However, the goal
of this paper is neither to study the impact of different
orders, nor to adapt these prioritization techniques to object-
oriented code and prioritization techniques.
• In practice, when applying a single goal strategy, one
might also bootstrap an initial random test suite to identif y
the trivial test goals, and then use a more sophisticated
technique to address the difﬁcult goals; here, a difﬁcult
question is when to stop the random phase and start the
search. In contrast, E VOSUITE has this initial random phase
integrated into its own search process.
TABLE 1
Number of classes, branches, and lines of code in the
case study subjects
Case Study #Classes #Branches LOC 1
Public All
COL Colt 135 298 10,795 20,741
CCL Commons CLI 14 15 662 1,078
CCD Commons Codec 21 22 1,369 2,205
CCO Commons Collections 246 421 8,683 19,190
CMA Commons Math 247 306 10,503 23,881
CPR Commons Primitives 210 231 2,874 7,008
GCO Google Collections 85 370 4,214 9,886
ICS Industrial Casestudy 21 29 373 809
JCO Java Collections 30 118 3,531 6,339
JDO JDom 57 61 4,098 6,452
JGR JGraphT 137 193 2,467 5,924
JTI Joda Time 131 199 8,681 18,003
NXM NanoXML 1 1 310 661
NCS Numerical Casestudy 11 11 209 421
REG Java Regular Expressions 3 91 1,922 3,020
SCS String Casestudy 12 12 607 606
TRO GNU Trove 205 591 10,585 24,297
XEN Xmlenc 7 7 1,645 788
XOM XML Object Model 165 185 11,794 23,814
ZIP Java ZIP Utils 3 4 219 441
Σ 1,741 3,165 85,541 175,564

## 5 E XPERIMENTS

The independence of the order in which test cases are selecte d
and the collateral coverage are inherent to the E VOSUITE
approach, therefore the evaluation focuses on the improvement
over the single branch strategy.
5.1 Case Study Subjects
For the evaluation, we chose a total of 19 open source libraries
and programs. For example, among those there are several
widely used libraries developed by Google and the Apache
Software Foundation. Furthermore, to analyze in more detai ls
some speciﬁc types of software, we also used a translation of
the String case study subjects employed by Alshraideh and
Bottaci [
2], and we also used a set of numerical applications
from [ 6]. To avoid a bias caused by considering only open
source code, we also selected a subset of an industrial case
study project previously used by Arcuri et al. [
9]. This results
in a total of 3,165 classes, which were tested by only calling
the API of the 1,741 public classes (the remaining classes ar e
member classes).
The choice of a case study is of paramount importance for
any empirical analysis in software engineering. To address this
problem, in this paper we consider several types of software ,
as for example container classes, numerical applications, and
software with high use of strings and arrays processing.
Table
1 summarizes the properties of these case study subjects.
To avoid bias in analyzing the results, we present and
discuss the results of our empirical study grouped by projec t.
In fact, different testing techniques can have comparative ly
different performance on different types of SUT. For exampl e,
1. LOC stands for non-commenting lines of source code, calcula ted with
JavaNCSS (http://javancss.codehaus.org/)

<!-- Page 9 -->

random testing has been shown to be very effective in testing
container classes [
40]. If one only chooses container classes
as case study and ignores for example numerical application s,
then random testing could be misleadingly advantaged in
technique comparisons. In fact, even if one uses several kin ds
of software as SUTs, then it all depends on the proportion
of the SUT types (e.g., if in the case study there are many
more container classes than numerical applications). Ther e-
fore, aggregated statistics on all the artifacts of a case st udy
need to be interpreted with care, as the proportion of differ ent
kinds of software types could lead to misleading results.
Unfortunately, how to deﬁne a representative case study for
test data generation is still an open research question.
5.2 Experimental Setup
As witnessed in Section
3, search algorithms are inﬂuenced by
a great number of parameters. For many of these parameters
there are “best practices”: For example, we chose a crossove r
probability of 3/ 4 based on past experience. In E VOSUITE ,
the probabilities for mutation are largely determined by th e
individual test suite size or test case length; the initial p rob-
ability for test case insertion was set to σ = 0. 1, and the
initial probability for statement insertion was set to σ ′ = 0. 5.
The maximum value for the perturbation of integral primitiv e
types ∆ was set to 20. Although longer test cases are better
in general [
5], we limited the length of test cases to L =
80 because we experienced this to be a suitable length at
which the test case execution does not take too long. The
maximum test suite size was set to N = 100, although the
initial test suites are generated with only two test cases ea ch.
The population size for the GA was chosen to be 80.
Different settings (e.g., population size) of an algorithm
would lead to different performance. Unfortunately, on a ne w
search problem (such as generation of test suites in this pap er)
it is not possible to know beforehand which are the best
settings to use. A tuning phase could lead to ﬁnd settings
for which E VOSUITE performs better, but tuning phases are
computational expensive. As even with common settings based
on the literature it is possible to achieve reasonable resul ts [
8],
we postponed the tuning investigation to future work, and
preferred to focus on having a larger case study with the aim
of reducing threats to external validity.
Search algorithms are often compared in terms of the
number of ﬁtness evaluations; in our case, comparing to a
single branch strategy would not be fair, as each individual
in E VOSUITE represents several test cases, such that the
comparison would favor E VOSUITE . As the length of test
cases can vary greatly and longer test cases generally have
higher coverage, we decided to take the number of executed
statements as execution limit. This means that the search is
performed until either a solution with 100% branch coverage is
found, ork statements have been executed as part of the ﬁtness
evaluations. In our experiments, we chose k = 1, 000, 000.
For the single branch strategy, the maximum test case
length, population size, and any probabilities are chosen
identical to the settings of E VOSUITE . At the end of the test
generation, the resulting test suite is minimized in the sam e
way as in E VOSUITE .
The stopping condition for the single branch strategy is
chosen the same as for E VOSUITE , i.e., maximum 1,000,000
statements executed. To avoid that this budget is spent entirely
on the ﬁrst branch if it is difﬁcult or infeasible, we apply th e
following strategy: For |B| branches and an initial budget of
X statements, the execution limit for each branch is X/|B|
statements. If a branch is covered, some budget may be left
over, and so after the ﬁrst iteration on all branches there is a
remaining budget X ′. For the remaining uncovered branches
B′ a new budget X ′/|B′| is calculated and a new iteration is
started on these branches. This process is continued until t he
maximum number of statements (1,000,000) is reached.
EVOSUITE and search-based testing are based on ran-
domized algorithms, which are affected by chance. Running
a randomized algorithm twice will likely produce different
results. It is essential to use rigorous statistical method s to
properly analyze the performance of randomized algorithms
when we need to compare two or more of them. In this paper,
we follow the guidelines described in [
7].
For each of the 1,741 public classes, we ran E VOSUITE
against the single branch strategy to compare their achieve d
coverage. Each experiment comparison was repeated 30 times
with different seeds for the random number generator. When
one can have an arbitrarily large number of artifacts for a
case study (e.g., in our case we could download and use
as SUT as many projects as we wanted from open source
repositories, because E VOSUITE is fully automated and has a
customized security manager to avoid undesired side effect s),
then there is the trade-off between the number of runs per
artifact and size of the case study. In general, it is advisab le
to have enough runs (e.g., 30) to detect statistical differe nce
of algorithm performances on single artifacts, and then hav e a
case study as large and variegated as possible to reduce thre ats
to external validity. Notice that, in our empirical analysis, even
with the use of a large cluster of computers it took several days
to run all the experiments.
5.3 Results
Due to space constraints we cannot provide full information of
the analyzed data [
7], but just show the data that are sufﬁcient
in claiming the superiority of the E VOSUITE technique. Sta-
tistical difference has been measured with the Mann-Whitney
U test. To quantify the improvement in a standardized way, we
used the Vargha-Delaney ˆA12 effect size [
44]. In our context,
the ˆA12 is an estimation of the probability that, if we run
EVOSUITE , we will obtain better coverage than running the
single branch strategy. When two randomized algorithms are
equivalent, then ˆA12 = 0. 5. A high value ˆA12 = 1 means
that, in all of the 30 runs of E VOSUITE , we obtained coverage
values higher than the ones obtained in all of the 30 runs of
the single branch strategy.
The box-plot in Figure
4 compares the actual obtained
coverage values (averaged out of the 30 runs) of E VOSUITE
and the single branch strategy ( Single). In total, the coverage
improvement of E VOSUITE ranged up to 188 times that of the
single branch strategy. This happened for a particular SUT i n
which E VOSUITE obtained a coverage of 70. 2% (averaged

<!-- Page 10 -->

TABLE 2
ˆA12 measure values in the coverage comparisons:
ˆA12 < 0. 5 means EVOSUITE resulted in less, ˆA12 = 0. 5
equal, and ˆA12 > 0. 5 better coverage than a single
branch approach. In brackets “()” the number of times the
effect size is statistically signiﬁcant at level 0. 05.
Case Study # ˆA12 < 0.5 # ˆA12 = 0.5 # ˆA12 > 0.5
COL 13(9) 30 92(79)
CCL 2(1) 6 6(4)
CCD 2(1) 13 6(5)
CCO 19(5) 137 90(81)
CMA 24(10) 100 123(103)
CPR 23(10) 150 37(19)
GCO 4(2) 31 50(42)
ICS 0(0) 17 4(3)
JCO 2(1) 10 18(17)
JDO 3(2) 27 27(25)
JGR 2(1) 88 47(41)
JTI 41(28) 28 62(41)
NXM 0(0) 0 1(1)
NCS 1(0) 10 0(0)
REG 0(0) 1 2(2)
SCS 4(4) 6 2(1)
TRO 2(1) 73 130(124)
XEN 0(0) 4 3(3)
XOM 22(11) 92 51(45)
ZIP 0(0) 1 2(2)
Σ 164(86) 824 753(638)
over 30 runs), while for the single branch strategy the avera ge
coverage was only 0. 3%. Calculated on all the SUTs in the
case study, E VOSUITE obtained an average coverage of 83%,
whereas the single branch strategy obtained 77%.
Figure 5 shows a box-plot of the results of the ˆA12̸= 0. 5
measure for the coverage grouped by case study subject; this
ﬁgure illustrates the strong statistical evidence that E VOSUITE
achieves higher coverage. In many cases, E VOSUITE is prac-
tically certain to achieve better coverage results, even wh en
we take the randomness of the results into account.
Whole test suite generation achieves higher coverage
than single branch test case generation.
Table 2 shows for the coverage comparisons how many
times we obtained ˆA12 values equal, lower and higher than
0. 5. We obtained p-values lower than 0. 05 in 724 out of 917
comparisons in which ˆA12 ̸= 0. 5. Among the 20 projects,
there is one for which E VOSUITE gave worse results, i.e.,
SCS. Without an in depth analysis on that project, it is difﬁcult
to conjecture why that is the case. The project SCS contains
a set of artiﬁcial classes, where all methods are static, take as
input (and manipulate) string objects, and have no infeasib le
branches. It might be that using a hybrid algorithm in which
EVOSUITE is enhanced with local search (e.g., see [ 26]) could
be effective for this type of software. But the use of local
search for test suite evolution is still an unexplored ﬁeld,
although promising (see for example [
11], [13], [26]). At any
rate, although the single branch strategy is statistically better
on four SUTs and achieves an average coverage of 86. 8%,
even if E VOSUITE is statistically better on only one SUT,
its average coverage is actually higher, i.e., 87. 7%. This is
not a contradiction. It could be explained by the fact that,
when E VOSUITE is worse on a speciﬁc SUT, it is only worse
by little, whereas when it is better, it is better by a larger
quantity. This is clearly visible in the boxplot in Figure
4,
where although the median value for E VOSUITE is lower, then
however its lower quartile and minimum value is much higher.
Notice that in many cases (i.e., 824) we have ˆA12 = 0. 5.
This did not come as a surprise: For some “easy” classes,
a budget of 1,000,000 statements executions would be more
than enough to cover all the feasible branches with very high
probability. In these cases, it is important to analyze what
is the resulting size of the generated test suites. When the
coverage is different, analyzing the resulting test suite s izes is
not reasonable (e.g., a test suite with higher coverage like ly
has to be larger).
For those cases where ˆA12 = 0. 5 for the coverage, Figure
6
compares the obtained test suite size values (averaged out o f
the 30 runs) of E VOSUITE and the single branch strategy
(Single). In the best case, we obtained a test suite size
(averaged out of the 30 runs) that for E VOSUITE was 62%
smaller. In particular, EVOSUITE has an average length of 3. 23
statements, whereas the length of the test suites generated with
the single branch strategy led to an average 8. 36 length.
Figure 7 shows ˆA12 for the length of the resulting test suites,
but only when p-values are lower than 0. 05. Recall that for
both E VOSUITE and the single branch strategy we use the
same post-processing technique to reduce the length of the
output test suites. When we obtain full coverage of all the
feasible branches, then E VOSUITE has a low probability of
generating larger test suites.
Whole test suite generation produces smaller test suites
than single branch test case generation.
The results obtained with E VOSUITE compared to the
traditional approach (of targeting each branch separately ) are
simply staggering. How is it possible to achieve such large
improvements? There can be several explanations. First, in
case of infeasible branches, all the effort spent by a single
branch at a time strategy would be wasted, apart from pos-
sible collateral coverage. Collateral coverage of difﬁcul t to
reach branches, however, would be quite unlikely. Second, t he
traditional ﬁtness function would have problems in guiding
the search toward private methods that are difﬁcult to execu te.
For example, consider the case of a private method that is
called only once in a public method, but that method call is
nested in a branch whose predicate is very complicated to
satisfy. Unless the ﬁtness function is extended to consider all
possible methods that can lead to execute the private method s
(as for example done in [
46]), then there would be no guidance
to execute those private methods. Third, assume that there i s
a difﬁcult branch to cover, and nested to that branch there
are several others. Once E VOSUITE is able to generate a test
sequence that covers that difﬁcult branch, this sequence ca n be
extended (e.g., by adding function calls at its end) or copie d in
another test case in the test suite (e.g., through the crosso ver
operator) to make it easier to cover the other nested branche s.

<!-- Page 11 -->

0.0 0.2 0.4 0.6 0.8 1.0
Average Branch Coverage
COL CCL CCD CCO CMA
0.0 0.2 0.4 0.6 0.8 1.0
EvoSuite
Single
0.0 0.2 0.4 0.6 0.8 1.0
Average Branch Coverage
CPR GCO ICS JCO JDO
0.0 0.2 0.4 0.6 0.8 1.0
EvoSuite
Single
0.0 0.2 0.4 0.6 0.8 1.0
Average Branch Coverage
JGR JTI NXM NCS REG
0.0 0.2 0.4 0.6 0.8 1.0
EvoSuite
Single
0.0 0.2 0.4 0.6 0.8 1.0
Average Branch Coverage
SCS TRO XEN XOM ZIP
0.0 0.2 0.4 0.6 0.8 1.0
EvoSuite
Single
Fig. 4. Average branch coverage: Even with an evolution limi t of 1,000,000 statements, EVOSUITE achieves higher
coverage.
COL CCL CCD CCO CMA
0.0 0.2 0.4 0.6 0.8 1.0
Effect Size
CPR GCO ICS JCO JDO
0.0 0.2 0.4 0.6 0.8 1.0
Effect Size
JGR JTI NXM NCS REG
0.0 0.2 0.4 0.6 0.8 1.0
Effect Size
SCS TRO XEN XOM ZIP
0.0 0.2 0.4 0.6 0.8 1.0
Effect Size
Fig. 5. ˆA12 for coverage: EVOSUITE has a high probability of achieving higher coverage than a single branch approach.
0 10 20 30 40 50 60
Average Length
COL CCL CCD CCO CMA
0 10 20 30 40 50 60
EvoSuite
Single
0 10 20 30 40 50 60
Average Length
CPR GCO ICS JCO JDO
0 10 20 30 40 50 60
EvoSuite
Single
0 10 20 30 40 50 60
Average Length
JGR JTI NXM NCS REG
0 10 20 30 40 50 60
EvoSuite
Single
0 10 20 30 40 50 60
Average Length
SCS TRO XEN XOM ZIP
0 10 20 30 40 50 60
EvoSuite
Single
Fig. 6. Average test suite length: Even after minimization, EVOSUITE test suites tend to be smaller than those created
with a single branch strategy (shown for cases with identical coverage).
COL CCL CCD CCO CMA
0.0 0.2 0.4 0.6 0.8 1.0
Effect Size
CPR GCO ICS JCO JDO
0.0 0.2 0.4 0.6 0.8 1.0
Effect Size
JGR JTI NXM NCS REG
0.0 0.2 0.4 0.6 0.8 1.0
Effect Size
SCS TRO XEN XOM ZIP
0.0 0.2 0.4 0.6 0.8 1.0
Effect Size
Fig. 7. ˆA12 for test suite length: EVOSUITE has a low probability of generating longer test suites than a single branch
approach.
On the other hand, in the traditional approach of targeting
one branch at a time, unless smart seeding strategies are use d
based on previously covered branches, the search to cover
nested branches would be harmed by the fact that covering
their difﬁcult parent needs to be done from scratch again.
Because our empirical analysis employs a very large case
study (1,741 classes for a total of 85,503 byte-code level
branches), we cannot analyze all of these branches to give an
exact explanation for the better performance of E VOSUITE .
However, the three possible explanations we gave are plausi -
ble, although further analyses (e.g., on artiﬁcial softwar e that
we can generate with known number of infeasible branches)
would be required to shed light on this important research
question. To this goal, we created an artiﬁcial problem to
experiment with, whose analysis is discussed later in the paper.
5.3.1 Difﬁcult Branches
Looking at the results in Table
2 we see that E VOSUITE does
not achieve 100% coverage for all classes. To some extent,
this is due to infeasible branches. Due to the large amount of
classes empirically investigated in this paper, it is not po ssible
to distinguish between all infeasible and difﬁcult branche s
by hand. However, identifying some of the difﬁcult cases is
helpful to understand the results and guide future research .
Not all infeasible branches are as obvious as the example in
Figure
1. Other examples of infeasible branches are given by
private methods that are not called in any public methods, dead
code, or methods of abstract classes that are overridden in a ll
concrete subclasses without calling the abstract super-cl ass.
Some difﬁcult branches we could identify are the following:
Environment dependencies such as databases or the

<!-- Page 12 -->

ﬁlesystem are not currently handled by E VOSUITE . Using
the custom security manager one can avoid that interactions
with the environment cause damage, but branches depending,
for example, on network connections or ﬁle contents usually
cannot be covered.
Methods called by native code such as readObject
and writeObject of the Java Serializable interface
cannot be directly called.
Anonymous and private classes are more difﬁcult to
cover than top level classes, as they can only be handled
indirectly via the owner classes’ public interface. An even
more difﬁcult variant of this problem are abstract classes t hat
are only instantiated by anonymous classes – there is no way
to directly test the abstract class, except by creating stub s.
Multi-threaded code is also difﬁcult for a search-based
approach, as the test generation would need to handle thread
creation and termination.
Static and private constructors are only executed once
after a class is loaded, and private constructors are often u sed
in singleton instances where the constructor is again only
called once. To achieve full coverage in such cases one would
need to unload classes after each test execution; E VOSUITE
uses a faster but less precise approach introduced in the
JCrasher [
15] tool, where static constructors are duplicated in
callable methods, and then re-executed before test executi on.
5.4 Infeasible Test Goals
A coverage goal is infeasible if there exists no test that wou ld
exercise it. For some simple cases, there could be technique s
that are able to identify infeasible targets; for example, d ead-
code detection might reveal some infeasible branches, such
as the one listed in Figure
1. However, in general it is an
undecidable problem whether a particular coverage goal or
program path is feasible [
23] or if a mutant is equivalent.
Furthermore, a branch might be infeasible for other reasons
(e.g., environmental dependencies), and applying techniq ues
to detect infeasible goals on several targets might have a no n
negligible computational overhead, which would reduce the
time budget for test data generation (e.g., less generation s in
an evolutionary algorithm). Depending on how effective the se
techniques are, their use might thus either increase or even
decrease the overall performance of the testing tool.
When targeting each coverage goal individually, any re-
sources invested for an infeasible goal are per deﬁnition
wasted. Depending on how the available resources are dis-
tributed across the individual goals, the more infeasible g oals
there are the fewer of the resources will be spent on the
feasible goals, thus leading to overall worse results.
In contrast, E VOSUITE does not focus on individual cover-
age goals, and so the infeasible goals have no effect on the
achieved coverage of the feasible goals. To demonstrate thi s
effect, we ran a set of experiments on the example code listed
in Figure
8. In the byte-code representation, this code contains
six feasible branches. At the position labelled in the sourc e
code we iteratively inserted infeasible branches ( if(x * x
== y * y + 2)) and analyzed the behavior of E VOSUITE
and the single branch strategy over the number of inserted
1class Infeasible{
2 void infeasibleGoals(int x, int y){
3 if (x > 0 && y > 0 && 2 ∗ x == Math.sqrt(y)) {
4 }
5 // Infeasible branches are added here
6 }
7}
Fig. 8. A simple example to demonstrate the effect of
infeasible coverage goals. In the default case, there are
three predicates, leading to six (feasible) branches in the
compiled byte-code.
0 20 40 60 80 100
0 1 2 3 4 5
Number of Infeasible Targets
Average Number of Missed Feasible Targets
EvoSuite
Single
Fig. 9. The effect of infeasible goals on the coverage of
the feasible goals in the code: The number of unsatisﬁed
coverage goals rises with the number of infeasible test
goals in the single branch strategy, whileEVOSUITE is not
inﬂuenced at all by the infeasible goals.
infeasible branches. For each version of the example code, w e
performed 100 runs of E VOSUITE and 100 runs of the single
branch strategy with different random seeds and a search lim it
of 40,000 statements. Figure
9 impressively demonstrates how
EVOSUITE is oblivious to the introduced infeasible branches,
while the performance of the single branch strategy degrade s.
To give more soundness to this analysis, we also applied
a Kruskal-Wallis test to verify the impact of the number of
infeasible targets on the number of missed (i.e., uncovered )
feasible branches. For the single branch strategy, we obtai ned
a p-value lower than 2. 2× 10−16, withχ 2 = 932. 5. This gives
strong statistical evidence that conﬁrms the trend in Figur e
9.
On the other hand, for E VOSUITE we obtained a very high
p-value, i.e. 0. 73, whereχ 2 = 9. 44. Notice that a high p-value
does not mean that we have strong statistical evidence to claim
that infeasible targets have no impact on E VOSUITE . To make
analyses as precise and sound as possible, one should quanti fy
the effect sizes and then use power analysis to calculate the
probability of Type II error [
7]. However, the differences in
coverage in Figure 9 look so small that, even if higher number
of runs might decrease the p-value of the test, then anyway the
differences would be so small to be of little practical inter est.

<!-- Page 13 -->

5.5 Comparisons with Other Tools
In this paper, we have carried out a large empirical analysis to
show that the EVOSUITE strategy of evolving whole test suites
is generally better than the traditional approach of search ing
for only one target at the time. To provide further evidence
on the effectiveness of E VOSUITE , and to get more insight on
the dynamics of test data generation, it would be important t o
compare its performance against other tool prototypes in th e
literature. Unfortunately, this was not possible. In this s ection,
we describe the challenges and shortcomings that would be
faced in tool comparisons.
First, because our tool handles Java byte-code, we could
only compare it with others that handle languages also com-
piling to Java byte-code. For example, this precludes (or it
makes them hard) comparisons with testing tools supporting
C (e.g., CUTE [
39]) and C# (e.g., PEX [ 42]). Similarly, tool
prototypes are often targeted for speciﬁc operating system s;
e.g., PEX [ 42] and Dsc [ 28] only work with Windows.
Second, although there are popular testing tools for Java, a s
for example Randoop [ 36], those do not address our testing
problem (i.e., generating high coverage test suites that ar e
small, so non-automated oracles can be manually veriﬁed by
the software engineers). Third, some old tool prototypes ar e
no longer supported, and can give problems when used on
new versions of Java and/or SUTs with speciﬁc features (e.g. ,
we did not manage to run jCUTE on several of the SUTs we
experimented with). Fourth, some tool prototypes are simpl y
not publicly available, and re-implementing them would be
too time consuming and prone to errors and misunderstanding
in the implementation.
Another important point is that many testing tools are only
semi-automatic and, for example, require the user to writin g
drivers and ad hoc generators for speciﬁc type of objects. Th is
is a kind of problem we faced when we tried to compare
EVOSUITE with tools such as JPF [
45] and TestFul [ 13],
and which makes large empirical studies difﬁcult. Another
problem for empirical studies on testing is that the tools ne ed
to guarantee that the test code does not break anything, e.g., by
running it in a sandbox like E VOSUITE – this is usually not the
case (e.g. the Randoop documentation
1 states: “W ARNING:
Testing code that modiﬁes your ﬁle system might result in
Randoop generating tests that modify your ﬁle system! Be
careful when choosing classes and methods to test”.).
Often research prototypes have known limitations. For
example, Dsc [
28] clearly indicates in its documentation 2
that it does not support ﬂoating-point numbers and has only
basic support for strings. Such limitations would put these
prototypes in disadvantage in tool comparisons, although t hey
might feature novel algorithms that are very useful for the type
of program constructs (e.g., constraints on integer variab les)
that they can handle.
To the best of our knowledge, we have not found any other
test data generation tool in the literature that satisﬁes al l the
above requirements and that we could use for comparisons
1. http://randoop.googlecode.com/hg/doc/index.html, acc essed August
2011.
2. http://ranger.uta.edu/∼ csallner/dsc/index.html, accessed August 2011.
with E VOSUITE . There are however commercial tools that
are likely to satisfy those constraints, as for example the
ones developed by companies such as Parasoft
3 and Agitar 4.
Unfortunately, comparisons with commercial tools have the ir
own set of challenges. For example, usually the details of th e
underlying technologies of commercial tools are not disclosed.
Therefore, it would be hard to understand why they behave in
a particular way on some SUTs, and so explaining differences
in results would be infeasible.

## 6 C ONVERGENCE

Search algorithms can be run for any arbitrary amount of
time (or ﬁtness evaluations, depending on the chosen stoppi ng
criterion). The more time it is allowed for the search, the better
results we would expect on average. If given enough time, will
a GA ﬁnd an optimal solution? Or is there the possibility that
it will be stuck forever in a sub-optimal area of search space ?
The answer to these questions lies in the convergence analysis
of search algorithms [
38].
Standard evolutionary algorithms using elitism are proven
to converge to optimal solutions [ 38]. This means that, if
left running for an inﬁnite time, they will always ﬁnd an
optimal solution. Formally, given Po(i) the probability of
ﬁnding an optimal solution within i steps of the search, we
would have limi→∞Po(i) = 1 . Convergence in inﬁnite time
might be of little practical interest, as it is not feasible t o
run a search algorithm for inﬁnite time. Furthermore, given
the bounds N and L, an exhaustive enumeration of the entire
search space would also ﬁnd an optimal solution in ﬁnite time .
However, there is a major motivation for proving convergence:
Convergence should be a pre-requisite of any algorithm – if
an algorithm does not guarantee an optimal solution even if
run for inﬁnite time, then its use is questionable.
To use search algorithms for testing object-oriented soft-
ware, new search operators are often designed in the literature,
because the standard ones based on bit-strings cannot be use d
(e.g., [
43]). But once non-standard operators are used, the
theoretical results coming from the literature of evolutio nary
computation cannot be applied. If new search operators are
designed, it is hence important to prove the convergence of
the resulting new algorithms, and we do that for the GA we
use in this paper (the results can be directly extended to all the
other search algorithms that use the same mutation operator
described in Section
3.5.2). To the best of our knowledge, this
is the ﬁrst time this type of theoretical results is provided for
the problem of test data generation.
Let us deﬁne the number of “iterations” of a search algo-
rithm as the number of ﬁtness evaluations that are computed
(this is a typical procedure in the formal analysis of search
algorithms). The runtimeR of a search algorithm is a random
variable describing the number of iterations it needs to ﬁnd an
optimal solution. Notice that the notationPo(i) is equivalent to
P(R≤i). Let us assume that, before a solution is evaluated,
it is always mutated with an operator µ. It does not matter if
other search operators are applied before µ (as for example
3. http://www.parasoft.com, accessed August 2011.
4. http://www.agitar.com, accessed August 2011.

<!-- Page 14 -->

a crossover). The best solution seen so far is always stored
(i.e., elitism). Let us call A the class of algorithms for which
all the above conditions hold. Notice that the GA used in
this paper (depicted in Algorithm
1) belongs to the class
A. The following lemma provides sufﬁcient conditions for
which a search algorithm in A converges. This lemma is a
simpliﬁcation and adaptation of similar theoretical resul ts in
the literature of search algorithms [ 38].
Lemma 1: For the class of search algorithms A, if µ is
able to sample an optimal solution with probability p lower
bounded by a constant (i.e., p≥c for some constant c), then
the search algorithms using µ converge, i.e., limi→∞P(R≤
i) = 1 , where P(R ≤ i) is the probability of ﬁnding an
optimal solution within i iterations. Furthermore,E[R]≤ 1/c ,
i.e., the expected number of iterations is upper bounded by t he
constant 1/c .
Proof: Because we are interested in the convergence for
i→∞ , we do not need to study the exact dynamics of the
search algorithms. We just provide loose lower bounds to the
effectiveness that are high enough to prove this theorem. We
can focus only on the mutation operator µ and in its ability
of sampling an optimal solution with probability p≥ c. The
process of sampling an optimal solution with µ at iteration i
can be described as a geometric distribution with parameter
greater or equal than c (see [
16]). Therefore:
lim
i→∞
P(R≤i)≥ lim
i→∞
1− (1−c)i = 1 .
The expected value E of a geometric distribution with
parameterp is equal to 1/p (see [16]). Therefore,E[R]≤ 1/c .
Because the algorithms in A always store the best solution
seen so far, the convergence is hence proven.
To prove that our GA converges, it is sufﬁcient to prove that
our mutation operator described in Section 3.5.2 is always able
to sample an optimal solution with probability lower bounde d
by a constant.
Proposition 1: The mutation operator described in Section
3.5.2 is able to sample an optimal solution To with probability
p≥c, for some constant c, when applied to any test suite T
whose number of test cases and their length is bounded in N
and L, respectively.
Proof: To prove this proposition, we do not need to
provide tight bounds (i.e., the highest possible constant c).
Very loose bounds will be sufﬁcient. It will be enough to
prove that with constant probability we can remove and add
any number of test cases in T .
An optimal solution To is composed of no≤N test cases,
each one with length up to L. With probability that is at least
(1/N )N , all the test cases are mutated. With probability (1/ 3)·
(2/ 3)2, only the remove operation is applied on a test case.
With probability at least (1/L )L, all the statements in a test
case are removed. Therefore, all the test cases are removed
with probability at least:
ρ =
( 1
N
22
33
1
LL
) N
.
After removing all the test cases in T , exactly no new
random test cases will be added with probability ψ = (1−
σ no+1)× ∏ no
j=1σ j = (1 −σ no+1)×σ no(no+1)/2 (see Sec-
tion 3.5.2). In fact we need the ﬁrst insertion with probability
σ 1, then second with probability σ 2, and so on until the last
one with probability σ no. Then, for the (no + 1)th test case,
we do not insert it with probability 1−σ no+1.
When we generate a new test case at random, each possible
test case in the chosen representation (Section 3.2) can be
sampled with non-zero probability, although the sampling i s
not uniform (Section 3.5.3). Let Ω be the lowest probability
for a test case to be sampled. Because N, L and Imax are
ﬁnite, then Ω is a constant.
In an optimal test suite of sizeno, there would beno distinct
test cases. If any of these are equal, then the duplicates cou ld
be removed because they do not increase the coverage (in fact,
the execution of test cases is independent, so none of them ca n
have effects on the others). There can be several optimal tes t
suites with size no, but, as a lower bound, we can consider
just one. Because the order in which the test cases are sample d
is not important, we can consider all their no! permutations.
Therefore, sampling the right test cases has probability at least
Ψ = no!× Ω no.
Finally, we can prove that the probability p of sampling an
optimal solution is at least p≥c, where c =ρ×ψ× Ψ .
Although the conditions to apply Lemma 1 are very general,
and proving whether they hold is rather straightforward (se e
the proof of Proposition 1), for many mutation operators
proposed in the software testing literature (e.g., [ 43]) it does
not seem that Lemma 1 is applicable. However, Lemma 1 is a
sufﬁcient condition, and so it might not be necessary. In oth er
words, it could well be that all the techniques that have been
proposed so far in the literature do converge, even if Lemma
1
does not apply to them. However, if a technique does not
converge, there might be cases for which it might never ﬁnd a
solution even if left running for inﬁnite time. Without a for mal
proof that is valid for all software (as for example Lemma
1), it
would not be possible to know beforehand whether a technique
would converge on any particular addressed problem instanc e.

## 7 T HREATS TO VALIDITY

The focus of this paper is on comparing the approach “entire
test suite” to “one target at the time”.
Threats to construct validity are on how the performance of
a testing technique is deﬁned. We gave priority to the achieved
coverage, with the secondary goal of minimizing the length.
This yields two problems: (1) in practical contexts, we migh t
not want a much larger test suite if the achieved coverage is
only slightly higher, and (2) this performance measure doesnot
take into account how difﬁcult it will be to manually evaluat e
the test cases for writing assert statements (i.e., checkin g the
correctness of the outputs).
Threats to internal validity might come from how the
empirical study was carried out. To reduce the probability o f
having faults in our testing framework, it has been carefull y
tested. But it is well known that testing alone cannot prove
the absence of defects. Furthermore, randomized algorithm s
are affected by chance. To cope with this problem, we ran
each experiment 30 times, and we followed rigorous statistical
procedures to evaluate their results.

<!-- Page 15 -->

Another possible threat to internal validity is that we did
not study the effect of the different conﬁgurations for the
employed GA. In this paper we claim that E VOSUITE is
superior to the common approach of focusing on only one
target at the time. However, in theory it might be possible th at
there exist parameter settings for which the one target at th e
time approach is better than any conﬁguration of E VOSUITE .
To shed light on this possible issue, we would need to carry
out large tuning phases on both the two approaches. However,
as already explained earlier in the paper, we preferred to us e
the computational time of the experiments to have a much
larger case study rather than applying tuning phases.
Although we used both open source projects and industrial
software as case studies, there is the threat to external validity
regarding the generalization to other types of software, wh ich
is common for any empirical analysis. Furthermore, we evalu -
ated the optimization of entire test suites against going to each
testing target individually only by using a GA. The superior ity
of an E VOSUITE -like approach might not hold when other
testing techniques are employed (e.g., other types of searc h
algorithms such as Simulated Annealing).
Our E VOSUITE prototype might not be superior to all
existing testing tools; this, however, is not our claim: We
have shown that whole test suite generation is superior to a
traditional strategy targeting one test goal at a time. Basi cally,
this insight can be used to improve any existing testing
tool, independent of the underlying test criterion (e.g., b ranch
coverage, mutation testing, ...) or test generation techni que
(e.g., search algorithm), although such a generalization to other
techniques will of course need further evidence.

## 8 C ONCLUSIONS

Coverage criteria are a standard technique to automate test
generation. In this paper, we have shown that optimizing whole
test suites towards a coverage criterion is superior to the
traditional approach of targeting one coverage goal at a tim e.
In our experiments, this results in signiﬁcantly better ove rall
coverage with smaller test suites.
While we have focused on branch coverage in this paper, the
ﬁndings also carry over to other test criteria. Consequently, the
ability to avoid being misled by infeasible test goals can he lp
overcoming similar problems in other criteria, for example ,
the equivalent mutant problem in mutation testing [
29].
Even though the results achieved with E VOSUITE already
demonstrate that whole test suite generation is superior to
single target test generation, there is ample opportunity t o
further improve our E VOSUITE prototype. For example, there
is potential in combining search-based test generation wit h
dynamic symbolic execution (e.g., [
12], [ 33]), and search
optimizations such as testability transformation [ 24] or local
search [ 26] should further improve the achieved coverage.
Furthermore, there are general enhancements in the literat ure
of search algorithms that we could integrate and evaluate in
EVOSUITE , as for example island models (e.g., see the recent
[3]) and adaptive parameter control [ 32].
In our empirical study, we targeted object-oriented software.
However, the E VOSUITE approach could be easily applied
to procedural software as well, although further research i s
needed to assess the potential beneﬁts in such a context.
The approach presented in this paper aims at producing
small test suites with high coverage, such that the develope r
can add test oracles in terms of assertions. Although keepin g
the test suites small is helpful in this respect, the oracle p rob-
lem is still very difﬁcult. In this respect, we are investiga ting
ways to support the developer by automatically producing
effective [
21] assertions, and to ease understanding we try to
make the produced test cases more readable [ 20].
To learn more about E VOSUITE , visit our Web site:
http://www.evosuite.org
Acknowledgments. We thank Valentin Dallmeier, Yana Mil-
eva, Andrzej Wasylkowski and Andreas Zeller for comments
on earlier versions of this paper. This work is funded by a
Google Focused Research Award on “Test Ampliﬁcation” and
the Norwegian Research Council.

## References

[1] S. Ali, L. Briand, H. Hemmati, and R. Panesar-Walawege, “A s ystem-
atic review of the application and empirical investigation o f search-
based test-case generation,” IEEE Transactions on Software Engineering
(TSE), vol. 36, no. 6, pp. 742–762, 2010.
[2] M. Alshraideh and L. Bottaci, “Search-based software te st data gener-
ation for string data using program-speciﬁc search operator s: Research
articles,” Software Testing, Veriﬁcation, and Reliability , vol. 16, no. 3,
pp. 175–203, 2006.
[3] L. Araujo and J. Merelo, “Diversity through multicultura lity: Assessing
migrant choice policies in an island model,” Evolutionary Computation,
IEEE Transactions on , no. 99, pp. 1–14, 2011.
[4] A. Arcuri, “It really does matter how you normalize the bran ch distance
in search-based software testing,” Software Testing, Veriﬁcation and
Reliability (STVR), 2011, http://dx.doi.org/10.1002/stvr.457.
[5] ——, “A theoretical and empirical analysis of the role of te st sequence
length in software testing for structural coverage,” IEEE Transactions
on Software Engineering (TSE) , 2011.
[6] A. Arcuri and L. Briand, “Adaptive random testing: An ill usion of
effectiveness?” inACM Int. Symposium on Software Testing and Analysis
(ISSTA), 2011.
[7] ——, “A practical guide for using statistical tests to ass ess random-
ized algorithms in software engineering,” in ACM/IEEE International
Conference on Software Engineering (ICSE) , 2011, pp. 1–10.
[8] A. Arcuri and G. Fraser, “On parameter tuning in search bas ed software
engineering,” in International Symposium on Search Based Software
Engineering (SSBSE), 2011, pp. 33–47.
[9] A. Arcuri, M. Z. Iqbal, and L. Briand, “Black-box system t esting of
real-time embedded systems using random and search-based test ing,” in
IFIP International Conference on Testing Software and Systems (ICTSS),
2010, pp. 95–110.
[10] ——, “Random testing: Theoretical results and practica l implications,”
IEEE Transactions on Software Engineering (TSE) , vol. 38, no. 2, pp.
258–277, 2012.
[11] A. Arcuri and X. Yao, “Search based software testing of o bject-oriented
containers,” Information Sciences , vol. 178, no. 15, pp. 3075–3095,
2008.
[12] A. Baars, M. Harman, Y . Hassoun, K. Lakhotia, P. McMinn, P . Tonella,
and T. V os, “Symbolic search-based testing,” inIEEE/ACM Int. Confer-
ence on Automated Software Engineering (ASE) , 2011.
[13] L. Baresi, P. L. Lanzi, and M. Miraz, “Testful: an evolut ionary test
approach for java,” in IEEE International Conference on Software
Testing, Veriﬁcation and Validation (ICST), 2010, pp. 185–194.
[14] B. Baudry, F. Fleurey, J.-M. J ´ez´equel, and Y . Le Traon, “Automatic test
cases optimization: a bacteriologic algorithm,” IEEE Software, vol. 22,
no. 2, pp. 76–82, Mar. 2005.
[15] C. Csallner and Y . Smaragdakis, “JCrasher: an automatic r obustness
tester for Java,” Softw. Pract. Exper., vol. 34, pp. 1025–1050, 2004.
[16] W. Feller, An Introduction to Probability Theory and Its Applications ,
Vol. 1, 3rd ed. Wiley, 1968.

<!-- Page 16 -->

[17] G. Fraser and A. Arcuri, “Evolutionary generation of wh ole test suites,”
in International Conference On Quality Software (QSIC). Los Alamitos,
CA, USA: IEEE Computer Society, 2011, pp. 31–40.
[18] ——, “Evosuite: Automatic test suite generation for obje ct-oriented soft-
ware.” in ACM Symposium on the Foundations of Software Engineering
(FSE), 2011, pp. 416–419.
[19] ——, “It is not the length that matters, it is how you contro l it,” in
IEEE International Conference on Software Testing, Veriﬁc ation and
Validation (ICST), 2011, pp. 150 – 159.
[20] G. Fraser and A. Zeller, “Exploiting common object usage i n test
case generation,” in ICST’11: Proceedings of the 4th International
Conference on Software Testing, Veriﬁcation and Validatio n. IEEE
Computer Society, 2011, pp. 80–89.
[21] ——, “Mutation-driven generation of unit tests and orac les,” IEEE
Transactions on Software Engineering , vol. 99, no. PrePrints, 2011.
[22] P. Godefroid, N. Klarlund, and K. Sen, “DART: directed a utomated
random testing,” in PLDI’05: Proceedings of the 2005 ACM SIGPLAN
Conference on Programming Language Design and Implementat ion.
ACM, 2005, pp. 213–223.
[23] A. Goldberg, T. C. Wang, and D. Zimmerman, “Applications of feasible
path analysis to program testing,” in ISSTA’94: Proceedings of the
1994 ACM SIGSOFT International Symposium on Software Testi ng and
Analysis. ACM, 1994, pp. 80–94.
[24] M. Harman, L. Hu, R. Hierons, J. Wegener, H. Sthamer, A. Bar esel, and
M. Roper, “Testability transformation,” IEEE Transactions on Software
Engineering, vol. 30, no. 1, pp. 3–16, 2004.
[25] M. Harman, S. G. Kim, K. Lakhotia, P. McMinn, and S. Yoo.,
“Optimizing for the number of tests generated in search based t est
data generation with an application to the oracle cost probl em,” in
International Workshop on Search-Based Software Testing (SBST), 2010.
[26] M. Harman and P. McMinn., “A theoretical and empirical study of search
based testing: Local, global and hybrid search.” IEEE Transactions on
Software Engineering (TSE) , vol. 36, no. 2, pp. 226–247, 2010.
[27] K. Inkumsah and T. Xie, “Improving structural testing of o bject-oriented
programs via integrating evolutionary testing and symbolic e xecution,”
in ASE’08: Proc. of the 23rd IEEE/ACM Int. Conference on Automa ted
Software Engineering, 2008, pp. 297–306.
[28] M. Islam and C. Csallner, “Dsc+mock: A test case + mock clas s
generator in support of coding against interfaces,” in International
Workshop on Dynamic Analysis (WODA) , 2010, pp. 26–31.
[29] Y . Jia and M. Harman, “An analysis and survey of the develo pment of
mutation testing,” CREST Centre, King’s College London, London, UK,
Technical Report TR-09-06, September 2009.
[30] B. Korel, “Automated software test data generation,” IEEE Transactions
on Software Engineering , pp. 870–879, 1990.
[31] F. Lammermann, A. Baresel, and J. Wegener, “Evaluating evo lutionary
testability for structure-oriented testing with software measurements,”
Applied Soft Computing , vol. 8, no. 2, pp. 1018–1028, 2008.
[32] F. Lobo, C. Lima, and Z. Michalewicz, Parameter setting in evolutionary
algorithms. Springer Verlag, 2007, vol. 54.
[33] J. Malburg and G. Fraser, “Combining search-based and co nstraint-
based testing,” in IEEE/ACM Int. Conference on Automated Software
Engineering (ASE), 2011.
[34] P. McMinn, “Search-based software test data generatio n: A survey,”
Software Testing, Veriﬁcation and Reliability , vol. 14, no. 2, pp. 105–
156, 2004.
[35] W. Miller and D. L. Spooner, “Automatic generation of ﬂoa ting-point
test data,” IEEE Transactions on Software Engineering , vol. 2, no. 3,
pp. 223–226, 1976.
[36] C. Pacheco and M. D. Ernst, “Randoop: feedback-directe d random test-
ing for Java,” in OOPSLA’07: Companion to the 22nd ACM SIGPLAN
Conference on Object-oriented Programming Systems and App lication.
ACM, 2007, pp. 815–816.
[37] J. C. B. Ribeiro, “Search-based test case generation fo r object-
oriented Java software using strongly-typed genetic progr amming,” in
GECCO’08: Proceedings of the 2008 GECCO conference compani on
on Genetic and evolutionary computation. ACM, 2008, pp. 1819–1822.
[38] G. Rudolph, “Convergence analysis of canonical geneti c algorithms,”
IEEE transactions on Neural Networks , vol. 5, no. 1, pp. 96–101, 1994.
[39] K. Sen, D. Marinov, and G. Agha, “CUTE: a concolic unit te sting
engine for C,” in ESEC/FSE-13: Proc. of the 10th European Software
Engineering Conf. held jointly with 13th ACM SIGSOFT Int. Symposium
on Foundations of Software Engineering . ACM, 2005, pp. 263–272.
[40] R. Sharma, M. Gligoric, A. Arcuri, G. Fraser, and D. Marin ov, “Testing
container classes: Random or systematic?” in Fundamental Approaches
to Software Engineering (FASE) , 2011.
[41] S. Silva and E. Costa, “Dynamic limits for bloat control in genetic
programming and a review of past and current bloat theories,” Genetic
Programming and Evolvable Machines , vol. 10, no. 2, pp. 141–179,
2009.
[42] N. Tillmann and J. N. de Halleux, “Pex — white box test gene ration
for .NET,” in TAP’08: International Conference on Tests And Proofs ,
ser. LNCS, vol. 4966. Springer, 2008, pp. 134 – 253.
[43] P. Tonella, “Evolutionary testing of classes,” in ACM Int. Symposium on
Software Testing and Analysis (ISSTA) , 2004, pp. 119–128.
[44] A. Vargha and H. D. Delaney, “A critique and improvement of the CL
common language effect size statistics of McGraw and Wong,” Journal
of Educational and Behavioral Statistics , vol. 25, no. 2, pp. 101–132,
2000.
[45] W. Visser, C. S. Pasareanu, and S. Khurshid, “Test Input Generation
with Java PathFinder,” in ACM Int. Symposium on Software Testing and
Analysis (ISSTA), 2004, pp. 97–107.
[46] S. Wappler and I. Schieferdecker, “Improving evolution ary class testing
in the presence of non-public methods,” in IEEE/ACM Int. Conference
on Automated Software Engineering (ASE) , 2007, pp. 381–384.
[47] S. Wappler and F. Lammermann, “Using evolutionary algorit hms for the
unit testing of object-oriented software,” in GECCO’05: Proceedings of
the 2005 Conference on Genetic and Evolutionary Computation. ACM,
2005, pp. 1053–1060.
[48] J. Wegener, A. Baresel, and H. Sthamer, “Evolutionary te st environment
for automatic structural testing,” Information and Software Technology ,
vol. 43, no. 14, pp. 841–854, 2001.
[49] D. Whitley, “The genitor algorithm and selective pressu re: Why rank-
based allocation of reproductive trials is best,” in Proceedings of the
Third International Conference on Genetic Algorithms (ICGA-89), 1989,
pp. 116–121.
[50] N. Williams, B. Marre, P. Mouy, and M. Roger, “PathCrawle r: automatic
generation of path tests by combining static and dynamic analy sis,” in
EDCC’05: Proceedings ot the 5th European Dependable Comput ing
Conference, ser. LNCS, vol. 3463. Springer, 2005, pp. 281–292.
[51] T. Xie, D. Marinov, W. Schulte, and D. Notkin, “Symstra: A framework
for generating object-oriented unit tests using symbolic ex ecution,” in
TACAS’05: 11th International Conference on Tools and Algor ithms for
the Construction and Analysis of Systems. Springer, 2005, pp. 365–381.
[52] S. Zhang, D. Saff, Y . Bu, and M. Ernst, “Combined static an d dynamic
automated test generation,” in ACM Int. Symposium on Software Testing
and Analysis (ISSTA) , 2011.
PLACE
PHOTO
HERE
Gordon Fraser is a post-doc researcher at
Saarland University. He received a PhD in com-
puter science from Graz University of Technol-
ogy, Austria, in 2007, and his research concerns
the prevention, detection, and removal of defects
in software. He develops techniques to generate
test cases automatically, and to guide the tester
in validating the output of tests by producing test
oracles and speciﬁcations.
PLACE
PHOTO
HERE
Andrea Arcuri received a BSc and a MSc de-
gree in computer science from the University
of Pisa, Italy, in 2004 and 2006, respectively.
He received a PhD in computer science from
the University of Birmingham, England, in 2009.
Since then, he has been a research scientist
at Simula Research Laboratory, Norway. His re-
search interests include search based software
testing and analyses of randomized algorithms.
