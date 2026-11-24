# Towards Learning to Complete Anything in Lidar

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v267/takmaz25a.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/167907. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: Ayça Takmaz, Cristiano Saltori, Neehar Peri, Tim Meinhardt, Riccardo de Lutio, Laura Leal-Taixé, Aljosa Osep
- 저자 판본: ICML 게재본에 인쇄된 다섯 번째 저자 Riccardo de Lutio의 성 표기를 반영했다. [표제면](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/takmaz25a/takmaz25a.pdf#page=1) · [학회 서지](https://proceedings.mlr.press/v267/takmaz25a.html)
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: sensor fusion, LiDAR, 3D Vision
- Official paper: https://proceedings.mlr.press/v267/takmaz25a.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/main/assets/takmaz25a/takmaz25a.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/takmaz25a/takmaz25a.pdf)

## Why This Paper Is Here

CAL은 여러 시점의 센서 관측에서 얻은 부분 형상과 의미 정보를 LiDAR만 사용하는 물체 완성 모델에 전달한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/takmaz25a/takmaz25a.pdf#page=1) · [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/takmaz25a/takmaz25a.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We propose CAL (Complete Anything in Lidar) for Lidar-based shape-completion in-the-wild.
- **p. 1 / Abstract - extractive body cue:** This is closely related to Lidar-based semantic/panoptic scene completion.
- **p. 1 / Abstract - extractive body cue:** However, contemporary methods can only complete and recognize objects from a closed vocabulary labeled in existing Lidar datasets.
- **p. 1 / Abstract - extractive body cue:** Different to that, our zero-shot approach leverages the temporal context from multi-modal sensor sequences to mine object shapes and semantic features of observed objects.
- **p. 1 / Abstract - extractive body cue:** These are then distilled into a Lidar-only instance-level completion and recognition model.
- **p. 1 / 1. Introduction - extractive body cue:** However, prior work can only localize and complete around 1
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we leverage image (Kirillov et al., 2023) and video (Ravi et al., 2024) segmentation foundation models to localize and track objects ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We propose the first method for Zero-Shot Lidar Panoptic Scene Completion.
- **p. 2 / 1. Introduction - extractive body cue:** 1, 2⃝) and demonstrate that our method can recognize and complete arbitrary objects not captured in canonical semantic vocabularies (Fig.
- **p. 4 / 3. Method - extractive body cue:** Our method takes a semantic vocabulary consisting of free-form semantic class descriptions only at test time.
- **p. 4 / 3.2. Learning To Complete Objects - extractive body cue:** The backbone consists of a sparse feature encoder (●) (Choy et al., 2019) followed by a dense 3D convolutional block (●).
- **p. 5 / 3.2. Learning To Complete Objects - extractive body cue:** We estimate scene-level occupancy using a multiscale sparse generative decoder that consists of decoder blocks D, two occupancy heads Bo and Bs, and a pseudo-semantic ...
- **p. 5 / 3.2. Learning To Complete Objects - extractive body cue:** The Transformer decoder then predicts segmentation masks over the completed scene and regresses CLIP features. tive decoder (●) uses three decoding blocks D1:L estimating occupancy ...
- **p. 5 / 3.2. Learning To Complete Objects - extractive body cue:** The transformer decoder produces instance masks and CLIP features, supervised by the mask-loss (Lmask: binary-cross entropy and Dice loss) and the feature distillation loss (LCLIP: ...
- **p. 4 / 3.2. Learning To Complete Objects - extractive body cue:** (2024) and employ a sparse-generative 3D U-Net (Dai et al., 2018) architecture that estimates scene-level occupancy, and a Transformer instance decoder (Cheng et al., 2022) ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | CAL takes a single input Lidar scan P, providing sparse and incomplete observations of scene geometry (Fig. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Learning To Complete Objects), p. 3 (3. Method) |
| State/latent | CAL, takes, single, input, Lidar, scan, providing, sparse, incomplete, observations, scene, geometry | geometry, map, object/relationship state | p. 4 (3.2. Learning To Complete Objects), p. 3 (3. Method), p. 5 (3.2. Learning To Complete Objects) |
| Output/action | Semantic Scene Completion (SSC) (Behley et al., 2019) assumes input in the form of a single Lidar point cloud P = {pn}N n=1, pn ∈R4, consisting of spatial positions and intensity channel. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Method), p. 5 (3.2. Learning To Complete Objects), p. 4 (3.1. Mining 3D Shape Priors From Unlabeled Data) |
| Objective/outcome | During each training iteration, the generative decoder produces coarse-to-fine voxel grids for each scale L, supervised with a binary occupancy loss (Locc: binary-cross entropy wrt. aggregated binary occupancy labels) and prototype clas ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.2. Learning To Complete Objects), p. 5 (3.2. Learning To Complete Objects) |

## Main Claims and Actual Contribution

- 주행 시퀀스에서 같은 물체의 관측을 모아 부분 완성 표적과 영상 기반 의미 특징을 만들고 인스턴스 단위로 증류한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/takmaz25a/takmaz25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/takmaz25a/takmaz25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/takmaz25a/takmaz25a.pdf#page=5)
- 학습한 표현을 의미·파놉틱 장면 완성, 가려진 부분까지 포함한 3차원 상자와 개방 어휘 물체 인식에 적용했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/takmaz25a/takmaz25a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/takmaz25a/takmaz25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/takmaz25a/takmaz25a.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.3. Pseudo-labeling engine analysis), p. 7 (4.2. Experimental results) |
| Embodiment/environment | We quantitatively assess CAL's zero-shot completion and recognition performance on Semantic Scene Completion (SSC) (Behley et al., 2019) and Panoptic Scene Completion (PSC) (Cao et al., 2024) benchmarks. | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | We evaluate our model's segmentation, completion, and recognition capabilities by specifying target classes (defined in each respective dataset) via prompts at test time (additional details in Appx. | role, split, size and leakage | p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Experimental results) |
| Metric | Table 15. Per-class performance analysis for Panoptic Scene Completion, evaluated on SemanticKITTI (Behley et al., 2019) dataset. Per-class scores for the baselines and class-frequencies are taken from (Cao et al., 2024). | definition, denominator, direction and uncertainty | p. 23 (Figure/Table caption), p. 6 (4.1. Experimental Setup), p. 7 (4.1. Experimental Setup) |
| Baseline/ablation | As there are no prior works tackling Lidar PSC in zero-shot setting, we construct two baselines adhering to the following criteria for a fair zero-shot comparison: (1) input should be a single ... | fair input/data/compute/action matching | p. 7 (4.2. Experimental results), p. 7 (4.2. Experimental results), p. 6 (4.1. Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5. Conclusion - extractive body cue:** We believe these are promising directions for future work.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 7. Number of CLIP prototypes. We evaluate SSC/PSC performance on SemanticKITTI when varying the number of CLIP prototypes C. We observe similar performance with ...
- **p. 7 / 4.2. Experimental results - extractive body cue:** We employ the LODE variant that does not use any semantic labels.
- **p. 7 / 4.2. Experimental results - extractive body cue:** Fully supervised baselines have a clear advantage over CAL as they train on closed-set, noise-free annotations with full scene coverage.
- **p. 8 / 4.3. Pseudo-labeling engine analysis - extractive body cue:** We observe no significant improvements between w = {1, 2} and a degradation in performance when increasing to w = 4 (10.97 PQ†) due to ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.2. Learning To Complete Objects), p. 4 (3.2. Learning To Complete Objects)이다.
