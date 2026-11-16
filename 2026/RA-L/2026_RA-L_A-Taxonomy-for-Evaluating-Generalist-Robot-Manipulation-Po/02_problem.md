# A Taxonomy for Evaluating Generalist Robot Manipulation Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

서로 다른 일반화 조건을 하나의 성공률로 비교하면 정책의 취약 축이 가려진다.

## Bottleneck and Changed Formulation

시각·의미·행동 변화를 분리하는 STAR-Gen taxonomy와 평가 지침을 제안한다.

## System and Robotics Loop

기본 과제 → 입력/필요 행동의 변화 축 → 축별 정책 평가.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

각 축의 동시 변화, base competence, in-domain adaptation과 평가 분할.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Bridge V2 기반 정책과 ALOHA 2의 실로봇 사례를 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2503.01238) · [저자 project/code](https://stargen-taxonomy.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
