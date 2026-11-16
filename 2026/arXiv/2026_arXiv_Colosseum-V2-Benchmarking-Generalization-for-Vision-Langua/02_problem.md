# Colosseum V2: Benchmarking Generalization for Vision Language Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA의 perception 일반화가 여러 robot morphology에서 행동 일반화로 이어지는지 점검해야 한다.

## Bottleneck and Changed Formulation

ManiSkill 기반 다중 morphology task로 in/out-of-domain policy 평가를 구성한다.

## System and Robotics Loop

Task·robot morphology·분포 변화 → ACT/π0.5 등 policy → task 성능.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

morphology별 action/control 정렬, task split과 simulator-real 대응.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

28 task·두 robot morphology와 simulation/real-world 지표 상관을 abstract에서 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2605.27759). Exact objective, constraints, success definition은 본문 수동 확인 필요.
