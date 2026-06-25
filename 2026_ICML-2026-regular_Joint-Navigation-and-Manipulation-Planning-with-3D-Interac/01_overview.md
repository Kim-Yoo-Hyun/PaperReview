# Joint Navigation and Manipulation Planning with 3D Interaction Chains

- Year/Venue: 2026 / ICML 2026 regular
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Robotics, 3D Vision, Navigation
- Authors: Keming Zhang, Sixian Zhang, Xinhang Song, Hongyu Wang, Yiyao Wang, Yingjie Wang, Shuqiang Jiang
- Paper: https://openreview.net/forum?id=oVB2xYWvpv
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
실내/실외 이동 에이전트는 언어 목표와 3D 공간 구조를 연결해야 하며, partial observation과 탐색-활용 균형 때문에 단순 2D 인식만으로는 안정적이지 않다.

## Core Idea
핵심은 metric/semantic map, 3D scene graph, neural field, 또는 VLM reasoning을 이용해 언어 목표를 이동 가능한 공간 의사결정으로 바꾸는 것이다.

## Paper-Specific Cues
- Topic cue: Open-vocabulary mobile manipulation (OVMM) requires long-horizon navigation in unseen environments and object-centric manipulation.
- Method cue: 초록에서 명시적 propose/present 문장을 자동 추출하지 못함.
- Result cue: Experiments in simulation and on a real Stretch 3 robot demonstrate consistent gains in both task success and trajectory efficiency.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `embodied navigation and spatial planning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- embodied navigation and spatial planning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Vision-Language Model, Robotics, 3D Vision, Navigation.
- 초록에서 확인되는 주요 cue: Open-vocabulary, OVMM, Most, Interaction, Chains, VLM, The, Experiments.
