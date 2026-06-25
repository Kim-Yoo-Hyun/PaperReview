# Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation

- Year/Venue: 2026 / ICML
- Category: Navigation and Embodied AI
- Tags: Navigation, Reinforcement Learning
- Authors: Zhixuan Shen, Jiawei Du, Ziyu Guo, Han Luo, Lilan Peng, Joey Tianyi Zhou, Haonan Luo, Tianrui Li
- Paper: https://openreview.net/forum?id=W5e8c9nwNo
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
실내/실외 이동 에이전트는 언어 목표와 3D 공간 구조를 연결해야 하며, partial observation과 탐색-활용 균형 때문에 단순 2D 인식만으로는 안정적이지 않다.

## Core Idea
핵심은 metric/semantic map, 3D scene graph, neural field, 또는 VLM reasoning을 이용해 언어 목표를 이동 가능한 공간 의사결정으로 바꾸는 것이다.

## Paper-Specific Cues
- Topic cue: Vision-Language Models (VLMs) have demonstrated exceptional general reasoning capabilities.
- Method cue: To this end, we propose ***S**andbox-**A**bstracted **G**rounded **E**xperience* (***SAGE***), a framework that enables agents to learn within a physics-grounded semantic abstraction rather than a ...
- Result cue: Vision-Language Models (VLMs) have demonstrated exceptional general reasoning capabilities.

## Input / Output
Input: language/navigation goal plus egocentric observations or 3D maps. Output: waypoint, action, route, or grounded target decision.

## Main Claims
- 논문은 `embodied navigation and spatial planning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- embodied navigation and spatial planning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Navigation, Reinforcement Learning.
- 초록에서 확인되는 주요 cue: Vision-Language, Models, VLMs, However, Despite, SAGE, Genesis, Evolution.
