# FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation Under Uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

물체 pose·동역학 불확실성 아래 힘을 제한하면서 조립해야 한다.

## Bottleneck and Changed Formulation

Force threshold와 dynamics randomization으로 sim-to-real 접촉 정책을 학습하고 성공을 예측한다.

## System and Robotics Loop

관측·허용 force 조건 → 접촉 동작·성공 예측.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

pose uncertainty 범위, gain randomization, 독립 실환경 trials.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

삽입·gear meshing·nut threading과 snap-fit/다단계 조립을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/10925874/) · [저자 project/code](https://noseworm.github.io/forge/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
