# LADDER: A Long-Horizon Robot Manipulation Benchmark

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

장면과 물체까지 바뀌면 긴 작업에서 정책이 실패한 이유를 단계 수의 증가와 분리하기 어렵다.

## Bottleneck and Changed Formulation

같은 환경에서 하위 목표 수를 1–10개로 바꾸고 직접 지시, 하위 지시, 도구 선택을 비교한다.

## System and Robotics Loop

언어 지시와 관측을 받는 실행 정책 또는 상위 조정기가 하위 동작·도구를 선택한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

시스템별 사용 가능한 성공 판정, 재시도 권한과 평가 예산.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

저자는 3개 시뮬레이션 평가군, 145과제, 시스템당 2,024회와 두 로봇 구성의 실물 실험을 보고했다. 시스템별 제어·추론 예산을 함께 봐야 한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.18053) · [저자 project/code](https://ladder.insait.ai/) · [공식 code](https://github.com/insait-institute/ladder). Exact objective, constraints, success definition은 본문 수동 확인 필요.
