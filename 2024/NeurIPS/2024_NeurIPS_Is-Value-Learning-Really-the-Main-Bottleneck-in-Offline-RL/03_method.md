# Is Value Learning Really the Main Bottleneck in Offline RL?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

Value learning·policy extraction·test-state 일반화를 분리해 비교하고 policy 개선 대안을 분석한다.

## Observation, State, and Action

같은 offline data·가치함수 → 서로 다른 policy extraction → ID/OOD 상태 행동.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: critic 고정·extraction 예산·평가 state coverage·test-time 최적화 비용.

## Method-Specific Comparison — Researcher Interpretation

같은 고정 critic에서 weighted BC와 behavior-constrained policy gradient만 바꾼다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ffb4e3118280a66b192b6f06e0e2596-Abstract-Conference.html). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
