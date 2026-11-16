# HIQL: Offline Goal-Conditioned RL with Latent States as Actions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

하나의 action-free 가치함수에서 latent subgoal 정책과 그 목표에 도달하는 하위 정책을 추출한다.

## Observation, State, and Action

상태·최종 목표 → latent subgoal → 실제 행동; 공유 value에서 두 정책 학습.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: goal relabeling·latent 목표 표현·subgoal 거리·action-free 데이터 범위.

## Method-Specific Comparison — Researcher Interpretation

같은 data/value/compute에서 평면 정책과 subgoal 정책의 horizon별 오류를 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6d7c4a0727e089ed6cdd3151cbe8d8ba-Abstract-Conference.html). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
