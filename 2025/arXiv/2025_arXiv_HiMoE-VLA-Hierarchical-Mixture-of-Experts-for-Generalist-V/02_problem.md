# HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

서로 다른 action space를 가진 데이터의 negative transfer를 줄인다.

## Bottleneck and Changed Formulation

Action-space별 expert와 공유 처리의 계층적 mixture를 구성한다.

## System and Robotics Loop

언어·영상·embodiment/action-space 정보 → expert routing → action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

routing에 쓰는 robot ID, contrastive objective, load balance, parameter 예산.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

CALVIN·LIBERO 및 실제 로봇 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2512.05693) · [저자 project/code](https://github.com/ZhiyingDu/HiMoE-VLA). Exact objective, constraints, success definition은 본문 수동 확인 필요.
