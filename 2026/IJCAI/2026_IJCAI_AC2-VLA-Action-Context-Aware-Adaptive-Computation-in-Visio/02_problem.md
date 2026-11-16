# AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

큰 VLA backbone의 반복 계산이 closed-loop 행동을 지연시킨다.

## Formulation and Robotics Loop

현재 관측·지시·이전 동작 → 계산 선택 → VLA action.

영상·지시·이전 행동 context로 cache 재사용·token pruning·layer 실행을 조절하고 action-guided distillation으로 학습한다.

## Assumptions to Verify

관측 age·cache invalidation·학습 추가 비용·FLOPs와 실측 latency.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

OpenVLA/CogACT·추론 가속 → AC2-VLA → real-time RL의 강한 비-RL 계산 대안.

RL 기반 시간 적응과 비교할 학습된 계산 절감 baseline이며 지연·feedback·성능의 비용 분리를 돕는다.

## Evidence Boundary

[공식 paper/abstract](https://ijcai.org/proceedings/2026/228). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
