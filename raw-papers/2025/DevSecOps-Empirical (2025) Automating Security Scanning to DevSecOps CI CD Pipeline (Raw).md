---
title: "Implementing and Automating Security Scanning to a DevSecOps CI/CD Pipeline"
creator: "Microsoft® Office Word 2007"
pages: 6
---

# Implementing and Automating Security Scanning to a DevSecOps CI/CD Pipeline

> **總頁數**：6 頁

---

## Page 1

2023 World Conference on Communication & Computing (WCONF)

Raipur, India. July 14-16, 2023

Implementing and Automating Security Scanning to

a DevSecOps CI/CD Pipeline

| Manohar Marandi | A.Bertia | Salaja Silas |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Computer Science and Engineering | Computer Science and Engineering | Computer Science and Engineering |  |  |  |  |
| Karunya Institute of Technology and | Karunya Institute of Technology and | Karunya Institute of Technology and |  |  |  |  |
| Sciences | Sciences | Sciences |  |  |  |  |
| Coimbatore, India | Coimbatore, India | Coimbatore, India |  |  |  |  |
| manoharmarandi@karunya.edu.in | bertia@karunya.edu | salaja_cse@karunya.edu |  |  |  |  |
| Abstract | — | With the growing adoption of DevOps and the | every stage [2]. DevSecOps aims to address the security risks |  |  |  |
| rise | of | containerization | and | Continuous | Integration/ | that arise when software is deployed at a rapid pace [6]. |

Continuous Deployment (CI/CD) in software development life

| cycle (SDLC) has brought significant changes to the industry. | Security scanning is a key aspect of the DevSecOps |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| While these methods offer many advantages, they also present | pipeline, and it is critical for discovering vulnerabilities early |  |  |  |  |  |  |  |  |  |  |  |
| unique security challenges, as containerized applications are | in | the | development | cycle. | Traditional | security | scanning |  |  |  |  |  |
| more | susceptible | to | cyber | attacks | than | traditional | methods | were | time-consuming | and | required | manual |
| deployments, | security | has | become | a | significant | concern. | involvement, leading to delays in the software development |  |  |  |  |  |
| Security | scanning | is | an | essential | aspect | of | DevSecOps | process. Implementing and automating security scanning will |  |  |  |  |
| pipelines, involving the analysis of software images deployed to | help | minimise | the | time | required | to | find | and | patch |  |  |  |
| cloud environments to identify vulnerabilities and mitigate | vulnerabilities, making the process more efficient [5]. |  |  |  |  |  |  |  |  |  |  |  |

security threats. This study will involve a thorough review of

existing literature on containerization and CI/CD security and

will analyze current security practices and measures used in

containerization-based CI/CD systems. Various tools and

techniques have been proposed for implementing and

automating image security scanning in DevSecOps pipelines by

integrating DAST (Dynamic application security testing) and

SAST (Static application security testing) vulnerability

scanning. . This research proposes a method for implementing

and automating image security scanning using the Snyk and

StackHawk tool, which provides a dashboard for SAST and

DAST separately for monitoring scanning results and

automating vulnerability fixes. The proposed method can be

integrated with GitHub, enabling automatic vulnerability

scanning and fixing during the build process. The research

evaluates the effectiveness of the proposed method by

demonstrating the ability of the method to improve the

security of DevSecOps pipelines. The findings suggest that the

proposed method can enhance the overall security of the Fig. 1. DevSecOps

application by reducing the time to detect and fix

vulnerabilities. To assure the security of containerized CICD pipelines,

organisations need to implement both Static Application

| Keywords | — | Security | Scanning, | DevSecOps, | Continuous | Security Testing (SAST) and Dynamic Application Security |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Integration | and | Continuous | Deployment | (CICD), | Static | Testing | (DAST) | tools[10]. | Static | Application | Security |
| application security testing(SAST), Dynamic application security | Testing | (SAST) | is | a | testing | methodology | that | analyzes |  |  |  |

testing (DAST)

source code to find and mitigate security vulnerabilities

[9,15]. On the other hand, Dynamic Application Security

I. INTRODUCTION

Testing (DAST) is a method of testing applications while

| As organizations move towards the adoption of DevOps | they | are | operating | to | discover | vulnerabilities | [2]. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| and agile development approaches, the increasing popularity | Implementing SAST and DAST tools in the containerized |  |  |  |  |  |  |
| of | containerized | Continuous | Integration | and | Continuous | CICD pipeline can help to identify and mitigate security |  |
| Deployment (CI/CD) pipelines have become a vital aspect of | risks throughout the entire software development lifecycle. |  |  |  |  |  |  |

modern software development workflows. Containerization

2023 World Conference on Communication & Computing (WCONF) | 979-8-3503-1120-4/23/$31.00 ©2023 IEEE | DOI: 10.1109/WCONF58270.2023.10235015 has various benefits such as portability, scalability, and The proposed method in this research paper involves

| consistency across different environments. [19], however | implementing | and | automating | security | scanning | to | a |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| security | becomes | an | integral | part | of | the | software | DevSecOps CI/CD pipeline. This approach incorporates the |  |
| development process. The incorporation of security into the | use of a dashboard to monitor security scanning using Snyk |  |  |  |  |  |  |  |  |
| DevOps pipeline is known as DevSecOps. As shown in fig 1. | and StackHawk tools. The dashboard allows for continuous |  |  |  |  |  |  |  |  |
| This approach integrates security into the entire software | monitoring of vulnerabilities and provides real-time updates |  |  |  |  |  |  |  |  |
| development | life | cycle | (SDLC) | , | from | planning | to | on the status of the scanning process [7,8]. The proposed |  |
| deployment, and emphasizes the importance of security in | method | also | includes | the | ability | to | automate | and | fix |
| 979-8-3503-1120-4/23/$31.00 ©2023 IEEE | 1 |  |  |  |  |  |  |  |  |


---

## Page 2

| vulnerabilities in GitHub, which further reduces the time | system. In [10] (Díaz, Pérez, Lopez, Mena and Yagüe) they |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| required to fix vulnerabilities and ensures that vulnerabilities | recommend | self | service | cybersecurity | monitoring | as | an |  |
| are fixed before code is deployed into production [1]. | enabler | to | incorporate | security | practices | in | a | DevOps |

This research paper aims to investigate the effectiveness

of implementing and automating security scanning in a

DevSecOps pipeline using the proposed method. The

research will evaluate the impact of this approach on the

software development process, the efficiency of vulnerability

identification and remediation, and the overall security of the

software developed. The paper will implement in addition to

what was discussed in case studies and also integrate static

testing and automate the process [17].

several hours to 3-4 minutes.

reports, and a project management system to build, regress

Buijtenen, Fransen, and Turkmen) access a way to integrate

three automated dynamic testing techniques into a CI/CD

pipeline for security testing. They conducted an empirical

analysis of the overhead introduced by the automated

dynamic testing techniques and identified unique

research/technology challenges in DevSecOps, proposing

preliminary solutions.

process can create a secure environment and more protected

2

framework. They underline that the self service

monitoring/alerting helps dissolving boundaries between

development, operations, and security teams by exposing

access to critically important security indicators, which

encourages a common culture and continuous development.

[7] (Ahmed, Francis) where the authors suggest that

integrating security into the DevOps process is essential to

ensure secure applications and reduce risk. They argue that

DevSecOps is an effective practice for integrating security

into the development process. In [12](Zunnurhain, Duclervil)

inspection is another technique to guarantee security is

Overall, the literature emphasises the importance of

The proposed methodology for this research focuses on

automating image security scanning in a DevSecOps CI/CD

pipeline and improving time efficiency. The literature review

highlights the importance of integrating security into the

software development process and the need for faster and

more automated security scanning to detect vulnerabilities at

an early stage. Therefore, the proposed technique will focus

| The remainder of this research paper is structured as | the | researchers | cover | cyber | security | and | several | agile |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| follows: Section 2 provides a literature review of the existing | software development life-cycle (SDLC) approaches. They |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| research on implementing and automating security scanning | focus | on | DevSecOps | and | build | criteria | for | a | new | and |  |  |  |  |  |  |  |
| in a DevSecOps pipeline. Section 3 describes the proposed | effective and efficient DevSecOps approach. The authors |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| methodology used in this research. Section 4 presents the | suggest that DevSecOps models are more trustworthy than |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Implementation | part | and | followed | by | section | 5 | that | is | earlier models and that the requirements for a new and |  |  |  |  |  |  |  |  |
| Performance. Then Section 6 is Result and analysis of the | successful | DevSecOps | model | were | defined. | They | have |  |  |  |  |  |  |  |  |  |  |
| study. Finally, Section 7 gives the conclusion of the study. | designed a website that provides for better security. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| II. | LITERATURE REVIEW | The | use | of | automated | tools | for | security | and | code |  |  |  |  |  |  |  |
| The | use | of | DevSecOps | practices | is | becoming | included | into | the | software | development | process. | In | [4] |  |  |  |
| increasingly popular in software development environments | (Petrovi | ć | , Cankar, Luzar,) the authors present a Python- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| to ensure security is integrated into the software development | based tool which allows automation of static code analysis |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| process. This makes the security scanning faster, and it can | and | tests | for | Infrastructure | as | Code | (IaC) | scripts. | The |  |  |  |  |  |  |  |  |
| detect security vulnerabilities as early as possible as seen in | suggested technology was assessed in different instances |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the | paper | [2] | (Putra | and | Kabetta) | presented | a | way | to | when it comes to terraform scripts. They observed that the |  |  |  |  |  |  |  |
| integrate DevSecOps within an Agile Software development | tool enables automation of code inspection and security |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| life cycle utilising GitLab and Docker technologies. The | checks, therefore boosting the quality of IaC scripts and |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| research utilised a hybrid of automated security static testing | assuring compliance with standards. in [18] (Hely, Bancel, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and dynamic security testing to assure the security. The | Flottes, Rouzeyre) the authors present a scan chain integrity |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| findings demonstrated that DevSecOps provides a solution to | detection technique, which supports both automated design |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the | difficulties | of | time-consuming | build, | test, | and | flow and IP reuse environment. They argue that the scan path |  |  |  |  |  |  |  |  |  |  |
| deployment phases in an Agile SDLC context. Automation | is a profound danger for secure chips, and scanning-based |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| of the deployment process lowered the time taken from | cyber attacks have been shown against DES or AES. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [3] (Chen and Suo) developed a combined operation and | integrating security into the software development process, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| maintenance | platform | of | DevSecOps | to | increase | the | particularly in Agile SDLC environments, and highlights |  |  |  |  |  |  |  |  |  |  |
| efficiency of company RnD (research and development) and | DevSecOps as an effective practice for achieving this goal. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| comprehend security protection automation. DevSecOps is | However, there are opportunities for further investigation, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| of considerable relevance to ensuring the security of apps | which suggests the need for faster and more automated |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and infrastructure. [13] (Sun, Cheng, Qu, and Li) designed | security scanning to detect vulnerabilities at an early stage |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and | implemented | a | security | test | pipeline | based | on | and Continuous monitoring of. The literature recommends |  |  |  |  |  |  |  |  |  |
| DevSecOps to seamlessly integrate security testing into the | the use of automated security static testing and dynamic |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| software development process. They created a management | security testing tools to ensure code inspection and security |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tool to uniformly manage and show security testing results in | checks are performed efficiently and effectively. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and manage closed-loop security issues. [17] (Rangnau, van | III. | PROPOSED METHODOLOGY |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [16] (Rahul, Balabhadruni, Kharvi, and Manu) discussed | on combining one of the popular image scanning tools, Snyk |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| how DevSecOps provides security while maintaining the | and StackHawk, with a CI/CD pipeline to automate Static |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| speed and agility of DevOps. They demonstrated how open- | Application | Security | Testing | (SAST) | and | Dynamic |  |  |  |  |  |  |  |  |  |  |  |
| source tools can be used to implement DevSecOps and | Application Security Testing (DAST) scanning throughout |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| provide | faster | response | time | and | fend | off | attacks. | the | build | process. | This | will | help | to | ensure | that | code |
| Implementing and integrating security as part of the pipeline | inspection and security checks are performed efficiently and |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


---

## Page 3

effectively, ultimately improving the overall security of the x Code: The secure coding stage involves

software development process. implementing security measures into the code, such

In this project, a dashboard was created to monitor the

security scanning findings generated by Snyk and

StackHawk. The dashboard gave a real-time view of the

A. Tool Selection

in software applications.

produces detailed vulnerability reports with specific remedial

actions and interacts smoothly with CI/CD processes [8].

complete solution to security scanning in a DevSecOps CI

3

as ensuring that code is free of common

vulnerabilities like SQL injection and cross-site

scripting (XSS).

process.

x Release: The penetration testing stage involves

x Monitor: The continuous monitoring stage involves

ongoing monitoring of the application to detect and

platform. To build, execute, and distribute the essential apps

programme Docker[21] is used.

With the help of Docker, applications are containerized

and run in the CI environment either locally or remotely.

Github Actions was chosen as the CI platform for this study,

as it offers CI/CD pipelines as a service in a cloud

environment.

In order to test our security scanning tool an application

is needed. An already vulnerable app was selected “ Damn

Vulnerable Web Application ” [20] as the study target

application. The application is a designed vulnerable website

purposes. The integration of image scanning tools,

security misconfigurations, and other security issues.

| application's security status, allowing developers to easily | x | Build: | The | SAST | (Static | Application | Security |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| identify and fix problems. The automation and remediation | Testing) stage involves using automated tools to |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| functionalities of Snyk and StackHawk were connected with | scan | the | code | for | vulnerabilities, | including | both |  |  |  |  |  |  |  |  |
| GitHub | to | automate | the | patching | of | vulnerabilities | known and potential vulnerabilities. This helps to |  |  |  |  |  |  |  |  |
| discovered during security scanning. | catch | vulnerabilities | early | in | the | development |  |  |  |  |  |  |  |  |  |
| The | selection | of | appropriate | tools | is | crucial | for | the | x | Test: | The | DAST | (Dynamic | Application | Security |
| effective deployment of security scanning in a DevSecOps | Testing) stage involves testing the application in a |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CI/CD pipeline. In this research, two prominent security | running environment to simulate real-world attacks |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| scanning tools, Snyk and StackHawk, were selected based on | and identify any security vulnerabilities that were |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| their efficiency in discovering and addressing vulnerabilities | not caught during the SAST stage. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Snyk | is | a | cloud-based | security | scanning | tool | that | carrying out further testing to identify vulnerabilities |  |  |  |  |  |  |  |
| specializes | in | identifying | vulnerabilities | in | open-source | that may have been missed in previous stages. This |  |  |  |  |  |  |  |  |  |
| libraries and containers. Snyk is easy to connect with CI/CD | may involve simulating an attack on the application |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| processes and includes automatic remediation features [7]. | to identify weaknesses that could be exploited. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| StackHawk is a cloud-based dynamic application security | x | Deploy: The deployment stage involves releasing the |  |  |  |  |  |  |  |  |  |  |  |  |  |
| testing (DAST) platform that enables security testing. It | application to the production environment. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The combination of Snyk and StackHawk provides a | respond to any security incidents that may arise. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CD pipeline. Snyk's focus on SAST and StackHawk's DAST | IV. | IMPLEMENTATION |  |  |  |  |  |  |  |  |  |  |  |  |  |
| capabilities | allow | for | a | more | thorough | scan, | while | In this section, a detailed description of the dynamic |  |  |  |  |  |  |  |
| StackHawk's automation and remediation features improve | security testing strategy implementation is provided, along |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| efficiency and efficacy. The selection of these technologies | with an implementation diagram (Figure 3). Together with |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| was based on their effectiveness, automation capabilities, | the | technologies | used | to | automate | security | testing, | To |  |  |  |  |  |  |  |
| and simplicity of connection with CI/CD pipelines. | develop a test environment that can be employed with any CI |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| B. DevSecOps Pipeline Design | used in the specified test scenarios, virtualization software |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Fig. 2. | DevSecOps Pipeline | and was created for educational and security tool testing |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The term "Plan - Code - Build - Test - Release - Deploy - | specifically Snyk and StackHawk, into the CI/CD pipeline |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Monitor" is a commonly used sequence of stages in the | for DevSecOps security scanning involves several steps. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| software development | life | cycle (SDLC), known | as the | First, the respective APIs and integrations of Snyk and |  |  |  |  |  |  |  |  |  |  |  |
| "DevOps pipeline." The term "DevSecOps pipeline" refers to | StackHawk are configured in the CI/CD pipeline. This may |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| a DevOps pipeline that includes security considerations at | involve | setting | up | authentication, | API | keys, | and | other |  |  |  |  |  |  |  |
| each stage of the SDLC. | necessary configurations to enable communication between |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| This paper has further specified each stage in the pipeline | the CI/CD pipeline and the scanning tools. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| to include specific security measures. These measures are as | Next, the image scanning tools are invoked during the |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| follows: | appropriate stages of the CI/CD pipeline. For example, Snyk |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| x | Plan: The security test plan stage involves planning | and StackHawk may be triggered to scan container images |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and designing the security tests that will be carried | during the build or deployment stages of the pipeline. The |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| out at each stage of the pipeline. | scanning tools analyze the images for known vulnerabilities, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


---

## Page 4

Fig. 3. Architecture

The output from the image scanning tools is then

collected and processed to generate meaningful results. This

may involve parsing the scan results, extracting relevant

information such as vulnerability details, severity levels, and

recommended fixes. The processed results are then

integrated into respective dashboards, such as the Snyk and

StackHawk dashboards, for easy visualization and

monitoring of the security status of container images.

The integration of Snyk and StackHawk in the CI/CD

of container images, providing early detection of

vulnerabilities and security issues. This allows for timely

V. PERFORMANCE

The performance evaluation of the security scanning

process in the DevSecOps CI/CD pipeline, using Snyk and

StackHawk, involves assessing the effectiveness and

efficiency of the vulnerability detection and reporting

mechanism through the following activities:

A. Detection of Vulnerabilities

Snyk and StackHawk are used to scan the Dockerized

application for vulnerabilities, security misconfigurations,

and integrated into the CI/CD pipeline, ensuring that security

testing is performed at each stage of the pipeline, from code

commit to deployment. shown in fig 4.(a) and 4 (b) are the

number of vulnerabilities detected and severity of the

vulnerability.

Fig. 4. (a) SAST Report

B. Dashboard Reporting

provides a clear overview of the vulnerabilities found, their

severity levels, and other relevant details. As shown in the

fig 5 (a) and 5 (b) below

Fig. 5. (b). StackHawk Dashboard

C. Performance Metrics

Performance metrics such as the number of

vulnerabilities detected, the severity levels of the

vulnerabilities, the time taken for the scanning process are

measured to assess the efficiency and effectiveness of the

implemented security scanning process.

4

| pipeline enables automated and continuous security scanning | Fig. 4. (b) DAST Report |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| remediation and ensures that only secure container images | The | results | of | the | security | scans | are | collected | and |
| are deployed in the production environment, enhancing the | processed, and the vulnerabilities detected by Snyk and |  |  |  |  |  |  |  |  |
| overall security posture of the DevSecOps CI/CD pipeline. | StackHawk are displayed in a dashboard. The dashboard |  |  |  |  |  |  |  |  |
| and other security issues. The scanning process is automated | Fig. 5. | (a) Snyk Dashboard |  |  |  |  |  |  |  |


*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

*[Image: Page 4 Image]*

---

## Page 5

TABLE I.

scanning process

to automatically fix vulnerabilities detected during security

scanning, saving time and improving efficiency. The

integration of image scanning capabilities ensured that

the application.

developers with a real-time view of the security state of their

the security posture of containerized apps in a DevSecOps

security scanning using Snyk and StackHawk tools, is an

effective approach to improving the security posture of

5

security scanning that ensures vulnerabilities are quickly and

effectively remediated.

The automated remediation features of Snyk and

StackHawk save time and improve efficiency, while the

integration of image scanning ensures that container images

are thoroughly scanned for vulnerabilities before they are

deployed. The dashboard developed for this research

provides developers with a real-time view of the security

status of their applications and container images, allowing

VIII. FUTURE SCOPE

In addition to the proposed method for implementing and

StackHawk tools, there are several avenues for future

pipelines. extending the proposed method by integrating

additional security scanning techniques or tools would

deployments. Future research should explore strategies to

deployment methodologies.

REFERENCE

Available: https://www.freecodecamp.org/news/oss-security-best-

practices/

Integrating Static and Dynamic Security Testing in CI/CD Pipelines,"

2022 IEEE International Conference of Computer Science and

Conference on Software Engineering and Service Science (ICSESS),

Code Inspection Using Python-Based DevSecOps Tool," 2022 30th

Telecommunications Forum (TELFOR), Belgrade, Serbia, 2022, pp.

[6] IBM. (2021). "DevSecOps: A Comprehensive Overview." IBM.

Available: https://snyk.io/solutions/devsecops/.

[8] StackHawk, "Automate Security Testing in CI/CD," StackHawk,

2021. [Online]. Available:

(HST), Waltham, MA, USA

| Fig. 6. | Total Vulnerabilities detected | for quick identification and remediation of vulnerabilities. |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Time taken for | SAST - Snyk | 19 sec | automating image security scanning using the Snyk and |  |  |  |  |  |  |  |  |  |  |  |
| DAST - Stackhawk | 2 min 1 sec | exploration | in | the | field | of | securing | DevSecOps | CI/CD |  |  |  |  |  |
| Based on the performance evaluation, the research paper | enhance the overall effectiveness of vulnerability detection. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| aims to provide insights into the accuracy, effectiveness, and | This | could | involve | incorporating | other | security | testing |  |  |  |  |  |  |  |
| efficiency of the implemented security scanning process | approaches | like | fuzz | testing, | manual | code | review, | or |  |  |  |  |  |  |
| using | Snyk | and | StackHawk | in | the | DevSecOps | CI/CD | behavioral | analysis | to | provide | a | more | comprehensive |
| pipeline, and how it contributes to enhancing the security of | assessment of application security. Moreover, scalability and |  |  |  |  |  |  |  |  |  |  |  |  |  |
| the Dockerized application throughout the CI/CD process. | performance | are | important | considerations | for | large-scale |  |  |  |  |  |  |  |  |
| VI. | RESULT | optimize | resource | allocation, | parallelize | or | distribute |  |  |  |  |  |  |  |
| The implementation and automation of security scanning | scanning tasks, and leverage cloud-based infrastructure to |  |  |  |  |  |  |  |  |  |  |  |  |  |
| using Snyk and StackHawk tools in a DevSecOps CI/CD | enhance | the | efficiency | of | the | CI/CD | pipeline | without |  |  |  |  |  |  |
| pipeline, | along | with | the | integration | of | image | scanning, | compromising security. These advancements will contribute |  |  |  |  |  |  |
| proved to be an effective approach to improving the security | to | the | ongoing | efforts | to | strengthen | the | security | of |  |  |  |  |  |
| posture | of | containerized | applications. | The | automated | DevSecOps CI/CD pipelines and mitigate the unique security |  |  |  |  |  |  |  |  |
| remediation features of Snyk and StackHawk were leveraged | challenges | posed | by | containerization | and | continuous |  |  |  |  |  |  |  |  |
| container images were thoroughly scanned for vulnerabilities | [1] | Sonya Moisset, "Open Source Software Security Handbook | – | Best |  |  |  |  |  |  |  |  |  |  |
| before they were deployed, improving the overall security of | Practices for Securing Your Projects," freecodecamp, 2023. [Online]. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The | dashboard | developed | for | this | research | provided | [2] | A. M. Putra and H. Kabetta, "Implementation of DevSecOps by |  |  |  |  |  |  |
| apps and container images, enabling for speedy identification | Information Technology (ICOSNIKOM), Laguboti, North Sumatra, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| and correction of vulnerabilities. This better insight into the | Indonesia, | 2022, | pp. | 1-6, | doi: |  |  |  |  |  |  |  |  |  |
| security of the programme allows for a more proactive | 10.1109/ICOSNIKOM56551.2022.10034883. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| approach to security, rather than depending primarily on | [3] | T. Chen and H. Suo, "Design and Practice of Security Architecture |  |  |  |  |  |  |  |  |  |  |  |  |
| reactive vulnerability management. | via | DevSecOps | Technology," | 2022 | IEEE | 13th | International |  |  |  |  |  |  |  |
| Overall, the implementation and automation of security | Beijing, | China, | 2022, | pp. | 310-313, | doi: |  |  |  |  |  |  |  |  |
| scanning | applying | Snyk | and | StackHawk | technologies, | 10.1109/ICSESS54813.2022.9930212. |  |  |  |  |  |  |  |  |
| together with the integration of image scanning, improved | [4] | N. Petrovi | ć | , M. Cankar and A. Luzar, "Automated Approach to IaC |  |  |  |  |  |  |  |  |  |  |
| CI/CD pipeline. The automation and integration of these | 1-4, doi: 10.1109/TELFOR56187.2022.9983681. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tools allowed for a more efficient and effective approach to | [5] | TestingXperts | (2022). | “ | Embedding | Security | Testing | in | DevOps |  |  |  |  |  |
| security | scanning, | minimizing | time | and | increasing | the | CI/CD | Pipeline | ” | [Online]. | Available: |  |  |  |
| overall security of the application. | https://www.testingxperts.com/blog/security-testing-in-devops |  |  |  |  |  |  |  |  |  |  |  |  |  |
| VII. | CONCLUSION | [Online]. Available: https://www.ibm.com/topics/devsecops |  |  |  |  |  |  |  |  |  |  |  |  |
| To | conclude, | the | implementation | and | automation | of | [7] | Snyk, "Snyk Security Testing for DevSecOps," Snyk, 2021. [Online]. |  |  |  |  |  |  |
| containerized applications in a DevSecOps CI/CD pipeline. | https://www.stackhawk.com/solutions/automated-security-testing/ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| The selection of Snyk and StackHawk for Static Application | [9] | A. Masood and J. Java, "Static analysis for web service security - |  |  |  |  |  |  |  |  |  |  |  |  |
| Security Testing (SAST) and Dynamic Application Security | Tools & techniques for a secure development life cycle," 2015 IEEE |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Testing | (DAST) | provide | a | comprehensive | approach | to | International Symposium on Technologies for Homeland Security |  |  |  |  |  |  |  |


*[Image: Page 5 Image]*

---

## Page 6

| [10] J. Díaz, J. E. Pérez, M. A. Lopez-Peña, G. A. Mena and A. Yagüe, | (SecDev), | Cambridge, | MA, | USA, | 2018, | pp. | 134-134, | doi: |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| "Self-Service Cybersecurity Monitoring as Enabler for DevSecOps," | 10.1109/SecDev.2018.00030. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| in | IEEE | Access, | vol. | 7, | pp. | 100283-100295, | 2019, | doi: | [16] Rahul, | Balabhadruni, | Prajwal | Kharvi | and | Monto | Manu. |  |  |
| 10.1109/ACCESS.2019.2930000. | “ | Implementation | of | DevSecOps | using | Open-Source | tools. | ” |  |  |  |  |  |  |  |  |  |
| [11] Z. Ahmed and S. C. Francis, "Integrating Security with DevSecOps: | International Journal of Advance Research, Ideas and Innovations in |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Techniques | and | Challenges," | 2019 | International | Conference | on | Technology 5 (2019): 1050-1051. |  |  |  |  |  |  |  |  |  |  |
| Digitization (ICD), Sharjah, United Arab Emirates, 2019, pp. 178- | [17] T. Rangnau, R. v. Buijtenen, F. Fransen and F. Turkmen, "Continuous |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 182, doi: 10.1109/ICD47981.2019.9105789. | Security Testing: A Case Study on Integrating Dynamic Security |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [12] K. Zunnurhain and S. R. Duclervil, "A New Project Management | Testing Tools in CI/CD Pipelines," 2020 IEEE 24th International |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tool | Based | on | DevSecOps," | 2019 | International | Conference | on | Enterprise | Distributed | Object | Computing | Conference | (EDOC), |  |  |  |  |
| Computational Science and Computational Intelligence (CSCI), Las | Eindhoven, | Netherlands, | 2020, | pp. | 145-154, | doi: |  |  |  |  |  |  |  |  |  |  |  |
| Vegas, | NV, | USA, | 2019, | pp. | 239-243, | doi: | 10.1109/EDOC49727.2020.00026. |  |  |  |  |  |  |  |  |  |  |
| 10.1109/CSCI49370.2019.00049. | [18] D. Hely, F. Bancel, M. . -L. Flottes and B. Rouzeyre, "A secure Scan |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [13] X. Sun, Y. Cheng, X. Qu and H. Li, "Design and Implementation of | Design Methodology," Proceedings of the Design Automation & Test |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Security | Test | Pipeline | based | on | DevSecOps," | 2021 | IEEE | 4th | in | Europe | Conference, | Munich, | Germany, | 2006, | pp. | 1-2, | doi: |
| Advanced Information Management, Communicates, Electronic and | 10.1109/DATE.2006.244019. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Automation Control Conference (IMCEC), Chongqing, China, 2021, | [19] S. Singh and N. Singh, "Containers & Docker: Emerging roles & |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| pp. 532-535, doi: 10.1109/IMCEC51613.2021.9482270. | future of Cloud technology," 2016 2nd International Conference on |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [14] Ö. | Ş | engül, H. Özk | ı | l | ı | ç | aslan, E. Arda, U. Yavano | ğ | lu, | İ | . A. Do | ğ | ru and | Applied and Theoretical Computing and Communication Technology |  |  |  |
| A. A. Selçuk, "Implementing a Method for Docker Image Security," | (iCATccT), | Bangalore, | India, | 2016, | pp. | 804-807, | doi: |  |  |  |  |  |  |  |  |  |  |
| 2021 | International | Conference | on | Information | Security | and | 10.1109/ICATCCT.2016.7912109. |  |  |  |  |  |  |  |  |  |  |
| Cryptology (ISCTURKEY), Ankara, Turkey, 2021, pp. 34-39, doi: | [20] github. | “ | DAMN VULNERABLE WEB APPLICATION | ” | [Online]. |  |  |  |  |  |  |  |  |  |  |  |  |
| 10.1109/ISCTURKEY53027.2021.9654383. | Available : https://github.com/digininja/DVWA |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [15] F. Gauthier, N. Keynes, N. Allen, D. Corney and P. Krishnan, | [21] docker. | “ | Docker | Overview | ” | [online]. | Available | : |  |  |  |  |  |  |  |  |  |
| "Scalable | Static | Analysis | to | Detect | Security | Vulnerabilities: | https://docs.docker.com/get-started/overview/ |  |  |  |  |  |  |  |  |  |  |

Challenges and Solutions," 2018 IEEE Cybersecurity Development

6

