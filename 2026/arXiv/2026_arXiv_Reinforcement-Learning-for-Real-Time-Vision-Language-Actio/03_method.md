# Reinforcement Learning for Real-Time Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

느린 VLA chunk 생성과 최신 관측을 사용하는 빠른 action edit를 분리해 EXPO-FT를 실시간 RL로 확장한다.

## Observation, State, and Action

느린 VLA action chunk + 최신 관측 → 경량 edit policy → 즉시 로봇 행동.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: edit 주파수·관측 timestamp·동기화·robot interaction 비용·단일 정책 여부.

## Method-Specific Comparison — Researcher Interpretation

같은 지연 조건에서 비동기 BC·기존 EXPO-FT·실시간 editor를 비교하고 실제 반응 시간을 분리한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/2609.18207). arXiv v1와 저자 project/code에서 EXPO-FT 원 방법과 real-time branch의 구분 확인. 공식 conference acceptance는 확인하지 않았다.
