# Strengthening Generative Robot Policies through Predictive World Modeling

- Year/Venue: 2025 / RA-L
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, diffusion policy, model-based planning, contact-rich manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://computationalrobotics.seas.harvard.edu/GPC/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Lacking explicit mechanisms for test-time correction or recovery, small deviations from the training distribution can compound over time and degrade performance .

## Core Idea
- —We present generative predictive control (GPC), a framework for inference-time enhancement of pretrained behavior-cloning policies.
- During evaluation, we use 100 action candidates for all baselines.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Across diverse robotic manipulation tasks—state- and visionbased, in simulation and on real hardware—GPC consistently outperforms standard behavior cloning and compares favorably to other inference-time adaptation baselines.
- While MPC-style planning has demonstrated robustness across robotics and control, it typically relies on carefully engineered models and objectives, making direct integration with modern generative policies challenging.
- By contrast, model predictive control (MPC) looks ahead: it evaluates candidate actions by simulating their future consequences under a predictive dynamics model, enabling online adaptation.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Rather than retraining or fine-tuning, GPC augments a frozen diffusion policy at deployment by coupling it with a predictive world model.
- —We present generative predictive control (GPC), a framework for inference-time enhancement of pretrained behavior-cloning policies.
- Lacking explicit mechanisms for test-time correction or recovery, small deviations from the training distribution can compound over time and degrade performance .

## Abstract Cue
- —We present generative predictive control (GPC), a framework for inference-time enhancement of pretrained behavior-cloning policies.
