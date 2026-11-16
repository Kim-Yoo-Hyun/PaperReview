# DataMIL: Selecting Data for Robot Imitation Learning with Datamodels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

대규모 prior 데이터의 무차별 co-training이 개별 target task를 악화시킬 수 있다.

## Bottleneck and Changed Formulation

Datamodel로 policy 성능에 기여하는 데이터를 선택하며 task-specific surrogate로 선택 중 rollout 비용을 줄인다.

## System and Robotics Loop

Prior 시연·target 데이터·policy surrogate → subset → target imitation policy.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

surrogate 정의, target 데이터 누설, policy family 및 selector 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

OXE 선택을 포함한 simulation 및 실로봇 manipulation 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html) · [저자 project/code](https://github.com/UT-Austin-RobIn/datamil). Exact objective, constraints, success definition은 본문 수동 확인 필요.
