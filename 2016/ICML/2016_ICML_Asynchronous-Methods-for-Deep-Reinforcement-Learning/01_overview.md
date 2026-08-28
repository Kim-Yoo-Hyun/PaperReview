# Asynchronous Methods for Deep Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2016 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, actor-critic, A3C
- Official paper: https://proceedings.mlr.press/v48/mniha16.html
- Code/Project: not identified
- Source audit: official proceedings abstract checked; implementation and result magnitudes remain UNVERIFIED.

## Why This Paper Is Here

DeepMind의 A3C로 actor-critic을 병렬 환경에 확장한 대표 deep RL foundation이다.

## Problem

deep RL의 correlated data와 느린 training을 replay buffer 없이 완화한다.

## Core Idea

여러 asynchronous actor-learners가 shared parameters에 policy/value gradients를 적용한다.

## Interface

parallel environment trajectories를 shared actor-critic policy update로 변환한다.

## Evaluation Scope

Atari, continuous control 및 3D navigation tasks가 보고되며 robotics hardware는 직접 평가하지 않는다.
