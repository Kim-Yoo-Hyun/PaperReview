# AWAC: Accelerating Online Reinforcement Learning with Offline Datasets

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

기존 시연·비최적 데이터에서 초기화한 정책을 적은 online 상호작용으로 개선한다.

## Formulation and Robotics Loop

Offline transition·online replay → critic → 가중 행동 모방 → 실제 행동 수집.

Dynamic programming과 advantage 기반 가중 최대우도 정책 갱신을 결합한다.

## Assumptions to Verify

advantage scale·weight clipping·replay 비율·새 데이터 수집 비용.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

정책 iteration·가중 회귀 → AWAC → IQL·Cal-QL·VLA offline-to-online.

RL 이득이 성공 선택이나 weighted imitation으로 설명되는지 비교할 핵심 baseline이다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/2006.09359). 저자 project·arXiv v6 확인. OpenReview forum은 browser challenge로 본문 접근 실패했고 공식 acceptance를 확인하지 못해 arXiv 2020으로 등록한다. Project의 code 링크는 식별했으나 해당 경로 직접 fetch는 실패했다.
