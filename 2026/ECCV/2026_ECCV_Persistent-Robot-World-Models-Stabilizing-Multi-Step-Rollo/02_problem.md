# Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Action-conditioned video world model의 autoregressive rollout에서 exposure bias 때문에 장기 prediction 품질이 저하되는 문제다.

## Bottleneck and Changed Formulation

자신이 생성한 history에 conditioning하며 여러 미래 rollout을 비교하는 RL post-training과 multi-view visual fidelity reward를 제안한다.

## System and Robotics Loop

Robot action + predicted video history → future multi-view video; 최적화 대상은 robot policy가 아니라 world model이다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Reward metric의 geometry/contact 민감도, rollout horizon, 실제 robot policy evidence 유무.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 abstract/project는 DROID에서 LPIPS/SSIM/PSNR 기반 rollout fidelity와 human preference 평가를 설명한다. Downstream policy improvement는 별도 검증 대상이다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2603.25685) · [저자 project/code](https://jaibardhan.com/persistworld/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
