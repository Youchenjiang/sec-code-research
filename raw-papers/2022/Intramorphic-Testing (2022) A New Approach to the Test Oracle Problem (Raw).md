# 30 Rigger2022 A New Approach to the Test Oracle Pro

- **Source File**: [`30_Rigger2022_A_New_Approach_to_the_Test_Oracle_Pro.pdf`](file:///c:/Users/g1014/Documents/GitHub/Youchen/code-security-research/papers/30_Rigger2022_A_New_Approach_to_the_Test_Oracle_Pro.pdf)
- **Total Pages**: 9

---

<!-- Page 1 -->

Intramorphic Testing
A New Approach to the Test Oracle Problem
Manuel Rigger
rigger@nus.edu.sg
National University of Singapore
School of Computing
Singapore
Zhendong Su
zhendong.su@inf.ethz.ch
ETH Zurich
Department of Computer Science
Switzerland

## Abstract

A test oracle determines whether a system behaves correctly
for a given input. Automatic testing techniques rely on an
automated test oracle to test the system without user inter-
action. Important families of automated test oracles include
Differential Testing and Metamorphic Testing, which are both
black-box approaches; that is, they provide a test oracle that
is oblivious to the system’s internals. In this work, we pro-
pose Intramorphic Testing as a white-box methodology to
tackle the test oracle problem. To realize an Intramorphic
Testing approach, a modified version of the system is created,
for which, given a single input, a test oracle can be provided
that relates the output of the original and modified systems.
As a concrete example, by replacing a greater-equals operator
in the implementation of a sorting algorithm with smaller-
equals, it would be expected that the output of the modified
implementation is the reverse output of the original imple-
mentation. In this paper, we introduce the methodology and
illustrate it via a set of use cases.
CCS Concepts: · Software and its engineering → Soft-
ware verification and validation .
Keywords:
test oracle problem, white-box testing, automated
testing
ACM Reference Format:
Manuel Rigger and Zhendong Su. 2022. Intramorphic Testing: A
New Approach to the Test Oracle Problem. In Proceedings of the
2022 ACM SIGPLAN International Symposium on New Ideas, New
Paradigms, and Reflections on Programming and Software (Onward!
’22), December 8ś10, 2022, Auckland, New Zealand. ACM, New York,
NY, USA, 9 pages. https://doi.org/10.1145/3563835.3567662
Onward! ’22, December 8ś10, 2022, Auckland, New Zealand
© 2022 Copyright held by the owner/author(s).
ACM ISBN 978-1-4503-9909-8/22/12.
https://doi.org/10.1145/3563835.3567662

## 1 Introduction

The test oracle problem is one of the greatest challenges for
software testing [1]. A test oracle is a mechanism to check the
correctness of a system’s output for a set of inputs [11]. Given
that software constantly evolves and typically lacks a formal
specification of the expected behavior, general test oracles
are difficult to obtain. However, partial test oracles are still
useful, as they can validate the output for some inputs [ 1].
In the most straightforward case, partial test oracles are
specified in the form of regression tests, where developers
specify the expected output of a test case.
A number of approaches have been proposed to allevi-
ate the test oracle problem through partial test oracles that
can be applied in an automated setting ( e.g., for automat-
ically generated tests) [ 1, 5, 20, 24]. The most influential
ones are differential testing [19] and metamorphic testing [4],
which, similar to regression testing, approach the problem
in a black-box manner; that is, they do not require access to
the program’s source code or internals. Differential testing
compares the output of various systems that implement the
same semantics; a mismatch between outputs for the same
test case indicates that at least one system is affected by a
bug. Metamorphic testing refers to a technique where, based
on an existing input to a system and its output, a new input
can be created for which the expected output is known.
This work presents Intramorphic Testing as a general
methodology toward the test oracle problem to complement
differential testing and metamorphic testing. The core idea
of Intramorphic Testing is to modify one or multiple com-
ponents of the system under test (SUT) in a way so that the
relationships between the outputs of the modified and orig-
inal systems for a set of inputs are known. Thus, different
from differential testing and metamorphic testing, Intramor-
phic Testing is a white-box approach that assumes access to
and knowledge of the system’s internals. Accordingly, we
expect concrete techniques to be realized by developersÐor
automatically derivedÐrather than implemented by testers.
In this paper, we present the general idea of Intramorphic
Testing and illustrate it with several concrete examples.
We believe that Intramorphic Testing techniques are al-
ready being realized and used by developers as part of an
effort to create testable code. However, they might have
been viewed as an undocumented implementation detail of
This work is licensed under a Creative Commons Attribution 4.0 Interna-
tional License.
128

<!-- Page 2 -->

Onward! ’22, December 8ś10, 2022, Auckland, New Zealand Manuel Rigger and Zhendong Su
a test suite, rather than an instance of a more broad testing
methodology. This paper aims to address this by unifying
such existing and future techniques under a common name
and abstract framework, thus fueling exchange and develop-
ment of Intramorphic Testing techniques.
In summary, this paper contributes the following:
• Intramorphic Testing, a general conceptual white-box
approach to tackling the test oracle problem;
• a conceptual comparison with regression testing, dif-
ferential testing, and metamorphic testing;
• examples that illustrate the idea.

## 2 Background and Motivation

Test oracles.
To the best of our knowledge, the term test
oracle was coined by Howden in 1978 [ 11]. Since then, a
number of approaches to tackle the problem have been pro-
posed, which were summarized in surveys by, for example,
Barr et al. [ 1] or Pezzè et al. [ 20]. Metamorphic testing was
proposed by Chen et al. in a technical report in 1998 [ 4]. Vari-
ous concrete metamorphic testing techniques were proposed
that were subsequently surveyed by, for example, Segura et
al. [24] or Chen et al. [ 5].
Terminology. Originally, a test oracle was defined to vali-
date a system’s output for a set of inputs [ 11]. This view is
restrictive, given that an input to the program might include
changes to the device or environment. Similarly, rather than
a directly-observable program output, non-functional obser-
vations include the program’s performance or changes to
the device’s state. Thus, Barr et al. [ 1] used stimuli for inputs
and observations for outputs to account for various testing
scenarios. We continue to use the original terminology of
inputs (denoted as
I ) and outputs (denoted as O), but refer
to them in the general sense of stimuli and observations. We
will denote the program under test as P.
Motivating Example. To outline the existing techniques
and our idea, let us assume a specific use case, namely that
we want to test the implementation of one or multiple sort-
ing algorithms.1 Let us assume that we implemented multi-
ple sorting algorithms such asbubble_sort(),insertion_sort(),
and merge_sort(). Let us also assume that we made a mistake
when implementing the in-place bubble_sort() algorithm, as
illustrated in Listing 1; the last array index in the code listing
should be j, rather than i. In the subsequent paragraphs,
we discuss how both instantiations of existing techniques as
well as an instantiation of the proposed Intramorphic Testing
technique could find the bug. In practice, we expect that In-
tramorphic Testing will be realized that can find bugs that are
overlooked, or difficult to find, by other testing approaches.
1A Jupyter Notebook with the code examples presented in this paper is
available at https://doi.org/10.5281/zenodo.7229326.
Regression Testing. Regression testing aims to ensure that
changes do not introduce bugs into the program through
manually written tests in which the developer specifies the
expected output. One common way of implementing regres-
sion tests is by implementing unit tests, where a specific unit
is tested in isolation.
To testbubble_sort() and the other sorting algorithms, we
could introduce unit tests with both typical inputs as well as
boundary values. Listing
2 shows a test case that triggers the
bug; sorting an array [3, 1, 2] incorrectly results in [1,←֓
2, 1], which does not match the expected array [1, 2, 3],
thus revealing the bug. Note that the test does not assume
access to the system’s internals; unit testing is a black-box
approach that could also be applied without access to the
source code. While unit testing is effective and widely used,
tests are typically implemented manually, and the developer
needs to specify the expected outcome of the test case.
Differential Testing.
Differential testing validates a set of
systems that implement the same semantics, by comparing
their output for a given input. As illustrated in Figure1, given
input I and equivalent systems P1, P2, . . . ,Pn, differential test-
ing validates that∀i, j : Pi(I) = Pj(I). Differential testing has
been applied to a variety of domains, such as, C/C++ com-
pilers [
31], Java Virtual Machines (JVMs) [ 6, 7], database
engines [25], debuggers [ 16], code coverage tools [ 32], sym-
bolic execution engines [ 13], SMT solvers [ 29], and Object-
Relational Mapping Systems (ORMs) [ 26].
As illustrated by Listing3, we can apply differential testing
by comparing the sorted arrays for multiple sorting algo-
rithms for the same input array. Given that the test oracle
requires no human in the loop, it can be effectively paired
with automated test generation; for example, in the listing,
we generate random arrays as test input. Note that the loop
does not terminate; in practice, it would be reasonable to
set a timeout or run the tests for a fixed number of itera-
tions. For an input array like
[3, 1, 2], differential testing
reveals a discrepancy between the output of the sorting algo-
rithms, demonstrating the bug. Similar to regression testing,
differential testing is a black-box approach; for example, we
could have also compared sorting algorithms implemented
in various languages based on checking their output alone.
Metamorphic Testing.
Metamorphic testing uses an input
to a system and its output to derive a new input for which a
test oracle can be provided via so-called Metamorphic Rela-
tions (MRs). This is illustrated in Figure 1. Given an input I
and P(I) = O, a follow-up input I′ is derived, so that a known
relationship between O and P(I′) = O′ is validated. Metamor-
phic testing is a high-level concept and finding effective MRs
is often challenging; MRs for testing various systems such as
compilers [15], database engines [ 22, 23], SMT solvers [ 30],
Android apps [27], as well as object detection systems [ 28]
have been proposed in the literature.
129

<!-- Page 3 -->

Intramorphic Testing Onward! ’22, December 8ś10, 2022, Auckland, New Zealand
Differential Testing
I
P
1
P
2
O
1
P
3
O
2
O
3
Metamorphic Testing
I
I'
P
O
O'
I
P
P' O ''
O
Intramorphic Testing
Oracle
for each
other
Interchangeable programs : P
1
(I) = P
2
(I) = P
3
(I) Derived follow-up input
Oracle
for each
other
Modified program
Oracle
for each
other
Figure 1. Differential testing, metamorphic testing, and Intramorphic Testing in comparison.
Listing 1. A Python implementation of bubble_sort affected
by a bug when swapping array elements.
def bubble_sort(arr):
length = len (arr)
for i in range (length):
for j in range (0, length - i - 1):
if arr[j] > arr[j+1]:
arr[j], arr[j+1] = arr[j+1], arr[ i]
return arr
Listing 2. A manually-written unit test.
arr = [3, 1, 2]
bubble_sort(arr)
assert arr == [1, 2, 3] # AssertionError, ←֓
actual: [1, 2, 1]
Listing 3. Differential testing using multiple implementa-
tions of sorting algorithms.
sorting_algorithms = [bubble_sort, merge_sort, ←֓
insertion_sort]
while True:
arr = get_random_array() # e.g., [3, 1, 2]
sorted_arrays = [alg(arr.copy()) for alg in ←֓
sorting_algorithms]
all_same = all (sorted_arr == sorted_arrays[0] ←֓
for sorted_arr in sorted_arrays)
assert all_same
As Listing 4 shows, we designed a MR that checks whether
the relative order of sorted elements is maintained when an
element is removed from an input array. For example, given
an input array i1 =[3, 1, 2] and a correctly-sorted array
o1 =[1, 2, 3], we derive a new input by removing one element
e from the input array, for example, e = 2, resulting in a new
input array i2 =[3, 1], for which we can infer the expected
result by removing e from o1, that is, o2 =[1, 3]. This specific
idea enables finding the bug as well. When passing[3, 1, 2] as
input array, the incorrect output[1, 2, 1] is produced; when
passing[3, 1] as input by removing 2, the output is [1, 3],
rather than[1, 1], breaking the MR’s assumption. As with
Listing 4. Metamorphic testing by comparing whether the
relative order is maintained for a smaller array.
while True:
arr = get_random_array()
if len (arr) >= 1:
sorted_arr = bubble_sort(arr.copy())
random_elem = random.choice(sorted_arr)
arr.remove(random_elem)
sorted_smaller_arr = bubble_sort(arr)
sorted_arr.remove(random_elem)
assert sorted_arr == sorted_smaller_arr
regression testing and unit testing, metamorphic testing is
a black-box approach. In contrast to differential testing, a
single implementation of a system ( e.g., sorting algorithm)
is sufficient to realize the technique.
Intramorphic Testing.
In this work, we propose Intramor-
phic Testing to tackle the test oracle problem by changing the
system under test so that, for a given input and the original
system’s output, an oracle for the output of the changed sys-
tem can be derived. Figure 1 illustrates the approach. Given
a program P, a new program P′ is derived for which, given
an input I , a known relationship between the two program’s
outputs (i.e., O = P(I) and O′ = P′(I)) is validated. Similar to
metamorphic testing, Intramorphic Testing is a high-level
idea and conceptualization, for which many instantiations
are possible.
To realize an Intramorphic Testing technique for our
use case, we could implement another alternative sorting
implementation bubble_sort_reverse() as a potential replace-
ment for bubble_sort() that sorts the array in descending
order. Thus, the expectation that we could check is that,
by reversing one of the two output arrays, two equiva-
lent arrays are obtained (see Listing
5). For example, for
an input [3, 1, 2], we would expect an output [3, 2, 1] for
bubble_sort_reverse() rather than [1, 2, 3]. This concrete In-
tramorphic Testing realization also detects the bug. Even if
bubble_sort_reverse() is affected by the same index bug ( i.e.,
by replacing only the comparison operator in Listing 1), it
would detect the bug, since bubble_sort() returns [3, 2, 3] as
130

<!-- Page 4 -->

Onward! ’22, December 8ś10, 2022, Auckland, New Zealand Manuel Rigger and Zhendong Su
Listing 5.
An Intramorphic Testing realization that adds an
additional reverse sorting function, whose reversed output
array is compared with the sorted output array of the original
sorting function.
while True:
arr = get_random_array()
sorted_arr = bubble_sort(arr.copy())
reverse_sorted_arr = bubble_sort_reverse(arr. ←֓
copy())
sorted_arr.reverse()
assert sorted_arr.reverse() == ←֓
reverse_sorted_arr
C
1
C
n
O
P
C
n-1
P ' = P[C
i
'/C
i
]
C
i
'/C
i
C
1
C
i
'
C
n
O '
C
n-1
C
i
Intramorphic
transformation
Test oracles
for each other
Figure 2. The core idea of Intramorphic Testing is to replace
a component so that the output is influenced in a known
way and can be related to the original system’s output.
an output and bubble_sort_reverse() would return [1, 2,←֓
1]. Note that, in order to realize the approach, we modified
the system under test by adding a new function, meaning
that the technique is a white-box approach; alternatively,
we could have also added an additional function argument
to define the sort order, or changed the function directly
to manually test the assumption underlying the test oracle.
The modification of the original program discriminates this
technique from regression testing, differential testing, and
metamorphic testing, which are all black-box techniques.

## 3 Intramorphic Testing

In this section, we present Intramorphic Testing and its scope
as well as its assumptions.
Programs as a composition of components.
It is intuitive
to think of a program P as a composition of components that
work together to achieve a certain desired functionality. For
example, graphical interfaces often implement the model-
view-controller pattern where the program consists of three
high-level components; the model represents the applica-
tion’s data structure, the view its (visual) representation, and
the controller accepts input and converts it to commands
for the model of the view [ 8]. Each such component in turn
likely consists of individual components, which can be mod-
ules or classes, blocks of code, operators, or expressionsÐwe
do not prescribe any particular granularity to components.
Based on this understanding, we can view P as a function
P(C1, . . . ,Ck), where C1, . . . ,Ck are P’s components.
Intramorphic Testing. Figure 2 illustrates the idea of In-
tramorphic Testing. Programmers developing P are expected
to have an intuition or concrete understanding of how chang-
ing a component Ci to C′
i affects the overall program. Let
us assume an input I to P, such that P(I) = O, that is, O
is the output from running the program P on input I . Let
Ci be a component of P, and C′
i be a modified component
derived from Ci . Let P′ = P[C′
i/Ci], that is, P′ is the program
where the component Ci is replaced by the component C′
i .
We refer to the method used to replace the component as
an intramorphic transformation. This local change induces
a global expectation at the program level. That is, we antic-
ipate P′(I) to change in a certain way with respect to P(I).
We refer to this expectation as an intramorphic relation and
can validate it on the outputs of P′(I) and P(I) by running
the programs; if the expectation is not met, program P or P′
is affected by a bug.
Challenges.
Designing Intramorphic Testing techniques is
challenging. Given that the main goal of testing is to uncover
bugs, an ideal transformation should be effective and yield
as few false alarms as possibleÐideally none. Considering
that developers need to implement the Intramorphic Testing
technique, doing so should require as little effort as possible.
Conceptually, P and P′ are separate programs. However, in
practice, the approach needs to be integrated into the devel-
opers’ workflows, where maintaining two separate program
versions seems impracticalÐprincipled approaches for main-
taining the program variants are needed. While we present
examples where we addressed these challenges, we expect
that future research will address them for various specific
domains and use cases.
Special case P(I) = P(I’).
A special case of Intramorphic
Testing is when P(I) = P(I′), that is, both the original and
modified programs produce the same output, which can be
achieved using various ways. This can be due to a semantics-
preserving transformation on P, producing an equivalent
program variant. Alternatively, multiple components might
be available that provide the same functionality; for example,
C might be a bubblesort, while C′ a quicksort, meaning that
they can be used interchangeably for most purposes. It is
also plausible that on the source code level,
P = P′, that
is, the two program versions are equivalent, but that, when
compiled to machine code, P /nequalP′, that is, the versions differ.
For example, different binary versions could be obtained by
compiling P and P′ with different compilers, different opti-
mization levels, or different static application options ( e.g.,
using macro metaprogramming [ 17]), which closely relates
to differential testing. Conceptually, this special case also
131

<!-- Page 5 -->

Intramorphic Testing Onward! ’22, December 8ś10, 2022, Auckland, New Zealand
relates to N-version programming [ 3], where multiple pro-
grams are developed based on the same initial specification.
Classification. Intramorphic Testing can be classified along
various dimensions:
• the granularity of the replaced component Ci (e.g.,
reaching from a replaced operator to a replaced system
in a system of systems);
• the format of the program P (e.g., source code or binary
code);
• how the metamorphic transformation is applied ( e.g.,
by adding a new source code component or directly
replacing it);
• the degree of automation for the intramorphic trans-
formation (e.g., whether the transformation is applied
manually or can be automatically applied to many
components);
• whether the intramorphic relation is complete ( i.e.,
whether the expected output can be given for any
input);
• whether the approach can result in false alarmsÐin
general, it is desirable for an automated testing ap-
proach that it only detects real bugs.
White-box approach. Intramorphic Testing is a white-box
approach, since it relies on modifying P. This contrasts the
approach from differential testing and metamorphic testing,
which are both black-box approaches. This influences the
target audience of the testing approach; Intramorphic Testing
might be primarily applicable for developers who want to
test their system, as they have a concrete understanding of
the system that they are developing. Similarly to approaches
for finding metamorphic relations [
12, 33], future approaches
to identifying and applying intramorphic transformations
and relations could be explored.

## 4 Examples

In this section, we illustrate three realizations of Intramor-
phic Testing techniques on well-scoped examples.
Example 1: Infix, prefix, and postfix printing.

## Abstract

syntax trees (ASTs) are a common way to represent programs.
For example, an arithmetic expression (a + 3)* 2 could
be represented as a tree Operation('*', Operation('+',←֓
Variable('a'), Constant(3)), Constant(2)), whereOperation←֓
is the constructor for a binary operation node expecting
the operator and the two operands as well as Constant and
Variable the constructors for integer constants and named
variables nodes. We assume that we want to test a method
as_string that is implemented by every node.
The most common way to print an AST is assuming
infix notation, where, for a binary operation, the operator
is printed between its operands. As in the example above,
a drawback of the infix notation is that operations need
to be parenthesized when an outer operator has a higher
precedence than an inner one. As Listing
6 shows, in our
implementation, we account for this by explicitly checking
whether the current operation is a multiplication and one
of the child nodes an addition, in which case the addition
needs to be parenthesized.
Implementations for the postfix and prefix notations are
more compact and less error-prone. The reason for this is that
for these notations, the order is unambiguous. For example,
the expression (a + 3)* 2 would be printed as * + a 3 2 in
prefix notation and as a 3 + 2 * in postfix notation.
We realize our testing approach based on the insight that
the original program can be modified by adding the pre-
fix and postfix printing functions, as demonstrated by the
functions
as_string_prefix and as_string_postfix (Listing 6),
which are more likely to be correct. As a specific test ora-
cle, we can test whether the same operations, variables, and
constants are printed by deriving all three representations
and comparing whether their individual tokens are the same,
after removing the parentheses from the infix notation (see
Listing 7). This allows detecting bugs where, for example, a
mistake was made when assigning the parenthesized expres-
sion (e.g., right = '('+ left + ')').
This example shows how Intramorphic Testing can be
useful to test a system where a complex component can be
replaced with a simpler one, and the output of the system
differs in a known way between the two components. We
implemented the test harness as an infinite loop. In practice,
it could be run for fixed inputs or a limited amount of time.
Example 2: Monte Carlo Simulations.
Monte Carlo sim-
ulations are often used for simulating complex systems in
physics [10]. They are a class of algorithms that rely on re-
peated sampling to obtain numerical results. Due to their
non-deterministic nature, testing Monte Carlo simulations is
generally difficult. However, for this example, for simplicity,
we assume that we would like to validate the correct imple-
mentation of a Monte Carlo simulation to estimate the value
of pi, for which we know the ground truth.
Listing 8 shows how we can use Monte Carlo
simulation to approximate the value of pi. The initial
get_pi_approximation function expects no arguments and
takes 1,000,000 samples. In each iteration, random x and y co-
ordinates are drawnÐthe call to the random function returns
a value from the interval[0.0, 1.0), effectively only consid-
ering a rectangle around the circle. We assume the circle’s
radius to be 1; thus, checking x**2+y**2 <= 1 corresponds to
checking whether the sample is part of the circle. Figure 3
illustrates the simulation; for the green points within the
circle, the inside variable is incremented.
The accuracy of the result of Monte Carlo simulations
converges towards the real value given a large number of
sampling steps [9]. According to the law of large numbers,
by sampling n steps with n→∞ , we expect to obtain an ap-
proximation of pi that is close to its real value. As a practical
132

<!-- Page 6 -->

Onward! ’22, December 8ś10, 2022, Auckland, New Zealand Manuel Rigger and Zhendong Su
Listing 6.
Infix as_string printing function as well as subse-
quently added prefix and postfix versions for testing. The
line prefixed by
+ were added to realize the Intramorphic
Testing approach.
class Operation:
def as_string(self):
left = self.left.as_string()
right = self.right.as_string()
if self.operator == '* ':
if isinstance (self.left, Operation) and ←֓
self.left.operator == '+ ':
left = '( ' + left + ') '
if isinstance (self.right, Operation) and ←֓
self.right.operator == '+ ':
right = '( ' + right + ') '
return '%s␣%s␣%s ' % (left, self.operator, ←֓
right)
+ def as_string_prefix(self):
+ return '%s␣%s␣%s ' % (self.operator, self. ←֓
left.as_string_prefix(), self.right. ←֓
as_string_prefix())
+
+ def as_string_postfix(self):
+ return '%s␣%s␣%s ' % (self.left. ←֓
as_string_postfix(), self.right. ←֓
as_string_postfix(), self.operator)
Listing 7.
Test harness to validate that for each string rep-
resentation, the same tokens are printed.
while True:
tree = random_tree()
tree_str = tree.as_string()
tree_prefix_str = tree.as_string_prefix()
tree_postfix_str = tree.as_string_postfix()
infix_tokens = sorted (tree_str.replace( '( ', ' '←֓
replace( ') ', ' ').split( '␣ '))
prefix_tokens = sorted (tree_prefix_str.split( '←֓
␣ '))
postfix_tokens = sorted (tree_postfix_str.split ←֓
(' ␣ '))
assert infix_tokens == prefix_tokens and ←֓
infix_tokens == postfix_tokens
realization of intramorphic testing, as shown in Listing 9, we
validate that we obtain a less accurate approximation of pi by
obtaining a low number of samples ( 10 in the listing), rather
than by using a large number of samples ( 1, 000, 000). While
there is no theoretical guarantee for this invariant to hold
in theory, we observed that it holds in practice. To specify
the number of samples, we modified get_pi_approximation in
Listing 8 to take take a parameter.
This realization of an intramorphic testing approach
demonstrates how numerical algorithms can be tested. In
Listing 8. Monte Carlo approximation of pi. The lines pre-
fixed by + were added to realize the Intramorphic Testing
approach, while the lines prefixed by - were removed.
- def get_pi_approximation():
+ def get_pi_approximation(n):
inside = 0
- for _ in range (1000000):
+ for _ in range (n):
x = random.random()
y = random.random()
if x**2+y**2 <= 1:
inside += 1
- pi = 4*inside/1000000
+ pi = 4*inside/n
return pi
Listing 9.
Test harness for the Monte Carlo approximation.
while True:
pi_diff_inacc = abs (get_pi_approximation(10)- ←֓
math.pi)
pi_diff_acc = abs (get_pi_approximation ←֓
1000000)- math.pi)
assert pi_diff_inacc >= pi_diff_acc
−1.00 −0.75 −0.50 −0.25 0.00 0.25 0.50 0.75 1.00
x
−1.00
−0.75
−0.50
−0.25
0.00
0.25
0.50
0.75
1.00
y
Figure 3. Visualization of the sampled points by the Monte
Carlo simulation to compute pi.
this case, the program is modified to use a smaller (or larger)
number of samples, with the expectation of obtaining a bet-
ter estimate with more samples. In practice, multiple samples
could be taken to avoid false alarms caused by improbable
cases where simulations with a fewer number of samples re-
sult in an approximation that is closer to the real value than
simulations with a larger number of samples. In contrast to
the first example, rather than adding a function, we modified
an existing function to take an additional parameter.
133

<!-- Page 7 -->

Intramorphic Testing Onward! ’22, December 8ś10, 2022, Auckland, New Zealand
0 100000 200000 300000 400000 500000
Iteration Number
3.10
3.12
3.14
3.16
3.18
3.20
Estimate for pi
Figure 4. With an increasing number of samples, the ap-
proximated value of pi converges towards its real value.
Example 3: Knapsack problem.
The knapsack problem is a
well-studied combinatorics problem; many real-world combi-
natorics problems can be encoded as knapsack problems [14].
Given a knapsack with a given capacity, the goal is to pack
items to maximize the value of items in the knapsack. Each
item has a value and weight associated with it. The items’
combined weight must not exceed the knapsack’s capacity.
Various variations of the problems exist. In this example, we
consider the unbounded knapsack problem, which places no
restriction on the number of copies of each item.
Let us assume that our implementation solves the knap-
sack problem using a greedy approach, as illustrated in List-
ing 10, as computing an optimal solution could be consid-
ered too resource-intensive. The parameter objects is a list
of triples ((name, value, weight)), that is, the name of the ob-
ject, its value (sometimes referred to as profit), and weight.
The second parameter capacity denotes the capacity of the
knapsack. The algorithm first sorts all items by value /←֓
weight, and then adds items to the knapsack as long as its
capacity is not exceeded. The algorithm has no guarantees
of computing an optimal solution.
The idea to test the implementation using intramorphic
testing is that we can replace the greedy algorithm with
the result of an algorithm that computes the optimal so-
lution, knowing that the result should be as least as good
as for the greedy algorithm. The test harness is shown in
Listing
11. The exhaustive algorithm that recursively ex-
plores all feasible solutions is implemented by the function
knapsack_exhaustive in Listing 10. The core idea of the algo-
rithm is that for every item at index item_index, the algorithm
explores separate branches assuming that the item is and is
not included in the knapsack.
While we chose the knapsack algorithm as an example, we
believe that intramorphic testing can be used for a wide range
of algorithms used to solve NP-complete problems or provide
approximate solutions; for example, register allocation is a
NP-complete problem and the same idea could be used to
Listing 10. Greedy and optimal algorithms to solve the knap-
sack problem.
def knapsack_greedy(objects, capacity):
packed = []
cum_value = 0
cum_weight = 0
objects.sort(key= lambda triple : float (←֓
triple[1]) / triple[2], reverse=True)
for (item, value, weight) in objects:
while cum_weight + weight <= capacity:
cum_weight += weight
cum_value += value
packed.append(item)
return (packed, cum_value, cum_weight)
+ def knapsack_exhaustive(objects, capacity):
+ return knapsack_recursive(objects, capacity ←֓
0, [], 0, 0)
+ def knapsack_recursive(objects, capacity, ←֓
item_index, packed, cum_value, cum_weight):
+ if capacity <= 0 or item_index >= len (←֓
objects):
+ return (packed, cum_value, cum_weight)
+ current_included_profit, ←֓
current_excluded_profit = 0, 0
+ space = False
+ cur_name, cur_value, cur_weight = objects[ ←֓
item_index]
+ if cur_weight <= capacity:
+ included_packed = packed.copy()
+ included_packed.append(cur_name)
+ current_included = knapsack_recursive( ←֓
objects, capacity - cur_weight, item_index, ←֓
included_packed, cum_value + cur_value, ←֓
cum_weight + cur_weight)
+ space = True
+ current_excluded = knapsack_recursive( ←֓
objects, capacity, item_index + 1, packed, ←֓
cum_value, cum_weight)
+ if space and (current_included[1] > ←֓
current_excluded[1]):
+ return current_included
+ else :
+ return current_excluded
compare a greedy linear-scan register allocator [ 21] with a
graph coloring one [2]. In contrast to the other two examples,
the change to the program was larger and more complex;
however, the run-time characteristics and guarantees could
be easier understood for such an optimal algorithm than for
a greedy approach.

## 5 Discussion

Examples.
We have presented three realizations of In-
tramorphic Testing approaches on diverse, narrowly-scoped
134

<!-- Page 8 -->

Onward! ’22, December 8ś10, 2022, Auckland, New Zealand Manuel Rigger and Zhendong Su
Listing 11.
Comparing the results of the optimal with the
greedy algorithm.
while True:
capacity = random_capacity()
vals = random_items()
(_, val_exh, _) = knapsack_exhaustive(vals, ←֓
capacity)
print (knapsack_exhaustive(vals, capacity))
(_, val_greedy, _) = knapsack_greedy(vals, ←֓
capacity)
assert val_exh >= val_greedy
problems. These examples demonstrate the approach’s gen-
eral idea as well as the challenges of designing intramorphic
transformations. We believe that in the future, various In-
tramorphic Testing techniques will be proposed that will op-
erate at various levels and based on different insights, which
could be, for example, specific to the domain or application.
Scope of the paper. We have illustrated the approach’s gen-
eral idea on examples, and refrained from discussing and
evaluating Intramorphic Testing techniques on large real-
world applications. We took inspiration from the original
technical report on metamorphic testing, which was orga-
nized in a similar way; its practical merit was demonstrated
in many innovative follow-up works [ 5, 24].
Cost. Besides the potential benefit in finding bugs, Intramor-
phic Testing incurs both immediate and long-term costs. The
main immediate cost is the manual effort needed to imple-
ment the approach. In addition, more code incurs a higher
complexity; additional parameters and conditionals intro-
duced may cause bugs. Moreover, Intramorphic Testing also
has a long-term cost, as the intramorphic transformations
need to be maintainedÐchanges in the codebase may require
changes to the transformations.
Future research.
We believe that future research might
lower the cost of Intramorphic Testing and make it more
practical. For example, rather than manually writing tests,
future techniques could automatically suggest intramorphic
relations. As another example, similar to inline tests [ 18],
approaches could be developed that facilitate co-evolvement
of the source code and intramorphic tests.

## 6 Conclusion

We have presented Intramorphic Testing, a general approach
to tackling the test oracle problem, and illustrated it with
various examples. The core idea of Intramorphic Testing is to
modify a component of the system under test, anticipating a
change on the program level. If this anticipated change does
not hold, we have discovered a bug in the system. We believe
that this technique will be widely useful to test systems while
incorporating the domain knowledge of developers.
Acknowledgments
This research was supported by a Ministry of Education
(MOE) Academic Research Fund (AcRF) Tier 1 grant.

## References

[1] Earl T. Barr, Mark Harman, Phil McMinn, Muzammil Shahbaz, and
Shin Yoo. 2015. The Oracle Problem in Software Testing: A Survey.
IEEE Trans. Softw. Eng. 41, 5 (may 2015), 507ś525. https://doi.org/10.
1109/TSE.2014.2372785
[2] Gregory J. Chaitin, Marc A. Auslander, Ashok K. Chandra, John Cocke,
Martin E. Hopkins, and Peter W. Markstein. 1981. Register Allocation
via Coloring. Comput. Lang. 6, 1 (jan 1981), 47ś57.
[3] Liming Chen and Algirdas Avizienis. 1978. N-version programming:
A fault-tolerance approach to reliability of software operation. In Proc.
8th IEEE Int. Symp. on Fault-Tolerant Computing (FTCS-8) , Vol. 1. 3ś9.
[4] Tsong Y Chen, Shing C Cheung, and Shiu Ming Yiu. 1998. Metamorphic
testing: a new approach for generating next test cases. (1998).
[5] Tsong Yueh Chen, Fei-Ching Kuo, Huai Liu, Pak-Lok Poon, Dave
Towey, T. H. Tse, and Zhi Quan Zhou. 2018. Metamorphic Testing: A
Review of Challenges and Opportunities. ACM Comput. Surv. 51, 1,
Article 4 (jan 2018), 27 pages. https://doi.org/10.1145/3143561
[6] Yuting Chen, Ting Su, and Zhendong Su. 2019. Deep Differential
Testing of JVM Implementations. InProceedings of the 41st International
Conference on Software Engineering (Montreal, Quebec, Canada) (ICSE
’19). IEEE Press, 1257ś1268. https://doi.org/10.1109/ICSE.2019.00127
[7] Yuting Chen, Ting Su, Chengnian Sun, Zhendong Su, and Jianjun Zhao.
2016. Coverage-Directed Differential Testing of JVM Implementations.
In Proceedings of the 37th ACM SIGPLAN Conference on Programming
Language Design and Implementation (Santa Barbara, CA, USA) (PLDI
’16). Association for Computing Machinery, New York, NY, USA, 85ś99.
https://doi.org/10.1145/2908080.2908095
[8] Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides.
1995. Design Patterns: Elements of Reusable Object-Oriented Software .
Addison-Wesley Longman Publishing Co., Inc., USA.
[9] Carl Graham and Denis Talay. 2013. Strong Law of Large Numbers and
Monte Carlo Methods . Springer Berlin Heidelberg, Berlin, Heidelberg,
13ś35. https://doi.org/10.1007/978-3-642-39363-1_2
[10] John Hammersley. 2013. Monte carlo methods . Springer Science &
Business Media.
[11] W.E. Howden. 1978. Theoretical and Empirical Studies of Program
Testing. IEEE Transactions on Software Engineering SE-4, 4 (1978),
293ś298. https://doi.org/10.1109/TSE.1978.231514
[12] Upulee Kanewala and James M Bieman. 2013. Using machine learning
techniques to detect metamorphic relations for programs without
test oracles. In 2013 IEEE 24th International Symposium on Software
Reliability Engineering (ISSRE) . IEEE, 1ś10.
[13] Timotej Kapus and Cristian Cadar. 2017. Automatic Testing of Sym-
bolic Execution Engines via Program Generation and Differential Test-
ing. In Proceedings of the 32nd IEEE/ACM International Conference on
Automated Software Engineering (Urbana-Champaign, IL, USA) (ASE
2017). IEEE Press, 590ś600.
[14] Hans Kellerer, Ulrich Pferschy, and David Pisinger. 2004. Knapsack
Problems. Springer Berlin Heidelberg, Berlin, Heidelberg. 1ś14 pages.
https://doi.org/10.1007/978-3-540-24777-7_1
[15] Vu Le, Mehrdad Afshari, and Zhendong Su. 2014. Compiler Val-
idation via Equivalence modulo Inputs. In Proceedings of the 35th
ACM SIGPLAN Conference on Programming Language Design and Im-
plementation (Edinburgh, United Kingdom) (PLDI ’14) . Association
for Computing Machinery, New York, NY, USA, 216ś226. https:
//doi.org/10.1145/2594291.2594334
[16] Daniel Lehmann and Michael Pradel. 2018. Feedback-Directed Differ-
ential Testing of Interactive Debuggers. In Proceedings of the 2018 26th
ACM Joint Meeting on European Software Engineering Conference and
135

<!-- Page 9 -->

Intramorphic Testing Onward! ’22, December 8ś10, 2022, Auckland, New Zealand
Symposium on the Foundations of Software Engineering (Lake Buena
Vista, FL, USA) (ESEC/FSE 2018). Association for Computing Machinery,
New York, NY, USA, 610ś620. https://doi.org/10.1145/3236024.3236037
[17] Jorg Liebig, Sven Apel, Christian Lengauer, Christian Kästner, and
Michael Schulze. 2010. An analysis of the variability in forty
preprocessor-based software product lines. In 2010 ACM/IEEE 32nd
International Conference on Software Engineering , Vol. 1. 105ś114.
https://doi.org/10.1145/1806799.1806819
[18] Yu Liu, Pengyu Nie, Owolabi Legunsen, and Milos Gligoric. 2022. Inline
Tests. In International Conference on Automated Software Engineering .
To appear.
[19] William M. McKeeman. 1998. Differential Testing for Software. DIGI-
TAL TECHNICAL JOURNAL 10, 1 (1998), 100ś107.
[20] Mauro Pezzè and Cheng Zhang. 2014. Chapter One - Automated Test
Oracles: A Survey. Advances in Computers, Vol. 95. Elsevier, 1ś48.
https://doi.org/10.1016/B978-0-12-800160-8.00001-2
[21] Massimiliano Poletto and Vivek Sarkar. 1999. Linear Scan Register
Allocation. ACM Trans. Program. Lang. Syst. 21, 5 (sep 1999), 895ś913.
https://doi.org/10.1145/330249.330250
[22] Manuel Rigger and Zhendong Su. 2020. Detecting Optimization Bugs
in Database Engines via Non-Optimizing Reference Engine Construction .
Association for Computing Machinery, New York, NY, USA, 1140ś1152.
https://doi.org/10.1145/3368089.3409710
[23] Manuel Rigger and Zhendong Su. 2020. Finding Bugs in Database
Systems via Query Partitioning. Proc. ACM Program. Lang. 4, OOPSLA,
Article 211 (nov 2020), 30 pages. https://doi.org/10.1145/3428279
[24] Sergio Segura, Gordon Fraser, Ana B. Sanchez, and Antonio Ruiz-
Cortés. 2016. A Survey on Metamorphic Testing. IEEE Transactions on
Software Engineering 42, 9 (2016), 805ś824. https://doi.org/10.1109/
TSE.2016.2532875
[25] Donald R. Slutz. 1998. Massive Stochastic Testing of SQL. InProceedings
of the 24rd International Conference on Very Large Data Bases (VLDB ’98).
Morgan Kaufmann Publishers Inc., San Francisco, CA, USA, 618ś622.
[26] Thodoris Sotiropoulos, Stefanos Chaliasos, Vaggelis Atlidakis, Dimitris
Mitropoulos, and Diomidis Spinellis. 2021. Data-Oriented Differential
Testing of Object-Relational Mapping Systems. In 2021 IEEE/ACM 43rd
International Conference on Software Engineering (ICSE) . 1535ś1547.
https://doi.org/10.1109/ICSE43902.2021.00137
[27] Ting Su, Yichen Yan, Jue Wang, Jingling Sun, Yiheng Xiong, Geguang
Pu, Ke Wang, and Zhendong Su. 2021. Fully Automated Functional
Fuzzing of Android Apps for Detecting Non-Crashing Logic Bugs.
Proc. ACM Program. Lang. 5, OOPSLA, Article 156 (oct 2021), 31 pages.
https://doi.org/10.1145/3485533
[28] Shuai Wang and Zhendong Su. 2020. Metamorphic Object Insertion for
Testing Object Detection Systems. In Proceedings of the 35th IEEE/ACM
International Conference on Automated Software Engineering (Virtual
Event, Australia) (ASE ’20) . Association for Computing Machinery,
New York, NY, USA, 1053ś1065. https://doi.org/10.1145/3324884.
3416584
[29] Dominik Winterer, Chengyu Zhang, and Zhendong Su. 2020. On the
Unusual Effectiveness of Type-Aware Operator Mutations for Testing
SMT Solvers. Proc. ACM Program. Lang. 4, OOPSLA, Article 193 (nov
2020), 25 pages. https://doi.org/10.1145/3428261
[30] Dominik Winterer, Chengyu Zhang, and Zhendong Su. 2020. Vali-
dating SMT Solvers via Semantic Fusion. In Proceedings of the 41st
ACM SIGPLAN Conference on Programming Language Design and Im-
plementation (London, UK) (PLDI 2020). Association for Computing
Machinery, New York, NY, USA, 718ś730. https://doi.org/10.1145/
3385412.3385985
[31] Xuejun Yang, Yang Chen, Eric Eide, and John Regehr. 2011. Finding
and Understanding Bugs in C Compilers. SIGPLAN Not. 46, 6 (jun
2011), 283ś294. https://doi.org/10.1145/1993316.1993532
[32] Yibiao Yang, Yuming Zhou, Hao Sun, Zhendong Su, Zhiqiang Zuo,
Lei Xu, and Baowen Xu. 2019. Hunting for Bugs in Code Coverage
Tools via Randomized Differential Testing. In Proceedings of the 41st
International Conference on Software Engineering (Montreal, Quebec,
Canada) (ICSE ’19). IEEE Press, 488ś499. https://doi.org/10.1109/ICSE.
2019.00061
[33] Jie Zhang, Junjie Chen, Dan Hao, Yingfei Xiong, Bing Xie, Lu Zhang,
and Hong Mei. 2014. Search-Based Inference of Polynomial Meta-
morphic Relations. In Proceedings of the 29th ACM/IEEE International
Conference on Automated Software Engineering (Vasteras, Sweden)
(ASE ’14). Association for Computing Machinery, New York, NY, USA,
701ś712. https://doi.org/10.1145/2642937.2642994
Received 2022-07-12; accepted 2022-10-02
136

