# OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Household manipulation의 task success만으로는 robot·물체·환경의 손상을 평가할 수 없다.

## Bottleneck and Changed Formulation

Contact/thermal/fluid signal을 damage로 변환하는 DamageSim과 damage-aware household task benchmark를 제공한다.

## System and Robotics Loop

Physical simulator state/signal → damage observation/reward/termination → IL/RL 및 VLA evaluation.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Damage threshold/단위, simulator fidelity, user preference와 real-world damage validation.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RSS abstract는 OmniGibson과 RoboCasa 구현, safer demonstration, damage-conditioned IL/RL, VLA safety 및 sim-to-real use case를 설명한다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p098.html) · [저자 project/code](https://robin-lab.cs.utexas.edu/oopsieverse/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
