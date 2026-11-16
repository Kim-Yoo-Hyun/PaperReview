# SPRINT: Scalable Policy Pre-Training via Language Instruction Relabeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

다양한 언어 조건 기술을 사전학습하려면 사람이 많은 과제 지시를 작성해야 한다.

## Bottleneck and Changed Formulation

LLM을 이용한 지시 재라벨과 서로 다른 궤적의 기술 연결을 offline RL 사전학습에 사용한다.

## System and Robotics Loop

기존 trajectory·언어 지시 → 재라벨/연결된 기술 자료 → 정책 사전학습 → 새 과제 적응. 단일 VLA online RL이라고 가정하지 않는다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

cross-trajectory 연결의 유효성, downstream adaptation 예산, 시뮬레이터와 실로봇의 서로 다른 행동 interface, code의 실제 공개 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

저자 abstract는 가정용 시뮬레이터와 실제 로봇 주방 조작의 장기 과제 적응을 보고한다. 공개 저장소는 ALFRED-RL simulation 경로를 안내한다.

## Evidence Anchor

[공식 paper/abstract](https://doi.org/10.1109/ICRA57147.2024.10610606) · [저자 project/code](https://clvrai.github.io/sprint/) · [공식 code](https://github.com/clvrai/sprint). Exact objective, constraints, success definition은 본문 수동 확인 필요.
