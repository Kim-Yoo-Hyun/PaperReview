# Problem

- Year/Venue: 2025 / NeurIPS spotlight
- Category: 3D Representation Learning and Foundation Models
- Tags: 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_EAG3R-Event-Augmented-3D-Geometry-Estimation-for-Dynamic-a/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Estimating geometry from videos or images is a fundamental problem in 3D vision, with broad applications in camera pose estimation, novel view synthesis, geometry reconstruction, and 3D perception.
- However, in real-world applications such as autonomous driving in the wild, which often involve fast motion and rapidly changing illumination, RGB cameras—dependent on long exposure times for imaging—face ...
- Prior work has leveraged event streams in 3D tasks such as depth estimation , surface reconstruction , 39th Conference on Neural Information Processing Systems (NeurIPS 2025).

## 해결하려는 문제
- Extensive experiments demonstrate that EAG3R significantly outperforms state-of-the-art RGB-only baselines across monocular depth estimation, camera pose tracking, and dynamic reconstruction tasks.
- Our method enables robust geometry estimation in challenging dynamic low-light scenes without requiring retraining on night-time data.
- In this paper, we propose EAG3R, a novel geometry estimation framework that augments pointmap-based reconstruction with asynchronous event streams.

## 선행 연구 / 배경 단서
- Our main contributions are as follows: • We propose EAG3R, the first event-augmented pointmap-based geometry estimation framework, which integrates asynchronous event streams with RGB-based reconstruction to handle dynamic ...
- Estimating geometry from videos or images is a fundamental problem in 3D vision, with broad applications in camera pose estimation, novel view synthesis, geometry reconstruction, and 3D perception.
- However, in real-world applications such as autonomous driving in the wild, which often involve fast motion and rapidly changing illumination, RGB cameras—dependent on long exposure times for imaging—face ...
