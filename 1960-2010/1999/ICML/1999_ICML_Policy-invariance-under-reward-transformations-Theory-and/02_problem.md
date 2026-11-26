# Policy invariance under reward transformations: Theory and application to reward shaping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

학습을 돕는 보상 변경이 원래 최적 정책을 바꾸는 조건을 묻는다.

## Formulation and Robotics Loop

MDP의 상태 전이·원 보상 → potential 기반 shaping → 정책 최적화.

상태 potential의 차이로 구성하는 보상 변환의 정책 보존 조건과 그 필요성을 분석한다.

## Assumptions to Verify

할인율·종료 potential·Markov 상태·history 의존 보상.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

보상 설계·IRL → potential shaping → STARE-VLA 및 robot reward model의 주장 경계를 비교한다.

VLM progress·단계 보상·접촉 보상으로 목표를 변경하는지 판단할 공통 이론 원전이므로 CORE다.

## Evidence Boundary

[공식 paper/abstract](https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf). 저자 원문 abstract와 Russell의 ICML-99 publication 기록 확인. PDF는 웹에서 확인했으며 local cache는 저장하지 않았다. ACM endpoint는 403으로 접근 실패해 DOI를 추정하지 않았다.
