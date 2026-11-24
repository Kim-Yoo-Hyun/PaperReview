# S3E: A Multi-Robot Multimodal Dataset for Collaborative SLAM

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2210.13723.
> PDF retrieval source: https://arxiv.org/pdf/2210.13723. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RA-L
- Authors: Dapeng Feng, Yuhua Qi, Shipeng Zhong, Zhiqiang Chen, Qiming Chen, Hongbo Chen, Jin Wu, Jun Ma
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics
- Official paper: https://arxiv.org/abs/2210.13723
- Full-text retrieval: https://arxiv.org/pdf/2210.13723
- Code/Project: https://pengyu-team.github.io/S3E/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

S3E는 여러 지상 로봇이 함께 이동하며 동기화·보정한 센서 기록을 제공해 단일 및 협력 SLAM을 같은 경로에서 시험할 수 있게 한다. [PDF 1쪽](https://arxiv.org/pdf/2210.13723v8#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The burgeoning demand for collaborative robotic systems to execute complex tasks collectively has intensified the research community's focus on advancing simultaneous localization and mapping (SLAM) ...
- **p. 1 / Abstract - extractive body cue:** Despite this interest, the scalability and diversity of existing datasets for collaborative trajectories remain limited, especially in scenarios with constrained perspectives where the generalization capabilities ...
- **p. 1 / Abstract - extractive body cue:** Addressing this gap, we introduce S3E, an expansive multimodal dataset.
- **p. 1 / Abstract - extractive body cue:** Captured by a fleet of unmanned ground vehicles traversing four distinct collaborative trajectory paradigms, S3E encompasses 13 outdoor and 5 indoor sequences.
- **p. 1 / Abstract - extractive body cue:** These sequences feature meticulously synchronized and spatially calibrated data streams, including 360-degree LiDAR point cloud, high-resolution stereo imagery, high-frequency inertial measurement units (IMU), and Ultrawideband ...
- **p. 4 / III. S3E DATASET - extractive body cue:** Playground: Open spaces with fewer obstructions challenge feature extraction and optimization.
- **p. 4 / III. S3E DATASET - extractive body cue:** Teaching Building and Tunnel: Poor lighting and similar geometric structures challenge robustness in maintaining

## Core Idea

- **p. 1 / C OLLABORATIVE Simultaneous Localization and Map - extractive body cue:** In this paper, we introduce four trajectory prototypes designed to meet these principles and evaluate the adaptability of C-SLAM methodologies across diverse closure strategies in ...
- **p. 1 / Abstract - extractive body cue:** Addressing this gap, we introduce S3E, an expansive multimodal dataset.
- **p. 2 / 3 UGVs - extractive body cue:** In conclusion, our work makes several key contributions to the field: ∙We have created a cutting-edge C-SLAM dataset using three ground robots, each equipped with ...
- **p. 3 / III. S3E DATASET - extractive body cue:** This includes the sensor types, their resolution, measurement range, accuracy, and any other pertinent technical details that define their contribution to the SLAM system's performance.
- **p. 2 / 3 UGVs - extractive body cue:** In the right part, our mobile platforms are available in two versions, each designed for different operational requirements.
- **p. 1 / C OLLABORATIVE Simultaneous Localization and Map - extractive body cue:** To fill this gap and enhance C-SLAM research, we introduce S3E dataset, offering a multimodal perspective with a variety of cooperative trajectory patterns in both ...
- **p. 3 / III. S3E DATASET - extractive body cue:** For synchronization across agents, we address two distinct scenarios: ∙In outdoor settings with access to Global Navigation Satellite System (GNSS) signals, we use GNSS time ...
- **p. 4 / III. S3E DATASET - extractive body cue:** Playground: Open spaces with fewer obstructions challenge feature extraction and optimization.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These sequences feature meticulously synchronized and spatially calibrated data streams, including 360-degree LiDAR point cloud, high-resolution stereo imagery, high-frequency inertial measurement units (IMU), and Ultrawideband (UWB) re ... | standardized observation, action, task state와 evaluation split | p. 1 (Abstract), p. 1 (C OLLABORATIVE Simultaneous Localization and Map) |
| State/latent | sequences, feature, meticulously, synchronized, spatially, calibrated, data, streams, including, degree, LiDAR, point | benchmark state/goal와 method decision | p. 1 (Abstract), p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 3 (III. S3E DATASET) |
| Output/action | 2) Communication Constraints: Robots are typically limited to sharing information within close proximity, necessitating trajectory designs that maintain a reasonable interaction distance for effective communication. | policy/controller trajectory 또는 measured result | p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET) |
| Objective/outcome | 2) Communication Constraints: Robots are typically limited to sharing information within close proximity, necessitating trajectory designs that maintain a reasonable interaction distance for effective communication. | success metric, robustness, generalization과 reproducibility | p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET) |

## Main Claims and Actual Contribution

- 서로 다른 로봇 간 이동 관계로 구성한 실외 13개·실내 5개 시퀀스에 스테레오 영상, LiDAR, IMU, UWB 거리 관측을 담았다. [PDF 1쪽](https://arxiv.org/pdf/2210.13723v8#page=1) · [PDF 4쪽](https://arxiv.org/pdf/2210.13723v8#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2210.13723v8#page=5)
- 센서별 좌표·시각 정보와 궤적 평가 조건을 설명하고 여러 SLAM 방식의 궤적 오차를 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2210.13723v8#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2210.13723v8#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2210.13723v8#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Embodiment/environment | The dataset features two mobile robot platform versions: ∙S3Ev1.0: Designed for indoor use with a compact design for exceptional maneuverability in tight spaces. ∙S3Ev2.0: Enhanced with a wider frame to accommodate a ... | hardware/simulator version and reset protocol | p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET) |
| Dataset/benchmark | To thoroughly assess the accuracy and robustness of CSLAM algorithms in complex, real-world scenarios, our dataset encompasses a diverse range of environments, each presenting unique challenges: Dormitory: High pedestrian and bicycle tr ... | role, split, size and leakage | p. 3 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 4 (III. S3E DATASET), p. 7 (IV. EXPERIMENTS) |
| Metric | The results, summarized in Table V and Table VI , reveal the absolute trajectory error (ATE) for both single-agent and collaborative SLAM (C-SLAM) systems in outdoor and indoor environments without UWB measurement. ... | definition, denominator, direction and uncertainty | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 3 (III. S3E DATASET) |
| Baseline/ablation | For most of the baselines, we only modify the intrinsic and extrinsic of the sensors and use the left camera for evaluation. | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / III. S3E DATASET - extractive body cue:** If inter-loop closures detection fails, we mark it "Failed".
- **p. 7 / VI. CONCLUSION - extractive body cue:** Our experiments using this dataset have highlighted the improved robustness of C-SLAM systems, especially in handling inter-loop closures.
- **p. 3 / III. S3E DATASET - extractive body cue:** Sensor Configuration Our S3E dataset encompasses a multimodal array of sensors, each selected for its operational range and noise characteristics, and meticulously synchronized to capture ...
- **p. 4 / III. S3E DATASET - extractive body cue:** Teaching Building and Tunnel: Poor lighting and similar geometric structures challenge robustness in maintaining
- **p. 4 / III. S3E DATASET - extractive body cue:** Each paradigm is meticulously crafted to offer a robust framework for assessing C-SLAM algorithms across a multitude of real-world collaborative robotic applications.
- **p. 5 / III. S3E DATASET - extractive body cue:** This diversity is crucial for evaluating C-SLAM performance, adaptability, and robustness, which are key for advancing collaborative robotic navigation and mapping technologies.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** However, in areas with limited overlap, reducing drift remained a challenge. - The incorporation of UWB measurements in CoLRIO significantly improved localization robustness and accuracy, ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (Abstract), p. 4 (III. S3E DATASET), p. 2 (3 UGVs), p. 1 (C OLLABORATIVE Simultaneous Localization and Map)이다.
