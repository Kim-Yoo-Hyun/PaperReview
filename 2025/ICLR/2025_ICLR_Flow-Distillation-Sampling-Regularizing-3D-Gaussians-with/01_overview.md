# Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/623307df18da128262aaf394cdcfb235-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/113507. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Lin-Zhuo Chen, Kangjie Liu, Youtian Lin, Zhihao Li, Siyu Zhu, Xun Cao, Yao Yao
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/623307df18da128262aaf394cdcfb235-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/623307df18da128262aaf394cdcfb235-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/623307df18da128262aaf394cdcfb235-Paper-Conference.pdf)

## Why This Paper Is Here

Flow Distillation Sampling은 관측 뷰에 가까운 새 시점에서 예상되는 광류를 이용해 장면별 3D 가우시안의 기하를 개선한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/623307df18da128262aaf394cdcfb235-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/623307df18da128262aaf394cdcfb235-Paper-Conference.pdf#page=4)

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

- 가우시안 기하에서 계산한 광류와 사전학습된 대응 모델이 두 뷰에서 추정한 광류를 일치시키도록 장면을 최적화한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/623307df18da128262aaf394cdcfb235-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/623307df18da128262aaf394cdcfb235-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/623307df18da128262aaf394cdcfb235-Paper-Conference.pdf#page=5)
- 깊이·메시·새 시점 영상을 각각 평가하고 대응 사전분포와 가상 카메라 이동 방식이 복원에 미치는 영향을 분석했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/623307df18da128262aaf394cdcfb235-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/623307df18da128262aaf394cdcfb235-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/623307df18da128262aaf394cdcfb235-Paper-Conference.pdf#page=9)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 4 (3 METHOD)이다.
