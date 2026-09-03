# SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, Vision-Language, semantic
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This highlights a key limitation: the absence of a robust model for processing 3D data end-to-end for semantic learning, along with the lack of sufficient data for training such a model.를 문제로 두고, Our contributions can be summarized as follows: • We present SceneSplat-7K, a high-quality large-scale Gaussian splats dataset spanning 7K indoor scenes, which boosts 3DGS scene understanding research. • We propose SceneSplat, a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recognizing arbitrary or previously unseen categories is essential for comprehensive real-world 3D scene understanding.
- **p. 1 / Abstract - extractive body cue:** Currently, all existing methods rely on 2D or textual modalities during training or together at inference.
- **p. 1 / Abstract - extractive body cue:** This highlights the clear absence of a model capable of processing 3D data alone for learning semantics end-to-end, along with the necessary data to train ...
- **p. 1 / Abstract - extractive body cue:** Meanwhile, 3D Gaussian Splatting (3DGS) has emerged as the de facto standard for 3D scene representation across various vision tasks.
- **p. 1 / Abstract - extractive body cue:** However, effectively integrating semantic reasoning into 3DGS in a generalizable manner remains an open challenge.
- **p. 2 / 1. Introduction - extractive body cue:** This highlights a key limitation: the absence of a robust model for processing 3D data end-to-end for semantic learning, along with the lack of sufficient ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this gap, current methods resort to multi-modality fusion, distilling knowledge from 2D vision-language models into 3D data.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We present SceneSplat-7K, a high-quality large-scale Gaussian splats dataset spanning 7K indoor scenes, which boosts 3DGS scene ...
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we propose GaussSSL, a self-supervised learning scheme that unlocks rich 3D feature learning from unlabeled scenes.
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** We propose to mitigate the decoder collapse issues by multitask reconstruction LMGM, as coding rate regularization stabilizes only the hierarchical encoder.
- **p. 4 / 4. Methodology - extractive body cue:** Building upon the SceneSplat-7K dataset, we carry out both vision-language 3DGS pretraining, which enables openvocabulary scene understanding, and self-supervised pretraining, which regularizes the latent space ...
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** 4.2, the precomputed language feature enables effective knowledge distillation.
- **p. 4 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** We first adapt the transformer encoder-decoder backbone from [51] to efficiently predict high-dimensional perprimitive features corresponding to collected 3DGS language labels.
- **p. 5 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** To enforce feature similarity in Euclidean space, we use L2 loss: \ m ath c al {L }_{ 2 } = \ frac {1}{/\mathcal {V}/} ...
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** For a batch of Gaussian scenes {Gn}B n=1 (global/local views Gb g, Gb l), we extract tokenized bottleneck features z ∈RM×de, compute global representations ¯z ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (5) The output tokens ˆ Tm are mapped to the input Gaussian space with the reconstruction projector ˆGm = Φ( ˆTm) ∈RN′×F . | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (4.3. Self Supervised Pretraining), p. 2 (1. Introduction) |
| State/latent | output, tokens, mapped, input, Gaussian, space, reconstruction, projector, SceneSplat, introduces, DGS, encoder | geometry, map, object/relationship state | p. 5 (4.3. Self Supervised Pretraining), p. 2 (1. Introduction), p. 4 (4.2. Vision-Language 3DGS Pretraining) |
| Output/action | SceneSplat introduces a 3DGS encoder that takes as input the parameters of a Gaussian-splat scene (center, scale, color, opacity) and outputs semantic features in a per-primitive manner, in a single forward pass. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 5 (4.2. Vision-Language 3DGS Pretraining) |
| Objective/outcome | The cosine similarity loss minimizes the angular difference be4964 | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 5 (4.3. Self Supervised Pretraining), p. 5 (4.2. Vision-Language 3DGS Pretraining) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We present SceneSplat-7K, a high-quality large-scale Gaussian splats dataset spanning 7K indoor scenes, which boosts 3DGS scene ...
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we propose GaussSSL, a self-supervised learning scheme that unlocks rich 3D feature learning from unlabeled scenes.
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** We propose to mitigate the decoder collapse issues by multitask reconstruction LMGM, as coding rate regularization stabilizes only the hierarchical encoder.
- **p. 4 / 4. Methodology - extractive body cue:** Building upon the SceneSplat-7K dataset, we carry out both vision-language 3DGS pretraining, which enables openvocabulary scene understanding, and self-supervised pretraining, which regularizes the latent space ...
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** 4.2, the precomputed language feature enables effective knowledge distillation.
- **p. 6 / 5.2. Label-free 3DGS Pretraining - extractive body cue:** Our method achieves a +0.1% improvement over supervised-only baselines on ScanNet20 and +0.5% on ScanNet200, while observing a performance drop on ScanNet++ primarily due to ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Zero-Shot 3D Semantic Segmentation on the Fine-Grained ScanNet++ (100 classes) [57], Matterport3D (160 classes) [2] and ScanNet200 (200 classes) [5] Benchmarks. We report ...
- **p. 6 / 5.1. Vision-Language Pretraining - extractive body cue:** Notably, [21] uses 8.32× training scenes to achieve its best results, Zero-Shot Prediction Ground Truth Figure 3.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (5.2. Label-free 3DGS Pretraining), p. 7 (Figure/Table caption) |
| Embodiment/environment | The dataset contains about seven thousand scenes, including both real-world and synthetic environments. | hardware/simulator version and reset protocol | p. 3 (3. SceneSplat Dataset), p. 8 (5.3. Further Statistical Evaluation) |
| Dataset/benchmark | We introduce SceneSplat-7K - a carefully curated dataset of 3D Gaussian Splats representing indoor scenes. | role, split, size and leakage | p. 3 (3. SceneSplat Dataset), p. 8 (5.3. Further Statistical Evaluation), p. 3 (3. SceneSplat Dataset), p. 4 (3.2. Data Statistic) |
| Metric | Table 2. Zero-Shot 3D Semantic Segmentation on the Fine-Grained ScanNet++ (100 classes) [57], Matterport3D (160 classes) [2] and ScanNet200 (200 classes) [5] Benchmarks. We report the foreground mean IoU (f-mIoU) and foreground ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 8 (5.3. Further Statistical Evaluation), p. 8 (5.3. Further Statistical Evaluation) |
| Baseline/ablation | Table 4. Supervised Semantic Segmentation Experiments. We report our best results from Tab. 3 comparing against the state-of- the-art Point Transformer method. (Tab. 1). Furthermore, compared with our reproduced im- plementation of ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (5.2. Label-free 3DGS Pretraining) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5.3. Further Statistical Evaluation - extractive body cue:** Low PSNRs usually come out of blurry input images, poor Gaussian centers optimization, and insufficient scene coverage, where the 3DGS parameters cannot resolve the scene ...
- **p. 7 / 5.3. Further Statistical Evaluation - extractive body cue:** Although the collected labels are not perfect, large-scale pretraining can filter noise and learn meaningful patterns.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This highlights a key limitation: the absence of a robust model for processing 3D data end-to-end for semantic learning, along with the lack of sufficient data for training such a model.를 문제로 두고, Our contributions can be summarized as follows: • We present SceneSplat-7K, a high-quality large-scale Gaussian splats dataset spanning 7K indoor scenes, which boosts 3DGS scene understanding research. • We propose SceneSplat, a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 5 (4.2. Vision-Language 3DGS Pretraining), p. 6 (4.3. Self Supervised Pretraining) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
