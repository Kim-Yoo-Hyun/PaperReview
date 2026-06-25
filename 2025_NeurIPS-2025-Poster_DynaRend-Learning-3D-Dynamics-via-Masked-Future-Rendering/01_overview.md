# DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation

- Year/Venue: 2025 / NeurIPS 2025 Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision
- Authors: Jingyi Tian, Le Wang, Sanping Zhou, Sen Wang, lijiayi, Gang Hua
- Paper: https://openreview.net/forum?id=r4dzaP61QH
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다.

## Core Idea
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Paper-Specific Cues
- Topic cue: Learning generalizable robotic manipulation policies remains a key challenge due to the scarcity of diverse real-world training data.
- Method cue: In this paper, we present DynaRend, a representation learning framework that learns 3D-aware and dynamics-informed triplane features via masked reconstruction and future prediction using ...
- Result cue: We evaluate DynaRend on two challenging benchmarks, RLBench and Colosseum, as well as in real-world robotic experiments, demonstrating substantial improvements in policy success rate, ...

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `robot manipulation and vision-language-action control`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- robot manipulation and vision-language-action control 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Robotics, 3D Vision.
- 초록에서 확인되는 주요 cue: Learning, While, DynaRend, RGB-D, The, RLBench, Colosseum.
