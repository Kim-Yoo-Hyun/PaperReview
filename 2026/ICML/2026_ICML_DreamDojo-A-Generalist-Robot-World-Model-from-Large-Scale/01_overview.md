# DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2026 / ICML Spotlight
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, human video, generalist policy, NVIDIA
- Official paper: https://arxiv.org/abs/2602.06949
- Code/Project: https://research.nvidia.com/labs/gear/
- Source audit: arXiv abstract and official NVIDIA GEAR publication listing checked; full method/results remain UNVERIFIED.

## Why This Paper Is Here

large-scale human video를 generalist robot world model로 전환하는 2026 NVIDIA frontier로, world-model pretraining과 robot action grounding의 최신 연결을 제공한다.

## Problem

robot interaction data 부족을 human video의 broad physical experience로 보완하면서 robot-controllable dynamics를 학습한다.

## Core Idea

large-scale human video pretraining과 robot data adaptation/conditioning을 결합한 generative robot world model을 제시한다.

## Interface

visual context와 action/task conditioning을 future robot-centric video/state prediction으로 연결한다.

## Evaluation Scope

다양한 robot tasks/embodiments의 prediction과 policy utility가 보고되며 exact protocols는 정독 후 확정한다.
