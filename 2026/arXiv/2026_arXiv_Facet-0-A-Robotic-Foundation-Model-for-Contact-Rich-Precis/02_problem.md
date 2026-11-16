# Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

정밀 조립에서 행동의 접촉 결과를 예측하고 실패에 적응해야 한다.

## Bottleneck and Changed Formulation

Joint action–wrench proposal과 distributional critic으로 접촉 결과를 학습하며 bounded actor가 현장 적응한다.

## System and Robotics Loop

Causal wrench 이력·vision-language·kinematics → 동작과 예측 wrench; wrench는 명령이 아니다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Frozen backbone/actor 경계, task adaptation 비용, 데이터 누출.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

세 embodiment의 force-synchronized corpus와 정밀 컴퓨터 조립 과제를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.01596) · [저자 project/code](https://pine-lab-ntu.github.io/facet-0/) · [공식 code](https://github.com/PINE-Lab-NTU/FACET). Exact objective, constraints, success definition은 본문 수동 확인 필요.
