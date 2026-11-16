# High-Dimensional Continuous Control Using Generalized Advantage Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

정책 gradient의 높은 분산과 비정상 데이터로 인한 불안정을 다룬다.

## Formulation and Robotics Loop

운동학 상태 → 정책 → 관절 토크; trajectory와 가치 추정 → advantage → 정책 갱신.

가치함수를 이용한 지수 가중 advantage 추정으로 bias–variance를 조절하고 trust-region 정책·가치 갱신을 결합한다.

## Assumptions to Verify

λ·γ의 시간 단위, truncation bootstrap, 가치함수 오차.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

TD(λ)·policy gradient → GAE → PPO·SimpleVLA-RL의 advantage 구현을 비교한다.

PPO 기반 VLA RL에서 advantage·bootstrap·시간 단위가 학습에 미치는 영향을 해석하기 위한 공통 원전이므로 CORE다.

## Evidence Boundary

[공식 paper/abstract](https://arxiv.org/abs/1506.02438). ICLR 2016 공식 accepted conference list로 게재 확인. 2015 최초 preprint와 2018 v6를 별도 논문으로 만들지 않는다.
