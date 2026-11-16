# DEAS: DEtached value learning with Action Sequence for Scalable Offline RL

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Action sequence를 critic에 쓰면 장기 문제의 horizon을 줄이면서도 가치 과대추정이 커질 수 있다.

## Bottleneck and Changed Formulation

행동 sequence 기반 가치 학습에 detached value learning을 적용하여 데이터 안의 고수익 행동으로 추정을 유도한다.

## System and Robotics Loop

Offline observation/action sequence → value estimation → sequence policy; VLA action chunk와 연결한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

value target gradient 경계, OOD action 처리, 실로봇 데이터·환경 예산.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

OGBench, RoboCasa Kitchen과 실세계 조작의 VLA 확장을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/68b7f71467c83d5d32275c5acbf6b588-Abstract-Conference.html) · [저자 project/code](https://changyeon.site/deas/) · [공식 code](https://github.com/csmile-1006/DEAS-Isaac-GR00T). Exact objective, constraints, success definition은 본문 수동 확인 필요.
