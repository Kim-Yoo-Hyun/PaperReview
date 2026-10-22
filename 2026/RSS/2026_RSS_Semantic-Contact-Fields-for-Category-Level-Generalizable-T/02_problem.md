# Semantic Contact Fields for Category-Level Generalizable Tool Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

새 도구 형상에서 semantic 목표와 접촉 제어를 함께 일반화한다.

## Bottleneck and Changed Formulation

3D semantic-contact field를 sim pretraining과 real pseudo-label 조정으로 학습한다.

## System and Robotics Loop

시각 의미·접촉 추정 → 3D field → diffusion policy.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

촉각 입력 종류, pseudo-label 정확도, unseen-tool split.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

서로 다른 도구를 사용하는 contact-rich 작업 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p004.html) · [저자 project/code](https://github.com/Kevinskwk/SCFields). Exact objective, constraints, success definition은 본문 수동 확인 필요.
