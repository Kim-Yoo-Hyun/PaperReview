# Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Mingtong Zhang, Dhruv Shah
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, verification, test-time-compute, self-improvement
- Aliases: VERITAS
- Official paper: https://roboticsproceedings.org/rss22/p079.html
- Venue verification: https://roboticsproceedings.org/rss22/p079.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

배포된 generalist 정책이 자율 경험에서 유용한 개선 신호를 얻기 어렵다.

## Core Idea and Contribution

시각 verifier가 후보 행동을 선택하고 검증된 rollout을 후속 정책 학습에 사용한다.

## Observation–State–Action Interface

기존 정책의 행동 후보 → gradient-free 시각 검증 → 실행·재학습 데이터.

## Evaluation Scope and Claim Boundary

SIMPLER와 실제 DROID setup에서 steering 및 offline 개선을 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p079.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

RL 자체의 기여를 주장할 때 반드시 비교할 자율 데이터 선택·모방 대안이다.

## Verification Boundary

verifier 오류와 성공 판정의 독립성, fine-tuning objective, 인간 개입의 집계 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
