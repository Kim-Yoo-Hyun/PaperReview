# Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA의 순차적 과제 적응에서 SFT 데이터 부담과 기존 능력 보존이 문제다.

## Bottleneck and Changed Formulation

행동 chunk의 이산 일치·연속 궤적 정렬·출력 형식 보상으로 reinforcement fine-tuning한다.

## System and Robotics Loop

관측·지시 → 행동 chunk; 참조 행동과의 일치도가 학습 보상.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

참조 궤적 의존성, rehearsal 여부, 순차 task order, 보상별 효과.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

SimplerEnv·LIBERO 및 실제 조작, LIBERO continual learning을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p086.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
