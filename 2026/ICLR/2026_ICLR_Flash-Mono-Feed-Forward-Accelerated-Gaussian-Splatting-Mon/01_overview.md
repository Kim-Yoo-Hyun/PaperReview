# Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/5fcacc84d87c97bee5baecb3fb8f6e88-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/245566. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Zicheng Zhang, Ke Wu, Xiangting Meng, Keyu Liu, Jieru Zhao, Wenchao Ding
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, SLAM, depth, 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/5fcacc84d87c97bee5baecb3fb8f6e88-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/5fcacc84d87c97bee5baecb3fb8f6e88-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Flash-Mono는 단안 영상열에서 카메라 자세와 2차원 Gaussian 표면 요소를 직접 예측하면서 장기 이동의 누적 오차를 보정한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/5fcacc84d87c97bee5baecb3fb8f6e88-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Monocular Gaussian Splatting SLAM suffers from critical limitations in time efficiency, geometric accuracy, and multi-view consistency.
- **p. 1 / ABSTRACT - extractive body cue:** These issues stem from the time-consuming Train-from-Scratch optimization and the lack of inter-frame scale consistency from single-frame geometry priors.
- **p. 1 / ABSTRACT - extractive body cue:** We contend that a feedforward paradigm, leveraging multi-frame context to predict Gaussian attributes directly, is crucial for addressing these challenges.
- **p. 1 / ABSTRACT - extractive body cue:** We present Flash-Mono, a system composed of three core modules: a feed-forward prediction frontend, a 2D Gaussian Splatting mapping backend, and an efficient hidden-state-based loop ...
- **p. 1 / ABSTRACT - extractive body cue:** We trained a recurrent feed-forward frontend model that progressively aggregates multi-frame visual features into a hidden state via cross attention and jointly predicts camera poses ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Furthermore, S3PO-GS (Cheng et al., 2025) addresses the challenges of scale drift and the lack of geometric priors commonly encountered in outdoor scenarios by introducing ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Building upon these limitations, approaches like WildGS-SLAM (Zheng et al., 2025), DepthGS (Zhao et al., 2025), and Dy3DGS-SLAM (Li et al., 2025) introduced geometry prior ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our main contributions are: • We propose a real-time (10 FPS+) monocular GS-SLAM framework that leverages a recurrent feed-forward model to predict poses ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** 4 OUR APPROACH In this section, we introduce our approach in the following order.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To overcome these challenges, we propose Flash-Mono, a monocular GS-SLAM system designed to deliver exceptional speed performance and high-quality mapping.
- **p. 6 / 1 INTRODUCTION - extractive body cue:** To address this, we introduce a novel mechanism to compute a geometric constraint between the current frame and a past frame with a single forward ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** The training objective consists of three loss components, summed over a sequence of length L.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** The model then employs two interconnected decoders that facilitate bidirectional information exchange between visual tokens Ft and the persistent hidden state Mt-1 via cross-attention.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** We then present our loop closure mechanism, which leverages the model's hidden state to enable global drift correction via Sim(3) optimization (§4.2).
- **p. 1 / ABSTRACT - extractive body cue:** We trained a recurrent feed-forward frontend model that progressively aggregates multi-frame visual features into a hidden state via cross attention and jointly predicts camera poses ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The function of model f is to jointly predict three outputs: (a) the camera pose ˆTt ∈SE(3), representing the transformation from the current camera frame to the coordinate system of the initial ... | camera/depth stream, pose, map와 language goal | p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION) |
| State/latent | function, model, jointly, predict, three, outputs, camera, pose, representing, transformation, current, frame | robot pose, free-space/semantic map와 local goal | p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 6 (1 INTRODUCTION) |
| Output/action | For each new keyframe, it takes as input the RGB image Ik, the globally optimized camera pose Tk ∈Sim(3), and the per-pixel 2DGS map ˆGk of Ik predicted by the frontend. | collision-free trajectory 또는 velocity command | p. 6 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective/outcome | The globally optimal set of poses T W ∗is found by minimizing a non-linear least-squares cost function over all constraints: T W ∗= arg min T W X (i,j)∈E | goal reach, safety, localization error와 replanning latency | p. 6 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- 순환형 전단의 은닉 상태에 여러 프레임의 특징을 모아 자세와 지도 요소를 예측하고 서브맵을 표현한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/5fcacc84d87c97bee5baecb3fb8f6e88-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/5fcacc84d87c97bee5baecb3fb8f6e88-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/5fcacc84d87c97bee5baecb3fb8f6e88-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/5fcacc84d87c97bee5baecb3fb8f6e88-Paper-Conference.pdf#page=6)
- 은닉 상태로 재방문을 탐지해 전역 유사변환을 최적화하고 궤적 오차와 지도 품질을 평가했다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/5fcacc84d87c97bee5baecb3fb8f6e88-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/5fcacc84d87c97bee5baecb3fb8f6e88-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/5fcacc84d87c97bee5baecb3fb8f6e88-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/5fcacc84d87c97bee5baecb3fb8f6e88-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (5 EXPERIMENTS), p. 1 (Figure/Table caption) |
| Embodiment/environment | 5.1 EXPERIMENTAL SETUP We evaluate our system on three challenging real-world datasets: ScanNet (Dai et al., 2017a), BundleFusion (Dai et al., 2017b), and KITTI (Geiger et al., 2012). | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Dataset/benchmark | ScanNet and BundleFusion consist of large-scale indoor scenes with motion blur and diverse lighting conditions. | role, split, size and leakage | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Metric | We evaluate tracking accuracy using Absolute Trajectory Error (ATE RMSE) and rendering quality via PSNR, SSIM, and LPIPS. | definition, denominator, direction and uncertainty | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Baseline/ablation | 5.2 TRACKING PERFORMANCE As shown in Table 1, Flash-Mono significantly outperformed all traditional and GS-SLAM baseline methods. | fair input/data/compute/action matching | p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** On KITTI, we primarily compare against S3POGS, as we encountered frequent failures while evaluating other indoor-focused GS-SLAM baselines due to the large-scale and high dynamic ...
- **p. 10 / 6 CONCLUSION - extractive body cue:** Furthermore, we introduced a novel loop closure mechanism that enables robust Sim(3) optimization to correct scale and pose drift inherent in monocular systems, leading to ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Since MonoGS and DepthGS are designed primarily for indoor scenes, they often fail under the large scale variance and dynamics in KITTI; therefore, we mainly ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Method Metric 00 05 06 07 08 28 S3PO-GS PSNR ↑ 16.65 15.64 13.55 fail 17.25 15.30 SSIM ↑ 0.5409 0.5320 0.4726 fail 0.5912 0.5053 ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 7: Qualitative Analysis on reconstructed ScanNet scene 0054. All baselines failed to reconstruct the scene. C MODEL SIZE AND ACCELERATION C.1 MODEL SIZE To ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 9: Case Study: Robust Relocalization Under Environmental Changes. The model gen- erates a hidden state from 8 context views captured at night (curtains closed, ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION)이다.
