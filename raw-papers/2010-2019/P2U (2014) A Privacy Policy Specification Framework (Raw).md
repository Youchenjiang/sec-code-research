---
title: "P2U: A Privacy Policy Specification Language for Secondary Data Sharing and Usage"
pages: 5
---

# P2U: A Privacy Policy Specification Language for Secondary Data Sharing and Usage

> **總頁數**：5 頁

---

## Page 1

2014 IEEE Security and Privacy Workshops 2014 IEEE Security and Privacy Workshops 2014 IEEE Security and Privacy Workshops

P2U: A Privacy Policy Specification Language for

Secondary Data Sharing and Usage

| Johnson Iyilade | Julita Vassileva |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Computer Science Department, | Computer Science Department, |  |  |  |  |  |  |  |  |
| University of Saskatchewan, 110 Science Place | University of Saskatchewan, 110 Science Place |  |  |  |  |  |  |  |  |
| S7N 5C9 Saskatoon, Canada | S7N 5C9 Saskatoon, Canada |  |  |  |  |  |  |  |  |
| Johnson.Iyilade@usask.ca | Julita.Vassileva@usask.ca |  |  |  |  |  |  |  |  |
| Abstract | — | Within | the | last | decade, | there | are | growing | providers, and society at large. For instance, reuse of existing |
| economic/social incentives and opportunities for secondary use of | user information by a new application helps the user avoid the |  |  |  |  |  |  |  |  |
| data in many sectors, and strong market forces currently drive | duplication | of | same | information | across | applications | [14]. |  |  |
| the | active | development | of | systems | that | aggregate | user | data | Moreover, allowing secondary sharing of user information |
| gathered by many sources. This secondary use of data poses | leads to increased breadth and depth in the user model, which |  |  |  |  |  |  |  |  |
| privacy threats due to unwanted use of data for the wrong | results in better personalization of services since more aspects |  |  |  |  |  |  |  |  |
| purposes such as discriminating the user for employment, loan | or features of the user are available in an aggregated user |  |  |  |  |  |  |  |  |
| and insurance. Traditional privacy policy languages such as the | model | [15][16]. | For | businesses, | the | resulting | better |  |  |

Platform for Privacy Preferences (P3P) are inadequate since they

were designed long before many of these technologies were

invented and basically focus on enabling user-awareness and

control during primary data collection (e.g. by a website).

I. INTRODUCTION

Recently, there is an exponential growth in the amount of

data about user available online. This data is shared voluntarily

by user or passively collected by applications that analyze

users’ behaviors, activities and context. For example, many

apps running on user’s mobile devices (e.g. smartphones and

tablets), store information about user’s locations, preferences

and interests. Wearable sensors, embedded in user’s glasses,

watches, shoes, and clothes gather data about the physical

world environment of the user. With the advent and growing

popularity of social networking sites and Web 2.0 applications,

users are actively connecting, sharing, and commenting on

these sites, thereby producing massive information about their

© 2014, Johnson Iyilade. Under license to IEEE. © 2014, Johnson Iyilade. Under license to IEEE. © 2014, Johnson Iyilade. Under license to IEEE.

DOI 10.1109/SPW.2014.12 DOI 10.1109/SPW.2014.12 DOI 10.1109/SPW.2014.12

personalization will lead to better targeted advertisements on

mobile devices, which is currently a big challenge for mobile

application providers [18]. Finally, the emerging opportunity to

with respect to employment, insurance and loans [17]. Hence,

from harms.

One way to achieve this balance is through a privacy policy

which allows data owners to set the permissions for a range of

allowable usages of data [2]. Currently, there exists a number

of privacy policy languages designed to enable both the user

and data providers communicate their desired privacy

protection. These include: Platform for Privacy Preferences

(P3P) [3], A P3P Preference Exchange Language (APPEL)[4],

eXtensible Access Control Markup Language (XACML) [6],

and Geographic Location / Privacy (GeoPriv) [7], Rei [20],

ExPDT [21], AIR[22], etc. Of these languages, P3P has been

the most widely used structured privacy policy language on the

Web [5].

18 18 18

| However, with the advent of Web 2.0 and Social Networking | aggregate user data from many sources (e.g. for Big Data |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sites, the landscape of privacy is shifting from limiting collection | Analytics) is driving innovation and societal benefits in many |  |  |  |  |  |  |  |  |  |  |  |  |  |
| of data by websites to ensuring ethical use of the data after initial | areas such as healthcare, national security, law enforcement, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| collection. To meet the current challenges of privacy protection in | education, and home-automation [9]. Despite these benefits, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| secondary | context, | we | propose | a | privacy | policy | language, | sharing and utilizing user data for secondary purposes pose |  |  |  |  |  |  |
| Purpose-to-Use (P2U), aimed at enforcing privacy while enabling | significant privacy risks to the user. For example, user data |  |  |  |  |  |  |  |  |  |  |  |  |  |
| secondary user information sharing across applications, devices, | could | be | used | for | potentially | harmful | purposes | such | as |  |  |  |  |  |
| and services on the Web. | surveillance or profiling the user for targeted discrimination |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Keywords | — | Privacy, | Secondary | Use, | Policy | Languages, | Usage | there is the need to balance the growing demand of secondary |  |  |  |  |  |  |
| Control | sharing for beneficial purposes with the need to protect user |  |  |  |  |  |  |  |  |  |  |  |  |  |
| interests, activities and social relationships. Furthermore, as | In its current state, we believe the P3P policy language is |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cloud | services | become | commonplace, | users | are | storing, | inadequate | in | meeting | the | privacy | challenges | of | user |
| processing and accessing a lot of their personal information | information sharing, particularly in a secondary context due to |  |  |  |  |  |  |  |  |  |  |  |  |  |
| online. Although, the information collected about user by these | its focus, underlying privacy principles, inflexibility and lack |  |  |  |  |  |  |  |  |  |  |  |  |  |
| applications | and | services | have | been | traditionally | kept | in | of formal semantics. First, it is developed with the goal of |  |  |  |  |  |  |
| disparate application silos and databases, there are growing | giving the user a tool to limit information collection by a |  |  |  |  |  |  |  |  |  |  |  |  |  |
| economic and social incentives for connecting and aggregating | website in a primary data collection context. However, with the |  |  |  |  |  |  |  |  |  |  |  |  |  |
| this data, thereby necessitating secondary sharing and use of | rise of social network and Web 2.0 technologies, users are now |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the data across systems [1]. In addition, there are numerous | active, voluntary providers of massive amounts of information |  |  |  |  |  |  |  |  |  |  |  |  |  |
| benefits | (in | terms | of | personalized | services) | of | such | about their activities online. | Therefore, the privacy challenge |  |  |  |  |  |
| “secondary” sharing of user information to the user, the service | of today is shifting from limiting the collection of user data |  |  |  |  |  |  |  |  |  |  |  |  |  |

*[Image: Page 1 Image]*

*[Image: Page 1 Image]*

*[Image: Page 1 Image]*

---

## Page 2

| towards | preventing | the | unintended | secondary | sharing | and | allowing websites to express their data collection practices to |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| usage of already collected data. Second, P3P assumes that the | the user, the companion W3C language, APPEL, allows the |  |  |  |  |  |  |  |  |  |
| site collecting the data knows all the purposes of use of data a | user to specify their privacy preferences to a website. Usually, |  |  |  |  |  |  |  |  |  |
| priori. Hence, it requires organizations to disclose the purpose | a P3P user agent then compares the P3P file against APPEL |  |  |  |  |  |  |  |  |  |
| of use of data at the point of collection and collected data can | file to discover any mismatch between the policy of a website |  |  |  |  |  |  |  |  |  |
| only | be | used | for | this | purpose. | This | assumption | fails | to | and the preferences of the user and warn the user of potential |
| acknowledge the possibility of finding new and beneficial use | privacy violation. Microsoft Internet Explorer 6 and Netscape |  |  |  |  |  |  |  |  |  |
| of data for various secondary purposes that may not even be | Navigator 7 were early adopters incorporating P3P as plugins |  |  |  |  |  |  |  |  |  |
| known when the data was collected [9]. | Finally, P3P has | to their browsers. |  |  |  |  |  |  |  |  |

remained a static language that does not allow negotiations of

the elements of the privacy policy, which will be very crucial

in emerging marketplaces for sharing and trading user data and

when dealing with users with different privacy personality

traits and preferences.

negotiable privacy policy that defines the purpose (of use), type

of data , retention period and price (of data).

last two decades, a number of policy languages have been

proposed. Examples include: the Platform for Privacy

Preferences (P3P) which was proposed by the W3C; A P3P

Preference Exchange Language (APPEL) also proposed by

W3C; eXtensible Access Control Markup Language

(XACML), Extended Privacy Definition Tool (ExPDT),

1

SecPAL4P, Rei, AIR and Geographic Location / Privacy . A

distinguishing characteristic of these languages is that they are

designed and developed to address emerging privacy

management issues in different situations and contexts [8]. For

example, the P3P became a W3C recommendation in 2002 to

the Web [5].

collection practices of Websites [3]. While P3P is targeted at

1

Although, the P3P language is still deployed in Microsoft

Internet Explorer, its adoption has remained stagnant for the

past few years. Now it only focuses on cookie-blocking

decisions [10]. Previous research and surveys have enumerated

the factors responsible for the slow adoption of P3P and some

[9]:

 Changing role of the user: P3P is premised on the role of

user as data subject that need to be protected from

organizations that collects information. With social

 New purposes of data use after initial collection: Since its

underlying design principle is the traditional “ notice and

consent ” , P3P assumes that all the purposes of use of data

is known during primary data collection and is expressed

by the organization prior to collection [9]. The assumption

that user data can only be used for pre-collection purposes

is limiting, since it fails to envisage new and potentially

very beneficial ways in which the data might be reused

after collection to support personalization of services,

offers, advertisement, etc.

across applications [12].

As the need for collaboration and secondary sharing of user

19 19 19

| In view of the above, this paper proposes | purpose-to-use | of its weaknesses, including: lack of incentives for organization |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (P2U) | , a privacy policy specification language inspired by the | to adopt it; errors in P3P files on many websites; and lack of |  |  |  |  |  |  |  |  |  |  |  |
| P3P but adapted to user information sharing in secondary | clear semantics. In addition, we believe that the P3P language, |  |  |  |  |  |  |  |  |  |  |  |  |
| context. P2U is designed to enable emerging marketplaces for | at | present | is | limited | in | facilitating | cross-system | user |  |  |  |  |  |
| sharing and trading user data | among applications, so that | information sharing and user privacy protection in a secondary |  |  |  |  |  |  |  |  |  |  |  |
| applications can offer and negotiate user data sharing with | data sharing context, which is becoming important for current |  |  |  |  |  |  |  |  |  |  |  |  |
| other applications according to an explicit user-editable and | web, cloud, and mobile applications for the following reasons |  |  |  |  |  |  |  |  |  |  |  |  |
| II. | EXISTING PRIVACY POLICY LANGUAGES | networks and Web 2.0 technologies, | the user’s role is |  |  |  |  |  |  |  |  |  |  |
| Privacy policy languages allow both the user and organizations | changing from being a passive data subject to that of |  |  |  |  |  |  |  |  |  |  |  |  |
| to express their privacy controls and permissions. They provide | producer of data. The assumption in these settings is that |  |  |  |  |  |  |  |  |  |  |  |  |
| a precise, machine-readable approach for specifying a privacy | user wants to share. Hence, the emphasis of privacy policy |  |  |  |  |  |  |  |  |  |  |  |  |
| policy and empower applications to elicit user data according | languages also needs to change from limiting primary data |  |  |  |  |  |  |  |  |  |  |  |  |
| to the terms specified in the policy by the website. Within the | collection to preventing unintended secondary use. |  |  |  |  |  |  |  |  |  |  |  |  |
| address | the | growing | collection | of | user | data | by | websites |  | Lack of support for negotiation: | P3P has adopted a static, |  |  |
| (particularly, e-commerce sites that use the information to learn | rigid, | and “ | take-it-or-leave- | it” | approach to privacy policy: |  |  |  |  |  |  |  |  |
| about | user | interests | and | provide | personalized | “ | an organization or service provider offers a privacy |  |  |  |  |  |  |
| recommendations), while the GeoPriv was formulated by IETF | policy; the user has to accept it as a whole or leave it | ” |  |  |  |  |  |  |  |  |  |  |  |
| in | 2001 | to | manage | privacy | in | the | growing | number | of | [11]. We believe that, as user data market evolves and |  |  |  |
| applications that require geo-location information about the | users become active players in this emerging data market, |  |  |  |  |  |  |  |  |  |  |  |  |
| user when providing context-aware services [7]. AIR [23] is | rigid and inflexible policies will not suffice. Negotiation of |  |  |  |  |  |  |  |  |  |  |  |  |
| focused on data accountability while Rei [20] is targeted at | some aspects of the policies will be required so as to |  |  |  |  |  |  |  |  |  |  |  |  |
| handling | conflict | resolution | across | policies | in | distributed | provide | flexibility | and | adaptability | to | various | privacy |
| systems. Of all the above languages, P3P has been the most | personality types, purpose and context of use, as well as |  |  |  |  |  |  |  |  |  |  |  |  |
| popular and widely used structured privacy policy language on | give incentives for users to allow sharing of their data |  |  |  |  |  |  |  |  |  |  |  |  |
| The | aim of | P3P | is | to inform web | users | about | the data- | III. | PROPOSED P2U POLICY LANGUAGE |  |  |  |  |
| This list is not exhaustive. Interested reader should see [8] | data across applications and data sources increases, we foresee |  |  |  |  |  |  |  |  |  |  |  |  |
| and [19] for a full list of existing policy languages. | the emergence of various marketplaces where user data can be |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 3

Figure 1. Main elements of P2U Policy Specification Language

shared and traded with the user ’s awareness and ability to

control with whom the information is shared, for what purpose

and for how long and for what compensation. We believe such

a marketplace involves four active participants: the user ,

middleware services to ensure semantic interoperability of

data, coordination and negotiation with data consumers based

consent collection principle, P2U is based on what we referred

to as the purpose-relevance - sharing principle. That is: only

As shown in Figure 1, P2U defines eight privacy specification

element. The policy element contains one provider , one

use. There are two attributes that can be specified in the

(ii) discurl (optional) - location of human readable version

of privacy policy.

provider

user.

unique identifier for this purpose. In addition, the purpose

element is further subdivided into three sub-elements

name “public” is used here, it means that the data is

(in days) for which data can be retained for the specified

20 20 20

| whose | information | is | being | shared, | data | providers |  | DATA-PROVIDER element | : Gives information about |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (applications | that | have | collected | user | data | for | a | primary | the data service provider that issued this privacy policy. |  |  |  |  |  |  |  |  |  |
| purpose | and | can | re-share | it | with | other | applications | for | There | are | two | attributes | that | can | be | in | the | provider |
| secondary use), | data consumers | (applications that need user | element: (i) | Name | (optional) | – | i.e. name of the provider, |  |  |  |  |  |  |  |  |  |  |  |
| data for secondary purposes). Lastly, a | data broker | provides | (ii) | Provid | (mandatory) | - | a | unique | identifier | for | the |  |  |  |  |  |  |  |
| on | preferences. | To | capture | user | and | data | provider’s |  | USER element | : The user element specifies the user for |  |  |  |  |  |  |  |  |
| expectations | and | facilitate | interactions | among | the | market | whom the privacy policy is about. The user element can |  |  |  |  |  |  |  |  |  |  |  |
| players, we propose a policy language called | Purpose-to-Use | have two attributes: i) | Name - | the username of the user on |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (P2U) | . Unlike P3P that is based on the traditional | notice and | the provider | ’s | network, ii) | Userid - | unique identifier of the |  |  |  |  |  |  |  |  |  |  |  |
| data that is relevant to a particular purpose and context of use |  | PURPOSE | element | : | This | specifies | the | data | sharing |  |  |  |  |  |  |  |  |  |
| is shared. | Hence, the policy recognizes that data can be reused | purpose, with whom it was shared, for how long it can be |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and shared after collection to fulfill various purposes that are | retained, and the kinds of data that is relevant for that |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| beneficial to the user, business or society. The policy also | purpose. There can be one or more purpose elements in a |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| supports | negotiation | by | data | consumers | of | some | policy | P2U policy file. The purpose elements have two key |  |  |  |  |  |  |  |  |  |  |
| elements such as | type of data | , | retention period | and | price | (of | attributes: | i) | name | (mandatory): | name | indicating | the |  |  |  |  |  |
| data). | purpose of sharing one or more data type, ii) | puid: | a |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| A. P2U Specification Elements | which are | consumer | , | retention | , and | data-group | . |  |  |  |  |  |  |  |  |  |  |  |
| elements, each of which has some other attributes that further | o | DATA-CONSUMER element | : The consumer element |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| elaborate on their usage. We hereby describe, in high-level | indicates the third-party application with whom this |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| form, the main elements of P2U: | policy was created. However, the same data can be |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | POLICY element | : This is the root element in P2U. The | shared with more than one consumer by indicating that |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Policy element encapsulates every other element in the | it is public. CONSUMER element has two attributes: (i) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| policy file. A P2U policy file has at least one policy | Name | - specifies the name of the consumer. When the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| user | and one or more | purpose(s) | . The policy is created by | shared with any third party application; (ii) | Consid: | a |  |  |  |  |  |  |  |  |  |  |  |  |
| a provider for a user and with one or more purpose(s) of | unique identifier for the consumer. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| policy element: (i) | Name | (mandatory) - P2U policy name | o | RETENTION element: | This specifies the time period |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 4

<POLICY discuri=http://mydatawebsite.com/privacy.html name= “ShoppingPolicy”>

<PROVIDER name = “FoodIntakeApp” provid=”p6528m2” />

<USER name =”Jerry” userid =”u1030050503050” />

<PURPOSE name=”Shopping Recommendations” puid=”102”>

<CONSUMER name=”MyShopApp” consid=”c10023” />

<RETENTION period=”180” />

<DATA-GROUP groupid=”g090353” negotiable=”TRUE”>

<DATA ref=”#dailyfoodintake.food” sell=”FALSE” />

<DATA ref=”#dailyfoodintake.quantity” sell=”FALSE” />

<DATA ref=”#dailyfoodintake.hungerscale” sell=”FALSE” />

</DATA-GROUP>

</PURPOSE>

</POLICY>

Figure 2: Simplified example of P2U policy file in XML format.

| purpose. The attribute | period | (in days) is mandatory. | Figure 2 shows a simplified example P2U policy file in |
| --- | --- | --- | --- |
| Also, an optional attribute | negotiable, | which is either | XML format for secondary user information sharing by an |
| TRUE or FALSE, indicates whether the retention period | hypothetical mobile app, | FoodIntakeApp | (data provider) |
| for the data is negotiable with the data consumer. If the | with another app, | MyShopApp | (data consumer) on behalf of |
| value is not stated, the default value is FALSE. | a user named | “Jerry” | and for the purpose of the user |

receiving “Shopping Recommendation s ” . In natural

| o | DATA-GROUP element | : This element describes the | language, the following permissions are allowed on user |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| group of data that can be shared for this purpose. There | data: | “retain the data for 180days” | ; | “You can access the |  |  |  |  |
| can be one or more variants of the data-group and each | following data about user for the purpose of Shopping |  |  |  |  |  |  |  |
| with | different | sharing | constraints. | Providing | these | Recommendation | – food, quantity, and hungerscale” | . In |
| variants allows the consumer and data providers to be | addition, if the data consumer app requires more data than |  |  |  |  |  |  |  |
| able to negotiate the data options that best meet the | is specified in the | “ShoppingP | olicy | ” | , it can negotiate with |  |  |  |
| needs of the consumer and not compromise the usage | the provider since the user sets the negotiable flag for data |  |  |  |  |  |  |  |
| policy of the data provider. Each variant is identified by | group to TRUE. |  |  |  |  |  |  |  |

a unique groupid attribute for the data group. In

addition, the data-group also contains a Boolean

| negotiable | attribute which indicates whether the data in | IV. | CONCLUSION AND FUTURE WORK |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the data-group can be negotiated or not. Finally, the data | This paper briefly reviews existing privacy languages and |  |  |  |  |  |  |  |  |  |
| group comprises one or more | data | elements. | enumerated | the | limitations | of | the | P3P | specification | in |

secondary information sharing. The paper then proposes a new

| (i) | DATA | element | – | The | DATA | element | policy language, called | purpose-to-use (P2U) | . Although, P2U |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| describes | the | individual | data | within | a | data | was inspired by P3P, it is not based on its principles. P2U |  |  |  |  |  |  |  |  |
| group. The data element has other attributes | supports information sharing across applications based on the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| about | the | data | that | constraint | how | each | principle of purpose of use. To support emerging market for |  |  |  |  |  |  |  |  |
| individual data within the group can be used. | user data sharing and provide some incentive to user for |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| These include: (i) | Ref (mandatory) - | a unique | sharing her data, the policy supports negotiation of some |  |  |  |  |  |  |  |  |  |  |  |  |
| reference | name | for | the | data; | (ii) | Expires | elements | of | the | privacy | policy | to | allow | flexibility | and |
| (optional) | : | specifies | an | expiry period | for | a | adaptability to the need of users and diverse contexts of use. |  |  |  |  |  |  |  |  |
| particular data. It performs a similar function | As future work, we hope to formulate a more detailed use-case |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| with | the | retention | element. | However, | this | for | the | policy | and | design | a | negotiation | protocol | for | the |
| attribute | only | affects | individual | data | while | interaction. We will also implement a prototype P2U policy to |  |  |  |  |  |  |  |  |  |
| retention | affects | the | data-group. | Where | the | support | secondary | user | data | sharing | among | mobile |  |  |  |
| expires | attribute is specified, it overrides the | applications as proof of concept. There are also many issues to |  |  |  |  |  |  |  |  |  |  |  |  |  |
| timestamp indicated in the retention element | be | addressed | in | the | future. | One | is | the | semantics | of | the |  |  |  |  |
| for the particular data; (iii) | Sell | – | this is a | language, especially for allowable purposes. We are working |  |  |  |  |  |  |  |  |  |  |  |
| boolean attribute that indicate whether the user | on defining a set of constraints [23] or rules [24] on data |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| is willing to sell the data or not. The default | retention period and data consumer that could access the data |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| value for the attribute is “FALSE”. (iii) | Price: | based on sensitivity of data group and different purpose of use. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| if the attribute sell is TRUE, then the price | Another issue that is not addressed yet is the influence of |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| attribute must be set by the user to indicate an | context | of use the policy. For example, releasing user data for |  |  |  |  |  |  |  |  |  |  |  |  |  |
| initial price for the data which the parties can | law enforcement or emergency purposes when explicit user |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| use during negotiation. | preference is not available or desirable and the system has to |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

decide based on the situation what is best for the user or

21 21 21

---

## Page 5

society. Also, since we aim to enable user awareness and [7] Schulzrinne, H. A Document Format for Expressing Privacy

control in setting preferences and permissions for secondary Preferences. Tech. rep., The Internet Engineering Task Force,

understand the policy, are not overwhelmed with too much

compliance and ensure that data consumers use data in

the privacy policies is through the use of trust and reputation

compelling approach to detect violators based on feedback

different areas such as e-commerce, peer-to-peer networks,

and mobile ad-hoc networks [25]. For example, we can allow

important factor to consider when determining what data to

application ’s trust level drops below a defined threshold, the

REFERENCES

at:http://www.stanfordlawreview.org/sites/default/files/online/to

IEEE Transactions on Software Engineering, Vol. 35, Issue

[3] W3C P3P Specification. Online at:

Preference Exchange Language 1.0 (APPEL 1.0). Tech. report,

World Wide Web Consortium, Retrieved December 12, 2012.

Retrieved June 12, 2005,

policy-04.txt.

symposium on Usable privacy and security (New York, NY,

nguages.pdf

Economic Value of Personal Data: Balancing Growth and

htm

[11] Preibusch S. (2006). Privacy Negotiations with P3P. Online at:

negotiation-p3p/

conference, June 10-14, Rome, Italy. pp 310-317.

[13] Carroll, J and Rosson, MB, 1987, “The paradox of the active

user” in JM Carroll (ed.) Interfaci ng Thought: Cognitive

Dolog, P.,Vassileva, J. (eds.) Proceedings of the Workshop on

pp. 61 – 66.

Web-Based Systems. Springer Berlin Heidelberg. Pp. 404-408.

[17] Toch E., Wang Y., Cranor L.F. (2012) Personalization and

Personalization-based Systems. User Model User-Adapted

Interactions. 22:203 – 220.

[18] Dredge, F. (2013): Facebook IPO filing reveals mobile risks and

opportunities. Available online at:

at: http://www.w3.org/Policy/pling/wiki/PolicyLangReview.

Language. Online at: http://rei.umbc.edu/

Online at: http://ceur-ws.org/Vol-328/paper12.pdf. Last

[22] AIR Policy Language. Online at:

Decision. Support System, 43:618-644.

22 22 22

| sharing of their data, it is also important that we ensure users | http://www.ietf.org/internetdrafts/draft-ietf-geopriv-common- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| information and are able to set their preferences [13]. The user | [8] | Kumaraguru, P., Cranor, L., Lobo, J., and Calo, S. A survey of |  |  |  |  |  |  |  |  |  |  |  |  |
| will be asked to review and set privacy preferences if the | privacy policy languages. Workshop on Usable IT Security |  |  |  |  |  |  |  |  |  |  |  |  |  |
| policy expires, if a new potential purpose for sharing emerges, | Management | (USM 07). In SOUPS '07: Proceedings of the 3rd |  |  |  |  |  |  |  |  |  |  |  |  |
| and if the user has set a flag to be notified for negotiation with | USA, | March | 2007), | Online | at: |  |  |  |  |  |  |  |  |  |
| user | data | consumers. | Another | issue | is | how | to | enforce | http://cups.cs.cmu.edu/soups/2007/workshop/Privacy_Policy_La |  |  |  |  |  |
| accordance with the contractual agreement for sharing the | [9] | World Economic Forum Report (October 2012). Unlocking the |  |  |  |  |  |  |  |  |  |  |  |  |
| data. The problem is similar to that of enforcing copyright | Protection. | Online | at: |  |  |  |  |  |  |  |  |  |  |  |
| agreements (digital rights management). | Multi-dimensional | http://www3.weforum.org/docs/WEF_IT_UnlockingValueData_ |  |  |  |  |  |  |  |  |  |  |  |  |
| solutions to this challenge are in the works [9], involving | BalancingGrowthProtection_SessionSummary.pdf |  |  |  |  |  |  |  |  |  |  |  |  |  |
| technical, legal, economic and social measures. We believe | [10] Goldman E. (2011). The Economics of Privacy. Online at: |  |  |  |  |  |  |  |  |  |  |  |  |  |
| one solution for enforcing compliance by data consumers with | http://blog.ericgoldman.org/archives/2011/12/economics_of_pr. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| mechanism. Trust and reputation (TR) mechanisms present a | http://www.w3.org/2006/07/privacy-ws/papers/24-preibusch- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| from others. TR mechanisms have been successfully applied | [12] Iyilade J. and Vassileva J. (2013). A Framework for Privacy- |  |  |  |  |  |  |  |  |  |  |  |  |  |
| in | managing | interactions | and | mitigating | misbehaviors | in | Aware | User | Data | Trading. | Proceeding | of | UMAP | 2013 |
| an independent monitoring and enforcement agent within the | Aspects of Human-Computer Interaction MIT Press. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| market to track complaints on misuse of data by a | data | [14] Heckmann, D. (2005). Ubiquitous User Modeling, Ph.D. thesis, |  |  |  |  |  |  |  |  |  |  |  |  |
| consumer. | This | agent | computes | trustworthiness | of | data | Computer Science Department, Saarland University, Germany |  |  |  |  |  |  |  |
| consumers based on violation their data use contract. In so | [15] Heckmann, D., Schwartz, T., Brandherm, B., Kröner, A. (2005): |  |  |  |  |  |  |  |  |  |  |  |  |  |
| doing, the framework allows the data-market community to | Decentralized User Modeling with UserML and GUMO. In: |  |  |  |  |  |  |  |  |  |  |  |  |  |
| police data usage itself and report potential violations to the | Decentralized, Agent Based and Social Approaches to User |  |  |  |  |  |  |  |  |  |  |  |  |  |
| framework management. The trust value will then form an | Modeling, DASUM-05, at UM2005, July, Edinburgh, Scotland, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| share | with | a | data | consumer | and | for | the | price | the | data | [16] Berkovsky S. (2006). Decentralized mediation of user models |  |  |  |
| consumer will have to pay to acquire the data. If the consumer | for a better personalization. Adaptive Hypermedia and Adaptive |  |  |  |  |  |  |  |  |  |  |  |  |  |
| consumer will be unable to participate in the user data market. | Privacy: | A | Survey | of | Privacy | Risks | and | Remedies | in |  |  |  |  |  |
| [1] | Tene O and Polonetsky J. (2012). Privacy in the Age of Big | http://www.guardian.co.uk/technology/2012/feb/02/facebook- |  |  |  |  |  |  |  |  |  |  |  |  |
| Data: A Time for Big Decisions. Standford Law Review. Online | ipo-mobile-risks. Last Accessed: July 15, 2013. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| pics/64-SLRO-63_1.pdf | [19] W3C (2009). Policy Language Review Wiki. Accessed Online |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [2] | Spiekermann, S. and Cranor, L. F., (2009). Engineering Privacy. | Last accessed date: 22-March-2014 |  |  |  |  |  |  |  |  |  |  |  |  |
| No.1, pp.67-82 | [20] UMBC equity research (2005). Rei : A Policy Specification |  |  |  |  |  |  |  |  |  |  |  |  |  |
| http://www.w3.org/TR/P3P11/ | [21] Kahmer M and Gilliot M. Extended Privacy Definition Tool. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [4] | Cranor, | L., | Langheinrich, | M., | and | Marchiori, | M. | A | P3P | accessed date: 16-March-2014 |  |  |  |  |
| Online: http://www.w3.org/TR/P3P-preferences/. | http://dig.csail.mit.edu/TAMI/2007/AIR/. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [5] | Dong, L., Mu, Y., Susilo, W.; Wang P. and Yan, I (2011), "A | [23] [24] | Li | N., | Yu | T., | Anton | A. | (2003). | A | Semantics-Based |  |  |  |
| Privacy Policy Framework for service Aggregation with P3P," | Approach | to | Privacy | Languages. | Online | at: |  |  |  |  |  |  |  |  |
| in Proceedings of 6 | th | International Conference on Internet and | http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.131.4 |  |  |  |  |  |  |  |  |  |  |  |
| Web Applications Services, Thinkmind, St. Maarten, pp. 171- | 832&rep=rep1&type=pdf. Last accessed date: 17-March, 2014 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 177 | [24] Denker G. and Martin D. (2004). Using Rules to define the |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [6] | Moses, | T. | eXtensible | Access | Control | Markup | Language | semantics | of | privacy | policies. | Online | at: |  |
| (XACML) Version 2.0. Tech. rep., Oasis, Retrieved June 17, | http://www.w3.org/2004/12/rules-ws/paper/76/ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2012, | http://xml.coverpages.org/XACMLv20CDCoreSpec.pdf, | [25] Jsang, A., Ismail, R., and Boyd, C. (2007). A survey of trust and |  |  |  |  |  |  |  |  |  |  |  |  |
| 2004. | reputation | systems | for | online | service | provision. | Journal | of |  |  |  |  |  |  |
