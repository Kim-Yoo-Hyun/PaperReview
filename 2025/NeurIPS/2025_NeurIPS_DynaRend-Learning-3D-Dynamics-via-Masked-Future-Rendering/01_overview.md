# DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=r4dzaP61QH.
> PDF retrieval source: https://arxiv.org/pdf/2510.24261. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, 3D Vision
- Official paper: https://openreview.net/forum?id=r4dzaP61QH
- Full-text retrieval: https://arxiv.org/pdf/2510.24261
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Despite the promise of end-to-end approaches for generalizable robotic control, the lack of abundant, diverse and high-quality robot data remains a key bottleneck.를 문제로 두고, Our contribution can be summarized as follows: • We propose DynaRend, a novel representation learning framework that learns generalizable triplane features via masked future rendering for robotic manipulation. • We conduct a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Learning generalizable robotic manipulation policies remains a key challenge due to the scarcity of diverse real-world training data.
- **p. 1 / Abstract - extractive body cue:** While recent approaches have attempted to mitigate this through self-supervised representation learning, most either rely on 2D vision pretraining paradigms such as masked image modeling, ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we present DynaRend, a representation learning framework that learns 3D-aware and dynamics-informed triplane features via masked reconstruction and future prediction using differentiable ...
- **p. 1 / Abstract - extractive body cue:** By pretraining on multi-view RGB-D video data, DynaRend jointly captures spatial geometry, future dynamics, and task semantics in a unified triplane representation.
- **p. 1 / Abstract - extractive body cue:** The learned representations can be effectively transferred to downstream robotic manipulation tasks via action value map prediction.
- **p. 1 / 1 Introduction - extractive body cue:** Despite the promise of end-to-end approaches for generalizable robotic control, the lack of abundant, diverse and high-quality robot data remains a key bottleneck.
- **p. 1 / 1 Introduction - extractive body cue:** However, these approaches mainly model dynamics in 2D and lack explicit awareness of the underlying 3D scene structure.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our contribution can be summarized as follows: • We propose DynaRend, a novel representation learning framework that learns generalizable triplane features via masked future rendering ...
- **p. 2 / 1 Introduction - extractive body cue:** We evaluate our method on two challenging robotic manipulation benchmarks, RLBench [21] and Colosseum [32].
- **p. 3 / 3 Methodology - extractive body cue:** In this section, we present the proposed DynaRend in detail.
- **p. 4 / 3 Methodology - extractive body cue:** Each demonstration consists of a trajectory sequence where each element is represented as a triplet including visual observation O, language instruction l, and end-effector state ...
- **p. 1 / 1 Introduction - extractive body cue:** Developing versatile robotic control policies capable of performing diverse tasks across varying environments has emerged as an active area of research in embodied AI [4, ...
- **p. 4 / 3 Methodology - extractive body cue:** To incorporate task-specific information, we encode the language instruction using a pretrained CLIP [34] text encoder and concatenate the resulting embeddings l with the triplane ...
- **p. 6 / 3 Methodology - extractive body cue:** This position is then used to query the triplane representation for subsequent rotation and gripper state prediction, following the same decoding procedure as during training.
- **p. 6 / 3 Methodology - extractive body cue:** The resulting feature is then passed through a lightweight MLP to predict discretized rotation Euler angles and the binary gripper open/close state, both supervised using ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Among various paradigms, keyframe-based manipulation has emerged as a popular approach, where the agent is tasked with predicting the next key action state - including the end-effector pose and gripper state - ... | image/video, language instruction, proprioception과 history | p. 3 (3 Methodology), p. 3 (3 Methodology) |
| State/latent | Among, various, paradigms, keyframe-based, manipulation, emerged, popular, where, agent, tasked, predicting, next | language-grounded task state와 action-policy context | p. 3 (3 Methodology), p. 3 (3 Methodology), p. 4 (3 Methodology) |
| Output/action | 3.1 Problem Definition Language-conditioned robotic manipulation is a fundamental yet challenging task that requires agents to ground natural language instructions into executable actions based on visual observations. | continuous action, pose 또는 action chunk | p. 3 (3 Methodology), p. 4 (3 Methodology), p. 4 (3 Methodology) |
| Objective/outcome | The overall objective for pretraining is a weighted combination of two loss terms for reconstruction and future prediction respectively: Lpretrain = λreconLrecon + λpredLpred, (6) where λrecon and λpred are loss weights. | instruction following, task success, generalization과 latency | p. 6 (3 Methodology), p. 6 (3 Methodology), p. 4 (3 Methodology) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our contribution can be summarized as follows: • We propose DynaRend, a novel representation learning framework that learns generalizable triplane features via masked future rendering ...
- **p. 2 / 1 Introduction - extractive body cue:** We evaluate our method on two challenging robotic manipulation benchmarks, RLBench [21] and Colosseum [32].
- **p. 3 / 3 Methodology - extractive body cue:** In this section, we present the proposed DynaRend in detail.
- **p. 4 / 3 Methodology - extractive body cue:** Each demonstration consists of a trajectory sequence where each element is represented as a triplet including visual observation O, language instruction l, and end-effector state ...
- **p. 1 / 1 Introduction - extractive body cue:** Developing versatile robotic control policies capable of performing diverse tasks across varying environments has emerged as an active area of research in embodied AI [4, ...
- **p. 7 / 4 Experiments - extractive body cue:** Notably, compared to the baseline RVT [13] model, DynaRend achieves an average success rate improvement of 32.3%.
- **p. 7 / 4 Experiments - extractive body cue:** Our model achieves the best trade-off between success rate and inference speed when compared to other baseline methods, demonstrating strong manipulation performance without sacrificing computational ...
- **p. 8 / 4 Experiments - extractive body cue:** Compared to existing 2D pretraining methods, such as MVP [43] and R3M [30], as well as 3D pretraining approaches like 3D-MVP [33], DynaRend achieves consistently ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | We conduct simulation experiments on two challenging robotic manipulation benchmarks: RLBench [21] and Colosseum [32]. | hardware/simulator version and reset protocol | p. 6 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | Colosseum [32] is a benchmark for evaluating the generalization capabilities of manipulation policies under 12 types of environmental perturbations across 20 tasks, including changes in object color, texture, size, and lighting. | role, split, size and leakage | p. 6 (4 Experiments), p. 9 (4 Experiments), p. 6 (4 Experiments), p. 9 (4 Experiments) |
| Metric | We report the average success rate and standard deviation for all tasks. policy architectures and pretraining strategies. | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Baseline/ablation | Our model achieves the best trade-off between success rate and inference speed when compared to other baseline methods, demonstrating strong manipulation performance without sacrificing computational efficiency. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4 Experiments - extractive body cue:** Notably, on tasks involving distractor objects, RVT-2 struggles to distinguish between different unseen items, leading to frequent failure cases.
- **p. 14 / A Implementation Details - extractive body cue:** To address this limitation, we leverage a pretrained visual-conditioned multi-view diffusion model to generate novel target views as additional supervision.
- **p. 6 / 4 Experiments - extractive body cue:** We report the average success rate across each perturbation category to assess the robustness of the policy to different types of environmental changes.
- **p. 8 / 4 Experiments - extractive body cue:** Removing masking entirely or applying an excessively high mask ratio both lead to degraded performance.
- **p. 8 / 4 Experiments - extractive body cue:** Additionally, when compared to the RVT baseline trained from scratch, DynaRend demonstrates significantly greater robustness to various types of environmental variations.
- **p. 9 / 4 Experiments - extractive body cue:** In contrast, our method maintains robust performance, benefiting from the pretrained spatially grounded and semantically coherent representations.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Despite the promise of end-to-end approaches for generalizable robotic control, the lack of abundant, diverse and high-quality robot data remains a key bottleneck.를 문제로 두고, Our contribution can be summarized as follows: • We propose DynaRend, a novel representation learning framework that learns generalizable triplane features via masked future rendering for robotic manipulation. • We conduct a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Methodology), p. 4 (3 Methodology) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
