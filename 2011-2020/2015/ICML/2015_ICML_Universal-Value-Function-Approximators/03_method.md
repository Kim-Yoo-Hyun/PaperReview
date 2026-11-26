# Universal Value Function Approximators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

상태와 목표를 입력으로 받는 가치함수와 분리된 embedding 학습을 제안하고 보상 기반 RL로 연결한다.

## Observation, State, and Action

상태 s·목표 g → 공유 가치 추정 V(s,g) → 목표 조건부 행동 선택.

## Objective and Training / Inference Boundary

위 설명은 초록에서 확인한 formulation이다. 정리의 가정·증명·구체적 갱신식은 본문 확인이 필요하다.

점검 항목: 목표 표현·목표 holdout·목표별 coverage·value와 policy 일반화의 구분.

## Method-Specific Comparison — Researcher Interpretation

같은 상태의 두 목표에서 분리·공유 value와 목표별 행동 선택을 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.mlr.press/v37/schaul15.html). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
