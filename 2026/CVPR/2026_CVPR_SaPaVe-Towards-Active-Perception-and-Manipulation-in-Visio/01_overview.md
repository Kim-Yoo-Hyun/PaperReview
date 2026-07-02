# SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics

- Year/Venue: 2026 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, active perception, Robotics
- Paper link: ./2026/CVPR/2026_CVPR_SaPaVe-Towards-Active-Perception-and-Manipulation-in-Visio/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing methods struggle to unify semantic-driven perception actively with robust, viewpoint-invariant execution accordingly.

## Core Idea
- We compare our method against several strong baselines: (1) In the first experiment, we compare our model with current powerful VLM, including the general models (e.g., Qwen2.5-VL-72B , ...
- To this end, we propose SaPaVe, an end-to-end framework that jointly learns these capabilities in a data-efficient manner.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments in both simulation and real-world settings show that SaPaVe outperforms recent VLA models such as GR00T N1 and π0 , achieving up to 31.25% higher success ...
- Our results show that tightly coupled perception and execution, when trained with decoupled yet coordinated strategies, enable efficient and generalizable active manipulation.
- To support this, we introduce ActiveViewPose-200K, comprising 200k image-language-camera movement pairs for semantic camera movement learning, and a 3D geometry-aware module that improves execution robustness under dynamic viewpoints.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To support this, we introduce ActiveViewPose-200K, comprising 200k image-language-camera movement pairs for semantic camera movement learning, and a 3D geometry-aware module that improves execution robustness under dynamic viewpoints.
- Extensive experiments in both simulation and real-world settings show that SaPaVe outperforms recent VLA models such as GR00T N1 and π0 , achieving up to 31.25% higher success ...
- To this end, we propose SaPaVe, an end-to-end framework that jointly learns these capabilities in a data-efficient manner.

## Abstract Cue
- Active perception and manipulation are crucial for robots to interact with complex scenes.
