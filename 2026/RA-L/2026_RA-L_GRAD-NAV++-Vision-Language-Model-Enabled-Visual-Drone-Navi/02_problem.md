# GRAD-NAV++: Vision-Language Model Enabled Visual Drone Navigation With Gaussian Radiance Fields and Differentiable Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

언어 목표를 드론의 시각 기반 저수준 제어로 연결하면서 효율적으로 학습해야 한다.

## Bottleneck and Changed Formulation

Gaussian radiance field와 differentiable dynamics를 이용한 학습에 VLM·mixture-of-experts를 결합한다.

## System and Robotics Loop

시각·언어 → VLA navigation/control; rendering과 dynamics gradient를 학습에 활용한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

언어 encoder·MoE 갱신 범위, dynamics model 오차, 이전 GRaD-Nav 대비 새 평가 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 실제 드론의 언어 조건부 navigation을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/11297793/) · [저자 project/code](https://qianzhong-chen.github.io/gradnavpp.github.io/) · [공식 code](https://github.com/Qianzhong-Chen/grad_nav). Exact objective, constraints, success definition은 본문 수동 확인 필요.
