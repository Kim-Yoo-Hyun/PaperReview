# Stable Language Guidance for Vision–Language–Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ACL
- Authors: Zhihao Zhan, Yuhao Chen, Jiaying Zhou, Qinhan Lyu, Hao Liu, Keze Wang, Liang Lin, Guangrun Wang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, language-grounding, robustness, semantic-steering
- Aliases: Residual Semantic Steering
- Official paper: https://aclanthology.org/2026.acl-long.190/
- Venue verification: https://aclanthology.org/2026.acl-long.190/
- Code/Project: https://github.com/Doo-mon/RSS
- Code: https://github.com/Doo-mon/RSS
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 같은 뜻의 지시를 바꿔 쓰면 VLA 행동이 달라지는 문제를 줄이기 위해 언어 학습 예시를 늘리고 행동 생성 시 시각 단서의 영향을 보정한다. [PDF 1쪽](https://aclanthology.org/2026.acl-long.190.pdf#page=1) · [PDF 3쪽](https://aclanthology.org/2026.acl-long.190.pdf#page=3)

## Core Idea and Contribution

- 언어 모델에서 지시의 여러 표현을 표집하고 시각 장면이 유도하는 행동 경향을 기준으로 언어에 해당하는 잔차 방향을 추정한다. [PDF 3쪽](https://aclanthology.org/2026.acl-long.190.pdf#page=3) · [PDF 4쪽](https://aclanthology.org/2026.acl-long.190.pdf#page=4)
- 지시 표현을 바꾼 조건과 물체 개념을 새로운 조합으로 지시한 조건에서 정책의 작업 성공률을 비교했다. [PDF 5쪽](https://aclanthology.org/2026.acl-long.190.pdf#page=5) · [PDF 6쪽](https://aclanthology.org/2026.acl-long.190.pdf#page=6)

## Observation–State–Action Interface

시각 관측·언어 표현들의 분포 → 의미/affordance 분리 추론 → VLA 행동. 검색한 demo를 바꾸는 개입과 현재 지시를 바꾸는 개입은 다르다.

## Evaluation Scope

공식 abstract는 manipulation benchmark의 언어 교란 강건성을 보고한다. Backbone·실기 여부·세부 성공률은 이번 abstract 확인 범위에서 확정하지 않는다.

근거: [공식 paper/abstract](https://aclanthology.org/2026.acl-long.190/) · [저자 project](https://github.com/Doo-mon/RSS).

## Why This Paper Is Here — Researcher Interpretation

지시 수정·집합 지시·시연 검색 후보가 공유하는 언어 민감성의 NEXT 직접 대안이다. 같은 의미의 표현 차이를 새로운 task conflict로 해석하지 않도록 등록한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
