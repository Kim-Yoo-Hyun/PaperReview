# Robotic task success evaluation under multi-modal non-parametric object pose uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

정확한 pose가 아니어도 task가 성공할 수 있으므로 pose error만으로 행동 여부를 결정하기 어렵다.

## Bottleneck and Changed Formulation

Simulation으로 허용 pose-error 공간을 미리 구하고 다봉 추정 오차 분포와 적분해 task 성공 가능성을 계산한다.

## System and Robotics Loop

Pose uncertainty와 task-specific acceptable-error 공간에서 성공 가능성을 얻는다. VLA 표현 학습은 별도다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

허용 오차 precompute 비용·동역학 전제·online pose distribution·최종본과 preprint 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 publisher 초록은 두 mobile manipulation task의 성공/실패 평가를 명시한다.

## Evidence Anchor

[공식 paper/abstract](https://www.emerald.com/ir/article-abstract/52/5/651/1254840/Robotic-task-success-evaluation-under-multi-modal?redirectedFrom=PDF). Exact objective, constraints, success definition은 본문 수동 확인 필요.
