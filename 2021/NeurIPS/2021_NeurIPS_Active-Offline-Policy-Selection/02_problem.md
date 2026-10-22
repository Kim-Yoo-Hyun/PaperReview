# Active Offline Policy Selection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Offline data가 있지만 online 평가 예산이 작은 상황에서 policy를 고른다.

## Bottleneck and Changed Formulation

OPE로 초기화하고 policy similarity 기반 Bayesian 선택으로 다음 평가를 배분한다.

## System and Robotics Loop

Logged data·policy 후보·평가 결과 → 다음 policy 선택.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

kernel 입력, adaptive reuse, candidate chronology, online budget.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

여러 benchmark와 다수 후보 정책의 selection 효율을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
