# A process-centric manipulation taxonomy for the organization, classification and synthesis of tactile robot skills

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

복잡한 접촉 작업을 재사용 가능한 tactile skill로 조직할 표현이 필요하다.

## Bottleneck and Changed Formulation

전문가의 process specification을 taxonomy와 parametric tactile skill로 연결한다.

## System and Robotics Loop

공정 요구 → skill specification → policy/controller → 접촉 feedback.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

전문가 specification 비용, grasp/접촉 가정, skill 선택과 저수준 controller 기여.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

산업 응용의 여러 tactile skill과 목표 pose 교란을 실로봇에서 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://www.nature.com/articles/s42256-025-01045-3). Exact objective, constraints, success definition은 본문 수동 확인 필요.
