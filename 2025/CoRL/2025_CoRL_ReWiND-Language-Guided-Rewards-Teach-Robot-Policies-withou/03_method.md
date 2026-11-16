# ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

소규모 시연으로 언어 조건부 reward와 offline 정책을 학습하고 새 과제에 online 적응한다.

## Observation–State–Action Interface

영상·지시 → 학습 보상 → offline pretraining·online policy update.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 사전학습 시연·외부 데이터 사용량, reward leakage, 신규 과제별 인간 감독.

Source가 명시한 evaluation 범위: Simulation과 실제 양팔 조작의 미관측 과제 적응을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 초기 정책에 학습 보상과 환경 보상을 각각 사용하고 unseen instruction을 별도 평가한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/zhang25a.html) · [저자 project/code](https://rewind-reward.github.io/) · [공식 code](https://github.com/rewind-reward/ReWiND). 수식·세부 구현·코드 실행은 미검증이다.
