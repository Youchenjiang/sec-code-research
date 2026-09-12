---year: 2024

secverify_category: "Category A"
categories:
  - "[[2A.1-Web與API動態漏洞掃描 (DAST)]]"
  - "[[2B.1-反饋引導式模糊測試 (Feedback-directed Fuzzing)]]"
title: "Wasserstein GAN-Based Android Certificate Validation Vulnerability Detection Framework"
creator: "LaTeX with acmart 2024/12/07 v2.11 Typesetting articles for the Association for Computing Machinery and hyperref 2023-02-07 v7.00v Hypertext links for LaTeX"
pages: 6
source: "Wasserstein (2024) Wasserstein GAN-Based Android Certificate Validation.pdf"
---

# Wasserstein GAN-Based Android Certificate Validation Vulnerability Detection Framework

> **文獻存檔**：[PDF 原文](<../../raw-papers/2024/Wasserstein (2024) Wasserstein GAN-Based Android Certificate Validation.pdf>) | [Markdown 原文](<../../raw-papers/2024/Wasserstein (2024) Wasserstein GAN-Based Android Certificate Validation (Raw).md>)

> **總頁數**：6 頁

---

## Page 1

Wasserstein GAN-Based Android Certificate Validation

Vulnerability Detection Framework

Yong Fang

University of Science and Technology of China

Hefei, Anhui, China

fangyxueit@163.com

Abstract

ity detection framework that integrates static analysis, adversarial

sample training, and optimization via large language models. Cen-

framework aims to enhance the robustness and generalization abil-

ity of static detection models against complex and obfuscated attack

patterns. Static analysis is performed on 2,000 popular Android ap-

plications from the androzoo dataset, with code and configuration

perimental results across standard, adversarial, and cross-domain

scenarios demonstrate that the proposed framework achieves an F1

score of 0.91 and reduces the false positive rate to 7.2%, significantly

outperforming traditional static detection tools in both accuracy

CCS Concepts

• Security and privacy → Software and application security; Soft-

ware security engineering.

Keywords

TLS Certificate Validation, Android Security, Generative Adversar-

ial Networks, Adversarial Robustness

This work is licensed under a Creative Commons

© 2025 Copyright held by the owner/author(s).

231

∗

School of Computer Science and Technology

ACM Reference Format:

Vulnerability Detection Framework. In 2025 2nd International Conference

on Generative Artificial Intelligence and Information Security (GAIIS 2025),

February 21–23, 2025, Hangzhou, China. ACM, New York, NY, USA, 6 pages.

1 Introduction

2 Related work

2.1 Static Analysis Methods

vulnerabilities (e.g., matching empty implementations of the check-

ServerTrusted method). However, their effectiveness is limited by

three major technical factors:

2.2 GAN-Based Methods for Vulnerability

Detection

2.2.1 Adversarial Sample Quality. Although WGANs are effective

in enhancing sample diversity, the generated samples may still

contain issues such as syntactic errors or semantic inconsistencies.

These defects introduce noise into the training dataset, ultimately

come these limitations, hybrid approaches have been proposed that

integrate static analysis, vulnerability detection, and generative

modeling, while employing iterative context learning for parameter

optimization. In such frameworks, static analysis is used to filter out

for vectorization. These features are then utilized by the vulnera-

| This paper presents an Android certificate validation vulnerabil- | Yong Fang. 2025. Wasserstein GAN-Based Android Certificate Validation |  |  |
| --- | --- | --- | --- |
| tered around the Wasserstein Generative Adversarial Network, the | https://doi.org/10.1145/3728725.3728761 |  |  |
| features extracted, focusing on certificate-related API usage, per- | Android’s dominance as a global OS is marred by pervasive TLS cer- |  |  |
| mission declarations, and network security settings. Among them, | tificate validation vulnerabilities, including insecure TrustManager |  |  |
| 110 APKs are identified as containing high-risk certificate miscon- | implementations and HostnameVerifier misconfigurations, which |  |  |
| figurations. Based on these features, a Transformer-based model | enable 37% annual growth in MITM attacks (CVE 2024). While |  |  |
| is constructed for feature vectorization and vulnerability identifi- | static analyzers like QARK/MobSF detect such flaws via rule-based |  |  |
| cation. To further improve model robustness, WGAN is employed | heuristics, their limited pattern coverage and high false positives |  |  |
| to generate adversarial samples that mimic real-world evasive vul- | hinder practical deployment. To overcome these limitations, we |  |  |
| nerabilities, which are used for adversarial training. Additionally, | propose a Wasserstein GAN-based hybrid detection framework |  |  |
| large language models are used to perform In-Context Learning, | integrating gradient-penalized generative modeling and context- |  |  |
| enabling semantic filtering, sample refinement, and iterative genera- | aware learning, achieving enhanced accuracy (F1-score +18.7%), |  |  |
| tor feedback. This results in a closed-loop, self-improving detection | reduced false positives ( | ↓ | 32.4%), and improved adversarial robust- |
| pipeline that combines detection, optimization, and feedback. Ex- | ness compared to baseline methods[1]. |  |  |
| and resilience. | Static analysis tools typically rely on predefined rules to identify |  |  |
| ∗ | Corresponding author | degrading the performance of the detection model [4].To over- |  |
| Attribution-NonCommercial-NoDerivs International 4.0 License. | syntactically invalid samples and extract certificate-related features |  |  |
| GAIIS 2025, Hangzhou, China | bility detection model to guide adversarial sample generation via |  |  |
| ACM ISBN 979-8-4007-1345-3/2025/02 | WGAN, with ICL employed to iteratively refine the generator pa- |  |  |
| https://doi.org/10.1145/3728725.3728761 | rameters. Empirical results demonstrate that this hybrid strategy |  |  |

![Page 1 Image](data:image/png;base64,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)

---

## Page 2

GAIIS 2025, February 21–23, 2025, Hangzhou, China Yong Fang

Figure 1: Certificate Validation Vulnerability Detection Pro-

cess.

can reduce false positive rates by up to 22% compared to standalone

GAN-based models.

3 Methodology

applications by designing a comprehensive detection framework

large-model-based optimization. The proposed method aims to

extract key certificate configuration features from Android APKs

model are iteratively refined through guidance from large-scale

language models, thereby forming a closed-loop, interpretable, and

highly robust vulnerability detection system.[2][5]

Figure 1 illustrates the overall design of the proposed method. In

lected from public Android datasets, including AndroZoo, domestic

platforms such as Pea Pod, and user devices. The APKs are decom-

piled using apktool, converting them into Smali code.Static analysis

is then performed to extract certificate-related features, including:

232

vectors for model training.The trained detection model identifies

TLS certificate validation vulnerabilities based on these features.

When a vulnerability is detected, a generative adversarial network

is used to synthesize adversarial samples, enhancing model robust-

ness. The detection results are also forwarded to the ICL module,

which invokes large language models (e.g., GPT-4 or DeepSeek) via

API to provide automated vulnerability analysis and remediation

suggestions[3].

3.1 Static Analysis Feature Extraction

Certificate authentication vulnerabilities may arise from insecure

configurations or improper implementation practices by developers.

In the static analysis and feature extraction module, we employ

apktool to decompile the APK, directly access the application’s code

structure and configuration files, and extract components related

to certificate validation, including SSLContext usage, custom Trust-

Manager, and HostnameVerifier implementations. These elements

are transformed into structured feature vectors, which serve as

inputs to the downstream detection model. This static approach

eliminates the need for a dynamic runtime environment, thereby

improving analysis efficiency and reducing deployment overhead.

During the static analysis phase, we focus on three categories of

features: configuration features, API call features, and code-level

features. Figure 2 shows the distribution of detected vulnerability

types. SSL Misuse is the most common (35.0%), followed by Trust-

Manager Override (29.2%) and HostnameVerifier Bypass (23.3%).

Other Issues account for 12.5%. This highlights the prevalence of

SSL-related security risks in Android applications.

3.1.1 Configuration Feature Extraction. This component extracts

network security–related settings from the AndroidManifest.xml

file, including the identification of custom networkSecurityConfig

files and their contents, the implementing classes for certificate-

related interfaces, and verification that certificate authority (CA)

validation has not been explicitly disabled. For instance, a devel-

oper may configure an insecure network security policy in the

AndroidManifest.xml by referencing a networkSecurityConfig file

<application

fig”>

</application>

nificant security risks:

<network-security-config>

<base-config>

<trust-anchors>

</trust-anchors>

</base-config>

</network-security-config>

| This study addresses certificate validation vulnerabilities in Android | that disables certificate validation: |  |  |
| --- | --- | --- | --- |
| that integrates static analysis, generative adversarial networks, and | android:networkSecurityConfig | = | ”@xml/network_security_con- |
| through static analysis—without relying on dynamic execution | In the APK’s res/xml/network_security_config.xml file, all certifi- |  |  |
| traces—and to construct a robust training process using a generative | cates are implicitly trusted if the following configuration is present, |  |  |
| adversarial network. Furthermore, the parameters of the adversarial | thereby disabling proper certificate validation and introducing sig- |  |  |
| the data collection and preprocessing phase, 2,000 APK files are col- | <certificates src | = | ”user” /> |
| configurations in AndroidManifest.xml; implementations of Trust- | 3.1.2 | API call features. | Custom X509TrustManager implementa- |
| Manager, SSLContext initialization, and HostnameVerifier usage | tion, unsafe call to SSLContext.getInstance(”SSL”), unsafe rewrite |  |  |
| in Java or Smali code. These features are encoded into structured | of HostnameVerifier.verify() method e.g.: returns true directly |  |  |

---

## Page 3

Wasserstein GAN-Based Android Certificate Validation Vulnerability Detection Framework GAIIS 2025, February 21–23, 2025, Hangzhou, China

Figure 2: Shows the distribution of the types of security

vulnerabilities detected.

skip hostname validation and override the verify() method;

public void checkServerTrusted(X509Certificate[] chain, String

authType) throws CertificateException {

trustManager.checkServerTrusted(chain, authType);

3.1.4 Data set construction. A total of 2,000 APK samples were

selected from the AndroZoo open-source dataset, with 100 positive

samples manually verified to contain certificate validation vulnera-

bilities. The dataset was split into training, validation, and test sets

3.2 Adversarial Sample Generation and Model

Robustness Enhancement Based on

Generative Networks

233

disguised vulnerabilities. The overall framework implements a

closed-loop ”generation-defense” mechanism: the generative net-

work simulates high-fidelity adversarial samples, while adversarial

training strengthens the detection model’s resilience, thereby form-

ing a dynamic and robust defense system[9].

3.2.1 Generator. To capture the characteristics of vulnerability

configurations, the generator takes as input a multi-dimensional

feature vector X, derived from static analysis of code structure,

configuration, and API calls.

푿 = [ 풙 1 , 풙 2 , . . . , 풙 풏 ] ∈ 푹 풏 × 풅

n: number of samples; d: feature dimension

The generator aims to produce fake feature vectors 퐺 ( 푧, 푋 ) that

approximate the distribution of real vulnerability instances and are

capable of deceiving the discriminator.

퐺 ( 푧, 푋 ) = ReLU ( 푊 2 ReLU ( 푊 1 [ 푧, 푋 ] + 푏 1 ) + 푏 2 )

푊 1 ,푊 2 is the network parameter matrix 푧 ∼ N ( 0 , 1 )

random noise 푋 Input feature 푏 1 , 푏 2 Offset term

3.2.2 Discriminator. The goal of the discriminator is to determine

whether the input feature vector is a real vulnerability sample or

Discriminator structure

휎 , activation function for output true − false determination

푊 1 ,푊 2 ,푊 3 is the weight parameter of the discriminator

푏 1 , 푏 2 , 푏 3 is the offset term WGAN Loss Function

2

Moving to the output and verification process, generated samples

include obfuscated vulnerabilities, such as renaming TrustManager

to ClassA while maintaining the original logic, which can help

to bypass static analysis tools. The loss function combines cross-

entropy loss 퐿

being 퐿

innovation is static feature interaction, which enhances network

traffic analysis by detecting issues like reflective code execution.

The attention mechanism prioritizes high-risk features, such as

checkServerTrusted, improving vulnerability detection accuracy

and robustness[6].

| SSLContext sc | = | SSLContext.getInstance(”SSL”); | a fake sample generated by the generator. In the discriminator |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| // Using the generic ”SSL” version instead of the TLS version poses | part, a convolutional neural network (CNN) is used to classify the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| a downgrade risk | input samples, and the discriminative ability of the model is further |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3.1.3 | Code Pattern Matching. | Bypass the checkServerTrusted() | enhanced by the Leaky ReLU activation function and the batch |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| method for certificate validation or implement the method empty; | normalization layer (Batch Normalization). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| @Override | 퐷 | ( | 푋 | ) | = | 휎 | ( | 푊 | 3 | LeakyReLU | ( | 푊 | 2 | LeakyReLU | ( | 푊 | 1 | 푋 | + | 푏 | 1 | ) + | 푏 | 2 | ) + | 푏 | 3 | ) |
| } | [ | ( | ( | ) | ) | ] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| @Override | 퐿 | 퐺푃 | = | 휆 | · | 퐸 | 푥 | ˜ | ∼ | 푃 | 푥 | ∇ | 푥 | ˜ | 퐷 | 푋 | ˜ | − | 1 |  |  |  |  |  |  |  |  |  |
| public X509Certificate[] getAcceptedIssuers() { | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| return trustManager.getAcceptedIssuers(); | 푋 | ˜ | represents interpolated samples between real and generated data, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| } | ensuring that the discriminator does not focus on trivial solutions. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| at a ratio of 7:1.5:1.5, ensuring a consistent distribution of positive | 퐶퐸 | and an adversarial loss | 퐿 | 푎푑푣 | , with the final loss |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and negative samples across all subsets. | 푇 표푡푎푙 | = | 퐿 | 퐶퐸 | + | 훾 | · | 퐿 | 푎푑푣 | , where | 훾 | is a scaling factor. The key |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| To improve model robustness against evasion techniques such as | Through continuous training, the generator learns the distribu- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| code obfuscation or forged certificate validation logic, a gener- | tion of vulnerability samples, producing more realistic forgeries. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ative adversarial network is introduced. Figure 3 illustrates the | Once trained, forged and real vulnerability samples are combined |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| overall workflow of the WGAN-based adversarial training process | into an adversarial set to retrain the detection model, strengthening |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| for enhancing the robustness of the vulnerability detection model. | its ability to identify fake vulnerabilities and unknown attacks. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The adversarial sample generation module leverages a Wasserstein | The two are constantly playing in the training process, so that |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| GAN to synthesize realistic adversarial examples based on feature | the generator gradually learns the distribution characteristics of the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| vectors extracted during static analysis. These samples are incorpo- | vulnerability samples and generates more realistic forged samples. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| rated into the training set to enhance the model’s ability to detect | After the training of the generator network is completed, we mix |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Page 4

GAIIS 2025, February 21–23, 2025, Hangzhou, China Yong Fang

Figure 3: WGAN Training Process.

Figure 4: Impact of Multi-Turn ICL Optimization on TLS Certificate Vulnerability Detection Accuracy.

| the generated forged samples with the real vulnerability samples to | become noise during the training process and reduce the robustness |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| form the adversarial sample set, and use the adversarial sample set | of the detection model. To further improve the effectiveness of the |  |  |  |  |  |  |  |
| to re-train the vulnerability detection model so that it has a stronger | training data, we introduce In-Context Learning to screen and |  |  |  |  |  |  |  |
| detection capability in the fake vulnerability and unknown attack | optimize the adversarial samples and provide more realistic and |  |  |  |  |  |  |  |
| scenarios. | attack-valued training data for the detection model. The generated |  |  |  |  |  |  |  |
| 푋 | train | = | 푋 | real | ∪ | 푋 | adv | forged samples are analyzed and screened using ChatGPT-4 or |
| where: | 푋 | real | is a real vulnerability sample | 푋 | adv | is a fake vulnerabil- | DeepSeek-API to achieve iterative optimization between sample |  |
| ity sample generated by the generator. | generation and detection model[8]. |  |  |  |  |  |  |  |
| The loss function of the detection model consists of the real | Through multiple rounds of ICL optimization, the accuracy of |  |  |  |  |  |  |  |
| vulnerability detection loss and the adversarial sample detection | ChatGPT and DeepSeek in TLS certificate vulnerability detection |  |  |  |  |  |  |  |
| loss together | improves from 23%–26% to 60%–70%. The first three iterations show |  |  |  |  |  |  |  |
| 퐿 | = | 퐿 | CE | + | 휆퐿 | adv | noticeable fluctuations, reflecting early instability, while the last |  |
| 퐿 | CE | is the cross-entropy loss for detecting the classification of real | two stabilize, indicating performance saturation. Figure 4. Effect |  |  |  |  |  |
| samples. | 퐿 | adv | is the detection loss of the antagonistic samples. | 휆 | is | of multi-turn ICL optimization on TLS certificate vulnerability de- |  |  |
| a balancing parameter to regulate the weights of both. | tection accuracy. The graph shows the improvement in detection |  |  |  |  |  |  |  |

accuracy for both ChatGPT and DeepSeek models over five itera-

3.3 Optimization Module Based on In-Context tions. As the number of iterations increases, both models exhibit

a significant increase in accuracy, with ChatGPT slightly outper-

Learning

forming DeepSeek, highlighting the effectiveness of iterative ICL

After completing the generation of adversarial samples for the optimization in improving vulnerability detection capabilities.

generative network, we found that some of the generated samples

may have poor quality or low attack value. These samples may

234

---

## Page 5

Wasserstein GAN-Based Android Certificate Validation Vulnerability Detection Framework GAIIS 2025, February 21–23, 2025, Hangzhou, China

Table 1: WGAN-based vulnerability detection framework performs.

Method Dataset (APK Count) F1 Score False Positive Rate (%) Adversarial

Training)

퐿 ICL = 훼퐿 validity + 훽퐿 plausibility + 훾퐿 adversariality

퐿 validity : the authenticity of the vulnerability

percentage of normal code that is incorrectly labeled as a vulner-

ability. Detection Precision: measures the proportion of detected

vulnerabilities that are actually real vulnerabilities. Experimental

235

Sample Defense

Improvement

and robustness.

5 Conclusion

tive adversarial networks, and ICL-assisted parameter optimization.

detection.

References

Computer and Communications Security (CCS’12). ACM, New York, NY, 50–61.

[2] Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley,

[3] Martin Arjovsky, Soumith Chintala, and Léon Bottou. 2017. Wasserstein GAN. In

[4] David Sounthiraraj, Justin Sahs, Garret Greenwood, Zhiqiang Lin, and Latifur

| Traditional Static Analysis | 1,200 | 0.72 | 18.3 | - |
| --- | --- | --- | --- | --- |
| WGAN-GEN | 1,200 + 800 Generated | 0.85 | 12.1 | 22% |
| WGAN-FEAT | 1,200 | 0.89 | 9.7 | 35% |
| WGAN-ADV (Adversarial | 1,200 + 500 Adversarial | 0.91 | 7.2 | 58% |
| ICL enhances vulnerability detection by iteratively optimizing | calls, and implementing classes. This further increases the F1 score |  |  |  |
| the generator. It analyzes samples, provides feedback, and refines | to 0.89, reduces the false positive rate to 9.7%, and improves adver- |  |  |  |
| parameters to generate more realistic attack behaviors. The feature | sarial defense capability to 35%, enhancing the model’s ability to |  |  |  |
| vectors of forged and real vulnerability samples are combined as | detect complex vulnerability paths and obfuscated code. WGAN- |  |  |  |
| labeled training data[7]. ICL evaluates samples based on authentic- | ADV introduces real adversarial samples into the training process. |  |  |  |
| ity, scenario reasonableness, and deception ability. Non-compliant | This configuration achieves the highest F1 score of 0.91, the lowest |  |  |  |
| samples prompt generator adjustments to enhance deception. A | false positive rate of 7.2%, and the strongest adversarial robustness |  |  |  |
| comprehensive loss function ensures balance among authenticity, | at 58%. These results demonstrate that progressive enhancements |  |  |  |
| reasonableness, and aggressiveness. | through sample generation, feature fusion, and adversarial training |  |  |  |
| The loss function is as follows: | substantially improve the model’s accuracy, false positive control, |  |  |  |
| 퐿 | plausibility | : the plausibility of the vulnerability scenario | This paper presents a novel framework for detecting TLS certificate |  |
| 퐿 | adversariality | : the ability of the generated samples to deceive the | validation vulnerabilities in Android applications, integrating static |  |
| detection model. | analysis, machine learning–based detection, Wasserstein genera- |  |  |  |
| 4 | Experiments | The framework aims to enhance the accuracy and robustness of tra- |  |  |
| To evaluate the effectiveness of the proposed method, this study con- | ditional detection tools. Experimental results show that it achieves |  |  |  |
| ducted experiments using the AndroZoo dataset, which contains | an F1 score of 0.91 and reduces the false positive rate to 7.2%, sig- |  |  |  |
| 2,000 Android APK files. These applications cover both domes- | nificantly outperforming baseline methods. Through adversarial |  |  |  |
| tic and international mainstream applications and contain a large | training, the model demonstrates improved resilience against eva- |  |  |  |
| number of known TLS certificate validation vulnerabilities. To vali- | sion attacks. We identify four critical categories of TLS certificate |  |  |  |
| date the performance of the framework, we compare the proposed | validation vulnerabilities: misconfigured trust anchors, weak cryp- |  |  |  |
| WGAN-based detection framework with traditional static analysis | tographic suite usage, certificate chain validation flaws, and missing |  |  |  |
| tools. This study focuses on the following performance metrics: | hostname verification. These findings highlight prevalent security |  |  |  |
| F1 Score: used to measure the accuracy and recall of the detection | weaknesses and demonstrate the potential of combining genera- |  |  |  |
| in an integrated manner. False Positive Rate (FPR): measures the | tive learning with static analysis for more effective vulnerability |  |  |  |
| results show that the WGAN-based vulnerability detection frame- | [1] Sascha Fah, Marian Harbach, Thomas Muders, Lars Baumgärtner, Bernd Freisleben, |  |  |  |
| work performs well in these evaluation metrics and significantly | and Matthew Smith. 2012. Why Eve and Mallory Love Android: An Analysis |  |  |  |
| outperforms traditional static analysis tools. The following is the | of Android SSL (In)Security. In Proceedings of the 2012 ACM Conference on |  |  |  |
| detailed performance: | https://doi.org/10.1145/2382196.2382205. Martin Arjovsky, Soumith Chintala, Léon |  |  |  |
| As shown in Table 1, this study experimentally evaluates the | Bottou Proceedings of the 34th International Conference on Machine Learning, |  |  |  |
| detection performance of the WGAN-based model under differ- | PMLR 70:214-223, 2017.Wasserstein Generative Adversarial Networks |  |  |  |
| ent configurations. WGAN-GEN utilizes a generative adversarial | Sherjil Ozair, Aaron Courville, and Yoshua Bengio. 2014. Generative adversarial |  |  |  |
| network to synthesize representative vulnerability samples. This | networks. In Proceedings of the 27th International Conference on Neural Infor- |  |  |  |
| improves the F1 score from 0.72 to 0.85, reduces the false posi- | mation Processing Systems (NIPS’14), MIT Press, Cambridge, MA, 2672–2680. |  |  |  |
| tive rate to 12.1%, and enhances adversarial robustness by 22%, | Proceedings of the 34th International Conference on Machine Learning (ICML’17). |  |  |  |
| indicating that sample augmentation helps the model better learn | JMLR.org, Sydney, Australia, 214–223. |  |  |  |
| vulnerability patterns. WGAN-FEAT incorporates static feature | Khan. 2014. SMV-Hunter: Large scale, automated detection of SSL/TLS man-in- |  |  |  |
| fusion, including permission declarations, certificate-related API | the-middle vulnerabilities in Android apps. In Proceedings of the Network and |  |  |  |

---

## Page 6

| GAIIS 2025, February 21–23, 2025, Hangzhou, China | Yong Fang |
| --- | --- |
| Distributed System Security Symposium (NDSS’14). Internet Society, San Diego, | Proceedings of the ACM Turing Celebration Conference - China (ACM TURC |
| CA, 1–14. | 2019). ACM, 1–9. |
| [5] Lucky Onwuzurike and Emiliano De Cristofaro. 2015. Danger is my middle name: | [8] Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, Qiushi Sun, Chengyou Jia, |
| experimenting with SSL vulnerabilities in Android apps. In Proceedings of the | Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, and Yu Qiao. 2024. |
| 8th ACM Conference on Security & Privacy in Wireless and Mobile Networks | OS-ATLAS: A foundation action model for generalist GUI agents. arXiv preprint |
| (WiSec’15). ACM, New York, NY, 1–6. | arXiv:2410.23218. https://arxiv.org/abs/2410.23218. |
| [6] Android 14 Security Bulletin. 2023. https://source.android.com/docs/security/ | [9] Zhendong Hei, Weifang Sun, Haiyang Yang, Meipeng Zhong, Yanling Li, Anil |
| bulletin | Kumar, Jiawei Xiang, Yuqing Zhou. Novel domain-adaptive Wasserstein generative |
| [7] Yingjie Wang, Xing Liu, Weixuan Mao, and Wei Wang. 2019. DCDroid: Automated | adversarial networks for early bearing fault diagnosis under various conditions. |
| detection of SSL/TLS certificate verification vulnerabilities in Android apps. In | 2025. https://doi.org/10.1016/j.ress.2025.110847 |

236
