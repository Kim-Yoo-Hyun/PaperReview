# OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Contact/thermal/fluid signal을 damage로 변환하는 DamageSim과 damage-aware household task benchmark를 제공한다.

## Observation–State–Action Interface

Physical simulator state/signal → damage observation/reward/termination → IL/RL 및 VLA evaluation.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Damage threshold/단위, simulator fidelity, user preference와 real-world damage validation.

Source가 명시한 evaluation 범위: RSS abstract는 OmniGibson과 RoboCasa 구현, safer demonstration, damage-conditioned IL/RL, VLA safety 및 sim-to-real use case를 설명한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 VLA checkpoint와 task에서 task-only와 damage-aware evaluation을 비교하고 성공 여부와 damage를 별도 보고한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p098.html) · [저자 project/code](https://robin-lab.cs.utexas.edu/oopsieverse/). 수식·세부 구현·코드 실행은 미검증이다.
