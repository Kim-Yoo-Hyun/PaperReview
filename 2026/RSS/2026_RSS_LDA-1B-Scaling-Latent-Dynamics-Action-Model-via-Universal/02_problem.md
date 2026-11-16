# LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

행동 모방만으로는 품질이 다양한 사람·로봇 데이터의 동역학 정보를 활용하기 어렵다.

## Bottleneck and Changed Formulation

구조화된 시각 latent에서 dynamics·policy·forecasting을 공동 학습하고 이질적 데이터를 통합한다.

## System and Robotics Loop

비동기 vision·action → multimodal diffusion transformer → 행동·미래 표현.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

저품질 데이터 정의, 데이터 역할별 objective, action/vision rate, 학습 데이터 중복.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 실제 contact-rich·dexterous·long-horizon 조작을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p210.html) · [저자 project/code](https://github.com/jiangranlv/LDA-1B). Exact objective, constraints, success definition은 본문 수동 확인 필요.
