# Colored Noise in PPO: Improved Exploration and Performance through Correlated Action Sampling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시간 상관을 갖는 colored noise로 stochastic action sampling을 바꾸고 noise color와 병렬 환경 수의 영향을 비교한다.

## Observation–State–Action Interface

On-policy stochastic actor의 action sampling을 바꾼다. VLA나 양팔 관계 학습을 직접 제안한 것은 아니다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 행동 likelihood와 trajectory correlation·noise 재사용·seed/환경 수.

Source가 명시한 evaluation 범위: On-policy RL의 correlated/white noise와 병렬 data 수집 조건을 비교한다. 이 조사에서 실제 로봇 trial은 확인하지 않았다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 variance·시간 상관·학습 예산에서 관계 조건과 고정 colored noise를 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/29139) · [저자 project/code](https://github.com/jkbjh/cn-ppo-paper-code). 수식·세부 구현·코드 실행은 미검증이다.
