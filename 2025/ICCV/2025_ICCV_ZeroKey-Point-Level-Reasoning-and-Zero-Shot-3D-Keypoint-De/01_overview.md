# ZeroKey: Point-Level Reasoning and Zero-Shot 3D Keypoint Detection from Large Language Models

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_ZeroKey-Point-Level-Reasoning-and-Zero-Shot-3D-Keypoint-De/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Point-level reasoning on visual data is challenging as it requires precise localization capability, posing problems even for powerful models like DINO or CLIP.
- This work opens new avenues for cross-modal learning and underscores the effectiveness of MLLMs in contributing to 3D computer vision challenges.
- Unfortunately, despite this tremendous progress, existing MLLMs still struggle with tasks that require precise points or pixel-level reasoning, such as localization, counting, or salient keypoint detection .

## Core Idea
- We propose a novel zero-shot approach for keypoint detection on 3D shapes.
- We then select the area overlapped with the bounding box prediction as the detected points and lift these 2D points to 3D using our method.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental evaluations demonstrate that our approach achieves competitive performance on standard benchmarks compared to supervised methods, despite not requiring any 3D keypoint annotations during training.
- Our results highlight the potential of integrating language models for localized 3D shape understanding.
- Specifically, we demonstrate, for the first time, that pixel-level annotations used to train recent MLLMs can be exploited for both extracting and naming salient keypoints on 3D models ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experimental evaluations demonstrate that our approach achieves competitive performance on standard benchmarks compared to supervised methods, despite not requiring any 3D keypoint annotations during training.
- We propose a novel zero-shot approach for keypoint detection on 3D shapes.
- In contrast, our method utilizes the rich knowledge embedded within Multi-Modal Large Language Models (MLLMs).

## Abstract Cue
- We propose a novel zero-shot approach for keypoint detection on 3D shapes.
