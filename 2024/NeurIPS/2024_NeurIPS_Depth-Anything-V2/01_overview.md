# Depth Anything V2

- Year/Venue: 2024 / NeurIPS
- Category: Foundations: Monocular Geometry
- Tags: depth, 3D Vision
- Paper link: ./2024/NeurIPS/2024_NeurIPS_Depth-Anything-V2/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Monocular depth estimation (MDE) is gaining increasing attention, due to its fundamental role in widespread downstream tasks.
- Precise depth information is not only favorable in classical applications, such as 3D reconstruction , navigation , and autonomous driving , but is also preferable in modern scenarios, ...
- Therefore, there have been numerous MDE models emerging recently, which are all capable of addressing open-world images.

## Core Idea
- Compared with the latest models built on Stable Diffusion, our models are significantly more efficient (more than 10× faster) and more accurate.
- KITTI Encoder NYU-D Sintel ETH3D DIODE AbsRel δ1 AbsRel δ1 AbsRel δ1 AbsRel δ1 AbsRel δ1 MiDaS V3.1 ViT-L 0.127 0.850 0.048 0.980 0.587 0.699 0.139 0.867 0.075 ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- As shown in Table 2, our results are superior to MiDaS and comparable to V1 .
- Improvement in these dimensions cannot be correctly reflected in current benchmarks.
- As shown in Table 3, on our proposed benchmark with diverse scenes, even our smallest model is significantly better than other heavy SD-based

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Compared with the latest models built on Stable Diffusion, our models are significantly more efficient (more than 10× faster) and more accurate.
- In addition to our models, considering the limited diversity and frequent noise in current test sets, we construct a versatile evaluation benchmark with precise annotations and diverse scenes ...

## Abstract Cue
- This work presents Depth Anything V2.
