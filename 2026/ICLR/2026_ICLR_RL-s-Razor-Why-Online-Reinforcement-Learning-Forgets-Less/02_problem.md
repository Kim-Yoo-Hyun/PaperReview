# RL's Razor: Why Online Reinforcement Learning Forgets Less

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

새 과제를 학습할 때 기존 정책의 능력이 보존되는 조건을 묻는다.

## Bottleneck and Changed Formulation

같은 신규 과제 성능에서 RL과 SFT의 망각·정책 KL을 비교하고 on-policy RL의 작은 분포 변화 편향을 분석한다.

## System and Robotics Loop

기존 정책 → RL/SFT 후학습 정책 → 신규·기존 과제 행동 평가.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

KL 방향·평가 관측 분포·기존 능력 정의·단순 학습률/모방 대안.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

언어 모델과 로봇 foundation model에서 적응 성능과 기존 능력 보존을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/618c95f4557c15b253fb0e6f548ea0c0-Abstract-Conference.html) · [저자 project/code](https://jyopari.github.io/posts/rl_razor). Exact objective, constraints, success definition은 본문 수동 확인 필요.
