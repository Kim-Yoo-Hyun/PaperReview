# How Should Vision-Language-Action Models Use Proprioceptive State?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

같은 flow-matching backbone에서 다섯 state interface와 history 길이를 통제한다.

## Observation–State–Action Interface

언어·영상·state/history → action chunk.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: world-frame localization 포함 여부, native state 사용, checkpoint 공개.

Source가 명시한 evaluation 범위: 45 atomic 및 20 composite task 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 slot 수의 repeated-current와 실제 history를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2608.03052) · 저자 프로젝트·코드 주소 미확인. 수식·세부 구현·코드 실행은 미검증이다.
