# When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

BC에서 online RL로 전환할 때 기존의 좋은 행동을 잃을 수 있다.

## Bottleneck and Changed Formulation

BC로부터 Q를 추정하고 BC·RL 행동을 가치에 따라 선택하며 online 학습한다.

## System and Robotics Loop

BC 정책·학습 정책 → Q-Gating → 실제 상호작용·RL 갱신.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Q 초기화에 필요한 상호작용, 두 정책 유지 비용, gating의 행동 분포 변화.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

D4RL·robomimic과 실제 pipe assembly·kitting을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p153.html) · [저자 project/code](https://pages.rai-inst.com/q2rl_website/) · [공식 code](https://github.com/rai-opensource/q2rl). Exact objective, constraints, success definition은 본문 수동 확인 필요.
