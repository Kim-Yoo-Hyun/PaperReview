# RLux-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA RL 구현이 model·algorithm·simulator마다 분리되어 공정한 비교와 효율적인 scaling이 어려운 문제다.

## Bottleneck and Changed Formulation

VLA/RL/simulator 공통 interface와 rendering·inference·training 자원 할당 구조를 제공한다.

## System and Robotics Loop

Simulator observation/reward → VLA rollout → training worker; resource allocation과 policy interface를 분리한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Model별 action interface, GPU utilization 산정, asynchronous policy lag.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RSS abstract는 LIBERO, ManiSkill, RoboTwin simulation에서 training efficiency와 policy 성능을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p089.html) · [저자 project/code](https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst). Exact objective, constraints, success definition은 본문 수동 확인 필요.
