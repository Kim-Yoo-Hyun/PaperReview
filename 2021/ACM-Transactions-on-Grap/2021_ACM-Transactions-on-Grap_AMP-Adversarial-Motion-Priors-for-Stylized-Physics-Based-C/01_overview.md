# AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://xbpeng.github.io/projects/AMP/.
> PDF retrieval source: https://doi.org/10.1145/3450626.3459670. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ACM Transactions on Graphics
- Authors: Xue Bin Peng, Ze Ma, Pieter Abbeel, Sergey Levine, Angjoo Kanazawa
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: humanoid, Reinforcement Learning, motion imitation, whole-body control, physics-based control
- Official paper: https://xbpeng.github.io/projects/AMP/
- Full-text retrieval: https://xbpeng.github.io/projects/AMP/AMP_2021.pdf
- Code/Project: https://xbpeng.github.io/projects/AMP/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://xbpeng.github.io/projects/AMP/AMP_2021.pdf) 기준이다.

## Why This Paper Is Here

AMP는 동작 자료와 시뮬레이션 캐릭터의 상태 전이를 구별하는 판별기에서 스타일 보상을 얻어 과제 수행과 함께 학습한다. [PDF 1쪽](https://xbpeng.github.io/projects/AMP/AMP_2021.pdf#page=1)

## Problem and Motivation

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Synthesizing natural and life-like motions for virtual characters is a crucial element for breathing life into immersive experiences, such as films and games.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The demand for realistic motions becomes even more apparent for VR applications, where users are provided with rich modalities through which to interact with virtual ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing control strategies that are able to replicate the properties of naturalistic behaviors is also of interest for robotic systems, as natural motions implicitly encode ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While examples of natural motions are commonplace, identifying the underlying characteristics that constitute these behaviors is nonetheless challenging, and more difficult still to replicate in ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** So what are the characteristics that constitute natural and lifelike behaviors?
- **p. 5 / 4 BACKGROUND - extractive body cue:** However, it can be exceptionally difficult to design a style-reward 𝑟𝑆 that leads a character to learn naturalistic behaviors, or behaviors that conform to a ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** However, this loss tends to lead to optimization challenges due to vanishing gradients as the sigmoid function saturates, which can hamper training of the policy ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The central contribution of this work is an adversarial learning approach for physics-based character animation that combines goalconditioned reinforcement with an adversarial motion prior, which ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Our framework enables physically simulated character to solve challenging tasks while adopting stylistic behaviors specified by unstructured motion data.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We present one of the first adversarial learning systems that is able to produce high-quality full-body motions for physically simulated characters.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** We demonstrate the effectiveness of our framework on a diverse cast of complex simulated characters and a challenging suite of motor control tasks.
- **p. 5 / 4 BACKGROUND - extractive body cue:** We propose to model the style-reward with a learned discriminator, which we refer to as an adversarial motion prior (AMP), by analogy to the adversarial ...
- **p. 7 / 4 BACKGROUND - extractive body cue:** 6.2 Network Architecture Each policy 𝜋is modeled by a neural network that maps a given state s𝑡and goal g to a Gaussian distribution over actions ...
- **p. 6 / 4 BACKGROUND - extractive body cue:** 6.1 States and Actions The state s𝑡consists of a set of features that describes the configuration of the character's body.
- **p. 4 / 4 BACKGROUND - extractive body cue:** At each time step 𝑡, the agent observes the state s𝑡∈S of the system, then samples an action a𝑡∈A from a policy a𝑡∼𝜋(a𝑡/s𝑡, g).

## Observation, State, and Output Interface

참조 동작과 정책 상태 전이를 판별하는 적대적 스타일 보상과 과제 보상으로 행동을 학습한다. 정책의 관절 목표는 PD 제어로 실행된다. 인간형 및 티라노사우루스 캐릭터의 이동·목표 접촉을 물리 시뮬레이션에서 평가했다. [PDF 5쪽](https://xbpeng.github.io/projects/AMP/AMP_2021.pdf#page=5) · [PDF 9쪽](https://xbpeng.github.io/projects/AMP/AMP_2021.pdf#page=9)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 6.2 Network Architecture Each policy 𝜋is modeled by a neural network that maps a given state s𝑡and goal g to a Gaussian distribution over actions 𝜋(a𝑡/s𝑡, g) = N (𝜇(s𝑡, g), Σ), ... | 캐릭터 상태·과제 목표와 학습용 참조 동작 | p. 7 (4 BACKGROUND), p. 4 (4 BACKGROUND) |
| State/latent | Network, Architecture, policy, modeled, neural, maps, given, state, goal, Gaussian, distribution, over | 상태 전이를 평가하는 동작 판별기 | p. 7 (4 BACKGROUND), p. 4 (4 BACKGROUND), p. 5 (4 BACKGROUND) |
| Output/action | Behavioral cloning can be used to directly fit a policy to map from states observed in M to their corresponding actions using supervised learning [Bojarski et al. | 저수준 PD 제어기에 보낼 관절 목표 | p. 4 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 4 (4 BACKGROUND) |
| Objective/outcome | 5.2 Least-Squares Discriminator The standard GAN objective detailed in Equation 5 typically uses a sigmoid cross-entropy loss function. | 과제 보상 및 생성한 움직임의 스타일 | p. 5 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 4 (4 BACKGROUND) |

## Main Claims and Actual Contribution

- 참고 동작과 정책이 만든 동작을 비교하는 적대적 목적함수를 과제 보상과 결합해 비정렬 동작 클립을 사용할 수 있게 했다. [PDF 3쪽](https://xbpeng.github.io/projects/AMP/AMP_2021.pdf#page=3) · [PDF 4쪽](https://xbpeng.github.io/projects/AMP/AMP_2021.pdf#page=4) · [PDF 5쪽](https://xbpeng.github.io/projects/AMP/AMP_2021.pdf#page=5)
- 이동·목표 접촉 등 물리 시뮬레이션 과제로 동작 스타일과 작업 수행을 평가하고 다른 형상의 캐릭터에도 적용했다. [PDF 8쪽](https://xbpeng.github.io/projects/AMP/AMP_2021.pdf#page=8) · [PDF 9쪽](https://xbpeng.github.io/projects/AMP/AMP_2021.pdf#page=9) · [PDF 10쪽](https://xbpeng.github.io/projects/AMP/AMP_2021.pdf#page=10) · [PDF 11쪽](https://xbpeng.github.io/projects/AMP/AMP_2021.pdf#page=11)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (8 RESULTS), p. 10 (8 RESULTS) |
| Embodiment/environment | Each environment is denoted by "Character: Task (Dataset)". | hardware/simulator version and reset protocol | p. 8 (8 RESULTS), p. 9 (8 RESULTS) |
| Dataset/benchmark | Policies trained using the larger Locomotion dataset is able to more closely follow the various target speeds by imitating different gaits. our policies can in large part be attributed to the motion ... | role, split, size and leakage | p. 8 (8 RESULTS), p. 9 (8 RESULTS), p. 9 (8 RESULTS), p. 12 (8 RESULTS) |
| Metric | Since AMP does not use a phase variable to synchronize the policy with the reference motion, the motions may progress at different rates, resulting in de-synchronization that can lead to large pose ... | definition, denominator, direction and uncertainty | p. 11 (8 RESULTS), p. 11 (8 RESULTS), p. 18 (Figure/Table caption) |
| Baseline/ablation | AMP produces results of comparable quality when compared to prior tracking-based methods, without requiring a manually designed reward function or synchronization between the policy and reference motion. | fair input/data/compute/action matching | p. 12 (8 RESULTS), p. 10 (8 RESULTS), p. 7 (8 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 8 RESULTS - extractive body cue:** These additional motion clips then enable our character to recover from a fall and continue to perform a given task (Figure 3(c)).
- **p. 9 / 8 RESULTS - extractive body cue:** When the character falls forward, it tucks its body into a roll during the fall in order to more quickly transition into a getup behavior.
- **p. 11 / 8 RESULTS - extractive body cue:** However, for some motions, such as the Front-Flip, AMP is prone to converging to locally optimal behaviors, where instead of performing a flip, the character ...
- **p. 12 / 8 RESULTS - extractive body cue:** 9 DISCUSSION AND LIMITATIONS In this work, we presented an adversarial learning system for physicsbased character animation that enables characters to imitate diverse behaviors from ...
- **p. 11 / 8 RESULTS - extractive body cue:** Unlike previous motion tracking methods, our approach does not require a manually designed tracking objective or a phase-based synchronization of the reference motion and the ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 5 (4 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 7 (4 BACKGROUND)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, it can be exceptionally difficult to design a style-reward 𝑟𝑆 that leads a character to learn naturalistic behaviors, or behaviors that conform to a particular style. (p. 5, 4 BACKGROUND).
- **Actual contribution:** We present one of the first adversarial learning systems that is able to produce high-quality full-body motions for physically simulated characters. (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** Training the motion prior with a diverse dataset results in more flexible and optimal policies that are able to achieve a wider range of target speeds. (p. 9, 8 RESULTS).
- **Explicit failure boundary:** 9 DISCUSSION AND LIMITATIONS In this work, we presented an adversarial learning system for physicsbased character animation that enables characters to imitate diverse behaviors from large unstructured datasets, without the ... (p. 12, 8 RESULTS).
