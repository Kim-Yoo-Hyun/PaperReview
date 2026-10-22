# ReViP: Mitigating False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

실제 목표가 달성되지 않았는데 완료 동작을 이어 가는 false completion을 다룬다.

## Bottleneck and Changed Formulation

시각적 task-stage cue로 vision–proprioception 결합을 조정한다.

## System and Robotics Loop

영상·언어·state와 stage cue → corrective action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

arXiv v3와 최신 project 방법 차이, observer latency, 공개 코드.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Object Drop, Distractor Swap, Relayout 및 robot manipulation 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2601.16667) · [저자 project/code](https://isee-laboratory.github.io/ReViP/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
