# SDGS: Spatial Difference Guided Gaussian Splatting for Simultaneous Localization and 3D Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Yijian Tian, Mingtao Ou, Zijian Pan, Xinglong Ji
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf)

## Why This Paper Is Here

SDGS는 하이브리드 픽셀 센서의 공간 차분으로 카메라 자세를 추적하고 영상 강도로 조밀한 가우시안 장면을 복원한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting (3DGS) pioneers explicit scene representation, enabling photorealistic, real-time 3D reconstruction.
- **p. 1 / Abstract - extractive body cue:** Conventional pipelines require precomputed camera poses for Gaussian parameter optimization, which introduces latency between perception and reconstruction.
- **p. 1 / Abstract - extractive body cue:** Recent works have adapted 3DGS to online settings without pose priors.
- **p. 1 / Abstract - extractive body cue:** However, these approaches often suffer from high computational costs and are vulnerable to lowquality image inputs.
- **p. 1 / Abstract - extractive body cue:** We propose a sparse, edge-guided reconstruction strategy that simultaneously estimates 6-DoF camera poses by aligning rendered 3D edges with input 2D edges, achieving about 2× ...
- **p. 1 / 1. Introduction - extractive body cue:** This is fundamentally due to the inherent limitations of traditional imaging mechanisms of vision sensors and their dense descriptors.
- **p. 1 / 1. Introduction - extractive body cue:** This makes it challenging for the system to achieve both efficiency and robustness in real world, making it difficult to balance reconstruction accuracy and speed.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We introduce a sparse edge descriptor using Gaussian ellipsoids as 3D representation, providing clear geometric cues while ...
- **p. 2 / 1. Introduction - extractive body cue:** Moreover, our method substantially reduces the resource overhead required for representing key geometries relative to fully dense approaches.
- **p. 5 / 3.2.2. Tracking - extractive body cue:** A Gaussian is marked as visible in the current view if its center falls within the observed depth range and has a non-negligible opacity contribution.
- **p. 5 / 3.3.1. SD Keyframe - extractive body cue:** With a regular opacity reset strategy, Gaussians that have never been marked as active will receive no supervision after reset and are pruned from the ...
- **p. 4 / 3.1.2. Edge-aligned 3D Gaussian Representation - extractive body cue:** SDGS overview: our approach uses high-frame-rate SD inputs to optimize a sparse Gaussian map and performs camera pose estimation via edge alignment.
- **p. 5 / 3.3.2. SD Loss - extractive body cue:** For SD photometric mapping, we use the loss defined as follows: \ m at hcal {L} _ { \te xt {sd}}=\bigl \/\, I(\mathcal {G}_A,T_{CW})-I_{\text {SD}} ...
- **p. 5 / 3.2.2. Tracking - extractive body cue:** At each level, the SD observation is downsampled and its distance transform is computed once; we then directly render I(\mat hca l {G}_{\mathrm {SD}}, T_{CW} ...
- **p. 4 / 3.1.2. Edge-aligned 3D Gaussian Representation - extractive body cue:** With the estimated poses, we then promote keyframes for dense RGB reconstruction using SD-guided initialization and optimization.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We estimate camera poses by aligning the rendered sparse edge map with the input edge image using a distance transform. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation) |
| State/latent | estimate, camera, poses, aligning, rendered, sparse, edge, input, image, distance, transform, SDGS | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation), p. 2 (1. Introduction) |
| Output/action | SDGS overview: our approach uses high-frame-rate SD inputs to optimize a sparse Gaussian map and performs camera pose estimation via edge alignment. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation), p. 2 (1. Introduction), p. 5 (3.2.2. Tracking) |
| Objective/outcome | We minimize \mathca l { L}_{\t ext { trackin g} } = \big \/\, I(\mathcal {G}_{\mathrm {SD}}, T_{CW}) \odot DT(I_{\text {SD}}) \,\big \/_{1}, \label {eq:track-loss} (7) so that each rendered positive response ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2.2. Tracking), p. 6 (3.4.2. SD-guided Mutually Exclusive RGB Supervision), p. 3 (3.1.1. Sparse Edge Descriptor) |

## Main Claims and Actual Contribution

- 윤곽을 나타내는 희소 가우시안과 외관을 표현하는 조밀한 가우시안을 구분하고 두 종류의 관측을 추적·매핑에 각각 배분한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf#page=6)
- 빠른 카메라 운동에서 궤적 정확도와 추적 비용을 비교하고, 노출 중 흐림이 포함된 영상의 복원 품질을 별도로 평가했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

표 1의 스테레오 Tianmouc 시퀀스에서 SDGS의 궤적 오차 RMSE는 slow 4.21 cm, fast 5.89 cm, extreme 3.91 cm다. 표 2는 별도 TUM RGB-D 자료에서 측정한 궤적 오차다. 저자가 보고한 약 2배의 속도 향상은 자세 최적화 반복 1회 기준이다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf#page=1) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf#page=7)

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** By combining emerging hybrid pixel cameras, we not only maintain robust tracking accuracy under extreme motions where other methods fail, but also reconstruct dense maps ...
- **p. 8 / 5. Conclusion - extractive body cue:** Our system balances tracking robustness, high-fidelity reconstruction, and system efficiency.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Our approach follows a "sketch-then-paint" paradigm. Similar to drawing the outline before adding colors, we first generate a discrete outline (skeleton) for efficient ...
- **p. 6 / 4.1.2. Datasets - extractive body cue:** We evaluate our method on three datasets to verify both the robustness and generalization ability: SD-Replica Datasets.
- **p. 7 / 4.2.1. Tracking Accuracy - extractive body cue:** We first evaluate our method against state-of-the-art approaches in terms of tracking 6-DoF pose accuracy and robustness under various motion conditions, based on the stereo ...
- **p. 7 / 4.2.2. Deblurring Metrics - extractive body cue:** Method Input tianmouc/slow tianmouc/fast tianmouc/extreme Average Gaussian-SLAM RGB 4.60 fail fail - SplaTAM 6.52 fail fail - MonoGS-RGBD 3.32 24.52 fail - WildGS-SLAM∗† 2.01 8.21 ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3.2. SD Loss), p. 5 (3.2.2. Tracking)이다.
