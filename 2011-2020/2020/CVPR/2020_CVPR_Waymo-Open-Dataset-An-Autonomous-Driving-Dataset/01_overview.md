# Scalability in Perception for Autonomous Driving: Waymo Open Dataset

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1912.04838.
> PDF retrieval source: https://arxiv.org/pdf/1912.04838. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / CVPR
- Authors: Pei Sun, Henrik Kretzschmar, Xerxes Dotiwalla, Aurelien Chouard, Vijaysai Patnaik, Paul Tsui, James Guo, Yin Zhou, Yuning Chai, Benjamin Caine, Vijay Vasudevan, Wei Han, Jiquan Ngiam, Hang Zhao, Aleksei Timofeev, Scott Ettinger, Maxim Krivokon, Amy Gao, Aditya Joshi, Yu Zhang, Jonathon Shlens, Zhifeng Chen, Dragomir Anguelov
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, LiDAR, sensor fusion, Dataset, 3D detection
- Official paper: https://arxiv.org/abs/1912.04838
- Full-text retrieval: https://arxiv.org/pdf/1912.04838
- Code/Project: https://waymo.com/open/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf)

## Why This Paper Is Here

Waymo Open Dataset 원 논문은 여러 도시에서 수집한 동기화 카메라·LiDAR 시퀀스와 시각 및 점군 인식용 평가 기준을 제시한다. [PDF 1쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf#page=1) · [PDF 2쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf#page=2)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The research community has increasing interest in autonomous driving research, despite the resource intensity of obtaining representative real world data.
- **p. 1 / Abstract - extractive body cue:** Existing selfdriving datasets are limited in the scale and variation of the environments they capture, even though generalization within and between operating regions is crucial ...
- **p. 1 / Abstract - extractive body cue:** In an effort to help align the research community's contributions with real-world selfdriving problems, we introduce a new large-scale, high quality, diverse dataset.
- **p. 1 / Abstract - extractive body cue:** Our new dataset consists of 1150 scenes that each span 20 seconds, consisting of well synchronized and calibrated high quality LiDAR and camera data captured ...
- **p. 1 / Abstract - extractive body cue:** It is 15x more diverse than the largest camera+LiDAR dataset available based on our proposed geographical coverage metric.
- **p. 1 / 1. Introduction - extractive body cue:** We demonstrate that the differences in these geographies lead to a pronounced domain gap, enabling exciting research opportunities in the field of domain adaptation.
- **p. 2 / 1. Introduction - extractive body cue:** Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** In an effort to help align the research community's contributions with real-world selfdriving problems, we introduce a new large-scale, high quality, diverse dataset.
- **p. 1 / 1. Introduction - extractive body cue:** To further accelerate the development of autonomous driving technology, we present the largest and most diverse multimodal autonomous driving dataset to date, comprising of images ...
- **p. 2 / 1. Introduction - extractive body cue:** We present benchmark results of several state-of-the-art 2D-and 3D object detection and tracking methods on the dataset.
- **p. 2 / 1. Introduction - extractive body cue:** Our dataset currently consists of 1000 scenes for training and validation, and 150 scenes for testing, where each scene spans 20 s.
- **p. 2 / 1. Introduction - extractive body cue:** This is the first dataset with such low-level, synchronized information available, making it easier to conduct research on LiDAR input representations other than the popular ...
- **p. 5 / 3.4. Sensor Data - extractive body cue:** See Figure 5 for an example output of the projection algorithm.
- **p. 5 / 3.4. Sensor Data - extractive body cue:** The algorithm is efficient and can be used in real time as it usually converges in 2 or 3 iterations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Detection methods may use data from any of the LiDAR and camera sensors; they may also choose to leverage sensor inputs from preceding frames. | standardized observation, action, task state와 evaluation split | p. 5 (4.1. Object Detection), p. 2 (1. Introduction) |
| State/latent | Detection, methods, data, LiDAR, camera, sensors, they, choose, leverage, sensor, inputs, preceding | benchmark state/goal와 method decision | p. 5 (4.1. Object Detection), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | In addition to sensor features such as elongation, we provide each range image pixel with an accurate vehicle pose. | policy/controller trajectory 또는 measured result | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Sensor Data) |
| Objective/outcome | We minimize the difference between t and ˜t by solving a single variable (t) convex quadratic optimization. | success metric, robustness, generalization과 reproducibility | p. 5 (3.4. Sensor Data), p. 3 (3.2. Coordinate Systems), p. 5 (4.1. Object Detection) |

## Main Claims and Actual Contribution

- 여러 방향의 카메라와 LiDAR를 보정하고 영상과 점군에 각각 2차원·3차원 상자 및 시간에 걸친 물체 식별자를 부여했다. [PDF 2쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf#page=2) · [PDF 3쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf#page=4)
- 검출·추적 과제의 지표와 분할을 정하고 지역이 달라질 때의 일반화와 학습 자료 규모의 영향을 비교했다. [PDF 5쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf#page=7)

## Evaluation Scope

CVPR 2020 논문의 자료는 20초짜리 주행 장면 1,150개다. 표 1은 차량당 LiDAR 5개·카메라 5개와 별도로 주석한 2차원·3차원 상자 수를 제시한다. [PDF 1쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf#page=1) · [PDF 2쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf#page=2)

## Explicit Limitations and Failure Boundary

- **p. 4 / 3.4. Sensor Data - extractive body cue:** Our experiments suggest that a highly elongated low-intensity return is a strong indicator for a spurious object, while low intensity alone is not a sufficient ...
- **p. 8 / 5.3. Domain Gap - extractive body cue:** This result does not hold when evaluating on SF.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Sensor Data)이다.

## 검색 태그 근거

여러 주행 지역에서 동기화한 카메라와 라이다를 제공한다. 영상과 점군의 상자 및 추적 ID로 검출·추적 성능을 평가한다. [원문 3쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf#page=3) · [원문 7쪽](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.pdf#page=7)
