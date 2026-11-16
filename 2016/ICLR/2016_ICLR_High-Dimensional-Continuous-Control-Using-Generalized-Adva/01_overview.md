# High-Dimensional Continuous Control Using Generalized Advantage Estimation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2016 / ICLR
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: reinforcement-learning, policy-gradient, advantage-estimation, variance-reduction
- Aliases: GAE
- Official paper: https://arxiv.org/abs/1506.02438
- Venue verification: https://www.iclr.cc/archive/www/2016.html
- Code/Project:
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. ICLR 2016 공식 accepted conference list로 게재 확인. 2015 최초 preprint와 2018 v6를 별도 논문으로 만들지 않는다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

정책 gradient의 높은 분산과 비정상 데이터로 인한 불안정을 다룬다.

## Core Idea and Contribution

가치함수를 이용한 지수 가중 advantage 추정으로 bias–variance를 조절하고 trust-region 정책·가치 갱신을 결합한다.

## Observation–State–Action Interface

운동학 상태 → 정책 → 관절 토크; trajectory와 가치 추정 → advantage → 정책 갱신.

## Evaluation Scope and Claim Boundary

시뮬레이션의 이족·사족 보행과 기립 과제를 평가한다. 실제 로봇 검증으로 확대하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/1506.02438). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

PPO 기반 VLA RL에서 advantage·bootstrap·시간 단위가 학습에 미치는 영향을 해석하기 위한 공통 원전이므로 CORE다.

## Verification Boundary

본문에서 확인할 항목: λ·γ의 시간 단위, truncation bootstrap, 가치함수 오차. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
