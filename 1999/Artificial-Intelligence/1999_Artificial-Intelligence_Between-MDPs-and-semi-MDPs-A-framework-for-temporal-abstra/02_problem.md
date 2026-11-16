# Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

서로 다른 시간 길이의 행동과 정책을 같은 RL 형식으로 다룬다.

## Formulation and Robotics Loop

상태 → option 선택 → 내부 정책 실행 → 종료 또는 중단 → 다음 결정.

여러 step 동안 실행되는 closed-loop option과 SMDP를 연결하고 중단·intra-option 학습을 분석한다.

## Assumptions to Verify

initiation·termination·closed-loop 조건·물리 시간 할인.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

MDP·Q-learning → options/SMDP → action chunk·실행 중단·시간별 credit assignment.

가변 chunk·재계획·중단을 해석할 기본 formulation을 보완하며 계층형 주제로 전환하라는 의미는 아니다.

## Evidence Boundary

[공식 paper/abstract](https://www.sciencedirect.com/science/article/pii/S0004370299000521). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
