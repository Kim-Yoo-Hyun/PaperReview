# Universal Value Function Approximators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

상태뿐 아니라 목표가 달라질 때도 하나의 가치함수를 일반화한다.

## Formulation and Robotics Loop

상태 s·목표 g → 공유 가치 추정 V(s,g) → 목표 조건부 행동 선택.

상태와 목표를 입력으로 받는 가치함수와 분리된 embedding 학습을 제안하고 보상 기반 RL로 연결한다.

## Assumptions to Verify

목표 표현·목표 holdout·목표별 coverage·value와 policy 일반화의 구분.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

TD/value approximation → UVFA → HER·HIQL·OGBench와 목표별 보존 진단.

HER·HIQL·목표 조건부 critic과 단일 VLA의 지시별 가치 표현을 이해하는 원전이므로 CORE다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.mlr.press/v37/schaul15.html). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
