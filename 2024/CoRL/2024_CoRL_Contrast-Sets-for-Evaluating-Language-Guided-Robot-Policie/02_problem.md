# Contrast Sets for Evaluating Language-Guided Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

작은 실로봇 시연 집합만으로 언어 지시 일반화의 취약점을 찾기 어렵다.

## Bottleneck and Changed Formulation

기존 test instance에 작고 구체적인 변화를 주는 contrast set으로 성능과 평가 노력의 관계를 분석한다.

## System and Robotics Loop

동일한 과제 주변의 지시·장면 변형 → language-guided policy → 행동 차이 평가.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

대조쌍 난이도·유효성 검수, 평가자 노력의 정의, 물리 reset 재현성.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

시뮬레이션 조작과 물리 로봇의 vision-and-language navigation을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/anwar25a.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
