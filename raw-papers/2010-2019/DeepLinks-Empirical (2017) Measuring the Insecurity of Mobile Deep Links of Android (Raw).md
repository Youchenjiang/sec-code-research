---
title: "V_M_Liu_Measuring_Insecurity"
pages: 19
---

# V_M_Liu_Measuring_Insecurity

> **總頁數**：19 頁

---

## Page 1

Measuring the Insecurity of

Mobile Deep Links of Android

Fang Liu, Chun Wang, Andres Pico, Danfeng Yao, and Gang Wang, Virginia Tech

https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/liu

This paper is included in the Proceedings of the

26th USENIX Security Symposium

August 16–18, 2017 • Vancouver, BC, Canada

ISBN 978-1-931971-40-9

Open access to the Proceedings of the

26th USENIX Security Symposium

is sponsored by USENIX

*[Image: Page 1 Image]*

*[Image: Page 1 Image]*

---

## Page 2

Measuring the Insecurity of Mobile Deep Links of Android

Fang Liu, Chun Wang, Andres Pico, Danfeng Yao, Gang Wang

Department of Computer Science, Virginia Tech

{ fbeyond, wchun, andres, danfeng, gangwang } @vt.edu

Abstract launch apps from websites with preloaded context , which

Mobile deep links are URIs that point to specific loca-

tions within apps, which are instrumental to web-to-app

communications. Existing “scheme URLs” are known to

have hijacking vulnerabilities where one app can freely

register another app’s schemes to hijack the communi-

cation. Recently, Android introduced two new meth-

ods “App links” and “Intent URLs” which were designed

worsen the situation. First, App links apply link verifica-

tion to prevent hijacking. However, only 194 apps (2.2%

out of 8,878 apps with App links) can pass the verifica-

tion due to incorrect (or no) implementations. Second,

we identify a new vulnerability in App link’s preference

setting, which allows a malicious app to intercept arbi-

trary HTTPS URLs in the browser without raising any

alerts. Third, we identify more hijacking cases on App

links than existing scheme URLs among both apps and

websites. Many of them are targeting popular sites such

as online social networks. Finally, Intent URLs have lit-

tle impact in mitigating hijacking risks due to a low adop-

tion rate on the web.

1 Introduction

becomes instrumental to many key user experiences. For

instance, from a restaurant’s home page, users can tap a

hyperlink to launch the phone app and call the restaurant,

or launch Google Maps for navigation. Recently, users

can even search in-app content with a web-based search

engine ( e.g. , Google) and directly launch the target app

by clicking the search result [5].

Threats to Mobile Deep Links. Despite the conve-

nience, researchers have identified serious security vul-

nerabilities in scheme URLs [18, 19, 55]. The most sig-

nificant one is link hijacking , where one app can register

another app’s scheme and induce the mobile OS to open

the wrong app. Fundamentally, link hijacking is possi-

ble because there is no restriction on what schemes apps

can register. A malicious app may register “ fb ” to hijack

the deep link request to the Facebook app to launch it-

self. This allows the malicious apps to perform phishing

attacks ( e.g. , displaying a fake Facebook login box) or

steal sensitive data carried by the link ( e.g. , PII) [19, 35].

Even though Android and iOS may prompt users be-

fore launching an app, there are many cases where such

prompting is skipped without user knowledge.

Recently, two new deep link mechanisms were pro-

| with security features, to replace scheme URLs. While | The key enabler of web-to-mobile communication is |  |  |
| --- | --- | --- | --- |
| the new mechanisms are secure in theory, little is known | mobile deep links. Like web URLs, mobile deep links |  |  |
| about how effective they are in practice. | are universal resource identifiers (URI) for content and |  |  |
| In this paper, we conduct the first empirical measure- | functions within apps [49]. The most widely used deep |  |  |
| ment on various mobile deep links across apps and web- | link is | scheme URL | supported by both Android [7] and |
| sites. Our analysis is based on the deep links extracted | iOS [3] since 2008. If an app wants to be launched from |  |  |
| from two snapshots of 160,000+ top Android apps from | the web, the app can register URI schemes to the mobile |  |  |
| Google Play (2014 and 2016), and 1 million webpages | OS during installation. For example, the Facebook app |  |  |
| from Alexa top domains. We find that the new linking | registers “ | fb://profile | ” to open user profiles. Later |
| methods (particularly App links) not only failed to de- | when the link “ | fb://profile/user1 | ” is clicked on the |
| liver the security benefits as designed, but significantly | web, OS then can direct users to the Facebook app. |  |  |
| With the wide adoption of smartphones, mobile websites | posed to address the security risks in scheme URLs: |  |  |
| and native apps have become the two primary interfaces | App link and Intent URL. 1) | App Link | [6, 9] was in- |
| to access online content [10, 44]. Today, a user can easily | troduced to Android and iOS in 2015. | It no longer al- |  |
| USENIX Association | 26th USENIX Security Symposium | 953 |  |

---

## Page 3

| lows developers to customize schemes, but exclusively | to server misconfigurations, including popular apps such |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| uses HTTP/HTTPS scheme. To prevent hijacking, App | as Airbnb. |  |  |  |  |  |  |  |
| links introduced a way to verify the app-to-link associa- | Second, | we | uncover | a | new | vulnerability | in | App |
| tion. More specifically, mobile OS verifies a registered | links, which allows malicious apps to | stealthily | intercept |  |  |  |  |  |
| link ( | e.g. | , | https://facebook.com/profile | ) by con- | HTTP/HTTPS URLs in the browser. The root cause is |  |  |  |
| tacting the corresponding web host ( | facebook.com | ) for | that Android grants excessive permissions to unverified |  |  |  |  |  |
| verification. This prevents apps other than Facebook to | App links through the preference setting. For an unver- |  |  |  |  |  |  |  |
| claim this link. | 2) | Intent URL | [2] is another solution | ified App link, Android by default will prompt users to |  |  |  |  |
| introduced in 2013, which only works on Android. In- | choose between the app and the browser. To disable pro- |  |  |  |  |  |  |  |
| tent URL defines how deep links should be called by | moting, users may set a “preference” to always use the |  |  |  |  |  |  |  |
| websites. | Instead of calling “ | fb://profile | ”, Intent | app for this link. This preference is overly permissive, |  |  |  |  |
| URL explicitly specifies the destination app identifier | since it not only disables prompting for the current link, |  |  |  |  |  |  |  |
| ( | i.e. | , package name) in the parameter to avoid confusion. | but all other unverified links registered by the app. | A |  |  |  |  |

malicious app, once received preference, can hijack any

| Measurements. | While most existing works focus | sensitive HTTP/HTTPS URLs ( | e.g. | , to a bank website) |  |
| --- | --- | --- | --- | --- | --- |
| on vulnerabilities in scheme URLs [18, 19, 55], little is | without alerting users. We validate this vulnerability in |  |  |  |  |
| known about how widely App links and Intent URLs | the latest Android 7.1.1. |  |  |  |  |
| are adopted, and how effective they are in mitigating | Third | , We detect more malicious hijacking attacks |  |  |  |
| the threat in practice. | In this paper, we conduct the | on App links (1,593 apps) than scheme URLs (893 |  |  |  |
| first large-scale measurement on the current ecosystem of | apps). | Case studies show that popular websites ( | e.g. | , |  |
| mobile deep links. Our goal is to detect and measure link | “ | google.com | ”) and apps ( | e.g. | , Facebook) are common |
| hijacking vulnerabilities across the web and mobile apps, | targets for traffic hijacking. In addition, we identify sus- |  |  |  |  |
| and understand the effectiveness of new linking mecha- | picious apps that act as the man-in-the-middle between |  |  |  |  |
| nisms in battling hijacking attacks. | websites and the original app to record sensitive URLs |  |  |  |  |
| We perform extensive measurements on a large col- | and the parameters ( | e.g. | , “ | https://paypal.com | ”). |
| lection of mobile apps and websites. | To measure the | Finally | , Intent URLs have very limited impact in miti- |  |  |
| adoption of different mobile deep links, we collected two | gating hijacking risks due to the low adoption rate among |  |  |  |  |
| snapshots of 160,000+ most popular Android apps from | websites. Only 452 websites out of the Alexa top 1 mil- |  |  |  |  |
| Google Play in 2014 and 2016, and crawled 1 million | lion contain Intent URLs (0.05%), which is a much lower |  |  |  |  |
| web pages (using a dynamic crawler) from Alexa top do- | ratio than that of App links (48.0%) and scheme URLs |  |  |  |  |
| mains. We primarily focus on Android for its significant | (19.7%). Meanwhile, among these websites, App links |  |  |  |  |
| market share (87%) [29] and availability of apps. | We | drastically increase the number of links that have hijack- |  |  |  |
| also perform a subset of analysis on iOS deep links. At | ing risks compared to existing vulnerable scheme URLs |  |  |  |  |
| the high-level, our method is to extract the link regis- | To the best of our knowledge, our study is the first |  |  |  |  |
| tration entries (URIs) from apps, and then measure their | empirical measurement on the ecosystem of mobile deep |  |  |  |  |
| empirical usage on websites. To detect hijacking attacks, | links across web and apps. We find the new linking meth- |  |  |  |  |
| we group apps that register the same URIs as link colli- | ods not only fail to deliver the security benefits as de- |  |  |  |  |
| sion groups. We find that not all link collisions are ma- | signed, but significantly worsen the situation. There is a |  |  |  |  |
| licious — certain links are expected to be shared such | clear mismatch between the security design and practical |  |  |  |  |
| as links for common functionality ( | e.g. | , “ | tel | ”) or third- | implementations due to the lack of incentives of develop- |
| party libraries ( | e.g. | , “ | zxing | ”). We develop methods to | ers, developer mistakes, and inherent vulnerabilities in |
| identify malicious hijacking attempts. | the link mechanism. Moving forward, we propose a list |  |  |  |  |

of suggestions to mitigate the threat. We have reported

| Findings. | Our study has four surprising findings, | the over-permission vulnerability to the Google Android |  |
| --- | --- | --- | --- |
| which lead to one overall conclusion: the newly intro- | team. The detailed plan for further notification and risk |  |  |
| duced deep link solutions not only fail to improve secu- | mitigation is described in | § | 8. |

rity, but significantly increase hijacking risks for users.

First, App links’ verification mechanism fails in prac- 2 Background and Research Goals

tice. Surprisingly, among 8,878 Android apps with App

| links, only 194 (2.2%) correctly implement link verifica- | Mobile deep links are URIs that point to specific loca- |  |
| --- | --- | --- |
| tion. The reasons are a combination of the lack of mo- | tions within mobile apps. Through deep links, websites |  |
| tivation from app developers and various developer mis- | can initiate useful interactions with apps, which is instru- |  |
| takes. We confirm a subset of mistakes in iOS App links | mental to many key user experiences, for example, open- |  |
| too: 1,925 out of 12,570 (15%) fail the verification due | ing apps, sharing and bookmarking in-app pages [49], |  |
| 954 | 26th USENIX Security Symposium | USENIX Association |

---

## Page 4

| Mobile Phone | Mobile Phone |
| --- | --- |
| Browser ⁄ Webview | foo.com |

| Scheme URL: | foo://p |
| --- | --- |
| Implicit intent | App |

bar

App Link: https://foo.com/p Implicit intent

Intent URL: App

foo

foo;package=com.foo;end

URL, App Link and Intent URL.

App Link: http://facebook.com/profile/1234

scheme host path

2.1 Mobile Deep Links

during installation. The URIs are declared in the in

the “data” field of intent filters . 2) Addressing: when

“ foo:// ” is clicked, mobile OS will search all the intent

filters for a potential match. Since the link matches the

URI of app “ foo ”, mobile OS will launch this app.

2 Get https://foo.com/assetlinks.json

Mobile OS

4 Verify 3 Return assetlinks.json

1 Register

| https://foo.com/* | assetlinks.json |
| --- | --- |
| foo | https://foo.com/* |

schemes and URIs for their app without any restriction.

Prior research has pointed out key security risks in

scheme URLs [19, 55], given that any app can register

book can also register “ fb:// ”. When a deep link is

box), or stealing sensitive data in the request [19, 35].

With an awareness of this risk, Android lets users be

the security guard. When multiple apps declare the same

scheme.

Figure 3 shows the App link association process. Sup-

pose app “ foo ” wants to register “ http://foo.com/* ”.

Mobile OS will contact the server at “ foo.com ” for ver-

ification. The app’s developer needs to set up an associ-

ation file “assetlinks.json” beforehand under the root di-

file must be hosted on an HTTPS server. If the file

| intent://p#Intent;scheme= | Explicit intent | App | app: foo |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Figure 1: | Three types of mobile deep links: | Scheme | Figure 3: App link verification process. |  |  |  |  |  |
| Scheme URL: | fb://profile/1234 | and iOS 2.0 [3] in 2008. | Figure 2 shows the syntax |  |  |  |  |  |
| scheme host | path | of a scheme URL. App developers can customize any |  |  |  |  |  |  |
| Figure 2: URI syntax for Scheme URLs and App links. | other apps’ schemes. For example, apps other than Face- |  |  |  |  |  |  |  |
| and searching in-app content using search engines [5]. In | clicked, it triggers an “implicit intent” to open any app |  |  |  |  |  |  |  |
| the following, we briefly introduce how deep links work | with a matched URI. This allows a malicious app to hi- |  |  |  |  |  |  |  |
| and the related security vulnerabilities. Then we describe | jack the request to the Facebook app to launch itself, ei- |  |  |  |  |  |  |  |
| our research goals and methodology. | ther for phishing ( | e.g. | , displaying a fake Facebook login |  |  |  |  |  |
| To understand how deep links work, we first introduce | URI, users will be prompted (with a dialog box) to se- |  |  |  |  |  |  |  |
| inter-app communications on Android. An Android app | lect/confirm their intended app. | However, if the mali- |  |  |  |  |  |  |
| is essentially a package of software | components | . | One | cious app is installed but the victim app is not, the mali- |  |  |  |  |
| app’s components can communicate with another app’s | cious app will automatically skip the prompting and hi- |  |  |  |  |  |  |  |
| components through | Intent | , a messaging object charac- | jack the link without user knowledge. Even when both |  |  |  |  |  |
| terized “action”, “category” and “data”. By sending an | apps are installed, the malicious app may trick users to |  |  |  |  |  |  |  |
| intent, one app can communicate with the other app’s | set itself as the “preference” and disable prompting. His- |  |  |  |  |  |  |  |
| front-end | Activities | , or background | Services | , | Content | torically speaking, relying on end-users as the sole secu- |  |  |
| Providers | and | Broadcast Receivers | . | rity defense is risky since users often fail to perceive the |  |  |  |  |
| Mobile deep links trigger a particular type of intent | nature of an attack, leading to bad decisions [12, 22, 53]. |  |  |  |  |  |  |  |
| to enable communications between the web and mobile | Solution1: App Link. | App Link was introduced |  |  |  |  |  |  |
| apps. As shown in Figure 1, after users click on a link | recently in October 2015 to Android 6.0 [6] as a more |  |  |  |  |  |  |  |
| in the browser (or in-app WebView), the browser sends | secure version of deep links. | It was designed to pre- |  |  |  |  |  |  |
| an intent to invoke the corresponding component in the | vent hijacking with two mechanisms. First, the authen- |  |  |  |  |  |  |  |
| target app. | Unlike app-to-app communication, mobile | tic app can build an association with the correspond- |  |  |  |  |  |  |
| deep link can only launch front-end Activity in the app. | ing website, which allows the mobile OS to open the |  |  |  |  |  |  |  |
| Mobile deep links work in two simple steps: 1) Reg- | App link exclusively using the authentic app. | Second, |  |  |  |  |  |  |
| istration: | an app “ | foo | ” should first register its URIs | App link no longer allows developers to customize their |  |  |  |  |
| (“ | foo:// | ” or “ | https://foo.com | ”) to the mobile OS | own schemes, but exclusively uses the | http | or | https |
| 2.2 | Security Risks of Deep Linking | rectory (“/.well-known/”) of the | foo.com | server. | This |  |  |  |
| Hijacking Risk in Scheme URL. | Scheme URL is | contains an entry that certifies that app “ | foo | ” is asso- |  |  |  |  |
| the first generation of mobile deep links, and is the least | ciated with the link “ | http://foo.com/* | ”, the mobile |  |  |  |  |  |
| secure one. | It was introduced since Android 1.0 [7] | OS will confirm the association. | The association file |  |  |  |  |  |
| USENIX Association | 26th USENIX Security Symposium | 955 |  |  |  |  |  |  |

---

## Page 5

| contains a field called “ | sha256 cert fingerprints | ”, | Link | Conditions | Prompt |  |
| --- | --- | --- | --- | --- | --- | --- |
| which is the SHA256 fingerprint of the associated app’s | Type | > | 1 | Set As | Link | User? |
| signing certificate. | The mobile OS is able to verify | Apps | Preference | Verified |  |  |
| the fingerprint and prevent hijacking because only the | 3 | 7 | / | 3 |  |  |

authentic app has the corresponding signing certificate.

Suppose a malicious app “ bar ” also wants to register

“ http://foo.com/* ”, the verification will fail, assum-

tion process. The association file for iOS is “apple-app-

site-association”. However, iOS and Android have dif-

ferent policies to handle failed verifications . iOS pro-

hibits opening unverified universal links in apps. An-

droid, however, leaves the decision to users: if an unver-

ified link is clicked, Android prompts users to choose if

they want to open the link in the app or the browser.

“ intent://p/#Intent;scheme=foo;package=com

.foo;end ” where the package name of the target app is

explicitly specified. Package name is a unique identifier

for an Android app. Clicking an intent URL will launch

an “explicit intent” to open the specified app.

Compared to scheme URLs and App links, Intent URL

does not need special URI registration on the app. Intent

URL can invoke the same interfaces defined by the URIs

of scheme URLs or App links, as well as other exposed

components [2].

While the hijacking risk of scheme URLs has been re-

ported by existing research [18, 19, 55], little is known

about how prevalently this risk exists among apps, and

how effective the new mechanisms (App links and Intent

URLs) are in reducing this risk in practice. We hypothe-

size that upgrading from scheme URL to App link/Intent

URL is a non-trivial task, considering that scheme URLs

may already have significant footprints on the web. Mo-

bile platforms might be able to enforce changes to apps

through OS updates, but their influence on the web is

likely less significant. In this paper, we conduct the first

large-scale measurement on the mobile deep link ecosys-

tem to understand the adoption of different linking meth-

ods and their effectiveness in battling hijacking threats.

| Scheme | 3 | 3 | / | 7 |
| --- | --- | --- | --- | --- |
| URL | 7 | 7 | / | 7 |
| 7 | 3 | / | 7 |  |
| / | 7 | 7 | 3 |  |

Table 1: Conditions for whether users will be prompted

after clicking a deep link on Android. ∗ App Links always

have at least one matched app, the mobile browser.

when a malicious app registers the URI that belongs to

the victim app. If mobile OS redirects the user to the

malicious app, it can lead to phishing ( e.g. , the malicious

not malicious.

The Role of Users. Users also play a role in this

threat model. After clicking on a deep link, a user may

be prompted with a dialog box to confirm the destination

app. As shown in Table 1, prompting can be skipped in

many cases. For scheme URLs , a malicious app can skip

prompting if the victim app is not installed, or by trick-

ing users to set the malicious app as the “preference”.

App link can skip prompting if the link has been verified.

Otherwise, users will be prompted to choose between the

browser and the app. Intent URLs will not prompt users

Our Goals. Our study seeks to answer key ques-

tions regarding how mobile deep links are implemented

in the wild and their security impact. We ask three sets of

questions. First , how prevalently are different deep links

adopted among apps over time? Are App links and Intent

URLs implemented properly as designed? Second , how

many apps are still vulnerable to hijacking attacks? How

many vulnerable apps are exploited by other real-world

apps? Third , how widely are hijacked links distributed

among websites? How much do App links and Intent

URLs contribute to mitigating such links?

To answer these questions, we first describe data col-

lection ( § 3), and measure the adoption of App links and

scheme URLs among apps ( § 4). We perform extensive

security analyses to understand how effective App links

| ing the attacker cannot access the root of | foo.com | server | App | / | 3 | 7 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| to modify the association file and the fingerprint. | Link | ∗ | / | 7 | 3 | 7 |  |
| The iOS version of App links is called universal link, | / | 3 | 3 | 7 |  |  |  |
| introduced at iOS 9.0 [9], which has the same verifica- | Intent URL | / | / | / | 7 |  |  |
| Solution 2: | Intent URL. | Intent URL was intro- | app displays forged UI to lure user passwords) or data |  |  |  |  |
| duced in 2013 and only works on Android [2]. | Intent | leakage ( | e.g. | , the deep link may carry sensitive data in the |  |  |  |
| URLs prevent hijacking by changing how the deep link | URL parameters such as PII and session IDs) [19, 35]. In |  |  |  |  |  |  |
| is called on the website. | As shown in Figure 1, in- | this threat model, mobile OS and browser (or WebView) |  |  |  |  |  |
| stead of calling “ | foo://p | ”, Intent URL is structured as | are not the targets of the attack, and we assume they are |  |  |  |  |
| 2.3 | Research Questions | at all since the target app is explicitly specified. |  |  |  |  |  |
| Threat Model. | Our study focuses on | link hijack- | can prevent hijacking ( | § | 5), and then describe the method |  |  |
| ing threat | since this is the security issue that App Links | to detect hijacking attacks among apps ( | § | 6). Finally, we |  |  |  |
| and Intent URLs aim to address. Link hijacking happens | move to the web to measure the usage of Intent URLs, |  |  |  |  |  |  |
| 956 | 26th USENIX Security Symposium | USENIX Association |  |  |  |  |  |

---

## Page 6

and the prevalence of hijacked links ( § 7). In § 8, we sum- websites to decide whether to use Intent URLs or scheme

marize key implications and discuss possible solutions. URLs to launch the app. We will examine the adoption

3 Datasets

We collected data from both mobile apps and websites,

including two snapshots of 160,000+ most popular An-

droid apps in 2014 and 2016, and web pages from Alexa

Mobile Apps. To examine deep link registration,

we crawled two snapshots of mobile apps from Google

Play. The first snapshot App2014 contains 164,322 most

popular free apps from 25 categories in December 2014

(crawled with an Android 4.0.1 client). In August 2016,

we crawled a second snapshot of top 160,000 free apps

using an Android 6.0.1 client. We find that 48,923 apps

in App2014 are no longer listed on the market in 2016.

4,963 apps in 2014 snapshot fell out of the top 160K list

in 2016. To match the two datasets, we also crawled

visit these web domains and load both static HTML page

4 Deep Link Registration by Apps

In this section, we start by analyzing mobile apps to un-

derstand deep link registration and adoption. In order to

receive deep link requests, an app needs to register its

URIs to mobile OS during installation. Our analysis in

this section focuses on Scheme URLs and App links. For

special registrations in the app. Instead, it is up to the

Intent URLs later by analyzing web pages ( § 7).

We provide an overview of deep link adoption by an-

alyzing 1) how widely the scheme URLs are adopted

among apps, and 2) whether App links are in the process

of replacing scheme URLs for better security.

Android apps register their URIs in the manifest file

( AndroidManifest.xml ). Both Scheme URLs and

App Links are declared in Intent filters as a set

of matching rules, which can either be actual links

( fb://login/ ) or a wild card ( fb://profile/* ).

Since there is no way to exhaustively obtain all links be-

hind a wild card, we treat each matching rule as a regis-

tration entry. Given a manifest file, we extract deep link

entries in three steps:

links, but link verification is not supported for these apps.

4.2 Scheme URL vs. App Link

Next, we compare the adoption of Scheme URLs and

App links across time, app categories and app popular-

ity. We seek to understand if the new App links are on

the way of replacing Scheme URLs.

gered by Intent URLs.

| top 1 million domains. | 4.1 | Extracting URI Registration Entries |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| these 4,963 apps in 2016, forming an | App2016 | dataset of | • | Step1: Detecting Open Interfaces. | We capture all |  |  |
| 164,963 apps. The two snapshots have 115,399 overlap- | the Activity intent filters whose “category” field con- |  |  |  |  |  |  |
| ping apps. For each app in | App2016 | , we also obtained | tains both | BROWSABLE | and | DEFAULT | . This returns |
| the developer information, downloading count, review | all the components that are reachable from the web. |  |  |  |  |  |  |
| count and rating. | • | Step2: | Extracting App Link. | Among intent fil- |  |  |  |
| Our app dataset is biased towards popular apps among | ters in Step 1, we capture those whose “action” con- |  |  |  |  |  |  |
| the 2.2 million apps in Google Play [48]. | Since these | tains | VIEW | . This returns intent filters with either App |  |  |  |
| popular apps have more downloads, potential vulnerabil- | Links or Scheme URLs in their “data” fields | 1 | . We ex- |  |  |  |  |
| ities could affect more users. Our result can serve as a | tract App Link URIs as those with http/https scheme. |  |  |  |  |  |  |
| lower bound of empirical risks. | Note that App Link intent filters have a special field |  |  |  |  |  |  |
| Alexa Top 1 Million Websites. | To understand deep | called | autoVerify | . If its value is TRUE, then mobile |  |  |  |
| link usage on the web, we crawled Alexa top 1 million | OS will perform verification on the App link. |  |  |  |  |  |  |
| domains [1] in October 2016. We simulate using an An- | • | Step3: | Extracting Scheme URL. | All the non- |  |  |  |
| droid browser (Android 6.0.1, Chrome/41/0/2272.96) to | http/https URIs from Step2 are Scheme URLs. |  |  |  |  |  |  |
| (index page) and the dynamic content from JavaScript. | We apply the above method to our dataset and the re- |  |  |  |  |  |  |
| This is done using modified OpenWPM [25], a head- | sult is summarized in Table 2. Among the 160K apps in |  |  |  |  |  |  |
| less browser-based crawler. | For each visit, the crawler | App2016 | , we find that 20.3K apps adopt scheme URLs |  |  |  |  |
| loads the web page and waits for 300 seconds allowing | and 8.9K apps adopt App links. Note that for the apps in |  |  |  |  |  |  |
| the page to load the dynamic content, or perform the redi- | App2014 | (Android 4.0 or lower), App Link had not been |  |  |  |  |  |
| rection. We store the final URL and HTML content. This | introduced to Android yet. | We find that 4,545 apps in |  |  |  |  |  |
| crawling is also biased towards popular websites, assum- | App2014 | register http/https URIs, which are essentially |  |  |  |  |  |
| ing that deep links on these sites are more likely to be | scheme URLs with “ | http | ” or “ | https | ” as the scheme. |  |  |
| encountered by users. We refer this dataset as | Alexa1M | . | For consistency, we still call these http/https links as App |  |  |  |  |
| Intent URLs, as described in | § | 2, developers do not need | 1 | The rest intent filters whose “action” is not | VIEW | can still be trig- |  |
| USENIX Association | 26th USENIX Security Symposium | 957 |  |  |  |  |  |

---

## Page 7

| Dataset | Total | Apps accept | Apps accept | Apps accept | Unique | Unique |
| --- | --- | --- | --- | --- | --- | --- |
| Apps | Scheme URLs | App Links | either Links | Schemes | Web Hosts |  |
| App2014 | 164,322 | 10,565 (6.4%) | 4,545 (2.8%) | 12,428 (7.6%) | 8,845 | 6,471 |
| App2016 | 164,963 | 20,257 (12.3%) | 8,878 (5.4%) | 23,830 (14.5%) | 18,839 | 18,561 |

Table 2: Two snapshots of Android apps collected in 2014 and 2016. 115,399 apps appear in the both datasets; 48,923

apps in App2014 are no longer listed on the market in 2016; App2016 has 49,564 new apps.

100 35 App Links App Categories. Among the 25 app cat-

80 30 Scheme URLs

25

40 15

10

| CDF of Apps (%) | 20 | Host |
| --- | --- | --- |
| 0 | Scheme | 5 |

Apps w/ Deep Links (%) 0

| # of New Schemes/Hosts per App | Download Count |
| --- | --- |
| Adoption over Time. | As shown in Table 2, there |

are significantly more apps that started to adopt deep

links from 2014 to 2016 (about 100% growth). However,

the growth rates are almost the same for App links and

Scheme URLs. There are still 2-3 times more apps using

scheme URLs than those with App links. Apps links are

far from replacing scheme URLs.

Figure 4 specifically looks at apps in both snapshots.

We select those that adopt either type of deep links in

either snapshot (13,538 apps), and compute the differ-

ences in their number of schemes/hosts between 2014

and 2016. We find that the majority of apps (over 96.2%)

either added more deep links or remained the same. Al-

most no apps removed or replaced scheme URLs with

App links. The conclusion is the same when we compare

the number of URI rules (omitted for brevity). This sug-

gests that scheme URLs are still heavily used, exposing

users to potential hijacking threat.

App Popularity. We find that deep links are

more commonly used by popular apps (based on down-

load count). In Figure 5, we divide apps in 2016 into

[ 1 K , 1 M ) , [ 1 M , ∞ ) . Each has 20,654, 127,323 and 5,223

users.

egories, we find that the following categories

PING (25.5%), SOCIAL (23.4%), LIFESTYLE

(21.0%), NEWS AND MAGAZINES (20.5%) and

content-heavy and often handle user personally identifi-

5 Security Analysis of App Links

Our result shows that App links are still not as popular

as scheme URLs. Then for apps that adopt App links,

are they truly secure against link hijacking? As we dis-

cussed in § 2.2, App link was designed to prevent hijack-

ing through a link verification process. If a user clicks

on an unverified App link, the mobile OS will prompt

the user to choose whether he/she would like to open

the link in the browser or using the app. In the fol-

lowing, we empirically analyze the security properties of

App links in two aspects. First, we measure how likely

app developers make mistakes when deploying App link

verification. Second, we discuss a new vulnerability

we discovered which allows malicious apps to skip user

prompting when unverified App links are clicked. Ma-

licious apps can exploit this to stealthily hijack arbitrary

HTTP/HTTPS URLs in the mobile browser without user

knowledge.

lems have been fixed.

| 60 | 20 | have | the | highest | deep | link | adoption | rate: | SHOP- |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5-4-3-2-1 0 1 2 3 4 5 6 7 8 9 | 10 | [0, 1K) | [1K, 1M) | [1M, | ∞ | ) | TRAVEL AND LOCAL | (20.2%). | These | apps | are |
| Figure 4: # of new schemes | Figure 5: % of apps w/deep | able information ( | e.g. | , social network app) and financial |  |  |  |  |  |  |  |
| and app link hosts per app | links; apps are divided by | data ( | e.g. | , shopping app). Link hijacking targeting these |  |  |  |  |  |  |  |
| between 2014 and 2016. | download count. | apps could have practical consequences. |  |  |  |  |  |  |  |  |  |
| three buckets based on their download count: | [ | 0 | , | 1 | K | ) | , | 5.1 | App Link Verification |  |  |
| apps respectively. Then we calculate the percentage of | We start by examining whether | link verification | truly |  |  |  |  |  |  |  |  |
| apps that adopt deep links in each bucket. We observe | protects apps from hijacking attacks. Since App link has |  |  |  |  |  |  |  |  |  |  |
| that 33% of the 5,223 most popular apps adopt scheme | not been introduced for | App2014 | , all the http/https links |  |  |  |  |  |  |  |  |
| URL, and the adoption rate goes down to 8% for apps | in 2014 were unverified. In the following, we focus on |  |  |  |  |  |  |  |  |  |  |
| with | < | 1K downloads. The trend is similar for App links. | apps in | App2016 | . In total, there are 8,878 apps that regis- |  |  |  |  |  |  |
| In addition, we find that apps | with | deep links have aver- | ter App links, involving 18,561 unique web domains. We |  |  |  |  |  |  |  |  |
| agely 4 million downloads per app, which is orders of | crawled two snapshots of the association files for each |  |  |  |  |  |  |  |  |  |  |
| magnitude higher than apps | without | deep links (125K | domain in January and May of 2017 respectively. | We |  |  |  |  |  |  |  |
| downloads per app). As deep links are associated with | use the January snapshot to discuss our key findings, and |  |  |  |  |  |  |  |  |  |  |
| popular apps, potential vulnerabilities can affect many | then use the May snapshot to check if the identified prob- |  |  |  |  |  |  |  |  |  |  |
| 958 | 26th USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |  |  |

---

## Page 8

| Date | Apps w/ | Apps Verif. | Apps | Apps with Failed Verifications | ∗ |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| App Links | Turned On | Verified | App | Host w/o | Host w/ | Wrong | Host | Host Assoc. |  |
| Misconfig. | Assoc. F. | HTTP | Path | Invalid F. | Other apps |  |  |  |  |
| Jan.17 | 8,878 | 415 | 194 | 26 | 177 | 11 | 0 | 10 | 60 |
| May.17 | 8,878 | 415 | 192 | 26 | 171 | 8 | 0 | 18 | 57 |

Table 3: App Link verification statistics and common mistakes (App2016) based on data from January 2017 and May

2017. ∗ One app can make multiple mistakes.

Type Date Hosts w/ Assoc. F.

Jan.17 12,570

iOS

| May.17 | 13,541 |
| --- | --- |
| Jan.17 | 1,833 |

Android

May.17 2,779

cessfully pass the verification (2%). More specifically,

only 415 apps (4.7%) set the “ autoVerify ” field as TRUE,

which triggers the verification process during app instal-

lation. This means the vast majority of apps (8,463,

95.3%) do not even start the verification process. Inter-

estingly, 434 apps actually have the association file ready

on their web servers, but the developers seem to forget to

configure the apps to turn on the verification.

not certify this app. We tested the app on our phone,

which indeed failed the verification.

In May 2017, we check all the apps again and find that

| Under HTTP | Wrong Path | Invalid File |
| --- | --- | --- |
| 1,817 (14%) | 0 (0%) | 108 (1%) |
| 1,820 (13%) | 0 (0%) | 113 (.8%) |
| 330 (18%) | 4 (.2%) | 81 (4%) |
| 474 (17%) | 0 (0%) | 118 (4%) |

the association files.

Misconfigurations for iOS and Android. To show

that App links verification can be easily misconfigured,

we put together 1,012,844 web domains to scan their as-

sociation files. These 1,012,844 domains is a union of

Alexa top 1 million domains and the 18,561 domains ex-

tracted from our apps. We scan the association files for

both Android and iOS.

5.2 Over-Permission Vulnerability

Table 4: Association files for iOS and Android obtained after scanning 1,012,844 domains.

| Failed Verifications. | As of January 2017, we find | more apps with an invalid association files in May com- |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a surprisingly low ratio of verified App links. | Among | pared to that of January. Manual examination shows that |  |  |  |  |  |  |
| 8,878 apps that register App Links, only 194 apps suc- | new mistakes are introduced when the developers update |  |  |  |  |  |  |  |
| Even for apps that turn on the verification, only 194 | As of January 2017, 12,570 domains (out 1 million) |  |  |  |  |  |  |  |
| out of 415 can successfully complete the process as of | have iOS association files and only 1,833 domains have |  |  |  |  |  |  |  |
| January 2017. Table 3 shows the common mistakes of | Android association files (Table 4). | It is unlikely that |  |  |  |  |  |  |
| the failed apps (one app can have multiple mistakes). | there are 10x more iOS-exclusive apps. | A more plau- |  |  |  |  |  |  |
| More specifically, 26 apps incorrectly set the App link | sible explanation is iOS developers are more motivated |  |  |  |  |  |  |  |
| ( | e.g. | , with a wildcard in the domain name), which is im- | to perform link verification, since iOS prohibits opening |  |  |  |  |  |
| possible for mobile OS to connect to. On the server-side, | unverified HTTP/HTTPS links in apps. In contrary, An- |  |  |  |  |  |  |  |
| 177 apps turn on the verification, but the destination do- | droid leaves the decision to users by prompting users to |  |  |  |  |  |  |  |
| main does not host the association file; 11 apps host the | choose between using apps or a browser. |  |  |  |  |  |  |  |
| file under an HTTP server instead of the required HTTPS | We | find | iOS | apps | also | have | significant | mis- |
| server; 10 apps’ files are in invalid JSON format; 60 | configurations. This analysis only covers a subset of pos- |  |  |  |  |  |  |  |
| apps’ association files do not contain the App link (or | sible mistakes compared to Table 3, but still returns a |  |  |  |  |  |  |  |
| the app) to be verified. Note that for these failed apps, | large number. As of January 2017, 1817 domains (14%) |  |  |  |  |  |  |  |
| we do not distinguish whether they are malicious apps | are hosting the association file under HTTP, and there |  |  |  |  |  |  |  |
| attempting to verify with a domain they do not own, or | are additional 108 domains (1%) with invalid JSON files. |  |  |  |  |  |  |  |
| simply mistakes by legitimate developers. | One example is the Airbnb’s iOS app. The app tries to |  |  |  |  |  |  |  |
| We confirm all these mistakes lead to failed verifica- | associate with “ | airbnb.com.gt | ”, which only hosts the |  |  |  |  |  |
| tions by installing and testing related apps on a phys- | association file under an HTTP server. This means users |  |  |  |  |  |  |  |
| ical phone. | We observe many of these mistakes are | will not be able to open this link in the Airbnb app. |  |  |  |  |  |  |
| made by popular apps from big companies. | For ex- | In May 2017, we scan these domains again. We ob- |  |  |  |  |  |  |
| ample, “ | com.amazon.mp3 | ” is Amazon’s official music | serve 7.7% of increase of hosts with association files for |  |  |  |  |  |
| app, which claims to be associated with “ | amazon.com | ”. | iOS and 51.6% increase for Android. However, the num- |  |  |  |  |  |
| However, the association file under | amazon.com | does | ber of misconfigured association files also increased. |  |  |  |  |  |
| most of the identified problems remain unfixed. More- | In addition to verification failures, we identify a new vul- |  |  |  |  |  |  |  |
| over, some apps introduce new mistakes: | there are 8 | nerability in the setting preferences for App links. Recall |  |  |  |  |  |  |
| USENIX Association | 26th USENIX Security Symposium | 959 |  |  |  |  |  |  |

---

## Page 9

| that unverified App links still have one last security de- | Discussion. | Fundamentally, this vulnerability is |  |  |  |
| --- | --- | --- | --- | --- | --- |
| fense — the end user. Android OS prompts users when | caused by the excessive permission to unverified App |  |  |  |  |
| unverified App links are clicked, and users can choose | links. | When setting preferences, the permission is not |  |  |  |
| between a browser and the matched app. We describe an | applied to the | link-level | , but to the | scheme-level | . We sus- |
| over-permission vulnerability | that allows malicious apps | pect that the preference system of App links is directly |  |  |  |
| to skip prompting for stealthy hijacking. | inherent from scheme URLs. | For scheme URLs, the |  |  |  |

Proof-of-Concept Attack. Suppose “ bar ” is a

malicious app that register both “ https://bar.com ”

and “ https://bank.com/transfer/* ”. The user

sets preference for using “ bar ” to open the link

“ https://bar.com ”, which is a normal action. Then

without user knowledge, the permission also applies to

Intent, and hands it over to the app bar . bar can then

change the recipient and use the session ID to transfer

money to the attacker. In this example, the attacker

sets the path of the URI as “ /transfer/* ” so that bar

would only be triggered during money transfer. The

app can make this even stealthier by quickly terminating

itself after the hijacking, and bouncing the user back to

the bank website in the browser.

preference is also set to the scheme level which makes

ble to this over-permission attack. In iOS, if the user sets

preference for one app to open an HTTPS link. The per-

mission goes to all the HTTPS links that the app has suc-

cessfully verified . The Android vulnerability is caused by

the fact that permission goes to unverified links.

tial hijacking attacks.

6 Link Hijacking

While many apps are vulnerable in theory, the real ques-

tion is how many vulnerable apps are exploited in prac-

tice? For a given app, how likely would other apps regis-

ter the same URIs ( a.k.a. , link collision)? Do link colli-

| Over-Permission through Preference Setting. | User | more sense ( | e.g. | , allowing the Facebook app to open all |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| prompting is there for better security, but prompting | “ | fb:// | ”). However, for App links, scheme-level permis- |  |  |  |  |  |
| users too much can hurt usability. | Android’s solution | sion means attackers can hijack any HTTP/HTTPS links. |  |  |  |  |  |  |
| is to take a middle ground using “preference” setting. | To successfully exploit this vulnerability, a malicious |  |  |  |  |  |  |  |
| When an App link is clicked, users can set “preference” | app needs to trick users to set the preference ( | e.g. | , using |  |  |  |  |  |
| for always opening the link in the native app without | benign functionalities). | For example, an attacker may |  |  |  |  |  |  |
| prompting again. | We find that the preference setting | design a recipe app that allows users to open recipe web |  |  |  |  |  |  |
| gives excessive permissions. Specifically, the preference | links in the app for an easy display and sharing. | This |  |  |  |  |  |  |
| not only disables the prompting for the current link that | recipe app can ask users to set the preference for opening |  |  |  |  |  |  |  |
| the user sees, but all other (unverified) HTTP/HTTPS | recipe links but secretly registers an online bank’s App |  |  |  |  |  |  |  |
| links that this app register. For example, if the user sets | links to receive the same preference. We have filed a bug |  |  |  |  |  |  |  |
| preference for “ | https://bar.com | ”, all the links with | report through Google’s Vulnerability Reward Program |  |  |  |  |  |
| “ | https:// | ” in this app receive the permission. Exploit- | (VRP) in February 2017. We are currently working with |  |  |  |  |  |
| ing this vulnerability allows malicious apps to hijack any | the VRP team to mitigate the threat. |  |  |  |  |  |  |  |
| HTTP/HTTPS URLs without alerting users. | iOS has a similar preference setting, but not vulnera- |  |  |  |  |  |  |  |
| “ | https://bank.com/transfer/* | ”. | 5.3 | Summary of Vulnerable Apps |  |  |  |  |
| Later, | suppose | this | user | visits | her | bank’s | Thus far, our analysis shows that most apps are still vul- |  |
| website | in | a | mobile | browser, | and | trans- | nerable to link hijacking. | First, scheme URLs are still |
| fers | money | through | an | HTTPS | request | heavily used among apps. | Second, for apps that adopt |  |
| “ | https://bank.com/transfer?sessionid=8154& | App links, only 2% can pass the link verification. The |  |  |  |  |  |  |
| amount=1000& recipient=tom | ”. | Because | of | the | over-permission vulnerability described above makes the |  |  |  |
| preference setting, this request will automatically trigger | situation even worse. In 2016, out of all 23,830 apps that |  |  |  |  |  |  |  |
| bar | without prompting the user. The browser wraps up | adopt deep links, 23,636 apps either use scheme URLs |  |  |  |  |  |  |
| this URL and the parameters in plaintext to create an | or unverified App links. These are candidates of poten- |  |  |  |  |  |  |  |
| We validate this vulnerability in both Android 6.0.1 | sions always have a malicious intention? If not, how can |  |  |  |  |  |  |  |
| and 7.1.1 (the latest version). We implement the proof- | we classify malicious hijacking from benign collisions? |  |  |  |  |  |  |  |
| of-concept attack by writing a malicious Android app to | To answer these questions, we first measure how likely |  |  |  |  |  |  |  |
| hijack the author’s own blog website (instead of an actual | it is for different apps to register the same URIs. | Our |  |  |  |  |  |  |
| bank). | The attack is successful: the malicious app hi- | analysis reveals the key categories of link collisions, and |  |  |  |  |  |  |
| jacked the plaintext parameters in the URL, and quickly | we develop a systematic procedure to label all of them. |  |  |  |  |  |  |  |
| bounced the user back to the original page in the browser. | This analysis allows us to focus on the highly suspicious |  |  |  |  |  |  |  |
| The bouncing is barely noticeable by users. | groups that are involved in malicious hijacking. Finally, |  |  |  |  |  |  |  |
| 960 | 26th USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |

---

## Page 10

| 100 | 100 | Scheme | Apps | Web Host | Apps |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 95 | 95 | file | © | F | 1278 | google.com | © | P | 480 |
| 90 | 90 | content | © | F | 727 | google.co.uk | © | P | 441 |
| 85 | 85 | oauth | © | T | 520 | zxing.appspot.com | © | T | 410 |

| 80 | 80 |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CDF of Apps (%) | 75 | App2016 | CDF of Apps (%) | 75 | App2016 |  |  |
| 1 | 10 | 100 | 1000 | 1 | 10 | 100 | 1000 |

we present more in-depth case studies to understand the

risk of typical attacks.

6.1 Characterizing Link Collision

web hosts from 5,615 apps involved in link collisions.

The corresponding numbers for 2016 are higher: 697

Categorizing Link Collisions. We find that not all

lyzing these schemes and hosts, we categorize collisions

x-oauthflow-twitter © T 369 maps.google.com © P 187

twitter © T

| testshop | © | T | 278 | feeds.feedburner.com | © | T | 126 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tapatalk-byo | © | T | 180 | feedsproxy.google.com | © | T | 110 |

Table 5: Top 10 schemes and app link hosts with link col-

lisions in App2016. We manually label them into three

types: © F = Functional, © P = Per-App, © T = Third-party

by multiple apps. IANA [13] maintains a list of URI

sion).

and hosts are registered without much restriction—

| 70 | App2014 | 70 | App2014 | x-oauthflow-espn- | 359 | beautygirlsinc.com | © | P | 148 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # of Apps per Scheme | # of Apps per Web Host | zxing | © | T | 321 | triposo.com | © | P | 131 |  |  |  |  |
| Figure 6: | # of Collision apps | Figure 7: | # of Collision apps | shopgate-10006 | © | T | 278 | feeds2.feedburner.com | © | T | 123 |  |  |
| per scheme. | per web host. | geo | © | F | 238 | feedproxy.google.com | © | T | 112 |  |  |  |  |
| Links collision happens when two or more apps register | schemes, most of which are functional ones. | This |  |  |  |  |  |  |  |  |  |  |  |
| the same deep link URIs. When the link is clicked, it is | collision type does not apply to App links. |  |  |  |  |  |  |  |  |  |  |  |  |
| possible for mobile OS to direct users to the wrong app. | • | Per-app scheme/host (P) | is designated to an indi- |  |  |  |  |  |  |  |  |  |  |
| Note that simply matching “scheme” or app link “host” | vidual app. “ | maps.google.com | ” is to open Google |  |  |  |  |  |  |  |  |  |  |
| is not sufficient. | For example, “ | myapp://a/1 | ” and | Maps (but registered by 186 other apps) and “ | fb | ” is |  |  |  |  |  |  |  |
| “ | myapp://a/2 | ” do not conflict with each other since | supposed to open Facebook app (but registered by |  |  |  |  |  |  |  |  |  |  |
| they use different “paths” in the URI. To this end, we de- | 4 other apps). Collisions on per-app schemes/hosts |  |  |  |  |  |  |  |  |  |  |  |  |
| fine two apps have link collision only if there is at least | are often malicious, with the exception if all apps are |  |  |  |  |  |  |  |  |  |  |  |  |
| one link that is opened by both apps. | from the same developer. |  |  |  |  |  |  |  |  |  |  |  |  |
| Prevalence of Link Collisions. | To identify link col- | • | Third-party | scheme/host | (T) | is | used | by | third- |  |  |  |  |
| lision, we first group apps based on the scheme (scheme | party | libraries, | which | often | leads | to | (uninten- |  |  |  |  |  |  |
| URL) or web host (App links). | Figure 6 and Figure 7 | tional) link collision. | “ | x-oauthflow-twitter | ” |  |  |  |  |  |  |  |  |
| show the number of apps that each scheme/host is as- | is | a | callback | URL | for | Twitter | OAuth. | Twit- |  |  |  |  |  |
| sociated with. | About 95% of schemes are exclusively | ter | suggests | developers | defining | their | own | call- |  |  |  |  |  |
| registered by one single app. The percentage is slightly | back URL, but many developers copy-paste this |  |  |  |  |  |  |  |  |  |  |  |  |
| lower for App links (76%–82%). Then for each group, | scheme from an online tutorial (unintentional colli- |  |  |  |  |  |  |  |  |  |  |  |  |
| we filter out apps that have no conflicting URIs with any | sion). | “ | feedproxy.google.com | ” is from a third- |  |  |  |  |  |  |  |  |  |
| other apps in the group, and produce apps with link colli- | party RSS aggregator. Apps use this service to redi- |  |  |  |  |  |  |  |  |  |  |  |  |
| sions. Within | App2014 | , we identify 394 schemes, 1,547 | rect user RSS requests to their apps (benign colli- |  |  |  |  |  |  |  |  |  |  |
| schemes and 3,272 web hosts from 8,961 apps. | Because of the “shared” nature, functional schemes |  |  |  |  |  |  |  |  |  |  |  |  |
| Our result is a lower bound of actual collisions, biased | or third-party schemes/hosts are expected to be used by |  |  |  |  |  |  |  |  |  |  |  |  |
| towards popular apps. Schemes/hosts that are currently | multiple apps. Related link collisions are benign or un- |  |  |  |  |  |  |  |  |  |  |  |  |
| mapped to a single app might still have collisions with | intentional. In contrary, per-app schemes/hosts are (ex- |  |  |  |  |  |  |  |  |  |  |  |  |
| apps outside of our dataset. For the rest of our analysis, | pected to be) designated to each app, and thus link colli- |  |  |  |  |  |  |  |  |  |  |  |  |
| we focus on the more recent 2016 dataset. | sion can indicate malicious hijacking attempts. |  |  |  |  |  |  |  |  |  |  |  |  |
| collisions have malicious intention. After manually ana- | 6.2 | Detecting Malicious Hijacking |  |  |  |  |  |  |  |  |  |  |  |
| into 3 types. Table 5 shows the top 10 mostly registered | Next, we detect malicious hijacking by labeling | per-app |  |  |  |  |  |  |  |  |  |  |  |
| schemes/hosts and their labels. | schemes/hosts. | This task is challenging since schemes |  |  |  |  |  |  |  |  |  |  |  |
| • | Functional scheme (F) | is reserved for a common | it | is | difficult | to | tell | based | on | the | name | of | the |
| functionality, instead of a particular app. “ | file | ” is | scheme/host. | Our | The | high-level | intuition | is: | 1) |  |  |  |  |
| registered by 1,278 apps that can open files. “ | geo | ” | third-party schemes/hosts often have official documen- |  |  |  |  |  |  |  |  |  |  |
| is registered by 238 apps that can handle GPS coor- | tations | to | teach | developers | how | to | use | the | library, |  |  |  |  |
| dinates. These schemes are expected to be registered | which are searchable online; 2) functional schemes are |  |  |  |  |  |  |  |  |  |  |  |  |
| USENIX Association | 26th USENIX Security Symposium | 961 |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 11

| Deep Links | After Pre- |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Link Collisions | Functional | Third-party | Per-app |  |  |  |
| In Total | Processing |  |  |  |  |  |
| #Schemes (#Apps) | 18,839 (20,257) | 697 (7,432) | 376 (6,350) | 30 (2,135) | 197 (3,972) | 149 (893) |
| #Hosts (#Apps) | 18,561 (8,878) | 3,272 (2,868) | 2,451 (2,083) | N/A | 137 (999) | 2,314 (1,593) |

Table 6: Filtering and classification results for schemes and App link hosts (App2016).

well-documented in public URI standard. To these 100 100

ends, we develop a filtering procedure to label per-app 80 80

schemes/hosts. For any manual labeling tasks, we have

two authors perform the task independently, and a third

and 3,272 hosts (8,961 apps) that have link collisions in

schemes and 2,451 web hosts for further labeling.

All these hosts are not third-party hosts, which helps to

trim down to 471 hosts for manual labeling. We follow

the same intuition to label third-party web hosts by man-

Testing Automated Classification. Clearly manu-

ally labeling cannot scale. Now that we have obtained

| 60 | 60 |
| --- | --- |
| 40 | 40 |

Per-app

| CDF of Apps (%) | 20 | Third-party |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Functional | 0 | Third-party |  |  |  |  |
| 2 | 10 | 100 | 1000 | 2 | 10 | 100 | 1000 |

ing SVM and Random Forests classifiers return an accu-

6.3 Hijacking Results and Case Studies

per-app schemes and hosts are hijacked, we perform in-

depth cases studies on a number of representative attacks.

| person to resolve any disagreements. | CDF of Apps (%) | 20 | Per-app |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pre-Processing. | We start with the 697 schemes | # of Collision Apps per Scheme | # of Collision Apps per Host |  |  |  |  |  |  |
| App2016 | . We exclude schemes/hosts where all the colli- | Figure 8: | # of collision apps | Figure 9: | # of collision apps |  |  |  |  |
| sion apps are from the same developer. This leaves 376 | per scheme. | per host. |  |  |  |  |  |  |  |
| Classifying Schemes. | We label schemes in two steps. | racy of 59% (SVM) and 62% (RF). If we only focus on |  |  |  |  |  |  |  |
| The results are shown in Table 6. | First, we filter out | schemes that have a higher-level of collisions ( | e.g. | , | > | 4 |  |  |  |
| functional schemes. IANA [13] lists 256 common URI | developers), it returns a higher accuracy: 84% (SVM) |  |  |  |  |  |  |  |  |
| schemes, among which there are a few per-apps scheme | and 75% (RF). The accuracy is not high enough for prac- |  |  |  |  |  |  |  |  |
| under “provisional” status ( | e.g. | , “ | spotify | ”). We man- | tical usage. Intuitively, there are not many restrictions on |  |  |  |  |
| ually filter them out and get 175 standard functional | how developers register their URIs, and thus it is possible |  |  |  |  |  |  |  |  |
| schemes. Matching this list with our dataset returns 30 | that the patterns of per-app schemes are not that strong. |  |  |  |  |  |  |  |  |
| functional schemes with link collisions. Then, to label | Since fully automated classification is not yet feasi- |  |  |  |  |  |  |  |  |
| third-party schemes, we manually search for their doc- | ble, we then explore useful heuristics to help app mar- |  |  |  |  |  |  |  |  |
| umentations or tutorials online. | For certain third-party | ket admins to conduct collision auditing. We rank fea- |  |  |  |  |  |  |  |
| schemes, we also check the app code to be sure. In to- | tures based on the information gain, and identify top 3 |  |  |  |  |  |  |  |  |
| tal, we identify 197 third-party schemes, and the rest 149 | features: average number of apps from the same devel- |  |  |  |  |  |  |  |  |
| schemes are per-app schemes (also manually checked). | oper (apDev), number of unique no-prefix components |  |  |  |  |  |  |  |  |
| Figure 8 shows the number of collision apps for | (npcNum) and number of unique components (ucNum). |  |  |  |  |  |  |  |  |
| different schemes. | Not surprisingly, per-app schemes | Regarding apDev, the intuition is that developers are |  |  |  |  |  |  |  |
| have fewer collision apps than functional and third-party | likely to use a different per-app scheme for each of their |  |  |  |  |  |  |  |  |
| schemes. | apps, but would share the same third-party schemes ( | e.g. | , |  |  |  |  |  |  |
| Classifying App Link Hosts. | This only requires | oauth | ) for all their apps. | A larger apDev of the colli- |  |  |  |  |  |
| labeling third-party hosts from per-app hosts. | In total, | sion link indicates a higher chance of being a third-party |  |  |  |  |  |  |  |
| there are 2,451 hosts after pre-processing. | We observe | scheme. Moreover, third-party schemes are likely to use |  |  |  |  |  |  |  |
| that 1633 hosts are jointly registered by 5 apps, and 347 | the same component name for different apps ( | i.e. | , less |  |  |  |  |  |  |
| subdomains of “ | google.com | ” are registered by 2 apps. | unique), leading to smaller npcNum and ucNum. |  |  |  |  |  |  |
| ually searching their official documentations. | In total, | In total, we identify 149 per-app schemes and 2,314 per- |  |  |  |  |  |  |  |
| we label 137 third-party hosts, and 2,314 per-app hosts. | app hosts that are involved in link collisions. The related |  |  |  |  |  |  |  |  |
| Figure 9 compares per-app hosts and third-party hosts on | apps (893 and 1,593 respectively) are either the attacker |  |  |  |  |  |  |  |  |
| their number of collision apps, which are very similar. | or victim in the hijacking attacks. | To understand how |  |  |  |  |  |  |  |
| the labels, we briefly explore the feasibility of automated | Traffic | Hijacking. | We | find | apps | that | regis- |  |  |
| classification. As a feasibility test, we classify per-app | ter popular websites’ links (or popular apps’ schemes) |  |  |  |  |  |  |  |  |
| schemes from third-party schemes using 10 features such | seeking to redirect user traffic to themselves. | For |  |  |  |  |  |  |  |
| as unique developers per scheme, and apps per scheme | example, | “ | google.com | ” | is | registered | by | 480 | apps |
| (feature list in Appendix). | 5-fold cross-validation us- | from | 305 | non-Google | developers. | The | scheme |  |  |
| 962 | 26th USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |

---

## Page 12

“ google.navigation ” from Google Maps is hijacked App Link Scheme URL Intent URL

ber of links distributed to the web. Hijacking their links

are likely to increase the attacker apps’ chance of being

invoked. We find many popular apps are among the hi-

jacking targets ( e.g. , Facebook, Airbnb, YouTube, Tum-

click on an http/https link in the browser, these Redirec-

tor apps redirect users to the corresponding apps. Es-

sentially, Redirector apps play the role of mobile OS in

redirecting URLs, but their underlying mechanisms have

several security implications. For example, URLLander

( com.chestnutcorp.android.urlander ) and Ap-

pRedirect ( com.nevoxo.tapatalk.redirect ) each

has registered HTTPS links from 36 and 75 web domains

respectively (unverified) and has over 10,000 installs. We

suspect that users install Redirector apps because of the

convenience, since these apps allow users to open the

if the destination apps have not yet adopted App links.

to all the popular websites that Redirector apps reg-

istered such as facebook.com , instagram.com , and

ebay.com . Particularly for eBay, we find that the offi-

the over-permission vulnerability (see § 5.2) — if the user

once sets a preference for just one of those links.

Dataset

Table 7: Number of deep links (and webpages that con-

tain deep links) in Alexa top 1 million web domains.

loads) registers to receive all “ careem://* ” deep links.

customers.

Bad Scheme Names. Hijackings are also caused by

developers using easy-to-conflict scheme names. For ex-

ample, Citi Bank’s official app uses “ deeplink ” as its

per-app scheme, which conflicts with 6 other apps. These

apps are not malicious, but may cause confusions — a

user is going to open the Citi Bank app, but a non-related

app shows up (and vice versa). We detect 14 poorly

named per-app schemes ( e.g. , “ myapp ”, “ app ”).

7.1 Intent URL Usage

practice.

Intent URLs vs. Other Links We start by extracting

| by 79 apps from 32 developers. | The intuition is that | (Webpage) | (Webpage) | (Webpage) |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| popular sites and apps already have a significant num- | Alexa1M | 3.2M (480K) | 431K (197K) | 1,203 (452) |  |  |  |
| blr). Traffic hijacking is the most common attack. | adding credit card information. QatarTaxi (10K down- |  |  |  |  |  |  |
| URL Redirector MITM. | A number of hijackings | After code analysis, we find all these links redirect users |  |  |  |  |  |
| are conducted by “URL Redirector” apps. When users | to the QatarTaxi app’s home screen, as an attempt to draw |  |  |  |  |  |  |
| destination apps (without bouncing to the browser) even | 7 | Mobile Deep Links on The Web |  |  |  |  |  |
| The redirection is hard coded without the consent of the | Our analysis shows that hijacking risks still widely exist |  |  |  |  |  |  |
| destination apps or the originated websites. | within apps. Next, we move to the web-side to examine |  |  |  |  |  |  |
| URL redirector apps can act as man-in-the-middle | how mobile deep links are distributed on the web, and |  |  |  |  |  |  |
| (MITM) to hijack HTTP/HTTPS URLs. | For example, | estimate the likelihood of users encountering hijacked |  |  |  |  |  |
| URLLander | registered | “ | https://www.paypal.com | ” | links. In addition, we focus on | Intent URL | to examine |
| for redirection. | When a user visits | paypal.com | us- | its adoption and usage. We seek to estimate the impact |  |  |  |
| ing a browser (usually logged-in), the URL contains | of Intent URLs to mitigating hijacking threats. |  |  |  |  |  |  |
| sensitive parameters including a SESSIONID. Once the | In the following, we first measure the prevalence of |  |  |  |  |  |  |
| user agrees to use URLLander for redirection, the URL | Intent URLs on the web, and compare it with scheme |  |  |  |  |  |  |
| and SESSIONID will be handed over to URLLander | URLs and App links. Then, we revisit the hijacked links |  |  |  |  |  |  |
| by the browser in plaintext. | This MITM threat applies | detected in | § | 6 and analyze their appearance on the web. |  |  |  |
| cial eBay app explicitly does not register to open the link | Intent URL is a secure way of calling deep links from |  |  |  |  |  |  |
| “ | payments.ebay.com | ”, but this link was registered by | websites by specifying the target app’s package name |  |  |  |  |
| Redirector apps. | We analyze the code of AppRedirect | (unique identifier). | In theory, Intent URL can be used |  |  |  |  |
| and find it actually writes every single incoming URL | to invoke existing app components defined by scheme |  |  |  |  |  |  |
| and parameters in a log file. | Redirection (and MITM) | URLs (and even App links) to prevent hijacking. | The |  |  |  |  |
| can be automated without prompting users by exploiting | key question is how widely are Intent URLs adopted in |  |  |  |  |  |  |
| Hijacking a Competitor’s App. | Many apps are | mobile deep links from web pages in | Alexa1M | collected |  |  |  |
| competitors in the same business, | and we find tar- | in | § | 3. For App links and scheme URLs, we match all the |  |  |  |
| geted hijacking cases between competing apps. | For | hyperlinks in the HTML pages with the link registration |  |  |  |  |  |
| example, Careem ( | com.careem.acma | ) and QatarTaxi | entries extracted from apps. We admit that this method |  |  |  |  |
| ( | com.qatar.qatartaxi | ) are two competing taxi book- | is conservative as we only include deep links registered |  |  |  |  |
| ing apps in Dubai. Careem is more popular (5M+ down- | by apps in our dataset. | But the matching is necessary |  |  |  |  |  |
| loads), which uses scheme “ | careem | ” for many function- | since not all the HTTP/HTTPS links or schemes on the |  |  |  |  |
| alities such as booking a ride (from hotel websites) and | web can invoke apps. For Intent URLs, we identify them |  |  |  |  |  |  |
| USENIX Association | 26th USENIX Security Symposium | 963 |  |  |  |  |  |

---

## Page 13

0.14 25

0.12

20

0.1

| 0.08 | 15 |
| --- | --- |
| 0.06 | 10 |

0.04

0.02 5

0

% Websites w/ Deep Link 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 0

% Websites w/ Deep Link 5 10 15 20 25 30 35 40 45

100 10000 Third-party

1000 Functional

60

| 40 | 100 |
| --- | --- |
| Scheme URL | 3.4K |

0

1 2 10 100 1000 # of Deeplinks (Thousand) 1

The key observation is Intent URLs are rarely used.

tent URL is also orders of magnitude lower than other

links (1,203 versus 3.2M and 431K). This extremely low

adoption rate indicates that Intent URLs have little im-

aware developers use Intent URLs on their own websites,

find that almost all websites (except 2) are owned by the

50

40

30

20

10

50 55 60 65 70 75 80 85 90 95 100 0

% Websites w/ Deep Link 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100

1000

Per-app

Functional 191K

398K

100

122K 36K

2.3K

# of Websites (Thousand) 1

these sites.

7.2 Measuring Hijacking Risk on Web

by scheme URLs.

5.3K websites (0.5%).

| Bins of Websites (in 10 Thousand) | Bins of Websites (in 10 Thousand) | Bins of Websites (in 10 Thousand) |
| --- | --- | --- |
| (a) Intent URLs | (b) Scheme URLs | (c) App Links |

Figure 10: Deep link distribution among Alexa top 1 million websites. Website domains are sorted and divided into

20 even-sized bins (50K sites per bin). We report the % of websites that contain deep links in each bin.

| 80 | Per-app | 2620K | Third-party | 456K |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| CDF of App (%) | 20 | Intent URL | 10 | 7.2K | 10 | 5.3K |
| # Web Domains per App | Scheme URL | AppLink | Scheme URL | AppLink |  |  |

Figure 11: Number of websites that Figure 12: Different type of hijacked Figure 13: Webpages that contain hi-

| host deep links for each app. | deep links in Alexa1M. | jacked deep links in Alexa1M. |  |  |
| --- | --- | --- | --- | --- |
| based on their special format (“ | intent://*;end | ”). The | (50 websites for more than half of the apps). It is chal- |  |
| matching results are shown in Table 7. | lenging to remove or upgrade scheme URLs across all |  |  |  |
| Out of 1 million web domains, only 452 (0.05%) contain | Insecure Usage of Intent URL. | Among the 1,203 |  |  |
| Intent URLs in their index page. As a comparison, App | Intent URLs, we find 25 Intent URLs did not specify the |  |  |  |
| links and Scheme URLs appear in 480K (48%) and 197K | package name of the target app (only the host or scheme). |  |  |  |
| (19.7%) of these sites. For the total number of links, In- | These 25 Intent URLs can be hijacked. |  |  |  |
| pact to mitigating hijacking risks in practice. | To estimate the level of hijacking risks on the web, we |  |  |  |
| Challenges to Intent URL Adoption. | Since Android | now revisit the hijacking attacks detected in | § | 6 (those |
| still supports scheme URLs, it is possible that developers | on per-app schemes/hosts). We seek to measure the vol- |  |  |  |
| are not motivated to use Intent URLs to replace the still- | ume of hijacked links among webpages, and estimation |  |  |  |
| functional scheme URLs. In addition, even if security- | App link’s contributions over existing risks introduced |  |  |  |
| it is difficult for them to upgrade scheme URLs that have | Hijacked Mobile Deep Links. | We extract links from |  |  |
| been distributed to other websites. | Alexa1M | that are registered by multiple apps, which re- |  |  |
| As shown in Figure 10(a), Intent URLs are highly | turns 408,455 scheme URLs and 2,741,817 App links. |  |  |  |
| skewed towards to high-ranked websites. | In contrary, | Among them, 7,242 scheme URLs and 2,619,565 App |  |  |
| Scheme URLs are more likely to appear in low-ranked | links contain per-app schemes/hosts ( | i.e. | , hijacked links). |  |
| domains (Figure 10(b)), and App links’ distribution is | The key observation is that App links introduce orders |  |  |  |
| relatively even (Figure 10(c)). A possible explanation is | of magnitude more hijacked links than scheme URLs, as |  |  |  |
| that popular websites are more security-aware. | shown in Figure 12 (log scale y-axis). We further exam- |  |  |  |
| Then we focus on apps, and examine how many web- | ine the number of | websites | that contain hijacked links. |  |
| sites that contain an app’s deep links (Figure 11). We find | As shown in Figure 13, App links have a dominating |  |  |  |
| that most apps have their Intent URLs on a single website | contribution: 456K websites (out of 1 million, 45.6%) |  |  |  |
| (90%). We randomly select 40+ pairs of the one-to-one | contains per-app App links that are subject to link hi- |  |  |  |
| mapped apps and websites for manual examination. We | jacking. The corresponding number for scheme URL is |  |  |  |
| app developers, which confirms our intuition. | Scheme | App links, designed as the secure version of deep |  |  |
| URLs are found in more than 5 websites for 90% of apps | links, actually expose users to a higher level of risks. In- |  |  |  |
| 964 | 26th USENIX Security Symposium | USENIX Association |  |  |

---

## Page 14

| tuitively, http/https links have been used on the web for | Legacy Issue. | Android does not strongly enforce |  |  |
| --- | --- | --- | --- | --- |
| decades. Once apps register App links, a large number | App link verification possibly due to the legacy issues. |  |  |  |
| of existing http/https links on the web are automatically | First, scheme URLs are still widely used on websites |  |  |  |
| interpreted as App links. This creates more opportunities | as discussed in | § | 7. | Disabling scheme links altogether |
| for malicious apps to perform link hijacking. | would inevitably affect users’ web browsing experience |  |  |  |

Links Carrying Sensitive Data. To illustrate the

practical consequences of link hijacking, we perform a

quick analysis on the hijacked links with a focus on their

parameters. A quick keyword search returns 74 sen-

sitive parameter names related to authentications ( e.g. ,

authToken , sessionid , password , access token ,

full list in Appendix). We find that 1075 hijacked links

contain at least one of the sensitive parameters. A suc-

cessful hijacking will expose these parameters to the at-

tacker app. This is just one example, and by no means

exhaustive in terms of possibly sensitive data carried in

hijacked links ( e.g. , PII, location).

Key Implications. Our results shed light on the prac-

tical challenges to mitigate vulnerable mobile deep links.

First, scheme URL was designed for mixed purposes,

including invoking a generic function (functional/third-

party schemes) and launching a target app (per-app

schemes). The multipurpose design makes it difficult

to uniformly enforce security policies ( e.g. , associating

schemes to apps). A more practical solution should pro-

hibit per-app schemes, while not crippling the widely de-

ployed functional/third-party schemes on the web.

Second, App links and Intent URLs were designed

with security in mind. However, their practical usage

has deviated from the initial design. Particularly for App

links, 98% of apps did not implement link verification

correctly. In addition to various configuration errors, a

more important reason is unverified links still work on

Android, and developers are likely not motivated to ver-

ify links. As a result, App links not only fail to provide

( e.g. , causing broken links [8]). Second, according to

Google’s report [11], over 60% of Android devices are

still using Android 5.0 or earlier versions, which do not

support App link verification. Android allows apps (6.0

or higher) to use verified App links while maintaining

backward compatibility by not enforcing the verification.

Countermeasures. We discuss three countermea-

sures to mitigate link hijacking risks. In the short term,

the most effective countermeasures would be disabling

scheme URLs in mobile browsers and WebViews. Note

that this is not to disable the app interfaces defined by

schemes, but to encourage (force) websites to use Intent

URLs to invoke per-app schemes safely. Android may

to avoid massively breaking functional links. For cus-

tomized scheme URLs that are still used on the web,

Android needs to handle their failure gracefully without

severely degrading user experience. Second, prohibit-

ing apps from opening unverified App links to prevent

link hijacking. The drawback is that apps without a web

front would face difficulties to use deep links — they will

need to rely on third-party services such as Brach.io [4]

or Firebase [5] to host their association files. Third,

addressing the over-permission vulnerability ( § 5.2), by

adopting more fine-grained preference setting ( e.g. , at the

host level or even the link level). This threat would also

go away if Android strictly enforces App link verifica-

tions.

Vulnerability Notification & Mitigation. Our study

identifies new vulnerabilities and attacks, and we are tak-

ing active steps to notifying the related parties for the risk

mitigation.

| 8 | Discussion | also whitelist a set of well-defined functional schemes |  |  |
| --- | --- | --- | --- | --- |
| better security, but worsen the situation significantly by | First, regarding the over-permission vulnerability, we |  |  |  |
| introducing more hijackable links. | have filed a bug report through Google’s Vulnerability |  |  |  |
| Finally, the insecurity of deep links leads to a tough | Reward Program (VRP) in February 2017. | As of June |  |  |
| trade-off between security and usability. | Mobile deep | 2017, we have established a case and submitted the sec- |  |  |
| links were designed for usability, to enable seamless | ond round of materials including the proof-of-concept |  |  |  |
| context-aware transitions from web to apps. | However, | app and a demo of the attack. We are waiting for further |  |  |
| due to the insecure design, mobile platforms have to con- | responses from Google. Second, we have reported our |  |  |  |
| stantly prompt users to confirm the links they clicked, | findings to the Android anti-malware team and the Fire- |  |  |  |
| which in turn hurts usability. | The current solution for | base team regarding the massive unverified App links and |  |  |
| Android (and iOS) takes a middle ground, by letting | the misconfiguration issues. Details regarding their miti- |  |  |  |
| users set “preference” for certain apps to disable prompt- | gation plan, however, were not disclosed to us. Third, as |  |  |  |
| ing. | We find this leads to new security vulnerabilities | shown in | § | 5.1, most of the misconfigured App links have |
| (over permission risk in | § | 5.2) that allow malicious apps | not been fixed after 5 months. In the next step, we plan |  |
| to hijack arbitrary HTTP/HTTPS URLs in the Android | to contact the developers, particularly those of hijacked |  |  |  |
| browser. | apps and help them to mitigate the configuration errors. |  |  |  |
| USENIX Association | 26th USENIX Security Symposium | 965 |  |  |

---

## Page 15

| Limitations. | Our study has a few limitations. First, | browser using XSS [27, 50] and origin-crossing [52]. |
| --- | --- | --- |
| our conclusions are limited to mobile deep links of An- | The threat also applies to customized in-app browsers |  |
| droid. Although iOS takes a more strict approach to en- | (called WebView) [20, 37, 40, 51]. In our work, we focus |  |
| forcing the link verification, it remains to be seen how | hijacking threats to apps, a different threat model where |  |
| well the security guarantees are achieved in practice. Our | browser is the not target. |  |

brief measurement in § 5.1 already shows that iOS uni-

versal links also have misconfigurations. More exten-

sive measurements are needed to fully understand the

potential security risks of iOS deep links. Second, our

measurement scope is still limited comparing to the size

of Android app market and the whole web. We argue

that data size is sufficient to draw our conclusions. By

measuring the most popular apps (160,000+) and web

domains (1,000,000), we collect strong evidence on the

incompetence of the newly introduced linking mecha-

nisms in providing better security. Third, we only fo-

cus on the link hijacking threat, because this is the se-

curity issue that App links and Intent URLs were de-

signed to address. There are other threats related to web-

to-mobile communications such as exploiting WebViews

and browsers [20, 37], and cross-site request forgery on

apps [27, 46, 50]. Our work is complementary to existing

work to better understand and secure the web-and-app

ecosystem.

9 Related Work

Inter-app Communication & Deep Links. Re-

searchers have discovered various vulnerabilities in the

inter-app communication mechanism in Android [19, 23]

and iOS [52], which leads to potential hijacking and

spoofing attacks. The fundamental issue is a lack of

source and destination authentication [52]. In the con-

text of app-to-app communication, attacks may cause

permission escalation [15, 21] and sensitive data leak-

age [46]. Mobile deep links ( e.g. , scheme URL) inherent

some of these vulnerabilities when facilitating commu-

nications between websites and apps. Unlike web URLs

whose uniqueness is guaranteed by the DNS, mobile

deep links lack a similar, centralized entity for link reg-

istration and addressing. As a result, multiple apps may

register the same link, leading to hijacking risks. Our

work is complementary to existing work since we focus

on large-scale empirical measurements, providing new

understandings to how the risks are mitigated in practice.

Other recent works on mobile deep links focus on im-

proving usability instead of security. Two systems are

proposed to automatically generate deep links for apps

via static and dynamic code analysis [38, 49].

Detection and Mitigation. Existing research has ex-

plored different approaches to detect vulnerabilities in

app-to-app communications. On one hand, static code

analysis leverages call graphs and flow analysis to de-

tect information leakages [15, 26, 36, 45, 57] and vul-

nerable interfaces for inter-app communications [14, 32,

33, 34, 41, 42, 43]. On the other hand, dynamic anal-

ysis tracks information flow in the runtime which can

capture attacks that would be otherwise missed by static

analysis [24, 28, 30, 54, 56]. To remove and miti-

gate vulnerabilities, researchers propose to automatically

generate app patches [39, 45, 58], enforce strict poli-

cies [16, 17, 31, 51, 59] and provide guidelines for writ-

ing safer apps [31]. Our work highlights the significant

gap between a security solution and the practical impact

in mitigating threats. Beyond technical solutions, other

factors such as developer incentives and capabilities and

mobile platform policies also play a big role.

10 Conclusion

In this paper, we conducted the first large-scale measure-

ment study on mobile deep links across popular Android

apps and websites. Our results showed strong evidence

that the newly proposed deep link methods (App links

and Intent URLs) fail to address the existing hijacking

risks in practice. In addition, we identified new vul-

nerabilities and empirical misconfigurations in App links

which ultimately expose users to a higher level of risks.

Finally, we made a list of suggestions to countermeasure

the link hijacking risks in Android. Moving forward, we

plan to further investigate automated methods for hijack-

ing detection, and conduct more extensive measurements

on iOS deep links in the future.

Acknowledgments

The authors wish to thank the anonymous reviewers and

our shepherd Manuel Egele for their helpful comments,

and Bolun Wang for sharing the scripts to collect the

meta data of Android apps. This project was supported

| Mobile Browser Security. | In web-to-app communi- | by NSF grant CNS-1717028. | Any opinions, findings, |
| --- | --- | --- | --- |
| cations, mobile browsers play an important role in bridg- | and conclusions or recommendations expressed in this |  |  |
| ing websites and apps, which can also be the target of | material are those of the authors and do not necessarily |  |  |
| attacks. For example, malicious websites may attack the | reflect the views of any funding agencies. |  |  |
| 966 | 26th USENIX Security Symposium | USENIX Association |  |

---

## Page 16

References [14] B AGHERI , H., S ADEGHI , A., G ARCIA , J., AND

[2] Android Intents with Chrome. https:

[3] App programming guide for ios. https:

//developer.apple.com/library/

[4] Branch. https://developer.branch.io/ .

[5] Firebase App Indexing. https://firebase.

google.com/docs/app-indexing .

android.com/training/app-links/index.

html .

//developer.android.com/training/

basics/intents/filters.html .

branch.io/ios-9-2-redirection-update-

uri-scheme-and-universal-links/ .

[9] Support Universal Links. https://

developer.apple.com/library/content/

documentation/General/Conceptual/

AppSearch/UniversalLinks.html .

[10] Smartphone apps crushing mobile web times.

https://www.emarketer.com/Article/

Smartphone-Apps-Crushing-Mobile-Web-

Time/1014498 , October 2016.

[11] Android platform versions. https://developer.

android.com/about/dashboards/index.

html , May 2017.

[12] A KHAWE , D., AND F ELT , A. P. Alice in warning-

land: A large-scale field study of browser security

warning effectiveness. In Proc. of USENIX Security

(2013).

//www.iana.org/assignments/uri-

schemes/uri-schemes.xhtml , February 2017.

M ALEK , S. COVERT: Compositional analysis of

actions in Software Engineering (2015).

analysis of inter-app communications. In Proc. of

ASIACCS (2017).

Technical Report TR-2011-04 (2011).

[17] B UGIEL , S., H EUSER , S., AND S ADEGHI , A.-R.

Flexible and fine-grained mandatory access control

on Android for diverse security and privacy poli-

[18] C HEN , E. Y., P EI , Y., C HEN , S., T IAN , Y.,

K OTCHER , R., AND T AGUE , P. Oauth demysti-

CCS (2014).

[19] C HIN , E., F ELT , A. P., G REENWOOD , K., AND

[20] C HIN , E., AND W AGNER , D. Bifocals: Analyzing

webview vulnerabilities in Android applications. In

Proc. of WISA (2014).

[21] D AVI , L., D MITRIENKO , A., S ADEGHI , A.-R.,

AND W INANDY , M. Privilege escalation attacks

on Android. In Proc. of ISC (2011).

[22] E GELMAN , S., C RANOR , L. F., AND H ONG , J.

You’ve been warned: An empirical study of the ef-

fectiveness of web browser phishing warnings. In

Proc. of CHI (2008).

[23] E LISH , K. O., Y AO , D., AND R YDER , B. G. On

the need of precise inter-app ICC classification for

detecting Android malware collusions. In Proc. of

MoST (2015).

[24] E NCK , W., G ILBERT , P., H AN , S., T ENDULKAR ,

V., C HUN , B.-G., C OX , L. P., J UNG , J., M C -

D ANIEL , P., AND S HETH , A. N. TaintDroid: an

2 (2014), 5.

[25] E NGLEHARDT , S., AND N ARAYANAN , A. Online

tracking: A 1-million-site measurement and analy-

sis. In Proc. of CCS (2016).

| [1] Alexa. | http://www.alexa.com | . | Android inter-app permission leakage. | IEEE Trans- |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| //developer.chrome.com/multidevice/ | [15] B | OSU | , A., L | IU | , F., Y | AO | , D. D., | AND | W | ANG | , G. |
| android/intents | . | Collusive data leak and more: | Large-scale threat |  |  |  |  |  |  |  |  |
| content/documentation/iPhone/ | [16] B | UGIEL | , S., D | AVI | , L., D | MITRIENKO | , A., F | IS | - |  |  |
| Conceptual/iPhoneOSProgrammingGuide/ | CHER | , T., | AND | S | ADEGHI | , A.-R. XManDroid: A |  |  |  |  |  |
| Inter-AppCommunication/Inter- | new Android evolution to mitigate privilege esca- |  |  |  |  |  |  |  |  |  |  |
| AppCommunication.html | . | lation attacks. | Technische Universit¨ | at Darmstadt, |  |  |  |  |  |  |  |
| [6] Handling | App | Links. | https://developer. | cies. In | Proc. of USENIX Security | (2013). |  |  |  |  |  |
| [7] Interacting | with | Other | Apps. | https: | fied for mobile application developers. In | Proc. of |  |  |  |  |  |
| [8] iOS 9.2 Update: | The Fall of URI Schemes and | W | AGNER | , D. Analyzing inter-application commu- |  |  |  |  |  |  |  |
| the Rise of Universal Links. | https://blog. | nication in Android. In | Proc. of MobiSys | (2011). |  |  |  |  |  |  |  |
| [13] A | UTHORITY | , | I. | A. | N. | Uniform | re- | information-flow tracking system for realtime pri- |  |  |  |
| source | identifier | (URI) | schemes. | http: | vacy monitoring on smartphones. | ACM TOCS 32 | , |  |  |  |  |
| USENIX Association | 26th USENIX Security Symposium | 967 |  |  |  |  |  |  |  |  |  |

---

## Page 17

| [26] G | ORDON | , | M. | I., | K | IM | , | D., | P | ERKINS | , | J. | H., | [38] M | A | , Y., L | IU | , X., D | U | , R., H | U | , Z., L | IU | , Y., Y | U | , |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G | ILHAM | , L., N | GUYEN | , N., | AND | R | INARD | , M. C. | M., | AND | H | UANG | , G. | DroidLink: | Automated |  |  |  |  |  |  |  |  |  |  |  |
| Information flow analysis of Android applications | generation of deep links for Android apps. | CoRR |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| in DroidSafe. In | Proc. of NDSS | (2015). | abs/1605.06928 | (2016). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [27] H | AY | , R., | AND | A | MIT | , Y. | Android browser cross- | [39] M | ULLINER | , C., O | BERHEIDE | , J., R | OBERTSON | , |  |  |  |  |  |  |  |  |  |  |  |  |
| application scripting (cve-2011-2357). Tech. rep., | W., | AND | K | IRDA | , E. | PatchDroid: Scalable third- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| July 2011. | party security patches for Android devices. In | Proc. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

of ACSAC (2013).

[28] H AY , R., T RIPP , O., AND P ISTOIA , M. Dynamic

detection of inter-application communication vul- [40] M UTCHLER , P., D OUP E ´ , A., M ITCHELL , J.,

nerabilities in Android. In Proc. of ISSTA (2015). K RUEGEL , C., AND V IGNA , G. A large-scale

study of mobile web app security. In Proc. of IEEE

[29] I NTERNATIONAL D ATA C ORPORATION MoST (2015).

(IDC). Smartphone OS Market Share. http:

//www.idc.com/prodserv/smartphone-os- [41] O CTEAU , D., J HA , S., D ERING , M., M C -

market-share.jsp , November 2016. D ANIEL , P., B ARTEL , A., L I , L., K LEIN , J., AND

L E T RAON , Y. Combining static analysis with

| [30] J | ING | , Y., A | HN | , G.-J., D | OUP | E | ´ | , A., | AND | Y | I | , J. H. | probabilistic models to enable market-scale An- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Checking intent-based communication in Android | droid inter-component analysis. In | Proc. of POPL |  |  |  |  |  |  |  |  |  |  |  |
| with intent space analysis. | In | Proc. of ASIACCS | (2016). |  |  |  |  |  |  |  |  |  |  |

(2016).

[42] O CTEAU , D., M C D ANIEL , P., J HA , S., B ARTEL ,

| [31] K | ANTOLA | , D., C | HIN | , E., H | E | , W., | AND | W | AGNER | , | A., B | ODDEN | , E., K | LEIN | , J., | AND | L | E | T | RAON | , |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D. | Reducing attack surfaces for intra-application | Y. Effective inter-component communication map- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| communication in Android. | In | Proc. of SPSM | ping in Android: An essential step towards holis- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (2012). | tic security analysis. In | Proc. of USENIX Security |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [32] K | LIEBER | , W., F | LYNN | , L., B | HOSALE | , A., J | IA | , L., | (2013). |  |  |  |  |  |  |  |  |  |  |  |  |
| AND | B | AUER | , L. | Android taint flow analysis for | [43] R | AVITCH | , | T., | C | RESWICK | , | E. R., | T | OMB | , | A., |  |  |  |  |  |
| app sets. In | Proc. of SOAP | (2014). | F | OLTZER | , A., E | LLIOTT | , T., | AND | C | ASBURN | , L. |  |  |  |  |  |  |  |  |  |  |
| [33] L | I | , | L., | B | ARTEL | , | A., | B | ISSYANDE | , | T. | F. | Multi-App security analysis with FUSE: Statically |  |  |  |  |  |  |  |  |
| D. A., K | LEIN | , J., L | E | T | RAON | , Y., A | RZT | , S., | detecting Android app collusion. | In | Proc. of |  |  |  |  |  |  |  |  |  |  |
| R | ASTHOFER | , | S., | B | ODDEN | , | E., | O | CTEAU | , | D., | PPREW | (2014). |  |  |  |  |  |  |  |  |
| AND | M | C | D | ANIEL | , | P. | IccTA: | detecting | inter- | [44] R | OWINSKI | , D. Digital strategy: Why native apps |  |  |  |  |  |  |  |  |  |
| component privacy leaks in Android apps. In | Proc. | versus mobile web is a false choice. | https: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| of ICSE | (2015). | //arc.applause.com/2016/09/13/native- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [34] L | IU | , F., C | AI | , H., W | ANG | , G., Y | AO | , D. D., E | L | - | apps-versus-mobile-web-decision/ | , |  |  |  |  |  |  |  |  |  |
| ISH | , K. O., | AND | R | YDER | , B. G. | MR-Droid: A | September 2016. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| scalable and prioritized analysis of inter-app com- | [45] S | B | ˆ | IRLEA | , D., B | URKE | , M. G., G | UARNIERI | , S., |  |  |  |  |  |  |  |  |  |  |  |  |
| munication risks. In | Proc. of MoST | (2017). | P | ISTOIA | , M., | AND | S | ARKAR | , V. | Automatic de- |  |  |  |  |  |  |  |  |  |  |  |
| [35] L | IU | , Y., S | ONG | , H. H., B | ERMUDEZ | , I., M | ISLOVE | , | tection of inter-application permission leaks in An- |  |  |  |  |  |  |  |  |  |  |  |  |
| A., B | ALDI | , M., | AND | T | ONGAONKAR | , A. Identify- | droid applications. | IBM Journal of Research and |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ing personal information in internet traffic. In | Proc. | Development 57 | , 6 (2013), 10–1. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| of COSN | (2015). | [46] S | CHLEGEL | , R., | Z | HANG | , K., | Z | HOU | , X., | I | NT | - |  |  |  |  |  |  |  |  |
| [36] L | U | , L., L | I | , Z., W | U | , Z., L | EE | , W., | AND | J | IANG | , | WALA | , M., K | APADIA | , A., | AND | W | ANG | , X. Sound- |  |
| G. CHEX: Statically vetting Android apps for com- | comber: A stealthy and context-aware sound trojan |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ponent hijacking vulnerabilities. | In | Proc. of CCS | for smartphones. In | Proc. of NDSS | (2011). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (2012). | [47] S | TAROV | , O., G | ILL | , P., | AND | N | IKIFORAKIS | , N. |  |  |  |  |  |  |  |  |  |  |  |  |
| [37] L | UO | , T., H | AO | , H., D | U | , W., W | ANG | , Y., | AND | Y | IN | , | Are you sure you want to contact us? | quantify- |  |  |  |  |  |  |  |
| H. Attacks on webview in the Android system. In | ing the leakage of pii via website contact forms. In |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Proc. of ACSAC | (2011). | Proc. of PETS | (2016). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 968 | 26th USENIX Security Symposium | USENIX Association |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 18

[48] S TATISTA : T HE STATISTICS PROTAL . Number Appendix

of available applications in the Google Play store

[49] T ANZIRUL A ZIM , O RIANA R IVA , S. N. uLink:

Enabling user-defined deep linking to app content.

[51] T UNCAY , G. S., D EMETRIOU , S., AND G UNTER ,

C. A. Draco: A system for uniform and fine-

grained access control for web code on Android.

In Proc. of CCS (2016).

[52] W ANG , R., X ING , L., W ANG , X., AND C HEN , S.

Unauthorized origin crossing on mobile platforms:

Threats and mitigation. In Proc. of CCS (2013).

[54] X IA , M., G ONG , L., L YU , Y., Q I , Z., AND L IU ,

[55] X ING , L., B AI , X., L I , T., W ANG , X., C HEN , K.,

L IAO , X., H U , S.-M., AND H AN , X. Cracking

app isolation on apple: Unauthorized cross-app re-

source access on MAC OS X and iOS. In Proc. of

CCS (2015).

[56] Y ANG , K., Z HUGE , J., W ANG , Y., Z HOU , L.,

AND D UAN , H. IntentFuzzer: Detecting capability

leaks of Android applications. In Proc. of ASIACCS

[57] Y ANG , Z., Y ANG , M., Z HANG , Y., G U , G.,

N ING , P., AND W ANG , X. S. AppIntent: analyzing

sensitive data transmission in Android for privacy

[58] Z HANG , M., AND Y IN , H. AppSealer: Auto-

matic generation of vulnerability-specific patches

[59] Z HANG , Y., Y ANG , M., G U , G., AND C HEN ,

wide application execution context. In Proc. of Se-

cureComm (2015).

used by a larger variety of apps and developers, but are

used for similar components in the third-party library

is a list of sensitive parameters identified in the mobile

thentication. These parameter names are used in § 7 to

match hijacked deep links that carry sensitive data. We

obtain this list by keyword searching and manual anno-

tation. This is by no means an exhaustive list. The goal

is provide examples to illustrate practical consequences

of link hijacking attacks.

| Feature | Description |
| --- | --- |
| aNum | Total # of apps |
| utcNum | # of unique third-party components |
| npcNum | # of unique components name (no prefix) |
| tDevP | % of third-party developers |
| ucP | % of unique components |

Table 8: Features used for scheme classification.

access token, actionToken, api key, apikey, apiTo-

ken, Auth, auth key, auth token, authenticity token,

authkey, authToken, autologin, AWSAccessKeyId,

cookie, csrf token, csrfKey, csrfToken, ctoken,

fk session id, FKSESSID, FOGSESSID, force sid,

SESSID, imprToken, jsessionid, key, keycode, keys,

LinkedinToken, live configurator token, LLSES-

SID, MessageKey, mrsessionid, navKey, newsid,

oauth callback, oauth token, pasID, pass, pass key,

redir token, reward key, roken2, seasonid, secret key,

secret perk token, ses key, sesid, SESS, sessid, ses-

sid2b4f0b11dea2f7ae4bfff49b6307d50f, SESSION,

vt session id, wmsAuthSign, ytsession

| from December 2009 to February 2016. | http: | Features for Classifying Schemes. | Table 8 shows a |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| //www.statista.com/statistics/266210/ | list of features for classifying per-app schemes and third- |  |  |  |  |  |  |  |  |  |
| number-of-available-applications-in- | party schemes in | § | 6. These features are selected based |  |  |  |  |  |  |  |
| the-google-play-store/ | , 2016. | on the intuition that third-party schemes are likely to be |  |  |  |  |  |  |  |  |
| In | Proc. of Mobisys | (2016). | Sensitive Mobile Deep Link Parameters . | Table 9 |  |  |  |  |  |  |
| [50] T | ERADA | , T. Attacking Android browsers via intent | deep links from Alexa top 1 million websites. | We ex- |  |  |  |  |  |  |
| scheme urls. Tech. rep., March 2014. | clusively focus on link parameters that are related to au- |  |  |  |  |  |  |  |  |  |
| [53] W | U | , M., M | ILLER | , R. C., | AND | G | ARFINKEL | , S. L. | uDev | # of developers |
| Do security toolbars actually prevent phishing at- | cNum | Total # of components |  |  |  |  |  |  |  |  |
| tacks? In | Proc. of CHI | (2006). | ucNum | # of unique components |  |  |  |  |  |  |
| X. Effective real-time android application auditing. | tDev | # of developers with third-party components |  |  |  |  |  |  |  |  |
| In | Proc. of IEEE S&P | (2015). | apDev | Average # of apps of the same developer |  |  |  |  |  |  |
| (2014). | formkey, | gsessionid, | guestaccesstoken, | hkey, | IK- |  |  |  |  |  |
| leakage detection. In | Proc. of CCS | (2013). | password, | PHPSESSID, | piggybackCookie, | plkey, |  |  |  |  |
| for preventing component hijacking attacks in An- | session id, | session rikey, | sessionGUID, | sessionid, |  |  |  |  |  |  |
| droid applications. In | Proc. of NDSS | (2014). | sh auth, sharedKey, SID, tok, token, uepSessionToken, |  |  |  |  |  |  |  |
| H. FineDroid: Enforcing permissions with system- | Table 9: Sensitive parameters in mobile deep links. |  |  |  |  |  |  |  |  |  |
| USENIX Association | 26th USENIX Security Symposium | 969 |  |  |  |  |  |  |  |  |

---

## Page 19
