# Learning from Hindsight for VLA Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

원 지시 실패에만 보상 0을 주면 실제 수행한 유용한 행동도 VLA 강화학습에 활용하지 못한다.

## Bottleneck and Changed Formulation

VLM으로 실패에서 달성한 행동을 보조 언어 목표로 붙이고 원 과제와 함께 정책을 학습한다.

## System and Robotics Loop

관측·원 지시 → VLA 행동; 수집 후 rollout을 VLM이 해석하여 보조 목표와 학습 신호를 만든다. 배포 제어기와 학습 relabeler를 구분한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

v2의 importance correction·label filtering·모방 대조와 우리 selector의 정확한 차이, VLM 감독 비용과 rollout 분모, 원 지시 평가 독립성.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

v2 abstract는 LIBERO-PRO의 분포 이동 조작과 실제 Franka 학습을 보고한다. 샘플 효율 개선은 해당 비교 조건의 저자 주장이다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2607.09042) · [저자 project/code](https://iamxjy.github.io/lfh-website/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
