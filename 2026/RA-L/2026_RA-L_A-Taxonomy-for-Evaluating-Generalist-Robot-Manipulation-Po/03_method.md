# A Taxonomy for Evaluating Generalist Robot Manipulation Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시각·의미·행동 변화를 분리하는 STAR-Gen taxonomy와 평가 지침을 제안한다.

## Observation–State–Action Interface

기본 과제 → 입력/필요 행동의 변화 축 → 축별 정책 평가.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 각 축의 동시 변화, base competence, in-domain adaptation과 평가 분할.

Source가 명시한 evaluation 범위: Bridge V2 기반 정책과 ALOHA 2의 실로봇 사례를 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

초기 관측을 맞춘 지시 쌍을 만들고 행동 필요성·성공 판정을 독립 확인한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2503.01238) · [저자 project/code](https://stargen-taxonomy.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
