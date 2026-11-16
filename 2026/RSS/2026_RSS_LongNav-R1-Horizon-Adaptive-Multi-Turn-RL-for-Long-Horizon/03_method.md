# LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

환경과의 multi-turn 상호작용 및 horizon을 반영한 advantage 추정으로 VLA를 학습한다.

## Observation–State–Action Interface

시각 관측·상호작용 이력 → 항법 의사결정 → 환경 피드백.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: action 단위, episode 길이별 정규화, rollout 분모, 실제 로봇의 저수준 제어기.

Source가 명시한 evaluation 범위: Object navigation과 실제 장기 항법의 zero-shot 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 초기 정책·상호작용 수에서 advantage 계산과 history 사용만 각각 바꿔 길이별 성공을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p068.html) · [저자 project/code](https://github.com/UMich-CURLY/LongNav-R1). 수식·세부 구현·코드 실행은 미검증이다.
