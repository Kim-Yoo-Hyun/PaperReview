# DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p075.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p075.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Tony Tao, Mohan Kumar Srirama, Jason Jingzhou Liu, Kenneth Shaw, Deepak Pathak
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, human video, dexterous manipulation, cross-embodiment, robot data, generalist policy
- Official paper: https://www.roboticsproceedings.org/rss21/p075.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p075.pdf
- Code/Project: https://dexwild.github.io
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

DexWild는 사람이 직접 손으로 수행한 다양한 조작과 로봇 시연을 공동 학습해 새로운 환경에서 다지 손 정책의 일반화를 높인다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p075.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large-scale, diverse robot datasets have emerged as 1 promising path toward enabling dexterous manipulation policies to generalize to novel environments, but acquiring such datasets presents ...
- **p. 1 / Abstract - extractive body cue:** While teleoperation provides highfidelity datasets, its high cost limits its scalability.
- **p. 1 / Abstract - extractive body cue:** Instead, what if people could use their own hands, just as they do in everyday life, {o collect data?
- **p. 1 / Abstract - extractive body cue:** In DexWild, a diverse team of data colleclors uses their hands to collect hours of interactions across a multitude of environments and objects.
- **p. 1 / Abstract - extractive body cue:** To record this data, we create DexWild-System, a low-cost, mobile, and easy-to-use device.
- **p. 2 / A. Generalization for Imitation Learning - extractive body cue:** This lack of robustness remains a key limitation of current systems.
- **p. 2 / B. Data Generation for Robot Manipulation - extractive body cue:** Overcoming the robot data bottleneck has become a central challenge in robot learning.

## Core Idea

- **p. 2 / 1. IyrRopuction - extractive body cue:** In this paper, we present DexWild, a system that enables effective learning of robust dexterous manipulation policies through co-training on human and robot demonstrations.
- **p. 2 / 1. IyrRopuction - extractive body cue:** 1) Scalable Data Collection System: A novel humanembodiment DexWild-System that enables untrained operators fo quickly collect 9,290 demonstrations across 93 diverse environments, achieving 4.6% speedup ...
- **p. 3 / C. Human Action Tracking Systems - extractive body cue:** We introduce DexWild-System, a user-friendly, high-fidelity platform for efficiently gathering natural human hhand demonstrations across diverse real-world settings.
- **p. 3 / A. Data Collection System - extractive body cue:** As shown in Figure 2, DexWild-System consists of only three components: a single tracking camera for wrist pose estimation, a battery-powered mini-PC for onboard data ...
- **p. 4 / A. Data Collection System - extractive body cue:** Although DexWildSystem consists of only a few portable components, we make ‘no compromises on data fidelity.
- **p. 4 / B. Training Data Modalities and Preprocessing - extractive body cue:** + Observation o,: An observation at a given timestep consists of two synchronized palm camera images Tpinky and Fenn captured at the current timestep, aS ...
- **p. 5 / B. Training Data Modalities and Preprocessing - extractive body cue:** To effectively learn from our multimodal, diverse data, our training Pipeline leverages large-scale pre-trained visual encoders and shows strong performance across different policy architectures.
- **p. 3 / C. Human Action Tracking Systems - extractive body cue:** Building on this system, we propose DexWild, an imitation learning framework that co-trains on large-scale DexWildSystem human demonstrations alongside a small number of robot demonstrations. ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This is achieved by adopting a relative state-action representation, where each state and action is captured as the relative difference from the previous time step's pose. | multi-view observation, language/task label과 action trajectory | p. 3 (A. Data Collection System), p. 4 (A. Data Collection System) |
| State/latent | achieved, adopting, relative, state-action, representation, where, state, action, captured, difference, previous, time | shared representation, embodiment/task identity와 data distribution | p. 3 (A. Data Collection System), p. 4 (A. Data Collection System), p. 2 (B. Data Generation for Robot Manipulation) |
| Output/action | Achieving this goal requires careful alignment of both the observation space and the action space between humans and robots. | dataset sample 또는 learned policy action | p. 4 (A. Data Collection System), p. 2 (B. Data Generation for Robot Manipulation), p. 4 (A. Data Collection System) |
| Objective/outcome | ‘Through the careful design of our hardware, observation, and action interfaces, we are able to train dexterous robot policies using a simple behavior cloning (BC) objective [31, 37, 36}. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 5 (B. Training Data Modalities and Preprocessing), p. 2 (C. Human Action Tracking Systems) |

## Main Claims and Actual Contribution

- 현장에서 사람이 착용할 수 있는 이동식 수집 장치를 만들고 사람·로봇 시연을 함께 학습하는 절차를 제시했다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p075.pdf#page=1) · [PDF 3쪽](https://www.roboticsproceedings.org/rss21/p075.pdf#page=3)
- 처음 보는 환경과 다른 로봇 형태에서 평가하고 사람·로봇 자료를 함께 쓸 때와 한 자료만 쓸 때를 비교했다. [PDF 6쪽](https://www.roboticsproceedings.org/rss21/p075.pdf#page=6) · [PDF 8쪽](https://www.roboticsproceedings.org/rss21/p075.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (V. ANALYSIS AND RI), p. 8 (Figure/Table caption) |
| Embodiment/environment | We evaluate our approach across three scenarios: 1) In-Domain: Environments where robot training data was collected, testing with novel objects 2) In-the-Wild: Environments present in DexWild but absent from robot training data ... | hardware/simulator version and reset protocol | p. 6 (C. Evaluation Environments), p. 6 (B. Evaluation Tasks) |
| Dataset/benchmark | We evaluate our approach across three scenarios: 1) In-Domain: Environments where robot training data was collected, testing with novel objects 2) In-the-Wild: Environments present in DexWild but absent from robot training data ... | role, split, size and leakage | p. 6 (C. Evaluation Environments), p. 6 (B. Evaluation Tasks) |
| Metric | Success requires the policy to adapt to varying object properties, environmental conditions, | definition, denominator, direction and uncertainty | p. 6 (B. Evaluation Tasks), p. 5 (Figure/Table caption), p. 6 (V. ANALYSIS AND RI) |
| Baseline/ablation | not stated or recoverable in the selected PDF body | fair input/data/compute/action matching | 본문 anchor 없음 |

## Explicit Limitations and Failure Boundary

- **p. 8 / 06 06 06 _ - extractive body cue:** Next, because humans typically perform these tasks successfully their demonstrations seldom include error recovery-causing trained policies to struggle to recover from unexpected failures.
- **p. 7 / 3) Does policy performance scale effectively with increasing - extractive body cue:** DexWild policies achieve a strong 68.1% average success rate, compared to just 13% for the robot ‘only baseline, Even when failures occur, DexWild policies exhibit ...
- **p. 8 / 06 06 06 _ - extractive body cue:** We identify three key limitations of Gello-based collection that our system overcomes
- **p. 6 / 3) Does policy performance scale effectively with increasing - extractive body cue:** This 36-point performance drop suggests that robot-only policies overft to environment-specitic features and fail to develop robust, transferable representations.
- **p. 6 / 3) Does policy performance scale effectively with increasing - extractive body cue:** dlomain settings (64.7% success rate) but degrade significantly in more challenging scenarios-in-the-wild (28.5%) and inthe-wild extreme (22.0%).
- **p. 7 / 3) Does policy performance scale effectively with increasing - extractive body cue:** 1:5) degrades performance (54.5% in-domain, 50.9% in-thewild), indicating that robot data remains essential for grounding fine-grained control,

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (A. Generalization for Imitation Learning), p. 2 (B. Data Generation for Robot Manipulation), p. 1 (1. IyrRopuction), p. 1 (Abstract), p. 4 (A. Data Collection System), p. 4 (B. Training Data Modalities and Preprocessing)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** 1) Lack of haptic feedback: Operators cannot feel objects, ‘making fine manipulation difficult for certain tasks. (p. 8, 06 06 06 _).
- **Actual contribution:** In this paper, we present DexWild, a system that enables effective learning of robust dexterous manipulation policies through co-training on human and robot demonstrations. (p. 2, 1. IyrRopuction).
- **Evaluation boundary:** We evaluate our approach across three scenarios: 1) In-Domain: Environments where robot training data was collected, testing with novel objects 2) In-the-Wild: Environments present in DexWild but absent from robot ... (p. 6, C. Evaluation Environments).
- **Explicit failure boundary:** This avoids the fragility of SLAMLbased wrist tracking, which often fails in feature-sparse environments or during occlusion-heavy tasks (e.g., drawer opening). (p. 4, A. Data Collection System).
