# PROGRESSOR: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Video에서 robot 학습에 쓸 progress reward를 얻는다.

## Bottleneck and Changed Formulation

초기·현재·목표 관측으로 progress를 추정하고 online refinement한다.

## System and Robotics Loop

영상 triplet → progress 추정 → robot reward.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

goal image 정보, refinement 데이터, train/test overlap, reward scale.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Human video와 실제 로봇 offline RL 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Ayalew_PROGRESSOR_A_Perceptually_Guided_Reward_Estimator_with_Self-Supervised_Online_Refinement_ICCV_2025_paper.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
