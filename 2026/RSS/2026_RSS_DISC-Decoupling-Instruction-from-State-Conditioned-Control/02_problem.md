# DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

관측 shortcut 때문에 지시가 정책 행동에 반영되지 않는 문제를 다룬다.

## Bottleneck and Changed Formulation

Instruction-only hypernetwork가 task-specific visuomotor policy의 파라미터를 생성한다.

## System and Robotics Loop

언어 → policy weights; 생성된 policy는 관측 → action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

generated parameter 수, training budget, 동일 장면 통제.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO-90, Meta-World 및 동일 visual context의 실제 로봇 비교를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p147.html) · [저자 project/code](https://github.com/ReNginx/DISC). Exact objective, constraints, success definition은 본문 수동 확인 필요.
