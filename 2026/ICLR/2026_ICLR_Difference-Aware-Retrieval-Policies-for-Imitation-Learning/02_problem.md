# Difference-Aware Retrieval Policies for Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Behavior cloning의 전역 state-to-action mapping은 배포 분포 변화에서 누적 오차를 겪는다.

## Bottleneck and Changed Formulation

시연의 가까운 상태·행동 및 query와의 상대 차이를 이용하는 semi-parametric policy를 학습한다.

## System and Robotics Loop

Query state·이웃 시연·상대 벡터 → action prediction.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

이웃 수, history 사용, retrieval 지연과 rollout split.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Continuous control과 manipulation, 고차원 시각 표현에서 BC와 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html) · [저자 project/code](https://weirdlabuw.github.io/darp-site/) · [공식 code](https://github.com/WEIRDLabUW/darp). Exact objective, constraints, success definition은 본문 수동 확인 필요.
