# TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

BC prior의 좁은 행동 범위가 후속 RL 탐색을 제한한다.

## Bottleneck and Changed Formulation

입력에 diffusion noise를 넣어 사전학습하고 RL이 조건화 noise 수준을 선택한다.

## System and Robotics Loop

관측·noise 수준 → 사전학습 정책의 행동; RL이 timestep을 조절.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

pretraining 추가 비용, high-level action 주기, baseline 탐색 분산, 로봇별 학습 시간.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

항법·조작 평가를 보고하며 project는 실제 VLA 후학습도 설명한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p208.html) · [저자 project/code](https://weirdlabuw.github.io/tmrl/) · [공식 code](https://github.com/matthewh6/tmrl). Exact objective, constraints, success definition은 본문 수동 확인 필요.
