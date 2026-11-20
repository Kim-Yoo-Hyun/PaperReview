# Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: Benchmarks and Datasets
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: robot-evaluation, Benchmark, policy-comparison
- Aliases: NSCORE
- Official paper: https://roboticsproceedings.org/rss22/p076.html
- Venue verification: https://roboticsproceedings.org/rss22/p076.html
- Code/Project: https://github.com/dasnyder5/nscore
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

이진 성공 외의 풍부한 신호로 robot policy를 효율적으로 비교한다.

## Core Idea and Contribution

Progress 등 bounded metric에 기반한 통계적 순차 비교를 제안한다.

## Observation–State–Action Interface

Trial-level metric → evidence update → policy comparison.

## Evaluation Scope and Claim Boundary

Simulation과 실제 robot policy 비교를 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p076.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C6의 progress-aware 선택을 신규 통계 방법으로 재주장하지 않도록 하는 최신 기준이다.

## Verification Boundary

boundedness, anytime 보장, metric 편향, 반복 model selection을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
