# Robust and Scalable Autonomous Reinforcement Learning in Irreversible Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

자율 RL에서 초기·목표 state 다양성과 비가역 실패를 함께 다룬다.

## Bottleneck and Changed Formulation

학습 진전에 따른 curriculum과 행동 기반 비가역성 식별을 결합한다.

## System and Robotics Loop

Forward/reset 경험 → informative state 선택·위험 회피.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

irreversibility 정의, behavior encoding, task-specific 정보, reset 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

가역/비가역 환경에서 성능과 manual reset 감소를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/56d748a1d7128158681280be7668e0d3-Abstract-Conference.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
