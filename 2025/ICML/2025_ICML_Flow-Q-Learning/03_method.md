# Flow Q-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Flow-matching behavior model과 distilled one-step actor를 결합하여 value maximization과 expressive behavior regularization을 연결한다.

## Observation–State–Action Interface

Offline state/image-action data → flow policy 및 one-step actor → continuous action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Critic target, actor distillation loss, OOD action 제약과 online data 혼합비.

Source가 명시한 evaluation 범위: 공식 abstract는 OGBench와 D4RL의 state/pixel offline 및 offline-to-online task 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

OGBench manipulation 한 task에서 FQL과 IQL을 같은 data로 비교하고, distillation/regularization 변화에 따른 return·sample efficiency·latency를 확인한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v267/park25f.html) · [저자 project/code](https://seohong.me/projects/fql/). 수식·세부 구현·코드 실행은 미검증이다.
