# DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=8oFvUBvF1u.
> PDF retrieval source: https://openreview.net/pdf/be9894ba90b07c5ec0bd2deda17f1b1b8eeab2aa.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, 3D Vision, semantic
- Official paper: https://openreview.net/forum?id=8oFvUBvF1u
- Full-text retrieval: https://openreview.net/pdf/be9894ba90b07c5ec0bd2deda17f1b1b8eeab2aa.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 vla 문제를 이해하기 위해 읽는다. 본문은 In summary, we make the following contributions: (i) a novel 3d matching dataset that remedies the lack of texture information and categories in previous datasets, (ii) a 3D dense correspondence model framework ...를 문제로 두고, In summary, we make the following contributions: (i) a novel 3d matching dataset that remedies the lack of texture information and categories in previous datasets, (ii) a 3D dense correspondence model framework ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Dense 3D correspondence can enhance robotic manipulation by enabling the generalization of spatial, functional, and dynamic information from one object to an unseen counterpart.
- **p. 1 / ABSTRACT - extractive body cue:** Compared to shape correspondence, semantic correspondence is more effective in generalizing across different object categories.
- **p. 1 / ABSTRACT - extractive body cue:** To this end, we present DenseMatcher, a method capable of computing 3D correspondences between in-the-wild objects that share similar structures.
- **p. 1 / ABSTRACT - extractive body cue:** DenseMatcher first computes vertex features by projecting multiview 2D features onto meshes and refining them with a 3D network, and subsequently finds dense correspondences with ...
- **p. 1 / ABSTRACT - extractive body cue:** In addition, we craft the first 3D matching dataset that contains colored object meshes across diverse categories.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, we make the following contributions: (i) a novel 3d matching dataset that remedies the lack of texture information and categories in previous datasets, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As a result, prior methods generating dense 3D features can be divided into two categories: (1) 3D networks that only utilize geometry information and are ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, we make the following contributions: (i) a novel 3d matching dataset that remedies the lack of texture information and categories in previous datasets, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our method achieves 43.5% improvement over previous shape-matching baselines.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our method addresses this by adding a 3D neural network, DiffusionNet (Sharp et al., 2022), to refine 2D features with 3D geometry, producing spatially consistent ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** 4.3 LOSS FUNCTION Our loss function consists of two components: L = Lsemantic + Lpreservation.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** By establishing correspondences, we can enable the robot to identify semantically similar components between two objects, which is cru- ∗Equal contribution,†Corresponding author.
- **p. 18 / A.3.2 TRAINING DENSEMATCHER - extractive body cue:** Our FeatUp module upsamples 16x16 features to 512x512 resolution.
- **p. 18 / A.3.2 TRAINING DENSEMATCHER - extractive body cue:** Thanks to our 3D network, we found that using only 3 lateral views plus 1 top and 1 bottom view during both training and inferencing ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Preprint SD& DINO • • • • • • • Renders Low-res Features SD& DINO SD& DINO High-res Features Remesh Project & Average DiffusionNet Functional Map Frozen FeatUp Render Sinusoidal Encoding Trainable ... | image/video, language instruction, proprioception과 history | p. 5 (1 INTRODUCTION), p. 19 (A.4.1 PRELIMINARY) |
| State/latent | Preprint, DINO, Renders, Low-res, Features, High-res, Remesh, Project, Average, DiffusionNet, Functional, Map | language-grounded task state와 action-policy context | p. 5 (1 INTRODUCTION), p. 19 (A.4.1 PRELIMINARY), p. 3 (1 INTRODUCTION) |
| Output/action | y \rangle = x^T A y = \sum _i A_{ii} x_i y_i. \label {eq:innerprod} (2) Given the area matrix and the contingent weight matrix of the mesh W ∈Rn×n (Meyer et al., ... | continuous action, pose 또는 action chunk | p. 19 (A.4.1 PRELIMINARY), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | We freeze the 2D backbone models during training, and optimize a 4-block DiffusionNet with 512 channels on DenseCorr3Dfor 6000 steps with a batch size of 8 using Adam Kingma & Ba (2014). | instruction following, task success, generalization과 latency | p. 18 (A.3.2 TRAINING DENSEMATCHER) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, we make the following contributions: (i) a novel 3d matching dataset that remedies the lack of texture information and categories in previous datasets, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our method achieves 43.5% improvement over previous shape-matching baselines.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our method addresses this by adding a 3D neural network, DiffusionNet (Sharp et al., 2022), to refine 2D features with 3D geometry, producing spatially consistent ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** 4.3 LOSS FUNCTION Our loss function consists of two components: L = Lsemantic + Lpreservation.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** By establishing correspondences, we can enable the robot to identify semantically similar components between two objects, which is cru- ∗Equal contribution,†Corresponding author.
- **p. 10 / 6.1.2 RESULTS - extractive body cue:** As can be seen, the mapping obtained with our method significantly outperforms baselines in terms of accuracy and continuity.
- **p. 7 / 6.1.2 RESULTS - extractive body cue:** Additionally, due to the generalization capability of pre-trained 2D backbones, we achieve much higher accuracy on out-of-distribution test categories listed in Tab.
- **p. 9 / 6.1.2 RESULTS - extractive body cue:** For each task, we measure the task success rates over five trials.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 10 (6.1.2 RESULTS), p. 7 (6.1.2 RESULTS) |
| Embodiment/environment | 6.2 ZERO-SHOT REAL WORLD ROBOTIC MANIPULATION We create six real-world manipulation environments, exploring the performance of DenseMatcher on daily life tasks by comparing the shape, size, material and category of the manipulated ... | hardware/simulator version and reset protocol | p. 7 (6.1.2 RESULTS), p. 8 (6.1.2 RESULTS) |
| Dataset/benchmark | We use a RealSense L515 RGB-D camera and a UR5 robot arm to conduct all the real-world experiments. | role, split, size and leakage | p. 7 (6.1.2 RESULTS), p. 8 (6.1.2 RESULTS), p. 8 (6.1.2 RESULTS), p. 7 (6 EXPERIMENTS) |
| Metric | For each task, we measure the task success rates over five trials. | definition, denominator, direction and uncertainty | p. 9 (6.1.2 RESULTS), p. 9 (6.1.2 RESULTS), p. 7 (6.1.2 RESULTS) |
| Baseline/ablation | 1, we found that our model achieves better AUC and Err compared to the baseline model. | fair input/data/compute/action matching | p. 7 (6.1.2 RESULTS), p. 10 (6.1.2 RESULTS), p. 7 (6 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 6.1.2 RESULTS - extractive body cue:** Additionally, due to the generalization capability of pre-trained 2D backbones, we achieve much higher accuracy on out-of-distribution test categories listed in Tab.
- **p. 7 / 6 EXPERIMENTS - extractive body cue:** ConsistFMap (Cao & Bernard, 2022) utilizes cycle-consistency for robust multi-shape matching across shape collections, making it a strong baseline in unsupervised shape matching.
- **p. 8 / 6.1.2 RESULTS - extractive body cue:** To avoid occlusion, we track the object and trace the contact points back to the first frame, thereby obtaining the template keypoint on the template ...
- **p. 18 / A.3.2 TRAINING DENSEMATCHER - extractive body cue:** In order to make our model robust to the number of vertices, we randomly set the re-meshing target to between 500 and 2500 vertices during ...
- **p. 21 / A.5 PERFORMANCE UNDER OCCLUSION - extractive body cue:** We study the performance of our model under occlusion in two cases.
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 11: Robot experiments visualization under occlusion conditions. A.5.2 PARTIAL SOURCE AND FULL TARGET In the second case, the source mesh is a partial mesh, ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 vla 문제를 이해하기 위해 읽는다. 본문은 In summary, we make the following contributions: (i) a novel 3d matching dataset that remedies the lack of texture information and categories in previous datasets, (ii) a 3D dense correspondence model framework ...를 문제로 두고, In summary, we make the following contributions: (i) a novel 3d matching dataset that remedies the lack of texture information and categories in previous datasets, (ii) a 3D dense correspondence model framework ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 18 (A.3.2 TRAINING DENSEMATCHER) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
