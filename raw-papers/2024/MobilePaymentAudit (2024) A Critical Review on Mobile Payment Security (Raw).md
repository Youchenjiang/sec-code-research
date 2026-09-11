---
title: "Mobile payment security, threats, and challenges"
creator: "'Certified by IEEE PDFeXpress at 02/06/2016 8:41:23 AM'"
pages: 5
---

# Mobile payment security, threats, and challenges

> **總頁數**：5 頁

---

## Page 1

Mobile Payment Security, Threats, and Challenges

| Yong Wang | Christen Hahn and Kruttika Sutrave |
| --- | --- |
| College of Computing | College of Computing |
| Dakota State University | Dakota State University |
| Madison, SD 57042 | Madison SD 57042 |

yong.wang@dsu.edu

as the POS, mobile payment platform, independent mobile

I. INTRODUCTION

etc. all developed and released their own mobile payment

systems. These mobile payment systems are available either on

the mobile subscriber’s monthly phone bill. An early example

payments at contactless POS using a NFC antenna and in iOS

apps. In addition to the NFC-enabled mobile payment systems,

many online mobile payment systems, such as PayPal and

Alipay, are also available in the Apple App store and the Google

1

cjhahn15637@pluto.dsu.edu,

kruttika.sutrave@trojans.dsu.edu

Unlike a POS device in a large retailer which is constantly

maintained, monitored, and exclusively used as a point of sale,

mobile payment system.

introduces mobile payment systems. Section III examines

A. Mobile Payment

A traditional card payment process is shown in Figure 1. It

includes five key players, consumer (cardholder), merchant or

| Abstract | – Mobile payment systems can be divided into five | Play store. These mobile payment systems can also be used to |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| categories including mobile payment at the POS, mobile payment | make purchases at a POS in grocery stores or at restaurants. |  |  |  |  |  |  |  |  |
| payment | system, | and | direct | carrier billing. | Although | mobile | Security is one of the biggest concerns in payment systems. |  |  |
| payment has gained its popularity in many regions due to its | Many regulations, i.e., PCI DSS (Payment Card Industry Data |  |  |  |  |  |  |  |  |
| convenience, it also faces many threats and security challenges. In | Security Standard) [4], are in place and have been enforced to |  |  |  |  |  |  |  |  |
| this paper, we present a mobile payment processing model and | ensure | payment | data | security. | Mobile | payment | service |  |  |
| introduce each type of mobile payment systems. We summarize | providers must also comply with these regulations. However, it |  |  |  |  |  |  |  |  |
| the security services desired in mobile payment systems and also | is not an easy task to protect data. PCI DSS was first released |  |  |  |  |  |  |  |  |
| the security mechanisms which are currently in place. We further | in 2004. Any merchant who accepts or processes payment cards |  |  |  |  |  |  |  |  |
| identify and discuss three security threats, i.e., malware, SSL/TLS | must comply with the PCI DSS. However, data breach still |  |  |  |  |  |  |  |  |
| vulnerabilities, and data breaches, and four security challenges, | occurs [5], [6]. When a data breach incident occurs, payment |  |  |  |  |  |  |  |  |
| i.e., malware detection, multi-factor authentication, data breach | card information, such as, user name, credit card number, |  |  |  |  |  |  |  |  |
| prevention, | and | fraud | detection | and | prevention, | in | mobile | expiration date, cardholder verification value, service code for |  |
| payment systems. | purchase, might be compromised. Users who are affected are |  |  |  |  |  |  |  |  |
| Keywords – Mobile payment, security, threats, remediation | also exposed to fraud and identity theft. |  |  |  |  |  |  |  |  |
| challenges | Mobile payment systems also face other threats and attacks. |  |  |  |  |  |  |  |  |
| Mobile devices have reimagined our lives [1]. They are also | a mobile device is not an exclusive device for mobile payment |  |  |  |  |  |  |  |  |
| innovating | the | way | of | payment | methods. | In | addition | to | or as a point of sale. A mobile device is often shared by multiple |
| traditional payment methods, such as cash, check, credit card, | apps and used for multiple purposes such as managing emails, |  |  |  |  |  |  |  |  |
| debit card, etc., payments can also be made easily on mobile | word processing, and entertainment. It is up to the users to |  |  |  |  |  |  |  |  |
| devices. Transactions on a mobile device can be conducted via | upgrade the mobile operating systems. A mobile device may or |  |  |  |  |  |  |  |  |
| Short Message Service (SMS) messages, at a point of sale | may not have the latest security patches. Many threats and |  |  |  |  |  |  |  |  |
| (POS), as a POS, and online in the Internet. Mobile payment | attacks have been reported on mobile devices, such as sniffing, |  |  |  |  |  |  |  |  |
| has | become | much | easier | and | convenient | and | gained | its | spam, spoofing, phishing, pharming, and malware [7]. These |
| popularity in many regions. Apple, Google, Samsung, PayPal, | threats and attacks must be considered in the development of a |  |  |  |  |  |  |  |  |
| iOS, Android, or both devices. Forrester forecasts that US | This paper focuses on security issues in mobile payment |  |  |  |  |  |  |  |  |
| mobile payments will reach $90B in 2017, compared to $12.8B | systems. The remainder of this paper is organized as follows: |  |  |  |  |  |  |  |  |
| mobile payments in 2012 [2]. | Section II presents a mobile payment processing model and |  |  |  |  |  |  |  |  |
| SMS payments were adopted earlier for purchasing using a | security mechanisms and desired security services in mobile |  |  |  |  |  |  |  |  |
| mobile device. A text message with payment information is sent | payment | systems. | Section | IV | discusses | mobile | payment |  |  |
| to a mobile payment service provider. The mobile payment | security threats and remediation, followed by a discussion of |  |  |  |  |  |  |  |  |
| service provider processes the transaction between the customer | mobile payment security challenges in Section V. Section VI |  |  |  |  |  |  |  |  |
| and the merchant. The cost of the purchase is then charged on | summarizes and concludes the paper. |  |  |  |  |  |  |  |  |
| of the mobile payment via SMS messages was demonstrated by | II. | MOBILE PAYMENT SYSTEMS |  |  |  |  |  |  |  |
| Coca Cola in 1997 using a Coke vending machine [3]. As NFC | Mobile payment is a payment service performed from or via |  |  |  |  |  |  |  |  |
| (Near | Field | Communication) | technology | advances, | NFC- | a mobile device. Many mobile payment systems are available |  |  |  |
| enabled mobile payment systems are also available. Apple | on iOS and Android devices. A bank account, a credit or debit |  |  |  |  |  |  |  |  |
| announced their Apply Pay program based on NFC technology | card, or a store-issued card, is often required to link to a mobile |  |  |  |  |  |  |  |  |
| on September 9, 2014. Apple Pay lets mobile devices make | payment account before a purchase can be made. |  |  |  |  |  |  |  |  |


---

## Page 2

| retailer, | acquiring | bank | (merchant | bank), | issuing | bank | provider. There is no merchant, acquirer, card associations, and |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (cardholder bank), card associations (Visa, MasterCard, etc.) | issuer involved in the process. The mobile payment service |  |  |  |  |  |  |  |
| [8]. A cardholder presents his/her card to a merchant to make a | provider serves the role as an acquirer. One example is WeChat |  |  |  |  |  |  |  |
| purchase. The transaction data is collected at the merchant | red envelope. WeChat red envelope is a program developed by |  |  |  |  |  |  |  |
| using a POS. The details of the transaction is sent to the | Tencent and was launched on January 17, 2014. It has the |  |  |  |  |  |  |  |
| acquiring bank. The acquiring bank captures the transaction | functions such as delivering virtual money, withdrawing cash, |  |  |  |  |  |  |  |
| information and routes it through the card network to the | checking transaction history, etc. A bank account is required to |  |  |  |  |  |  |  |
| cardholder’s | issuing | bank. | The | issuing | bank | receives | the | link to the WeChat account if a user wants to deposit cash or |
| transaction information from the acquiring bank and responds | withdraw cash from the account. Otherwise, the user can deliver |  |  |  |  |  |  |  |
| by approving or declining the transaction. The response code is | virtual money to peers as long as there is a balance in the user’s |  |  |  |  |  |  |  |
| routed back to the acquiring bank and reaches the merchant’s | account. During Chinese New Year in 2015, over 40 million |  |  |  |  |  |  |  |
| terminal. The cardholder receives the desired products or | virtual red envelopes were exchanged. In just a few days, |  |  |  |  |  |  |  |
| services if the transaction is approved by the issuing bank. | millions of new users signed up for WeChat’s red envelope |  |  |  |  |  |  |  |

program and linked their bank accounts to WeChat [9].

B. Mobile Payment Systems

Mobile payment enriches the traditional payment methods

by introducing mobile at the POS (for cardholder), mobile as

the POS (for merchant or retailer), mobile payment platform,

and direct carrier billing. Mobile payment systems can therefore

be divided into five categories, i.e., mobile payment at the POS,

mobile payment as the POS, mobile payment platform,

independent mobile payment system, and direct carrier billing.

Mobile wallet usually refers to mobile payment at the POS and

mobile payment platform which can be used to make purchases

from multiple merchants and retailers.

1) Mobile Payment at the POS: This method enables the

customer to pay with a mobile phone at the POS. Many of the

| Figure 1. | Traditional Card Payment Process | methods are based on built-in NFC technology, such as, Apple |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Figure 2 shows a process of mobile payment. In addition to | Pay and Google Wallet. |  |  |  |  |  |  |  |  |
| the five key players in the traditional card payment process, two | These built-in payment systems are easy to set up on a |  |  |  |  |  |  |  |  |
| new players are introduced. These two new players are mobile | mobile device. To set up Apple Pay, first, either scan the card |  |  |  |  |  |  |  |  |
| network | operators | (MNOs) | and | mobile | payment | service | number in with the camera or enter the information manually |  |  |
| providers (MPSPs). MNOs are mobile network carriers who | including the card number, three digit security code, expiration |  |  |  |  |  |  |  |  |
| offer direct carrier billing services. MPSPs are the service | date, and the name on the card. Apple Pay then contacts the card |  |  |  |  |  |  |  |  |
| providers who provide mobile payment services. | issuer | to | ensure | the | card | information | is | correct. | Once |

confirmed, the user needs to agree to the terms and conditions.

The application then talks to the card issuer once more and

confirms, sets up, and adds the card to the wallet. Android Pay

and Samsung Pay have similar setups.

To use a built-in payment system, hold the phone over a

NFC-enabled terminal to make a connection using NFC. Then,

depending on the smartphone, either unlock the phone, double

click the home button, or place your finger on the fingerprint

scanner to approve the transaction. The transaction is validated

with the secure element (SE) chip. This chip relays

authorization back to the NFC modem, and the transaction

finishes the same way a traditional credit card swipe would. The

terminal sends the merchant’s id number, card information, and

transaction amount to the card processor. Once the processor

reads the information, it sends an authorization request to the

card issuing bank. The card issuing bank then checks for fraud

and verifies if the card can cover the transaction amount. It

Figure 2. Mobile Payment Process either approves or declines the transaction. The merchant is

then notified whether the transaction was accepted or not.

As new players are introduced, new business models are

| also created. A mobile payment user can now send money to | Samsung Pay works a bit different than the other built-in |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| another user within a mobile payment system. The process may | payment systems. In addition to the NFC technology, Samsung |  |  |  |  |  |  |  |
| involve | only | cardholders | and | a | mobile | payment | service | Pay also utilizes magnetic secure transmission (MST). MST |

2


*[Image: Page 2 Image]*

*[Image: Page 2 Image]*

---

## Page 3

| allows users to use Samsung Pay at almost any store, because it | 5) | Direct Carrier Billing: | This method allows users to |
| --- | --- | --- | --- |
| can talk to standard magnetic credit card readers where a retailer | purchase products or services using their mobile devices. It |  |  |
| has not upgraded to the NFC readers. This process mimics the | does not require a credit or debit card as a payment. The cost of |  |  |
| same signal as physically swiping a card. | the purchase is charged on the mobile subscriber’s monthly |  |  |

mobile device. The setup is easy, quick, and convenient. It can

accepts NFC payments like Apply Pay. PayPal also provides

can also be used as mobile wallet to make a payment at a POS.

A bank account or a credit/debit card account is usually required

PayPal and Alipay (most popular in China) are two popular

online payment systems which allow individuals and businesses

Both sides signup with the mobile payment platforms and

provide their bank accounts to these acquirers and in turn the

acquirers handle the transactions. A buyer chooses to make a

payment via one of acquirers. The acquirer credits the seller’s

account and debits from the buyer’s account, and both sides are

informed about the transaction.

platforms. A company may decide to develop its own online

payment service to support mobile devices. These systems are

called independent mobile payment systems. Examples of these

independent mobile payment systems include the mobile apps

from Amazon, Starbucks, etc.

Independent mobile payment systems are very similar to

mobile payment platforms except that the independent mobile

mobile payment platform if it is widely adopted and supported

by merchants and retailers. For example, WeChat red envelope

was a program introduced by WeChat in 2014. It became so

popular and has been transformed to a mobile payment

platform, WeChat Wallet, and adopted by many merchants and

retailers in China.

3

phone bill. Direct carrier billing usually involves charging via

Boku works with 250 carrier partners and provides direct carrier

A. Mobile Payment Security Services

include authentication, access control, confidentiality, integrity,

nonrepudiation, and availability [12].

pin/passcode/screen lock pattern to gain access to a mobile

device, a mobile payment may also require users to use

fingerprints or enter pin/password to make a purchase.

Confidentiality protects the transaction data from passive

attacks. Integrity prevents the transaction data being modified

when data is at rest, in transit, and in use. Nonrepudiation

prevents either a user or a service provider from denying a

Many of these security services depend on cryptographic

operations, such as encryption, hashing, digital signatures, etc.

NFC-based mobile payment approaches, such as Apple Pay and

Google Wallet, also utilize the secure element built-in on

mobile devices for cryptographic processing.

B. Mobile Payment Security Mechanisms

as below:

• Fingerprint: Apple Pay and Samsung Pay have the

option to use fingerprint to authorize a payment by

simply touching a finger to the fingerprint scanner on

the device.

| 2) | Mobile Payment as the POS: | This method allows a | SMS messages. A user enters his/her mobile phone number to |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| merchant to use mobile as the POS and process card payments. | make purchases on a website. A transaction code is provided to |  |  |  |  |  |  |  |  |
| This method usually requires a mobile app downloaded to a | the user via a text message. The user enters the code on the |  |  |  |  |  |  |  |  |
| mobile device and requires a credit card reader connected to the | website to confirm the purchase. |  |  |  |  |  |  |  |  |
| provide card payment services at any time and from anywhere. | Direct carrier billing is very popular in Europe. For example, |  |  |  |  |  |  |  |  |
| Square Register is an example of the mobile payment at the | billing service in Europe [10]. Using the service from Boku, |  |  |  |  |  |  |  |  |
| POS. Square Register supports both transactions from a credit | users can purchase products from merchants such as Facebook, |  |  |  |  |  |  |  |  |
| card reader and keyed-in transactions. Three types of credit card | EA, Sony, Spotify, Lookout, and Riot Games. The market for |  |  |  |  |  |  |  |  |
| readers are supported currently, i.e., Square reader for magnetic | direct carrier billing on mobile devices alone is projected to be |  |  |  |  |  |  |  |  |
| stripe cards, Square reader for EMV chip cards, and Square | almost $6B by 2017 [11]. However, its growth outside of |  |  |  |  |  |  |  |  |
| contactless and chip reader. Square contactless and chip reader | Europe is very slow due to many regulatory constraints. |  |  |  |  |  |  |  |  |
| similar mobile payment as the POS service. | III. | MOBILE PAYMENT SECURITY |  |  |  |  |  |  |  |
| 3) | Mobile | Payment | Platform: | This | method | provides | Mobile payment security is critical for all mobile payment |  |  |
| online payment services on a mobile device. It requires a mobile | users | and | service | providers. | The | payment | data | must | be |
| app downloaded and installed on a mobile device. This method | protected when it is at rest, in transit, and in use. |  |  |  |  |  |  |  |  |
| to link to the mobile payment account. | The desired security services in a mobile payment system |  |  |  |  |  |  |  |  |
| to transfer funds over the Internet. PayPal and Alipay act as | Authentication | includes | two | specific | services, | user |  |  |  |
| middle man. They are mostly used for online shopping, to pay | authentication and transaction data origin authentication. A |  |  |  |  |  |  |  |  |
| utility bills, transfer money to other accounts, and to check out | mobile payment system must provide ways to verify both the |  |  |  |  |  |  |  |  |
| on shopping apps. Customers and merchants both need to have | user identity and the origin of the transaction data. Access |  |  |  |  |  |  |  |  |
| accounts to use the services provided by these payments | control ensures only the authorized person can gain access to |  |  |  |  |  |  |  |  |
| systems. | the | mobile | payment | system. | In | addition | to | the |  |
| 4) | Independent Mobile Payment System: | This method | transmitted message. Availability ensures a mobile payment |  |  |  |  |  |  |
| provides similar mobile payment services like mobile payment | system being accessible whenever users request them. |  |  |  |  |  |  |  |  |
| payment system is used only for the company itself. An | Many security mechanisms have been adopted to ensure |  |  |  |  |  |  |  |  |
| independent mobile payment system can be transformed to a | mobile payment security. These mechanisms are summarized |  |  |  |  |  |  |  |  |


---

## Page 4

• User name/password: Mobile payment platforms and has been out in the wild since OpenSSL release 1.0.1 on March

independent mobile payment systems often use user 14, 2012.

name/password to verify user identities and authorize a

purchase.

• SSL/TLS: SSL/TLS are widely used to protect data in

the Internet. SSL/TLS can provide confidentiality,

integrity, and authentication for mobile payment data

IV. MOBILE PAYMENT THREATS AND REMEDIATION

A. Malware

payment system. In 2014, Symantec has identified more than 1

B. SSL/TLS Vulnerabilities

4

SSL/TLS is also vulnerable to man-in-the-middle (MITM)

attack. In a SSL/TLS MITM attack, a malicious user sits

accounts or use the compromised accounts to make fraudulent

transactions.

C. Data Leakage

transaction data to make a purchase.

The regulations requires all the parties in the payment

valuable lessons from these data breaches and prevent such

incidents from occurring.

pattern is the last security mechanism to prevent unauthorized

transactions.

| • | Multi-factor | authentication: | Many | mobile | payment | transparently in the middle between a client and a SSL/TLS |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| systems | also | use | multi-factor | authentication | to | server. All the network traffic between the client and the server, |  |  |  |  |  |  |  |  |  |
| authenticate users. For example, an authentication code | which should be encrypted to prevent network sniffing, is |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| is required when a user signs into the service using a | exposed to the attacker in plain text. The sensitive information, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| new phone. The authentication code is then sent to the | such as a username/password and credit card number, is all at |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| user via an email to the user’s registered email account. | risk. The attacker can steal money from compromised user |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| when it transits in the Internet. | Compared to the traditional payment card process, two new |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| • | Secure Element: NFC-based mobile payment systems | players are involved in the mobile payment process. In a typical |  |  |  |  |  |  |  |  |  |  |  |  |  |
| also use the secure element on a mobile device to | scenario, for example, when a user makes a purchase using a |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| protect sensitive data and for cryptographic processing. | mobile wallet at a mobile as POS, five players are involved in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For | example, | in | Apple | Pay, | fingerprint | and | other | the | process, | i.e., | mobile | wallet | service | provider, | mobile |
| sensitive material, such as the device’s unique account | payment as POS service provider, merchant, acquiring bank, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| number, are stored in the secure element. | and | issuing | bank. | All | the | players | require | to | collect | the |  |  |  |  |  |
| Mobile payment systems are targets of cyber criminals. | process to comply with standards to secure payment data. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Many threats and attacks have been found on mobile devices. | However, incidents may still occur. In the incidents of data |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| These threats and attacks could also target a mobile payment | breaches in Target [5] and Home Depot [15], criminals gained |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| system. Compromising a mobile payment account may cause | access | to | the payment | card | information | including names, |  |  |  |  |  |  |  |  |  |
| user privacy exposure and financial loss. Detailed discussions | mailing addresses, phone numbers, etc. Millions of customers |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| on mobile device threats and attacks could be found in [7]. In | were affected. In both breaches in Target and Home Depot, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| this section, we summarize the threats and attacks which have | custom-built malware, Backoff, was deployed to the POS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| serious impacts to mobile payment security. | systems [16]. Mobile payment service providers can learn |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Mobile malware is one of the main threats to a mobile | D. | Mobile Payment Threats Remediation |  |  |  |  |  |  |  |  |  |  |  |  |  |
| million apps that are classified as malware [13]. Most malware | To mitigate mobile payment risks, mobile payment users |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| on mobile devices is related to activities such as recording calls, | and service providers both need to take security measures to |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| instant messages, locating via GPS, forwarding call logs and | protect | data | security | and | prevent | data | breaches. | Security |  |  |  |  |  |  |  |
| other vital data. Zeus is an infamous Trojan malware designed | measures for mobile payment users to take include, but are not |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| to steal one-time passwords sent by banks to authenticate | limited to, use strong pin/password/screen lock pattern to |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| mobile transactions. It appears to be part of Trusteer’s Rapport | protect mobile devices, upgrade mobile operating systems and |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| software and assures that users are securely logged into their | apply all security patches as suggested, prevent downloading |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| banks’ | online | portal. | However, | in | the | background, | Zeus | malware | on mobile | devices, use | cautions | when receiving |  |  |  |
| monitors all incoming SMS messages and forwards them to a | suspected | SMS | messages | and | emails, | do | not | connect | to |  |  |  |  |  |  |
| remote malicious website. A Zeus criminal can intercept the | untrusted hotspots for Wi-Fi access, and do not proceed if |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| banking credentials and drain the victim’s bank accounts. | receiving messages such as “ | can't verify the identity of the |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ZitMo, a mobile version of Zeus, has been found in Symbian, | website” | . Mobile payment apps may require users to sign in |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BlackBerry and Android and could be used to steal one-time | only once and cache the password for future use. Users need to |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| passwords sent by banks to authenticate mobile transactions. | use cautions if this is the case since a pin/password/screen lock |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Many mobile payment systems depend on SSL/TLS to | Mobile | payment | service | providers | must | take | all | the |  |  |  |  |  |  |  |
| protect | data | in | the | Internet. | However, | SSL/TLS | and | its | necessary steps to ensure mobile payment app security, protect |  |  |  |  |  |  |
| implementation may also have vulnerabilities which could be | payment data, and prevent data breaches on the backend. Many |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| leveraged by malicious users to breach the security. The | mobile payment apps use SSL/TLS to protect data security in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Heartbleed Bug is a serious vulnerability found in the OpenSSL | the | Internet. | These | mobile | payment | apps | must | validate |  |  |  |  |  |  |  |
| cryptographic library [14]. Malicious users can use the bug to | certificates | from the | server. | If | a | mobile | payment | system |  |  |  |  |  |  |  |
| steal information protected by the SSL/TLS encryption. The | receives an invalid certificate, it should stop right away and |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Heartbleed Bug was exposed in April 2014. However, the bug | alert users that a potential attack is likely happening. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


---

## Page 5

| V. | MOBILE PAYMENT SECURITY CHALLENGES | REFERENCES |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Many security mechanisms have been adopted to ensure the | [1] | M. | Meeker, | “INTERNET | TRENDS | 2015 | – | CODE |  |  |  |  |
| security of mobile payment. However, mobile payment also | CONFERENCE,” 2015. |  |  |  |  |  |  |  |  |  |  |  |
| faces security challenges such as malware detection, multi- | [2] | Forrester, “Forrester Forecast: Mobile Payments To Reach |  |  |  |  |  |  |  |  |  |  |
| factor | authentication, | data | breach | prevention, | and | fraud | $90B | By | 2017,” | 2013. | [Online]. | Available: |
| detection and protection. | https://www.forrester.com/Forrester+Forecast+Mobile+P |  |  |  |  |  |  |  |  |  |  |  |
| A. | Malware Detection | ayments+To+Reach+90B+By+2017/-/E-PRE4544. |  |  |  |  |  |  |  |  |  |  |

security. Many cautions have been used to detect and prevent

propagate on mobile devices [17]. Mobile malware detection is

a challenging issue [18]. Existing malware detection methods

include mobile forensic, static analysis, dynamic analysis, etc.

However, none of them are effective to detect malware on

mobile devices. Effective malware detection method is desired.

Mobile payment systems may use multi-factor

authentication process.

C. Data Breach Prevention

Data breach may occur. In an incident of a data breach,

is at risk. It may also cause identity theft.

everywhere. This also allows criminals to use mobile payment

cards or compromised mobile payment accounts to steal money

or make fraudulent transactions. When a fraudulent transaction

happens, it must be detected and prevented. If a user has

financial loss due to fraud, a clear definition of mobile payment

assurance policy may help the user build confidence to use a

mobile payment system.

VI. SUMMARY

Mobile payment has gained its popularity in many regions

due to its convenience. However, it also faces many threats and

detection and prevention. To remediate mobile payment risks,

mobile payment users and service providers both need to take

security measures to protect data security and prevent data

breaches.

5

[3] Intuit, “The History of Money and Payments,” 2015.

money-and-payments/.

Documents.” [Online]. Available:

https://www.pcisecuritystandards.org/index.php.

[5] Target, “Response & resources related to Target’s data

breach,” 2014. .

[6] HomeDepot, “The Home Depot Reports Findings in

[7] Y. Wang, K. Streff, and S. Raman, “Smartphone Security

2012, pp. 41–62.

[9] D. Yin, “Tencent’s WeChat Sends 1 Billion Virtual Red

Envelopes On New Year's Eve,” Forbes , 2015. [Online].

Available:

years-eve/.

http://www.boku.com/about/.

e-Money,” 2014.

Principles and Practice , 6th Editio. Pearson, 2013.

[13] Symantec, “Internet Security Threat Report,” 2015.

[14] Codenomicon, “The Heartbleed Bug,” 2014. [Online].

Available: http://heartbleed.com/.

[15] HomeDepot, “The Home Depot Reports Findings in

Payment Data Breach Investigation,” 2014. [Online].

Available:

https://corporate.homedepot.com/MediaCenter/Document

s/Press Release.pdf.

| Malware is one of the main concerns of mobile payment | [Online]. Available: http://payments.intuit.com/history-of- |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| malware spreading. However, malware still finds a way to | [4] | PCI | Security | Standards | Council, | “PCI | Standards | and |
| B. | Multi-factor Authentication | Payment Data Breach Investigation,” 2014. . |  |  |  |  |  |  |
| authentication to prevent user fraud when a user signs into the | Challenges,” | Computer (Long. Beach. Calif). | , vol. 45, no. |  |  |  |  |  |
| service using a new mobile device. Users are required to enter | 12, pp. 52–58, Dec. 2012. |  |  |  |  |  |  |  |
| an authentication code which is distributed to the user using | [8] | M. Blochlinger, “Mobile Payment Systems,” in | Internet |  |  |  |  |  |
| another communication channel, e.g., emails. However, mobile | Economics VI - Technical Report No. IFI-2012.02 | , B. |  |  |  |  |  |  |
| devices could also be lost or stolen. Malicious users may have | Stiller, K. Farkas, F. Hecht, G. S. Machado, P. Poullie, F. |  |  |  |  |  |  |  |
| access to the email account and thus spoof the multi-factor | Santos, C. Tsiaras, A. Vancea, and M. Waldburger, Eds. |  |  |  |  |  |  |  |
| sensitive information such as mobile phone numbers, credit | http://www.forbes.com/sites/davidyin/2015/02/19/tencent |  |  |  |  |  |  |  |
| card accounts, and purchase records are exposed. User privacy | s-wechat-sends-1-billion-virtual-red-envelopes-on-new- |  |  |  |  |  |  |  |
| D. | Fraud Detection and Protection | [10] boku, “We Care About Payments.” [Online]. Available: |  |  |  |  |  |  |
| Mobile payment provides payment services at any time from | [11] Boku, “The Future of Direct Carrier Billing in Europe and |  |  |  |  |  |  |  |
| services for their benefits. Criminals may use stolen payment | [12] W. | Stallings, | Cryptography | and | Network | Security: |  |  |
| security challenges. Malware is one of the main threats to a | [16] NCCIC, | “Backoff: | New | Point | of | Sale | Malware.” |  |
| mobile payment system. Mobile payment users need to increase | Department of Homeland Security, pp. 1–10, 2014. |  |  |  |  |  |  |  |
| security awareness to prevent malware on mobile devices. | [17] Apple, “XcodeGhost Q&A,” 2015. [Online]. Available: |  |  |  |  |  |  |  |
| SSL/TLS vulnerabilities and data breaches are two other main | http://www.apple.com/cn/xcodeghost/. |  |  |  |  |  |  |  |
| concerns of mobile payment security. Mobile payment also | [18] Y. Wang and Y. Alshboul, “Mobile Security Testing |  |  |  |  |  |  |  |
| faces security challenges such as malware detection, multi- | Approaches and Challenges,” in | First Conference On |  |  |  |  |  |  |
| factor | authentication, | data | breach | prevention, | and | fraud | Mobile And Secure Services | , 2015. |

