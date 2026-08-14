# Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

- Year/Venue: 2023 / RSS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, bimanual manipulation, Imitation Learning, action chunking
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://tonyzhaozh.github.io/aloha/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- To address these challenges, we develop a simple yet novel algorithm, Action Chunking with Transformers (ACT), which learns a generative model over action sequences.
- Imitation learning, however, presents its own challenges, particularly in highprecision domains: errors in the policy can compound over time, and human demonstrations can be non-stationary.
- Performing these tasks typically requires high-end robots, accurate sensors, or careful calibration, which can be expensive and difficult to set up.

## Core Idea
- We improve BC, for example by incorporating history with various architectures , using a different training objective overview each component in the following two paragraphs.
- To address these challenges, we develop a simple yet novel algorithm, Action Chunking with Transformers (ACT), which learns a generative model over action sequences.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We improve BC, for example by incorporating history with various architectures , using a different training objective overview each component in the following two paragraphs.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We improve BC, for example by incorporating history with various architectures , using a different training objective overview each component in the following two paragraphs.
- To address these challenges, we develop a simple yet novel algorithm, Action Chunking with Transformers (ACT), which learns a generative model over action sequences.
- We present a low-cost system that performs end-to-end imitation learning directly from real demonstrations, collected with a custom teleoperation interface.

## Abstract Cue
- —Fine manipulation tasks, such as threading cable ties or slotting a battery, are notoriously difficult for robots because they require precision, careful coordination of contact forces, and closed-loop visual feedback.
