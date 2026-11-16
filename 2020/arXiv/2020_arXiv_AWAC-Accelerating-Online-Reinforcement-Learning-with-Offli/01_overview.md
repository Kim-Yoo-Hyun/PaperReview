# AWAC: Accelerating Online Reinforcement Learning with Offline Datasets

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2020 / arXiv
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-to-online, reinforcement-learning, advantage-weighting, manipulation
- Aliases: AWAC
- Official paper: https://arxiv.org/abs/2006.09359
- Venue verification: https://arxiv.org/abs/2006.09359
- Code/Project: https://awacrl.github.io/
- Code: https://github.com/vitchyr/rlkit/tree/master/examples/awac
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 저자 project·arXiv v6 확인. OpenReview forum은 browser challenge로 본문 접근 실패했고 공식 acceptance를 확인하지 못해 arXiv 2020으로 등록한다. Project의 code 링크는 식별했으나 해당 경로 직접 fetch는 실패했다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

기존 시연·비최적 데이터에서 초기화한 정책을 적은 online 상호작용으로 개선한다.

## Core Idea and Contribution

Dynamic programming과 advantage 기반 가중 최대우도 정책 갱신을 결합한다.

## Observation–State–Action Interface

Offline transition·online replay → critic → 가중 행동 모방 → 실제 행동 수집.

## Evaluation Scope and Claim Boundary

시뮬레이션과 실제 다지 손·서랍 열기·밸브 조작을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2006.09359) · [저자 project/code](https://awacrl.github.io/) · [공식 code](https://github.com/vitchyr/rlkit/tree/master/examples/awac). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

RL 이득이 성공 선택이나 weighted imitation으로 설명되는지 비교할 핵심 baseline이다.

## Verification Boundary

본문에서 확인할 항목: advantage scale·weight clipping·replay 비율·새 데이터 수집 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
