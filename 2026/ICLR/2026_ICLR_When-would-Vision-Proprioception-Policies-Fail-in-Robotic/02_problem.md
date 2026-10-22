# When would Vision-Proprioception Policies Fail in Robotic Manipulation?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Vision–proprioception 정책의 일반화 실패가 발생하는 시점을 분석한다.

## Bottleneck and Changed Formulation

Motion-transition phase에 따라 proprioception gradient를 조정하는 GAP을 제안한다.

## System and Robotics Loop

영상·proprioception → manipulation action; 학습 중 phase-guided gradient 조정.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

phase 추정 신호, task split, native Octo 코드·checkpoint.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation·실제 single/dual-arm 및 Octo 적용을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2b3bb2c95195130977a51b3bb251c40a-Abstract-Conference.html) · [저자 project/code](https://gewu-lab.github.io/GAP/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
