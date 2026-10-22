# How Should Vision-Language-Action Models Use Proprioceptive State?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA에 state를 어디에, 얼마나 긴 history로 넣어야 하는지 비교한다.

## Bottleneck and Changed Formulation

같은 flow-matching backbone에서 다섯 state interface와 history 길이를 통제한다.

## System and Robotics Loop

언어·영상·state/history → action chunk.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

world-frame localization 포함 여부, native state 사용, checkpoint 공개.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

45 atomic 및 20 composite task 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2608.03052) · [저자 project/code](https://arxiv.org/abs/2608.03052). Exact objective, constraints, success definition은 본문 수동 확인 필요.
