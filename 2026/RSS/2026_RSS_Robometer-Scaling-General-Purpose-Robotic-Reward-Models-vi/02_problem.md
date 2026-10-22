# Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

성공·실패를 포함한 이질적 robot trajectory에서 범용 reward를 학습한다.

## Bottleneck and Changed Formulation

Progress supervision과 trajectory comparison을 결합한다.

## System and Robotics Loop

영상 trajectory·비교 정보 → progress/reward.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

policy version chronology, failure labels, reward training 중복, calibration.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

대규모 multi-robot 자료와 downstream 실제 robot RL을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p140.html) · [저자 project/code](https://robometer.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
