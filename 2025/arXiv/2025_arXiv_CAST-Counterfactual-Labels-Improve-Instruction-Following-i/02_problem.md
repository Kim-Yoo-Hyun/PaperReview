# CAST: Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

비슷한 관측에서 행동과 지시가 다양하지 않으면 VLA가 언어를 무시하고 데이터 편향에 의존할 수 있다.

## Bottleneck and Changed Formulation

VLM 기반 counterfactual 라벨과 대응 행동 자료로 기존 robot dataset의 지시·행동 다양성을 늘려 언어 추종을 학습한다.

## System and Robotics Loop

기존 trajectory와 counterfactual instruction/action 자료 → VLA 학습 → navigation 또는 manipulation 행동. 실제 수행된 실패의 hindsight 라벨과 합성 counterfactual을 구분한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

합성 행동의 물리적 유효성, 원 데이터/평가 중복, language와 action 증강 기여 분리, 공개 모델/자료의 논문 version 대응.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

v2 abstract는 실내외 3개 navigation 환경과 distractor가 있는 manipulation의 instruction following을 평가한다고 보고한다. 정확한 trial·split·수치는 본문 확인 필요다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2508.13446) · [저자 project/code](https://cast-vla.github.io/) · [공식 code](https://github.com/catglossop/CAST). Exact objective, constraints, success definition은 본문 수동 확인 필요.
