# Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

앞선 작업이 바꾼 물리 상태 때문에 새 목표 작업의 기존 능력에 접근하지 못할 수 있다.

## Bottleneck and Changed Formulation

목표 작업의 re-entry pose를 조건으로 frozen decoder를 통한 gradient를 이용해 action-stream 표현을 수정하고, 정책 자체가 복귀 행동을 생성하는 inference-time 개입을 제안한다.

## System and Robotics Loop

현재 상태·새 목표·re-entry pose → 동결 VLA 내부 표현 개입 → 복귀 행동과 목표 작업 실행. 재진술만 사용하는 언어 조건과 정보·개입 위치가 다르다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

re-entry pose 획득과 관측 접근, decoder별 개입 위치·계산 비용, 복귀/인계 조건, 실제 로봇 평가 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO-Goal, LIBERO-Object와 실제 xArm에서 instruction switching과 복구를 보고한다. 정확한 비교 수치·시행 수·특권 정보 조건은 신규 노트에서 본문 정독 완료로 표시하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.30913). Exact objective, constraints, success definition은 본문 수동 확인 필요.
