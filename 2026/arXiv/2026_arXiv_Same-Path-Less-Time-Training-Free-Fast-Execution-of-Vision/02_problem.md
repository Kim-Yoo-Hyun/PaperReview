# Same Path, Less Time: Training-Free Fast Execution of Vision-Language-Action Models under Inference Latency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

추론 대기와 느린 시연 속도로 인한 배포 시간 손실을 줄인다.

## Bottleneck and Changed Formulation

Frozen chunk policy에 경로 유지 time scaling을 적용해 비동기 추론과 실행 속도를 맞춘다.

## System and Robotics Loop

고정 VLA 행동 chunk·추론 지연 → 경로/진행도 정렬 → 속도 조절된 실행 명령.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

실제 지연과 주입 지연·동작 제한·gripper 동기화·실제 로봇 전이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO와 LIBERO-Dynamic에서 지연을 주입해 성공률과 task throughput을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2611.01390). Exact objective, constraints, success definition은 본문 수동 확인 필요.
