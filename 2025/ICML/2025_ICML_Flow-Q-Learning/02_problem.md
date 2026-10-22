# Flow Q-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

복잡한 multimodal action 분포를 갖는 flow policy에 offline Q-learning을 적용할 때 효율적인 actor 최적화가 필요하다.

## Bottleneck and Changed Formulation

Flow-matching behavior model과 distilled one-step actor를 결합하여 value maximization과 expressive behavior regularization을 연결한다.

## System and Robotics Loop

Offline state/image-action data → flow policy 및 one-step actor → continuous action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Critic target, actor distillation loss, OOD action 제약과 online data 혼합비.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 abstract는 OGBench와 D4RL의 state/pixel offline 및 offline-to-online task 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v267/park25f.html) · [저자 project/code](https://seohong.me/projects/fql/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
