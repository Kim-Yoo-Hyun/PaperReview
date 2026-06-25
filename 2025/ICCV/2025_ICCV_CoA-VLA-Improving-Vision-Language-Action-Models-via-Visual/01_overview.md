# CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Authors: Jinming Li, Yichen Zhu, Zhibin Tang, Junjie Wen, Minjie Zhu, Xiaoyu Liu, Chengmeng Li, Ran Cheng, Yaxin Peng, Yan Peng, Feifei Feng ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 9759-9769
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다.

## Core Idea
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Paper-Specific Cues
- Topic cue: Robot foundation models, particularly Vision-Language-Action (VLA) models, have garnered significant attention for their ability to enhance robot policy learning, greatly improving robot's generalization and ...
- Method cue: This prompts an important question: can robot models achieve better performance in multi-task, complex environments by reviewing prior observations and then providing task-specific reasoning ...
- Result cue: OpenAI's recent model, O1, showcased impressive capabilities in solving complex problems by utilizing extensive reasoning chains.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `robot manipulation and vision-language-action control`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- robot manipulation and vision-language-action control 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: VLA, Vision-Language Model.
- 초록에서 확인되는 주요 cue: Robot, Vision-Language-Action, VLA, OpenAI, This, Chain-of-Affordance, CoA-VLA, Specifically.
