# EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes

- Year/Venue: 2025 / NeurIPS spotlight
- Category: 3D Representation Learning and Foundation Models
- Tags: 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_EAG3R-Event-Augmented-3D-Geometry-Estimation-for-Dynamic-a/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Estimating geometry from videos or images is a fundamental problem in 3D vision, with broad applications in camera pose estimation, novel view synthesis, geometry reconstruction, and 3D perception.
- However, in real-world applications such as autonomous driving in the wild, which often involve fast motion and rapidly changing illumination, RGB cameras—dependent on long exposure times for imaging—face ...
- Prior work has leveraged event streams in 3D tasks such as depth estimation , surface reconstruction , 39th Conference on Neural Information Processing Systems (NeurIPS 2025).

## Core Idea
- Our method enables robust geometry estimation in challenging dynamic low-light scenes without requiring retraining on night-time data.
- In this paper, we propose EAG3R, a novel geometry estimation framework that augments pointmap-based reconstruction with asynchronous event streams.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that EAG3R significantly outperforms state-of-the-art RGB-only baselines across monocular depth estimation, camera pose tracking, and dynamic reconstruction tasks.
- We compare EAG3R with state-of-the-art pose free learning-based reconstruction method, including DUSt3R , MonST3R , and Easi3R .
- We report results using standard metrics: Absolute Relative Error (Abs Rel ↓), Scale-invariant RMSE log (RMSE log ↓), and the threshold accuracy δ < 1.25 (↑), where lower ...

## Limitation
- We discuss limitations and broader impact in the appendix.

## Contribution
- Extensive experiments demonstrate that EAG3R significantly outperforms state-of-the-art RGB-only baselines across monocular depth estimation, camera pose tracking, and dynamic reconstruction tasks.
- Our method enables robust geometry estimation in challenging dynamic low-light scenes without requiring retraining on night-time data.
- In this paper, we propose EAG3R, a novel geometry estimation framework that augments pointmap-based reconstruction with asynchronous event streams.

## Abstract Cue
- Robust 3D geometry estimation from videos is critical for applications such as autonomous navigation, SLAM, and 3D scene reconstruction.
