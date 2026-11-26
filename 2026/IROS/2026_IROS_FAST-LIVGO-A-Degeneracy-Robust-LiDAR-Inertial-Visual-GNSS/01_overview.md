# FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2606.19190.
> PDF retrieval source: https://arxiv.org/pdf/2606.19190. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / IROS
- Authors: Zhiyu Chen, Chunran Zheng, Jiayu Wen, XiaoLei Zhang, Jiaming Xu, Feng Pan, Yukang Cui
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, sensor fusion, LiDAR-inertial odometry
- Official paper: https://arxiv.org/abs/2606.19190
- Full-text retrieval: https://arxiv.org/pdf/2606.19190
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://arxiv.org/pdf/2606.19190v2)

## Why This Paper Is Here

FAST-LIVGO는 LiDAR·관성·영상·GNSS를 오차 상태 필터에 결합해 일부 센서 관측의 기하 정보가 약한 구간에서도 궤적을 추정한다. [PDF 1쪽](https://arxiv.org/pdf/2606.19190v2#page=1) · [PDF 3쪽](https://arxiv.org/pdf/2606.19190v2#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robust state estimation and mapping in long-term, large-scale, and highly dynamic environments remains a key challenge in robotics.
- **p. 1 / Abstract - extractive body cue:** Existing LiDAR-Inertial-Visual Odometry (LIVO) systems achieve strong local accuracy but suffer from accumulated drift over long distances and may fail in geometrically degraded or textureless ...
- **p. 1 / Abstract - extractive body cue:** Meanwhile, GNSS-aided fusion frameworks often rely on LiDAR or visual odometry for state prediction and outlier rejection, making them vulnerable when odometry degenerates.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose a tightly coupled LiDAR-Inertial-Visual-GNSS fusion framework based on an Error-State Iterated Kalman Filter.
- **p. 1 / Abstract - extractive body cue:** An online spatiotemporal alignment module using Dynamic Time Warping is introduced for highly dynamic conditions.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, in large-scale field missions or high-speed Unmanned Aerial Vehicle (UAV) flights, pure LIVO systems still face critical limitations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Existing loosely-coupled schemes underutilize the high precision of GNSS carrier phases, while traditional tightly-coupled frameworks lack adaptive integrity monitoring under alternating LIVO and GNSS degradation.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these issues, we propose a tightly-coupled multi-sensor fusion system formulated within an Error-State Iterated Kalman Filter (ESIKF), aiming at globally consistent mapping in ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** The processing pipeline consists of two main modules: LIVO Update: Adopting the FAST-LIVO2 strategy, this module sequentially updates the state using camera photometric residuals and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The main contributions are summarized as follows: • A tightly-coupled LiDAR-Inertial-Visual-GNSS fusion framework based on ESIKF.
- **p. 3 / III. METHODOLOGY - extractive body cue:** The resulting optimal time lag δtrI is then compensated when utilizing GNSS observations.
- **p. 2 / III. METHODOLOGY - extractive body cue:** Notation and State Transition Model We define the full system state vector x in continuous time as an element of the manifold M.
- **p. 3 / III. METHODOLOGY - extractive body cue:** We construct the following objective function to solve for the

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 라이다 스캔, 카메라, IMU와 GNSS |
| 표현 | 오차 상태를 추정하는 필터와 국소 지도 |
| 출력 | 보정한 센서 플랫폼의 자세와 위치 |
| 평가 | 벤치마크 및 실물 수집 데이터의 궤적 오차 |

[방법 3쪽](https://arxiv.org/pdf/2606.19190v2#page=3) · [평가 7쪽](https://arxiv.org/pdf/2606.19190v2#page=7)

## Main Claims and Actual Contribution

- 동적 시간 정합으로 센서 정보를 맞추고 도플러와 고정 기준점의 시간 차분 반송파 위상을 관측식으로 사용한다. [PDF 3쪽](https://arxiv.org/pdf/2606.19190v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2606.19190v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2606.19190v2#page=5)
- LiDAR·관성·시각 추정의 퇴화 정도에 따라 이상치 제거 방식을 바꾸고, M3DGR과 자체 고정익 무인기 비행에서 궤적을 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2606.19190v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2606.19190v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2606.19190v2#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Embodiment/environment | Evaluation on Benchmark Dataset (M3DGR) We conducted standardized quantitative comparisons on the public M3DGR dataset [10], which provides RTK ground | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | We benchmarked our method against SOTA open-source systems, including LIO-SAM [8], FAST-LIVO2 [3], and LIGO [21]. | role, split, size and leakage | p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Metric | Our robust mechanism effectively filters these hidden errors to extract ultimate accuracy. | definition, denominator, direction and uncertainty | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (Figure/Table caption) |
| Baseline/ablation | Notably, although the ablation version (Ours w/o Rejection) outperforms pure FAST-LIVO2 due to GNSS integration, it remains slightly inferior to our complete version. | fair input/data/compute/action matching | p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTAL RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** In contrast, looser-coupled systems like LIO-SAM and LIGO generate meter-level errors but avoid complete failure.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Under such harsh conditions, a critical finding is that the ablation version (Ours w/o Rejection) directly suffers from trajectory divergence and system failure (marked as ...
- **p. 5 / IV. STATE ESTIMATION - extractive body cue:** When encountering feature degradation (e.g., textureless long corridors), the prior covariance bPk inflates.
- **p. 5 / IV. STATE ESTIMATION - extractive body cue:** Signals with low Carrier-to-Noise density (C/N0 <35 dB-Hz) or low elevation angles (< 15◦) are physically filtered out.
- **p. 7 / 2) High-Precision Mapping in Large-Scale Highly Dy - extractive body cue:** 2) Outdoor LIVO Degraded Scenario: In regions (a)-(c) of View 1 (Fig.
- **p. 7 / 2) High-Precision Mapping in Large-Scale Highly Dy - extractive body cue:** 1) Indoor GNSS Degraded Scenario: In the long indoor corridor (see region (d) in Fig.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (III. METHODOLOGY), p. 3 (III. METHODOLOGY)이다.

## 검색 태그 근거

오차 상태 필터가 LiDAR 점군, RGB 카메라, IMU와 GNSS를 융합한다. M3DGR에 더해 실물 고정익 무인기와 휴대형 장치로 수집한 데이터에서 궤적 오차를 평가했다. [원문 3쪽](https://arxiv.org/pdf/2606.19190v2#page=3) · [원문 7쪽](https://arxiv.org/pdf/2606.19190v2#page=7)
