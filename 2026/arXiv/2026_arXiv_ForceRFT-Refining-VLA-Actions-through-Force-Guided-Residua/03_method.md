# ForceRFT: Refining VLA Actions through Force-Guided Residual Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Frozen SmolVLA prior의 동작을 wrist-feedback residual RL로 보정하며 human correction과 autonomous TD를 분리한다.

## Observation–State–Action Interface

Wrist wrench·변화량·base motion → pose residual; critic은 autonomous 구간을 사용한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 개입 경계, 데이터 예산, force 관측 주기와 base chunk 비용.

Source가 명시한 evaluation 범위: 실제 plug·ring-on-peg·wiping에서 residual imitation을 포함한 기준선과 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 데이터에서 residual imitation/RL 및 feedback 제거를 교차 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.22840). 수식·세부 구현·코드 실행은 미검증이다.
