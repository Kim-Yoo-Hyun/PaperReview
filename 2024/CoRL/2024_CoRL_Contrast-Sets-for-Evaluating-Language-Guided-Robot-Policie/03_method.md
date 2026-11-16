# Contrast Sets for Evaluating Language-Guided Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

기존 test instance에 작고 구체적인 변화를 주는 contrast set으로 성능과 평가 노력의 관계를 분석한다.

## Observation–State–Action Interface

동일한 과제 주변의 지시·장면 변형 → language-guided policy → 행동 차이 평가.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 대조쌍 난이도·유효성 검수, 평가자 노력의 정의, 물리 reset 재현성.

Source가 명시한 evaluation 범위: 시뮬레이션 조작과 물리 로봇의 vision-and-language navigation을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 scene의 지시 대조쌍을 구성하고 학습 전후 paired success와 instruction-consistency를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/anwar25a.html). 수식·세부 구현·코드 실행은 미검증이다.
