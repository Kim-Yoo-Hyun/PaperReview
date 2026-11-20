# CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Sensor availability와 task intent를 이용해 sparse expert를 routing한다.

## Observation–State–Action Interface

RGB·언어·proprioception·optional depth → action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: v2 depth degradation 평가, availability indicator, 공식 CoRL 채택 확인.

Source가 명시한 evaluation 범위: LIBERO, RoboCasa GR1, 실제 dual-arm 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Known missingness와 present-but-corrupt 조건을 같은 정보로 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2607.03693) · 저자 프로젝트·코드 주소 미확인. 수식·세부 구현·코드 실행은 미검증이다.
