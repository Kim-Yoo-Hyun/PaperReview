# Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

소량 시연 SFT 뒤 VLA가 학습 물체·공간에 고착되어 새로운 지시를 따르지 못한다.

## Bottleneck and Changed Formulation

후학습 중 시각 grounding을 보존하고 추론 시 contrastive prompt guidance로 denoising을 조절한다.

## System and Robotics Loop

영상·언어 → 시각 grounding을 보존한 VLA → 지시 조건부 동작.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

시각 보존 손실·guidance 입력·새 지시 split·RL과 SFT의 데이터/비용 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 실제 로봇의 여덟 평가에서 새로운 지시에 대한 일반화를 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2604.23121) · [저자 project/code](https://suninghuang19.github.io/delock_page/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
