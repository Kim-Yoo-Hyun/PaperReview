# G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Wenbo Hu, Jingli Lin, Yilin Long, Yunlong Ran, Lihan Jiang, Yifan Wang, Chenming Zhu, Runsen Xu, Tai Wang, Jiangmiao Pang
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: VLM, 3D reconstruction, spatial reasoning
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf) 기준이다.

## Why This Paper Is Here

G²VLM은 여러 영상의 3차원 기하를 복원하는 학습과 언어 기반 공간 추론을 하나의 시각언어모형에 결합한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language Models (VLMs) still lack robustness in spatial intelligence, demonstrating poor performance on spatial understanding and reasoning tasks.
- **p. 1 / Abstract - extractive body cue:** We attribute this gap to the absence of a visual geometry learning process capable of reconstructing 3D space from 2D images.
- **p. 1 / Abstract - extractive body cue:** We present G2VLM, a geometry grounded vision-language model that bridges two fundamental aspects of spatial intelligence: spatial 3D reconstruction and spatial understanding.
- **p. 1 / Abstract - extractive body cue:** G2VLM natively leverages learned 3D visual geometry features to directly predict 3D attributes and enhance spatial reasoning tasks via in-context learning and interleaved reasoning.
- **p. 1 / Abstract - extractive body cue:** Our unified design is highly scalable for spatial understanding: it trains on abundant multiview image and video data, while simultaneously leveraging the benefits of 3D ...
- **p. 2 / 1. Introduction - extractive body cue:** We argue that this limitation stems from how current VLMs acquire their physical world knowledge.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this limitation, we propose to integrate visual geometry learning into the VLM.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We introduce G2VLM, the first unified model that bridges spatial 3D reconstruction and high-level spatial understanding in ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this limitation, we propose to integrate visual geometry learning into the VLM.
- **p. 3 / 1. Introduction - extractive body cue:** We present G2VLM, a unified model that integrates both a geometric perception expert for 3D reconstruction and a semantic perception expert for multimodal understanding and ...
- **p. 4 / 3. Unified Spatial Vision-Language Model - extractive body cue:** We introduce G2VLM, a unified geometry-grounded VLM that integrates spatial 3D reconstruction and spatial understanding.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** Our model's input is a sequence (Ii)N i=1 of N RGB images Ii ∈R3×H×W , we present the detailed design for each expert as follows.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** As illustrated in Figure 3, G2VLM adopts a Mixture-ofTransformer-Experts (MoT) architecture [16] that consists of two transformer experts-one geometry perception expert dedicated to visual geometry ...
- **p. 5 / 3.3. Spatial Reasoning Learning - extractive body cue:** For joint-training, we use AdamW optimizer for 16K iterations with a lr of 2e-5 on 64 A800 GPUs over 3 days.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** For geometric perception expert, we incorporate a DINOV2 vision encoder to inject low-level visual information to LLM which further reasons the 3D-aware feature through global ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (1) where Ti ∈SE(3) ⊂R4×4 is the camera pose, Xi ∈ RH×W ×3 is the associated pixel-aligned 3D point map represented in its own camera coordinate system, each corresponding to the input ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.1. Model Architecture), p. 2 (1. Introduction) |
| State/latent | where, camera, pose, associated, pixel-aligned, point, represented, coordinate, system, corresponding, input, image | geometry, map, object/relationship state | p. 4 (3.1. Model Architecture), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | On visual geometry tasks, G2VLM achieves competitive results against state-of-theart (SOTA) feed-forward 3D reconstruction models, such as VGGT [52], across depth estimation, point estimation, and camera pose estimation tasks. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Model Architecture) |
| Objective/outcome | We explore three distinct joint-training strategies, where the semantic perception expert is, by default, optimized using a cross-entropy (CE) loss: • CE Loss Only: Freeze the geometric perception expert, only the semantic ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.2. Visual Geometry Learning), p. 5 (3.3. Spatial Reasoning Learning) |

## Main Claims and Actual Contribution

- 기하와 의미를 맡는 두 전문가를 연결하고 점 지도·상대 카메라 자세·표면 법선에 대한 감독을 적용한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf#page=5)
- 다중 시점 3차원 복원과 공간 질의응답을 각각 평가해 기하 표현이 두 종류의 과제에 기여하는지 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (4.1. Visual Geometry Results) |
| Embodiment/environment | Following the evaluation settings in [55, 62], we evaluate the quality of reconstructed multiview point maps on the 7-Scenes [45] and ETH3D [44] datasets. | hardware/simulator version and reset protocol | p. 6 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results) |
| Dataset/benchmark | G2VLM effectively reconstructs a diverse set of open-domain images, spanning object-level, structure-level, indoor, and outdoor scenes, including both dynamic and static content. | role, split, size and leakage | p. 6 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 7 (4.1. Visual Geometry Results), p. 7 (4.2. Spatial Understanding & Reasoning Results) |
| Metric | These results demonstrate that our method achieves on-par performance with VGGT in completion and comparable results in accuracy. | definition, denominator, direction and uncertainty | p. 7 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 7 (4.1. Visual Geometry Results) |
| Baseline/ablation | Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach over the baselines. Notably, it con- firms a ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 7 (4.1. Visual Geometry Results), p. 7 (4.2. Spatial Understanding & Reasoning Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** While our model exhibits strong generalization abilities in both visual geometry and spatial reasoning, one potential limitation is training instability with large-scale models.
- **p. 7 / 4.2. Spatial Understanding & Reasoning Results - extractive body cue:** We leave the scaling of our model to future work, as this is a promising direction to unlock even stronger performance.
- **p. 7 / 4.1. Visual Geometry Results - extractive body cue:** These results underscore our model's strong capabilities, particularly since it does not use camera tokens (like VGGT) which provides a strong camera pose prior or ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (1. Introduction), p. 4 (3.1. Model Architecture), p. 5 (3.3. Spatial Reasoning Learning)이다.
