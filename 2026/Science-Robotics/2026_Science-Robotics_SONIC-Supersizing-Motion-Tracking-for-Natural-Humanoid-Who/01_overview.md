# SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2026 / Science Robotics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, Motion Tracking, NVIDIA
- Official paper: https://research.nvidia.com/labs/dair/publication/sonic2026/
- Code/Project: https://research.nvidia.com/labs/dair/publication/sonic2026/
- Source audit: official NVIDIA publication page and journal status checked; full training/evaluation details remain UNVERIFIED.

## Why This Paper Is Here

motion tracking의 data·model·training scale을 확장해 자연스러운 real-humanoid whole-body control을 목표로 한 2026 frontier다.

## Problem

대규모 diverse motion을 실제 humanoid가 robust하고 자연스럽게 추종하는 데 필요한 controller scaling을 다룬다.

## Core Idea

large motion corpus와 scalable physics learning을 이용해 general motion-tracking whole-body policy를 학습한다.

## Interface

reference human motion과 humanoid proprioception을 real-time joint actions로 매핑한다.

## Evaluation Scope

physical humanoid의 diverse whole-body motion tracking과 robustness가 보고되며 exact hardware/trial protocol은 정독이 필요하다.
