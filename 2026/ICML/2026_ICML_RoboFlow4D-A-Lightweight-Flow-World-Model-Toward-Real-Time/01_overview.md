# RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, Reinforcement Learning
- Authors: Sixu Lin, Junliang Chen, Huaiyuan Xu, Zhuohao Li, Guangming Wang, Yixiong Jing, Sheng Xu, Runyi Zhao
- Paper: https://openreview.net/forum?id=fh6XBnjFlv
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다.

## Core Idea
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Paper-Specific Cues
- Topic cue: Planning and acting in 3D environments is a fundamental capability for robotic manipulation in the real world.
- Method cue: To address these challenges, we introduce RoboFlow4D, a lightweight flow world model that unifies perception and planning by estimating temporal motion in physical 3D ...
- Result cue: Extensive experiments in both simulation and real-world settings demonstrate that RoboFlow4D consistently improves manipulation success rates and computational efficiency, advancing flow-guided planning for embodied ...

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `robot manipulation and vision-language-action control`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- robot manipulation and vision-language-action control 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: VLA, Vision-Language Model, Robotics, Reinforcement Learning.
- 초록에서 확인되는 주요 cue: Planning, Although, RoboFlow4D, This, Through, Extensive, Our.
