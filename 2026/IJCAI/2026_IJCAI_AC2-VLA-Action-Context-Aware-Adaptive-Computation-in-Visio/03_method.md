# AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

영상·지시·이전 행동 context로 cache 재사용·token pruning·layer 실행을 조절하고 action-guided distillation으로 학습한다.

## Observation, State, and Action

현재 관측·지시·이전 동작 → 계산 선택 → VLA action.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: 관측 age·cache invalidation·학습 추가 비용·FLOPs와 실측 latency.

## Method-Specific Comparison — Researcher Interpretation

같은 hardware·관측 age에서 dense·adaptive compute·real-time RL의 성공/지연을 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://ijcai.org/proceedings/2026/228). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
