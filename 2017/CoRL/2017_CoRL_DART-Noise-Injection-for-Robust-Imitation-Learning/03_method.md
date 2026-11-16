# DART: Noise Injection for Robust Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

전문가가 시연할 때 noise를 주입하고 학습 정책의 오류에 맞춰 noise 수준을 조절한다.

## Observation, State, and Action

교란된 시연 상황 → 전문가 복구 행동 → offline imitation 정책.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: noise 분포·전문가 회복 능력·개입 비용·train-test 교란.

## Method-Specific Comparison — Researcher Interpretation

동일 전문가 개입·시연 수로 정상 BC·교란 BC·RL을 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.mlr.press/v78/laskey17a.html). 공식 CoRL abstract 및 저자 project/code 공개 확인. 공개 repository의 simulation 구현과 실제 HSR 재현 경로는 구별한다.
