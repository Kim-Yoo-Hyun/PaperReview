# Decoupled Q-Chunking

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: chunked-critic, reactivity, long-horizon
- Aliases: DQC
- Official paper: https://openreview.net/pdf/bde79a617f6c016e2c51c7771416933c0646102c.pdf
- Venue verification: https://openreview.net/pdf/bde79a617f6c016e2c51c7771416933c0646102c.pdf
- Code/Project: https://github.com/ColinQiyangLi/dqc
- Code: https://github.com/ColinQiyangLi/dqc
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

Chunked critic의 빠른 value backup을 활용하면서 긴 open-loop action sequence를 학습·실행해야 하는 제약을 줄인다.

## Core Idea and Contribution

Critic이 평가하는 chunk 길이와 actor가 출력하는 chunk 길이를 분리한다.

## Observation–State–Action Interface

State → 짧은 actor action chunk; 긴 critic horizon을 통한 value 학습. 실제 controller frequency는 본문 확인 필요.

## Evaluation Scope and Claim Boundary

최종 paper의 abstract와 공식 code는 장기 offline goal-conditioned task 평가를 설명한다. 실제 로봇 contact 평가 여부는 확인 필요.

근거: [공식 paper/abstract](https://openreview.net/pdf/bde79a617f6c016e2c51c7771416933c0646102c.pdf) · [저자 project/code](https://github.com/ColinQiyangLi/dqc). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. Critic과 actor의 chunk 길이를 분리한다. Q-chunking의 value propagation 이점과 짧은 action horizon의 반응성 사이의 설계 문제를 직접 다룬다. 실제 contact feedback 성능으로의 확장은 본문/실험 확인이 필요하다.

## Verification Boundary

부분 chunk value 추정, policy extraction objective, reactive 평가의 실제 포함 여부을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
