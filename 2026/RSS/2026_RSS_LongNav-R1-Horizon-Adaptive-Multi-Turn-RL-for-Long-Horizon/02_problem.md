# LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

긴 항법 episode에서 단일 턴 학습은 시간적 credit assignment를 충분히 다루기 어렵다.

## Bottleneck and Changed Formulation

환경과의 multi-turn 상호작용 및 horizon을 반영한 advantage 추정으로 VLA를 학습한다.

## System and Robotics Loop

시각 관측·상호작용 이력 → 항법 의사결정 → 환경 피드백.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

action 단위, episode 길이별 정규화, rollout 분모, 실제 로봇의 저수준 제어기.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Object navigation과 실제 장기 항법의 zero-shot 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p068.html) · [저자 project/code](https://github.com/UMich-CURLY/LongNav-R1). Exact objective, constraints, success definition은 본문 수동 확인 필요.
