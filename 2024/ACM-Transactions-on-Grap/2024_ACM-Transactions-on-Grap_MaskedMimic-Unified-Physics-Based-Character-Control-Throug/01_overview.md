# MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2409.14393.
> PDF retrieval source: https://research.nvidia.com/labs/par/maskedmimic/. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ACM Transactions on Graphics
- Authors: Chen Tessler, Yunrong Guo, Ofir Nabati, Gal Chechik, Xue Bin Peng
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, whole-body control, motion imitation, NVIDIA
- Official paper: https://arxiv.org/abs/2409.14393
- Full-text retrieval: https://arxiv.org/pdf/2409.14393v1
- Code/Project: https://research.nvidia.com/labs/par/maskedmimic/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://arxiv.org/pdf/2409.14393v1) 기준이다.

## Why This Paper Is Here

MaskedMimic은 시공간적으로 일부만 주어진 동작 조건을 채워 물리 시뮬레이션 캐릭터의 전신 행동을 생성한다. [PDF 1쪽](https://arxiv.org/pdf/2409.14393v1#page=1)

## Problem and Motivation

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The development of virtual characters capable of following dynamic user instructions and interacting with diverse scenes has been a significant challenge in computer graphics.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This challenge spans a wide range of applications, including gaming, digital humans, virtual reality, and many more.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For instance, a character might be instructed to "Climb the hill to the castle, wave to the guard, go inside, navigate to the throne room, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This scenario requires the integration of multiple complex behaviors: locomotion across uneven terrain, text-guided animation, and object interaction.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Prior works in physics-based simulation has addressed these challenges by developing specialized controllers for specific tasks such as locomotion, object interaction, and VR tracking.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** For example, a typical problem in VR is to generate full-body motion from only head and hands sensors.

## Core Idea

- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Our framework consists of two stages.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** We present MaskedMimic, a versatile control model that enables physically simulated characters to generate diverse behaviors from flexible userspecified constraints.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Training on masked motion sequences enables the model to generalize to novel combinations of objectives.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose a framework that trains a versatile control model by leveraging the rich multi-modal information within existing motion capture datasets, such as kinematic trajectories, ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** We now review the fundamental concepts and notations behind our framework.
- **p. 7 / 3. Inference - extractive body cue:** The decoder D(𝑎𝑡/𝑠𝑡,𝑧𝑡) is then conditioned on a latent sampled from the encoder's distribution, and produces an action for the simulated character.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** To train a versatile controller that can be directed using partial goals, we propose a simple training scheme that trains the controller on randomly masked ...
- **p. 8 / 3. Inference - extractive body cue:** The encoder and decoder are modeled as fully-connected networks, and observe a flattened concatenation of the input features.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (2) 𝑝(𝑠,𝑔/𝜋) denotes the distribution of states and goals observed under the student policy. | proprioception, reference pose/motion, visual or language command | p. 4 (3 PRELIMINARIES), p. 5 (3. Inference) |
| State/latent | denotes, distribution, states, goals, observed, under, student, policy, Character, Observations, step, observes | whole-body pose, balance/contact state와 skill/mode | p. 4 (3 PRELIMINARIES), p. 5 (3. Inference), p. 4 (3 PRELIMINARIES) |
| Output/action | Character Observations: At each step, 𝜋FC observes the current humanoid state 𝑠𝑡, consisting of the 3D body pose and velocity, canonicalized with respect to the character's local coordinate frame: 𝑠𝑡= (𝜃𝑡⊖𝜃root 𝑡 ... | joint/whole-body action, motion target 또는 task trajectory | p. 5 (3. Inference), p. 4 (3 PRELIMINARIES), p. 5 (3. Inference) |
| Objective/outcome | The agent's objective is to learn a policy that maximizes the discounted cumulative reward: 𝐽= E𝑝(𝜏/𝜋) " 𝑇 ∑︁ 𝑡=0 𝛾𝑡𝑟𝑡 # , (1) where 𝑝(𝜏/𝜋) = 𝑝(𝑠0)Π𝑇-1 𝑡=0 𝑝(𝑠𝑡+1/𝑠𝑡,𝑎𝑡)𝜋(𝑎𝑡/𝑠𝑡,𝑔𝑡) is the ... | tracking, balance, skill/task success와 recovery | p. 4 (3 PRELIMINARIES), p. 7 (3. Inference), p. 5 (3. Inference) |

## Main Claims and Actual Contribution

- 전체 동작을 추종하는 정책을 먼저 학습한 뒤 관절·시간·조건을 가려 부분 지정 목표에서 동작을 복원하도록 증류한다. [PDF 5쪽](https://arxiv.org/pdf/2409.14393v1#page=5) · [PDF 7쪽](https://arxiv.org/pdf/2409.14393v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2409.14393v1#page=8)
- 관절 목표가 드문 경우의 추종과 경로·텍스트·물체 상호작용 등 서로 다른 제어 입력을 같은 시뮬레이션 정책으로 평가했다. [PDF 10쪽](https://arxiv.org/pdf/2409.14393v1#page=10) · [PDF 11쪽](https://arxiv.org/pdf/2409.14393v1#page=11) · [PDF 12쪽](https://arxiv.org/pdf/2409.14393v1#page=12)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 15 (8 RESULTS), p. 11 (8 RESULTS) |
| Embodiment/environment | To evaluate the effectiveness of our framework, we construct a benchmark consisting of common tasks introduced by prior systems. | hardware/simulator version and reset protocol | p. 9 (7.2 Evaluation), p. 10 (7.2 Evaluation) |
| Dataset/benchmark | Additionally, MaskedMimic is designed to tackle a wide range of tasks across diverse scenes, which likely contributes to the model's enhanced generalization capabilities. | role, split, size and leakage | p. 9 (7.2 Evaluation), p. 10 (7.2 Evaluation), p. 11 (8 RESULTS), p. 12 (8 RESULTS) |
| Metric | We evaluate versions of the model with key components removed (Section 6), and measure the impact on the average success rate and error (i.e. average minimal distance from a valid sitting position ... | definition, denominator, direction and uncertainty | p. 14 (8 RESULTS), p. 9 (7.2 Evaluation), p. 11 (8 RESULTS) |
| Baseline/ablation | This test establishes the baseline capability for motion generation, both in terms of success rates and tracking quality, and allows comparison to prior systems for motion tracking. | fair input/data/compute/action matching | p. 10 (7.2 Evaluation), p. 10 (7.2 Evaluation), p. 11 (8 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 15 / 8 RESULTS - extractive body cue:** 9 LIMITATIONS AND FUTURE WORK Although MaskedMimic presents a unified model for controlling physically simulated humanoids, there remains a number of limitations with our model.
- **p. 11 / 8 RESULTS - extractive body cue:** 2023, 2024], reducing the tracking failure rate on unseen motions by 62.5%.
- **p. 11 / 8 RESULTS - extractive body cue:** In addition to a lower failure rate, our controller also supports a wider range of motions, irregular terrains, and object interactions.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. The MaskedMimic framework: The first phase produces a fully- constrained controller 𝜋FC. This full-body tracker is trained using reinforce- ment learning to imitate ...
- **p. 15 / 8 RESULTS - extractive body cue:** We hypothesize that this limitation stems from the naive mapping of motions from flat to irregular terrains based on the root-to-floor distance normalization.
- **p. 14 / 8 RESULTS - extractive body cue:** Notably, MaskedMimic does not produce a single solution.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Training scene (screenshot): The top region consists of standard flat terrain, enabling the controller to reproduce the original motions in a setting that ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 7 (3. Inference), p. 8 (3. Inference)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** This challenge spans a wide range of applications, including gaming, digital humans, virtual reality, and many more. (p. 2, 1 INTRODUCTION).
- **Actual contribution:** Training on masked motion sequences enables the model to generalize to novel combinations of objectives. (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** This test establishes the baseline capability for motion generation, both in terms of success rates and tracking quality, and allows comparison to prior systems for motion tracking. (p. 10, 7.2 Evaluation).
- **Explicit failure boundary:** 9 LIMITATIONS AND FUTURE WORK Although MaskedMimic presents a unified model for controlling physically simulated humanoids, there remains a number of limitations with our model. (p. 15, 8 RESULTS).
