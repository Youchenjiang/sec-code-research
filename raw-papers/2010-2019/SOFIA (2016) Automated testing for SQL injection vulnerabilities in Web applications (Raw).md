# 03 SOFIA2016 Automated testing for SQL injection

- **Source File**: [`03_SOFIA2016_Automated_testing_for_SQL_injection.pdf`](file:///c:/Users/g1014/Documents/GitHub/Youchen/code-security-research/papers/03_SOFIA2016_Automated_testing_for_SQL_injection.pdf)
- **Total Pages**: 11

---

<!-- Page 1 -->

Automated Testing for SQL Injection Vulnerabilities: An
Input Mutation Approach
Dennis Appelt, Cu Duy Nguyen, and
Lionel C. Briand
Interdisciplinary Centre for Security , Reliability
and T rust
University of Luxembourg, Luxembourg
{dennis.appelt,duy.nguyen,lionel.briand}@uni.lu
Nadia Alshahwan
Centre for Research one Evolution, Search and
T esting
Department of Computer Science, University
College London, UK
nadia.alshahwan@ucl.ac.uk

## Abstract

Web services are increasingly adopted in various domains,
from ﬁnance and e-government to social media. As they
are built on top of the web technologies, they suﬀer also an
unprecedented amount of attacks and exploitations like the
Web. Among the attacks, those that target SQL injection
vulnerabilities have consistently been top-ranked for the last
years. Testing to detect such vulnerabilities before making
web services public is crucial. We present in this paper an
automated testing approach, namely µ4SQLi, and its un-
derpinning set of mutation operators. µ4SQLi can produce
eﬀective inputs that lead to executable and harmful SQL
statements. Executability is key as otherwise no injection
vulnerability can be exploited. Our evaluation demonstrated
that the approach is eﬀective to detect SQL injection vul-
nerabilities and to produce inputs that bypass application
ﬁrewalls, which is a common conﬁguration in real world.
Categories and Subject Descriptors
D.2.5 [Testing and Debugging]
General Terms
Reliability; Security
Keywords
Mutation Testing; SQL Injection; Test Generation.
1. INTRODUCTION
The Service Oriented Architecture (SOA) paradigm has
been rapidly adopted in a wide range of areas, from ﬁnan-
cial systems, business integration and e-government to so-
cial media and end-user mobile applications. This shift has
been further accelerated by the rise of cloud-based systems.
There are currently more than ten thousand public web ser-
Permission to make digital or hard copies of all or part of this work for
personal or classroom use is granted without fee provided that copies are
not made or distributed for proﬁt or commercial advantage and that copies
bear this notice and the full citation on the ﬁrst page. To copy otherwise, to
republish, to post on servers or to redistribute to lists, requires prior speciﬁc
permission and/or a fee.
ISSTA ’14, July 21-25, 2014, San Jose, CA, USA
Copyright 2014 ACM 978-1-4503-2645-2/14/07 ...$10.00.
vices (key units in the SOA) available1. The number is even
larger if we consider also private web services that are de-
ployed within and among institutions.
The popularity of SOA applications can be attributed to
their continuous availability, interoperability, and ﬂexibil-
ity. However, this also makes them attractive to malicious
users. The number of reported web vulnerabilities is growing
sharply [13]. Recent vulnerability reports found that web-
based systems can receive up to 26 attacks per minute [6].
A security testing survey of publicly available web services
owned by companies such as Microsoft and Google found
that at least 8% of web services contained vulnerabilities
[31]. These ﬁndings, together with the high pressure of time
to market, suggest the need for automated security testing
approaches that can cope with the increasing security risks
and the limited time and resources allocated for testing.
Throughout the past decade, SQL injection (SQLi) vul-
nerabilities have been consistently ranked by the Open Web
Application Security Project (OWASP) 2 as a top security
risk. SQLi attacks target database-driven systems by inject-
ing SQL code fragments into vulnerable input parameters
that are not properly checked and sanitised. These injected
code fragments could change the application’s behaviour if
they ﬂow into SQL statements exposing or changing the sys-
tem’s data.
A large body of work in the literature addresses SQLi vul-
nerabilities, e.g., [14, 21, 25, 26, 28, 33]. Some approaches
perform vulnerability analysis, such as taint analysis [33,
35], to detect input ﬁelds that are not properly sanitised.
Such approaches link to speciﬁc languages and suﬀer from
high false positive rates and the dynamic typing and variable
naming of the languages [9]. These white-box approaches
often require access and may need to modify source code,
which might not always be feasible when companies out-
source the development of their systems or acquire third-
party components. Other approaches are black-box [1, 19]
but bounded to known attack patterns that tend to become
out-dated very quickly as the web evolves.
In this paper we propose a black-box automated test-
ing approach targeting SQLi vulnerabilities, calledµ4SQLi.
Starting from “legal” initial test cases, our approach applies
a set of mutation operators that are speciﬁcally designed
to increase the likelihood of generating successful SQLi at-
tacks. More speciﬁcally, new attack patterns are likely to
1Data reported by http://www.programmableweb.com, ac-
cessed January 11 nd 2014.
2https://www.owasp.org
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for proﬁt or commercial advantage and that copies bear this notice and the full citation
on the ﬁrst page. Copyrights for components of this work owned by others than ACM
must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior speciﬁc permission and/or a
fee. Request permissions from Permissions@acm.org.
ISSTA’14, July 21–25, 2014, San Jose, CA, USA
Copyright 2014 ACM 978-1-4503-2645-2/14/07...$15.00
http://dx.doi.org/10.1145/2610384.2610403
259

<!-- Page 2 -->

be generated by applying multiple mutation operators on
the same input. Moreover, some of our mutation operators
are designed to obfuscate the injected SQL code fragments
to bypass security ﬁlters, such as web application ﬁrewalls
(WAF), while others aim to repair SQL syntax errors that
might be caused by previous mutations. As a result, our ap-
proach can generate test inputs that produce syntactically
correct and executable SQL statements that can reveal SQL
vulnerabilities, if they exist. By producing SQLi attacks
that bypass the ﬁrewall and result in executable SQL state-
ments we ensure to ﬁnd exploitable vulnerabilities as op-
posed to vulnerabilities that can not be exploited, for exam-
ple because a ﬁlter blocks all attacks. In addition, concrete
sample attacks produced by our approach can help develop-
ers to ﬁx the source code or the security ﬁlter’s conﬁgura-
tion. Our approach is fully automated and supported by a
tool called Xavier 3.
We have evaluated our approach on some open-source sys-
tems that expose web service interfaces. Compared to a
baseline approach, called Std, which consists of an up-to-
date set of 137 known SQLi attack patterns, our approach
is faster and is signiﬁcantly more likely to detect vulnera-
bilities within a limited time budget. Moreover, when the
subject systems are protected by a WAF, none of the in-
puts generated by Std that reveal vulnerabilities can get
through the ﬁrewall, while our approach can still generate
a good amount of inputs, getting through the ﬁrewall and
revealing all-but-one known vulnerabilities.
The remainder of this paper is organised as follows: Sec-
tion 2 provides a background on SQLi vulnerabilities and
reviews related work. Section 3 presents our proposed mu-
tation operators and security testing approach and tool. Sec-
tion 4 presents the evaluation together with a discussion of
results and threats to validity. Finally, Section 5 concludes
the work.
2. BACKGROUND AND RELA TED WORK
This section provides a brief background on web services
and SQLi vulnerabilities and reviews previous work on SQLi
testing.
2.1 Background
In systems that use databases, such as web-based sys-
tems, the SQL statements that are used to access the back-
end database are usually treated by the native application
code as strings. These strings are formed by concatenating
diﬀerent string fragments based on user choices or the ap-
plication’s control ﬂow. Once a SQL statement is formed,
special functions are used to send the SQL statement to the
database server to be executed. For example, a SQL state-
ment is formed as follows (a simpliﬁed example from one of
our web services in the case study):
$sql = "Select * From hotelList where country =’";
$sql = $sql . $country;
$sql = $sql . ’"’;
$result = mysql_query($sql) or die(mysql_error());
The variable $country is an input provided by the user,
which is concatenated with the rest of the SQL statement
and then stored in the string variable $sql. The string is
3Contact us for download
then passed to the function mysql query that sends the SQL
statement to the database server to be executed.
SQLi is an attack technique in which attackers inject mali-
cious SQL code fragments into these input parameters. Such
attacks are possible when input parameters are used directly
in SQL statements without proper validation or sanitisa-
tion. An attacker might construct input values in a way that
changes the behaviour of the resulting SQL statement en-
abling the attacker to perform actions on the database that
were not intended by the application’s developer. These ac-
tions could lead to exposure of sensitive data, insertion or
alteration of data without authorisation, loss of data, or even
taking control of the database server.
In the previous example, if the input $country has the
value ’ or 1=1 -- , the resulting SQL statement would be:
Select * From hotelList where country=’’ or 1=1 --’
The ﬁrst quote closes the existing quote in the statement
and the double dash at the end comments out the ﬁnal quote,
making the resulting SQL statement syntactically valid. The
clause or 1=1 is a tautology, i.e. the condition will always
be true, bypassing the original condition in the where clause
and returning all rows in the table.
To avoid such attacks, application developers use ﬁlters
and sanitisation techniques to prevent malicious inputs from
aﬀecting the application’s behaviour. Developers have to be
careful not to block valid inputs that might resemble mali-
cious inputs. For example, a ﬁlter that rejects inputs with
single quotes would protect from the attack in the previous
example. However, the ﬁlter will also reject valid inputs in
which single quotes take part (e.g., O’Brian).
Web services, the basic blocks for the service-oriented ar-
chitecture, provide facilities for the easy access and exchange
of information across the Web. Each web service provides
a set of operations that can be invoked by clients. An op-
eration is similar to a method in traditional programming
languages, it has a set of input parameters and returns a
structured output. The interface and features of a web ser-
vice are typically described by a publicly available Web Ser-
vices Description Language (WSDL) ﬁle.
In this paper we consider SQLi vulnerabilities of the in-
put parameters of a service under test: an input parameter
is vulnerable to SQLi attacks if it is used in any SQL state-
ment of the implementation of a service and if, through this
parameter, an attacker can send malicious inputs that can
change the intended logic of the SQL statement. To exploit
such vulnerabilities, the attacker has to provide inputs that
result in executable SQL statements. Otherwise, the result-
ing statements are rejected by the database, thus no access
or changes to the data are possible.
2.2 Related Work
Previous research on SQLi detection used both white-box
and black-box approaches to detect vulnerabilities. Several
white-box approaches used taint analysis to identify inval-
idated inputs that ﬂow into SQL statements [21, 26, 28,
33]. Fu and Qian [14] suggested using symbolic execution to
identify the constraints that need to be satisﬁed to lead to a
SQLi attack. Shar et al. [25] used data mining of the source
code to predict vulnerabilities. As well as requiring access
to the source code, which as we mentioned before might not
always be possible, most of these approaches rely, in some
260

<!-- Page 3 -->

aspects of their algorithms, on a set of known vulnerability
patterns.
Existing black-box approaches also rely on known injec-
tion patterns when generating test cases. Ciampa et al. [7]
proposed an approach that analyses the output, including
error messages, of both legal and malicious test cases to
learn more about the type and structure of the back-end
database. This information is then used to craft attack in-
puts that are more likely to be successful at revealing vul-
nerabilities. Antunes et al. [1, 2] also analysed the diﬀerence
in the behaviour of an application when using malicious and
legal inputs to detect vulnerabilities. Huang et al. [19] used
a test generation approach that uses known attack patterns.
Known SQLi patterns have been enumerated and dis-
cussed by various academic [1, 2, 15] and online security
sources [30, 29]. However, relying on these patterns might
not be suﬃcient to test an application as attackers are always
ﬁnding new techniques to exploit vulnerabilities. Moreover,
there might be a large number of diﬀerent representations
for the same pattern, for example, using diﬀerent encodings.
Some approaches proposed run-time prevention techniques
rather than testing techniques. In the majority of these ap-
proaches [16, 17, 22, 27, 34], static analysis is used to collect
all possible forms of SQL statements that can be produced
by the program. At run-time, if the structure of a SQL
statement does not match any of those collected forms, the
statement is ﬂagged as a potential attack. Sekar [23] com-
bined taint analysis and policies to detect injection attacks
at run-time. Run-time prevention approaches are comple-
mentary to testing approaches and can also be used as an
eﬀective oracle for testing [3].
In our previous paper [3], we found that using run-time
prevention techniques as an oracle improved the detection
rates for SQLi testing. We also identiﬁed the need for a
more sophisticated oracle that could reason about the ex-
ploitability of a discovered vulnerability. In this paper, we
try to address this issue by enhancing the oracle to evaluate
the executability of a formed attack. A malicious input can
successfully evade all security mechanisms but the resulting
attack could produce a SQL statement that is not executable
and, therefore, provides no evidence that the vulnerability
is exploitable.
Mutation testing has been proposed and studied exten-
sively [20] as a method of evaluating the adequacy of test
suites where the program under test is mutated to simulate
faults. Shahriar and Zulkernine [24] deﬁned SQLi speciﬁc
mutation operators to evaluate the eﬀectiveness of a test
suite in ﬁnding SQLi vulnerabilities. Mutation analysis was
also used by Fonseca et al. [12] to compare the eﬀectiveness
of commercial security testing tools. The mutation opera-
tors we propose in this paper mutate test inputs to increase
the likelihood of triggering vulnerabilities rather than the
program under test to evaluate the eﬀectiveness of test suites
in ﬁnding faults.
Holler et al. [18] proposed an approach called LangFuzz
to test interpreters for security vulnerabilities, such as mem-
ory safety issues, by mutating the input code. The approach
has been applied successfully to uncover defects in Mozilla
JavaScript and PHP interpreter. However, our approach dif-
fers in various aspects: (1) We target SQL injection vulner-
abilities that require diﬀerent mutation operators and test
generation techniques; (2) The observability of failures in the
case of SQL vulnerabilities is much more challenging than
looking for crashes. We need to intercept communication
between a SUT and its database to analyse SQL statements
for executability and vulnerability detection.
3. APPROACH
We propose an automated technique, namely µ4SQLi,
for detecting SQLi vulnerabilities. Our technique rests on
a set of mutation operators that manipulate inputs (legiti-
mate ones) to create new test inputs to trigger SQLi attacks.
Moreover, these operators can be combined in diﬀerent ways
and multiple operators can be applied to the same input.
This makes it possible to generate inputs that contain new
attack patterns, thus increasing the likelihood of detecting
vulnerabilities.
Speciﬁcally, we want to generate test inputs that can by-
pass web application ﬁrewalls and result in executable SQL
statements. A WAF may block SQLi attacks and prevent
a vulnerable web service from being exploited. Therefore,
eﬀective test inputs need to get through the WAF in order
to reach the service. Furthermore, they should lead to exe-
cutable SQL statements as otherwise, security problems are
unlikely to arise since the database engine will reject them
and consequently no data would be leaked or compromised.
This section introduces our proposed mutation operators
to generate test data. For each mutation operator, along
with its deﬁnition, a concrete example is provided. In some
operators we discuss also their preconditions with respect to
input and previously applied operators. We will then discuss
our test generation technique and the automated tool we
developed to support the technique.
3.1 Mutation Operators
Mutation operators (MO) can be classiﬁed by their pur-
pose into the following three classes: Behaviour-changing,
syntax-repairing and obfuscation. Table 1 provides a sum-
mary of all mutation operators.
Table 1: Summary of mutation operators classiﬁed
into behaviour-changing, syntax-repairing, and ob-
fuscation operators.
MO name Description
Behaviour-Changing Operators
MO or Adds an OR-clause to the input
MO and Adds an AND-clause to the input
MO semi Adds a semicolon followed by an additional
SQL statement
Syntax-Repairing Operators
MO par Appends a parenthesis to a valid input
MO cmt Adds a comment command (-- or #) to an in-
put
MO qot Adds a single or double quote to an input
Obfuscation Operators
MO wsp Changes the encoding of whitespaces
MO chr Changes the encoding of a character literal en-
closed in quotes
MO html Changes the encoding of an input to HTML
entity encoding
MO per Changes the encoding of an input to percent-
age encoding
MO bool Rewrites a boolean expression while preserving
it’s truth value
MO keyw Obfuscates SQL keywords by randomising the
capitalisation and inserting comments
261

<!-- Page 4 -->

3.1.1 Behaviour-Changing
This class of mutation operators mutates inputs with the
aim of changing the application’s expected behaviour if the
application is vulnerable to SQLi. For example, a mutated
input could cause the application to return more database
rows than expected, exposing sensitive data to an unau-
thorised user. We deﬁne the following behaviour-changing
operators:
Operator: MO or
Adds OR x=x to the WHERE clause of a SQL state-
ment where x is a random number or a character
enclosed in single or double quotes.
Example: from original input: 1; MO or produces a mu-
tated input: 1 OR 1=1 . As a result, if the SQL statement
that takes the input is predeﬁned as ” SELECT * FROM ta-
ble WHERE id=” + input , the input will change the logic
of the statement and turns it as follows: SELECT * FROM
table WHERE id=1 OR 1=1 . This resulting statement will
return all the data of table.
Operator: MO and
Adds AND x=y to the WHERE clause of a SQL
statement where x and y are random numbers or
single characters enclosed in single or double quotes
and x is not equal to y.
Preconditions:
MO or has not been applied.
Example: original input: 1, mutated input: 1 AND 1=2 .
That will turn, for example, a predeﬁned statement: ” SE-
LECT * FROM table WHERE id=” + input to: SELECT
* FROM table WHERE id=1 AND 1=2 , thus, negating the
logic of the original statement.
Operator: MO semi
Adds a semicolon (;) followed by an additional SQL
statement to the input. The resulting query has the
form sql stmt1; sql stmt2, where sql stmt1 is the orig-
inal SQL statement and sql stmt2 is a randomly cho-
sen SQL statement from a predeﬁned list.
Example: original input: 1, mutated input: 1; SELECT
waitfor(5) FROM dual . This changes the predeﬁned state-
ment: ” SELECT * FROM users WHERE id=” + input
to: SELECT * FROM users WHERE id=1; SELECT wait-
for(5) FROM dual .
3.1.2 Syntax-Repairing
As mentioned before, a SQLi attack aims to change the
behaviour of the application by injecting malicious inputs.
Therefore, the malicious input itself is expected to contain
SQL statement fragments. This type of input, unlike regu-
lar valid inputs, could cause a SQL syntax error when being
combined with its targets, i.e., predeﬁned SQL statements.
Since the approach we propose is a black-box technique, the
predeﬁned SQL statement syntax is unknown to the test
generator making it challenging to generate inputs that do
not cause syntax errors. This class of mutation operators
mutates inputs with the goal of trying to repair SQL syn-
tax errors when they might be encountered. The mutation
operators we deﬁne in this class are the following:
Operator: MO par
Appends a closing parenthesis to the end of an input.
Preconditions:
A behaviour-changing mutation operator has been
previously applied.
Example: original input: 67, mutated input: 67). When
the input is further mutated with MO or and MO cmt,
the obtained mutated input will be: 67) OR 1=1 - {}-. Let
us consider a predeﬁned statement: ” SELECT * FROM ta-
ble WHERE character=CHR(” + input + ” )” , where func-
tion CHR converts an integer to its corresponding Unicode
character. The changed SQL statement: SELECT * FROM
table WHERE character=CHR(67) OR 1=1 – ) .
Operator: MO cmt
Adds a SQL comment command (double dashes --
and the hash character #) to the input. Any SQL
that follows a comment command is not executed.
Preconditions:
Another operator, such as MO par, has been previ-
ously applied and caused a syntax error.
Example: original input: 67, after being mutated with
MO or and MO par: 67) OR 1=1 . This changes the pre-
deﬁned statement: ” SELECT * FROM table WHERE char-
acter=CHR(” + input + ” )”to a combined statement, which
causes a syntax error: SELECT * FROM table WHERE
character=CHR(67) OR 1=1) .
We then apply MO cmt to obtain: 67) OR 1=1 # . The
ﬁnal statement: SELECT * FROM table WHERE charac-
ter=CHR(67) OR 1=1 #) Applying this mutation causes
the last parenthesis to be ignored by the parser, thereby
avoiding parser error due to the unbalanced number of paren-
theses.
Operator: MO qot
Adds either a single quote (’) or a double quote (”)
to the mutant.
Preconditions:
A behaviour-changing mutation operator, which con-
tains a character literal, has been previously applied.
Example: original input: Smith, mutated with MO or:
Smith OR 1=1 . This changes the predeﬁned statement:
” SELECT * FROM table WHERE name=’” + input + ” ’”
to combined statement, which does not result in the desired
change of behavior, since the mutant is treated as a string
literal: SELECT * FROM table WHERE name=’Smith OR
1=1’). After being further mutated with MO qot
and MO cmt: Smith’ OR 1=1 # , the ﬁnal statement is
SELECT * FROM table WHERE name=’Smith’ OR 1=1
#), which is syntactically correct and changes the logic of
the original statement.
3.1.3 Obfuscation
Some applications employ input ﬁlters, e.g., a web appli-
cation ﬁrewall, to defend against SQLi attacks. In essence,
a WAF examines every input to check for suspicious string
patterns typically used in SQLi attacks, such as SQL key-
words, and blocks them. For example, a WAF uses a black-
list that deﬁnes forbidden characters or strings to decide if
an input is suspicious. In practice, many security-critical
systems are protected by such ﬁlters. For example, a soft-
ware system, which handles credit card data, has to employ
262

<!-- Page 5 -->

a WAF to prevent attacks and to be compliant with indus-
try security standards. Obfuscation mutation operators try
to avoid ﬁltering by mutating an input to a semantically
equivalent input but in a diﬀerent form. This might prevent
the ﬁlter from recognising the forbidden characters/strings
in the mutated input. We deﬁne the following obfuscation
mutation operators:
Operator: MO wsp
Replaces a whitespace with a semantically equivalent
character (+, /**/, or unicode encodings: %20, %09,
%0a, %0b, %0c, %0d and %a0).
Preconditions:
The input contains at least one whitespace.
Example: original input: 1 OR 1=1 , mutated input: 1+-
OR+1=1. This changes the predeﬁned statement: ” SE-
LECT * FROM table WHERE id=” + input to SELECT
* FROM table WHERE id=1+OR+1=1 .
Operator: MO chr
Replaces a character literal enclosed in quotes ( ’c’)
with an equivalent representation, where c is an ar-
bitrary printable ASCII character. Equivalent repre-
sentations are:
• Short binary representation, for example, ’a’ is
replaced with b’1100001’.
• Long binary representation, for example, ’a’ is
replaced with binary’1100001’.
• Unicode representation, for example, ’a’ is re-
placed with n ’a’.
• Hexadecimal representation, for example, ’a’ is
replaced with x’61’.
Preconditions:
A behaviour-changing mutation operator, which con-
tains a character literal, has been previously applied.
Example: original input: 1, mutated with MO or: 1 OR
’a’=’a’, further mutated with MO chr: 1 OR ’a’=x’61’ .
This changes the predeﬁned statement: ” SELECT * FROM
table WHERE id=” + input to: SELECT * FROM table
WHERE id=1 OR ’a’=x’61’ .
Operator: MO html
Changes the encoding of a mutant using HTML en-
tity encoding. In HTML entity encoding, a character
can be encoded in two ways: (i) numeric character
reference in the form &#N where N is the charac-
ter’s code position in the used character set in deci-
mal or hexadecimal representation; (ii) Character en-
tity reference [32] in the form &SymbolicName. For
example, &quot; is the encoding for the single quote
character (’).
Preconditions:
For character entity reference encoding, only charac-
ters with symbolic names can be encoded.
Example: original input: 1, mutated with MO or: 1 OR
’a’=’a’, further mutated with MO html: 1 OR &quot;-
a&quot; = &quot;a&quot; . This turns the predeﬁned state-
ment: ” SELECT * FROM table WHERE id=” + input to:
SELECT * FROM table WHERE id=1 OR &quot;a&quot;
= &quot;a&quot; .
Operator: MO per
Changes the encoding of a mutant using percent en-
coding:%HH, where HH is a two digit hexadecimal
value referring to the character’s ASCII code. For
example, the single quote character (’) is encoded as
%27.
Example: original input: 1, mutated with MO or: 1 OR
’a’=’a’, further mutated with MO per: 1 OR%20’a’=’a’ .
This turns the predeﬁned statement: ” SELECT * FROM
table WHERE id=” + input to SELECT * FROM table
WHERE id=1
OR%20’a’=’a’.
Operator: MO bool
Replaces a boolean expression with an equivalent
boolean expression. For example, the boolean ex-
pression 1=1 which is used in MO or could be ob-
fuscated as not false=!!1 . Both expressions evaluate
to true, which maintains the same semantic meaning
of the mutant after obfuscation.
Preconditions:
Can only be applied to input values that contain a
boolean expression.
Example: original input: 1, mutated with MO or: 1 OR
1=1, further mutated with MO bool: 1 OR not false=!!1 .
This turns the predeﬁned statement ” SELECT * FROM
table WHERE id=” + input to: SELECT * FROM table
WHERE id=1 OR not false=!!1 .
Operator: MO keyw
Obfuscates SQL keywords and operators using dif-
ferent techniques: Randomly changing the case of
some letters, adding comments in the middle of a
keyword or replacing a keyword with an alternative
representation. Most SQL parsers are case insensi-
tive, e.g. the keyword select, SELECT or SeLeCt
are all valid. Some parsers accept keywords which
contain a comment in the middle of the keyword
(e.g. sel/*comment here*/ect ). Finally, some key-
words have alternative forms, e.g. OR can also be
expressed as||.
Preconditions:
The input value contains at least one SQL keyword.
Example: original input: 1, mutated with MO or: 1 OR
1=1, further mutation with MO keyw: 1 || 1=1. This
changes the predeﬁned statement: ” SELECT * FROM table
WHERE id=” + input to: SELECT * FROM table WHERE
id=1|| 1=1.
3.2 Test Generation
A single or multiple mutation operators of diﬀerent types
can be applied to a single input parameter to generate de-
sired inputs. The latter case aims at detecting subtle vulner-
abilities that can only be triggered with an input generated
by combining multiple mutation operators. For example,
consider an application that ﬁlters inputs by searching for
known attack patterns that can be generated using one of the
behaviour-changing operators. To form a successful attack,
it is necessary to ﬁrst apply a behaviour-changing operator
and then apply one or more obfuscation operators.
Each chain of mutations has to start from a valid test case,
which satisﬁes the input validations of the application under
263

<!-- Page 6 -->

test. Starting from a valid test case ensures that we avoid
generating test cases that would be directly rejected by the
application due to dependencies between inputs or complex
input structures that are unlikely to be generated randomly.
Moreover, valid test cases have the beneﬁt of being more
likely to satisfy input validations and reach critical parts
of the application, such as SQL queries. For example, if an
application expects a credit card number together with other
inputs, which we wish to mutate, the credit card number
has to follow a well-deﬁned format; otherwise the test case
would be instantly rejected. With the presented approach,
valid test cases from existing functional test suites can be
reused or, if such test suites do not exist, valid test cases
can be manually created using SoapUI 4 and similar tools.
Algorithm 1 formally deﬁnes the test generation algo-
rithm: Starting from a valid test case, each input is mu-
tated a predeﬁned number of times. The function Apply MO
(Line 4) randomly applies one or more mutation operator(s)
to the current Input. The function uses a simple grammar
that deﬁnes the diﬀerent legal ways to combine operators
and ensures that all preconditions for the applied operators
are satisﬁed. The operation under test is then called with
the updated test case TC′. If the oracle ﬂags a vulnerabil-
ity, all SQL statements that were issued as a result of the
call are checked. If the percentage of executable SQL state-
ments (i.e., statements that do not contain a syntax error)
is above a predeﬁned threshold P , the input is reported as
vulnerable and the test case is saved to help the test en-
gineer in debugging and ﬁxing the vulnerability (Line 5-8).
In our experiments we choose P = 100%, meaning that all
triggered SQL statements must be executable.
Algorithm 1 Test Generation Algorithm:
Input TC: A test case: ArrayOf( Input)
OP: A web service operation to be tested
Output TS: Test Suite for SQLi vulnerabilities
V: Set of vulnerable inputs
1: TS =∅
2: for each Input in TC do
3: while max tries not reached do
4: TC′ = apply MO(TC,Input)
5: if call(OP,TC′) = VulnrFlagged then
6: if executable SQL≥ P then
7: V = V ∪ Input
8: TS = TS∪ TC′
9: end if
10: end if
11: end while
12: end for
13: return TS, V
Figure 1 shows an example of a SOAP message (a test
case) generated by our approach. Here the input values of
the parameters minPrice, maxPrice, and start are kept from
the original test case, while the input value of the parameter
country has been mutated to contain a SQLi attack.
3.3 Test Oracle
When a malicious input is sent to a target system, it may
result in making the system misbehave if successful. In most
cases, the manifestation of abnormal behaviours can be ob-
4http://www.soapui.org
<soapenv:Envelope>
<soapenv:Header/>
<soapenv:Body>
<urn:getRoomsByRate>
<minPrice xsi:type="xsd:float">100</minPrice>
<maxPrice xsi:type="xsd:float">400</maxPrice>
<country xsi:type="xsd:string">"||not 0--</country>
<start xsi:type="xsd:integer">1</start>
</urn:getRoomsByRate>
</soapenv:Body>
</soapenv:Envelope>
Figure 1: Example of a generated test case, the pa-
rameter country contains a mutated SQLi attack.
served from the results the target system returns (e.g., web
pages showing unintended content) or from the surrounding
environment (e.g., crashes, illegal calls to the operating sys-
tem, or unintended accesses to data). In our experiments,
because we focus on SQL injections, we deploy a database
proxy that intercepts the communication between the target
system and its database, to identify if an input is potentially
harmful or not. For example, we can use GreenSQL 5 for
this purpose. A previous study that compared GreenSQL
to ﬁve similar tools has found it to be the most eﬀective in
detecting SQL injection attacks [11].
Details of using a database proxy as oracle has been dis-
cussed in our previous work [3]. Typically, a database proxy
is deployed and trained with normal database accesses. Such
training data are the results of regular usage of the systems
or the execution of existing functional test suites. Based on
the training data, the proxy learns regular patterns of legal
SQL statements. Once trained, the proxy will continue ob-
serving the traﬃc between the system and its database and
raise alarms when identifying suspicious database queries.
Each alarm corresponds to one database SQL statement,
and one test case can result in multiple SQL statements and
thus multiple alarms. To avoid false positives due to incom-
plete training, manual inspection may be needed to verify
that all SQL statements ﬂagged actually point to a vulner-
ability in the system.
3.4 Tool
The presented mutation approach has been implemented
as a Java tool, called Xavier6. It can be used to test SOAP-
based web services for SQLi vulnerabilities. Figure 2 shows
the key components of the tool ( Test generator and Moni-
tor) and how it is used in practice. The test generator takes
as inputs the WSDL ﬁle of the web service under test and a
sample test case for each web service operation that has to
be tested. Such a sample test case can be easily generated by
professional tools, such as SoapUI, or by existing approaches
[5]. The tool, then, examines the sample test case to ﬁnd all
input parameters for an operation and replaces each param-
eter, one at a time, with a SQLi attack generated with our
mutation approach. The modiﬁed test case will be sent to
the web service under test (the SUT in the ﬁgure). In some
settings, there could be a web application ﬁrewall (the WAF
component) deployed in between the test generator and the
SUT. The oracle component (the DB proxy component in
the ﬁgure) observes the interactions between the SUT and
its database to detect malicious SQL statements. Finally,
the Monitor component of Xavier constantly queries the or-
5http://www.greensql.com
6Contact us for download
264

<!-- Page 7 -->

acle component to know whether generated inputs reveal a
SQLi vulnerability.
In Xavier, we integrate GreenSQL to intercept SQL state-
ments. The database proxy uses a learning approach to de-
tect SQLi vulnerabilities. Therefore, it has to be trained in
a learning phase to recognise legal SQL statements. In the
detection phase, the proxy considers all intercepted state-
ments, which have not been learned previously, as SQLi at-
tacks.
WAF SUT
Monitor
Data
base
Test
generator
XAVIER
DB
ProxyWSDL
Input
samples
Monitor
test reports
Figure 2: Components of Xavier and how Xavier is
used in practice.
Every suspected malicious statement is further analysed if
it forms syntactically correct SQL. An attacker is only able
to exploit a SQLi vulnerability, if he can inject the malicious
input in such a way that the resulting SQL statement is
free of syntax errors. Otherwise, the attacker is unable to
reach his goal, e.g., to obtain/modify data or change the
application’s control ﬂow, if the malicious statement is not
executed. The tool MySQL-Proxy 7 is used to monitor if a
SQL statement has been executed or if there was an error
during execution.
4. EXPERIMENTS AND RESULTS
We have evaluated the eﬀectiveness of our approach on
two open source systems and in two diﬀerent settings: with
and without the presence of a web application ﬁrewall (WAF).
The main motivation for the latter is that, in most contexts,
including those of our industry partners, such a ﬁrewall is
typically present (or sometimes integrated) and is the ﬁrst
protection layer encountered by attackers. Such situations
are therefore deemed more realistic. The ﬁrewall deployed
in our experiment is ModSecurity with the OWASP Core
Rule Set (version 2.2.0). As the baseline for our evaluation,
we considered a comprehensive list of known SQLi attack
patterns since, in practice, this is what penetration testers
typically use.
We aim at evaluating the performance of our proposed
mutation technique in comparison with standard attacks.
More speciﬁcally, we investigate the following research ques-
tions:
RQ1: Are standard attacks and mutated inputs (generated
byµ4SQLi) likely to reveal exploitable SQLi vulnerabilities?
RQ2: With and without the presence of the WAF, which
input generation technique performs better?
4.1 Subject Applications
Two open-source subjects, namely HotelRS and Sugar-
CRM were used in our experiments. HotelRS was created
by researchers to study service-oriented architectures and
was used in previous studies [8]. SugarCRM is a popular
customer relationship management system (received 189K+
7http://dev.mysql.com/doc/refman/5.1/en/mysql-
proxy.html
downloads as of 2013 8). These systems provide web service
APIs to the external world. Such interfaces allow other sys-
tems, namely service consumers, to access to the business
functionality and data of the subject systems. However,
they are also target for SQLi attacks if the inputs through
those interfaces are inadequately treated.
Table 2: Size in terms of web service operations,
parameters, and lines of code of the subject appli-
cations.
Application #Operations #Parameters #LoC
HotelRS 7 21 1,566
SugarCRM 26 87 352,026
Total 33 108 353,592
Table 2 provides information about the number of oper-
ations, input parameters and lines of code for the chosen
applications. In terms of size in number of lines of code,
HotelRS and SugarCRM, with 1.5KLoCs and 352KLoCs
respectively, are not particularly large but they provide a re-
spectable number of services with many input parameters,
with known vulnerabilities. SugarCRM and HotelRS are
both implemented using PHP, use a MySQL database, and
provide a SOAP-based Web Service API. Those are popu-
lar technologies used in the implementation of many web
services.
For each subject we manually create a test suite for its
web services using SoapUI: one test case for each operation.
In total, we have created 33 initial test cases for the two
subjects in our experiments.
4.2 Treatments
We refer to the baseline approach consisting of 137 known
attack patterns as Std (Standard attacks). Such patterns
were consolidated in a repository of SQLi attack patterns [1].
They include diﬀerent contemporary categories of attacks,
such as Boolean-based, UNION query-based. In a previous
study [3] we compared Std to SqlMap, a state-of-the-art
penetration testing tool, and found Std to be more eﬀective
in ﬁnding vulnerabilities. In the context of our study, the
whole set of attack patterns of Std is applied for every indi-
vidual input parameter. The second treatment used in our
study is our approach, µ4SQLi.
4.3 Variables
Given a set of test cases targeting a speciﬁc web service
parameter, we deﬁneT as the total number of test cases that
generate SQL statements that are ﬂagged by the database
proxy. Among these tests, we further investigate if their gen-
erated SQL statements are executable or not. We refer to
Te for the total number of tests that can lead to ﬂagged and
executable SQL statements. To compare Std andµ4SQLi,
we need to consider both T andTe, as we will see that look-
ing atT alone would lead to very diﬀerent conclusions since
only executable SQL statements can be exploitable. Non-
executable statements can be generated because the corre-
sponding inputs, after being processed by a target, produce
in syntax-error SQL statements. They hardly have a secu-
rity impact since the database engine would reject them and,
hence, no data would be leaked or compromised.
If a technique yields higherTe, it is considered to be more
eﬀective at detecting exploitable vulnerabilities. In other
8http://sourceforge.net
265

<!-- Page 8 -->

words, whenTe is high, it is more likely to detect exploitable
vulnerabilities for a test suite of ﬁxed size. Moreover, it
is also likely to detect vulnerabilities faster, i.e., we need a
smaller number of tests to be executed in order to detect the
vulnerabilities. This, in practice, is important when dealing
with a large number of services and input parameters.
Since one test case can give rise to multiple SQL state-
ments, we need to determine how to computeTe when there
is a mix of executable and non-executable statements. Since,
in practice, one single ﬂagged and executable statement gen-
erated by a speciﬁc input can entail serious consequences,
when more SQL statements are executable, the chance to
uncover vulnerabilities is higher. In our analysis, with the
intent of being conservative in our results, a test t is consid-
ered to be part of Te if and only if all the ﬂagged statements
generated by t are executable.
4.4 Results
We ran µ4SQLi and Std on every parameter of the two
selected subjects, SugarCRM and HotelRS. There are
in total 108 input parameters for all their web services.
As described earlier, Std entails 137 test executions for
every parameter, whereas with µ4SQLi, since it is non-
deterministic, we need to run more test executions to ac-
count for randomness. To do so in an eﬃcient way, given
the substantial execution time (about 5.7 hours per vulnera-
ble parameter on a virtual machine of 1Gb RAM and 2,6Ghz
CPU) we generated and ran 1000 tests for each parameter.
We, then, adopted a Bootstrapping approach (sampling with
replacement) [10] and formed 10k test suites (each has 137
tests) by sampling from these 1000 tests, so that each test
suite would be comparable to Std with respect to Te. In
the tables 3 and 4, we report the percentage of T and Te
for Std on each subject and their average percentage for
µ4SQLi over 10k test suites. We only report results for
vulnerable input parameters of the two test techniques and
after being conﬁrmed through manual inspection.
Table 3: Results of Std and µ4SQLi on the subject
applications when no WAF is enabled.
Subject Parameter Std µ4SQLi
%T %Te %T %Te
(avg) (avg)
HotelRS country 12.41 5.84 40.62 21.80
arrDate 35.04 9.49 42.05 12.50
depDate 35.04 9.49 42.96 12.03
name 35.04 9.49 43.36 12.91
address 35.04 9.49 39.81 11.00
email 35.04 9.49 41.73 11.24
SugarCRM value 37.23 0.0 41.48 22.51
ass user id 32.85 8.03 42.49 13.91
query1 32.85 3.65 9.82 0.30
query2 54.74 5.84 81.72 33.45
order by 59.85 10.95 85.98 33.55
rel mod qry 47.45 2.92 49.79 0.00
Table 3 shows our results when the subjects were not pro-
tected by the WAF. The ﬁrst and second column indicate
the subjects and their vulnerable parameters, the subse-
quent columns show the percentage of tests that generate
ﬂagged SQL statements (% T ) and the percentage of such
ﬂagged tests (out of 137) that also lead to executable SQL
statements (%Te). For µ4SQLi, as indicated, such percent-
ages are averages over 10k test suites. For HotelRS, both
techniques ﬁnd six SQLi vulnerabilities. With regards to
the parameter country, 12.41% of 137 test cases provided by
Std are ﬂagged by GreenSQL as SQLi attacks and, among
them, 5.84% generate executable SQL statements. Results
for the remaining ﬁve parameters found to be vulnerable by
Std are identical: 35.04% of the tests lead to SQL state-
ments being ﬂagged by GreenSQL and among them, 9.49%
generate executable SQL statements. While µ4SQLi and
Std detect the same vulnerabilities, %T and %Te are higher
forµ4SQLi: across the reported parameters, T ranges from
39.81% to 43.36% and Te from 11% to 21.80%. For Sug-
arCRM, both techniques detect ﬁve out of six vulnerabil-
ities, but both Std and µ4SQLi failed to generate an ex-
ecutable SQL statement for one parameter, that is value
and rel mod query, respectively. Except for the parameter
query1 µ4SQLi has always a higher T measure. Similarly,
µ4SQLi has a higher Te measure for all parameters except
for query1 and rel mod query.
Even when using µ4SQLi, %Te is generally lower than
%T across the input parameters. However, it is large enough
to be highly likely to detect an exploitable vulnerability by
running a few dozens test cases or less, as only one ﬂagged
test case leading to an executable SQL statement is enough
to demonstrate the vulnerability of a parameter. Taking
the parameter ass user id as an example, with an average
%Te of 13.91%, running 50 test cases would yield a very
small probability, 0 .0006 (i.e., (1 − 0.1391)50), of missing
the vulnerability. % T is typically much larger than % Te,
thus showing that generating executable SQL statements is
rather diﬃcult.
Table 4: Results of Std and µ4SQLi on the subject
applications protected by the WAF.
Subject Parameter Std µ4SQLi
%T %Te %T %Te
(avg) (avg)
HotelRS country 0.73 0.0 36.84 20.69
arrDate 2.19 0.0 35.91 9.11
depDate 5.84 0.0 36.59 11.42
name 6.57 0.0 38.34 11.72
address 7.30 0.0 39.67 9.64
email 6.57 0.0 36.33 9.88
SugarCRM value 2.19 0.0 37.42 20.48
ass user id 5.11 0.0 29.35 6.89
query1 0.73 0.0 8.97 0.20
query2 3.65 0.0 76.56 31.43
order by 7.30 0.0 80.08 31.96
rel mod qry 6.57 0.0 44.82 0.0
Table 4 shows the results of the experiments when the
subjects were protected by the WAF. For HotelRS, once
again, both approaches were able to generate, for each vul-
nerable parameter, SQLi statements which was ﬂagged by
GreenSQL (%T > 0). However, one important diﬀerence
is that only µ4SQLi was able to generate test cases which
lead to executable SQL statements. Std failed to do so for
all tested parameters. Similarly, for SugarCRM, %T is
signiﬁcantly higher for µ4SQLi than Std. And once again,
only µ4SQLi was able to generate test cases that led to
executable SQL statements for ﬁve out six vulnerable pa-
rameters (except rel mod qry), whereas Std failed to do so
for all tested parameters. Our conclusions are similar to the
results when no WAF is present, except that % T and %Te
tend to be lower with a WAF. This is to be expected as some
of the attacks generated are ﬁltered out by the WAF.
Regarding the performance of µ4SQLi on the parameter
266

<!-- Page 9 -->

query1, the vulnerability, though not impossible to ﬁnd, is
still extremely diﬃcult to detect (only 0.3% of test cases
can uncover it). Further work is needed to investigate the
reasons.
We further examined why µ4SQLi experienced, for pa-
rameter rel mod qry, a sharp drop from T (49.72% without
WAF) to Te (0%). µ4SQLi failed to trigger an executable
statement for this parameter since, given the SQL statement
into which the test case is injected, non of the mutation op-
erators could possibly result in a syntactically correct state-
ment. The vulnerable statement is:
SELECT opportunity id id FROM accounts opportunities
, opportunities WHERE [...] AND <test case inserted
here> AND [...]
The injection occurs in the where clause of the SQL state-
ment. MO or and MO and are the mutation operators
that target SQLi vulnerabilities in the where clause. For
both of these operators, all generated mutants for this par-
ticular SQL statement begin either with a single quote or
a double quote, e.g. ”||’d’=’d’– or ’ or 1 , but since their is
no matching opening single or double quote an syntax er-
ror is introduced. For example, once concatenated with the
mutant the statement becomes:
SELECT opportunity id id FROM accounts opportunities
, opportunities WHERE [...] AND ” ||’d’=’d’– AND [...]
This problem can be solved by improving how the muta-
tion operators append a clause. For example, in this partic-
ular case, starting the mutant with a number instead of a
quote prevents a syntax error. With this additional ﬁx, the
vulnerability will be detected. More generally, we expect
that the performance of µ4SQLi will be further improved
once we improve the mutation operators.
Answering the research question RQ1, we can see that
both techniques can, in most cases, reveal vulnerabilities
(%Te > 0) when the subjects were not protected by the
WAF. However, when they are protected, onlyµ4SQLi can
reveal such vulnerabilities (in 10 out of 12 parameters) while
Std revealed none of them. Such a diﬀerence is highly sig-
niﬁcant as it has many practical implications to be discussed
below.
To provide a better view of the comparison between the
two input generation techniques, we produced a set of plots.
All of them are available in our technical report [4]. Figures
3 and 4 depict the results when the subjects were protected
with a WAF. The box-plots depict the results of µ4SQLi
(recall it is non-deterministic) in terms of % T (lower part)
and %Te (upper part). The dash and triangle dots are the
result of Std. As we can see, without having to resort to
a statistical test, the diﬀerences are clearly signiﬁcant. In
the upper part of the ﬁgures, none of the tests generated by
Std could result in executable SQL statements and therefore
missed all the vulnerabilities. By contrast, µ4SQLi missed
only one of the vulnerabilities inSugarCRM. In short, from
the ﬁgures and above tables, we can see that the performance
of µ4SQLi in terms of generating tests that lead to ﬂagged
and executable SQL statements is signiﬁcantly better than
Std.
4.5 Discussion
Results without the WAF indicate that both approaches
can detect vulnerabilities in the examined subjects. Both
techniques were able to provide, for most vulnerable param-
eters, test cases leading to SQL statements that are ﬂagged
Figure 3: Results obtained from HotelRS with ﬁre-
wall enabled: the box-plots depict the results of
µ4SQLi, the dashed line depicts the results of Std.
None of the executable SQL statements generated
by Std can get through the WAF.
Figure 4: Results obtained from SugarCRM with
the ﬁrewall enabled.
267

<!-- Page 10 -->

by GreenSQL and deemed executable. It is interesting to
note, however, that a signiﬁcantly higher percentage of test
cases generated ﬂagged and executable statements when us-
ing µ4SQLi. The practical implications of these results is
that, since the execution time of a test case generated by ei-
ther Std orµ4SQLi is comparable, when testing many ser-
vices with many input parameters, µ4SQLi will be a more
eﬀective and less costly technique to detect exploitable vul-
nerabilities. They will be more likely to be detected within
a ﬁxed test budget and will be detected faster.
Results with the WAF are even more dramatic. Only
µ4SQLi is able, for all parameters but one, to generate
ﬂagged and executable SQL statements. Since the pres-
ence of a WAF or similar protection mechanism is a much
more realistic situation in practice, these results imply that
in many situations, standard attacks are not eﬀective when
looking for tangible evidence that there are exploitable SQLi
vulnerabilities.
When the subjects were protected by the WAF, there was
an even more contrasting diﬀerence in the results of the tech-
niques. With the WAF enabled, µ4SQLi achieved results
that are similar to when no WAF was used: T and Te ex-
perienced only a slight drop. That diﬀerence was due to
the WAF identifying and blocking only a small number of
attacks. This is an evidence that the proposed obfuscation
mutation operators are eﬀective at bypassing the WAF. On
the contrary, the test results for Std dropped considerably.
T experienced a large drop and Te went down to zero. This
can be attributed to the WAF recognising most of the test
cases as SQLi attacks and blocking them. The low percent-
age of test cases which bypass the ﬁrewall do not result in
executable SQL statements.
Overall, the results indicate that the obfuscation and syntax-
repairing have helped µ4SQLi in bypassing the WAF and
triggering executable SQLi attacks.
In the experiments withStd andµ4SQLi, both approaches
start from the same valid test cases. Thus, the comparison
is unbiased. It might be interesting to repeat our experi-
ments for a single web service with distinct test cases. Each
test case may reach diﬀerent parts of the code leading to
the generation of diverse SQL statements. Thus, we might
achieve higher coverage and increase our chances to ﬁnd a
vulnerability.
4.6 Threats to Validity
The potential threats to validity of our results fall into the
internal and external categories:
Internal threats: This is about whether the associa-
tions we observed between treatments (test techniques) and
generated executable SQL statements can be conﬁdently in-
terpreted as due to the inherent properties of the techniques.
For Std we used a comprehensive list of 137 known attack
patterns mentioned in [1]. As far as we are aware, this
is the state of practice for penetration testing. Regarding
µ4SQLi, since it is non-deterministic and to account for
randomness, we generated and ran 1000 tests per parame-
ter and then sampled (with replacement, a procedure called
Bootstrapping) 10K test suites of 137 test cases to enable
a statistical comparison with standard attacks. We have
also inspected the reports of GreenSQL to remove any false
alarms.
As used in many production systems, we chose ModSecu-
rity as a WAF and used the OWASP Core Rule Set.
External threats: This concerns the generalization of
the results. Obviously, like any study in speciﬁc systems,
it needs to be replicated. The computation cost of running
such experiments is however high and, although we only
used two systems in the experiments, them are from diﬀer-
ent domains and SugarCRM is used by real users as the
number of downloads indicates. Although we compared only
two test techniques, they are representative of the state of
the art in black-box SQLi testing, as the review of related
works indicates.
5. CONCLUSION
SQL injections have been ranked among the most common
categories of vulnerabilities. Attacks that exploit such type
of vulnerabilities increase rapidly over time. Automated
testing techniques are important, not only to detect vulner-
abilities in web services before they can be published, but
also to reduce testing eﬀort in contexts where the numbers of
services and their input parameters are large. In particular,
there is a need for black-box techniques that do not require
access to the source code, as this is a common constraint
when third party components are used or software develop-
ment is (partly) outsourced. Existing techniques that have
investigated this speciﬁc problem are bounded to known at-
tack patterns that become out-dated very quickly, especially
given the fast evolution of web services and their underpin-
ning technologies. Their performance may also be limited by
the presence of application protection mechanisms, such as
ﬁrewalls, which may block known attacks. Our results con-
ﬁrm this problem by showing that state-of-practice, stan-
dard attacks do not, in most cases, make it through the
ﬁrewall. In addition, the few that were not blocked by the
ﬁrewall lead to non-executable SQL statements because of
syntax errors.
We presented in this paper an automated mutation tech-
nique for SQL injection vulnerabilities, supported by a tool,
which focuses on mutating the input values of web service
parameters. This technique makes use of a set of mutation
operators that are able (1) to generate inputs with a high
likelihood of modifying the behaviour of services, (2) to cor-
rect inputs to remove possible syntax errors due to muta-
tions, and (3) to obfuscate attacks to increase their chances
to make it though the ﬁrewall. The ultimate goal of our
technique is to generate randomised inputs to detect SQL
vulnerabilities by the way of SQL statements that are exe-
cutable, are passing the ﬁrewall, and are unduly revealing
or compromising data in the database. Our experimental
results have demonstrated that our technique and tool per-
formed much better than state-of-practice standard attack
patterns, and that the probability of detecting SQL injection
vulnerabilities is high, even in the presence of a ﬁrewall, and
with a reasonable number of test case executions for each
input parameter in each service.
6. ACKNOWLEDGEMENTS
This work was supported by the National Research Fund,
Luxembourg (grant FNR/P10/03 and FNR4800382). We
specially thank the testing and security team of our indus-
try partner, CETREL, for their collaboration within this
project.
268

<!-- Page 11 -->

7. REFERENCES
[1] N. Antunes, N. Laranjeiro, M. Vieira, and H. Madeira.
Eﬀective detection of SQL/XPath injection vulnerabilities
in web services. In Proceedings of the 6th IEEE
International Conference on Services Computing (SCC
’09), pages 260–267, 2009.
[2] N. Antunes and M. Vieira. Detecting SQL injection
vulnerabilities in web services. In Proceedings of the 4th
Latin-American Symposium on Dependable Computing
(LADC ’09), pages 17–24, 2009.
[3] D. Appelt, N. Alshahwan, and L. Briand. Assessing the
impact of ﬁrewalls and database proxies on sql injection
testing. In Proceedings of the 1st International Workshop
on Future Internet Testing, 2013.
[4] D. Appelt, N. Alshahwan, C. D. Nguyen, and L. Briand.
Black-box sql injection testing. Technical report, University
of Luxembourg and University College London, 2014.
[5] C. Bartolini, A. Bertolino, E. Marchetti, and A. Polini.
Ws-taxi: A wsdl-based testing tool for web services. In
ICST, pages 326–335, 2009.
[6] T. Beery and N. Niv. Web application attack report, 2013.
[7] A. Ciampa, C. A. Visaggio, and M. Di Penta. A
heuristic-based approach for detecting SQL-injection
vulnerabilities in web applications. In Proceedings of the
ICSE Workshop on Software Engineering for Secure
Systems (SESS ’10) , pages 43–49, 2010.
[8] J. Coﬀey, L. White, N. Wilde, and S. Simmons. Locating
software features in a soa composite application. In Web
Services (ECOWS), 2010 IEEE 8th European Conference
on, pages 99–106, 2010.
[9] M. Cova, V. Felmetsger, and G. Vigna. Vulnerability
analysis of web-based applications. In L. Baresi and
E. Nitto, editors, Test and Analysis of Web Services , pages
363–394. Springer Berlin Heidelberg, 2007.
[10] B. Efron and R. Tibshirani. An Introduction To The
Bootstrap, volume 57. CRC press, 1993.
[11] I. A. Elia, J. Fonseca, and M. Vieira. Comparing sql
injection detection tools using attack injection: An
experimental study. In Proceedings of the IEEE 21st
International Symposium on Software Reliability
Engineering (ISSRE ’10) , pages 289–298, 2010.
[12] J. Fonseca, M. Vieira, and H. Madeira. Testing and
comparing web vulnerability scanning tools for SQL
injection and XSS attacks. In Proceedings of the 13th
Paciﬁc Rim International Symposium on Dependable
Computing (PRDC ’07) , pages 365–372, 2007.
[13] M. Fossi and E. Johnson. Symantec global internet security
threat report, volume xiv, 2009.
[14] X. Fu and K. Qian. SAFELI: SQL injection scanner using
symbolic execution. In Proceedings of the workshop on
Testing, Analysis, and Veriﬁcation of Web Services and
Applications (TAV-WEB ’08), pages 34–39, 2008.
[15] W. G. Halfond, J. Viegas, and A. Orso. A classiﬁcation of
sql-injection attacks and countermeasures. In Proceedings
of the IEEE International Symposium on Secure Software
Engineering (ISSSE ’06) , pages 13–15, 2006.
[16] W. G. J. Halfond and A. Orso. Amnesia: analysis and
monitoring for neutralizing SQL-injection attacks. In
Proceedings of the 20th IEEE/ACM International
Conference on Automated Software Engineering (ASE
’05), pages 174–183, 2005.
[17] W. G. J. Halfond and A. Orso. Preventing SQL injection
attacks using AMNESIA. In Proceedings of the 28th
International Conference on Software Engineering (ICSE’
06), pages 795–798, 2006.
[18] C. Holler, K. Herzig, and A. Zeller. Fuzzing with code
fragments. In Proceedings of the 21st Usenix Security
Symposium, 2012.
[19] Y.-W. Huang, S.-K. Huang, T.-P. Lin, and C.-H. Tsai. Web
application security assessment by fault injection and
behavior monitoring. In Proceedings of the 12th
International Conference on World Wide Web (WWW
’03), pages 148–159, 2003.
[20] Y. Jia and M. Harman. An analysis and survey of the
development of mutation testing. IEEE Transactions on
Software Engineering, 37(5):649–678, 2011.
[21] A. Kieyzun, P. J. Guo, K. Jayaraman, and M. D. Ernst.
Automatic creation of SQL injection and cross-site scripting
attacks. In Proceedings of the 31st International Conference
on Software Engineering (ICSE ’09) , pages 199–209, 2009.
[22] I. Lee, S. Jeong, S. Yeo, and J. Moon. A novel method for
SQL injection attack detection based on removing SQL
query attribute values. Mathematical and Computer
Modelling, 55(1):58–68, 2012.
[23] R. Sekar. An eﬃcient black-box technique for defeating web
application attacks. In Proceedings of the 16th Annual
Network and Distributed System Security Symposium , 2009.
[24] H. Shahriar and M. Zulkernine. MUSIC: Mutation-based
SQL injection vulnerability checking. In Proceedings of the
8th International Conference on Quality Software
(QSIC’08), pages 77–86. IEEE, 2008.
[25] L. K. Shar, H. B. K. Tan, and L. Briand. Mining sql
injection and cross site scripting vulnerabilities using hybrid
program analysis. In Software Engineering (ICSE), 2013
35th International Conference on , pages 642–651, 2013.
[26] Y. Shin. Improving the identiﬁcation of actual input
manipulation vulnerabilities. In Proceedings of the 14th
ACM SIGSOFT Symposium on Foundations of Software
Engineering, 2006.
[27] Y. Shin, L. Williams, and T. Xie. Sqlunitgen: Test case
generation for sql injection detection. North Carolina State
University, Raleigh Technical report, NCSU CSC TR , 21,
2006.
[28] B. Smith, L. Williams, and A. Austin. Idea: using system
level testing for revealing SQL injection-related error
message information leaks. In Proceedings of the 2nd
International Conference on Engineering Secure Software
and Systems (ESSoS ’10) , pages 192–200, 2010.
[29] SQL Injection Wiki. SQL injection cheat sheet.
http://www.sqlinjectionwiki.com/, 2013.
[30] The Open Web Application Security Project (OWASP).
Testing for SQL injection (owasp-dv-005).
http://www.owasp.org, 2013.
[31] M. Vieira, N. Antunes, and H. Madeira. Using web security
scanners to detect vulnerabilities in web services. In
Proceedings of the IEEE/IFIP International Conference on
Dependable Systems Networks (DSN ’09) , pages 566–571,
2009.
[32] W3C. Character entity references in HTML 4.
http://www.w3.org/TR/html4/sgml/entities.html, 2012.
[33] G. Wassermann and Z. Su. Sound and precise analysis of
web applications for injection vulnerabilities. In Proceedings
of the 28th ACM SIGPLAN Conference on Programming
Language Design and Implementation (PLDI ’07) , pages
32–41, 2007.
[34] K. Wei, M. Muthuprasanna, and S. Kothari. Preventing
SQL injection attacks in stored procedures. In Proceedings
of the Australian Software Engineering Conference
(ASWEC ’06), pages 191–198, 2006.
[35] Y. Xie and A. Aiken. Static detection of security
vulnerabilities in scripting languages. In Proceedings of the
15th Conference on USENIX Security Symposium -
Volume 15, USENIX-SS’06, Berkeley, CA, USA, 2006.
USENIX Association.
269

