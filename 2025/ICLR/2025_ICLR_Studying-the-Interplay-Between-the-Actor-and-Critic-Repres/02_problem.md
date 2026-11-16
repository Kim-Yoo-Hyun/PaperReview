# Studying the Interplay Between the Actor and Critic Representations in Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

정책과 가치 추정에 필요한 정보가 다를 때 표현을 공유할지 분리할지 다룬다.

## Bottleneck and Changed Formulation

공유/분리 표현과 각 역할의 전문화를 비교한다. 별도 critic은 탐색과 수집 데이터에도 영향을 준다고 보고한다.

## System and Robotics Loop

고차원 관측 → actor 행동·critic 가치 추정의 on-policy 학습.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

환경별 capacity·optimizer·data collection 통제, VLA에 그대로 적용 가능한 결론의 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 abstract의 표현·downstream 성능 비교까지 확인. 세부 환경·seed·수치·모델 용량 통제는 본문 대조 필요.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html) · [저자 project/code](https://github.com/francelico/deac-rep). Exact objective, constraints, success definition은 본문 수동 확인 필요.
