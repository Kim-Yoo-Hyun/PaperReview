# VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

실제 rollout으로 action-conditioned video world model을 개선하고 그 synthetic rollout으로 VLA를 개선하는 반복 학습을 제안한다.

## Observation–State–Action Interface

VLA action-conditioned video model → synthetic rollout; real rollout → world-model update → policy update.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Policy update objective, 실패 data 구성, synthetic/real 혼합비와 evaluation leakage.

Source가 명시한 evaluation 범위: ICML abstract는 실제 robot의 여러 downstream task에서 base policy 및 synthetic-rollout 학습 효과를 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Fixed world model, 반복 갱신 world model, real-data-only policy 학습을 동일 real-data budget으로 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/guo26i.html) · [저자 project/code](https://sites.google.com/view/vla-w). 수식·세부 구현·코드 실행은 미검증이다.
