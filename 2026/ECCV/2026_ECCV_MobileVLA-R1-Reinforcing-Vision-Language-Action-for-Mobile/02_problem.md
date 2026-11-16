# MobileVLA-R1: Reinforcing Vision-Language-Action for Mobile Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

모바일 로봇의 언어 추론과 실행 가능한 제어를 정합시키기 어렵다.

## Bottleneck and Changed Formulation

구조화 CoT alignment 뒤 GRPO RL로 추론·제어 일관성을 학습한다.

## System and Robotics Loop

영상·지시 → reasoning과 navigation command/control output → quadruped execution. 출력 형식을 low-level motor torque와 혼동하지 않는다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

속도·이산 행동 output 형식, low-level controller 고정 여부, 2.0 코드와 원 논문 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

VLN·VLA benchmark와 실제 사족 로봇 배포를 보고한다. MobileVLA-R1 2.0의 추가 주장은 포함하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2511.17889) · [저자 project/code](https://aigeeksgroup.github.io/MobileVLA-R1/) · [공식 code](https://github.com/AIGeeksGroup/MobileVLA-R1). Exact objective, constraints, success definition은 본문 수동 확인 필요.
