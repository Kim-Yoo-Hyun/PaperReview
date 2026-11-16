# Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

명시적 긴 chain-of-thought는 행동 결정을 지연시킨다.

## Bottleneck and Changed Formulation

Teacher의 언어·시각 계획을 preference-guided distillation으로 압축하여 verbalizable latent reasoning을 학습한다.

## System and Robotics Loop

관측·지시 → compact latent plan → action model. 압축된 추론과 action model의 연결을 구분한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

teacher 감독 비용, action model 별도 학습 여부, end-to-end latency.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Embodied manipulation·reasoning benchmark의 latency와 장기 계획·적응·복구를 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Fast-ThinkAct_Efficient_Vision-Language-Action_Reasoning_via_Verbalizable_Latent_Planning_CVPR_2026_paper.html) · [저자 project/code](https://jasper0314-huang.github.io/fast-thinkact/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
