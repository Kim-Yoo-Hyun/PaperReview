# Tac2Real: Reliable and GPU Visuotactile Simulation for Online Reinforcement Learning and Zero-Shot Real-World Deployment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Visuotactile online RL simulation에서 contact physics fidelity와 GPU throughput을 동시에 확보하는 문제다.

## Bottleneck and Changed Formulation

PNCG-IPC 기반 tactile simulation, multi-GPU 병렬화 및 TacAlign sim-to-real alignment를 결합한다.

## System and Robotics Loop

Contact dynamics → tactile marker displacement/visual signal → RL policy → insertion action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Tactile sensor calibration, contact parameter 분포, marker fidelity와 code 공개 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 abstract/project는 contact-rich peg insertion의 zero-shot real-world transfer 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2603.28475) · [저자 project/code](https://ningyurichard.github.io/tac2real-project-page/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
