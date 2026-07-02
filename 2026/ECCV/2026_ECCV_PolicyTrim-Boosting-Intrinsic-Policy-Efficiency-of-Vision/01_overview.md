# PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models

- Year/Venue: 2026 / ECCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2026/ECCV/2026_ECCV_PolicyTrim-Boosting-Intrinsic-Policy-Efficiency-of-Vision/paper.pdf
- Code/Project: https://inceptionwang.github.io/PolicyTrim/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Task ID Task ID (a) Step Count Across Tasks (Left: Baseline, Right: Ours) Misalignment Start Grasp Failure Step Success Rate X.
- While existing efforts predominantly focus on compute-centric efficiency to reduce per-step inference latency, the intrinsic policy efficiency of these models remains largely unexplored.
- Vision-Language-Action (VLA) models provide a unified paradigm for robotic manipulation, yet their real-world deployment is often bottlenecked by execution efficiency.

## Core Idea
- We propose a two-stage posttraining framework that extends the executable action horizon per inference and reduces the number of steps required to complete a task for VLA models.
- To address this, we propose PolicyTrim, a reinforcement learning-based post-training framework that extends the reliable action chunk length and reduces redundant physical steps.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments across three benchmarks and three VLA models demonstrate that PolicyTrim improves action chunk utilization by 3× and reduces physical execution steps by 51.4%.
- These results suggest that our efficiency gains arise from a fundamentally improved execution strategy rather than any sacrifice in task competence.
- The consistent improvements across diverse physical simulators, action spaces, and model architectures demonstrate that PolicyTrim generalizes well beyond the LIBERO benchmark, confirming that policy efficiency optimization yields substantial ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments across three benchmarks and three VLA models demonstrate that PolicyTrim improves action chunk utilization by 3× and reduces physical execution steps by 51.4%.
- To address this, we propose PolicyTrim, a reinforcement learning-based post-training framework that extends the reliable action chunk length and reduces redundant physical steps.
- While existing efforts predominantly focus on compute-centric efficiency to reduce per-step inference latency, the intrinsic policy efficiency of these models remains largely unexplored.

## Abstract Cue
- Vision-Language-Action (VLA) models provide a unified paradigm for robotic manipulation, yet their real-world deployment is often bottlenecked by execution efficiency.
