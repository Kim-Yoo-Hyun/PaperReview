# AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Category: Benchmarks and Datasets
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: robot-evaluation, Benchmark, policy-comparison
- Aliases:
- Official paper: https://proceedings.mlr.press/v305/zhou25a.html
- Venue verification: https://proceedings.mlr.press/v305/zhou25a.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

실제 generalist policy의 반복 평가를 자동화한다.

## Core Idea and Contribution

평가 job scheduling·자동 success 검출·scene reset을 결합한다.

## Observation–State–Action Interface

Submitted policy → scene 실행/성공 판정/reset → 평가 결과.

## Evaluation Scope and Claim Boundary

WidowX/BridgeData 계열 실제 평가와 수동 판정을 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/zhou25a.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C5/C6의 reset ledger와 반복 평가를 설계할 핵심 system 기준이다.

## Verification Boundary

target start distribution, 자동 judge 오류, 제외 trial, human 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
