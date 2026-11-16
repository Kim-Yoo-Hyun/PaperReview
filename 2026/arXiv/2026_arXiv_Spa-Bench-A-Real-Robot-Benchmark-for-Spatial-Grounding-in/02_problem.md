# Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

조작 성공률만으로는 공간 표현을 이해했는지와 기본 운동 능력이 부족한지를 구별하기 어렵다.

## Bottleneck and Changed Formulation

SO-101의 공간 지시 과제에서 익숙한 객체·개념·행동을 유지한 배치 변화와 직접 지시·표현·무행동 진단을 비교한다.

## System and Robotics Loop

실제 로봇의 관측·공간 언어 지시 → VLA 행동 → 목표별 채점. Counting과 no-action을 별도 진단으로 포함한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

ID/OOD support, 모델별 완료 범위와 trial 분모, 직접 지시의 정보량, 최종 수량·무행동 채점, 공개 data/코드의 실제 가용 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

저자는 여섯 tabletop task와 여러 VLA의 실제 rollout을 보고한다. 전체 protocol을 수행한 모델과 부분 baseline이 다르므로 분모를 섞지 않는다. 공개 project의 model/data 링크는 확인했으나 독립 실행 code URL은 확인하지 못했다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.12696) · [저자 project/code](https://justintiensmith.github.io/Spa-Bench/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
