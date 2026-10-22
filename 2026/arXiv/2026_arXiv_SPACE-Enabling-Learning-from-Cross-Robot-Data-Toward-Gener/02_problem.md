# SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

같은 움직임도 로봇 dynamics에 따라 다른 command를 요구한다.

## Bottleneck and Changed Formulation

Cartesian state delta를 예측하고 action adapter로 robot command로 변환한다.

## System and Robotics Loop

관측 → EEF state displacement → robot-specific adapter → 제어 명령.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

state delta 계산, adapter supervision, online 적응 자료, 실제 시간.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Embodiment·동일 기종 개체·frequency/payload/gain 변화 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2606.24049) · [저자 project/code](https://haeone.site/space-website/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
