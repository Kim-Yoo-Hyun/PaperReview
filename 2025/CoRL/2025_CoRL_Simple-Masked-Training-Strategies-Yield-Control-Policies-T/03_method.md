# Simple Masked Training Strategies Yield Control Policies That Are Robust to Sensor Failure

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

여러 sensor를 처리하는 encoder와 학습 중 modality dropout으로 결손에 대비한다.

## Observation–State–Action Interface

가용 sensor와 결손 처리 표현 → RL control policy.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 결손 종류·지속 시간·학습 노출, proprio와 image mask 차이.

Source가 명시한 evaluation 범위: Locomotion과 manipulation, simulation과 실로봇의 sensor failure를 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 센서와 dropout 예산에서 masked training과 추가 adaptive fusion을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/skand25a.html) · [저자 project/code](https://pvskand.github.io/projects/RME). 수식·세부 구현·코드 실행은 미검증이다.
