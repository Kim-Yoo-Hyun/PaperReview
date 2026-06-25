# ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation

- Year/Venue: 2026 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, active perception, 3D manipulation
- Authors: Zhenyang Liu, Yongchong Gu, Yikai Wang, Xiangyang Xue, Yanwei Fu ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2026, pp. 8141-8151
- Paper: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다.

## Core Idea
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Paper-Specific Cues
- Topic cue: Recent advances in robot manipulation have leveraged pre-trained vision-language models (VLMs) and explored integrating 3D spatial signals into these models for effective action prediction, ...
- Method cue: To address these limitations, we propose ActiveVLA, a novel vision-language-action framework that empowers robots with active perception capabilities for high-precision, fine-grained manipulation.
- Result cue: Additionally, ActiveVLA applies a 3D zoom-in to improve resolution in key areas.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `robot manipulation and vision-language-action control`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- robot manipulation and vision-language-action control 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: VLA, active perception, 3D manipulation.
- 초록에서 확인되는 주요 cue: Recent, VLMs, VLA, However, ActiveVLA, Critical, Active, Drawing.
