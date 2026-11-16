# PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: policy-evaluation, real-to-sim, 3DGS
- Aliases: PolaRiS
- Official paper: https://roboticsproceedings.org/rss22/p062.html
- Venue verification: https://roboticsproceedings.org/rss22/p062.html
- Code/Project: https://polaris-evals.github.io/
- Code: https://github.com/arhanjain/PolaRiS
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

시뮬레이션의 정책 순위가 실제 로봇 성능을 충분히 반영하지 못한다.

## Core Idea and Contribution

짧은 실환경 스캔으로 시뮬레이터를 만들고 simulation co-training으로 잔여 차이를 줄인다.

## Observation–State–Action Interface

실환경 영상 → 재구성 환경 → generalist 정책 평가.

## Evaluation Scope and Claim Boundary

실제·시뮬레이션의 짝지은 rollout으로 정책 순위 상관을 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p062.html) · [저자 project/code](https://polaris-evals.github.io/) · [공식 code](https://github.com/arhanjain/PolaRiS). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

SIMPLER·RoboCasa의 점수를 실제 개선으로 해석하기 전 필요한 평가 타당성 비교다.

## Verification Boundary

평가 전에 허용된 co-training 데이터, 독립 실환경 trial, 장면 선택 편향을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
