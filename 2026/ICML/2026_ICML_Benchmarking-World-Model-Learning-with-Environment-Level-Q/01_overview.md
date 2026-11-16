# Benchmarking World-Model Learning with Environment-Level Queries

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICML
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: world model, Benchmark, counterfactual, environment-query
- Aliases: WorldTest, AutumnBench
- Official paper: https://proceedings.mlr.press/v306/warrier26a.html
- Venue verification: https://proceedings.mlr.press/v306/warrier26a.html
- Code/Project: https://zenodo.org/records/19498269
- Code: project_only
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. 공식 PMLR abstract와 Software 링크 확인. Zenodo landing page 직접 접근 실패; 링크 존재만 기록하며 파일/코드 release와 실행 가능성은 미검증.

## Problem and Importance

단일 rollout의 예측이나 return만으로 환경 전반을 이해했는지 판단하기 어렵다.

## Core Idea and Contribution

도달 가능성·개입 결과 같은 environment-level query를 평가하는 WorldTest를 제안한다.

## Observation–State–Action Interface

환경 상호작용 → 학습된 model/belief → 여러 유형의 환경 질의.

## Evaluation Scope and Claim Boundary

AutumnBench grid-world에서 사람과 학습 agent를 비교한다. 실로봇 평가는 아니다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/warrier26a.html) · [저자 project/code](https://zenodo.org/records/19498269). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA world model의 시각 품질·정책 순위와 환경 이해를 구분할 평가 방법론이다.

## Verification Boundary

query 정답 접근, exploration budget, 환경 생성 분할, robot task로의 전이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
