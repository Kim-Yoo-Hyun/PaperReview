# ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, Gaussian Splatting
- Authors: Guanxing Lu, Shiyi Zhang, Ziwei Wang*, Changliu Liu, Jiwen Lu, Yansong Tang
- Paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5194_ECCV_2024_paper.php
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: "Performing language-conditioned robotic manipulation tasks in unstructured environments is highly demanded for general intelligent robots.
- Method cue: In this paper, we propose a dynamic Gaussian Splatting method named ManiGaussian for multi-task robotic manipulation, which mines scene dynamics via future scene reconstruction.
- Result cue: We evaluate our ManiGaussian on 10 RLBench tasks with 166 variations, and the results demonstrate our framework can outperform the state-of-the-art methods by 13.1% ...

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Robotics, Gaussian Splatting.
- 초록에서 확인되는 주요 cue: Performing, Conventional, Gaussian, Splatting, ManiGaussian, Specifically, Then, RLBench.
