# ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

새 언어 과제마다 보상 설계나 시연을 다시 확보하는 비용이 크다.

## Bottleneck and Changed Formulation

소규모 시연으로 언어 조건부 reward와 offline 정책을 학습하고 새 과제에 online 적응한다.

## System and Robotics Loop

영상·지시 → 학습 보상 → offline pretraining·online policy update.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

사전학습 시연·외부 데이터 사용량, reward leakage, 신규 과제별 인간 감독.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 실제 양팔 조작의 미관측 과제 적응을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/zhang25a.html) · [저자 project/code](https://rewind-reward.github.io/) · [공식 code](https://github.com/rewind-reward/ReWiND). Exact objective, constraints, success definition은 본문 수동 확인 필요.
