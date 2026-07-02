# Problem

- Year/Venue: 2026 / ECCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2026/ECCV/2026_ECCV_PolicyTrim-Boosting-Intrinsic-Policy-Efficiency-of-Vision/paper.pdf
- Code/Project: https://inceptionwang.github.io/PolicyTrim/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Task ID Task ID (a) Step Count Across Tasks (Left: Baseline, Right: Ours) Misalignment Start Grasp Failure Step Success Rate X.
- While existing efforts predominantly focus on compute-centric efficiency to reduce per-step inference latency, the intrinsic policy efficiency of these models remains largely unexplored.
- Vision-Language-Action (VLA) models provide a unified paradigm for robotic manipulation, yet their real-world deployment is often bottlenecked by execution efficiency.

## 해결하려는 문제
- Extensive experiments across three benchmarks and three VLA models demonstrate that PolicyTrim improves action chunk utilization by 3× and reduces physical execution steps by 51.4%.
- To address this, we propose PolicyTrim, a reinforcement learning-based post-training framework that extends the reliable action chunk length and reduces redundant physical steps.
- While existing efforts predominantly focus on compute-centric efficiency to reduce per-step inference latency, the intrinsic policy efficiency of these models remains largely unexplored.

## 선행 연구 / 배경 단서
- Task ID Task ID (a) Step Count Across Tasks (Left: Baseline, Right: Ours) Misalignment Start Grasp Failure Step Success Rate X.
