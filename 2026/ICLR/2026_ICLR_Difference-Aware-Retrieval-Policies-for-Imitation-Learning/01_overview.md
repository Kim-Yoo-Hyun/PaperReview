# Difference-Aware Retrieval Policies for Imitation Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, evaluation, data-selection
- Aliases:
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html
- Code/Project: https://weirdlabuw.github.io/darp-site/
- Code: https://github.com/WEIRDLabUW/darp
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

Behavior cloning의 전역 state-to-action mapping은 배포 분포 변화에서 누적 오차를 겪는다.

## Core Idea and Contribution

시연의 가까운 상태·행동 및 query와의 상대 차이를 이용하는 semi-parametric policy를 학습한다.

## Observation–State–Action Interface

Query state·이웃 시연·상대 벡터 → action prediction.

## Evaluation Scope and Claim Boundary

Continuous control과 manipulation, 고차원 시각 표현에서 BC와 비교한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html) · [저자 project/code](https://weirdlabuw.github.io/darp-site/) · [공식 code](https://github.com/WEIRDLabUW/darp). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

학습 전 subset 선택과 실행 중 retrieval의 효과를 분리할 직접 대안이다.

## Verification Boundary

이웃 수, history 사용, retrieval 지연과 rollout split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
