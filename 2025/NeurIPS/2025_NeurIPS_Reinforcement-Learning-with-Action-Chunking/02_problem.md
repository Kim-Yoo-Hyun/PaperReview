# Reinforcement Learning with Action Chunking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Offline demonstration을 online RL exploration에 활용하면서 long-horizon sparse-reward 문제의 value backup을 개선하는 문제다.

## Bottleneck and Changed Formulation

Chunked action space에서 RL을 수행하여 시간적으로 일관된 exploration과 n-step TD backup을 결합한다.

## System and Robotics Loop

State → action chunk → 여러 환경 step 실행; critic도 action sequence를 평가한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Chunk 실행 중 feedback 처리, n-step target 조건과 exploration budget.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 abstract는 long-horizon sparse-reward manipulation task에서 offline 성능과 online sample efficiency를 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/50348e8f9aef984abe0ea1ec2a326f78-Abstract-Conference.html) · [저자 project/code](https://github.com/ColinQiyangLi/qc). Exact objective, constraints, success definition은 본문 수동 확인 필요.
