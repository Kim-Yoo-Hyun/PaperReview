# TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA의 의미 모듈과 행동 모듈을 같은 속도로 갱신할 때 안정성과 제어 적응의 요구가 충돌한다.

## Bottleneck and Changed Formulation

VLM을 동결하고 semantic projection과 action expert를 서로 다른 빈도의 RL 갱신으로 적응한다.

## System and Robotics Loop

영상·지시 → 동결 VLM·적응 projection → RL action expert → 로봇 동작.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

학습 task-set·두 학습기의 데이터/gradient 경계·초기 능력·비용 정의.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

CALVIN과 실제 조작 과제에서 후학습 정책·갱신 전략을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2608.07314) · [저자 project/code](https://anonymous.4open.science/w/tempo-page/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
