# MuJoCo: A Physics Engine for Model-Based Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2012 / IROS
- Category: Benchmarks and Datasets
- Tags: Robotics, simulation, Physics Engine, Control
- Official paper: https://doi.org/10.1109/IROS.2012.6386109
- Code/Project: https://mujoco.org/
- Source audit: publisher metadata, official project page, and abstract checked; solver details remain UNVERIFIED.

## Why This Paper Is Here

continuous contact dynamics와 efficient simulation을 제공해 modern robot RL/control benchmark의 공통 인프라가 된 foundation system이다.

## Problem

model-based control과 optimization에 필요한 빠르고 정확한 articulated rigid-body/contact simulation을 제공한다.

## Core Idea

generalized-coordinate dynamics와 contact/constraint 처리를 결합한 physics engine을 설계한다.

## Interface

robot model과 control input을 simulated state transition, contact와 sensor output으로 변환한다.

## Evaluation Scope

simulation speed·accuracy와 control application이 중심이며 최신 GPU simulator와의 비교는 후속 연구에서 확인한다.
