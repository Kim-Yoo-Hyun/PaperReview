# VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

다양한 저수준 도구를 long-horizon 언어 계획에 연결한다.

## Bottleneck and Changed Formulation

VLM orchestrator가 interruptible VLA/WAM·perception/action 도구를 조정한다.

## System and Robotics Loop

언어·영상·도구 결과 → skill 호출/중단 → action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

tool별 privileged input, interrupt semantics, checkpoint·evaluator 공개.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RoboVoLo와 실제 open-vocabulary long-horizon manipulation 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/forum?id=sF3YZbbTNX) · [저자 project/code](https://chicychen.github.io/VoLo/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
