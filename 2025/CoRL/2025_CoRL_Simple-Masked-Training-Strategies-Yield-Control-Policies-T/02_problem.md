# Simple Masked Training Strategies Yield Control Policies That Are Robust to Sensor Failure

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

센서 결손이 배포된 robot policy의 행동을 불안정하게 만든다.

## Bottleneck and Changed Formulation

여러 sensor를 처리하는 encoder와 학습 중 modality dropout으로 결손에 대비한다.

## System and Robotics Loop

가용 sensor와 결손 처리 표현 → RL control policy.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

결손 종류·지속 시간·학습 노출, proprio와 image mask 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Locomotion과 manipulation, simulation과 실로봇의 sensor failure를 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/skand25a.html) · [저자 project/code](https://pvskand.github.io/projects/RME). Exact objective, constraints, success definition은 본문 수동 확인 필요.
