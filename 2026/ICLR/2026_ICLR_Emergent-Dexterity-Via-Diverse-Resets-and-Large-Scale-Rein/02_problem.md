# Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

접촉 조작 RL이 좁은 상태 영역만 반복하면 계산량을 늘려도 장기 탐색이 정체된다.

## Bottleneck and Changed Formulation

다양한 robot-object 상호작용 reset을 프로그램으로 생성하고 공통 보상으로 RL을 학습한 뒤 visuomotor 정책으로 증류한다.

## System and Robotics Loop

다양한 simulator reset → RL 정책 → 시각 정책 증류 → 실제 로봇.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

reset 생성의 물리 유효성·특권 정보, 증류 비용, 초기 조건 분할.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

장기 dexterous manipulation과 넓은 초기 조건, zero-shot 실로봇 전이를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8e3e3488623d64c493a7f11cf1f2e49f-Abstract-Conference.html) · [저자 project/code](https://omnireset.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
