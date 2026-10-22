# PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

State와 robot action을 3D point flow 공간에서 연결하고 action-conditioned scene dynamics를 학습한다.

## Observation–State–Action Interface

RGB-D capture + robot action의 point-flow 표현 → scene 3D point flow → MPC action selection.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: RGB-D calibration, point-flow action 변환, partial observability와 MPC cost 정의.

Source가 명시한 evaluation 범위: CVF abstract/저자 project는 real/sim training data와 Franka의 pushing·deformable/articulated manipulation·tool use 평가를 설명한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

간단한 pushing task에서 3D model과 visual model의 action ranking을 비교하고 prediction error와 실제 goal error를 함께 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf) · [저자 project/code](https://point-world.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
