# πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Flow-Noise의 학습 가능한 noise 과정과 Flow-SDE의 ODE–SDE 변환을 대안으로 제시한다.

## Observation–State–Action Interface

Flow denoising과 environment interaction의 확률적 정책 인터페이스.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Flow-Noise/Flow-SDE 구분, likelihood 집계, normalizer와 update budget.

Source가 명시한 evaluation 범위: 여러 benchmark에서 ID/OOD 개선을 보고한다. 접촉 강성 학습 효과를 직접 입증한 것은 아니다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 source/초기화에서 action dimension별 log-prob·entropy·학습 비용을 확인한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2510.25889) · [저자 project/code](https://github.com/RLinf/RLinf). 수식·세부 구현·코드 실행은 미검증이다.
