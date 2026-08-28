# RT-H: Action Hierarchies Using Language

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / Robotics: Science and Systems
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, Action Hierarchy, language, Google DeepMind
- Official paper: https://www.roboticsproceedings.org/rss20/p049.html
- Code/Project: not identified
- Source audit: official RSS proceedings abstract checked; full benchmark tables remain UNVERIFIED.

## Why This Paper Is Here

language motion concepts를 중간 action hierarchy로 사용해 VLA의 reasoning과 low-level control 사이를 연결한 Google 계보의 핵심 paper다.

## Problem

flat action prediction이 correction, compositional generalization과 human intervention에 불리한 문제를 다룬다.

## Core Idea

policy가 먼저 language motion command를 예측하고 이를 robot action으로 변환하는 hierarchical action representation을 학습한다.

## Interface

image/language instruction → language motion concept → low-level robot action의 계층을 갖는다.

## Evaluation Scope

real-robot manipulation에서 RT-style baselines, generalization 및 intervention을 비교한다.
