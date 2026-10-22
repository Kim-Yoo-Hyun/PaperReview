# Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Category: Benchmarks and Datasets
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: robot-evaluation, Benchmark, policy-comparison
- Aliases: Active Experiment Selection
- Official paper: https://proceedings.mlr.press/v305/anwar25a.html
- Venue verification: https://proceedings.mlr.press/v305/anwar25a.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Multi-task robot policy 평가를 적은 실험으로 수행한다.

## Core Idea and Contribution

비용을 고려한 active experiment selection과 task/policy 정보를 활용한다.

## Observation–State–Action Interface

Policy·task·prior·관측 결과 → 다음 평가 선택.

## Evaluation Scope and Claim Boundary

실제 및 simulated 평가 자료를 이용한 효율 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/anwar25a.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C6의 task-aware cost-aware 평가 배분에 대한 직접 REFERENCE다.

## Verification Boundary

prior 언어 정보, 관측 noise, offline matrix와 실제 online 실행 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
