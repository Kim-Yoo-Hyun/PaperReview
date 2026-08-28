# Information Theoretic MPC for Model-Based Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2017 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, model predictive control, model-based RL, Planning
- Official paper: https://ieeexplore.ieee.org/document/7989202/
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; objective derivation and result magnitudes remain UNVERIFIED.

## Why This Paper Is Here

sampling-based MPC와 learned dynamics를 결합하는 MPPI 계열의 대표 foundation으로, online replanning과 recovery 연구의 기반이다.

## Problem

비선형·비convex control 문제에서 dynamics model을 이용해 실시간 action sequence를 최적화한다.

## Core Idea

path-integral/information-theoretic 관점의 sampled trajectory weighting으로 receding-horizon control sequence를 갱신한다.

## Interface

current state와 dynamics model을 짧은 horizon action sequence와 첫 control action으로 변환한다.

## Evaluation Scope

aggressive autonomous driving/control 사례가 보고되며 hardware와 sampling 설정은 원문에서 확인한다.
