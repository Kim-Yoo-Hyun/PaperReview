# Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

시간에 따라 memory를 채우는 정책이 대기 시간을 실제 과제 진행으로 오인할 수 있다.

## Bottleneck and Changed Formulation

무효 pause/fidget과 memory/timestamp 대조로 temporal shortcut을 진단하고 event-indexed memory를 비교한다.

## System and Robotics Loop

관측 memory·시간/사건 index → VLA 행동 → 반복 조작과 종료 판단.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

event 기준의 관측 접근권·counting task 외 전이·제어 개입과 memory 효과의 분리.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RoboMME counting task에서 무효 사건·시간표식·memory 입력을 통제해 성공 변화를 측정한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2611.14488) · [저자 project/code](https://github.com/bennidict23/memory-clock). Exact objective, constraints, success definition은 본문 수동 확인 필요.
