# Colored Noise in PPO: Improved Exploration and Performance through Correlated Action Sampling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

PPO의 시간적으로 독립적인 action noise가 탐색 trajectory의 구조를 놓칠 수 있다.

## Bottleneck and Changed Formulation

시간 상관을 갖는 colored noise로 stochastic action sampling을 바꾸고 noise color와 병렬 환경 수의 영향을 비교한다.

## System and Robotics Loop

On-policy stochastic actor의 action sampling을 바꾼다. VLA나 양팔 관계 학습을 직접 제안한 것은 아니다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

행동 likelihood와 trajectory correlation·noise 재사용·seed/환경 수.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

On-policy RL의 correlated/white noise와 병렬 data 수집 조건을 비교한다. 이 조사에서 실제 로봇 trial은 확인하지 않았다.

## Evidence Anchor

[공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/29139) · [저자 project/code](https://github.com/jkbjh/cn-ppo-paper-code). Exact objective, constraints, success definition은 본문 수동 확인 필요.
