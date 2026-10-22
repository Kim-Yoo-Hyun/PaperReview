# Self-Adaptive VLA for Robust Robot Deployment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

배포 시 hardware shift로 반복 실패하는 VLA를 적응시킨다.

## Bottleneck and Changed Formulation

실패 rollout context를 encoder와 AdaLN으로 주입하고 여러 trial의 token을 합친다.

## System and Robotics Loop

영상·proprioception·action history → context-conditioned action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

episode/trial 간 offset 유지, encoder 모델, expert action 보상.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

정밀 bimanual·dexterous 작업의 actuation bias와 encoder offset 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.30092) · [저자 project/code](https://icefoxzhx.github.io/self-adaptive-vla/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
