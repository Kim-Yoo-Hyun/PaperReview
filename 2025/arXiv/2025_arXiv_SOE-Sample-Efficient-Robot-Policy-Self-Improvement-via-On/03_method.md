# SOE: Sample-Efficient Robot Policy Self-Improvement via On-Manifold Exploration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Task 관련 latent를 학습하고 유효한 행동 manifold에서 탐색하며 human-guided exploration을 지원한다.

## Observation–State–Action Interface

기본 policy에 추가하는 latent exploration 모듈이며 원 VLA 가중치의 공동 갱신과 구별해야 한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Manifold 학습 데이터·추가 supervision·policy update 방식·안전 주장 조건.

Source가 명시한 evaluation 범위: 저자 project는 robomimic의 4개 simulation task와 mug hanging·toaster loading·lamp capping 실제 과제를 제시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

공통 policy·latent capacity·interaction budget에서 조건 없는 manifold와 관계 conditioning을 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2509.19292) · [저자 project/code](https://ericjin2002.github.io/SOE/) · [공식 code](https://github.com/EricJin2002/SOE). 수식·세부 구현·코드 실행은 미검증이다.
