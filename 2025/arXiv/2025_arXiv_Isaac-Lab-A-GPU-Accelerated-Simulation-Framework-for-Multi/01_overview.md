# Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2025 / arXiv
- Category: Benchmarks and Datasets
- Tags: Robotics, simulation, GPU, Robot Learning, NVIDIA
- Official paper: https://research.nvidia.com/labs/prl/publication/isaaclab2025/
- Code/Project: https://isaac-sim.github.io/IsaacLab/
- Source audit: official NVIDIA research and documentation pages checked; performance details remain UNVERIFIED.

## Why This Paper Is Here

Orbit을 계승해 RL, imitation, motion generation과 다양한 sensor modality를 통합한 NVIDIA의 현재 robot-learning simulation foundation이다.

## Problem

다양한 robot morphology, sensor와 learning paradigm을 하나의 scalable simulation workflow로 구성한다.

## Core Idea

Isaac Sim 기반 vectorized environments, modular managers/configuration과 multi-modal sensors를 통합한다.

## Interface

simulated scene/sensor data와 batched robot actions를 RL/IL training APIs로 연결한다.

## Evaluation Scope

다양한 locomotion/manipulation examples와 GPU scaling이 보고되며 version-specific results는 정독 후 기록한다.
