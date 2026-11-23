# Is Your Imitation Learning Policy Better than Mine? Policy Comparison with Near-Optimal Stopping

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / RSS
- Authors: David Snyder, Asher James Hancock, Apurva Badithela, Emma Dixon, Patrick Miller, Rares Andrei Ambrus, Anirudha Majumdar, Masha Itkina, Haruki Nishimura
- Category: Benchmarks and Datasets
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: robot-evaluation, Benchmark, policy-comparison
- Aliases: STEP
- Official paper: https://roboticsproceedings.org/rss21/p077.html
- Venue verification: https://roboticsproceedings.org/rss21/p077.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

적은 robot trial로 두 imitation policy를 신뢰성 있게 비교한다.

## Core Idea and Contribution

순차 검정으로 비교를 멈출 시점을 결정한다.

## Observation–State–Action Interface

Policy별 binary success trial → sequential evidence → 중단/선택.

## Evaluation Scope and Claim Boundary

Simulation 및 실제 policy 비교를 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss21/p077.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C6의 trial budget·통계적 중단에 대한 표준 직접 기준이다.

## Verification Boundary

독립성, indifference region, 오류 확률, 다중 비교 처리을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
