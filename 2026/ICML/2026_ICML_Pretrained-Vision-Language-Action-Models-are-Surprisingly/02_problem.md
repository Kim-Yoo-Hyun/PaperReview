# Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA 순차 학습에서 기존 능력이 얼마나 보존되는가.

## Bottleneck and Changed Formulation

사전학습과 소량 experience replay의 망각 억제 효과를 분석한다.

## System and Robotics Loop

사전학습 VLA → 새 task fine-tuning/replay → robot action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

pretraining 중복, replay 비율, old-task 평가와 모듈별 동결.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

순차 robot task의 학습·망각 비교를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/liu26bu.html) · [저자 project/code](https://continual-vlas.github.io/forget-me-not/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
