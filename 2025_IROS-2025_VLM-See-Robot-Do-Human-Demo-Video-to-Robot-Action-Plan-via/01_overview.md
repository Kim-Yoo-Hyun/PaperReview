# VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model

- Year/Venue: 2025 / IROS 2025
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics
- Authors: Beichen Wang, Juexiao Zhang, Shuwen Dong, Irving Fang, Chen Feng
- Paper: https://arxiv.org/abs/2410.08792
- PDF status: downloaded
- GitHub/Project: https://ai4ce.github.io/SeeDo/

## Problem
로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다.

## Core Idea
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Paper-Specific Cues
- Topic cue: Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability.
- Method cue: Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline.
- Result cue: To validate our approach, we collected a set of long-horizon human videos demonstrating pick-and-place tasks in three diverse categories and designed a set of ...

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `robot manipulation and vision-language-action control`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- robot manipulation and vision-language-action control 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Vision-Language Model, Robotics.
- 초록에서 확인되는 주요 cue: Vision, Language, Models, VLMs, Existing, VLM, Our, SeeDo.
