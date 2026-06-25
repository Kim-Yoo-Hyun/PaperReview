# SUGAR: Pre-training 3D Visual Representations for Robotics

- Year/Venue: 2024 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: 3D representation, Robotics, pretraining
- Authors: Shizhe Chen, Ricardo Garcia, Ivan Laptev, Cordelia Schmid ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024, pp. 18049-18060
- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Chen_SUGAR_Pre-training_3D_Visual_Representations_for_Robotics_CVPR_2024_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다.

## Core Idea
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Paper-Specific Cues
- Topic cue: Learning generalizable visual representations from Internet data has yielded promising results for robotics.
- Method cue: To address these limitations we introduce a novel 3D pre-training framework for robotics named SUGAR that captures semantic geometric and affordance properties of objects ...
- Result cue: Experimental results show that SUGAR's 3D representation outperforms state-of-the-art 2D and 3D representations.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `robot manipulation and vision-language-action control`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다.

## Contribution
- robot manipulation and vision-language-action control 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D representation, Robotics, pretraining.
- 초록에서 확인되는 주요 cue: Learning, Internet, Yet, Meanwhile, SUGAR, Experimental.
