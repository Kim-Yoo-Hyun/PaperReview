# Exploring the Limits of Combinatorial Generalization in Embodied Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

독립적으로 수행할 수 있는 동작도 앞 동작이 남긴 상태에서 바로 이어 수행하기 어렵다.

## Bottleneck and Changed Formulation

RoboCombine은 단계 순서에 맞는 성공과 단계 간 전환을 측정한다. HSE는 계획·전환·행동을 나누며 PRTI는 개별 기술의 시작 상태를 확장한다.

## System and Robotics Loop

전체 지시 또는 하위 지시와 전환 신호가 실행 정책에 전달된다. 정답 전환을 제공하는 평가 트랙이 따로 있다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

각 트랙의 정답 신호, 단계별 분모, 자세 초기화 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공개 저장소의 19개 조합 과제와 세 트랙을 확인했다. 초록에 보고된 PRTI 비교는 정답 전환 시각을 준 조건이다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.15425) · [저자 project/code](https://github.com/AutoLab-SAI-SJTU/RoboCombine). Exact objective, constraints, success definition은 본문 수동 확인 필요.
