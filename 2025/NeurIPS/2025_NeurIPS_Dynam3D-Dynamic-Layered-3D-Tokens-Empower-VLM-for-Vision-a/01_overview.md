# Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=s6k9l5yX8e.
> PDF retrieval source: https://arxiv.org/pdf/2505.11383. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, 3D Vision, Navigation
- Official paper: https://openreview.net/forum?id=s6k9l5yX8e
- Full-text retrieval: https://arxiv.org/pdf/2505.11383
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 2) These models lack mechanisms for structured scene memory.를 문제로 두고, In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and real-time hierarchical updates in dynamic environme ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-and-Language Navigation (VLN) is a core task where embodied agents leverage their spatial mobility to navigate in 3D environments toward designated destinations based on natural ...
- **p. 1 / Abstract - extractive body cue:** Recently, video-language large models (Video-VLMs) with strong generalization capabilities and rich commonsense knowledge have shown remarkable performance when applied to VLN tasks.
- **p. 1 / Abstract - extractive body cue:** However, these models still encounter the following challenges when applied to real-world 3D navigation: 1) Insufficient understanding of 3D geometry and spatial semantics; 2) Limited ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to ...
- **p. 1 / Abstract - extractive body cue:** Given posed RGB-D images, our Dynam3D projects 2D CLIP features into 3D space and constructs multi-level 3D patch-instance-zone representations for 3D geometric and semantic understanding ...
- **p. 1 / 1 Introduction - extractive body cue:** 2) These models lack mechanisms for structured scene memory.
- **p. 1 / 1 Introduction - extractive body cue:** Despite these recent advances, several limitations still remain: 1) Video-based models struggle to capture spatial geometry and semantics in large-scale 3D environments.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and ...
- **p. 2 / 1 Introduction - extractive body cue:** We propose Dynam3D to alleviate the limitations mentioned above.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to ...
- **p. 1 / 1 Introduction - extractive body cue:** As illustrated in Figure 1(a), recent works [5-7] have predominantly focused on using video-based large models [8-10] to develop monocular VLN systems.
- **p. 2 / 1 Introduction - extractive body cue:** These rendered 3D patch features combined with instance and zone representations serve as visual input to the 3D Vision-Language Model (VLM).
- **p. 1 / Abstract - extractive body cue:** By leveraging large-scale 3D-language pretraining and task-specific adaptation, our Dynam3D sets new state-of-the-art performance on VLN benchmarks including R2R-CE, REVERIE-CE and NavRAG-CE under monocular settings.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to train 3D-VLM in navigation action prediction. | camera/depth stream, pose, map와 language goal | p. 1 (Abstract), p. 2 (1 Introduction) |
| State/latent | address, limitations, Dynam3D, dynamic, layered, representation, model, leverages, language-aligned, generalizable, hierarchical, representations | robot pose, free-space/semantic map와 local goal | p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/action | Instruction: "Please go to the kitchen and take the bread out of the microwave for me." … Video-Language Large Model … Action 3D-Language Large Model Action • Large-scale scene exploration and memory ... | collision-free trajectory 또는 velocity command | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | This is due to the practical constraint that most robots are equipped with monocular cameras instead of panoramic cameras. | goal reach, safety, localization error와 replanning latency | p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and ...
- **p. 2 / 1 Introduction - extractive body cue:** We propose Dynam3D to alleviate the limitations mentioned above.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to ...
- **p. 1 / 1 Introduction - extractive body cue:** As illustrated in Figure 1(a), recent works [5-7] have predominantly focused on using video-based large models [8-10] to develop monocular VLN systems.
- **p. 7 / 4 Experiments - extractive body cue:** Our Dynam3D still demonstrates substantial improvements, outperforming NaVid by over 13% in Success Rate (SR) on REVERIE-CE and by over 5% on NavRAG-CE.
- **p. 7 / 4 Experiments - extractive body cue:** Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly 5% in navigation success rate (SR).
- **p. 8 / 4 Experiments - extractive body cue:** Under the Lifelong Memory setting, our Dynam3D also achieves performance gains, with a 2.7% SR improvement on R2R-CE and a 4.9% SR improvement on REVERIE-CE.
- **p. 8 / 4 Experiments - extractive body cue:** In the static environment (Table 4) Dynam3D achieves a 20% higher success rate than baselines, reaching 70% after pre-exploration.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | Methods Pre-exploration Lifelong Memory R2R-CE Val REVERIE-CE Val NE↓OSR↑SR↑SPL↑NE↓OSR↑SR↑SPL↑ NaVid [5] × × 5.47 49.1 37.4 35.9 6.74 36.3 26.6 20.8 g3D-LF [14] × × 5.70 59.5 47.2 34.6 6.50 41.6 34.4 ... | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Dataset/benchmark | To ensure a fair comparison on the more challenging and realistic benchmarks such as REVERIE-CE which use coarse-grained and high-level destination description, and NavRAG-CE which requires understanding complex user demands, we retrain ... | role, split, size and leakage | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 14 (A.1 Datasets and Experimental Details) |
| Metric | Our Dynam3D still demonstrates substantial improvements, outperforming NaVid by over 13% in Success Rate (SR) on REVERIE-CE and by over 5% on NavRAG-CE. | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Baseline/ablation | Compared to prior state-of-the-art methods, e.g., g3D-LF and Uni-NaVid, our Dynam3D achieves an improvement of nearly 5% in navigation success rate (SR). | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Different vision-language large models for monocular VLN tasks. Compared to previous video-based representations (a), our Dynam3D (b) adopts dynamic hierarchical 3D representations offering ...
- **p. 9 / 4 Experiments - extractive body cue:** The navigation performance significantly decreases without Subspace Alignment supervision (Table 6, row 3), highlighting the limitations of naive CLIP feature distillation for 3D instance supervision.
- **p. 8 / 4 Experiments - extractive body cue:** In the dynamic setting (Figure 4 and Table 5), the target is manually moved to another location once the robot reach within two meters of ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 2) These models lack mechanisms for structured scene memory.를 문제로 두고, In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and real-time hierarchical updates in dynamic environme ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
