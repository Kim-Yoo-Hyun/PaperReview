# Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

여러 step 동안 실행되는 closed-loop option과 SMDP를 연결하고 중단·intra-option 학습을 분석한다.

## Observation, State, and Action

상태 → option 선택 → 내부 정책 실행 → 종료 또는 중단 → 다음 결정.

## Objective and Training / Inference Boundary

위 설명은 초록에서 확인한 formulation이다. 정리의 가정·증명·구체적 갱신식은 본문 확인이 필요하다.

점검 항목: initiation·termination·closed-loop 조건·물리 시간 할인.

## Method-Specific Comparison — Researcher Interpretation

같은 행동열에서 고정 chunk와 상태 의존 종료를 분리해 discount·return의 정의를 대조한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://www.sciencedirect.com/science/article/pii/S0004370299000521). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
