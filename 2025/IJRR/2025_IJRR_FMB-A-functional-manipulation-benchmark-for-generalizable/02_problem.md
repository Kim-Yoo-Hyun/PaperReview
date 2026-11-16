# FMB: A functional manipulation benchmark for generalizable robotic learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

접촉이 복잡한 개별 조작과 장시간 skill 조합을 재현 가능한 조건에서 함께 평가해야 한다.

## Bottleneck and Changed Formulation

복제 가능한 3D 프린트 물체·조립 과제와 imitation baseline을 구성한다.

## System and Robotics Loop

물체/로봇 관측 → grasp·reorientation·assembly skill → 다단계 조립.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

skill/전체 과제 성공 정의, object split, reset과 force/torque 접근.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실로봇의 개별 skill과 조합 과제를 평가하는 데이터·CAD·정책 자산을 제공한다.

## Evidence Anchor

[공식 paper/abstract](https://journals.sagepub.com/doi/full/10.1177/02783649241276017) · [저자 project/code](https://functional-manipulation-benchmark.github.io/) · [공식 code](https://github.com/rail-berkeley/fmb). Exact objective, constraints, success definition은 본문 수동 확인 필요.
