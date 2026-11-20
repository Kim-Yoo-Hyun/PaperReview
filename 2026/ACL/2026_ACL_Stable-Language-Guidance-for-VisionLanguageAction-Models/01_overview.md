# Stable Language Guidance for Vision–Language–Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

시각 prior가 언어의 의도를 압도하고 표현 변화에 정책이 민감해지는 문제를 다룬다.

## Core Idea and Contribution

Paraphrase에 대한 Monte Carlo 통합과 visual affordance prior를 분리하는 residual semantic steering을 결합한다.

## Observation–State–Action Interface

시각 관측·언어 표현들의 분포 → 의미/affordance 분리 추론 → VLA 행동. 검색한 demo를 바꾸는 개입과 현재 지시를 바꾸는 개입은 다르다.

## Evaluation Scope

공식 abstract는 manipulation benchmark의 언어 교란 강건성을 보고한다. Backbone·실기 여부·세부 성공률은 이번 abstract 확인 범위에서 확정하지 않는다.

근거: [공식 paper/abstract](https://aclanthology.org/2026.acl-long.190/) · [저자 project](https://github.com/Doo-mon/RSS).

## Why This Paper Is Here — Researcher Interpretation

지시 수정·집합 지시·시연 검색 후보가 공유하는 언어 민감성의 NEXT 직접 대안이다. 같은 의미의 표현 차이를 새로운 task conflict로 해석하지 않도록 등록한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
