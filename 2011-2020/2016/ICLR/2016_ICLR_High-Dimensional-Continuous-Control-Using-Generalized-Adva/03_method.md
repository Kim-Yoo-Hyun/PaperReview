# High-Dimensional Continuous Control Using Generalized Advantage Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

가치함수를 이용한 지수 가중 advantage 추정으로 bias–variance를 조절하고 trust-region 정책·가치 갱신을 결합한다.

## Observation, State, and Action

운동학 상태 → 정책 → 관절 토크; trajectory와 가치 추정 → advantage → 정책 갱신.

## Objective and Training / Inference Boundary

위 설명은 초록에서 확인한 formulation이다. 정리의 가정·증명·구체적 갱신식은 본문 확인이 필요하다.

점검 항목: λ·γ의 시간 단위, truncation bootstrap, 가치함수 오차.

## Method-Specific Comparison — Researcher Interpretation

같은 trajectory에서 step/chunk bootstrap과 종료 mask를 고정해 advantage 및 gradient 차이를 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/1506.02438). ICLR 2016 공식 accepted conference list로 게재 확인. 2015 최초 preprint와 2018 v6를 별도 논문으로 만들지 않는다.
