# DialogVLA: Bridging Reasoning Action in Bimanual Manipulation via Parallel Mixture-of-Experts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Structured dialog와 parallel skill/arm MoE가 flow action expert를 조건화한다.

## Observation–State–Action Interface

Multi-view·언어·proprioception → 양팔 action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 공식 proceedings, 원문 공개, source version, code release.

Source가 명시한 evaluation 범위: 저자 project는 RoboTwin, RoboCasa GR1 및 실제 양팔 평가를 제시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 양팔 task에서 role routing 제거 ablation을 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://jjjenghi.github.io/dialogvla/) · [저자 project/code](https://jjjenghi.github.io/dialogvla/). 수식·세부 구현·코드 실행은 미검증이다.
