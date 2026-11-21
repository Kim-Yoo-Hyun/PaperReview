# Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://roboticsproceedings.org/rss14/p49.html.
> PDF retrieval source: https://arxiv.org/pdf/1709.10087. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / RSS
- Authors: Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, Sergey Levine
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, Reinforcement Learning, dexterous manipulation
- Official paper: https://roboticsproceedings.org/rss14/p49.html
- Full-text retrieval: https://arxiv.org/pdf/1709.10087
- Code/Project: https://sites.google.com/view/deeprl-dexterous-manipulation
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

DAPG는 소수의 사람 시연을 정책 그래디언트 학습에 사용해 다지 손 조작에 필요한 시뮬레이션 경험을 줄인다. [PDF 1쪽](https://arxiv.org/pdf/1709.10087#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Dexterous multi-fingered hands are extremely versatile and provide a generic way to perform a multitude of tasks in human-centric environments.
- **p. 1 / Abstract - extractive body cue:** However, effectively controlling them remains challenging due to their high dimensionality and large number of potential contacts.
- **p. 1 / Abstract - extractive body cue:** Deep reinforcement learning (DRL) provides a model-agnostic approach to control complex dynamical systems, but has not been shown to scale to highdimensional dexterous manipulation.
- **p. 1 / Abstract - extractive body cue:** Furthermore, deployment of DRL on physical systems remains challenging due to sample inefficiency.
- **p. 1 / Abstract - extractive body cue:** Consequently, the success of DRL in robotics has thus far been limited to simpler manipulators and tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these methods typically rely on accurate dynamics models and state estimates, which are often difficult to obtain for contact rich manipulation tasks, especially in ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the current benchmarks are typically quite limited both in the dimensionality of the tasks and the complexity of the interactions.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** To overcome this challenge, we propose to augment the policy search process with a small number of human demonstrations collected in virtual reality (VR).
- **p. 2 / I. INTRODUCTION - extractive body cue:** We attribute this to human priors in the demonstrations which bias the learning towards more robust strategies. • We propose a set of dexterous hand ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Indeed, model-free methods have been used for acquiring manipulation skills [52], [13], but so far have been limited to simpler behaviors with 2-3 finger hands ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Thus, before we can develop DRL methods suitable for dexterous manipulation with robotic hands, we must set up a suite of manipulation tasks that exercise ...
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** A number of pre-conditioned policy gradient methods have been developed in literature [19], [4], [35], [34], [43], [40], [44] and in principle any of them ...
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** We first present some RL preliminaries, followed by the base RL algorithm we use for learning, and finally describe our procedure to incorporate demonstrations.
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** First, NPG computes the vanilla policy gradient, or REINFORCE [54] gradient: g = 1 NT N X i=1 T X t=1 ∇θ log πθ(ai t/si ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | However, this versatility comes at the price of high dimensional observation and action spaces, complex and discontinuous contact patterns, and under-actuation during nonprehensile manipulation. | observation history와 expert trajectory/action | p. 1 (I. INTRODUCTION), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)) |
| State/latent | However, versatility, comes, price, high, dimensional, observation, action, spaces, complex, discontinuous, contact | behavior policy와 temporal action context | p. 1 (I. INTRODUCTION), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), p. 2 (I. INTRODUCTION) |
| Output/action | S ∈Rn and A ∈Rm represent the state and actions. | predicted action 또는 action chunk | p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), p. 2 (I. INTRODUCTION), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)) |
| Objective/outcome | In policy gradient methods, the parameters of the policy are directly optimized to maximize the objective, η(θ), using local search methods such as gradient ascent. | imitation error, task success, robustness와 compounding error | p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)) |

## Main Claims and Actual Contribution

- 시연으로 정책을 초기화하고 정책 그래디언트 갱신에도 시연 행동에 대한 항을 추가한다. [PDF 3쪽](https://arxiv.org/pdf/1709.10087#page=3) · [PDF 4쪽](https://arxiv.org/pdf/1709.10087#page=4)
- 모의 다지 손에서 물체 재배치·도구 사용 등 접촉 과제를 비교하고 시연 사용 여부에 따른 표본 효율과 행동을 평가했다. [PDF 5쪽](https://arxiv.org/pdf/1709.10087#page=5) · [PDF 7쪽](https://arxiv.org/pdf/1709.10087#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 6 (2) Do the resulting policies exhibit desirable properties like) |
| Embodiment/environment | In order to benchmark the capabilities of DRL with regard to the dexterous manipulation tasks outlined in Section III, we evaluate the NPG algorithm described briefly in Section V, and the DDPG ... | hardware/simulator version and reset protocol | p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like) |
| Dataset/benchmark | 3) Are the resulting movements safe for execution on physical hardware, and are elegant/nimble/human-like? | role, split, size and leakage | p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like), p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like) |
| Metric | Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with sparse task completion rewards. | definition, denominator, direction and uncertainty | p. 6 (V. RESULTS AND DISCUSSION), p. 7 (2) Do the resulting policies exhibit desirable properties like), p. 6 (2) Do the resulting policies exhibit desirable properties like) |
| Baseline/ablation | Figure 10: Performance of RL with demonstrations methods - DAPG(ours) and DDPGfD. DAPG significantly outperforms DDPGfD. For DAPG, we plot the performance of the stochastic policy used for exploration. At any iteration, ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with sparse ...
- **p. 6 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** robustness to variations in the environment?
- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** The mental models of solution strategies that humans have for these tasks are indeed quite robust.
- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** Furthermore, we take the additional step of analyzing the robustness of these policies to variations in environments that were not experienced during training.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG))이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, these methods typically rely on accurate dynamics models and state estimates, which are often difficult to obtain for contact rich manipulation tasks, especially in the real world. (p. 1, I. INTRODUCTION).
- **Actual contribution:** To overcome this challenge, we propose to augment the policy search process with a small number of human demonstrations collected in virtual reality (VR). (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Figure 1: We demonstrate a wide range of dexterous manipulation skills such as object relocation, in-hand manipulation, tool use, and opening doors using DRL methods. By augmenting with human demonstrations, ... (p. 1, Figure/Table caption).
- **Explicit failure boundary:** Indeed, model-free methods have been used for acquiring manipulation skills [52], [13], but so far have been limited to simpler behaviors with 2-3 finger hands or wholearm manipulators, which do ... (p. 1, I. INTRODUCTION).
