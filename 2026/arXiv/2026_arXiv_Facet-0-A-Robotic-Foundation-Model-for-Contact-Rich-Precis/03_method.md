# Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Joint action–wrench proposal과 distributional critic으로 접촉 결과를 학습하며 bounded actor가 현장 적응한다.

## Observation–State–Action Interface

Causal wrench 이력·vision-language·kinematics → 동작과 예측 wrench; wrench는 명령이 아니다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Frozen backbone/actor 경계, task adaptation 비용, 데이터 누출.

Source가 명시한 evaluation 범위: 세 embodiment의 force-synchronized corpus와 정밀 컴퓨터 조립 과제를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 데이터·접촉 관측에서 action-only와 action/gain 학습을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.01596) · [저자 project/code](https://pine-lab-ntu.github.io/facet-0/) · [공식 code](https://github.com/PINE-Lab-NTU/FACET). 수식·세부 구현·코드 실행은 미검증이다.
