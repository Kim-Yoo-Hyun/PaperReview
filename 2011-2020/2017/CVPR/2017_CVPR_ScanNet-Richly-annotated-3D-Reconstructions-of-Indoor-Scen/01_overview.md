# ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1702.04405.
> PDF retrieval source: https://arxiv.org/pdf/1702.04405. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / CVPR
- Authors: Angela Dai, Angel X. Chang, Manolis Savva, Maciej Halber, Thomas Funkhouser, Matthias Nießner
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Dataset, semantic, 3D reconstruction
- Official paper: https://arxiv.org/abs/1702.04405
- Full-text retrieval: https://arxiv.org/pdf/1702.04405
- Code/Project: http://www.scan-net.org/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf)

## Why This Paper Is Here

ScanNet은 일반 사용자가 수집한 실내 RGB-D 영상을 카메라 궤적·표면·물체 의미가 연결된 3차원 장면 자료로 구축했다. [PDF 1쪽](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf#page=1) · [PDF 2쪽](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf#page=2)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A key requirement for leveraging supervised deep learning methods is the availability of large, labeled datasets.
- **p. 1 / Abstract - extractive body cue:** Unfortunately, in the context of RGB-D scene understanding, very little data is available - current datasets cover a small range of scene views and have ...
- **p. 1 / Abstract - extractive body cue:** To address this issue, we introduce ScanNet, an RGB-D video dataset containing 2.5M views in 1513 scenes annotated with 3D camera poses, surface reconstructions, and ...
- **p. 1 / Abstract - extractive body cue:** To collect this data, we designed an easy-to-use and scalable RGB-D capture system that includes automated surface reconstruction and crowdsourced semantic annotation.
- **p. 1 / Abstract - extractive body cue:** We show that using this data helps achieve state-of-the-art performance on several 3D scene understanding tasks, including 3D object classification, semantic voxel labeling, and CAD ...
- **p. 1 / 1. Introduction - extractive body cue:** Typically, 3D deep learning methods use synthetic data to mitigate this lack of real-world data [91, 6].
- **p. 1 / 1. Introduction - extractive body cue:** Thus, many of the current RGB-D datasets [74, 92, 77, 32] are orders of magnitude smaller than their 2D counterparts.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we introduce ScanNet, a dataset of richlyannotated RGB-D scans of real-world environments containing 2.5M RGB-D images in 1513 scans acquired in 707 ...
- **p. 1 / 1. Introduction - extractive body cue:** In the collection of this dataset, we have considered two main research questions: 1) how can we design a framework that allows many people to ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** This allows us to select the floor plane based on the scan bounding box and the normal most similar to the IMU up vector direction.
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** We chose the BundleFusion system [12] as it was designed and evaluated for similar sensor setups as ours, and provides real-time speed while being reasonably ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** BundleFusion produces accurate pose alignments which we then use to perform volumetric integration through VoxelHashing [62] and extract a high resolution surface mesh using the ...
- **p. 4 / 3.2. Surface Reconstruction - extractive body cue:** There is a large variety of algorithms targeting this scenario [59, 88, 7, 62, 37, 89, 42, 9, 90, 38, 12].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For each input scan, we first run BundleFusion [12] at a voxel resolution of 1 cm3. | standardized observation, action, task state와 evaluation split | p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction) |
| State/latent | input, scan, first, BundleFusion, voxel, resolution, chose, system, designed, evaluated, similar, sensor | benchmark state/goal와 method decision | p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction), p. 1 (1. Introduction) |
| Output/action | We chose the BundleFusion system [12] as it was designed and evaluated for similar sensor setups as ours, and provides real-time speed while being reasonably robust given handheld RGBD video data. | policy/controller trajectory 또는 measured result | p. 4 (3.2. Surface Reconstruction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | This annotation is in progress at ≈35%, with gray regions indicating unannotated surfaces. | success metric, robustness, generalization과 reproducibility | p. 4 (3.2. Surface Reconstruction) |

## Main Claims and Actual Contribution

- 촬영 도구와 재구성 절차를 제공하고 표면에 의미 라벨과 일부 물체의 정렬된 CAD 모델을 붙였다. [PDF 2쪽](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf#page=2) · [PDF 3쪽](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf#page=4)
- 같은 자료에서 3차원 물체 분류, 복셀 의미 라벨링과 CAD 검색의 과제 및 기준선 결과를 제시했다. [PDF 6쪽](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf#page=8)

## Evaluation Scope

원 논문에 보고된 규모는 서로 다른 실내 공간 707곳, RGB-D 스캔 1,513회, 영상 약 250만 장이다. 표 3의 물체 분류·복셀 라벨링 분할은 전체 수집 규모와 구분한다. [PDF 1쪽](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf#page=1) · [PDF 2쪽](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf#page=2) · [PDF 6쪽](https://openaccess.thecvf.com/content_cvpr_2017/papers/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.pdf#page=6)

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced annotation framework. ciently providing (dense) annotations in 3D is ...
- **p. 8 / 6. Conclusion - extractive body cue:** We demonstrated that the richlyannotated scan data collected so far in ScanNet is useful in achieving state-of-the-art performance on several 3D scene understanding tasks; we ...
- **p. 3 / 3.1. RGB-D Scanning - extractive body cue:** This feature was critical for providing intuition to users who are not familiar with the constraints and limitations of 3D reconstruction algorithms.
- **p. 5 / 3.3. Semantic Annotation - extractive body cue:** The main limitation of this interface is due to the mismatch between the corpus of available CAD models and the objects observed in the ScanNet ...
- **p. 5 / 3.3. Semantic Annotation - extractive body cue:** A promising way to alleviate this limitation is to algorithmically suggest candidate retrieved and aligned CAD models such that workers can perform an easier verification ...
- **p. 6 / 5.1. 3D Object Classification - extractive body cue:** When training data is synthetic and test is performed on real data, there is also a significant discrepancy of test performance, as data characteristics, such ...
- **p. 6 / 5.1. 3D Object Classification - extractive body cue:** Note that the number of instances does not include the rotation augmentation. ing, research has developed approaches to classify objects using only geometric data with ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 4 (3.2. Surface Reconstruction), p. 7 (5.1. 3D Object Classification), p. 20 (Figure/Table caption)이다.
