# LADDER: A Long-Horizon Robot Manipulation Benchmark

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: Benchmarks and Datasets
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Benchmark, long-horizon, manipulation, subgoals
- Aliases: LADDER
- Official paper: https://arxiv.org/abs/2610.18053
- Venue verification: https://arxiv.org/abs/2610.18053
- Code/Project: https://ladder.insait.ai/
- Code: https://github.com/insait-institute/ladder
- Source audit: arXiv 초록, 저자 코드와 평가 에피소드의 공개 배포를 확인했다. 학회 게재는 확인되지 않았다.

## Problem and Importance

장면과 물체까지 바뀌면 긴 작업에서 정책이 실패한 이유를 단계 수의 증가와 분리하기 어렵다.

## Core Idea and Contribution

같은 환경에서 하위 목표 수를 1–10개로 바꾸고 직접 지시, 하위 지시, 도구 선택을 비교한다.

## Observation–State–Action Interface

언어 지시와 관측을 받는 실행 정책 또는 상위 조정기가 하위 동작·도구를 선택한다.

## Evaluation Scope and Claim Boundary

저자는 3개 시뮬레이션 평가군, 145과제, 시스템당 2,024회와 두 로봇 구성의 실물 실험을 보고했다. 시스템별 제어·추론 예산을 함께 봐야 한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.18053) · [저자 project/code](https://ladder.insait.ai/) · [공식 code](https://github.com/insait-institute/ladder). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

긴 조작의 계획 오류와 실행 오류를 추적할 수 있는 공개 실행 기록이 있어 일반 정책 비교에 직접 필요하다.

## Verification Boundary

시스템별 사용 가능한 성공 판정, 재시도 권한과 평가 예산을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
