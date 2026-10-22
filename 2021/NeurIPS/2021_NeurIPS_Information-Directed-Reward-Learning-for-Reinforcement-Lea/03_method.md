# Information Directed Reward Learning for Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

잠재 최적 정책 간 return 차이에 대한 information gain으로 query를 선택한다.

## Observation–State–Action Interface

Bayesian reward belief·policy 후보 → query → expert feedback.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: reward prior, policy 후보 생성, expert noise, compute 비용.

Source가 명시한 evaluation 범위: 여러 환경과 query 유형에서 label efficiency를 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 feedback 예산에서 random·uncertainty·IDRL 계열을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper/2021/hash/1fa6269f58898f0e809575c9a48747ef-Abstract.html). 수식·세부 구현·코드 실행은 미검증이다.
