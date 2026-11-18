# Guiding real-world reinforcement learning for in-contact manipulation tasks with Shared Control Templates

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

접촉 과제의 자유로운 RL 탐색은 많은 실제 상호작용과 위험한 동작을 요구한다.

## Bottleneck and Changed Formulation

물체 관계·task geometry의 알려진 제약을 shared-control template으로 표현해 RL이 탐색하는 차원을 줄인다.

## System and Robotics Loop

Template가 제한한 state/action 공간에서 unknown task knowledge를 학습한다. 단일 VLA 내부의 learned exploration은 아니다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

수동 task constraint·phase 전환·안전 보증 전제·reward 정보.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

7-DoF 실제 로봇의 pouring·grid-clamp placement를 다룬다. 논문의 안전 주장 조건을 보편적 보증으로 일반화하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/article/10.1007/s10514-024-10164-6). Exact objective, constraints, success definition은 본문 수동 확인 필요.
