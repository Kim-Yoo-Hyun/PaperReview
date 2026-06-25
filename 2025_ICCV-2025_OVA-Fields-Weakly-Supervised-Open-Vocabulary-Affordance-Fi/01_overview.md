# OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection

- Year/Venue: 2025 / ICCV 2025
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, semantic
- Authors: Heng Su, Mengying Xie, Nieqing Cao, Yan Ding, Beichen Shao, Xianlei Long, Fuqiang Gu, Chao Chen ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 6385-6395
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Su_OVA-Fields_Weakly_Supervised_Open-Vocabulary_Affordance_Fields_for_Robot_Operational_Part_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다.

## Core Idea
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Paper-Specific Cues
- Topic cue: In recent years, affordance detection has become essential for robotic manipulation in real-world scenes, where robots must autonomously interpret commands and perform actions.
- Method cue: To address this, we introduce OVA-Fields, a framework for affordance detection in 3D scenes with complex semantics.
- Result cue: Experimental results demonstrate that OVA-Fields achieves 52.4% mIoU on complex semantic real-world scenes and 90% success rate in real-world robot manipulation tasks (e.g., "take ...

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `robot manipulation and vision-language-action control`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- robot manipulation and vision-language-action control 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Robotics, semantic.
- 초록에서 확인되는 주요 cue: Current, OVA-Fields, Experimental, RGB-D, Our.
