# Towards Physically Executable 3D Gaussian for Embodied Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=HB6KvsqcAn.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/246616. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, Navigation, Gaussian Splatting
- Official paper: https://openreview.net/forum?id=HB6KvsqcAn
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/246616
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 (2) Lack of a physically executable structure.를 문제로 두고, We introduce a 3DGS-Mesh Hybrid Representation: starting from our mesh scene data, we extract collision bodies for each object as the physics layer, while using 3DGS to provide photorealistic appearance.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** 3D Gaussian Splatting (3DGS), a 3D representation method with photorealistic real-time rendering capabilities, is regarded as an effective tool for narrowing the sim-to-real gap.
- **p. 1 / ABSTRACT - extractive body cue:** However, it lacks fine-grained semantics and physical executability for Visual-Language Navigation (VLN).
- **p. 1 / ABSTRACT - extractive body cue:** To address this, we propose SAGE-3D (Semantically and Physically Aligned Gaussian Environments for 3D Navigation), a new paradigm that upgrades 3DGS into an executable, semantically ...
- **p. 1 / ABSTRACT - extractive body cue:** It comprises two components: (1) ObjectCentric Semantic Grounding, which adds object-level fine-grained annotations to 3DGS; and (2) Physics-Aware Execution Jointing, which embeds collision objects into ...
- **p. 1 / ABSTRACT - extractive body cue:** We release InteriorGS, containing 1K object-annotated 3DGS indoor scene data, and introduce SAGE-Bench, the first 3DGS-based VLN benchmark with 2M VLN data.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (2) Lack of a physically executable structure.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Consequently, deriving reliable collision geometries from 3DGS is difficult, and aligning semantics with appearance is non-trivial.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce a 3DGS-Mesh Hybrid Representation: starting from our mesh scene data, we extract collision bodies for each object as the physics layer, while using ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we present SAGE-3D (Semantically and Physically Aligned Gaussian Environments for 3D Navigation), a paradigm that upgrades 3DGS from a purely perceptual scene ...
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** The training data did not include any VLN-CE R2R or RxR samples.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** We selected 500k "trajectory-instruction" pairs from SAGE-Bench, with no overlap with the test set.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Vision-and-Language Navigation (VLN) is a core capability for Vision-Language Action (VLA) models, enabling them to follow natural language instructions and navigate complex indoor spaces (Wei et al., 2025; Zhang et al., 2024). | camera/depth stream, pose, map와 language goal | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | Vision-and-Language, Navigation, VLN, core, capability, Vision-Language, Action, VLA, models, enabling, them, follow | robot pose, free-space/semantic map와 local goal | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/action | For data, we provide a hierarchical instruction scheme that combines high-level semantic goals (especially task-causal ones like "I'm thirsty, get water from the table") with low-level actions (e.g., "move from stool to ... | collision-free trajectory 또는 velocity command | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 15 (A IMPLEMENTATION DETAILS) |
| Objective/outcome | We run A*-based shortest-path search to generate trajectories with a cost function that integrates free-space distance, narrow-passage penalties, and area preferences to ensure both obstacle avoidance and task feasibility. | goal reach, safety, localization error와 replanning latency | p. 15 (A IMPLEMENTATION DETAILS) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce a 3DGS-Mesh Hybrid Representation: starting from our mesh scene data, we extract collision bodies for each object as the physics layer, while using ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we present SAGE-3D (Semantically and Physically Aligned Gaussian Environments for 3D Navigation), a paradigm that upgrades 3DGS from a purely perceptual scene ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Even the recent SOTA model NaVILA achieves only a 0.39 success rate on high-level instructions, significantly lower than its 0.56 success rate on low-level instructions.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** The results show that 3DGS scene data achieves a perframe rendering time of 6.2 ms and an average memory usage of 220 MB, outperforming the ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4, models trained entirely on SAGE-Bench data (without any VLN-CE data) achieved clear performance improvements over their respective baselines.
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Specifically, with the same number of augmented scenes (800), increasing the sampling density progressively improves the VLN model's performance on the val-unseen split.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** In addition to the three novel metrics we proposed in Section 3.3 for evaluating the natural continuity of model navigation - CSR, ICP, and PS ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For example, the 0.20 OSR achieved by InternVL-3 exceeds that of NaVid (0.17 OSR).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Embodiment/environment | Data in # Train SAGE-Bench VLN #Scenes #Samples SR ↑ OSR ↑ SPL ↑ CSR ↑ ICP ↓ PS ↑ 800 240k 0.42 0.47 0.42 0.50 0.61 0.63 800 120k 0.40 0.43 ... | hardware/simulator version and reset protocol | p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Dataset/benchmark | These findings indicate that the number of scenes (Scenes) has a greater impact than the number of samples (Samples), suggesting that diversity of environments is more critical for learning VLN. | role, split, size and leakage | p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Metric | In addition to the three novel metrics we proposed in Section 3.3 for evaluating the natural continuity of model navigation - CSR, ICP, and PS - we also adopt common metrics used ... | definition, denominator, direction and uncertainty | p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Baseline/ablation | 4, models trained entirely on SAGE-Bench data (without any VLN-CE data) achieved clear performance improvements over their respective baselines. | fair input/data/compute/action matching | p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, two episode complexity categories, and three newly designed natural ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4 corroborate this finding: the NaVILA model (blue trajectory) exhibits unsmooth movement and persistent collisions that conventional metrics fail to reveal.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Traditional 3DGS vs. Our work. Compared with traditional 3DGS, our InteriorGS pro- vides object-level 3DGS annotations across diverse indoor and outdoor scenes, including ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Overview of SAGE-3D, which consists of two key components: (1) Object-Level Semantic Grounding, 3DGS data is annotated by expect at the object level, ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** An episode is terminated immediately if a collision occurs, and the maximum episode time is set to 120 seconds.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** In addition to the three novel metrics we proposed in Section 3.3 for evaluating the natural continuity of model navigation - CSR, ICP, and PS ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** For instance, in Case 1, the model hugs the wall for a long period, yet the collision rate CR is only 1, while our ICP ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 (2) Lack of a physically executable structure.를 문제로 두고, We introduce a 3DGS-Mesh Hybrid Representation: starting from our mesh scene data, we extract collision bodies for each object as the physics layer, while using 3DGS to provide photorealistic appearance.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 15 (A IMPLEMENTATION DETAILS), p. 15 (A IMPLEMENTATION DETAILS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
