# Long-Context Robot Imitation Learning by Focusing on Key History Frames

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

긴 관측 이력은 학습에 없던 history에서 잘못된 상관에 의존할 수 있다.

## Bottleneck and Changed Formulation

VLM이 선택한 소수의 의미 있는 keyframe으로 정책 history를 압축한다.

## System and Robotics Loop

관측 이력 → 의미 keyframe → history-conditioned 로봇 행동.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

VLM 호출 비용, event 검출의 미래 정보 누출, history 길이별 평가.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

기억이 필요한 실제 조작과 simulation 과제를 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p201.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
