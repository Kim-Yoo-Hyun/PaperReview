# LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Embodiment별 action interface가 새 로봇 전이를 제한한다.

## Bottleneck and Changed Formulation

언어 action 표현으로 사전학습하고 새로운 embodiment로의 zero-shot 전이를 탐색한다.

## System and Robotics Loop

영상·지시 → 언어 action → 로봇별 실행.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

zero-shot 정의, robot-specific mapping, pretraining 중복.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

새 embodiment 전이와 robot adaptation 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p203.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
