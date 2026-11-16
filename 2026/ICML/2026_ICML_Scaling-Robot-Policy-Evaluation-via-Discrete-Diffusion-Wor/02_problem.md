# Scaling Robot Policy Evaluation via Discrete Diffusion World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

World model이 실패를 정상 장면으로 보정하면 policy 평가와 순위가 왜곡된다.

## Bottleneck and Changed Formulation

Action을 unified token으로 다루는 discrete diffusion과 keyframe memory·progress 출력을 결합한다.

## System and Robotics Loop

관측·언어·action chunk → 미래 관측·성공 지표 → policy ranking.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

성공 평가기 독립성, 실패 데이터, final/preprint 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO·RoboTwin 및 real-robot task 기반 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/li26hi.html) · [저자 project/code](https://dworldeval.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
