# Multimodal LiDAR-Camera Novel View Synthesis with Unified Pose-free Neural Fields

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://neurips.cc/virtual/2025/poster/118967.
> PDF retrieval source: https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: Weiyi Xue, Fan Lu, Yunwei Zhu, Zehan Zheng, Haiyun Wei, Sanqing Qu, Jiangtong Li, Ya Wu, Guang Chen
- 저자 판본: NeurIPS 게재본은 Haiyun Wei를 다섯 번째 저자로 싣는다. 학회 웹 서지에는 여덟 번째로 올라 있다. [표제면](https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf#page=1) · [학회 서지](https://proceedings.neurips.cc/paper_files/paper/2025/hash/70915b08a205ea5522528690d93518f6-Abstract-Conference.html)
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: geometry, sensor fusion, LiDAR, 3D Vision, camera pose
- Official paper: https://neurips.cc/virtual/2025/poster/118967
- Full-text retrieval: https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf)

## Why This Paper Is Here

MUP은 정확한 센서 자세가 주어지지 않은 주행 시퀀스에서 카메라 영상과 LiDAR 스캔을 공동 신경장으로 복원한다. [PDF 1쪽](https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf#page=4)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Pose-free Neural Radiance Field (NeRF) aims at novel view synthesis (NVS) without relying on accurate poses, exhibiting significant practical value.
- **p. 1 / Abstract - extractive body cue:** Image and LiDAR point cloud are two pivotal modalities in autonomous driving scenarios.
- **p. 1 / Abstract - extractive body cue:** While demonstrating impressive performance, single-modality pose-free NeRFs often suffer from local optima due to the limited geometric information provided by dense image textures or the ...
- **p. 1 / Abstract - extractive body cue:** Although prior methods have explored the complementary strengths of both modalities, they have only leveraged inherently sparse point clouds for discrete, nonpixel-wise depth supervision, and ...
- **p. 1 / Abstract - extractive body cue:** As a result, a Multimodal Unified Pose-free framework remains notably absent.
- **p. 2 / 1 Introduction - extractive body cue:** Nevertheless, prior research [37] has faced challenges due to the significant domain gap and uncoordinated convergence problems [27, 42, 34] between these modalities.
- **p. 2 / 1 Introduction - extractive body cue:** Compared to continuous LiDAR-Camera Fields, projecting LiDAR point clouds onto images as discrete depth priors fails to provide continuous, pixel-wise supervision.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In summary, our primary contributions can be delineated as follows: (1) We propose MUP, a unified pose-free framework that combines the advantages of two modalities ...
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, to enhance color-depth consistency, we introduce a consistency constraint by projecting image pixels onto adjacent frames using depth derived from NeRF.
- **p. 2 / 1 Introduction - extractive body cue:** To alleviate modality conflicts [37] and address the uncoordinated convergence problem, we introduce a multimodal-specific coarse-to-fine training approach [16], facilitating the utilization of a singular ...
- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our method across diverse scenarios using the KITTI-360 [15] and NuScenes [4] autonomous driving datasets.
- **p. 5 / 4 Methodology - extractive body cue:** Finally, we present the proposed consistency constraint and the overall optimization pipeline in Section 4.3.
- **p. 5 / 4 Methodology - extractive body cue:** Based on this observation, we propose a multimodal training method for optimizing the hash grid, which also stabilizes pose optimization and mitigates modality conflicts.
- **p. 5 / 4 Methodology - extractive body cue:** Then, we introduce our MMG module in Section 4.2, which provides explicit geometric guidance to avoid local optima.
- **p. 7 / 4 Methodology - extractive body cue:** Based on these correspondences, we introduce a point-to-image error using photometric loss, which serves as a regularization term.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For the image modality, we use a lightweight MLP to refine the geo-MLP output, helping reduce modality conflicts. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (4 Methodology), p. 5 (4 Methodology) |
| State/latent | image, modality, lightweight, MLP, refine, geo-MLP, output, helping, reduce, conflicts, observation, multimodal | geometry, map, object/relationship state | p. 5 (4 Methodology), p. 5 (4 Methodology), p. 7 (4 Methodology) |
| Output/action | Based on this observation, we propose a multimodal training method for optimizing the hash grid, which also stabilizes pose optimization and mitigates modality conflicts. | point map, pose, scene graph, affordance 또는 query result | p. 5 (4 Methodology), p. 7 (4 Methodology), p. 2 (1 Introduction) |
| Objective/outcome | To explore how modality features are fused, we independently truncate the gradients of reconstruction loss LCamera and LLiDAR to hash grids and geo-MLP. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4 Methodology), p. 6 (4 Methodology), p. 5 (4 Methodology) |

## Main Claims and Actual Contribution

- 점군의 기하 관계와 인접 영상의 광도 제약을 이용해 자세를 갱신하고 센서별 특징을 거친 단계에서 세밀한 단계로 융합한다. [PDF 4쪽](https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf#page=6)
- KITTI-360과 nuScenes에서 새로운 시점의 영상과 LiDAR 관측을 각각 평가하고 모달리티 간 기하 최적화의 효과를 분석했다. [PDF 7쪽](https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 9 (5 Experiment) |
| Embodiment/environment | For the NuScenes dataset, it includes six cameras and a LiDAR sensor, with keyframes that are typically used, which are time-synchronized based on timestamps. | hardware/simulator version and reset protocol | p. 8 (5 Experiment), p. 8 (5 Experiment) |
| Dataset/benchmark | As for the registration-first approach, ColoredICP [24] exhibits limited accuracy in large-scale outdoor scenes. | role, split, size and leakage | p. 8 (5 Experiment), p. 8 (5 Experiment), p. 9 (5 Experiment), p. 9 (5 Experiment) |
| Metric | Figure 4: Consistency constraint. We project rendered images onto other frames by depth obtained from NeRF to compute the photometric error. It's particularly effective for textureless regions. Implicit Pose Optimization. In the ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 8 (5 Experiment), p. 8 (5 Experiment) |
| Baseline/ablation | Figure 5: Qualitative comparison of NVS. We compared MUP with pose-free and registration-first methods. Nope-NeRF and Colored-ICP-assisted fail due to the large-scale scene. BA-Alignmif struggles to converge. All baselines fail entirely ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 9 (5 Experiment), p. 10 (5 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 7 Conclusion - extractive body cue:** We revisit the limitations of single-modality pose-free methods in large-scale scenes.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: NVS results w/ and w/o accurate poses. Compared to continuous LiDAR-Camera Fields, projecting LiDAR point clouds onto images as discrete depth priors fails ...
- **p. 9 / 5 Experiment - extractive body cue:** Alignmif [37] cannot be effectively used in ill-conditioned optimization.
- **p. 10 / 5 Experiment - extractive body cue:** Additionally, it is not designed to handle dynamic scenes, which is a non-negligible limitation in autonomous driving scenarios.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative comparison of NVS. We compared MUP with pose-free and registration-first methods. Nope-NeRF and Colored-ICP-assisted fail due to the large-scale scene. BA-Alignmif struggles ...
- **p. 8 / 5 Experiment - extractive body cue:** Following [47, 16], we perturbed poses of car with additive noise corresponding to a standard deviation of 20 deg in rotation and 3m in translation.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 5 (4 Methodology)이다.

## 검색 태그 근거

카메라 영상과 라이다 스캔의 공유 신경장을 최적화하면서 두 센서의 자세를 보정한다. 주행 자료에서 카메라 뷰와 라이다 스캔을 새 관측 위치에서 합성하는 성능을 비교한다. [원문 4쪽](https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf#page=4) · [원문 7쪽](https://papers.neurips.cc/paper_files/paper/2025/file/70915b08a205ea5522528690d93518f6-Paper-Conference.pdf#page=7)
