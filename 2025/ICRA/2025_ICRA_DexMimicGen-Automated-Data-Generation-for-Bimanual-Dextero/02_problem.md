# DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

양팔·다지 손의 동시 조작 시연 수집 비용이 크다.

## Bottleneck and Changed Formulation

소수 인간 시연을 재사용해 시뮬레이션의 양팔 dexterous trajectory를 생성한다.

## System and Robotics Loop

source demonstration·새 초기 상태 → 합성 trajectory → imitation policy.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

object-state/segmentation 접근, source-target task 대응, 생성 실패 및 sim-to-real 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

양팔 조작 simulation과 real2sim2real 사례를 제시한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2410.24185) · [저자 project/code](https://dexmimicgen.github.io/) · [공식 code](https://github.com/NVlabs/dexmimicgen). Exact objective, constraints, success definition은 본문 수동 확인 필요.
