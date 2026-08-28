# Hybrid Position/Force Control of Manipulators

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1981 / Journal of Dynamic Systems, Measurement, and Control
- Category: Robotics Foundations: Contact and Whole-Body Control
- Tags: Robotics, force control, contact, manipulation
- Official paper: https://doi.org/10.1115/1.3139652
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; controller derivation details remain UNVERIFIED.

## Why This Paper Is Here

접촉 작업에서 position과 force를 서로 다른 task direction에 배분하는 고전적 제어 관점을 제공한다.

## Problem

환경 constraint가 있는 manipulation에서 모든 방향을 position control하는 방식의 한계를 해결한다.

## Core Idea

task space를 position-controlled subspace와 force-controlled subspace로 분해해 hybrid feedback law를 구성한다.

## Interface

end-effector pose/velocity와 contact force를 받아 joint actuation 명령으로 연결한다.

## Evaluation Scope

개념적·제어 이론적 검증이 중심이며 최신 학습 기반 비교는 없다.
