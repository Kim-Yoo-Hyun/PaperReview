# Restoring the Right Stream: Training-Free OOD Robustness for Vision–Language–Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Frozen VLA에서 shift가 들어간 input stream에 맞는 보정을 적용한다.

## Bottleneck and Changed Formulation

Gated Per-Stream Manifold Restoration으로 visual/state 입력을 따로 복원한다.

## System and Robotics Loop

영상·proprioception·언어 → gated restoration → frozen policy.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

native state interface, gate oracle leakage, code·trial manifest 공개.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

OpenVLA-OFT와 LIBERO-Plus 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://www.mdpi.com/1099-4300/28/9/975) · [저자 project/code](https://www.mdpi.com/1099-4300/28/9/975). Exact objective, constraints, success definition은 본문 수동 확인 필요.
