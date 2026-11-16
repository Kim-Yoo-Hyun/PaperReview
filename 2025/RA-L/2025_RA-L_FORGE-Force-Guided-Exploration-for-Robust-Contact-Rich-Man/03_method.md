# FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation Under Uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Force threshold와 dynamics randomization으로 sim-to-real 접촉 정책을 학습하고 성공을 예측한다.

## Observation–State–Action Interface

관측·허용 force 조건 → 접촉 동작·성공 예측.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: pose uncertainty 범위, gain randomization, 독립 실환경 trials.

Source가 명시한 evaluation 범위: 삽입·gear meshing·nut threading과 snap-fit/다단계 조립을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 관측·force ceiling·환경 비용의 비-VLA RL과 VLA RL을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/10925874/) · [저자 project/code](https://noseworm.github.io/forge/). 수식·세부 구현·코드 실행은 미검증이다.
