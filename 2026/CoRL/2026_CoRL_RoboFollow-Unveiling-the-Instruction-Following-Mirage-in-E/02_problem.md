# RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Robot policy의 높은 성공률이 지시 이해를 과대평가할 수 있다.

## Bottleneck and Changed Formulation

같은 scene의 여러 지시 등으로 instruction following을 단계별 평가한다.

## System and Robotics Loop

Scene·다양한 instruction → policy rollout → intent/execution 판정.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

scene entropy, evaluator oracle, task infeasibility, real-robot coverage.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation benchmark와 제한된 실제 검증을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/forum?id=A9AQjk3dAt) · [저자 project/code](https://github.com/AutoLab-SAI-SJTU/RoboFollow). Exact objective, constraints, success definition은 본문 수동 확인 필요.
