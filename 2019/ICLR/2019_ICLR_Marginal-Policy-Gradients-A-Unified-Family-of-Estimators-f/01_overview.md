# Marginal Policy Gradients: A Unified Family of Estimators for Bounded Action Spaces with Applications

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2019 / ICLR
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: RL, evaluation, learning-foundation
- Aliases: MPG
- Official paper: https://openreview.net/forum?id=HkgqFiAcFm
- Venue verification: https://iclr.cc/Downloads/2019
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. OpenReview live challenge; ICLR 공식 Downloads/2019와 공식 indexed accepted manuscript를 확인했다. Content는 arXiv abstract 기준.

## Problem and Importance

변환 후 같은 실행 행동이 되는 action sample의 gradient 분산을 줄인다.

## Core Idea and Contribution

Marginal policy gradient family로 angular/clipped estimator를 통합한다.

## Observation–State–Action Interface

Raw action distribution → execution transform → marginal score.

## Evaluation Scope and Claim Boundary

RTS와 navigation task 및 variance 분석을 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=HkgqFiAcFm). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C3의 action equivalence 주장을 제한하는 가장 직접적인 이론 계보다.

## Verification Boundary

transform measurability, discrete/continuous 차이, action-slot weighting을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
