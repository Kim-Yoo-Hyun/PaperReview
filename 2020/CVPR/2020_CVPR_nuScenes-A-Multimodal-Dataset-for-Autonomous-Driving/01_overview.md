# nuScenes: A Multimodal Dataset for Autonomous Driving

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1903.11027.
> PDF retrieval source: https://arxiv.org/pdf/1903.11027. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / CVPR
- Authors: Holger Caesar, Varun Bankiti, Alex H. Lang, Sourabh Vora, Venice Erin Liong, Qiang Xu, Anush Krishnan, Yu Pan, Giancarlo Baldan, Oscar Beijbom
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, LiDAR, sensor fusion, Dataset
- Official paper: https://arxiv.org/abs/1903.11027
- Full-text retrieval: https://arxiv.org/pdf/1903.11027
- Code/Project: https://www.nuscenes.org/nuscenes
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf)

## Why This Paper Is Here

nuScenes는 카메라·레이더·LiDAR가 동기화된 도심 주행 시퀀스와 3차원 물체 주석을 제공해 멀티센서 인식을 평가한다. [PDF 1쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf#page=1) · [PDF 4쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf#page=4)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robust detection and tracking of objects is crucial for the deployment of autonomous vehicle technology.
- **p. 1 / Abstract - extractive body cue:** Image based benchmark datasets have driven development in computer vision tasks such as object detection, tracking and segmentation of agents in the environment.
- **p. 1 / Abstract - extractive body cue:** Most autonomous vehicles, however, carry a combination of cameras and range sensors such as lidar and radar.
- **p. 1 / Abstract - extractive body cue:** As machine learning based methods for detection and tracking become more prevalent, there is a need to train and evaluate such methods on datasets containing ...
- **p. 1 / Abstract - extractive body cue:** In this work we present nuTonomy scenes (nuScenes), the first dataset to carry the full autonomous vehicle sensor suite: 6 cameras, 5 radars and 1 ...
- **p. 2 / 1.1. Contributions - extractive body cue:** From the complexities of the multimodal 3D detection challenge, and the limitations of current AV datasets, a large-scale multimodal dataset with 360◦coverage across all vision ...
- **p. 1 / 1. Introduction - extractive body cue:** Since the three sensor types have different failure modes during difficult conditions, the joint treatment of sensor data is essential for agent detection and tracking.

## Core Idea

- **p. 2 / 1.1. Contributions - extractive body cue:** Our second contribution is new detection and tracking metrics aimed at the AV application.
- **p. 2 / 1.1. Contributions - extractive body cue:** It enables research on multiple tasks such as object detection, tracking and behavior modeling in a range of conditions.
- **p. 1 / Abstract - extractive body cue:** In this work we present nuTonomy scenes (nuScenes), the first dataset to carry the full autonomous vehicle sensor suite: 6 cameras, 5 radars and 1 ...
- **p. 1 / 1. Introduction - extractive body cue:** At the bottom we show the human written scene description.
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore the reflectance of lidar is an important feature [40, 51].
- **p. 1 / 1. Introduction - extractive body cue:** Such algorithms rely increasingly on machine learning, which drives the need for benchmark datasets.
- **p. 2 / 1. Introduction - extractive body cue:** Still, to the best of our knowledge, no other 3D dataset provides attribute annotations, such as pedestrian pose or vehicle state.
- **p. 3 / 1.2. Related datasets - extractive body cue:** It provides 200k 3D boxes over 22 scenes which helped advance the state-of-the-art in 3D object detection.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Still, to the best of our knowledge, no other 3D dataset provides attribute annotations, such as pedestrian pose or vehicle state. | standardized observation, action, task state와 evaluation split | p. 2 (1. Introduction), p. 2 (1.1. Contributions) |
| State/latent | Still, best, knowledge, other, dataset, provides, attribute, annotations, pedestrian, pose, vehicle, state | benchmark state/goal와 method decision | p. 2 (1. Introduction), p. 2 (1.1. Contributions), p. 3 (1.2. Related datasets) |
| Output/action | Third, we publish the devkit, evaluation code, taxonomy, annotator instructions, and database schema for industrywide standardization. | policy/controller trajectory 또는 measured result | p. 2 (1.1. Contributions), p. 3 (1.2. Related datasets), p. 1 (1. Introduction) |
| Objective/outcome | Operating points where recall or precision is less than 10% are removed in order to minimize the impact of noise commonly seen in low precision and recall regions. | success metric, robustness, generalization과 reproducibility | p. 5 (3.1. Detection), p. 1 (1. Introduction), p. 4 (2. The nuScenes dataset) |

## Main Claims and Actual Contribution

- 서로 다른 도시와 기상·조명 조건에서 수집한 센서 자료를 보정하고 키프레임에 물체 상자·범주·속성을 주석했다. [PDF 3쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf#page=5)
- 거리 기반 검출 매칭과 위치·크기·방향·속도·속성 오차를 결합한 검출 지표를 정의하고 추적 평가도 제시했다. [PDF 5쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf#page=7)

## Evaluation Scope

원 논문은 약 20초 길이의 주행 장면 1,000개를 수집했다. 23개 주석 범주 중 10개가 3차원 검출 평가 대상이며, AP의 매칭 기준은 지면에 투영한 두 상자 중심 사이의 거리다. [PDF 1쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf#page=1) · [PDF 4쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf#page=5)

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Future work will add image-level and pointlevel semantic labels and a benchmark for trajectory prediction [63].
- **p. 3 / 2. The nuScenes dataset - extractive body cue:** From a large body of training data we manually select 84 logs with 15h of driving data (242km travelled at an av4In preliminary analysis we ...
- **p. 4 / 2. The nuScenes dataset - extractive body cue:** This method is very robust and we achieve localization errors of ≤10cm.
- **p. 7 / 4.2. Analysis - extractive body cue:** As expected, when using IOU matching, small objects like pedestrians and bicycles fail to achieve above 0 AP, making ordering impossible (Figure 7).

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1.1. Contributions), p. 1 (1. Introduction)이다.
