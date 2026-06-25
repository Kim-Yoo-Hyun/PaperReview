# Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes

- Year/Venue: 2026 / ICLR Poster
- Category: Benchmarks and Datasets
- Tags: Vision-Language Model, Robotics, 3D Vision, Benchmark
- Authors: ZhiYuan Feng, Zhaolu Kang, Qijie Wang, Zhiying Du, Jiongrui Yan, Shi Shubin, Chengbo Yuan, Huizhi Liang
- Paper: https://openreview.net/forum?id=jXDZJAfRZB
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다.

## Core Idea
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Paper-Specific Cues
- Topic cue: Vision-language models (VLMs) are essential to Embodied AI, enabling robots to perceive, reason, and act in complex environments.
- Method cue: To bridge this gap, we introduce \textbf{MV-RoboBench}, a benchmark specifically designed to evaluate the multi-view spatial reasoning capabilities of VLMs in robotic manipulation.
- Result cue: The results show that state-of-the-art models remain far below human performance, underscoring the substantial challenges VLMs face in multi-view robotic perception.

## Input / Output
Input: benchmark-specific observations/instructions. Output: standardized labels, tasks, or evaluation scores for comparing models.

## Main Claims
- 논문은 `robot manipulation and vision-language-action control`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- robot manipulation and vision-language-action control 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Vision-Language Model, Robotics, 3D Vision, Benchmark.
- 초록에서 확인되는 주요 cue: Vision-language, VLMs, Embodied, They, Vision-Language-Action, VLA, Yet, Whether.
