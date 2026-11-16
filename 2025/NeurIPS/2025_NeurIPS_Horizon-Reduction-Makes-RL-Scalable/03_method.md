# Horizon Reduction Makes RL Scalable

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

Horizon 감소 기법을 비교하고 짧은 유효 결정 길이를 활용하는 SHARSA를 제안한다.

## Observation, State, and Action

대규모 goal-conditioned data → horizon을 줄인 value/policy 학습 → 목표 행동.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: 유효 결정 길이·coverage·데이터 크기·학습 계산량·물리 시간.

## Method-Specific Comparison — Researcher Interpretation

데이터·물리 시간·모델 크기를 맞춰 n-step return과 정책 chunk를 독립 변화시킨다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
