# ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

결정론적 flow 생성 경로를 online policy-gradient 학습과 탐색에 연결할 때 확률 계산과 적은 생성 step의 안정성이 필요하다.

## Bottleneck and Changed Formulation

Flow 경로에 학습 가능한 잡음을 넣어 이산 시간 확률 과정으로 바꾸고 정책 likelihood를 사용해 online RL 후학습한다.

## System and Robotics Loop

관측 → flow velocity와 학습용 noise → 생성된 연속 행동. 정책 생성 과정의 확률과 물리 행동의 주변 밀도를 구분해 읽어야 한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

생성 경로 likelihood와 action likelihood의 차이, DPPO 비교의 모델/자료/시간 통제, noise 학습과 step 축소 효과, 실제 로봇 평가 여부.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 abstract는 locomotion과 state/visual manipulation에서 Rectified Flow·Shortcut 정책 후학습을 보고한다. 최신 저장소의 VLA 지원을 원 논문 실험으로 소급하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/98d6f928497d9eaad9f320fb2db3040d-Abstract-Conference.html) · [저자 project/code](https://reinflow.github.io/) · [공식 code](https://github.com/ReinFlow/ReinFlow). Exact objective, constraints, success definition은 본문 수동 확인 필요.
