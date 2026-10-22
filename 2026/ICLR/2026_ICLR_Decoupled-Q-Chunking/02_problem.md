# Decoupled Q-Chunking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Chunked critic의 빠른 value backup을 활용하면서 긴 open-loop action sequence를 학습·실행해야 하는 제약을 줄인다.

## Bottleneck and Changed Formulation

Critic이 평가하는 chunk 길이와 actor가 출력하는 chunk 길이를 분리한다.

## System and Robotics Loop

State → 짧은 actor action chunk; 긴 critic horizon을 통한 value 학습. 실제 controller frequency는 본문 확인 필요.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

부분 chunk value 추정, policy extraction objective, reactive 평가의 실제 포함 여부.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

최종 paper의 abstract와 공식 code는 장기 offline goal-conditioned task 평가를 설명한다. 실제 로봇 contact 평가 여부는 확인 필요.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/pdf/bde79a617f6c016e2c51c7771416933c0646102c.pdf) · [저자 project/code](https://github.com/ColinQiyangLi/dqc). Exact objective, constraints, success definition은 본문 수동 확인 필요.
