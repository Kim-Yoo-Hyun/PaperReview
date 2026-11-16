# CoMo: Learning Continuous Latent Motion from Internet Videos for Scalable Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Discrete latent motion은 세밀한 연속 동작과 로봇 행동의 대응을 잃을 수 있다.

## Bottleneck and Changed Formulation

시간 차분과 temporal contrastive 학습으로 연속 motion latent를 얻는다.

## System and Robotics Loop

인터넷 영상 → motion pseudo-label → robot policy 공동 학습.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

정적 배경 shortcut, reverse-video negative의 유효성, action-label 없이 가능한 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Diffusion·autoregressive 정책의 simulation·실제 조작을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.html) · [저자 project/code](https://github.com/MCG-NJU/CoMo). Exact objective, constraints, success definition은 본문 수동 확인 필요.
