# SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA SFT에 필요한 robot trajectory 비용과 distribution shift에서의 낮은 task 성능을 줄인다.

## Bottleneck and Changed Formulation

Outcome reward 기반 VLA RL에 trajectory sampling, parallel rollout/rendering 및 loss 계산 최적화를 결합한다.

## System and Robotics Loop

OpenVLA-OFT의 observation/language → action rollout → outcome reward → policy update.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

실제 robot online training 범위, sparse reward 생성, data leakage 및 compute accounting.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

ICLR abstract는 LIBERO, RoboTwin 1.0/2.0 및 real-world task 결과를 보고한다. Real-world 평가와 실제 online training은 구분해야 한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html) · [저자 project/code](https://github.com/PRIME-RL/SimpleVLA-RL). Exact objective, constraints, success definition은 본문 수동 확인 필요.
