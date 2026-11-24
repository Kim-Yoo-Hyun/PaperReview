# TokenSplat: Token-aligned 3D Gaussian Splatting for Feed-forward Pose-free Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Yihui Li, Chengxin Lv, Zichen Tang, Hongyu Yang, Di Huang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf)

## Why This Paper Is Here

TokenSplat은 카메라 자세가 주어지지 않은 영상에서 공통 좌표계의 3D 가우시안과 카메라 자세를 한 번의 순전파로 추정한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present TokenSplat, a feed-forward framework for joint 3D Gaussian reconstruction and camera pose estimation from unposed multi-view images.
- **p. 1 / Abstract - extractive body cue:** At its core, TokenSplat introduces a Token-aligned Gaussian Prediction module that aligns semantically corresponding information across views directly in the feature space.
- **p. 1 / Abstract - extractive body cue:** Guided by coarse token positions and fusion confidence, it aggregates multiscale contextual features to enable long-range cross-view reasoning and reduce redundancy from overlapping Gaussians.
- **p. 1 / Abstract - extractive body cue:** To further enhance pose robustness and disentangle viewpoint cues from scene semantics, TokenSplat employs learnable camera tokens and an Asymmetric Dual-Flow Decoder (ADF-Decoder) that enforces ...
- **p. 1 / Abstract - extractive body cue:** This maintains clean factorization within a feed-forward architecture, enabling coherent reconstruction and stable pose estimation without iterative refinement.
- **p. 1 / 1. Introduction - extractive body cue:** However, these approaches typically entangle scene content and viewpoint cues in the same feature embeddings, making it difficult to disentangle camera parameters from scene content ...
- **p. 1 / 1. Introduction - extractive body cue:** Despite this progress, most existing 3DGS-based reconstruction pipelines [3, 6, 21, 22, 25, 26, 45] rely on per-scene optimization, which restricts their *Corresponding author scalability ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • We propose TokenSplat, a feed-forward pose-free reconstruction framework that jointly estimates camera poses and 3D Gaussian ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose TokenSplat, a feed-forward 3D Gaussian splatting framework that reconstructs 3D scenes from an arbitrary number of unposed images while ...
- **p. 2 / 1. Introduction - extractive body cue:** To jointly optimize 3D reconstruction and camera pose estimation within a feed-forward architecture, we introduce learnable camera tokens and an Asymmetric DualFlow Decoder (ADF-Decoder) that ...
- **p. 3 / 3.2. Architecture - extractive body cue:** 1, our method is a Transformer-based architecture for feed-forward 3D reconstruction from unposed images.
- **p. 4 / 3.3. Asymmetric Dual-Flow Decoder - extractive body cue:** The ADF-Decoder consists of 12 decoder blocks.
- **p. 3 / 3.2. Architecture - extractive body cue:** The outputs of these decoders are then utilized in two parallel branches: the Camera Pose Estimation Head predicts per-view camera transformations, while the Token-aligned Gaussian ...
- **p. 4 / 3.4. Token Fusion for Scene Reconstruction - extractive body cue:** Multi-scale features {Fi}nl i=1 from different layers of the Transformer decoder corresponding to the fused tokens are first upsampled and linearly projected: ˆFi = Proji(Fi), ...
- **p. 3 / 3.2. Architecture - extractive body cue:** To establish a canonical scene representation, the reference view I1 is decoded using a ViT decoder with cross-attention to other views.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For camera pose estimation, the network predicts per-view poses Pi that transform each input image Ii into the canonical reference view I1. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Problem Formulation), p. 1 (1. Introduction) |
| State/latent | camera, pose, estimation, network, predicts, per-view, poses, transform, input, image, canonical, reference | geometry, map, object/relationship state | p. 3 (3.1. Problem Formulation), p. 1 (1. Introduction), p. 3 (3.2. Architecture) |
| Output/action | Recent feed-forward variants [1, 5, 18, 40, 50] alleviate this by predicting 3D Gaussians directly from input images, but their applicability remains constrained by the requirement for accurate camera poses. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 3 (3.2. Architecture), p. 2 (1. Introduction) |
| Objective/outcome | The overall camera pose loss is: Lpose = LMSE(P, ˆP) + Lalign. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.6. Loss Functions), p. 5 (3.6. Loss Functions), p. 3 (3.1. Problem Formulation) |

## Main Claims and Actual Contribution

- 기준 장면 토큰과 시점별 토큰을 비대칭 이중 경로에서 결합하고 영상 토큰에 대응하는 가우시안을 예측한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf#page=5)
- 새 시점 영상 합성과 카메라 자세 추정을 따로 평가하고 디코더와 토큰 정렬이 두 결과에 주는 영향을 분석했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.2. Experimental Results), p. 5 (4.2. Experimental Results) |
| Embodiment/environment | We evaluate our method on novel view synthesis (NVS) and camera pose estimation across sparse and long-sequence real-world datasets. | hardware/simulator version and reset protocol | p. 5 (4. Experiment), p. 6 (4.2. Experimental Results) |
| Dataset/benchmark | Following [23], we train and evaluate on RE10K under both 4-view and 8-view reference settings, and further perform cross-dataset generalization tests on ScanNet. | role, split, size and leakage | p. 5 (4. Experiment), p. 6 (4.2. Experimental Results), p. 5 (4.1. Experimental Settings), p. 6 (4.2. Experimental Results) |
| Metric | For camera pose estimation, we report Absolute Translation Error (ATE), Relative Translation Error (RPE-t), and Relative Rotation Error (RPE-r). | definition, denominator, direction and uncertainty | p. 5 (4.1. Experimental Settings), p. 6 (4.2. Experimental Results), p. 5 (4.1. Experimental Settings) |
| Baseline/ablation | As can be seen, TokenSplat consistently outperforms state-of-the-art pose-free methods, including those specifically designed for multi-view input such as VicaSplat and AnySplat, which leverage crossneighbor attention and pixel-aligned ... | fair input/data/compute/action matching | p. 5 (4.2. Experimental Results), p. 6 (4.2. Experimental Results), p. 8 (4.3. Ablation Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** It yields consistent accuracy improvements and robust zero-shot generalization across diverse datasets.
- **p. 5 / 4.2. Experimental Results - extractive body cue:** Despite the difference in view counts, TokenSplat maintains stable reconstruction quality, while competing methods, including AnySplat, which fuses pixel-aligned Gaussians by predicting fusion confidence, and ...
- **p. 6 / 4.2. Experimental Results - extractive body cue:** FreeSplat generates numerous scattered Gaussians, while NoPoSplat and SPFSplat show poor scalability and fail to generalize to unseen distant viewpoints.
- **p. 6 / 4.2. Experimental Results - extractive body cue:** On ScanNet, the model maintains accurate pose estimation under the 28-view setting, reducing ATE by 0.018 over AnySplat, confirming both robustness and scalability of TokenSplat ...
- **p. 8 / 4.3. Ablation Analysis - extractive body cue:** Compared to our full model (a), (b) replacing the Token-aligned Gaussian Prediction with a pixelaligned Gaussian head degrades both reconstruction and pose estimation, with SSIM ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Architecture), p. 4 (3.4. Token Fusion for Scene Reconstruction), p. 4 (3.3. Asymmetric Dual-Flow Decoder)이다.
