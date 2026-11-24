# Human2LocoMan: Learning Versatile Quadrupedal Manipulation with Human Pretraining

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p122.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p122.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Yaru Niu, Yunzhe Zhang, Mingyang Yu, Changyi Lin, Chenhao Li, Yikai Wang, Yuxiang Yang, Wenhao Yu, Tingnan Zhang, Zhenzhen Li, Jonathan Francis, Bingqing Chen, Jie Tan, Ding Zhao
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, quadruped locomotion, loco-manipulation, human demonstrations
- Official paper: https://www.roboticsproceedings.org/rss21/p122.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p122.pdf
- Code/Project: https://human2bots.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Human2LocoMan은 인간과 사족 조작 로봇의 관측·행동 중 대응하는 부분을 맞춰 사람 시연을 로봇 조작 학습에 활용한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p122.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Quadrupedal robots have demonstrated impressive locomotion capabilities in complex environments, but equipping them with autonomous versatile manipulation skills in a scalable way remains a significant ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce a cross-embodiment imitation learning system for quadrupedal manipulation, leveraging data collected from both humans and LocoMan, a quadruped equipped with ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we develop a teleoperation and data collection pipeline, which unifies and modularizes the observation and action spaces of the human and the robot.
- **p. 1 / Abstract - extractive body cue:** To effectively leverage the collected data, we propose an efficient modularized architecture that supports co-training and pretraining on structured modalityaligned data across different embodiments.
- **p. 1 / Abstract - extractive body cue:** Additionally, we construct the first manipulation dataset for the LocoMan robot, covering various household tasks in both unimanual and bimanual modes, supplemented by a corresponding ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, the substantial embodiment gap between humans and quadrupedal robots poses challenges to both data collection and policy transfer.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While quadrupedal robots have demonstrated impressive locomotion capabilities in complex environments [1, 2, 3, 4, 5, 6, 7], and recent advances have extended their abilities ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our paper provides the following contributions: • We propose Human2LocoMan, a framework that enables flexible and scalable collection of human demonstrations and teleoperated ...
- **p. 6 / III. METHODOLOGY - extractive body cue:** This design preserves modality-specific distributions unique to each embodiment and enables the model to explicitly account for distributional gaps across embodiments, which is core to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these challenges, and drawing inspiration from the LocoMan platform [14]-a quadrupedal robot equipped with two leg-mounted loco-manipulators that offers a versatile foundation for ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** In this section, we present the design and implementation of our system, Human2LocoMan, which integrates teleoperation, data collection, and a Transformer-based architecture for cross-embodied learning.
- **p. 4 / III. METHODOLOGY - extractive body cue:** The dataset consists of aligned vision, proprioception, and actions from the human and the robot.
- **p. 5 / III. METHODOLOGY - extractive body cue:** Similar to the design in [78], we use a cross-attention layer to format observational features into a fixed number of tokens for each modality.
- **p. 4 / III. METHODOLOGY - extractive body cue:** We adopt a two-stage training process: the modularized cross-embodiment model is first pretrained on easy-to-collect human data, and then finetuned on a small amount of ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** For image inputs, the features are obtained from a pretrained ResNet encoder that can be finetuned during training; for proprioceptive or state-like inputs, the features ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The trunk is an encoder-decoder Transformer, where the input sequence length and the output sequence length are both fixed, as the number of tokens for each observation or action modality is fixed ... | proprioception, terrain/perception observation과 velocity command | p. 6 (III. METHODOLOGY), p. 6 (III. METHODOLOGY) |
| State/latent | trunk, encoder-decoder, Transformer, where, input, sequence, length, output, fixed, number, tokens, observation | body/contact state, foothold 또는 behavior mode | p. 6 (III. METHODOLOGY), p. 6 (III. METHODOLOGY), p. 5 (III. METHODOLOGY) |
| Output/action | By explicitly decomposing the input and output modalities and encoding them separately, we are leveraging the innate structure of observations and actions and imposing such a structure on the token sequences processed ... | joint target, torque, footstep 또는 locomotion action | p. 6 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 7 (III. METHODOLOGY) |
| Objective/outcome | In general, given a dataset De on an embodiment e and aligned action modalities m1, ..., mk, the total loss to optimize when training on e is: Le(θ) = k X i=1 ... | velocity/progress, stability, energy와 terrain generalization | p. 6 (III. METHODOLOGY), p. 7 (III. METHODOLOGY), p. 6 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- 두 형태의 데이터를 같은 구성 요소별로 수집하고 대응하는 모달리티를 공유하는 정책으로 사전학습과 공동학습을 수행한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss21/p122.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss21/p122.pdf#page=4) · [PDF 6쪽](https://www.roboticsproceedings.org/rss21/p122.pdf#page=6)
- LocoMan의 단팔·양팔 실물 작업에서 사람 시연의 추가와 로봇 데이터 수에 따른 성공률을 비교한다. [PDF 8쪽](https://www.roboticsproceedings.org/rss21/p122.pdf#page=8) · [PDF 9쪽](https://www.roboticsproceedings.org/rss21/p122.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Embodiment/environment | Both unimanual and bimanual toy collection tasks assess the robot's ability to grasp objects of varying shapes, colors, and positions. | hardware/simulator version and reset protocol | p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Dataset/benchmark | In this task, the robot must pick up a toy randomly positioned within a rectangular area and place it into a designated basket on the ground. | role, split, size and leakage | p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS) |
| Metric | Fig. 6: Substep success rate. The success rate for some substep is calcuated as the percentage of trials where the robot success- fully completed the substep. For each task, we calculate this ... | definition, denominator, direction and uncertainty | p. 10 (Figure/Table caption), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Baseline/ablation | (2) How does MXT compare to state-of-the-art imitation learning architectures? | fair input/data/compute/action matching | p. 7 (IV. EXPERIMENTS), p. 10 (Figure/Table caption), p. 8 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 3) Data - extractive body cue:** MXT-Scratch: MXT trained only on the LocoMan data. "L" denotes the larger training set (80 trajectories for SO-Uni, 60 trajectories for Pour and Scoop), while ...
- **p. 11 / 3) Data - extractive body cue:** Additionally, as depicted in Figure 8, MXT-Pretrained consistently achieves lower validation loss than MXT-Scratch, whereas the gap between HPT-Pretrained and HPT-Scratch is less consistent and ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** As shown in Figure 4, this task involves three pairs of shoes, with one pair being out-of-distribution (OOD).
- **p. 9 / 3) Data - extractive body cue:** The policy is rolled out for 24 times with in-distribution (ID) objects and 12 times with out-of-distribution (OOD) objects.
- **p. 11 / 3) Data - extractive body cue:** Efficiency, robustness, and generalizability.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)이다.
