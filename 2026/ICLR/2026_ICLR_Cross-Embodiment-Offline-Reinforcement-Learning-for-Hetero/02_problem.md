# Problem - Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10010454; PDF retrieval source: https://arxiv.org/pdf/2602.18025. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these paradigms, and propose methods to mitigate the challenges ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Scalable robot policy pre-training has been hindered by the high cost of collecting high-quality demonstrations for each platform.
- **p. 1 / ABSTRACT - extractive body cue:** In this study, we address this issue by uniting offline reinforcement learning (offline RL) with cross-embodiment learning.
- **p. 1 / ABSTRACT - extractive body cue:** Offline RL leverages both expert and abundant suboptimal data, and cross-embodiment learning aggregates heterogeneous robot trajectories across diverse morphologies to acquire universal control priors.
- **p. 1 / ABSTRACT - extractive body cue:** We perform a systematic analysis of this offline RL and cross-embodiment paradigm, providing a principled understanding of its strengths and limitations.
- **p. 1 / ABSTRACT - extractive body cue:** To evaluate this offline RL and cross-embodiment paradigm, we construct a suite of locomotion datasets spanning 16 distinct robot platforms.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these paradigms, and propose ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, despite the promise of foundation models for robotics, they face a critical limitation.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these ... | offline robot transition/trajectory dataset과 deployment MDP | body wording is the source claim |
| Observation / input | 3 EXPERIMENTAL SETUP 3.1 PROBLEM SETTING We study multi-embodiment offline RL, where a single policy must control multiple robot morphologies under a ... | dataset state/observation, action, reward와 return-to-go | exact sensor/frame/preprocessing from PDF body |
| State / latent | EXPERIMENTAL, SETUP, PROBLEM, SETTING, study, multi-embodiment, offline, where, single, policy | Q/value 또는 sequence-policy state | notation and tensor shape require body check |
| Output / action | RELATED, WORKS, OFFLINE, aims, learn, policy, maximizes, cumulative | dataset-supported action sequence | exact unit/frame/decoder require body check |
| Target outcome | offline return and deployment safety | offline policy value, OOD safety와 closed-loop success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | dataset transition (s,a,r,s′); body terms: EXPERIMENTAL, SETUP, PROBLEM, SETTING, study, multi-embodiment, offline, where, single, policy | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Decision / output variable | dataset-supported policy action; body terms: NETWORK, ARCHITECTURE, section, present, cross-embodiment, learning, offline, setting | p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (1 INTRODUCTION) |
| Objective / loss / cost | offline value with OOD control; cue terms: RELATED, WORKS, OFFLINE, aims, learn, policy, maximizes, cumulative | p. 7 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 7 (1 INTRODUCTION), p. 8 (1 INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 8 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Success / guarantee | offline return and deployment safety | p. 14 (Figure/Table caption), p. 10 (1 INTRODUCTION), p. 15 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, despite the promise of foundation models for robotics, they face a critical limitation.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Since collecting large datasets for any single robot is costly, pre-training on heterogeneous robot data has become a popular strategy to improve generalization capability (Open ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** To date, applications of offline RL to robot foundation models have been rare, owing to the difficulty of learning from unlabeled interaction data; thus, a ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Collecting manipulation data is time-consuming and expensive, and each new task requires careful teleoperation, specialized hardware, and often manual labeling, making data scaling difficult.

## What the Paper Changes

PDF body contribution framing (p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): 3.3 NETWORK ARCHITECTURE In this section, we present our approach to cross-embodiment learning in an offline RL setting.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this, we propose a novel group-task update strategy based on robot embodiment information.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** To address this issue, we propose a novel mitigation strategy that groups robots according to their embodiment, thus reducing gradient conflicts.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce and analyze the new benchmark that combines offline RL with crossembodiment learning across up to 16 distinct robot platforms.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these paradigms, and propose ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | We also identified a core failure mode, inter-robot gradient conflicts, whose incidence grows with both the proportion of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | We leave this combined direction for future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Table 2: Expert vs. 70% Suboptimal IQL performance across robots and avg. gradient cosine similarity C on the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | A likely reason is that coarse categories such as leg count cannot capture gradient-relevant factors like actuator placement, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

offline_rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), interface p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), objective p. 7 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 7 (1 INTRODUCTION), p. 8 (1 INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
