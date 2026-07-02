# Problem

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Illustration of the Out-of-Vision (OOV) limitation in existing VLA models.
- SOMA addresses this limitation by equipping VLAs with a persistent, spatial memory constructed from multi-view observations acquired via a movable head camera, enabling reasoning beyond the current visual ...
- Most existing VLAs implicitly assume that task-relevant objects are always visible, leading to brittle and reactive behaviors when targets fall outside the camera’s field of view.

## 해결하려는 문제
- Experiment results show that SOMA not only improves task success rates, but also induces qualitatively different manipulation behaviors, with faster target localization, reduced viewpoint search, and near one-shot ...
- Head Camera We introduce SOMA, the Spatial memory framework for Out-of-Vision Manipulation in VisionLanguage-Action (VLA) models.
- The framework consists of three components: Spatial Memory Construction for aggregating angular-wise observations into a unified spatial–semantic representation by scanning, Dynamic Memory Refinement for maintaining global consistency over ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
