# Universal Pose Pretraining for Generalizable Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VQA 중심 표현과 희소한 로봇 action supervision이 세밀한 3D 상태 차이를 학습하기 어렵게 한다.

## Bottleneck and Changed Formulation

Camera-centric pose token으로 공간·trajectory 사전학습을 한 뒤 로봇 action space에 적응한다.

## System and Robotics Loop

3D pose·trajectory supervision으로 표현을 학습하고 embodiment별 행동을 출력한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

3D 데이터 규모·pose supervision·camera convention·test object 중복.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 초록은 RoboTwin 2.0·LIBERO 및 실세계 물체 일반화 실험을 명시한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p145.html) · [저자 project/code](https://hetolin.github.io/PoseVLA/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
