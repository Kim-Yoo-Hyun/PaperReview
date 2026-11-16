# Delphic Offline Reinforcement Learning under Nonidentifiable Hidden Confounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

관측되지 않은 변수가 행동과 결과를 함께 바꾸면 offline 정책 평가가 편향된다.

## Bottleneck and Changed Formulation

관측과 양립하는 world model 간 차이로 confounding 불확실성을 정의하고 보수적 RL에 반영한다.

## System and Robotics Loop

offline trajectory → confounding/model uncertainty → pessimistic policy.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

비식별성 가정, uncertainty estimator, pessimism 수준, 의료→로봇 적용 한계.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Sepsis benchmark와 의료 기록에서 평가하며 robot/VLA 효과를 검증한 논문은 아니다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0b9ff9baa226af39f86045ecdc173672-Abstract-Conference.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
