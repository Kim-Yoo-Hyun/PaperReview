# SPA: 3D Spatial-Awareness Enables Effective Embodied Representation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=6TLdqAZgzn.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114708. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, 3D Vision
- Official paper: https://openreview.net/forum?id=6TLdqAZgzn
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114708
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This limitation arises from their primary emphasis on 2D semantic understanding, which, though valuable, is still insufficient for the sophisticated spatial reasoning required in embodied AI tasks, where agents need to navigate ...를 문제로 두고, Our contribution can be summarized as follows. • We propose a significant spatial hypothesis: 3D spatial awareness is crucial for embodied representation learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we introduce SPA, a novel representation learning framework that emphasizes the importance of 3D spatial awareness in embodied AI.
- **p. 1 / ABSTRACT - extractive body cue:** Our approach leverages differentiable neural rendering on multi-view images to endow a vanilla Vision Transformer (ViT) with intrinsic spatial understanding.
- **p. 1 / ABSTRACT - extractive body cue:** We present the most comprehensive evaluation of embodied representation learning to date, covering 268 tasks across 8 simulators with diverse policies in both single-task and ...
- **p. 1 / ABSTRACT - extractive body cue:** The results are compelling: SPA consistently outperforms more than 10 state-of-the-art representation methods, including those specifically designed for embodied AI, vision-centric tasks, and multi-modal applications, ...
- **p. 1 / ABSTRACT - extractive body cue:** Furthermore, we conduct a series of real-world experiments to confirm its effectiveness in practical scenarios.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This limitation arises from their primary emphasis on 2D semantic understanding, which, though valuable, is still insufficient for the sophisticated spatial reasoning required in embodied ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Existing visual representation learning methods for embodied AI (Nair et al., 2022; Radosavovic et al., 2023; Majumdar et al., 2023; Karamcheti et al., 2023; Shang ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contribution can be summarized as follows. • We propose a significant spatial hypothesis: 3D spatial awareness is crucial for embodied representation learning.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our experiments provide clear evidence for the hypothesis. • We introduce SPA, a novel paradigm for representation learning in embodied AI.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce SPA, a general 3D spatial-aware representation learning framework for embodied AI.
- **p. 3 / 2 METHODOLOGY - extractive body cue:** Unlike the bird's-eye view (BEV) construction in autonomous driving (Li et al., 2022), which usually relies on a fixed scene range around ego vehicle , ...
- **p. 4 / 2 METHODOLOGY - extractive body cue:** Our framework has the capability to distill knowledge from multiple vision foundation models by adding multiple rendering heads.
- **p. 3 / 2 METHODOLOGY - extractive body cue:** Finally, we explain the image rendering from the feature volume and loss functions for network optimization in Sec.
- **p. 3 / 2 METHODOLOGY - extractive body cue:** We then unpatchify them to obtain a latent feature map of size H P × W P , where P is the ViT patch size.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive body cue:** Given an image pair from different viewpoints, we first extract features from each image using a frozen, pre-trained Vision Transformer (ViT) encoder.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In this section, we first describe our process for handling multi-view image inputs and feature extraction in Sec. | image/video, language instruction, proprioception과 history | p. 3 (2 METHODOLOGY), p. 3 (2 METHODOLOGY) |
| State/latent | section, first, describe, process, handling, multi-view, image, inputs, feature, extraction, Sec, INPUT | language-grounded task state와 action-policy context | p. 3 (2 METHODOLOGY), p. 3 (2 METHODOLOGY), p. 1 (1 INTRODUCTION) |
| Output/action | 2.1 INPUT PROCESS AND FEATURE EXTRACTION Given a set of multi-view images I = {I1, I2, . . . , IN}, where each Ii ∈R3×H×W and N ∈Z+, we utilize a 2D ... | continuous action, pose 또는 action chunk | p. 3 (2 METHODOLOGY), p. 1 (1 INTRODUCTION), p. 23 (C.2 PRE-TRAINING DETAILS) |
| Objective/outcome | Finally, we explain the image rendering from the feature volume and loss functions for network optimization in Sec. | instruction following, task success, generalization과 latency | p. 3 (2 METHODOLOGY), p. 4 (2 METHODOLOGY), p. 22 (C.2 PRE-TRAINING DETAILS) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contribution can be summarized as follows. • We propose a significant spatial hypothesis: 3D spatial awareness is crucial for embodied representation learning.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our experiments provide clear evidence for the hypothesis. • We introduce SPA, a novel paradigm for representation learning in embodied AI.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce SPA, a general 3D spatial-aware representation learning framework for embodied AI.
- **p. 3 / 2 METHODOLOGY - extractive body cue:** Unlike the bird's-eye view (BEV) construction in autonomous driving (Li et al., 2022), which usually relies on a fixed scene range around ego vehicle , ...
- **p. 4 / 2 METHODOLOGY - extractive body cue:** Our framework has the capability to distill knowledge from multiple vision foundation models by adding multiple rendering heads.
- **p. 7 / Figure/Table caption - extractive body cue:** Tab. 3. For detailed results on each task and each random seed, please refer to Appendix D. We also have visualized the performance radar chart ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Correlation between mean success rate and camera pose regression error. 5.2 ADDITIONAL COMPARISONS (Q1) We primarily compare with SOTA methods using the ViT-L ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Influence of different datasets. We present the performance results on the VC-1 benchmark. Mean S.R. refers to the mean success rate across all ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | (14) F REAL-WORLD EXPERIMENT DETAILS Our real-world hardware setup is based on the open-source Low-Cost-Robot project (Koch, 2024). | hardware/simulator version and reset protocol | p. 23 (C.2 PRE-TRAINING DETAILS), p. 23 (C.2 PRE-TRAINING DETAILS) |
| Dataset/benchmark | Each epoch includes 5 times the dataset size. | role, split, size and leakage | p. 23 (C.2 PRE-TRAINING DETAILS), p. 23 (C.2 PRE-TRAINING DETAILS), p. 21 (C.1 DATASET DETAILS), p. 21 (C.1 DATASET DETAILS) |
| Metric | Meta-World RL Task Method (ViT-B) Success Rate Episode Reward button-press-topdown-v2 CLIP 0.93 653.97 DINOv2 1.00 746.04 MAE 0.46 517.54 MoCoV3 0.99 749.93 SPA (Ours) 1.00 778.47 hammer-v2 CLIP 0.00 401.41 DINOv2 0.67 ... | definition, denominator, direction and uncertainty | p. 24 (C.2 PRE-TRAINING DETAILS), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Baseline/ablation | Figure 4: Correlation between mean success rate and camera pose regression error. 5.2 ADDITIONAL COMPARISONS (Q1) We primarily compare with SOTA methods using the ViT-L backbone, which is commonly available and pre-trained ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 5 (Figure/Table caption), p. 23 (C.2 PRE-TRAINING DETAILS) |

## Explicit Limitations and Failure Boundary

- **p. 22 / C.1 DATASET DETAILS - extractive body cue:** Since Droid does not provide depth data, we utilize Croco-Stereo Weinzaepfel et al.
- **p. 22 / C.2 PRE-TRAINING DETAILS - extractive body cue:** This initialization does not affect the validity of our conclusions, as demonstrated by the ablation study of SPA-MAE in Sec.
- **p. 24 / C.2 PRE-TRAINING DETAILS - extractive body cue:** Simple multiview attention-based interaction, as used in MV-MAE, does not perform as effectively in learning 3D spatial awareness.
- **p. 7 / Figure/Table caption - extractive body cue:** Tab. 3. For detailed results on each task and each random seed, please refer to Appendix D. We also have visualized the performance radar chart ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This limitation arises from their primary emphasis on 2D semantic understanding, which, though valuable, is still insufficient for the sophisticated spatial reasoning required in embodied AI tasks, where agents need to navigate ...를 문제로 두고, Our contribution can be summarized as follows. • We propose a significant spatial hypothesis: 3D spatial awareness is crucial for embodied representation learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (2 METHODOLOGY), p. 3 (2 METHODOLOGY), p. 22 (C.2 PRE-TRAINING DETAILS), p. 4 (2 METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
