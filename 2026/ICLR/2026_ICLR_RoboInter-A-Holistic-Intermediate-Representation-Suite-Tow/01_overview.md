# RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation

- Year/Venue: 2026 / ICLR Poster
- Category: Benchmarks and Datasets
- Tags: Vision-Language Model, Robotics, Benchmark
- Authors: Hao Li, Ziqin Wang, Zi-han Ding, Shuai Yang, Yilun Chen, Yang Tian, Xiaolin Hu, Tai Wang
- Paper: https://openreview.net/forum?id=PGUC3mmMoi
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다.

## Core Idea
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Paper-Specific Cues
- Topic cue: Advances in large vision-language models (VLMs) have stimulated growing interest in vision-language-action (VLA) systems for robot manipulation.
- Method cue: To bridge this gap, we introduce the RoboInter Manipulation Suite, a unified resource including data, benchmarks, and models of intermediate representations for manipulation.
- Result cue: 초록에서 result claim 문장을 자동 추출하지 못함.

## Input / Output
Input: benchmark-specific observations/instructions. Output: standardized labels, tasks, or evaluation scores for comparing models.

## Main Claims
- 논문은 `robot manipulation and vision-language-action control`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- robot manipulation and vision-language-action control 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Vision-Language Model, Robotics, Benchmark.
- 초록에서 확인되는 주요 cue: Advances, VLMs, VLA, However, Recent, RoboInter, Manipulation, Suite.
