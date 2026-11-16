# SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

이진 성공 보상만으로는 실패 rollout의 진행 정보를 활용하기 어렵다.

## Bottleneck and Changed Formulation

같은 batch의 성공 궤적을 기준으로 world-model latent에서 실패의 진행 보상을 만든다.

## System and Robotics Loop

성공·실패 rollout → latent 진행 비교 → VLA 정책 갱신.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

성공 없는 batch 처리, world-model 사전학습 비용, 진행 측정 오류, reward scale.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO와 LIBERO-Plus에서 학습 효율·견고성을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
