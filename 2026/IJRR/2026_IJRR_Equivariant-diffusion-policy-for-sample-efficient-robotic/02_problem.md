# Equivariant diffusion policy for sample-efficient robotic manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Diffusion policy의 복잡한 denoising 학습에는 많은 시연이 필요하다.

## Bottleneck and Changed Formulation

조작의 기하학적 대칭성을 denoising에 반영해 데이터 효율을 높인다.

## System and Robotics Loop

관측·noisy action trajectory → equivariant denoiser → action trajectory.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

적용 가능한 symmetry, 절대/상대 action, RGB/point-cloud 정보량, checkpoint 선택.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

MimicGen simulation과 실로봇 manipulation에서 소량 시연 학습을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://journals.sagepub.com/doi/10.1177/02783649261424445) · [저자 project/code](https://equidiff.github.io/) · [공식 code](https://github.com/pointW/equidiff). Exact objective, constraints, success definition은 본문 수동 확인 필요.
