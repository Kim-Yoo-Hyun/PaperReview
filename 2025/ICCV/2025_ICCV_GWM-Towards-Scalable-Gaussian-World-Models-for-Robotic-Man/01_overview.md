# GWM: Towards Scalable Gaussian World Models for Robotic Manipulation

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Gaussian Splatting, world model, Robotics
- Authors: Guanxing Lu, Baoxiong Jia, Puhao Li, Yixin Chen, Ziwei Wang, Yansong Tang, Siyuan Huang ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 9263-9274
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: Training robot policies within a learned world model is trending due to the inefficiency of real-world interactions.
- Method cue: To this end, we propose a novel branch of world model named Gaussian World Model (GWM) for robotic manipulation, which reconstructs the future state ...
- Result cue: The established image-based world models and policies have shown prior success, but lack robust geometric information that requires consistent spatial and physical understanding of ...

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Gaussian Splatting, world model, Robotics.
- 초록에서 확인되는 주요 cue: Training, The, Gaussian, World, Model, GWM, Diffusion, Transformer.
