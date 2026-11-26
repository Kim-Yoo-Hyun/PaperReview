# LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v267/mcvay25a.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/165205. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: Paul Mcvay, Sergio Arnaud, Ada Martin, Arjun Majumdar, Krishna Murthy Jatavallabhula, Phillip Thomas, Ruslan Partsey, Daniel Dugas, Abha Gejji, Alexander Sax, Vincent-Pierre Berges, Mikael Henaff, Ayush Jain, Ang Cao, Ishita Prasad, Mrinal Kalakrishnan, Michael Rabbat, Nicolas Ballas, Mido Assran, Oleksandr Maksymets, Aravind Rajeswaran, Franziska Meier
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: 3D Vision, self-supervised, 3D visual grounding
- Official paper: https://proceedings.mlr.press/v267/mcvay25a.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/main/assets/mcvay25a/mcvay25a.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

LOCATE 3D는 자연어로 설명한 물체를 카메라 자세가 알려진 RGB-D 영상열에서 찾아 3차원 마스크와 경계 상자로 출력한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/mcvay25a/mcvay25a.pdf#page=1)

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

- 2차원 기반 모델의 특징을 점군에 연결하고, 가려진 부분의 잠재 특징을 예측하는 3D-JEPA로 장면 인코더를 사전학습했다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/mcvay25a/mcvay25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/mcvay25a/mcvay25a.pdf#page=4)
- 여러 촬영 장치에서 얻은 3차원 지시 대상 주석을 구축하고, 언어 조건 복호기의 위치 추정과 다른 촬영 조건으로의 일반화를 평가했다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/mcvay25a/mcvay25a.pdf#page=5) · [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/mcvay25a/mcvay25a.pdf#page=6) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/mcvay25a/mcvay25a.pdf#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 3 (1. Introduction), p. 4 (1. Introduction), p. 2 (1. Introduction), p. 5 (2.3.2. TRAINING LOCATE 3D)이다.
