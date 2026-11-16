# VLA-R1: Enhancing Reasoning in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Action 생성만 감독하면 affordance·기하 관계를 고려하는 명시적 추론이 약할 수 있다.

## Bottleneck and Changed Formulation

CoT 데이터와 region alignment·trajectory consistency·format reward를 사용한 GRPO 후학습을 결합한다.

## System and Robotics Loop

시각·지시 → affordance region·trajectory와 reasoning → downstream robot control. 직접 joint action 최적화와 구분한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

annotation 접근, downstream controller의 역할, execution feedback 사용 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

In/out-of-domain, simulation과 실로봇 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2510.01623) · [저자 project/code](https://gigaai-research.github.io/VLA-R1/) · [공식 code](https://github.com/GigaAI-research/VLA-R1). Exact objective, constraints, success definition은 본문 수동 확인 필요.
