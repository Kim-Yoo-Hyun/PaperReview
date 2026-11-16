# DataMIL: Selecting Data for Robot Imitation Learning with Datamodels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Datamodel로 policy 성능에 기여하는 데이터를 선택하며 task-specific surrogate로 선택 중 rollout 비용을 줄인다.

## Observation–State–Action Interface

Prior 시연·target 데이터·policy surrogate → subset → target imitation policy.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: surrogate 정의, target 데이터 누설, policy family 및 selector 비용.

Source가 명시한 evaluation 범위: OXE 선택을 포함한 simulation 및 실로봇 manipulation 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 target·budget에서 random, similarity, DataMIL 계열 선택을 먼저 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html) · [저자 project/code](https://github.com/UT-Austin-RobIn/datamil). 수식·세부 구현·코드 실행은 미검증이다.
