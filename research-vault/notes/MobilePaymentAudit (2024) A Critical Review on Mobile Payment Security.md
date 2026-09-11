---year: 2024

secverify_category: "Category A"
categories:
  - "[[2A.1-Web與API動態漏洞掃描 (DAST)]]"
  - "[[2B.1-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]"
title: "Mobile Payment Security: A Critical Analysis of Vulnerabilities & Emerging Threats"
pages: 19
source: "MobilePaymentAudit (2024) A Critical Review on Mobile Payment Security.pdf"
---

# Mobile Payment Security: A Critical Analysis of Vulnerabilities & Emerging Threats

> **文獻存檔**：[PDF 原文](<../../raw-papers/2024/MobilePaymentAudit (2024) A Critical Review on Mobile Payment Security.pdf>) | [Markdown 原文](<../../raw-papers/2024/MobilePaymentAudit (2024) A Critical Review on Mobile Payment Security (Raw).md>)

> **總頁數**：19 頁

---

## Page 1

25 January 2024

Mobile Payment Security: A Critical Analysis of

Vulnerabilities & Emerging Threats

Nurainaa Nabihah Rahmad , Nurul Syazwani Mohd Zullzaidi , Nurul Dina Farisah Azmi , Nur Madeehah Khairudin

Abstract

The article explores the security aspects of mobile payment systems (MPS) in the context of

urban Internet of Things (IoT) technology. MPS leverages mobile devices and the internet to

facilitate convenient financial transactions, catering to a user base of over 960 million globally.

Nevertheless, the ease of mobile payments is accompanied by security apprehensions, including

device susceptibilities, theft risks, and potential cyber assaults. This paper examines the technical

environment of MPS, focusing on their development over time, the current utilization of

technologies like NFC, and the security measures that regulate these systems. The paper also

explores alternative payment protocols and current security measures, providing a valuable

understanding of the correlation between mobile payments and online security. This investigation

aims to enhance the safety and understanding of mobile payment systems and provide guidance for

future enhancements in security measures to create a more secure digital transaction environment.

Keywords

components, circuits, devices and systems, cybersecurity, mobile payment, mobile security, risk

management, security

Posted on 25 January 2024 — CC-BY 4.0 — This is a preprint and has not been peer reviewed. Data may be preliminary. — https://

doi.org/10.36227/techrxiv.170620372.22051414/v1

---

## Page 2

Mobile Payment Security: A Critical Analysis of Vulnerabilities &

Emerging Threats

1 1 1

Nurainaa Nabihah Rahmad , Nurul Syazwani Mohd Zullzaidi , Nurul Dina Farisah Azmi ,

1

and Nur Madeehah Khairudin

1

Affiliation not available

January 25, 2024

Abstract

The article explores the security aspects of mobile payment systems (MPS) in the context of urban Internet of Things (IoT)

technology. MPS leverages mobile devices and the internet to facilitate convenient financial transactions, catering to a user base

of over 960 million globally. Nevertheless, the ease of mobile payments is accompanied by security apprehensions, including

device susceptibilities, theft risks, and potential cyber assaults. This paper examines the technical environment of MPS, focusing

on their development over time, the current utilization of technologies like NFC, and the security measures that regulate

these systems. The paper also explores alternative payment protocols and current security measures, providing a valuable

understanding of the correlation between mobile payments and online security. This investigation aims to enhance the safety

and understanding of mobile payment systems and provide guidance for future enhancements in security measures to create a

more secure digital transaction environment.

Introduction

Urban IoT technology has facilitated the rise of mobile payments, which have become a significant payment

method, serving an impressive user base of 960 million worldwide [1]. These technologies leverage the

widespread use of mobile devices and the internet to offer unparalleled convenience and accessibility in

conducting financial transactions. Nevertheless, this convenience is accompanied by an intricate landscape

of security issues and weaknesses that necessitates meticulous consideration. The Mobile Payment System

(MPS) enables consumers to purchase goods or services securely and allows retailers to transact through

mobile devices. MPS stands for Mobile Payment System, which encompasses traditional and new methods

of securely conducting financial transactions between individuals or organizations using a mobile device over

a mobile network [2].

Trust and confidence are crucial when conducting financial transactions through mobile payments. Users

often resist participating in transactions due to security and privacy concerns associated with mobile pay-

ments. Mobile devices are susceptible to theft or misplacement, leading to financial fraud or identity theft in

the event of loss or theft. Engaging in transactions on a mobile device entails the risks commonly linked to

mobile usage. Diverse cyber-attack forms leverage technological vulnerabilities, enabling hackers to exploit

these weaknesses and deceive individuals [3].

Due to the significant number of users who trust and depend on mobile payment systems, there is a pressing

requirement for extensive research on the underlying mechanisms and obstacles associated with this tech-

nology. Companies can optimize and perfect this technology by gaining a more profound comprehension

of these factors to cater effectively to the evolving demands of users. This article thoroughly examines the

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

1

---

## Page 3

security protocols associated with mobile payments. The study encompasses possible challenges and risks,

such as situations where data theft or vulnerabilities may occur. This study aims to enhance comprehension

of the correlation between mobile payments and online security. This comprehension will be valuable in

contemplating strategies to enhance the security of these systems in forthcoming advancements.

Overview

Mobile payment is a contemporary and efficient method of conducting transactions through mobile devices,

employing diverse technologies like Short Message Service (SMS) and Quick Response (QR) codes to facilitate

smooth and uninterrupted transactions. Users can expediently and securely conduct financial transactions

using this uncomplicated payment method through their cell phones or other mobile devices. Mobile payment

promotes using mobile devices for purchasing goods and services, eliminating the need for cash, cards, or

cheques [4].

The advent of mobile payment has significantly streamlined and enhanced convenience, garnering extensive

adoption in diverse locations. Prominent companies like Apple, Google, Samsung, and PayPal have intro-

duced their mobile payment systems, which are accessible on either iOS, Android, or both operating systems.

Initially, SMS payments were convenient for conducting transactions on mobile devices. This approach in-

volves sending payment information to a mobile payment service provider via text. Consequently, the mobile

payment service provider facilitates the transaction between the customer and the merchant. The purchase

expense is ultimately included in the mobile subscriber’s monthly phone bill [5].

The COVID-19 pandemic has increased mobile communication, highlighting its advantages for the overall

user population. The surge in popularity has led to a new ecosystem in mobile payments, characterized by

a significant rise in the utilization of mobile wallets for conducting financial transactions. The substantial

growth of e-commerce and m-commerce businesses could be attributed to the worldwide adoption of mobile

payments. Amidst the epidemic, businesses increasingly preferred online payments instead of cash on delivery.

With the evolution of needs and behaviors, individuals embraced mobile payments due to their inherent

convenience, which obviated the necessity of constantly carrying physical currency [6].

Retail adoption of mobile payments varies significantly [7] despite the numerous benefits associated with

this technology. Near Field Communication (NFC) is a wireless technology that allows the exchange of data

between devices close to each other. Mobile devices now possess NFC capabilities, enabling them to function

as customers, credit cards, and access card identifiers. The adoption of NFC-enabled mobile devices for

payment transactions has steadily increased due to the technology’s fast speed, simplicity, and user-friendly

nature. NFC performs at a frequency of 13.56 MHz, enabling data exchange through a straightforward

touch method within a range of 10 cm. The system supports data speeds of 106, 212, or 424 Kbit/s. The

integration of NFC capability into a single chip has enabled its incorporation into mobile phones and various

other items and devices [8].

Attackers can exploit vulnerabilities in the data and physical layers by manipulating the distance between

connected devices using NFC technology. Although data layer vulnerabilities are commonly addressed using

conventional software engineering principles and cryptography, physical layer attacks present a distinct chal-

lenge. Relying solely on cryptographic protections is often inadequate, as evidenced by relay attacks that

bypass cryptographic systems. To address NFC vulnerabilities, it is necessary to employ non-cryptographic

methods to enhance security in addition to cryptographic standards [9].

According to the research in [10], the security model consists of four critical parts, which are as follows:

1. The mobile terminal utilizes wireless internet connectivity to establish communication with application

servers, the Trusted Third Party (TTP) server, and other mobile terminals. The mobile terminal’s client

program manages tasks such as parsing and packaging XML documents and performing encryption,

decryption, and digital signature operations.

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

2

---

## Page 4

2. The application server, functioning as an e-commerce server on the internet, responds to requests from

mobile terminals by providing appropriate services. It establishes communication with the TTP and

mobile terminals through specialized protocols designed for identification purposes. Additionally, it

performs tasks such as packaging and parsing XML documents, encrypting and decrypting data using

symmetric and public vital methods, and digitally signing specific parts of XML documents.

3. Trusted Third Party (TTP): The TTP facilitates efficient access for mobile terminals and Public Key

Infrastructure (PKI) systems, enabling seamless integration of application programs across different

PKI systems. Mobile terminals, application servers, and other transactional organizations can utilize

it as irrefutable evidence in the case of a transaction dispute. In addition, TTP validates signatures

for mobile terminals, reducing the computational burden on them.

4. The PKI System is a comprehensive security framework that utilizes public vital techniques to offer

security services. It is widely acknowledged as an online authentication mechanism for e-commerce

security.

The study in [11] identifies the typical entities involved in these payment protocols as follows:

1. The customer or cardholder (C) initiates the transaction using a mobile device.

2. Merchant (M): The individual who receives payment from the customer.

3. The issuer (I) refers to the customer’s financial institution.

4. The Acquirer (A) refers to the financial institution representing the Merchant.

5. Payment Gateway (PG): A payment gateway managed by the acquirer that acts as a mediator between

the issuer and the acquirer to process transactions.

Based on study [11], three basic transactions are essential inside payment protocols:

1. Payment: C uses a mobile device to pay M for services received.

2. Value Subtraction: C requests that I deduct the transaction amount from their account, which corre-

sponds to the transaction price.

3. Value Claim: M requests that A or PG credit their account with the transaction value.

The study in [11] provides explanations about existing mobile payment protocols:

1. ECash: This framework allows for secure and anonymous online payments involving C, M, Client’s

Bank, and Merchant’s Bank (E-Bank). For anonymity, E-Bank controls electronic currency via RSA

and a blind signature. By monitoring coin deposits, ECash protects against double spending.

2. NetCash is an anonymous monetary exchange system that includes C, M, and Currency Server. Net-

Cash employs symmetric and asymmetric encryption to ensure security, scalability, and interoperability

by validating coins for fraud and double spending during offline transactions.

3. Secure Electronic Transfer Protocol (SET): This credit card payment protocol uses both symmetric

and asymmetric cryptography and involves C, M, I, A, and a certificate authority. Through SSL,

DES, and RSA digital signatures, SET achieves client and mutual authentication, confidentiality, and

integrity. However, it necessitates a significant amount of computation and storage space.

4. i-Key-Protocol (iKP): iKP employs asymmetric cryptography and includes C, M, and PG. It delivers

SET-like security by enabling a single or more Certificate Authorities. Order Information is secure

using SSL or IPSec, although the protocol is computationally demanding.

5. Shedid’s modified Secure Electronic Transfer Protocol (MSET) minimises computing cost by replac-

ing asymmetric cryptography with symmetric approaches. Through a two-step process, it preserves

security and establishes a secure communication channel between entities.

6. MPCP2: A client-centric private mobile payment protocol involving C, M, I, and A. It provides cus-

tomers with transaction control while decreasing cryptographic processes, communication strain, and

computation expense. MPCP2 prevents replay attacks and preserves payer confidentiality.

7. SLMPP (Secure Lightweight Mobile Payment Protocol): Sekhar and Sarvabhatla’s protocol includes

C, M, I, A, and PG, with a focus on the payer’s dominance in transactions. SLMPP minimises

cryptographic procedures, protects entities from payment gateway fraud, and preserves privacy.

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

3

---

## Page 5

8. Lightweight Protocol for Mobile Payment (LPMP): Tripathi and Ojha’s protocol, which is intended for

low-end mobile devices, uses efficient symmetric key cryptography. LPMP eliminates merchant setup

procedures, reduces computational effort, and prevents different security attacks such as man-in-the-

middle and masquerade while keeping transaction attributes.

Research Methodology

In this part, we explain how we conducted our research. We perform a review based on the guidelines

for review methodologies discussed in payment OR online transaction OR digital transaction OR payment

card OR credit card) AND (Security OR security control OR security measure OR intelligence OR payment

fraud OR information technology) [12]. Our preliminary search results gave 1060 research articles by enter

Mobile Payment Security keyword. Then filter result by Journals and Article and make it got 161 results

for further screening. Our research method comprises five steps as shown in Figure 1. It is drawn from

the approaches suggested by [12]. The initial step is to establish the scope of the review in order to get a

convergence of search results. Next step is searching in the review databases, with suitable search string

containing keywords. This is followed by screening of preliminary search results to narrow down the content

for review. Following the screening process, the chosen research articles are analysed and discussed. Finally,

we are conducting a brief survey using Google Forms and are seeking the participation of 50 respondents to

gather insights regarding User Awareness on Mobile Payment Security.

Defining Scope

The objective of this review is to identify the research advancements in Mobile Payment Security that could

enhance the effectiveness of security measures for digital payments. We aim to search and analyse research

articles published between 2013 and 2023, specifically focusing on articles that are relevant to our review.

Searching

The search process can be segmented into the following tasks: defining sources, developing search string, and

implementing search. The relevant search fields encompass digital payment systems and security payment.

The renowned academic online database IEEE is chosen as the review source, given its comprehensive

coverage of the topic and its convenient content search capability. Our review search exclusively encompasses

research publications published in journals or conference proceedings. Both complete articles and preview-

only articles are preserved in search results. In order to obtain further information on Mobile Payment

Security, we expand the search results beyond the Computer Science domain.

Screening

The screening stage is a crucial phase in performing a literature review, serving as a strategic filter to narrow

down the selection of research that will be incorporated into the final analysis. Figure 2 illustrates that the

screening process includes the use of exclusion and inclusion criteria. These criteria are intended to carefully

choose a pertinent and concentrated collection of articles for the review.

During the preliminary screening step, the researchers analyzed the titles and keywords of 1060 articles

received through the search method. This stage is essential for rapidly identifying publications that are in

line with the study focus and rejecting those that are not. At this stage, a total of 60 articles were rejected

because they did not relate to the specific subjects of ”mobile payment” or ”security payment,” as described

by the inclusion criteria.

Fig. 1 Research Methodology for Systhematic Literature Review Fig. 2 Literature Search and Screening Process Chart

Following the initial filter, the remaining 100 publications got additional examination through abstract re-

view. Abstracts contain succinct summaries of the publications, providing a brief overview of their primary

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

4

---

## Page 6

discoveries and their significance to the research subject. In this step, we implemented an extra set of exclu-

sion criteria that especially focused on empirical research. This indicates a preference for narrowing down

the selection to papers that include theoretical, conceptual, or review-oriented material, while eliminating

those that primarily report empirical studies.

In addition, the researchers intentionally chose to remove materials pertaining to ”money payment” or

Near Field Communication (NFC). This exemplifies a sophisticated method in determining the criteria for

inclusion, emphasizing the significance of precision in delineating the extent of the

review. The researchers attempt to preserve a more homogeneous and relevant set of literature for their

analysis by removing publications that focus on distinct features, such as traditional ”money payment” or

a specific technology like NFC.The screening stage is a systematic process used to carefully examine a wide

range of literature, with the goal of including only the most relevant papers in the review. By using a

rigorous strategy, the quality and relevance of the final compilation are improved, leading to a more robust

and focused literature evaluation.

Currently, the inclusion criteria for articles pertaining to ”mobile payment OR security payment” are being

applied. After sifting, we ultimately obtained 25 articles, which we then read in preparation for further

research. We construct our search string from keywords, such as Mobile Payment and Security Payment. To

optimise the search process, both single-word and two-word keywords are utilised. The literature evaluations

conducted thus far have not provided a comprehensive list of keywords that adequately meet the topic of

our review. Thus, we carefully merge specific terms.

Analysis of Result

The goal of literature analysis is to identify prominent research gaps and potential research contributions.

We analyse the results containing literature distribution and obtain an integrated outlook to the situation

of security research for digital payments growth [12].

Survey Result

The purpose of the survey results is to validate the reliability of the provided review, specifically in the context

of user awareness regarding Mobile Payment Security. This investigation involves systematically examining

data collected from 50 respondents through a Google Form. The overarching goal is to substantiate or

challenge assertions made in the review, contributing to a comprehensive understanding of user awareness of

Mobile Payment Security. This comprehensive inquiry ensures the originality and authenticity of our findings

in addressing the specific concerns related to user awareness in the context of mobile payment security.

MOBILE PAYMENT VULNERABILITIES

Different types of attacks can be considered for each layer. The same flaws can affect multiple layers or

categories. A layered approach to security management in mobile payment systems, as shown in Figure 3,

can provide a complete taxonomy of vulnerabilities and attacks [13].

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

5

---

## Page 7

Fig. 3 Taxonomy of vulnerabilities in m-payment systems [13]

Connection Protocol

A radio transmission medium such as NFC addresses issues of communication interception. A server, mobile

devices, a mobile verification terminal and mobile Point of Sale (POS) terminal are other components of the

NFC mobile payment system [14]. Possible attacks that can be executed against the NFC systems including

those for mobile payments are listed below [13].

1. Eavesdropping is the interception of transmitted radio signals by a potential attacker. The attacker

must have the necessary equipment to receive the signal as well as specific knowledge to extract and

interpret the data contained in the received signal to accomplish this. With the necessary equipment,

the attacker can bypass the customer’s cell phone when making the transaction.

2. Data Corruption: In this case, the attacker’s goal is not only the interception of transmitted data, but

also the alteration of the transmission. In the most basic case, the attacker simply wishes to disrupt

communication so that the receiver is unable to understand the data sent by the other device. This

type of attack can be carried out by transmitting data on the same frequencies as the original data.

This is possible if the attacker is well-versed in the protocols, modulation, and encoding employed by

the system under attack. This attack is simple to execute, but it only allows the attacker to disrupt

communication.

3. Data Modification: In this case, the attacker intends to send valid data to the receiving device, but

the data is tampered with. As a result, this attack differs from simple data corruption. The attack’s

viability is heavily dependent on transmission parameters such as the modulation index. The use of

encryption techniques makes this type of attack extremely difficult.

4. Man in the Middle: In this case, two people who want to communicate with each other are duped by

a third party, causing them to engage in a three-way conversation without their knowledge. To avoid

this, it may be beneficial to use a communication method in which one device operates in active mode

and the other in passive mode. As a result, one of the two parts continuously generates an RF field.

Platform

J2ME is a popular software platform, but it is vulnerable to a variety of attacks. J2ME is one of the preferred

platforms and several researchers have developed prototypes for their m-payment systems using J2ME [15].

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

6

---

## Page 8

Malicious Java Applications (MIDlets) installed on a customer’s mobile terminal and capable of sending SMS

to a Payment Gateway and then initiating a transaction without his approval or accessing data stored by

another MIDlet via some lower-level APIs are two examples. Side channel attacks on hardware platforms are

possible based on information intercepted by an attacker using a physical cryptosystem. The most negative

outcome is SIM card cloning.

Operating System The operating system layer is fundamentally vulnerable to mobile malware and spyware

attacks [13]. Malware, often known as malicious software, refers to any programme or file designed with

the explicit aim of causing harm to a computer, network, or server [27]. Worms, viruses, and trojans are

the most common types of malwares, but the latter is now particularly prevalent. A virus is a malicious

application that has the ability to replicate itself, and these various replicas have the capability to infect other

applications, boot sectors, or files by attaching or adding itself to them [26]. A Trojan is a type of malicious

software that illegally gains access to sensitive user interactions, such as purchase transactions and premium

rate calls, without the user’s permission. It operates discreetly in the background of the victim’s device [26].

Trojans do not require a propagation vector and can attract users by masquerading as utility programmes

or popular games. Trojans are typically combined with spyware capable of detecting and collecting data

related to phone calls such as PbStealer, web browsing, HTTP connections, or m-payment details such as

digital receipts, user credentials, or SMS such as Flexispy. It can send SMS messages from the customer’s cell

phone to the payment gateway without the customer’s knowledge. The message includes the authorization

code or security code that was sent to the customer’s phone number [13]. Other than that, Spyware is a type

of malicious software that monitors and records the activity of a victim’s device, including their location,

contacts, calls, text messages, and emails. Under certain circumstances, it has the capability to transmit

such data to another location through accessible networks (such as email, SMS, etc.) and assume control

over a device without the user’s awareness [26].

MOBILE PAYMENT VULNERABILITIES

Ensuring mobile payment security is crucial for both customers and service providers in the mobile payment

industry. Payment data must be safeguarded during storage, transmission, and active utilization [5].

Mobile Payment Security Services

The essential security services required in a mobile payment system encompass authentication, access con-

trol, confidentiality, integrity, nonrepudiation, and availability [17]. Authentication comprises two separate

services: user authentication and transaction data origin authentication. A mobile payment system must

incorporate mechanisms to authenticate the user’s identity and the origin of transaction data. Access control

ensures that only authorized individuals can utilize the mobile payment system.

Aside from the pin/passcode/screen lock pattern required to unlock a mobile device, a mobile payment

may require customers to utilize fingerprint authentication or enter a pin/password to complete a purchase.

Confidentiality is upheld to safeguard transaction data from passive attacks. Integrity ensures that data

remains unaltered, whether at rest, in transit, or use. Nonrepudiation prevents any party, whether a user or

a service provider, from denying or disowning communicated messages.

The presence of a mobile payment system guarantees its accessibility upon user request. Many security

services depend on cryptographic procedures such as encryption, hashing, digital signatures, and similar

techniques. Near Field Communication (NFC) mobile payment solutions, like Apple Pay and Google Wallet,

utilize the secure element integrated into mobile devices for cryptographic processing [5].

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

7

---

## Page 9

Mobile Payment Security Mechanisms

Various security measures have been employed to guarantee the security of mobile payments. The subsequent

mechanisms are summarised:

1. Fingerprint: Apple Pay and Samsung Pay enable customers to authenticate a payment by placing their

finger on the device’s fingerprint scanner [5].

2. Username/password: Mobile payment platforms and independent mobile payment systems commonly

utilize username/password to verify user identities and grant authorization for purchases [5].

3. Mobile payment systems often utilize multi-factor authentication to verify consumers’ identities. Users

must provide an authentication code when they log into the service using a new phone. The authenti-

cation code is subsequently emailed to the user’s designated email address [5].

4. SSL/TLS encryption is a widely used method on the Internet to safeguard data. SSL/TLS provides

confidentiality, integrity, and authentication for mobile payment data as it is transmitted over the

Internet [5].

5. NFC-based mobile payment systems utilize the secure element on a mobile device to safeguard sensitive

data and perform cryptographic operations. Apple Pay utilizes a secure element to store the user’s

fingerprint and other confidential data, including the device’s account number [5].

implications

Security is a highly significant challenge in payment systems. In order to ensure the security of payment

data, various regulations, such as the Payment Card Industry Data Security Standard (PCI DSS), have been

implemented and are strictly enforced. Mobile payment service providers are also required to adhere to these

laws. Nevertheless, safeguarding data is a challenging endeavor. The Payment Card Industry Data Security

Standard (PCI DSS) was introduced in 2004. The Payment Card Industry Data Security Standard (PCI

DSS) applies to all merchants that accept or process credit cards. Nevertheless, data breaches persist [19],

[20]. In a data breach, payment card information, including username, credit card number, expiration date,

cardholder verification value, and service code for purchase, may be at risk of being compromised [5].

Users impacted are also vulnerable to fraudulent activities and the theft of their personal information.

Mobile payment systems are susceptible to various hazards and assaults. A mobile device is not explicitly

designed for mobile payment or as a point of sale, unlike a point of sale (POS) device found in large retailers.

POS devices are regularly maintained, monitored, and exclusively used for sales transactions. Multiple

applications commonly share a mobile device and serve various purposes, including email administration,

document manipulation, and leisure activities.

Users must update their mobile operating systems. It is still being determined whether the latest security

updates have been installed on a mobile device [5]. Mobile devices have been susceptible to various risks and

attacks, such as sniffing, spam, spoofing, phishing, pharming, and malware [21]. It is imperative to consider

these menaces and assaults when developing a mobile payment system [5].

Malware

Mobile malware poses a significant risk to the security of a mobile payment system. In 2014, Symantec

discovered more than 1 million applications that were infected with malware [19]. Most malware found on

mobile devices is linked to call recording, instant messaging, GPS location tracking, sending call logs, and

accessing other critical data. Zeus is a prominent form of Trojan software specifically created to collect one-

time passwords banks provide to verify mobile transactions. This component of Trusteer’s Rapport program

guarantees secure connectivity for consumers accessing their banks’ web portals.

Nevertheless, Zeus diligently monitors and transmits all incoming SMS messages to a remote malevolent

website. A Zeus crook can pilfer the victim’s financial credentials and exhaust their bank accounts. A

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

8

---

## Page 10

mobile version of the Zeus malware, known as ZitMo, has been detected on Symbian, BlackBerry, and

Android platforms. This malware can steal one-time passwords that banks use to authenticate mobile

transactions [5].

SSL/TLS Vulnerabilities

Several mobile payment systems depend on SSL/TLS to protect data transmitted over the Internet. However,

SSL/TLS and its implementation may contain flaws that the wrong users could exploit to compromise security

[5]. The Heartbleed Bug is a critical vulnerability in the OpenSSL cryptographic library [23]. Unscrupulous

individuals can exploit the vulnerability to pilfer data safeguarded by SSL/TLS encryption. The Heartbleed

vulnerability was identified in April 2014.

Nevertheless, the vulnerability has existed since the launch of OpenSSL 1.0.1 on March 14, 2012. SSL/TLS

is susceptible to man-in-the-middle (MITM) attacks. In an SSL/TLS MITM (Man-in-the-Middle) attack,

individuals with malicious intent position themselves between a client and an SSL/TLS server. The assailant

can view all network data between the client and the server in its original, unencrypted form. It is imperative

to employ encryption to prevent interception of network traffic. Confidential information, such as login

credentials and credit card details, is currently at risk. The perpetrator can illicitly appropriate funds from

compromised user accounts or exploit them for fraud [5].

Data Leakage

The mobile payment process involves the addition of two new participants in comparison to the traditional

payment card method. When a user uses a mobile wallet to purchase at a mobile point of sale (POS), there

are five entities involved in the process: the provider of the mobile wallet service, the provider of the mobile

payment as POS service, the merchant, the acquiring bank, and the issuing bank. In order to complete a

purchase, all players must gather transaction data initially.

The regulations require all parties involved in the payment process to follow security standards for payment

data strictly. Occurrences may still transpire [5]. In the instances of Target [19] and Home Depot [24],

perpetrators gained unauthorized access to credit card data, including names, mailing addresses, phone

numbers, and other relevant information. Countless customers were affected. The POS systems in Target

and Home Depot hacks were targeted by a specifically designed malware called Backoff [16]. Mobile payment

service providers can learn valuable insights from these data breaches and prevent future issues [5].

MOBILE PAYMENT THREATS REMEDIATION

To minimize the risks linked to mobile payments, both users and service providers should implement security

measures that protect the integrity of data and prevent any unauthorized access or disclosure of sensitive

information. Utilize strong pin/password/screen lock pattern to protect mobile devices, regularly update

mobile operating systems and install all recommended security patches, avoid downloading malicious software

onto mobile devices, exercise caution when receiving suspicious SMS messages and emails, avoid connecting

to untrusted hotspots for Wi-Fi access, and refrain from proceeding if encountering messages such as ”unable

to authenticate the user’s identity [5].

Users of mobile payment applications may be required to authenticate their account once and have

their password securely stored for future use. If this scenario arises, users must exercise prudence, as a

pin/password/screen lock pattern acts as the ultimate security measure to discourage unauthorized transac-

tions. Mobile payment service providers must implement necessary measures to ensure the security of mobile

payment applications, safeguard payment data, and protect backend data. Several mobile payment appli-

cations employ SSL/TLS protocols to guarantee the security of data during transmission over the Internet.

Authentication of the server’s certificates is mandatory for these mobile payment applications. If a mobile

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

9

---

## Page 11

payment system comes across an invalid certificate, it must immediately cease its operations and notify users

about the possibility of an attack [5].

THE DEVELOPMENT OF MOBILE KEY (MKEY)

An organized methodology employing hardware encryption devices has been implemented to enhance the

security and reliability of mobile payment data. Incorporating the high-confidential security annex, Mkey

(Mobile Key), represents a significant advancement in enhancing mobile security. The Mkey is a separate

safety encryption device operating independently of the leading information security features. It utilizes

hardware implementation to address security aspects beyond the MIS-SDK’s capabilities.

The system employs hardware encryption, key diversification, and customized interfaces and maintains a

clear separation between mobile devices and cards. Mkey enhances mobile security and tackles the challenge

of ensuring strong privacy by integrating an external encryption device for cell phone safety. Mkey’s technical

expertise lies in its utilization of hardware encryption, which supplants software encryption and integrates

preventive attack modules. Mkey is engineered to possess structural autonomy from mobile phones and

businesses, establishing connections through interfaces such as IF cards or RF-SIM cards.

The adaptable functionality of the system allows for the fulfillment of electronic wallet and electronic pass-

book needs. This is achieved through flexible configuration and security algorithm enhancements without

necessitating any modifications to the mobile phone setup. Mkey offers secure data storage and encryp-

tion. Its versatile interface adaptation technology facilitates data transfer between Mkey and mobile devices

through NFC, RFID, SDIO, USB, Bluetooth, IrDA, Zigbee, and data lines.

The integration of Mkey into the mobile payment system, as depicted in Figure 4, showcases its utilization

in enhancing security capabilities. Mkey is crucial in ensuring secure data decryption and verification on the

server side. It provides identity authentication and data encryption for mobile phone transactions. Mkey

and MIS-SDK have a mutually beneficial and interdependent relationship, where MIS-SDK offers software

encryption while Mkey contributes hardware encryption. The partnership between MIS-SDK and Mkey

establishes a robust mobile security solution that offers a two-tiered approach to security within the mobile

payment ecosystem [16].

Fig. 4 The Application of Mkey in mobile payment system [16]

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

10

---

## Page 12

RESULT SURVEY

A survey was conducted to see on user awareness regarding mobile payments and its security. Figure 5 to

17 below are the results of 40 respondents.

Fig. 5 Respondents Age

Fig. 6 Respondents Gender

Fig. 7 Respondents Education Level

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

11

---

## Page 13

Fig. 8 Respondents Mobile Payment Usage

Fig. 9 Respondents Mobile Payment Method

Fig. 10 Respondents Mobile Payment Concern

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

12

---

## Page 14

Fig. 11 Respondents Experience Regarding Mobile Payment Security

Fig. 12 Respondents and Mobile Payment Security Features

Fig. 13 Respondents Awareness of Mobile Payment Security Features

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

13

---

## Page 15

Fig. 14 Respondents and Mobile Payments Updates

Fig. 15 Respondents and Mobile Payments Security Measures

Fig. 16 Respondents and Mobile Payments Education

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

14

---

## Page 16

Fig. 17 Respondents and Mobile Payments Information

In our Mobile Payment Security Awareness Survey with 40 respondents, we observed a diverse age distribu-

tion, with the majority falling within the 18-24 age brackets, constituting 67.5%. Gender distribution was

60% identifying as female and 40% as male. Regarding education, 52.58% held a bachelor’s degree, while 30%

is diploma and other level of education consists of Penilaian Menengah Rendah (PMR) and Sijil Pelajaran

Malaysia (SPM). In terms of mobile payment usage, 22.5% reported using these methods on a daily basis,

and the majority falling to rarely constituting 35% with Google Pay being the most utilized (42.5%).

Security awareness revealed that 57.5% of participants were very concerned and 15% of participants were

somewhat concerned about the security of their financial information when using mobile payments. Notably,

60% had not experienced security issues or unauthorized transactions. Concerning knowledge of security

features, 55% of participants expressed familiarity with these security features. The remaining 17.5% were

not aware of these measures, while another 27.5% were unsure. Some features that are recognized are

biometric authentication such as face recognition and fingerprint identification.

In terms of security practices, a significant majority (70%) regularly updated their mobile payment apps,

while 85% employed additional security measures such as PINs or passwords. 67.5% of the respondents

sought information to enhance security, primarily from social media (67.7%).

Regarding of improvements or addition security measures, majority of respondents would like to have a

more security measures adapted to mobile payment security such as multi factor authentication or TAC for

every payment, which some mobile payment apps already implementing them. Some also said to include

device health checks and to ensure an easier flow of payments, and regularly update the face recognition to

3 months.

When asking for feedback or comments regarding mobile payments, most of respondents don’t say anything

but one respondent said that they used mobile payments app for games, so it really makes sense that people

wanted a faster payment transaction.

These findings offer valuable insights into the mobile payment security landscape, emphasizing the impor-

tance of ongoing user education and the adoption of secure practices to safeguard financial transactions.

Additionally, respondents provided diverse suggestions and feedback, highlighting areas for potential im-

provement in mobile payment security measures. Security landscape are dynamics, hence behavioral and

adaptive methods are the tools needed to analyze traffic in these ever-changing and agile environment [28-29].

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

15

---

## Page 17

CONCLUSION

Mobile payment systems (MPS) demonstrate contemporary financial inclusivity but possess vulnerabilities.

The utilization of NFC and QR technologies allows for rapid transactions. However, these systems are

susceptible to various risks and dangers. The study reveals weaknesses in devices and protocols, highlighting

the necessity for strong security measures. Studying security protocols and methodologies highlights the

need for non-cryptographic improvements in NFC technologies. Collaboration, user awareness, and layered

security are essential for maintaining trust. The study highlights the crucial equilibrium between convenience

and security in MPS, emphasizing the need for ongoing innovations to strengthen these systems against

emerging threats.

Acknowledgement

We, the authors, collectively extend our heartfelt gratitude to Sir Mohammad Hafiz Yusof from the College

of Computing Informatics and Mathematics at Universiti Teknologi MARA (UiTM), Tapah, Malaysia. His

guidance and unwavering support have been invaluable, significantly enriching our research journey. Our

deepest thanks go to our parents for their unwavering love, encouragement, and sacrifices, serving as our

constant inspiration. We also appreciate the support and encouragement from our mentors, colleagues, and

friends. Lastly, we acknowledge the divine guidance and blessings that provided strength and guidance

throughout our collaborative research endeavors.

References

[1] L. Fang et al. , “A Secure and Authenticated Mobile Payment Protocol Against Off-site Attack

Strategy,” IEEE Trans. Dependable Secur. Comput. , vol. 19, no. 5, pp. 3564–3578, 2021, doi:

10.1109/TDSC.2021.3102099.

[2] abdullah almuhammadi, “An Overview of Mobile Payments, Fintech, and Digital Wallet in Saudi Arabia,”

pp. 271–278, 2020.

[3] T. Ganesan, T. S. Ong, W. P. Cheah, and T. Connie, “Assessment of Security Risk Impact on Mo-

bile Payment Services,” IEEE Int. Conf. Artif. Intell. Eng. Technol. IICAIET 2020 , 2020, doi:

10.1109/IICAIET49801.2020.9257829.

[4] M. Xiao and M. Junjie, “Mobile Payment as a Trend: Impetus and Barriers behind this Technology,”

Proc. - 2021 2nd Int. Conf. Educ. Knowl. Inf. Manag. ICEKIM 2021 , pp. 512–515, 2021, doi:

10.1109/ICEKIM52309.2021.00118.

[5] Y. Wang, C. Hahn, and K. Sutrave, “Mobile payment security, threats, and challenges,” Proc. 2016

2nd Conf. Mob. Secur. Serv. MOBISECSERV 2016 , pp. 1–5, 2016, doi: 10.1109/MOBISEC-

SERV.2016.7440226.

[6] B. Galhotra, A. Jatain, S. B. Bajaj, and V. Jaglan, “Mobile Payments: Assessing the Threats, Challenges

and Security Measures,” Proc. 5th Int. Conf. Electron. Commun. Aerosp. Technol. ICECA 2021 , no.

Iceca, pp. 997–1004, 2021, doi: 10.1109/ICECA52323.2021.9676092.

[7] T. Wiradinata, “Mobile Payment Services Adoption: The Role of Perceived Technology Risk,” 2018 Int.

Conf. Orange Technol. ICOT 2018 , pp. 1–5, 2018, doi: 10.1109/ICOT.2018.8705859.

[8] M. Al-tamimi and A. Al-haj, “for NFC Mobile Payment Applications,” pp. 827–832, 2017.

[9] V. Njebiu, M. Kimwele, and R. Rimiru, “Secure Contactless Mobile Payment System,” Proc. -

2021 IEEE Latin-American Conf. Commun. LATINCOM 2021 , pp. 1–6, 2021, doi: 10.1109/LATIN-

COM53176.2021.9647831.

[10] W. Feifei, “Research on security of mobile payment model based on trusted third party,” NSWCTC

2010 - 2nd Int. Conf. Networks Secur. Wirel. Commun. Trust. Comput. , vol. 1, pp. 442–445, 2010, doi:

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

16

---

## Page 18

10.1109/NSWCTC.2010.110.

[11] B. Narwal, “Security Analysis and Verification of Authenticated Mobile Payment Protocols,” 2019

4th Int. Conf. Inf. Syst. Comput. Networks, ISCON 2019 , pp. 202–207, 2019, doi: 10.1109/IS-

CON47742.2019.9036151.

[12] N. Priya and J. Ahmed, “A Survey on Digital Payments Security: Recent Trends and Future Opportu-

nities,” Int. J. Comput. Trends Technol. , vol. 69, no. 8, pp. 26–34, 2021, doi: 10.14445/22312803/ijctt-

v69i8p107.

[13] A. Vizzarri, M. Vari, and A. Vizzarri, “Security in Mobile Payments,” no. October 2013, 2016.

[14] J. Panduro-Ramirez, J. Padilla-Caballero, A. Rana, S. K, W. K. Ibrahim, and M. B. Alazzam, “Empirical

Method to Analysis Mobile Payment Authentication Enhancement using Blockchain,” pp. 1228–1233, 2023,

doi: 10.1109/icacite57410.2023.10182636.

[15] S. Agarwal, “Security Issues in Mobile Payment Systems,” Indian Inst. . . . , no. July 2015, pp. 142–152,

2007, [Online]. Available: http://www.csi-sigegov.orgwww.csi-sigegov.org/2/14 310 2.pdf

[16] J. Xu, T. Pan, and L. Zheng, “Design and implementation of high security mobile payment system,” Proc.

- Int. Conf. Commun. Syst. Netw. Technol. CSNT 2012 , pp. 493–497, 2012, doi: 10.1109/CSNT.2012.112.

[17] W. Stallings, Cryptography and Network Security: Principles and Practice, 6th Editio. Pearson, 2013.

[18] PCI Security Standards Council, “PCI Standards and Documents.” [Online]. Available:

https://www.pcisecuritystandards.org/index.php.

[19] Target, “Response & resources related to Target’s data breach,” 2014. .

[20] HomeDepot, “The Home Depot Reports Findings in Payment Data Breach Investigation,” 2014. PCI

Security Standards Council Official PCI Security Standards Council Site A global forum that brings together

payments industry stakeholders to develop and drive adoption of data security standards and resources for

safe payments.

[21] Y. Wang, K. Streff, and S. Raman, “Smartphone Security Challenges,” Computer (Long. Beach. Calif).,

vol. 45, no. 12, pp. 52–58, Dec. 2012.

[22] Symantec, “Internet Security Threat Report,” 2015.

[23] Codenomicon, “The Heartbleed Bug,” 2014. [Online]. Available: http://heartbleed.com/.

[24] HomeDepot, “The Home Depot Reports Findings in Payment Data Breach Investigation,” 2014. [On-

line]. Available: https://corporate.homedepot.com/MediaCenter/Document s/Press Release.pdf.

[25] NCCIC, “Backoff: New Point of Sale Malware.” Department of Homeland Security, pp. 1–10, 2014.

[26] M. Ahvanooey, Q. Li, M. Rabbani, and A. Rajput, “A Survey on Smartphones Security: Software

Vulnerabilities, Malware, and Attacks,” IJACSA) International Journal of Advanced Computer Science and

Applications , vol. 8, no. 10, 2017, Available: https://arxiv.org/ftp/arxiv/papers/2001/2001.09406.pdf

[27] B. Lutkevich, “What is malware? Definition from SearchSecurity,” SearchSecurity , Jun. 2022.

https://www.techtarget.com/searchsecurity/definition/malware

[28] M. H. M. Yusof and A. M. Zin, ”Network-Level Behavioral Malware Analysis Model based on Bayesian

Network,” 2021 International Conference on Computer & Information Sciences (ICCOINS), Kuching,

Malaysia, 2021, pp. 316-321, doi: 10.1109/ICCOINS49721.2021.9497140.

[29] Yusof, M.H.M., Mokhtar, M.R., Zain, A.M., & Maple, C. (2018). Embedded Feature Selection Method

for a Network-Level Behavioural Analysis Detection Model. International Journal of Advanced Computer

Science and Applications, 9, 509-517.

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

17

---

## Page 19

’

Posted on 25 Jan 2024 — CC-BY 4.0 — https://doi.org/10.36227/techrxiv.170620372.22051414/v1 — e-Prints posted on TechRxiv are preliminary reports that are not peer reviewed. They should not b...

18
