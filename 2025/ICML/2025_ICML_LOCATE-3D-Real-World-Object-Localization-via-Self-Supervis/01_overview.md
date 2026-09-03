# LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=FKi6yjXwCN.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/165205. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: 3D Vision, Reinforcement Learning
- Official paper: https://openreview.net/forum?id=FKi6yjXwCN
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/165205
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 They often require human annotation at inference time in the form of detailed 3D meshes or object instance segmentation, making them difficult to deploy on real-world devices.를 문제로 두고, Specifically, each decoder module consists of three attention blocks: (1) a self-attention block that enables queries to refine their representations through mutual interaction, (2) a cross-attention block where queries extract relevant ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present LOCATE 3D, a model for localizing objects in 3D scenes from referring expressions like "the small coffee table between the sofa and the ...
- **p. 1 / Abstract - extractive body cue:** Notably, LOCATE 3D operates directly on sensor observation streams (posed RGB-D frames), enabling real-world deployment on robots and AR devices.
- **p. 1 / Abstract - extractive body cue:** Key to our approach is 3D-JEPA, a novel self-supervised learning (SSL) algorithm applicable to sensor point clouds.
- **p. 1 / Abstract - extractive body cue:** It takes as input a 3D pointcloud featurized using 2D foundation models (CLIP, DINO).
- **p. 1 / Abstract - extractive body cue:** Subsequently, masked prediction in latent space is employed as a pretext task to aid the self-supervised learning of contextualized pointcloud features.
- **p. 1 / 1. Introduction - extractive body cue:** They often require human annotation at inference time in the form of detailed 3D meshes or object instance segmentation, making them difficult to deploy on ...
- **p. 3 / 1. Introduction - extractive body cue:** We found directly reconstructing such fine-grained and high-dimensional features to be difficult.

## Core Idea

- **p. 4 / 2.3.1. LANGUAGE-CONDITIONED 3D DECODER - extractive body cue:** Specifically, each decoder module consists of three attention blocks: (1) a self-attention block that enables queries to refine their representations through mutual interaction, (2) a ...
- **p. 5 / 2.3.1. LANGUAGE-CONDITIONED 3D DECODER - extractive body cue:** Our decoder consists of three parallel prediction heads (Figure 7) that process the refined learned queries Q independently as object proposals.
- **p. 1 / 1. Introduction - extractive body cue:** We outline our contributions in this work below.
- **p. 5 / 2.3.1. LANGUAGE-CONDITIONED 3D DECODER - extractive body cue:** For bounding boxes, we developed a novel architecture (Figure 7).
- **p. 2 / 1. Introduction - extractive body cue:** We show that the resulting 3D-JEPA features are contextualized for the scene, while the features lifted from 2D foundation models only provide local understanding.
- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive body cue:** In order to not destroy the pretrained features we use a stage-wise learning rate scheduler (Kumar et al., 2022); specifically we start by training the ...
- **p. 5 / 2.3.2. TRAINING LOCATE 3D - extractive body cue:** We apply progressively weighted deep supervision at every decoder layer and maintain an Exponential Moving Average (EMA) of the model weights to use for evaluation ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Preprocessing: Lifting 2D Foundation Model Features into 3D Point Clouds We begin by preprocessing the inputs (posed RGB-D images) by constructing a 3D pointcloud to encode geometry, and featurizing the pointcloud with ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | Preprocessing, Lifting, Foundation, Model, Features, Point, Clouds, begin, inputs, posed, RGB-D, images | geometry, map, object/relationship state | p. 3 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | In the first preprocessing phase, we leverage the underlying sensor observation stream to lift features from 2D foundation models (Radford et al., 2021; Oquab et al., 2023) into 3D point clouds (Jatavallabhula ... | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Objective/outcome | Specifically, LOCATE 3D optimizes a composite loss function, which includes: (1) a mask loss, combining Dice and cross-entropy loss terms (Cheng et al., 2021); (2) a bounding box loss, composed of L1 ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (2.3.2. TRAINING LOCATE 3D), p. 5 (2.3.2. TRAINING LOCATE 3D) |

## Main Claims and Actual Contribution

- **p. 4 / 2.3.1. LANGUAGE-CONDITIONED 3D DECODER - extractive body cue:** Specifically, each decoder module consists of three attention blocks: (1) a self-attention block that enables queries to refine their representations through mutual interaction, (2) a ...
- **p. 5 / 2.3.1. LANGUAGE-CONDITIONED 3D DECODER - extractive body cue:** Our decoder consists of three parallel prediction heads (Figure 7) that process the refined learned queries Q independently as object proposals.
- **p. 1 / 1. Introduction - extractive body cue:** We outline our contributions in this work below.
- **p. 5 / 2.3.1. LANGUAGE-CONDITIONED 3D DECODER - extractive body cue:** For bounding boxes, we developed a novel architecture (Figure 7).
- **p. 2 / 1. Introduction - extractive body cue:** We show that the resulting 3D-JEPA features are contextualized for the scene, while the features lifted from 2D foundation models only provide local understanding.
- **p. 8 / 4.4. Evaluating LOCATE 3D in novel environments - extractive body cue:** Our results show that LOCATE 3D achieved a success rate of 8/10 trials, outperforming baselines with a maximum success rate of 5.66/10 (see details in ...
- **p. 8 / 4.4. Evaluating LOCATE 3D in novel environments - extractive body cue:** First, replacing raw RGB inputs with lifted foundation features (CF) significantly improves crossdataset performance across all benchmarks (SN++: 37.5% →51.5%, ARKitScenes: 11.3% →41.7%, FRE: 39.9% ...
- **p. 20 / Figure/Table caption - extractive body cue:** Table 7: Impact of LX3D train data. We report accuracy @25 IoU. ARKitScenes column contains both pretrain and val split as we saw no significant ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |
| Embodiment/environment | First, replacing raw RGB inputs with lifted foundation features (CF) significantly improves crossdataset performance across all benchmarks (SN++: 37.5% →51.5%, ARKitScenes: 11.3% →41.7%, FRE: 39.9% →54.1%). | hardware/simulator version and reset protocol | p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments) |
| Dataset/benchmark | We evaluate on the validation split of the benchmarks and report top-1 accuracy without assuming ground-truth object proposals. | role, split, size and leakage | p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 6 (4. Experiments and Analysis), p. 5 (3. LOCATE 3D DATASET Overview) |
| Metric | Table 7: Impact of LX3D train data. We report accuracy @25 IoU. ARKitScenes column contains both pretrain and val split as we saw no significant difference when split up. Adding LX3D training ... | definition, denominator, direction and uncertainty | p. 20 (Figure/Table caption), p. 7 (Figure/Table caption), p. 20 (Figure/Table caption) |
| Baseline/ablation | Notably, LOCATE 3D outperforms both baselines across most metrics, showcasing the robustness of our approach. | fair input/data/compute/action matching | p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 8 (4.4. Evaluating LOCATE 3D in novel environments), p. 6 (4.1. How does LOCATE 3D compare to prior methods) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.5. Computational Analysis - extractive body cue:** Limitations We can utilize such caching because our benchmarks operate under static (ScanNet) or quasi-static (robot) environments.
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 8: Learning rate schedule for encoder and decoder. Fine-tuning a pre-trained encoder alongside a randomly initialized decoder requires careful balancing to prevent unstable gradients ...
- **p. 6 / 4. Experiments and Analysis - extractive body cue:** This choice better represents realworld deployment scenarios though it typically results in performance degradation due to sensor noise, missing regions, and registration errors, as discussed ...
- **p. 8 / 4.4. Evaluating LOCATE 3D in novel environments - extractive body cue:** As outlined earlier, our model is capable of working with sensor streams and does not require human intervention at test time (e.g., for mesh refinement ...
- **p. 24 / Figure/Table caption - extractive body cue:** Table 10: Impact of scene diversity. We train all models on SR3D+NR3D+ScanRefer and add 30K samples from L3DD. We ablate whether these extra samples come ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 12: Examples of the Spot robot at the end of navigation task before the pick task (right) the output bounding boxes of LOCATE 3D+ ...

## Why Read It

RL, IL, offline learning, and robot data의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 They often require human annotation at inference time in the form of detailed 3D meshes or object instance segmentation, making them difficult to deploy on real-world devices.를 문제로 두고, Specifically, each decoder module consists of three attention blocks: (1) a self-attention block that enables queries to refine their representations through mutual interaction, (2) a cross-attention block where queries extract relevant ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 3 (1. Introduction), p. 4 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (2.3.2. TRAINING LOCATE 3D) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
