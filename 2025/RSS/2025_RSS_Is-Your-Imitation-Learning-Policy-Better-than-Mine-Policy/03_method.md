# Is Your Imitation Learning Policy Better than Mine? Policy Comparison with Near-Optimal Stopping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

순차 검정으로 비교를 멈출 시점을 결정한다.

## Observation–State–Action Interface

Policy별 binary success trial → sequential evidence → 중단/선택.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 독립성, indifference region, 오류 확률, 다중 비교 처리.

Source가 명시한 evaluation 범위: Simulation 및 실제 policy 비교를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

고정한 두 policy·독립 trial로 sequential vs fixed-budget 비교를 수행한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss21/p077.html). 수식·세부 구현·코드 실행은 미검증이다.
