# Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=BzsjHiBfLk.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/113507. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D Vision
- Official paper: https://openreview.net/forum?id=BzsjHiBfLk
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/113507
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, sensor depth acquisition is costly, and the depth prior information from pre-trained monocular deep models inevitably suffer from the scale ambiguity (Liu et al., 2023b).를 문제로 두고, In this paper, we introduce Flow Distillation Sampling (FDS), an online method for distilling matching prior from a pre-trained optical flow model into the 3DGS training process.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** 3D Gaussian Splatting (3DGS) has achieved excellent rendering quality with fast training and rendering speed.
- **p. 1 / ABSTRACT - extractive body cue:** However, its optimization process lacks explicit geometric constraints, leading to suboptimal geometric reconstruction in regions with sparse or no observational input views.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we try to mitigate the issue by incorporating a pre-trained matching prior to the 3DGS optimization process.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce Flow Distillation Sampling (FDS), a technique that leverages pre-trained geometric knowledge to bolster the accuracy of the Gaussian radiance field.
- **p. 1 / ABSTRACT - extractive body cue:** Our method employs a strategic sampling technique to target unobserved views adjacent to the input views, utilizing the optical flow calculated from the matching model ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, sensor depth acquisition is costly, and the depth prior information from pre-trained monocular deep models inevitably suffer from the scale ambiguity (Liu et al., ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** FDS aims to enhance the geometry quality of Gaussian radiance field by leveraging the matching prior

## Core Idea

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Flow Distillation Sampling (FDS), an online method for distilling matching prior from a pre-trained optical flow model into the 3DGS ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized as follows: • FDS leverages matching prior information to recover absolute scale, significantly enhancing the geometric quality of the Gaussian radiance ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) has been widely applied to the field of 3D reconstruction and rendering, including novel view synthesis of ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Finally the Prior Flow is used to supervise Radiance flow, which enhances the geometric quality of Gaussian Radiance Field. into the unobserved novel view.
- **p. 3 / 3 METHOD - extractive body cue:** Our FDS regulates the optimization of Gaussian radiance field by incorporating matching priors from the pretrained deep model.
- **p. 4 / 3 METHOD - extractive body cue:** 3.2 FLOW DISTILLATION SAMPLING Given a collection of images {Ii}i=1,2,...N, Gaussian Radiance Field typically employs the following loss function for rendering optimization: L = 1
- **p. 3 / 3 METHOD - extractive body cue:** The generation of Radiance Flow and our proposed FDS loss, along with the equipped camera sampling scheme, are detailed in Sec.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our contributions are summarized as follows: • FDS leverages matching prior information to recover absolute scale, significantly enhancing the geometric quality of the Gaussian radiance field. • An adaptive camera sampling scheme ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 INTRODUCTION), p. 4 (3 METHOD) |
| State/latent | contributions, summarized, follows, FDS, leverages, matching, prior, information, recover, absolute, scale, significantly | geometry, map, object/relationship state | p. 2 (1 INTRODUCTION), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION) |
| Output/action | As mentioned above, we can project pixel x = (u1, v1) in m-th view image to the n-th view by its corresponding depth and their pose transformation: Dn(u2, v2) "u2 v2 1 ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3 METHOD), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Objective/outcome | 3.2 FLOW DISTILLATION SAMPLING Given a collection of images {Ii}i=1,2,...N, Gaussian Radiance Field typically employs the following loss function for rendering optimization: L = 1 | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3 METHOD), p. 3 (3 METHOD), p. 3 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Flow Distillation Sampling (FDS), an online method for distilling matching prior from a pre-trained optical flow model into the 3DGS ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized as follows: • FDS leverages matching prior information to recover absolute scale, significantly enhancing the geometric quality of the Gaussian radiance ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) has been widely applied to the field of 3D reconstruction and rendering, including novel view synthesis of ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Finally the Prior Flow is used to supervise Radiance flow, which enhances the geometric quality of Gaussian Radiance Field. into the unobserved novel view.
- **p. 8 / 4.2 RESULTS - extractive body cue:** We found that Sea Raft (Wang et al., 2024) outperforms Raft (Teed and Deng, 2020) on FDS, indicating that a better optical flow model can ...
- **p. 9 / 4.2 RESULTS - extractive body cue:** From the results, it can be seen that depth order information provided by monocular depth improves reconstruction accuracy.
- **p. 9 / 4.2 RESULTS - extractive body cue:** Meanwhile, our FDS achieves the best performance among all the priors, and by integrating all three components, we obtained the optimal results.
- **p. 8 / 4.2 RESULTS - extractive body cue:** By incorporating the matching prior through FDS, the quality of the rendered depth is significantly improved.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.2 RESULTS), p. 9 (4.2 RESULTS) |
| Embodiment/environment | 4.1.2 DATASETS AND METRICS We evaluate our method for 3D reconstruction and novel view synthesis tasks on Mushroom (Ren et al., 2024), ScanNet (v2) (Dai et al., 2017), and Replica (Straub et ... | hardware/simulator version and reset protocol | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Dataset/benchmark | 3D Reconstruction and novel view synthesis results on ScanNet dataset. | role, split, size and leakage | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4.2 RESULTS) |
| Metric | Additionally, for mesh evaluation, we use metrics including Accuracy, Completion, Chamfer-L1 distance, Normal Consistency, and F-scores. | definition, denominator, direction and uncertainty | p. 8 (4 EXPERIMENTS), p. 9 (4.2 RESULTS), p. 10 (4.2 RESULTS) |
| Baseline/ablation | With the integration of FDS, the mesh quality is significantly enhanced compared to the baseline, featuring fewer floaters and more well-defined shapes. | fair input/data/compute/action matching | p. 9 (4.2 RESULTS), p. 8 (4.2 RESULTS), p. 8 (4.2 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 4.2 RESULTS - extractive body cue:** Due to the significant movement between images, the Prior Flow fails to accurately match the pixel between them, leading to a further degradation in geometric ...
- **p. 9 / 4.2 RESULTS - extractive body cue:** The multi-view depth prior, hindered by the limited feature overlap between input views, fails to offer reliable geometric information.
- **p. 10 / 4.2 RESULTS - extractive body cue:** 4.4 LIMITATION AND FURTHER WORK Firstly, our FDS faces challenges in scenes with significant lighting variations between different views, as shown in the lamp of ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We removed the depth distortion loss in 2DGS because we found that it degrades its results in indoor scenes.
- **p. 8 / 4.2 RESULTS - extractive body cue:** This demonstrates the robustness and effectiveness of the FDS method across different datasets.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, sensor depth acquisition is costly, and the depth prior information from pre-trained monocular deep models inevitably suffer from the scale ambiguity (Liu et al., 2023b).를 문제로 두고, In this paper, we introduce Flow Distillation Sampling (FDS), an online method for distilling matching prior from a pre-trained optical flow model into the 3DGS training process.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 4 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
