# Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://iclr.cc/virtual/2026/poster/10010454.
> PDF retrieval source: https://arxiv.org/pdf/2602.18025. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, offline reinforcement learning, cross-embodiment, transfer
- Official paper: https://iclr.cc/virtual/2026/poster/10010454
- Full-text retrieval: https://arxiv.org/pdf/2602.18025
- Code/Project: https://iclr.cc/virtual/2026/poster/10010454
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 offline_rl 문제를 이해하기 위해 읽는다. 본문은 To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these paradigms, and propose methods to mitigate the challenges that arise ...를 문제로 두고, 3.3 NETWORK ARCHITECTURE In this section, we present our approach to cross-embodiment learning in an offline RL setting.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Scalable robot policy pre-training has been hindered by the high cost of collecting high-quality demonstrations for each platform.
- **p. 1 / ABSTRACT - extractive body cue:** In this study, we address this issue by uniting offline reinforcement learning (offline RL) with cross-embodiment learning.
- **p. 1 / ABSTRACT - extractive body cue:** Offline RL leverages both expert and abundant suboptimal data, and cross-embodiment learning aggregates heterogeneous robot trajectories across diverse morphologies to acquire universal control priors.
- **p. 1 / ABSTRACT - extractive body cue:** We perform a systematic analysis of this offline RL and cross-embodiment paradigm, providing a principled understanding of its strengths and limitations.
- **p. 1 / ABSTRACT - extractive body cue:** To evaluate this offline RL and cross-embodiment paradigm, we construct a suite of locomotion datasets spanning 16 distinct robot platforms.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these paradigms, and propose ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, despite the promise of foundation models for robotics, they face a critical limitation.

## Core Idea

- **p. 4 / 1 INTRODUCTION - extractive body cue:** 3.3 NETWORK ARCHITECTURE In this section, we present our approach to cross-embodiment learning in an offline RL setting.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this, we propose a novel group-task update strategy based on robot embodiment information.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** To address this issue, we propose a novel mitigation strategy that groups robots according to their embodiment, thus reducing gradient conflicts.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce and analyze the new benchmark that combines offline RL with crossembodiment learning across up to 16 distinct robot platforms.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these paradigms, and propose ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Specifically, we encode each action with an action encoder to obtain a latent action vector, which we then concatenate with the latent representation of the ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For example, implicit Q-learning (IQL) (Kostrikov et al., 2021) first fits a state value function Vψ(s) via expectile regression to capture an upper expectile of ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** We pre-train via offline RL on a dataset excluding one robot, then finetune that robot with pre-trained networks, comparing it to a model trained without ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3 EXPERIMENTAL SETUP 3.1 PROBLEM SETTING We study multi-embodiment offline RL, where a single policy must control multiple robot morphologies under a common state-action interface. | dataset state/observation, action, reward와 return-to-go | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | EXPERIMENTAL, SETUP, PROBLEM, SETTING, study, multi-embodiment, offline, where, single, policy, must, control | Q/value 또는 sequence-policy state | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/action | Finally, the policy πϕ(a / s) is extracted via advantage-weighted BC, avoiding any need to evaluate out-of-distribution actions. | dataset-supported action sequence | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective/outcome | 2 RELATED WORKS 2.1 OFFLINE RL Offline RL aims to learn a policy that maximizes cumulative reward using only a static dataset of environment interactions without further online interaction (Levine et al., ... | offline policy value, OOD safety와 closed-loop success | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 4 / 1 INTRODUCTION - extractive body cue:** 3.3 NETWORK ARCHITECTURE In this section, we present our approach to cross-embodiment learning in an offline RL setting.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this, we propose a novel group-task update strategy based on robot embodiment information.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** To address this issue, we propose a novel mitigation strategy that groups robots according to their embodiment, thus reducing gradient conflicts.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce and analyze the new benchmark that combines offline RL with crossembodiment learning across up to 16 distinct robot platforms.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these paradigms, and propose ...
- **p. 9 / 1 INTRODUCTION - extractive body cue:** From the table, EG achieves the most stable and substantial improvement on the 70% Suboptimal Forward dataset (+14.41, +38.34%).
- **p. 8 / 1 INTRODUCTION - extractive body cue:** First, we evaluate performance improvements in cross-embodiment offline RL on six datasets containing varying proportions of suboptimal data.
- **p. 9 / 1 INTRODUCTION - extractive body cue:** It is somewhat surprising that the Heuristic split did not improve performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 9 (1 INTRODUCTION), p. 8 (1 INTRODUCTION) |
| Embodiment/environment | Preprint (a) Embodiment-based similarity matrix (b) Average gradient cosine similarity matrix (c) Embodiment-based similarity vs. mean gradient cosine similarity Figure 3: (a) Embodiment-based similarity matrix (1 - min-max-normalized F ... | hardware/simulator version and reset protocol | p. 7 (1 INTRODUCTION), p. 8 (1 INTRODUCTION) |
| Dataset/benchmark | The gains are especially large when the dataset contains more suboptimal trajectories, as in the replay and 70% Suboptimal splits. | role, split, size and leakage | p. 7 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION), p. 7 (1 INTRODUCTION) |
| Metric | Table 7: Reward coefficients rc and curriculum length T for each robot. C DATASET DETAIL Figure 7 overlays histograms of the total reward per episode for the Forward datasets, comparing the three ... | definition, denominator, direction and uncertainty | p. 14 (Figure/Table caption), p. 10 (1 INTRODUCTION), p. 15 (Figure/Table caption) |
| Baseline/ablation | Compared to the IQL cross-embodiment baseline, the average improvement in the Suboptimal datasets 70% is 7.15% for PCGrad, 18.33% for SEL and 33.99% for EG. | fair input/data/compute/action matching | p. 9 (1 INTRODUCTION), p. 10 (1 INTRODUCTION), p. 8 (1 INTRODUCTION) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 7 CONCLUSION - extractive body cue:** We also identified a core failure mode, inter-robot gradient conflicts, whose incidence grows with both the proportion of suboptimal data and the number of embodiments.
- **p. 10 / 7 CONCLUSION - extractive body cue:** We leave this combined direction for future work.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Expert vs. 70% Suboptimal IQL performance across robots and avg. gradient cosine similarity C on the 70% subop- timal dataset. Cells shaded blue ...
- **p. 9 / 1 INTRODUCTION - extractive body cue:** A likely reason is that coarse categories such as leg count cannot capture gradient-relevant factors like actuator placement, link lengths, mass distribution, and joint couplings.
- **p. 9 / 1 INTRODUCTION - extractive body cue:** In contrast, Random yields only a small gain (+1.16, +3.08%), and the intuitive fourway split Heuristic actually degrades performance (-3.14, -8.31%).

## Why Read It

RL, IL, offline learning, and robot data의 offline_rl 문제를 이해하기 위해 읽는다. 본문은 To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these paradigms, and propose methods to mitigate the challenges that arise ...를 문제로 두고, 3.3 NETWORK ARCHITECTURE In this section, we present our approach to cross-embodiment learning in an offline RL setting.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (1 INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
