# Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

3D foundation latent·2D semantic feature·proprioception을 합쳐 action chunk와 미래 3D latent를 공동 예측한다.

## Observation–State–Action Interface

RGB·proprioception → action chunk 및 dense point map으로 해석할 미래 latent. RL exploration covariance와 별개다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 미래 geometry target·3D foundation freeze 여부·양팔 action frame·data budget.

Source가 명시한 evaluation 범위: RoboTwin simulation과 실세계 양팔 조작에서 성공·협응·공간 예측을 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 action-geometry backbone과 데이터에서 독립/관계 조건 noise만 바꾼다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf) · [저자 project/code](https://github.com/Chongyang-99/GAP). 수식·세부 구현·코드 실행은 미검증이다.
