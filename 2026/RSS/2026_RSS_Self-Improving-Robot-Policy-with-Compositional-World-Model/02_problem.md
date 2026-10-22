# Self-Improving Robot Policy with Compositional World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Contact-rich/dynamic task에서 VLA의 작은 실행 오차가 누적되지만 실제 환경 on-policy RL은 reset·hardware 비용이 높다.

## Bottleneck and Changed Formulation

Multi-view controllable dynamics와 progress value model을 분리하여 imagined rollout에서 advantage를 만들고 policy를 개선한다.

## System and Robotics Loop

Observation/action → imagined multi-view future → progress value/advantage → policy update.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Progress label 생성, failure coverage, value calibration과 real rollout 예산.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RSS abstract는 dynamic brick sorting, backpack packing, box closing의 세 real-world task 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p012.html) · [저자 project/code](https://github.com/OpenDriveLab/RISE). Exact objective, constraints, success definition은 본문 수동 확인 필요.
