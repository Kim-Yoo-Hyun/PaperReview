# LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

기존 LIBERO 평가에서 task 이해와 행동 암기가 혼동될 수 있다.

## Bottleneck and Changed Formulation

물체·초기 상태·지시·환경 perturbation으로 일반화와 지시 의존성을 점검한다.

## System and Robotics Loop

변형 task/지시 → VLA → 실행 결과.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

변경된 목표의 타당성, 언어 교란의 의미, v1/v2 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO 기반 변형 평가를 보고한다. 극단적 저하 수치의 task validity는 별도 본문 감사가 필요하다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2510.03827) · [저자 project/code](https://github.com/Zxy-MLlab/LIBERO-PRO). Exact objective, constraints, success definition은 본문 수동 확인 필요.
