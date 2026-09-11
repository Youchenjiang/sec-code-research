---
title: "Humanoid: A Deep Learning-based Approach to Automated Black-box Android App Testing"
authors: "Yuanchun Li, Ziyue Yang, Yao Guo, Xiangqun Chen"
venue: "IEEE/ACM ASE 2019 / arXiv:1901.02633"
year: 2024
pages: 12
layout_pipeline: "High-Fidelity Seamless Academic Parser v3.0"
---

# Humanoid: A Deep Learning-based Approach to Automated Black-box Android App Testing

**Authors:** Yuanchun Li, Ziyue Yang, Yao Guo, Xiangqun Chen  
*Key Laboratory of High Confidence Software Technologies (Peking University), Ministry of Education, Beijing, China*  
*arXiv:1901.02633v2 [cs.SE] | IEEE/ACM International Conference on Automated Software Engineering (ASE)*

---

> **Abstract** — Automated input generators are widely used for large-scale dynamic analysis of mobile apps. Such input generators must constantly choose which UI element to interact with and how to interact with it, in order to achieve high coverage with a limited time budget. Currently, most input generators adopt pseudo-random or brute-force searching strategies, which may take very long to find the correct combination of inputs that can drive the app into new and important states. In this paper, we propose Humanoid, a deep learning-based approach to GUI test input generation by learning from human interactions. Our insight is that if we can learn from human-generated interaction traces, it is possible to automatically prioritize test inputs based on their importance as perceived by users. We design and implement a deep neural network model to learn how end-users would interact with an app (specifically, which UI elements to interact with and how). Our experiments showed that the interaction model can successfully prioritize user-preferred inputs for any new UI (with a top-1 accuracy of 51.2% and a top-10 accuracy of 85.2%). We implemented an input generator for Android apps based on the learned model and evaluated it on both open-source apps and market apps. The results indicated that Humanoid was able to achieve higher coverage than six state-of-the-art test generators. However, further analysis showed that the learned model was not the main reason of coverage improvement. Although the learned interaction pattern could drive the app into some important GUI states with higher probabilities, it had limited effect on the width and depth of GUI state search, which is the key to improve test coverage in the long term. Whether and how human interaction patterns can be used to improve coverage is still an unknown and challenging problem.

> **Index Terms** — Dynamic analysis, automated input generation, graphical user interface, deep learning, mobile application

---

<!-- Section 1 -->
## 1 INTRODUCTION

Mobile applications (apps in short) have seen widespread adoption in recent years, with over three million apps available for download in both Google Play and Apple App Store, while billions of downloads have been accumulated [1], [2]. These apps need to be adequately inspected by the app markets and governments who want to prevent malicious or inappropriate apps being published. Many dynamic analysis methods [3], [4], [5] are proposed for such purpose. These methods usually require running an app in a sandbox, and the completeness of analysis is based on how many functionalities in the app are covered. However, due to the huge amount of apps and limited human resources, it is difficult for auditors to manually run the apps. As a result, automated input generators for mobile apps have been studied extensively in both academia and industry.

The inputs for mobile apps are typically represented by the interactions with the graphical user interface (GUI) of an app. Specifically, an interaction may include clicking, scrolling, or inputting text into a GUI element, such as a button, an image, or a text block. The job of an input generator is to produce a sequence of interactions for the app under analysis, which can be used to detect software-related problems, such as bugs, vulnerabilities, and security issues. The effectiveness of a input generator is often measured by its coverage. Given unlimited time, one can potentially try all possible interaction sequences and combinations to achieve a perfect coverage. However, in real-world situations where the time budget for analysis is typically limited and the app may contain hundreds of GUI states and dozens of possible interactions in each state, an input generator can only choose a small subset of interaction sequences to explore.

The key to success for an automated input generator is to choose the "best" interactions for a given app, while the definition of "best" is based on the goal of analysis. For example, if the input generator is used by developers to find bugs in their apps, the unexpected or corner-case input would be preferred. While if the purpose of analysis is to audit the apps (e.g. detecting inappropriate content, privacy leakage, accessibility issues, etc.), the best input would be the interactions that end-users are more likely to pick, so that the commonly-used content can get more attention during analysis. Existing work on automated GUI input generation [6], [7], [8], [9], [10], [11] are usually focused on the bug-finding scenario, where random strategies or corner-case-targeted strategies are effective. However, these approaches may not be as effective in the dynamic analysis and auditing scenario, since they ignore the GUI information, thus is impossible to understand which interactions would be preferred by the users. The key question we want to investigate in this paper is: *Can we teach an automated input generator to prioritize inputs like a human being?*

This paper proposes Humanoid, an automated GUI input generator that is able to learn how humans interact with mobile apps and then use the learned model to guide input generation as a human. With the knowledge and model learned from human interaction traces, Humanoid can prioritize the possible interactions on a GUI page according to their importance from user perspective, thus generating inputs that can lead to important states faster and achieve higher coverage.

We can use the GUI page from an app shown in Figure 1 as a motivating example. There are more than 20 actions that can be performed on that page, while most of them are ineffective or unrelated to the core functionalities of the app, such as swiping left on the current page, which is actually not scrollable, or clicking the advertisement on the bottom. While a random input generator may have to try all possible choices (including those ineffective ones), Humanoid is able to increase the probabilities of clicking the menu buttons, which are more likely to drive the app into additional important GUI states.

![Figure 1: An illustration of how Humanoid chooses inputs for a UI state](../assets/Humanoid%20(2024)%20Deep%20Learning-Based%20Black-box%20Testing/fig_1_illustration.png)
*Fig. 1: An illustration of how Humanoid chooses inputs for a UI state. The left side is a screenshot of the current UI of an Android app under analysis, and the right side enumerates the most possible interactions in the UI state. Humanoid computes a probability for each action based on a model learned from human interaction traces. The probability represents how likely the action will be chosen by Humanoid as the test input.*

The core of Humanoid is a deep neural network (DNN) model that predicts which inputs are more likely to be generated by human users. The input of the model is the current UI state as well as the most recent UI transitions, represented as a stack of images, while the output is a predicted distribution of possible next actions, including the action type and the corresponding location coordinates on the screen. By comparing the predicted distribution with all possible actions on the UI page, the model is able to assign a probability to each action.

We then design a biased random search algorithm to generate inputs based on the probabilities predicted by the DNN model. The algorithm always tries to pick an unexplored action in the current state as the input. If there are multiple unexplored actions, the one with the highest probability is picked. If all actions have already been explored, the algorithm will pick the action that can lead to the state with the most unexplored actions. The reason why this strategy can improve coverage is that the important states that users prefer to visit and with more possible inputs are more frequently and adequately explored. Given a limited time budget, spending time on these important states can improve coverage more efficiently than on other random states.

We implemented Humanoid and trained the interaction model with 304,976 human interactions extracted from a large-scale crowd-sourced UI interaction dataset Rico [12]. As a generic input generator, the model can be easily integrated with other dynamic analysis tools by simply replacing their input selection logic.

To evaluate the interaction model, we examined whether the model can learn human interaction patterns by using it to prioritize the possible actions for each UI state from a subset of the Rico interaction trace dataset. The results show that, for most UI states in the interaction traces, human-performed actions are ranked in the top 10% across all actions according to Humanoid-predicted probabilities, which was significantly better than a random strategy whose expectation would be around 50%.

To evaluate the input generation algorithm, we compared Humanoid with six state-of-the-art input generators in Android. These input generators are primarily designed for testing purpose (e.g. finding bugs), thus may not be very effective in covering apps’ functionalities. The apps used for testing include 68 open-source apps obtained from the AndroTest [13] dataset, which is a widely-used benchmark dataset for evaluating Android test input generators. We also tested 200 popular apps from Google Play, to see whether Humanoid is also effective for more complicated apps in real-world scenarios. The results show that, Humanoid was able to achieve 43.3% line coverage for open-source apps and 24.1% activity coverage for market apps, which was significantly higher than the best results (38.8% and 19.7%) achieved by other input generators within the same time duration.

We further analyzed Humanoid’s input generation algorithm by replacing the learned interaction model with a random policy, in order to see whether the coverage improvement was actually brought by the learned model. The result showed that, given sufficient time, there was no significant difference between the test coverage achieved with and without the learned model. This is because that coverage improvement is primarily due to how many different states are visited, instead of how much or how fast a input generator can navigate into human-preferred states. The former mainly depends on the state space search algorithm, rather than the interaction model learned from human interaction traces.

This paper makes the following main contributions:
1. **Pioneering Concept**: To the best of our knowledge, this is the first work to introduce the idea of prioritizing GUI inputs by learning from human interaction traces, in order to generate effective inputs for automated dynamic mobile app analysis.
2. **Deep Learning Model**: We propose and implement a deep learning model to prioritize test inputs according to their importance from users’ perspective. We demonstrate that Humanoid is able to rank the human-preferred interactions higher than others in new apps.
3. **End-to-End Input Generator**: We design and implement an input generator, named Humanoid, to automatically generate interactions that are more frequently performed by users. We evaluate Humanoid with extensive experiments.

---

<!-- Section 2 -->
## 2 BACKGROUND AND RELATED WORK

### 2.1 Android UI
For a mobile app, user interface (UI) is the place where interactions between humans and machines occur. App developers design UI to help users understand the features of their apps, and users interact with the apps through the UI. The graphical user interface (GUI) is the most important type of UI for most mobile apps, where apps present content and actionable widgets on the screen and users interact with the widgets using actions such as clicks, swipes, and text inputs.

The GUI pages (or screenshots) presented in mobile apps typically use a tree-structured layout. For example, in a screenshot of an Android app, all UI elements are built using View and ViewGroup objects and organized as a tree. A View is a leaf node that draws something on the screen that the user can see and interact with. A ViewGroup is a parent node that holds other nodes in order to define the layout of the interface. A UI state can be identified as a snapshot of the structure and content in the current UI tree, and a node in the UI tree is called a UI element.

An app can be viewed as a combination of many GUI states and the transitions between them. Each GUI state serves different functionalities or renders different content. App users navigate between UI states by interacting with the UI elements.

### 2.2 Automated GUI Input Generation
Automated GUI input generation has become an active research area since the prevalence of mobile apps. Most of the research work target at the Android platform, partly due to the popularity of Android apps, as well as the fragmentation of Android devices and OS releases.

In Android, input generators interact with apps in the same way as humans: sending simulated gestures to the GUI of an app. Since the acceptable gestures in a UI state are limited, the main difference between different test generators is their strategies used in prioritizing these actions. There are mainly three types of strategies: random, model-based, and targeted.

A typical example using the random strategy is Monkey [6], the official tool for automated app testing in Android. Monkey sends random types of input events to random locations on the screen without considering its GUI structure. DynoDroid [7] also uses a random strategy, while the input sent by DynoDroid is smarter than Monkey: A lot of unacceptable events are filtered out based on the GUI structure and registered event listeners in an app. Sapienz [10] makes use of a genetic algorithm to optimize random test sequences. Polariz [14] extracts and reuses "motifs" obtained by human testers to help generate random test sequences.

Several other testing tools build and use the GUI model of mobile apps to generate test input. These models are usually represented as finite state machines that store the transitions between app window states. Such GUI models can be constructed dynamically [8], [9], [11], [15], [16], [17], [18], [19], [20] or statically [21]. Based on the GUI models, testing tools can generate events that can quickly navigate the app to unexplored states. These model-based strategies can be further optimized in various ways. For example, Stoat [11] can iteratively refine the test strategy based on existing explorations, and DroidMate [18] can infer acceptable actions for a UI element by mining from other apps.

The targeted strategy is designed to address the problem that some app behavior can only be revealed with specific test inputs. For example, a malicious app may only send SMS messages upon receiving a certain broadcast [22]. These testing tools [23], [24], [25], [26] usually use sophisticated static analysis techniques such as data flow analysis and symbolic execution to find the interactions that can lead to the target states. However, their effectiveness can be easily affected by the complexity of app code and the difficulty of mapping code to UI elements.

Unlike existing input generators that are mainly designed for developers to test their own apps, our work aims to assist auditors (app markets and governments) in large-scale dynamic app analysis, such as inappropriate content detection [5], privacy leakage detection [3], ad fraud detection [4], etc. In such scenarios, the input generator should prioritize user-preferred interactions over unexpected or corner-case inputs, in order to trigger more functionalities that may be used by users.

### 2.3 Software GUI Analysis
GUI is an indispensable part of software on most major platforms including Android. Analyzing the app’s GUI is of great interest to many researchers and practitioners. There are mainly two lines of research in this area. One is to understand the behavior of apps from the software engineering perspective. Another is from the human-computer interaction perspective to analyze the user interface design.

As mentioned before, many automated testing tools build and use GUI models to guide test input generation. Unlike such models that mainly use the transitions between UI states to abstract the app behavior, there are also some approaches focused on analyzing the information in each individual UI state. For example, Huang et al. [27] and Rubin et al. [28] proposed to detect stealthy behaviors in Android apps by comparing the actual behaviors with the UI. PERUIM [29] extracted the mapping between an app’s permissions to its UI to help users understand why each permission is requested, and AUDACIOUS [30] provided a way to control permission access based on UI components. Chen et al. [31] introduced a machine learning-based method to extract UI skeletons from UI images, in order to facilitate GUI development.

In human-computer interaction research, software GUI is mainly used to mine UI design practices [32], [33] and interaction patterns [34] at scale. The mined knowledge can further be used to guide UI and UX (user experience) design. To facilitate mobile app design mining, Deka et al. have collected and released a dataset named Rico [12], which consists of a large number of UI screens and human interactions.

Our work lies in the intersection between software engineering and human-computer interaction: we propose a deep learning approach to mining human interaction patterns from the Rico dataset and use the learned patterns to guide automated input generation.

---

<!-- Section 3 -->
## 3 OUR APPROACH

In order to employ human knowledge on mobile apps to augment mobile app testing, this paper proposes Humanoid, a new automated input generator that is able to prioritize inputs based on knowledge learned from human-generated app interaction traces. Similar to many existing input generators, Humanoid uses a GUI model to understand and explore the behavior of the app under analysis. However, unlike traditional model-based approaches that randomly choose an action to perform when exploring a UI state, Humanoid prioritizes the actions that are more likely to be performed by human users. We expect that such strategy can drive the app into important states more frequently and achieve higher coverage than random strategies.

### 3.1 Approach Overview

Figure 2 shows the overview of Humanoid. The core of Humanoid is a deep learning model (i.e. interaction model) that learns the patterns about how humans interact with apps. Based on the interaction model, the whole system can be separated into two phases, including an offline phase for training the model with human-generated interaction traces and an online phase in which the model is used to guide test input generation.

![Figure 2: Overview of our approach](../assets/Humanoid%20(2024)%20Deep%20Learning-Based%20Black-box%20Testing/fig_2_overview.png)
*Fig. 2: Overview of our approach. Phase 1 conducts offline learning from human-generated traces; Phase 2 executes dynamic input generation with UI Transition Graph (UTG) feedback.*

In the offline learning phase, we use a deep neural network model to learn the relation between the GUI contexts and user-performed interactions. A GUI context is represented as the visual information in the current UI state and the latest UI transitions, while an interaction is represented as the action type (touch, swipe, etc.) and the location coordinates of the action. After learning from large-scale human interaction traces, Humanoid is able to predict a probability distribution of the action type and action location for a new UI state. The predicted distribution can then be used to calculate the probability of each UI element being interacted with by humans and how to interact with it.

During the online testing phase, we adopt a biased random search algorithm to generate inputs. The algorithm maintains a GUI model named UI transition graph (UTG) to remember the explored states and actions in the app. Both the GUI model and the interaction model are used by Humanoid to decide what input to send. The algorithm picks new actions to explore based on the probabilities predicted by the interaction model and navigate between explored UI states based on the UTG.

### 3.2 Interaction Trace Preprocessing

First of all, we will need a large dataset (Rico [12]) with human interaction traces to train a user interaction model, which is the key component in Humanoid. Because the human interaction traces in Rico are not designed for training for our purpose, we first need to preprocess the interaction traces.

A raw human interaction trace is usually a continuous stream of motion events sent to the screen [12], where each motion event is comprised of when (the timestamp) and where (the x,y coordinate) the cursor (the user’s finger) enters, moves, and leaves the screen. The state change is also continuous because of the animations and dynamically loaded content.

The input acceptable to our model is a set of user interaction flows. Each interaction flow consists of a sequence of UI states $\langle s_1, s_2, s_3, \dots, s_n \rangle$ and a sequence of actions $\langle a_1, a_2, a_3, \dots, a_n \rangle$ that are taken in the corresponding UI states. To convert the raw interaction traces to the format acceptable to our model, we need to split cursor movements and identify user actions from them.

We consider seven types of user actions in Humanoid, including `touch`, `long_touch`, `swipe_up/down/left/right`, and `input_text`. Most use cases in apps can be accomplished with these types of actions. Each action is represented by the action type and the target location on the screen. In order to extract user actions from raw cursor traces, we first aggregate the cursor movements into interaction sessions.

An interaction session is defined as the period between when the cursor enters the screen and when the cursor leaves the screen. We denote the timestamps of the session start and the session end as $time_{start}$ and $time_{end}$, and the cursor locations as $loc_{start}$ and $loc_{end}$. Then we map interaction sessions to user actions according to a list of heuristic rules, as shown in Table 1.

### Table 1: Rules to Extract Actions from Cursor Movements

| Condition | Action Type | Location |
| :--- | :--- | :--- |
| $|loc_{end} - loc_{start}| < 50\text{px}$ and $time_{end} - time_{start} < 500\text{ms}$ | `touch` | $loc_{start}$ |
| $|loc_{end} - loc_{start}| < 50\text{px}$ and $time_{end} - time_{start} \ge 500\text{ms}$ | `long touch` | $loc_{start}$ |
| $|loc_{end} - loc_{start}| \ge 50\text{px}$ and $loc_{end}$ is on the left/right/top/bottom of $loc_{start}$ | `swipe left` / `right` / `up` / `down` | $loc_{start}$ |
| Successive interaction sessions where the keyboard is displayed and an editable element is focused | `input text` | Center of editable element |

*Note: $|loc_{end} - loc_{start}|$ represents Euclidean distance. Parameters are heuristically chosen to accommodate Android default configurations.*

Once we have extracted the sequence of actions $\langle a_1, a_2, \dots, a_n \rangle$, we are able to match UI state changes with the actions based on the action timestamps. We use the UI state captured right before the timestamp of $a_i$ as $s_i$ to form the state sequence $\langle s_1, s_2, \dots, s_n \rangle$. The state sequence and the action sequence together represent a user interaction flow, which will be used as the training data for our human interaction model.

### 3.3 Model Training

This section explains in more details on how we use a deep neural network model to learn human interaction patterns from human interaction traces.

End-users interact with an app based on what they want to do with the app and what they see on its GUI. Since different apps often share common UI design patterns, it is intuitive that the way how humans interact with GUI is generalizable across different apps. The goal of the interaction model is to capture such generalizable interaction patterns.

We introduce a concept *UI context* to model what humans reference when they interact with an app. A UI context $context_i$ consists of the current UI state $s_i$ and three latest UI transitions $(s_{i-1}, a_{i-1}), (s_{i-2}, a_{i-2}), (s_{i-3}, a_{i-3})$. The current UI state represents what the users see when they perform the action, while the latest UI transitions are used to model the users’ underlying intention during the current interaction session. The reason why we used exactly three historic UI transitions is because most common interaction patterns contain no more than three actions [34].

Figure 3 shows how we represent the UI states and actions in our model. Each UI state is represented as a two-channel UI skeleton image, in which the first channel (red channel) renders the bounding box regions of text UI elements and the second channel (green channel) renders the bounding box regions of non-text UI elements. The reason why we use the UI skeletons instead of the original screenshots is that most characters on the screenshots do not affect how humans interact with the apps. For example, the UI style (font size, button style, background color, etc.) of the same app may change across different OS and app versions, whereas the way how users use the app remains the same. Some apps even provide functionalities like "night mode" to allow users change the UI styles internally. Such UI style characters may bring noises to our model and affect the model’s generalization ability, thus we exclude them from the input representation.

![Figure 3: Representation of UI states and actions](../assets/Humanoid%20(2024)%20Deep%20Learning-Based%20Black-box%20Testing/fig_3_representation.png)
*Fig. 3: The representation of UI states and actions in the interaction model.*

Each action is represented by its action type and target location coordinates. The action type is encoded as a seven-dimensional vector, in which each dimension maps to one of the seven action types as described earlier. The action target location is encoded as a heatmap. Each pixel in the heatmap is the probability of the pixel being the action target location. We use a heatmap rather than the raw coordinates to represent the action location because the raw coordinates are highly non-linear and more difficult to learn [35].

In summary, the representation of a UI context, i.e. the input feature for our interaction model, is a stack of images including one 2-channel image for the current UI state and three 3-channel images for three latest UI transitions (each transition include one 2-channel image for the UI state and one 1-channel image for the action). All images are scaled to the size of $180 \times 320$ pixels. For ease of learning, we also add one channel of zero padding for the current UI state. In the end, a UI context is represented as a $4 \times 180 \times 320 \times 3$ vector.

Given the UI context vector, the output of the interaction model is an "action" that is likely to be performed by humans in the current state. Note that the predicted "action" is not an actual acceptable action in the current UI state. Instead, it is a probability distribution of types and locations of the expected human-like actions. Specifically, the goal of the model is to learn two conditional probability distributions:

1. **Action Type Distribution**: $P(type \mid context)$
2. **Action Location Distribution**: $P(location \mid context, type)$

Figure 4 shows the architecture of the deep learning model used in Humanoid. The model takes the representation of the current UI context as input, and outputs the probability distribution of the next action (including the action type and the action location). It consists of five major components: convolutional layers, residual LSTM modules, de-convolutional layers, a fully connected layer and loss functions.

![Figure 4: Architecture of the deep learning model](../assets/Humanoid%20(2024)%20Deep%20Learning-Based%20Black-box%20Testing/fig_4_dnn_architecture.png)
*Fig. 4: The architecture of the deep learning model used in Humanoid. The model takes the representation of current UI context as input, predicting action types and action coordinates.*

- **Convolutional layers**: Convolutional network structure has become a popular approach for image feature extraction, since it has been proved very powerful in computer vision tasks on large real-world datasets [36]. In our model, we use 5 convolutional layers with ReLU activations to extract features from UI skeleton images and action heatmaps. After each convolutional layer, there is a stride-2 max-pooling layer that reduces the width and height of its input to half. The pooling layers also help the model to identify UI elements having the same shape but different surroundings.
- **Residual LSTM modules**: LSTM (Long-Short-Term Memory) networks are widely adopted in sequence modeling problems, such as machine translation [37], video classification [38], etc. In our model, extracting features from historical transitions is also a sequence modeling problem. We insert residual LSTM modules after each of the last 3 convolutional layers, in order to capture UI transition sequence features on different resolution levels. In a residual LSTM module, the last dimension of input and the output of the normal LSTM are directly added through a residual path. Such residual structure makes the neural network easier to optimize [39], and gives hint that the location of an action should lie inside a UI element. To decrease model complexity, we also added a $1 \times 1$ convolutional layer before each residual LSTM module to reduce the feature dimension.
- **De-convolutional layers**: This component is used to generate high-resolution probability distributions from the low-resolution output of residual LSTM modules. There are several options to accomplish this, such as bilinear interpolation, de-convolution, etc. We use de-convolutional layers, as it is easier to integrate with deep neural networks and more general than the interpolation methods. Features on different resolution levels are combined to improve the quality of generated heatmap [40]. A softmax layer is followed to normalize the generated heatmap so that all pixels in the heatmap sum to 1, which is the probability distribution of action locations.
- **Fully connected layer**: A single fully connected layer with softmax is used to generate the probability distribution of action types.
- **Loss functions**: The model predicts both the action location and action type as probability distributions. Thus their cross-entropy losses against the ground truth (the action performed by humans) are suitable for model optimization. We use the sum of these two losses and a layer weight regularizer (to avoid overfitting) as the final loss function in the training process.

During training, each action $a_i$ in an interaction flow ($\langle s_1, s_2, \dots, s_n 
angle, \langle a_1, a_2, \dots, a_n \rangle$) is converted to target probability distributions where $p_{type}(t) = 1$ if $t = a_i.type$, else $0$. For location, $p_{loc}(x, y) = f(x - a_i.x, y - a_i.y)$ where $f$ is a Gaussian distribution with variance 20.

Similarly, when applying the model, we feed it with the representation of the current UI state to predict probability distributions $p_{type}(t)$ and $p_{loc}(x, y)$ for the next action. To convert them to probabilities of actual clickable elements in the current state, we traverse the UI tree and calculate:

$$P(action) = p_{type}(action.type) 	imes \sum_{(x,y) \in action.element} p_{loc}(x, y)$$

The action probabilities can finally be used to guide test input generation in the next step.

### 3.4 Test Input Generation with Humanoid

In this section, we describe how we apply the learned human interaction model to generate human-like test inputs.

Humanoid generates two types of test inputs, including explorations and navigations. Exploration inputs are used to discover the unseen behaviors in an app, while navigation inputs drive the app to known states that contain unexplored actions. When choosing from exploration inputs, the test generator does not know about the consequences of each test input, and the decision is made based on the guidance of the human interaction model (traditional test generators usually choose the input randomly). When generating navigation inputs, the test generator knows the target states of the input, as it has saved the memory of the transitions.

Similar to many existing test generators, Humanoid uses a GUI model to save the memory of transitions. The GUI model we use is represented as UI transition graphs (UTG in short), which is a directed graph, whose nodes are UI states and edges are the actions that lead to UI state transitions. The UTG is constructed at runtime: each time the test generator observes a new state $s_i$, it adds a new edge $\langle s_{i-1}, a_{i-1}, s_i 
\rangle$ to the UTG.

![Figure 5: UI transition graph example](../assets/Humanoid%20(2024)%20Deep%20Learning-Based%20Black-box%20Testing/fig_5_utg.png)
*Fig. 5: An example of a UI transition graph (UTG).*

With the UTG, the test generator can navigate to any known state by following the path to the state. To decide between exploration and navigation and generate the input action, Humanoid adopts a biased random search strategy:
- In each step, Humanoid checks whether there are unexplored actions in the current state.
- If there are unexplored actions, Humanoid chooses **exploration**, querying the interaction model and picking unexplored actions weighted by their predicted probabilities.
- If the current state is fully explored, Humanoid chooses **navigation**, calculating the shortest path in the UTG to the known state containing the highest number of unexplored actions.

---

<!-- Section 4 -->
## 4 EVALUATION

We evaluate Humanoid by primarily answering the following research questions:
1. **Model Efficacy**: Can Humanoid’s deep learning model learn and predict correct human interaction patterns? What is its prediction accuracy and cost? (Section 4.2)
2. **Testing Capability**: Can Humanoid generate effective inputs for new Android apps? How does it compare with existing testing tools in terms of test coverage? (Section 4.3)
3. **Ablation Insight**: Does Humanoid really learn from human traces? Is the high coverage brought by the interaction model? (Section 4.4)

### 4.1 Experimental Setup

The dataset we used to train the Humanoid model is processed from Rico [12], a large crowd-sourced dataset of human interactions. We extracted interaction flows from the raw data by identifying action sequences and state sequences. In the end, we obtained 12,278 interaction flows belonging to 10,477 apps. Each interaction flow contains 24.8 states on average.

![Figure 6: CDF for number of actions](../assets/Humanoid%20(2024)%20Deep%20Learning-Based%20Black-box%20Testing/fig_6_cdf.png)
*Fig. 6: CDF for the number of actions for each UI state in the dataset.*

The cumulative distribution function (CDF) for the number of possible actions in each UI state is shown in Figure 6. On average, each UI state has 50.7 possible action candidates, while more than 10% of the UI states include more than 100 possible action candidates.

The machine we used to train and test the interaction model is a workstation with two Intel Xeon E5-2620 CPUs, 64GB RAM and an NVidia GeForce GTX 1080 Ti GPU (Ubuntu 16.04, TensorFlow [41]). For app testing, we evaluated on 68 open-source apps from AndroTest [13] (measuring Emma [42] line coverage) and 200 popular commercial apps from Google Play (measuring activity coverage).

### 4.2 Evaluation of the Deep Learning Model

#### 4.2.1 Model Accuracy
We randomly selected 100 apps from the dataset and used their interaction traces for testing. The interaction traces for the remaining 10,377 apps were used for training (302,382 UI states for training and 2,594 UI states for testing). For each UI state in the testing set, we used the interaction model to predict the probabilities for all possible actions and sort the actions in the descending order of predicted probabilities. The actions performed by humans were considered as the ground truth.

### Table 2: Top-N Accuracy of the Humanoid Interaction Model

| Top-N Metric | Random Strategy Accuracy | Humanoid Model Accuracy | Relative Improvement |
| :---: | :---: | :---: | :---: |
| **Top-1** | 5.8% | **51.2%** | **+782.8%** |
| **Top-3** | 17.5% | **67.6%** | **+286.3%** |
| **Top-5** | 29.1% | **74.8%** | **+157.0%** |
| **Top-10** | 58.3% | **85.2%** | **+46.1%** |

*Evaluation across 2,594 testing UI states comparing predicted action probabilities against human-generated ground truth.*

Table 2 shows that Humanoid was able to assign the highest probability to the human-generated action for more than 50% of the UI states. The mean percentile rank was 20.6% and the median was 9.5%, meaning that Humanoid was able to prioritize human-like actions into the top 10% for most UI states.

#### 4.2.2 Training and Prediction Cost
It took about 66 hours to train the model with 304,976 actions. Inference time per UI state was **107.9 ms**, which is negligible compared to the ~2 seconds needed by Android emulators to process inputs and render new screens.

### 4.3 Test Coverage

#### 4.3.1 Testing on Open-source Apps
We evaluated Humanoid against six state-of-the-art tools: Monkey [6], PUMA [16], Stoat [11], DroidMate [18], Sapienz [10], and DroidBot [15]. Each tool was run for one hour per app across 68 open-source apps.

### Table 3: Line Coverage Comparison across 68 Open-Source Android Apps

| App ID | Package Name | Monkey (MO) | PUMA (PU) | Stoat (ST) | DroidMate (DM) | Sapienz (SA) | DroidBot (DB) | Humanoid (HU) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `com.example.amazed` | 67% | 50% | 57% | 14% | 60% | 63% | **67%** |
| 2 | `com.example.anycut` | 61% | 61% | 11% | 48% | 59% | 62% | **63%** |
| 3 | `com.google.android.divideandconquer` | 80% | - | 45% | 45% | 71% | 52% | 58% |
| 4 | `com.android.lolcat` | 24% | - | 23% | 17% | 22% | 23% | **27%** |
| 5 | `info.bpace.munchlife` | 58% | 44% | 40% | 44% | 56% | 41% | **65%** |
| 6 | `org.passwordmaker.android` | 47% | 29% | 35% | 39% | 46% | 43% | **58%** |
| 7 | `com.google.android.photostream` | 19% | 22% | 24% | 12% | 27% | 22% | **27%** |
| 8 | `com.bwx.bequick` | 40% | 33% | 30% | 35% | 38% | 37% | **46%** |
| 9 | `com.example.android.musicplayer` | 53% | 51% | 42% | 52% | 52% | 52% | **53%** |
| 10 | `com.google.android.opengles.spritetext` | 61% | 58% | 60% | 2% | 58% | 59% | 59% |
| ... | *(30 open-source benchmark apps omitted for display brevity)* | ... | ... | ... | ... | ... | ... | ... |
| 66 | `net.mandaria.tippytipper` | 64% | 46% | 35% | 8% | 77% | 47% | **85%** |
| 67 | `es.senselesssolutions.gpl.weightchart` | 47% | 19% | 25% | 21% | 39% | 52% | **52%** |
| 68 | `de.freewarepoint.whohasmystuff` | 53% | 53% | 36% | 47% | 60% | 56% | **67%** |
| **AVG** | **Overall Mean Line Coverage** | **39%** | **31%** | **28%** | **26%** | **39%** | **35%** | **43%** |

*MO: Monkey, PU: PUMA, ST: Stoat, DM: DroidMate, SA: Sapienz, DB: DroidBot, HU: Humanoid. '-' indicates tool crashed.*

![Figure 7: Line coverage comparison of different testing tools](../assets/Humanoid%20(2024)%20Deep%20Learning-Based%20Black-box%20Testing/fig_7_line_coverage.png)
*Fig. 7: Line coverage comparison of different testing tools over 68 open-source Android apps.*

On average, Humanoid achieved a line coverage of **43.3%**, the highest across all input generators. Figure 8 demonstrates the progressive coverage growth over testing time.

![Figure 8: Progressive line coverage for open-source apps](../assets/Humanoid%20(2024)%20Deep%20Learning-Based%20Black-box%20Testing/fig_8_progressive_coverage.png)
*Fig. 8: Progressive line coverage over time (minutes) for open-source Android apps.*

### Table 4: Exemplary Apps where Humanoid Significantly Outperforms Existing Tools

| App Package Name | Humanoid Coverage | Best of Others | Root-Cause Analysis / Testing Advantage |
| :--- | :---: | :---: | :--- |
| `org.passwordmaker.android` | **58%** | 47% | Users configure password hashes sequentially (text $	o$ level $	o$ method). Humanoid assigns higher probabilities to these specific actions, exploring multiple algorithms within budget. |
| `com.kvance.Nectroid` | **53%** | 32% | Music player requiring custom playlist creation before playback. Humanoid successfully completed the multi-step playlist creation flow, where all baseline tools stalled. |
| `com.templaro.opsiz.aka` | **82%** | 61% | Morse-code audio converter. Requires: input text $	o$ click Option $	o$ click Create in exact sequence. Humanoid generated this sequence with high probability. |
| `com.tum.yahtzee` | **59%** | 44% | Dice game requiring entering two numeric values and pressing Play. Other tools trapped in keyboard exploration; Humanoid prioritized clicking Play. |
| `net.mandaria.tippytipper` | **85%** | 77% | Dense screen layout with dozens of buttons. Humanoid successfully prioritized the small OK and Split Bill buttons based on spatial UI awareness. |

#### 4.3.2 Testing on Commercial Market Apps
For 200 popular commercial Google Play market apps (3-hour testing sessions), activity coverage results are illustrated in Figure 9 and Figure 10.

![Figure 9: Activity coverage comparison of testing tools](../assets/Humanoid%20(2024)%20Deep%20Learning-Based%20Black-box%20Testing/fig_9_activity_coverage.png)
*Fig. 9: Activity coverage comparison of the testing tools over 200 popular Google Play market apps.*

![Figure 10: Progressive activity coverage for market apps](../assets/Humanoid%20(2024)%20Deep%20Learning-Based%20Black-box%20Testing/fig_10_market_coverage.png)
*Fig. 10: Progressive activity coverage over time (minutes) for market apps.*

Humanoid reached **24.1%** activity coverage, notably exceeding the best existing tool (Sapienz at 19.7%).

### 4.4 Effectiveness of the Learned Model
To determine whether coverage gains were caused by the learned model or the search algorithm, we executed an ablation study substituting the interaction model with a random action policy:
- The results revealed that given sufficient time budget, line coverage between the model-guided and random policy converged to similar levels.
- **Key Insight**: Coverage improvement is primarily governed by *how many distinct states are visited* (the state space search algorithm), whereas the learned interaction model accelerates *how rapidly the tool navigates into human-preferred states*.

---

<!-- Section 5 & 6 -->
## 5 LIMITATIONS AND FUTURE WORK

1. **Static UI Feature Bias**: The current model relies predominantly on visual skeleton layouts and cannot interpret dynamic semantic changes occurring within WebView or cross-platform OpenGL renderers.
2. **Text Input Diversity**: While Humanoid accurately identifies editable fields, text value generation relies on fixed dictionary heuristics rather than context-aware generative NLP models.
3. **Hybrid Integration**: Future work will explore coupling the human-like prioritization engine with targeted symbolic execution to penetrate deep guarded conditional branches.

## 6 CONCLUDING REMARKS

This paper proposed Humanoid, a deep learning-based automated GUI test input generator for Android apps. By learning from crowd-sourced interaction traces, Humanoid successfully predicts human-preferred interactions on unseen UI states, accelerating discovery of core app functionalities and achieving higher coverage than six state-of-the-art tools across 68 open-source apps and 200 commercial apps.
