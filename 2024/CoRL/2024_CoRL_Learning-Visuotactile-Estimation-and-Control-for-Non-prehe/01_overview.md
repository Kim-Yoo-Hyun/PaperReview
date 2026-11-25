# Learning Visuotactile Estimation and Control for Non-prehensile Manipulation under Occlusions

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CoRL
- Authors: Juan Del Aguila Ferrandis, João Moura, Sethu Vijayakumar
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, force-torque, state-estimation, occlusion, non-prehensile
- Aliases:
- Official paper: https://proceedings.mlr.press/v270/ferrandis25a.html
- Venue verification: https://proceedings.mlr.press/v270/ferrandis25a.html
- Conference edition: 2024 · https://proceedings.mlr.press/v270/
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. CoRL 개최 2024, PMLR 출판 2025. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 물체가 손에 가려지는 비파지 조작에서 시각·촉각으로 상태와 그 불확실성을 추정해 제어에 활용한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/ferrandis25a/ferrandis25a.pdf#page=1)

## Core Idea and Contribution

- 시뮬레이터의 상태를 아는 강화학습 정책으로 자료를 수집한 뒤 제한된 센서 정보에서 물체 상태의 확률적 추정치를 학습한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/ferrandis25a/ferrandis25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/ferrandis25a/ferrandis25a.pdf#page=4)
- 카메라 가림 조건과 실제 로봇에서 불확실성까지 제어기에 제공하는 방식과 일부 감각 또는 추정 정보만 쓰는 방식을 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/ferrandis25a/ferrandis25a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/ferrandis25a/ferrandis25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/ferrandis25a/ferrandis25a.pdf#page=8)

## Observation–State–Action Interface

시각·촉각 → 추정 상태/불확실성 → uncertainty-aware control.

## Evaluation Scope and Claim Boundary

비파지 manipulation의 가림 조건과 실로봇 sim-to-real을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/ferrandis25a.html). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

접촉 VLA의 센서 이득과 상태 추정·feedback controller 이득을 분리할 직접 대안이다.

## Verification Boundary

privileged training input, tactile modality, occlusion 분포, estimator와 policy ablation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 판본과 출처

저자 표기·순서는 표제면 기준이다. [표제면](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/ferrandis25a/ferrandis25a.pdf#page=1)
