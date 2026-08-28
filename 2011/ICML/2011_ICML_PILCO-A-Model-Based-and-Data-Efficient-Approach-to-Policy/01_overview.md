# PILCO: A Model-Based and Data-Efficient Approach to Policy Search

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2011 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, model-based RL, Gaussian Process
- Official paper: https://www.deisenroth.cc/publication/deisenroth-2011-c/
- Code/Project: not identified
- Source audit: author publication page and abstract checked; derivations and result magnitudes remain UNVERIFIED.

## Why This Paper Is Here

robot data efficiency를 uncertainty-aware learned dynamics와 policy search로 해결한 대표 model-based RL foundation이다.

## Problem

실제 시스템에서 많은 interaction 없이 continuous-control policy를 학습한다.

## Core Idea

Gaussian-process dynamics의 predictive uncertainty를 장기 cost prediction에 전파하고 analytic policy gradient를 계산한다.

## Interface

state-action transition data를 learned dynamics와 continuous control policy로 연결한다.

## Evaluation Scope

저차원 control과 real-robot 사례가 보고되며 task·sample count는 원문 확인이 필요하다.
