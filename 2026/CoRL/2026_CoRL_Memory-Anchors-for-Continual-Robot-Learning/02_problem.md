# Memory Anchors for Continual Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

새 task 적응 중 기존 robot 행동을 선택적으로 보존한다.

## Bottleneck and Changed Formulation

겹치는 latent representation에서 요구 action이 충돌하는 memory를 replay anchor로 사용한다.

## System and Robotics Loop

현재/과거 sample의 representation·action → replay 선택 → policy update.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

latent layer, action normalization, task order, replay step scaling.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO와 real-robot continual learning 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/forum?id=dSbtHPqFj9) · [저자 project/code](https://robot-adaptation.github.io/MemoryAnchors). Exact objective, constraints, success definition은 본문 수동 확인 필요.
