# CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

기하 동작만 출력하는 VLA의 접촉 순응성 부족을 다룬다.

## Bottleneck and Changed Formulation

Compliance Expert가 동작·강성·virtual displacement를 생성하고 geometric impedance로 실행한다.

## System and Robotics Loop

RGB·언어 → 동작과 시변 강성 행렬.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

강성–displacement 식별성, force 입력 유무, 데이터·controller 공정성.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

접촉 과제에서 vanilla/compliance-aware VLA 및 구성요소 ablation을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.23614) · [저자 project/code](https://compvla.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
