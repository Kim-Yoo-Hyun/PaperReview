# RFMPose: Generative Category-level Object Pose Estimation via Riemannian Flow Matching

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Category-level pose의 대칭과 다중 가능한 해를 한 점 추정만으로 표현하기 어렵다.

## Bottleneck and Changed Formulation

Riemannian flow와 geodesic 경로·optimal transport를 사용하며 likelihood 추정 경로를 제안한다.

## System and Robotics Loop

물체 관측의 category-level 6D pose 후보를 생성한다. Generative likelihood는 task 성공 확률과 별개다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Likelihood 구현·symmetry convention·공개 checkpoint·tracking 평가 조건.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Omni6DPose의 pose metric과 sim-to-real/추적 확장을 보고한다. 이번 등록에서는 정책 제어 trial을 추정하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html) · [저자 project/code](https://github.com/shabiouyang/RMFPose). Exact objective, constraints, success definition은 본문 수동 확인 필요.
