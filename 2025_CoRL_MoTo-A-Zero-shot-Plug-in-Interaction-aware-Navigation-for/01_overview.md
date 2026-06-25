# MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation

- Year/Venue: 2025 / CoRL
- Category: Navigation and Embodied AI
- Tags: Navigation, mobile manipulation, VLM
- Authors: not extracted
- Paper: https://proceedings.mlr.press/v305/wu25c.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
실내/실외 이동 에이전트는 언어 목표와 3D 공간 구조를 연결해야 하며, partial observation과 탐색-활용 균형 때문에 단순 2D 인식만으로는 안정적이지 않다.

## Core Idea
핵심은 metric/semantic map, 3D scene graph, neural field, 또는 VLM reasoning을 이용해 언어 목표를 이동 가능한 공간 의사결정으로 바꾸는 것이다.

## Paper-Specific Cues
- Topic cue: Mobile manipulation is the fundamental challenge for robotics in assisting humans with diverse tasks and environments in everyday life.
- Method cue: Specifically, we propose an interaction-aware navigation policy to generate agent docking points for generalized mobile manipulation.
- Result cue: However, recent advances in manipulation foundation models demonstrate impressive generalization capability on a wide range of fixed-base manipulation tasks, which are still limited to ...

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `embodied navigation and spatial planning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- embodied navigation and spatial planning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Navigation, mobile manipulation, VLM.
- 초록에서 확인되는 주요 cue: Mobile, Conventional, However, Therefore, MoTo, Specifically, VLM, Extensive.
