# Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

깊이 센서와 기존 재구성의 scale/정밀도 오차가 로봇 물리 상호작용을 방해한다.

## Bottleneck and Changed Formulation

RGB와 robot state에서 local geometry·camera pose를 추정하고 robot frame의 metric geometry로 정렬한다.

## System and Robotics Loop

RGB/로봇 상태 → point map·camera pose·robot-frame scene geometry; 별도 downstream policy에 전달한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Robot state privilege·similarity transform·훈련 물체 중복·latency.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Robo3R-4M 합성 데이터로 학습하고 imitation·sim-to-real·grasp synthesis·collision-free planning의 downstream 효과를 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p056.html) · [저자 project/code](https://yangsizhe.github.io/robo3r/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
