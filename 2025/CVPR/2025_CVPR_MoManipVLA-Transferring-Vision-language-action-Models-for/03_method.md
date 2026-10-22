# MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

VLA의 end-effector waypoint와 base–arm bi-level trajectory optimization을 연결한다.

## Observation–State–Action Interface

언어·관측 → waypoint → base/arm trajectory.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: waypoint frame, solver budget, controller, real-robot split.

Source가 명시한 evaluation 범위: OVMM 및 실제 로봇 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Base 고정과 이동 허용을 동일 waypoint·collision 조건에서 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html) · [저자 project/code](https://gary3410.github.io/momanipVLA/). 수식·세부 구현·코드 실행은 미검증이다.
