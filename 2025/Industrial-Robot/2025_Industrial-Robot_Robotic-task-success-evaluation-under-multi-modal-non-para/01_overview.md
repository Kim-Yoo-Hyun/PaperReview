# Robotic task success evaluation under multi-modal non-parametric object pose uncertainty

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / Industrial Robot
- Authors: Lakshadeep Naik, Thorbjørn Mosekjær Iversen, Aljaz Kramberger, Norbert Krüger
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: pose uncertainty, task success, mobile manipulation, tolerance
- Aliases:
- Official paper: https://api.crossref.org/works/10.1108/IR-10-2024-0467
- Venue verification: https://www.emerald.com/ir/article-abstract/52/5/651/1254840/Robotic-task-success-evaluation-under-multi-modal?redirectedFrom=PDF
- Code/Project: not identified
- Code: not_identified
- 방법·평가 확인 (2026-11-25): [원문 3, 4, 6, 7쪽](https://arxiv.org/pdf/2403.10874v1#page=3) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. Industrial Robot 52(5), 651–662; top-tier로 표시하지 않는다. 2024 preprint와 2025 journal은 동일 entry로 관리. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 물체의 6차원 자세 오차와 로봇 과제가 허용하는 오차를 함께 모델링해 주어진 추정으로 행동이 성공할 확률을 계산한다. [PDF 1쪽](https://arxiv.org/pdf/2403.10874v1#page=1)

## Core Idea and Contribution

- 실행 가능한 오차 범위를 시뮬레이션으로 미리 구하고, 여러 봉우리를 가질 수 있는 자세 오차 분포와 결합해 과제별 성공 가능성을 산출한다. [PDF 3쪽](https://arxiv.org/pdf/2403.10874v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2403.10874v1#page=4)
- 이동 조작에서 파지를 위한 베이스 위치의 역기구학적 도달 가능성과 실제 파지 성공을 따로 평가해 영상 신뢰도 및 단일 가우시안 불확실성과 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2403.10874v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2403.10874v1#page=7)

## Observation–State–Action Interface

Pose uncertainty와 task-specific acceptable-error 공간에서 성공 가능성을 얻는다. VLA 표현 학습은 별도다.

## Evaluation Scope and Claim Boundary

공식 publisher 초록은 두 mobile manipulation task의 성공/실패 평가를 명시한다.

근거: [공식 paper/abstract](https://www.emerald.com/ir/article-abstract/52/5/651/1254840/Robotic-task-success-evaluation-under-multi-modal?redirectedFrom=PDF). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

불확실성이 남아도 성공하면 행동한다는 원리를 신규성에서 제외하게 하는 직접 비교다.

## Verification Boundary

허용 오차 precompute 비용·동역학 전제·online pose distribution·최종본과 preprint 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
