# AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

물성 조건부 particle graph dynamics를 학습하고 online 상호작용으로 물성 변수를 조정한다.

## Observation–State–Action Interface

물체 particle·interaction → 물성 추정/dynamics → manipulation planning.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: particle extraction, 물성 식별 가능성, probe 비용.

Source가 명시한 evaluation 범위: 로프·입자·상자·천 등 real-world 물체의 예측과 조작을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

물성 적응 유무와 단순 feedback baseline을 같은 조작 목표에서 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss20/p010.html) · [저자 project/code](https://robopil.github.io/adaptigraph/) · [공식 code](https://github.com/Boey-li/AdaptiGraph). 수식·세부 구현·코드 실행은 미검증이다.
