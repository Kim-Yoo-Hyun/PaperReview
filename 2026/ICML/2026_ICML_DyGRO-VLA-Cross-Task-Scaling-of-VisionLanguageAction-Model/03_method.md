# DyGRO-VLA: Cross-Task Scaling of Vision–Language–Action Models via Dynamic Grouped Residual Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Cross-task latent representation과 mixture-of-RL-residuals를 이용한 두 단계 grouped residual optimization을 제안한다.

## Observation–State–Action Interface

VLA observation/language → cross-task latent features 및 residual policy update → robot action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Task grouping, residual routing, representation loss와 unseen split leakage.

Source가 명시한 evaluation 범위: ICML abstract는 LIBERO, RoboTwin2와 real-world 평가 및 multitask/distribution-shift 조건을 명시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 base VLA에서 standard RL과 DyGRO-VLA를 비교하고 seen/unseen task 성공률과 representation 변화·추론 비용을 기록한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/lin26af.html) · [저자 project/code](https://github.com/EDEM-AI/DyGRO-VLA). 수식·세부 구현·코드 실행은 미검증이다.
