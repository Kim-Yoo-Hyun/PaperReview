# Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2303.18240.
> PDF retrieval source: https://arxiv.org/abs/2303.18240. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, representation learning, Embodied AI, Benchmark
- Official paper: https://arxiv.org/abs/2303.18240
- Full-text retrieval: https://arxiv.org/abs/2303.18240
- Code/Project: https://eai-vc.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Our findings reveal a challenge and opportunity for the community - the search for a PVR that is universally dominant (or "foundational") for EAI calls for innovations in architecture, learning paradigm, data ...를 문제로 두고, The visual cortex is a region of an organism's brain, which together with the motor cortex, enables sight to be converted into movement.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present the largest and most comprehensive empirical study of pre-trained visual representations (PVRs) or visual ‘foundation models' for Embodied AI.
- **p. 1 / Abstract - extractive body cue:** First, we curate CORTEXBENCH, consisting of 17 different tasks spanning locomotion, navigation, dexterous, and mobile manipulation.
- **p. 1 / Abstract - extractive body cue:** Next, we systematically evaluate existing PVRs and find that none are universally dominant.
- **p. 1 / Abstract - extractive body cue:** To study the effect of pre-training data size and diversity, we combine over 4,000 hours of egocentric videos from 7 different sources (over 4.3M images) ...
- **p. 1 / Abstract - extractive body cue:** Contrary to inferences from prior work, we find that scaling dataset size and diversity does not improve performance universally (but does so on average).
- **p. 3 / 1 Introduction - extractive body cue:** Our findings reveal a challenge and opportunity for the community - the search for a PVR that is universally dominant (or "foundational") for EAI calls ...
- **p. 1 / 1 Introduction - extractive body cue:** Unfortunately, prior studies are incommensurable - using different self-supervised learning (SSL) algorithms on different pre-training datasets, designed

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** The visual cortex is a region of an organism's brain, which together with the motor cortex, enables sight to be converted into movement.
- **p. 1 / 1 Introduction - extractive body cue:** In this work, we ask the same question that Fukushima [1, 2] asked nearly 50 years ago - how do we design an artificial visual ...
- **p. 2 / 1 Introduction - extractive body cue:** The exhaustiveness of this study enables us to draw conclusions with unprecedented scope and confidence.
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** We present an evaluation of object navigation (ObjectNav) using the HM3D-SEM dataset [61].
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** The dataset was collected using Habitat-Web [61, 71] and Amazon Mechanical Turk, and consists of 77k demonstrations for 80 scenes from the HM3D-SEM dataset [69].
- **p. 16 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** We use patch representations for ViT-based PVRs and grid-features from last convolutional layer for ResNet models, passed through a compression layer [14] for a lower ...
- **p. 16 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** When using vision transformers (ViT) based PVRs, we use the [CLS] token as input to the policy, and with ResNets we use features from the ...
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** For Reach-Cube, the state for the BC policy is [xft t , zt], where xft t is the current fingertip position and zt is the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For Reach-Cube, the state for the BC policy is [xft t , zt], where xft t is the current fingertip position and zt is the latent visual state vector, obtained by passing ... | standardized observation, action, task state와 evaluation split | p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 1 (1 Introduction) |
| State/latent | Reach-Cube, state, policy, where, current, fingertip, position, latent, visual, vector, obtained, passing | benchmark state/goal와 method decision | p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 1 (1 Introduction), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH) |
| Output/action | In this work, we ask the same question that Fukushima [1, 2] asked nearly 50 years ago - how do we design an artificial visual cortex, the module in a computational system ... | policy/controller trajectory 또는 measured result | p. 1 (1 Introduction), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 16 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH) |
| Objective/outcome | We train agents with the reward functions presented in [67] utilizing the following settings: success weighting cs = 5.0, angle success weighting ca = 5.0, goal radius rg = 1.0, angle threshold ... | success metric, robustness, generalization과 reproducibility | p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 18 (A.6 Scaling Hypothesis Pretraining Details), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH) |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** The visual cortex is a region of an organism's brain, which together with the motor cortex, enables sight to be converted into movement.
- **p. 1 / 1 Introduction - extractive body cue:** In this work, we ask the same question that Fukushima [1, 2] asked nearly 50 years ago - how do we design an artificial visual ...
- **p. 2 / 1 Introduction - extractive body cue:** The exhaustiveness of this study enables us to draw conclusions with unprecedented scope and confidence.
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** We present an evaluation of object navigation (ObjectNav) using the HM3D-SEM dataset [61].
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** The dataset was collected using Habitat-Web [61, 71] and Amazon Mechanical Turk, and consists of 77k demonstrations for 80 scenes from the HM3D-SEM dataset [69].
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: An artificial visual cortex for embodied in- telligence must support a diverse range of sensorimotor skills, environments, and embodiments; we curate COR- TEXBENCH ...
- **p. 8 / Results - extractive body cue:** Specifically, we see an improvement in ObjectNav success rate (SR) of +7.4 (60.3 →67.7), ImageNav SR of +11.3 (70.3 →81.6), and Mobile Pick SR of ...
- **p. 8 / Results - extractive body cue:** In domains that involve large-scale IL or RL (ObjectNav, ImageNav, and Mobile Pick), the strategy proposed in [5] of adapting VC-1 with E2E fine-tuning significantly ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 2 (Figure/Table caption), p. 8 (Results) |
| Embodiment/environment | We carried out experiments on the real TriFinger robot (shown in Figure 9) for the Push-Cube task, after training a model using behavior cloning on 30 real-world demonstrations. | hardware/simulator version and reset protocol | p. 21 (A.11 TriFinger Hardware Experiment Setup), p. 5 (Results) |
| Dataset/benchmark | Habitat 2.0 [15] includes mobile manipulation tasks in which agents control a Fetch robot with a 7-DoF arm, mobile base [46], and suction gripper to rearrange objects in apartment scenes. | role, split, size and leakage | p. 21 (A.11 TriFinger Hardware Experiment Setup), p. 5 (Results), p. 5 (Results), p. 6 (Results) |
| Metric | Mean Success: the average success rate across all benchmarks. | definition, denominator, direction and uncertainty | p. 4 (Results), p. 8 (Results), p. 2 (Figure/Table caption) |
| Baseline/ablation | However, we find that several of these pre-trained models often outperform a random training from scratch baseline. | fair input/data/compute/action matching | p. 5 (Results), p. 8 (Figure/Table caption), p. 2 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 16 / A.1 Limitations - extractive body cue:** This study presents a thorough examination of visual foundation models but has several limitations.
- **p. 5 / Results - extractive body cue:** Additionally, we include randomly initialized ViTs with frozen- and finetuned weights to assess the necessity of pre-training and the limitations of pure in-domain learning.
- **p. 9 / Results - extractive body cue:** While this adaptation strategy cannot address task-specialization, it may serve to mitigate domain gap.
- **p. 9 / Results - extractive body cue:** In aggregate, these results suggests that MAE adaptation can be explored as a powerful alternative in few-shot domains or where E2E fine-tuning fails.
- **p. 5 / Results - extractive body cue:** Interestingly, while the model pre-trained on the largest dataset (CLIP) performs well on one benchmark (ObjectNav) it does not perform well across all tasks.
- **p. 6 / Results - extractive body cue:** While larger than Ego4D+M and Ego4D+N, it does not include any new types of data beyond the manipulation and navigation videos in the previous subsets.
- **p. 7 / Results - extractive body cue:** However, in Table 4, we find exceptions where this general trend does not hold.

## Why Read It

RL, IL, offline learning, and robot data의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Our findings reveal a challenge and opportunity for the community - the search for a PVR that is universally dominant (or "foundational") for EAI calls for innovations in architecture, learning paradigm, data ...를 문제로 두고, The visual cortex is a region of an organism's brain, which together with the motor cortex, enables sight to be converted into movement.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 16 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Our findings reveal a challenge and opportunity for the community - the search for a PVR that is universally dominant (or "foundational") for EAI calls for innovations in architecture, learning ... (p. 3, 1 Introduction).
- **Actual contribution:** The visual cortex is a region of an organism's brain, which together with the motor cortex, enables sight to be converted into movement. (p. 1, 1 Introduction).
- **Evaluation boundary:** Figure 4: Comparison of VC-1 with existing PVRs. VC-1 matches or exceeds existing PVRs on all benchmarks except R3M on AD, MW, and DMC, indicating an opportunity for model adaptation. ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** In aggregate, these results suggests that MAE adaptation can be explored as a powerful alternative in few-shot domains or where E2E fine-tuning fails. (p. 9, Results).
