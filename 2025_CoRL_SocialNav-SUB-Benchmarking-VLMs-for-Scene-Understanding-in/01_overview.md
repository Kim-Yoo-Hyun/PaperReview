# SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation

- Year/Venue: 2025 / CoRL
- Category: Navigation and Embodied AI
- Tags: VLM, Navigation, Benchmark
- Authors: not extracted
- Paper: https://proceedings.mlr.press/v305/munje25a.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
실내/실외 이동 에이전트는 언어 목표와 3D 공간 구조를 연결해야 하며, partial observation과 탐색-활용 균형 때문에 단순 2D 인식만으로는 안정적이지 않다.

## Core Idea
핵심은 metric/semantic map, 3D scene graph, neural field, 또는 VLM reasoning을 이용해 언어 목표를 이동 가능한 공간 의사결정으로 바꾸는 것이다.

## Paper-Specific Cues
- Topic cue: Robot navigation in dynamic, human-centered environments requires socially-compliant decisions grounded in robust scene understanding, including spatiotemporal awareness and the ability to interpret human intentions.
- Method cue: In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SocialNav-SUB), a Visual Question Answering (VQA) dataset and benchmark designed to evaluate VLMs ...
- Result cue: Recent Vision-Language Models (VLMs) show exhibit promising capabilities such as object recognition, common-sense reasoning, and contextual understanding—that align with the nuanced requirements of social ...

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `embodied navigation and spatial planning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- embodied navigation and spatial planning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: VLM, Navigation, Benchmark.
- 초록에서 확인되는 주요 cue: Robot, Recent, Vision-Language, Models, VLMs, However, Social, Navigation.
