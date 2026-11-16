# ActMem-VLA: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

현재 관측이 비슷한 서로 다른 작업 단계에서 행동이 모호해지는 문제를 다룬다.

## Bottleneck and Changed Formulation

Mamba 행동 이력 memory와 PreAction Expert를 학습하고 frozen action expert에 denoising을 넘긴다.

## System and Robotics Loop

실행 행동 이력·현재 맥락 → memory/PAE → frozen AE의 행동 refinement.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

memory reset·실제 실행 이력의 정의·효과 피드백 접근권·분할과 예산.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO-Mem과 네 실제 조작 과제에서 memory 및 기존 VLA와 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.37307). Exact objective, constraints, success definition은 본문 수동 확인 필요.
