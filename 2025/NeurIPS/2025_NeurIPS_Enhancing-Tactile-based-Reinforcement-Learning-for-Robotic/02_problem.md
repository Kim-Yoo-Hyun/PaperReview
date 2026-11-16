# Enhancing Tactile-based Reinforcement Learning for Robotic Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

접촉 정보를 추가해도 RL이 이를 안정적으로 활용하지 못하며 proprioception만으로 놓치는 물체 움직임이 있다.

## Bottleneck and Changed Formulation

희소 이진 접촉·proprioception 표현을 self-supervised learning으로 학습하고 SSL memory와 on-policy memory의 분리를 검토한다.

## System and Robotics Loop

Binary contact·proprioception → 표현/memory → contact-rich control.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

센서 노이즈·빈도, sim contact의 현실성, 실물 센서 전이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RoTO 시뮬레이션의 공 튀기기·Baoding 회전 등 dexterity를 평가한다. 실로봇 결과로 확대하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html) · [저자 project/code](https://elle-miller.github.io/tactile_rl/) · [공식 code](https://github.com/elle-miller/roto). Exact objective, constraints, success definition은 본문 수동 확인 필요.
