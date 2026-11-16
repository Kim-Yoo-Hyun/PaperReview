# ForceRFT: Refining VLA Actions through Force-Guided Residual Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

시연 기반 force VLA의 복구 coverage와 task return 최적화 부족을 다룬다.

## Bottleneck and Changed Formulation

Frozen SmolVLA prior의 동작을 wrist-feedback residual RL로 보정하며 human correction과 autonomous TD를 분리한다.

## System and Robotics Loop

Wrist wrench·변화량·base motion → pose residual; critic은 autonomous 구간을 사용한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

개입 경계, 데이터 예산, force 관측 주기와 base chunk 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실제 plug·ring-on-peg·wiping에서 residual imitation을 포함한 기준선과 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.22840). Exact objective, constraints, success definition은 본문 수동 확인 필요.
