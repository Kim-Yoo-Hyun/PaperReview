# Method

- Year/Venue: 2026 / ECCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2026/ECCV/2026_ECCV_PolicyTrim-Boosting-Intrinsic-Policy-Efficiency-of-Vision/paper.pdf
- Code/Project: https://inceptionwang.github.io/PolicyTrim/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose a two-stage posttraining framework that extends the executable action horizon per inference and reduces the number of steps required to complete a task for VLA models.
- To address this, we propose PolicyTrim, a reinforcement learning-based post-training framework that extends the reliable action chunk length and reduces redundant physical steps.
- This paper introduces PolicyTrim, an RL-based post-training framework designed to enhance policy efficiency.

## 원리적 동기
- Task ID Task ID (a) Step Count Across Tasks (Left: Baseline, Right: Ours) Misalignment Start Grasp Failure Step Success Rate X.
- While existing efforts predominantly focus on compute-centric efficiency to reduce per-step inference latency, the intrinsic policy efficiency of these models remains largely unexplored.
- We propose a two-stage posttraining framework that extends the executable action horizon per inference and reduces the number of steps required to complete a task for VLA models.

## 핵심 방법론
- We propose a two-stage posttraining framework that extends the executable action horizon per inference and reduces the number of steps required to complete a task for VLA models.
- This paper introduces PolicyTrim, an RL-based post-training framework designed to enhance policy efficiency.
