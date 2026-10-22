# LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Visual geometry backbone을 metric scale에 맞추고 history 기반 geometry를 복원하여 navigation policy를 conditioning한다.

## Observation–State–Action Interface

Historical visual observation → metric geometry/implicit localization memory → local trajectory.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 정책과 MPC가 각각 보는 pose, calibration, simulator GT 접근 및 metric scale supervision.

Source가 명시한 evaluation 범위: 저자 abstract/project는 simulation과 real-world navigation, obstacle avoidance 및 embodiment/environment generalization 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Geometry memory 유무를 동일 camera와 controller로 비교하고 pose noise·occlusion 하에서 success·collision·latency를 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2512.19629) · [저자 project/code](https://steinate.github.io/logoplanner.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
