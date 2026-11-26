# Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/fe7f375ef01e43f17d2c32b28a176577-Abstract-Conference.html.
> PDF retrieval source: https://arxiv.org/pdf/2602.13810. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Guojian Zhan, Letian Tao, Pengcheng Wang, Yixiao Wang, Yuxin Chen, Yiheng Li, Hongyang Li, Masayoshi Tomizuka, Shengbo Li
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, flow policy, one-step generation, manipulation, offline RL
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/fe7f375ef01e43f17d2c32b28a176577-Abstract-Conference.html
- Full-text retrieval: https://arxiv.org/pdf/2602.13810
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

평균 속도 정책은 잠재 잡음에서 행동까지의 평균 속도장을 학습해 한 번의 흐름 갱신으로 연속 행동을 생성한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/fe7f375ef01e43f17d2c32b28a176577-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Learning expressive and efficient policy functions is a promising direction in reinforcement learning (RL).
- **p. 1 / ABSTRACT - extractive body cue:** While flow-based policies have recently proven effective in modeling complex action distributions with a fast deterministic sampling process, they still face a trade-off between expressiveness ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we propose mean velocity policy (MVP), a new generative policy function that models the mean velocity field to achieve the fastest one-step ...
- **p. 1 / ABSTRACT - extractive body cue:** To ensure its high expressiveness, an instantaneous velocity constraint (IVC) is introduced on the mean velocity field during training.
- **p. 1 / ABSTRACT - extractive body cue:** We theoretically prove that this design explicitly serves as a crucial boundary condition, thereby improving learning accuracy and enhancing policy expressiveness.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, a key limitation of existing generative policies is their dependence on iterative multi-step refinement from noise to actions (Wang et al., 2024a; 2025; Ding ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, this ODE theoretically suffers from the problem of multiple solutions due to a lack of explicit boundary conditions, that is, the value at any ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized threefold: • We propose a new flow-based policy, namely mean velocity policy (MVP), that enables fastest one-step action generation.
- **p. 3 / 3 METHOD - extractive body cue:** First, we introduce the mean velocity policy (MVP), showing how its integration with a "generateand-select" mechanism enables a direct mapping from noise to optimal actions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose the mean velocity policy (MVP) as an affirmative answer.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this, we introduce an instantaneous velocity constraint (IVC) to compensate for the lack of boundary conditions.
- **p. 5 / 3 METHOD - extractive body cue:** Inspired by this, we introduce the instantaneous velocity constraint (IVC), a training objective that explicitly enforces a boundary condition at t.
- **p. 4 / 3 METHOD - extractive body cue:** The resulting action, a⋆, then serves three purposes: (1) interacting with the environment, (2) acting as the target action for policy training, and (3) calculating ...
- **p. 6 / 3 METHOD - extractive body cue:** The policy training loss Lpolicy combines the mean velocity model loss in Eq.
- **p. 4 / 3 METHOD - extractive body cue:** In practice, at any given state s, the agent first generate N diverse candidate actions as ai = ai k(1) = ϵi + uθ(ϵi, 0, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For standard flow-based policies, this mapping is framed as a generative process: a velocity model, v(a(t), t, s), transforms a standard Gaussian noise (source) into the optimal action (target), with the state ... | multi-view observation, language/task label과 action trajectory | p. 3 (3 METHOD), p. 2 (2 PRELIMINARIES) |
| State/latent | standard, flow-based, policies, mapping, framed, generative, process, velocity, model, transforms, Gaussian, noise | shared representation, embodiment/task identity와 data distribution | p. 3 (3 METHOD), p. 2 (2 PRELIMINARIES), p. 3 (3 METHOD) |
| Output/action | (1) Grounded in the off-policy learning paradigm, our approach utilizes an action-value function (Qfunction) to guide policy improvement, which denotes the expected cumulative return for taking an action a in a state ... | dataset sample 또는 learned policy action | p. 2 (2 PRELIMINARIES), p. 3 (3 METHOD), p. 4 (3 METHOD) |
| Objective/outcome | Let θ denote the learnable parameters, the training objective is to minimize the residual of the mean flow identity in Eq. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD) |

## Main Claims and Actual Contribution

- 평균 속도장 학습에 순간 속도 일치 조건을 부과하고 이 조건이 경계에서 필요한 이유를 유도한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/fe7f375ef01e43f17d2c32b28a176577-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/fe7f375ef01e43f17d2c32b28a176577-Paper-Conference.pdf#page=4)
- Robomimic과 OGBench에서 과제 성공률과 흐름 단계 수에 따른 계산 부담을 비교한다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/fe7f375ef01e43f17d2c32b28a176577-Paper-Conference.pdf#page=6) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/fe7f375ef01e43f17d2c32b28a176577-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/fe7f375ef01e43f17d2c32b28a176577-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Embodiment/environment | We consider a total of 9 sparse-reward robotic manipulation tasks with varying difficulties. | hardware/simulator version and reset protocol | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Dataset/benchmark | 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 0.5 1.0 Success Rate (a) Robomimic-lift 0.0 0.5 1.0 1.5 2.0 Steps (×106) 0.0 0.5 1.0 Success Rate (b) Robomimic-can 0.0 0.5 1.0 1.5 ... | role, split, size and leakage | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Metric | Overall, our MVP secures the top position with an average success rate of 0.88 ± 0.05. | definition, denominator, direction and uncertainty | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Baseline/ablation | Figure 4: Training curves of ablation on the IVC. (2) Comparison with one-step variants of the aforementioned baselines. We compared our MVP against one-step variants of the aforementioned baselines: FQL-Onestep, BFN-Onestep, and ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Velocity field: blue arrows de- note the mean velocity over a time in- terval, with red arrows representing the instantaneous velocity at a ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The poor performance of BFN and QC is primarily because they rely on a 10-step flow policy, which requires iterative computation to transform noise into ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 5 (3 METHOD)이다.
