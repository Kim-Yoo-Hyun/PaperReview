# AWAC: Accelerating Online Reinforcement Learning with Offline Datasets

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

Dynamic programming과 advantage 기반 가중 최대우도 정책 갱신을 결합한다.

## Observation, State, and Action

Offline transition·online replay → critic → 가중 행동 모방 → 실제 행동 수집.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: advantage scale·weight clipping·replay 비율·새 데이터 수집 비용.

## Method-Specific Comparison — Researcher Interpretation

데이터·초기 정책·학습량을 맞춰 BC·success-only BC·AWAC·online RL을 대조한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/2006.09359). 저자 project·arXiv v6 확인. OpenReview forum은 browser challenge로 본문 접근 실패했고 공식 acceptance를 확인하지 못해 arXiv 2020으로 등록한다. Project의 code 링크는 식별했으나 해당 경로 직접 fetch는 실패했다.
