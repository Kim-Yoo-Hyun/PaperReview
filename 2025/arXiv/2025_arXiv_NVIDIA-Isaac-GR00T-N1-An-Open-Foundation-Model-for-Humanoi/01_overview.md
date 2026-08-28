# NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2025 / arXiv
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, humanoid, Foundation Models, NVIDIA
- Official paper: https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots
- Code/Project: https://developer.nvidia.com/isaac/gr00t
- Source audit: official NVIDIA publication and project pages checked; full data/model details remain UNVERIFIED.

## Why This Paper Is Here

humanoid를 대상으로 vision-language instruction과 action generation을 결합하고 공개 model/data ecosystem을 제시한 NVIDIA foundation-policy 계보의 핵심이다.

## Problem

다양한 humanoid manipulation tasks와 embodiments에 adaptation 가능한 generalist robot foundation model을 구축한다.

## Core Idea

VLM backbone과 diffusion/action model을 결합한 dual-system architecture 및 heterogeneous robot data training을 제시한다.

## Interface

multimodal observations와 language instruction을 humanoid manipulation action chunks로 매핑한다.

## Evaluation Scope

여러 humanoid embodiments와 manipulation tasks의 adaptation/generalization이 보고되며 exact splits와 baselines는 정독이 필요하다.
