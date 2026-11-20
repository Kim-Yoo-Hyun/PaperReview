# SOE: Sample-Efficient Robot Policy Self-Improvement via On-Manifold Exploration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

기존 policy의 action mode collapse와 무작위 perturbation이 유효한 탐색을 제한한다.

## Bottleneck and Changed Formulation

Task 관련 latent를 학습하고 유효한 행동 manifold에서 탐색하며 human-guided exploration을 지원한다.

## System and Robotics Loop

기본 policy에 추가하는 latent exploration 모듈이며 원 VLA 가중치의 공동 갱신과 구별해야 한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Manifold 학습 데이터·추가 supervision·policy update 방식·안전 주장 조건.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

저자 project는 robomimic의 4개 simulation task와 mug hanging·toaster loading·lamp capping 실제 과제를 제시한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2509.19292) · [저자 project/code](https://ericjin2002.github.io/SOE/) · [공식 code](https://github.com/EricJin2002/SOE). Exact objective, constraints, success definition은 본문 수동 확인 필요.
