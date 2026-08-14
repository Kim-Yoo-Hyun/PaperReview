# Problem — Flow Matching for Generative Modeling

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2023 / ICLR
- Category: Foundations: Generative Models
- Tags: Flow Matching, generative modeling, continuous normalizing flow, action generation
- Official paper: https://iclr.cc/virtual/2023/poster/11309
- Official PDF: https://openreview.net/pdf?id=PqvMRDCJT9t
- Code/Project: https://openreview.net/forum?id=PqvMRDCJT9t
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Target Problem

Continuous normalizing flow를 likelihood 계산이나 trajectory simulation 없이 대규모로 안정적으로 학습하는 방법이 필요하다.

## Core Assumptions

- 선택한 conditional probability path의 vector field를 회귀할 수 있다.
- robot control에 쓸 때는 generative sample quality가 action feasibility와 같지 않다.

## Closed-Loop Position

이 논문은 현재 robotics loop에서 `DDPM → Flow Matching → π0 / flow-based robot policies` 연결을 담당한다. 실제 정독 시 observation/state/action/control 중 어느 interface를 고정하고 어느 부분을 학습하는지 확인한다.

## Falsification Question

이미지 생성 결과만으로 robot action의 dynamics/contact feasibility를 보장하지 않는다.
