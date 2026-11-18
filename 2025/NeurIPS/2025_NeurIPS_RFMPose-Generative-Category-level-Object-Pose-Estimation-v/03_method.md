# RFMPose: Generative Category-level Object Pose Estimation via Riemannian Flow Matching

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Riemannian flow와 geodesic 경로·optimal transport를 사용하며 likelihood 추정 경로를 제안한다.

## Observation–State–Action Interface

물체 관측의 category-level 6D pose 후보를 생성한다. Generative likelihood는 task 성공 확률과 별개다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Likelihood 구현·symmetry convention·공개 checkpoint·tracking 평가 조건.

Source가 명시한 evaluation 범위: Omni6DPose의 pose metric과 sim-to-real/추적 확장을 보고한다. 이번 등록에서는 정책 제어 trial을 추정하지 않는다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 K에서 top-score와 diversity-preserving 후보의 task-relevant coverage를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html) · [저자 project/code](https://github.com/shabiouyang/RMFPose). 수식·세부 구현·코드 실행은 미검증이다.
