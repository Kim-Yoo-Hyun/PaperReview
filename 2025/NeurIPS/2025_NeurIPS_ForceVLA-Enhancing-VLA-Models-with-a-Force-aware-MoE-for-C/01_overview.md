# ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Robotics
- Authors: Jiawen Yu, Hairuo Liu, Qiaojun Yu, Jieji Ren, Ce Hao, Haitong Ding, Guangyu Huang, Guofan Huang
- Paper: https://openreview.net/forum?id=2845H8Ua5D
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다.

## Core Idea
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Paper-Specific Cues
- Topic cue: Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations.
- Method cue: To address these limitations, we propose \textbf{ForceVLA}, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems.
- Result cue: ForceVLA improves average task success by 23.2\% over strong $\pi_0$-based baselines, achieving up to 80\% success in tasks such as plug insertion.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `robot manipulation and vision-language-action control`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- robot manipulation and vision-language-action control 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: VLA, Robotics.
- 초록에서 확인되는 주요 cue: Vision-Language-Action, VLA, However, ForceVLA, FVLMoE, Mixture-of-Experts, This, ForceVLA-Data.
