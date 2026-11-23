# SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RA-L
- Authors: Kuan Fang, Yuxin Chen, Xinghao Zhu, Farzad Niroui, Lingfeng Sun, Jiuguang Wang
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: mobile-manipulation, affordance, 3D-grounding, whole-body
- Aliases: SAGA
- Official paper: https://robot-saga.github.io/
- Venue verification: https://ieeexplore.ieee.org/document/11568510/
- Code/Project: https://robot-saga.github.io/
- Code: project_only
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. IEEE indexed publisher 내용으로 게재를 확인했고 직접 본문 접근은 제한적이었다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

다양한 지시와 환경을 하나의 이동 조작 제어기로 연결할 때 semantic intent와 시각 변동을 분리한다.

## Core Idea and Contribution

Task를 구조화된 affordance로 표현하고 관측의 3D heatmap에 grounding하여 whole-body 조작 정책을 조건화한다.

## Observation–State–Action Interface

언어·지정 point·예시 시연 → 관측에 정렬된 affordance → quadrupedal manipulator의 whole-body 행동.

## Evaluation Scope

실제 quadrupedal manipulator의 11개 task에서 end-to-end 및 modular 대안과 비교한다. IEEE의 RA-L 11(9), 2026 게재를 우선하며 lab page의 오래된 under-review 표기는 채택하지 않는다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11568510/) · [저자 project](https://robot-saga.github.io/).

## Why This Paper Is Here — Researcher Interpretation

VoxPoser·Mobile ALOHA와 구조적 3D grounding을 잇는 NEXT다. 다양한 로봇을 다룬다는 목표에서 의미 표현과 embodiment별 제어의 경계를 비교한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
