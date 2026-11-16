# Policy invariance under reward transformations: Theory and application to reward shaping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

상태 potential의 차이로 구성하는 보상 변환의 정책 보존 조건과 그 필요성을 분석한다.

## Observation, State, and Action

MDP의 상태 전이·원 보상 → potential 기반 shaping → 정책 최적화.

## Objective and Training / Inference Boundary

위 설명은 초록에서 확인한 formulation이다. 정리의 가정·증명·구체적 갱신식은 본문 확인이 필요하다.

점검 항목: 할인율·종료 potential·Markov 상태·history 의존 보상.

## Method-Specific Comparison — Researcher Interpretation

작은 명시적 MDP에서 원 보상·potential 차이·그냥 progress 점수의 최적 행동을 대조한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf). 저자 원문 abstract와 Russell의 ICML-99 publication 기록 확인. PDF는 웹에서 확인했으며 local cache는 저장하지 않았다. ACM endpoint는 403으로 접근 실패해 DOI를 추정하지 않았다.
