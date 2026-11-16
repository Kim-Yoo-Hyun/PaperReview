# RehearseVLA: Simulated Post-Training for VLAs with Physically-Consistent World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

현실 reset 비용과 부족한 시연이 VLA online 후학습을 제한한다.

## Bottleneck and Changed Formulation

물리 일관성을 지향한 world simulator와 보상·종료를 판단하는 VLM reflector를 구성한다.

## System and Robotics Loop

행동 → 미래 영상 예측 → 보상·종료 판단 → VLA 후학습.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

실제/가상 rollout 분모, 물리 일관성 검증, reflector의 감독 비용, 종료 오탐.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

소수 시연 조건의 복잡한 로봇 조작 개선을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html) · [저자 project/code](https://github.com/iSEE-Laboratory/RehearseVLA). Exact objective, constraints, success definition은 본문 수동 확인 필요.
