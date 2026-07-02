# DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_DynaRend-Learning-3D-Dynamics-via-Masked-Future-Rendering/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Despite the promise of end-to-end approaches for generalizable robotic control, the lack of abundant, diverse and high-quality robot data remains a key bottleneck.
- To address this, we leverage pretrained visual-conditioned generative models to augment target views by synthesizing novel views from existing views, reducing reliance on dense camera setups and enhancing ...
- However, these approaches mainly model dynamics in 2D and lack explicit awareness of the underlying 3D scene structure.

## Core Idea
- In this section, we present the proposed DynaRend in detail.
- In this paper, we present DynaRend, a representation learning framework that learns 3D-aware and dynamics-informed triplane features via masked reconstruction and future prediction using differentiable volumetric rendering.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We evaluate DynaRend on two challenging benchmarks, RLBench and Colosseum, as well as in real-world robotic experiments, demonstrating substantial improvements in policy success rate, generalization to environmental perturbations, ...
- We conduct simulation experiments on two challenging robotic manipulation benchmarks: RLBench and Colosseum .
- 4.1 Simulation Experiments Environmental setup.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We evaluate DynaRend on two challenging benchmarks, RLBench and Colosseum, as well as in real-world robotic experiments, demonstrating substantial improvements in policy success rate, generalization to environmental perturbations, ...
- Learning generalizable robotic manipulation policies remains a key challenge due to the scarcity of diverse real-world training data.
- In this paper, we present DynaRend, a representation learning framework that learns 3D-aware and dynamics-informed triplane features via masked reconstruction and future prediction using differentiable volumetric rendering.

## Abstract Cue
- Learning generalizable robotic manipulation policies remains a key challenge due to the scarcity of diverse real-world training data.
