# Dichotomous Diffusion Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Diffusion 정책의 직접 value 최대화는 불안정하고 likelihood 근사는 비용이 크다.

## Bottleneck and Changed Formulation

보상 최대화·최소화 diffusion policy를 따로 학습하고 score의 선형 결합으로 추론 greediness를 조절한다.

## System and Robotics Loop

Offline transition → 두 diffusion score → 결합된 action generation.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

두 모델의 추가 계산량, 추론 결합 계수 선택, manipulation 전이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

ExORL·OGBench의 offline 및 offline-to-online RL과 NAVSIM 자율주행 VLA를 평가한다. 주행 VLA 결과를 조작 VLA의 근거로 확대하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/64a0192102e1421a2b2c15ae0bdb9f3a-Abstract-Conference.html) · [저자 project/code](https://lrmbbj.github.io/DIPOLE/) · [공식 code](https://github.com/LRMbbj/DIPOLE). Exact objective, constraints, success definition은 본문 수동 확인 필요.
