# CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

로봇별 동역학 차이와 다봉 행동 분포 때문에 항법 정책 전이가 어렵다.

## Bottleneck and Changed Formulation

Planner 데이터로 embodiment-agnostic flow expert를 학습하고 이를 고정한 채 로봇별 경량 refiner를 online RL로 적응한다.

## System and Robotics Loop

기하 행동 prior → dynamics-aware refiner → 로봇 제어. 언어 VLA나 단일 공동 갱신 정책과 구분한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

planner 관측 접근, dynamics별 상호작용 분모, morphology별 평가 조건.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

사족·이족·quadrotor 실험과 실제 배포를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/514bdfb12b318ad02c6f28dc68f2feea-Abstract-Conference.html) · [저자 project/code](https://github.com/amap-cvlab/CE-Nav). Exact objective, constraints, success definition은 본문 수동 확인 필요.
