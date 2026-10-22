# Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

초기 관측 분포 차이 때문에 VLA가 실패하는 상황을 줄인다.

## Bottleneck and Changed Formulation

Active perception으로 관측을 맞추고 정렬된 continuation 자료로 adaptation한다.

## System and Robotics Loop

초기 영상·state → camera/관측 정렬 → VLA continuation.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

camera 행동 비용, state change, 성공 continuation 선택, data budget.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO와 실제 robot manipulation을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.23378). Exact objective, constraints, success definition은 본문 수동 확인 필요.
