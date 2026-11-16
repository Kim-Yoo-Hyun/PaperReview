# General agents need world models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / ICML
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: world model, generalization, theory
- Aliases:
- Official paper: https://proceedings.mlr.press/v267/richens25a.html
- Venue verification: https://proceedings.mlr.press/v267/richens25a.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다.

## Problem and Importance

다단계 목표 일반화에 환경 예측 모델이 필요한지 형식적으로 묻는다.

## Core Idea and Contribution

일반화 가능한 정책에서 예측 world model을 추출할 수 있음을 이론적으로 분석한다.

## Observation–State–Action Interface

다양한 목표를 수행하는 policy → 추출 가능한 환경 예측 model.

## Evaluation Scope and Claim Boundary

공식 abstract는 다단계 목표·성능과 모델 정확도의 이론적 관계를 제시한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v267/richens25a.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

명시적 video model 사용과 정책에 내재한 예측 능력을 구별하는 AI 이론 참조다.

## Verification Boundary

일반화·목표 집합 정의, 추출 접근 권한, 정리 조건과 실제 로봇 적용 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
