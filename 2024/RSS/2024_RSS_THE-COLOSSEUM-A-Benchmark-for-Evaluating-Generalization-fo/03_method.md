# THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Manipulation task에 시각·물리 perturbation을 체계적으로 적용하는 simulation benchmark를 제시한다.

## Observation–State–Action Interface

Task·환경 변화 → manipulation policy → 조건별 성공.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 복합 요인 상호작용, simulator와 실세계 조건의 대응.

Source가 명시한 evaluation 범위: Simulation 비교와 대응 실세계 perturbation의 관련성을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

단일 perturbation과 결합 perturbation을 같은 초기 상태에서 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss20/p133.html) · [저자 project/code](https://robot-colosseum.github.io/) · [공식 code](https://github.com/robot-colosseum/robot-colosseum). 수식·세부 구현·코드 실행은 미검증이다.
