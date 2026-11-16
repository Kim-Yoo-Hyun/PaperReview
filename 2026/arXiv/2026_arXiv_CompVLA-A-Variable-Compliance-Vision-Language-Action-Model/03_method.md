# CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Compliance Expert가 동작·강성·virtual displacement를 생성하고 geometric impedance로 실행한다.

## Observation–State–Action Interface

RGB·언어 → 동작과 시변 강성 행렬.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 강성–displacement 식별성, force 입력 유무, 데이터·controller 공정성.

Source가 명시한 evaluation 범위: 접촉 과제에서 vanilla/compliance-aware VLA 및 구성요소 ablation을 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 동작·gain 표현에서 imitation과 RL을 같은 초기화로 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.23614) · [저자 project/code](https://compvla.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
