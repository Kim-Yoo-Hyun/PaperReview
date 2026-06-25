# ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation

- Year/Venue: 2026 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, consistency, 4D reasoning
- Authors: Wei Li, Jizhihui Liu, Li Yixing, Junwen Tong, Rui Shao, Liqiang Nie ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2026, pp. 6706-6717
- Paper: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다.

## Core Idea
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Paper-Specific Cues
- Topic cue: Current Vision-Language-Action (VLA) models primarily focus on mapping 2D observations to actions but exhibit notable limitations in spatiotemporal perception and reasoning: 1) spatial representations ...
- Method cue: To address these challenges, we propose **ConsisVLA-4D**, a unified and efficient framework that enhances spatiotemporal consistency in 3D-Perception and 4D-Reasoning.
- Result cue: Building upon these, we introduce **3) CS-Thinker** to achieve **C**ross-**S**cene spatiotemporal consistency as actions unfold.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `robot manipulation and vision-language-action control`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- robot manipulation and vision-language-action control 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: VLA, consistency, 4D reasoning.
- 초록에서 확인되는 주요 cue: Current, Vision-Language-Action, VLA, ConsisVLA-4D, Perception, Reasoning, Specifically, CV-Aligner.
