# SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
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
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. IEEE indexed publisher 내용으로 게재를 확인했고 직접 본문 접근은 제한적이었다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

SAGA는 물체의 어디에 어떻게 작용할지를 나타내는 3차원 어포던스를 이용해 사족 로봇의 전신 조작을 제어한다. [PDF 1쪽](https://arxiv.org/pdf/2512.12842v1#page=1)

## Core Idea and Contribution

- 언어 지시, 지정한 점, 시연에서 나온 목표를 공통의 구조화된 공간 표현으로 바꿔 전신 정책에 제공한다. [PDF 3쪽](https://arxiv.org/pdf/2512.12842v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2512.12842v1#page=4)
- 여러 실제 조작 과제에서 지시 방식과 물체 배치가 바뀌었을 때 목표 접촉을 만들고 과제를 마치는 능력을 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2512.12842v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2512.12842v1#page=6)

## Observation–State–Action Interface

언어·지정 point·예시 시연 → 관측에 정렬된 affordance → quadrupedal manipulator의 whole-body 행동.

## Evaluation Scope

실제 quadrupedal manipulator의 11개 task에서 end-to-end 및 modular 대안과 비교한다. IEEE의 RA-L 11(9), 2026 게재를 우선하며 lab page의 오래된 under-review 표기는 채택하지 않는다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11568510/) · [저자 project](https://robot-saga.github.io/).

## Why This Paper Is Here — Researcher Interpretation

VoxPoser·Mobile ALOHA와 구조적 3D grounding을 잇는 NEXT다. 다양한 로봇을 다룬다는 목표에서 의미 표현과 embodiment별 제어의 경계를 비교한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
