# Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1992 / Machine Learning
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Policy Gradient, REINFORCE
- Official paper: https://doi.org/10.1007/BF00992696
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; estimator derivation remains UNVERIFIED.

## Why This Paper Is Here

REINFORCE likelihood-ratio gradient estimator의 고전으로 stochastic policy optimization의 출발점이다.

## Problem

differentiable environment model 없이 stochastic policy parameter를 expected reward 방향으로 갱신한다.

## Core Idea

sampled action의 log-probability gradient에 return/reinforcement signal을 곱한 unbiased estimator를 사용한다.

## Interface

trajectory reward를 stochastic policy parameter update로 변환한다.

## Evaluation Scope

connectionist learning examples와 estimator 분석이 중심이며 modern continuous-control benchmark는 없다.
