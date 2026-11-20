# TacCoRL: Integrating Tactile Feedback into VLA via Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

시각 VLA가 놓치는 접촉 상태와 시연에 드문 실패 근방 행동을 학습한다.

## Bottleneck and Changed Formulation

촉각 VLA를 sim-real co-training으로 초기화하고 simulation RL과 실환경 supervised anchor로 개선한다.

## System and Robotics Loop

영상·언어·촉각 → VLA 행동; 배포 시 privileged simulation state를 쓰지 않는다고 보고한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

촉각 합성 정합성, real anchor 비용, 물리 변화별 분할.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실제 양팔 접촉 과제로 전이를 평가한다. 실제 로봇 online RL을 사용한 결과와 구별한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2606.11743) · [저자 project/code](https://tac-corl.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
