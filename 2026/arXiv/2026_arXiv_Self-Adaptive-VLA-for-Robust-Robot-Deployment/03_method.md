# Self-Adaptive VLA for Robust Robot Deployment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

실패 rollout context를 encoder와 AdaLN으로 주입하고 여러 trial의 token을 합친다.

## Observation–State–Action Interface

영상·proprioception·action history → context-conditioned action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: episode/trial 간 offset 유지, encoder 모델, expert action 보상.

Source가 명시한 evaluation 범위: 정밀 bimanual·dexterous 작업의 actuation bias와 encoder offset 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 관측·실패 trial 예산으로 static-context와 online history를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.30092) · [저자 project/code](https://icefoxzhx.github.io/self-adaptive-vla/). 수식·세부 구현·코드 실행은 미검증이다.
