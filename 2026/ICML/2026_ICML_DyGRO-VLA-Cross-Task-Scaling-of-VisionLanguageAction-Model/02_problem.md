# DyGRO-VLA: Cross-Task Scaling of Vision–Language–Action Models via Dynamic Grouped Residual Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Task별 RL fine-tuning이 pretrained VLA를 좁은 task에 과적합시켜 cross-task 일반성을 훼손하는 문제다.

## Bottleneck and Changed Formulation

Cross-task latent representation과 mixture-of-RL-residuals를 이용한 두 단계 grouped residual optimization을 제안한다.

## System and Robotics Loop

VLA observation/language → cross-task latent features 및 residual policy update → robot action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Task grouping, residual routing, representation loss와 unseen split leakage.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

ICML abstract는 LIBERO, RoboTwin2와 real-world 평가 및 multitask/distribution-shift 조건을 명시한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/lin26af.html) · [저자 project/code](https://github.com/EDEM-AI/DyGRO-VLA). Exact objective, constraints, success definition은 본문 수동 확인 필요.
