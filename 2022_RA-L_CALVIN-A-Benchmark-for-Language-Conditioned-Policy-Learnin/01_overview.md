# CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks

- Year/Venue: 2022 / RA-L
- Category: Benchmarks and Datasets
- Tags: Vision-Language Action, Benchmark, Robotics
- Authors: Oier Mees, Lukas Hermann, Erick Rosete-Beas, Wolfram Burgard
- Paper: https://arxiv.org/abs/2112.03227
- PDF status: downloaded
- GitHub/Project: https://calvin.cs.uni-freiburg.de/

## Problem
로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다.

## Core Idea
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Paper-Specific Cues
- Topic cue: General-purpose robots coexisting with humans in their environment must learn to relate human language to their perceptions and actions to be useful in a ...
- Method cue: In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn long-horizon language-conditioned tasks.
- Result cue: We show that a baseline model based on multi-context imitation learning performs poorly on CALVIN, suggesting that there is significant room for developing innovative ...

## Input / Output
Input: benchmark-specific observations/instructions. Output: standardized labels, tasks, or evaluation scores for comparing models.

## Main Claims
- 논문은 `robot manipulation and vision-language-action control`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- robot manipulation and vision-language-action control 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Vision-Language Action, Benchmark, Robotics.
- 초록에서 확인되는 주요 cue: General-purpose, Moreover, CALVIN, Composing, Actions, Language, Vision, Our.
