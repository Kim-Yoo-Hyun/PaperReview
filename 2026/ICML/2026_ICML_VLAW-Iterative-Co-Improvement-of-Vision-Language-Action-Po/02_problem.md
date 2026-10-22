# VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Demonstration 중심으로 학습한 world model은 실패 interaction과 작은 contact detail을 충분히 표현하지 못해 policy improvement에 제약이 생긴다.

## Bottleneck and Changed Formulation

실제 rollout으로 action-conditioned video world model을 개선하고 그 synthetic rollout으로 VLA를 개선하는 반복 학습을 제안한다.

## System and Robotics Loop

VLA action-conditioned video model → synthetic rollout; real rollout → world-model update → policy update.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Policy update objective, 실패 data 구성, synthetic/real 혼합비와 evaluation leakage.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

ICML abstract는 실제 robot의 여러 downstream task에서 base policy 및 synthetic-rollout 학습 효과를 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/guo26i.html) · [저자 project/code](https://sites.google.com/view/vla-w). Exact objective, constraints, success definition은 본문 수동 확인 필요.
