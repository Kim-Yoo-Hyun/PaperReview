# RoboNet: Large-Scale Multi-Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2019 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Dataset, multi-robot, manipulation
- Official paper: https://proceedings.mlr.press/v100/dasari20a.html
- Code/Project: https://www.robonet.wiki/
- Source audit: official proceedings abstract and project page checked; dataset statistics and experiment details remain UNVERIFIED.

## Why This Paper Is Here

여러 기관·로봇의 조작 데이터를 결합해 cross-robot generalization을 연구한 대규모 robot-data lineage의 초기 대표작이다.

## Problem

한 로봇/환경에서 수집한 data가 다른 embodiment와 viewpoint로 잘 transfer되지 않는 문제를 다룬다.

## Core Idea

heterogeneous multi-robot interaction dataset과 conditioned video prediction/control 모델을 구축한다.

## Interface

camera observations, robot actions와 embodiment context를 future prediction 및 planning-based control로 연결한다.

## Evaluation Scope

여러 robot platform 사이의 transfer와 visual foresight control을 평가한다.
