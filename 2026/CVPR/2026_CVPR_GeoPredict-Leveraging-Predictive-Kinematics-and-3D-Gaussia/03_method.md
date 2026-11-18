# GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

로봇 keypoint trajectory와 3D Gaussian geometry 예측을 학습 supervision으로 사용한다.

## Observation–State–Action Interface

Motion history·영상에서 action을 생성하며 3D decoding은 학습용이다. 배포 query token과 native 3D reconstruction을 구별한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Depth supervision·keypoint target·배포 추가 token 비용·baseline data fairness.

Source가 명시한 evaluation 범위: RoboCasa Human-50·LIBERO·실세계 조작에서 geometry 관련 이득을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 policy/data에서 global geometry와 task-local geometry loss를 compute-matched 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html) · [저자 project/code](https://github.com/jingjingqian75/GeoPredict). 수식·세부 구현·코드 실행은 미검증이다.
