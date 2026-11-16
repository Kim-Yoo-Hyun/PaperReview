# AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

새로운 물성의 deformable 물체를 예측하고 조작하기 어렵다.

## Bottleneck and Changed Formulation

물성 조건부 particle graph dynamics를 학습하고 online 상호작용으로 물성 변수를 조정한다.

## System and Robotics Loop

물체 particle·interaction → 물성 추정/dynamics → manipulation planning.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

particle extraction, 물성 식별 가능성, probe 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

로프·입자·상자·천 등 real-world 물체의 예측과 조작을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss20/p010.html) · [저자 project/code](https://robopil.github.io/adaptigraph/) · [공식 code](https://github.com/Boey-li/AdaptiGraph). Exact objective, constraints, success definition은 본문 수동 확인 필요.
