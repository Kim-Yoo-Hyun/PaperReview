# Constraint-Grounded Reinforcement Learning for Variable Impedance Control in Contact-Rich Robotic Insertion

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / arXiv
- Authors: Lin He, Min Deng
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: variable-impedance, reinforcement-learning, insertion, force-limit, force-feedback
- Aliases: CG-RL
- Official paper: https://arxiv.org/abs/2609.13516
- Venue verification: https://arxiv.org/abs/2609.13516
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://arxiv.org/pdf/2609.13516v1
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다.

## Problem and Importance

CG-RL은 주어진 축 방향 힘 상한과 접촉 피드백에 따라 삽입 속도·잔차 동작·임피던스 이득을 조절하며, 제어기가 요청 이득을 허용 구간에 투영한다. [PDF 1쪽](https://arxiv.org/pdf/2609.13516v1#page=1) · [PDF 5쪽](https://arxiv.org/pdf/2609.13516v1#page=5)

## Core Idea and Contribution

- 정책에는 힘 상한을 입력하고 이득 구간은 제어기만 사용하게 설계했다. 투영은 적용 이득의 범위를 보장하며 힘 상한 준수는 시행에서 측정한다. [PDF 5쪽](https://arxiv.org/pdf/2609.13516v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.13516v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.13516v1#page=7)
- 경사 삽입 시뮬레이션에서 힘 상한을 지키며 삽입한 성공률은 다섯 학습 시드 평균 85.8±7.7%, 고정 중간 이득 기준선은 50.1±1.0%였다. [PDF 10쪽](https://arxiv.org/pdf/2609.13516v1#page=10) · [PDF 15쪽](https://arxiv.org/pdf/2609.13516v1#page=15)

## Observation–State–Action Interface

접촉 feedback·force limit → residual motion·속도·요청 gain.

## Evaluation Scope and Claim Boundary

허용 구간 투영이 보장하는 대상은 적용 이득이다. 힘 상한을 지킨 삽입의 85.8±7.7%는 경사 삽입 시뮬레이션에서 측정한 시드 간 평균±표준편차다. [PDF 5쪽](https://arxiv.org/pdf/2609.13516v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.13516v1#page=6) · [PDF 10쪽](https://arxiv.org/pdf/2609.13516v1#page=10) · [PDF 15쪽](https://arxiv.org/pdf/2609.13516v1#page=15)

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.13516).

## 검색 태그 근거

정책은 힘 상한과 접촉 반응을 관측해 잔차 변위·삽입 속도·이득을 요청한다. 실행부만 허용 이득 구간을 받아 요청을 투영한다. 힘 상한 준수 여부는 Isaac Lab의 Franka 경사 삽입 시행에서 측정했다. [원문 5쪽](https://arxiv.org/pdf/2609.13516v1#page=5) · [원문 7쪽](https://arxiv.org/pdf/2609.13516v1#page=7) · [원문 10쪽](https://arxiv.org/pdf/2609.13516v1#page=10)

## Why This Paper Is Here — Researcher Interpretation

동작·강성 공동 RL 자체가 새롭지 않음을 보이는 controller 비교 자료다.

## Verification Boundary

Projection과 actor 범위, force constraint의 경험적/형식적 보장 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
