# ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

표준 초기 상태에서는 각각 가능한 작업도 실행 중 지시를 바꾸면 전환되지 않을 수 있다.

## Bottleneck and Changed Formulation

상태별 task steerability를 측정하고, 전환이 어려운 상태의 추정·전환 구간 데이터 생성·정책 self-refinement를 연결한다.

## System and Robotics Loop

현재 관측과 새 언어 지시 → multitask policy의 행동. 중간 상태에서의 전환 능력과 초기 상태의 작업 능력을 구별한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

steerability score의 분모·switch timing·초기 능력, estimator와 실제 성공의 관계, 데이터 생성 비용, 제약 유지·철회가 평가에 포함되는 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO와 실제 로봇의 지시 전환을 평가한다. 공개 repository는 LIBERO 평가·데이터 생성 경로를 제공하지만 로컬 native 실행은 아직 확인하지 않았다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p143.html) · [저자 project/code](https://resteer-vla.github.io/) · [공식 code](https://github.com/ChenZhenY/ReSteer). Exact objective, constraints, success definition은 본문 수동 확인 필요.
