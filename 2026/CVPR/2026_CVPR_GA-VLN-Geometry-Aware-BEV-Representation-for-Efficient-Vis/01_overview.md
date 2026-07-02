# GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation

- Year/Venue: 2026 / CVPR
- Category: Navigation and Embodied AI
- Tags: Vision-Language Navigation, geometry, BEV
- Paper link: ./2026/CVPR/2026_CVPR_GA-VLN-Geometry-Aware-BEV-Representation-for-Efficient-Vis/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Despite significant progress in Vision-Language Navigation (VLN), existing approaches still rely on dense RGB videos that produce excessive patch tokens and lack explicit spatial structure, resulting in substantial ...

## Core Idea
- To address these issues, we introduce the Geometry-Aware BEV (GABEV) – a compact, 3D-grounded feature representation that integrates both explicit and implicit geometric cues into multimodal large language ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments show that our method achieves state-of-the-art results using only navigation data, without DAgger augmentation or mixed VQA training, demonstrating the robustness and data efficiency of the proposed ...
- Together, these complementary cues – explicit depth-based projection and implicit learned priors – yield compact yet spatially expressive representations that substantially improve navigation efficiency and performance.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments show that our method achieves state-of-the-art results using only navigation data, without DAgger augmentation or mixed VQA training, demonstrating the robustness and data efficiency of the proposed ...
- To address these issues, we introduce the Geometry-Aware BEV (GABEV) – a compact, 3D-grounded feature representation that integrates both explicit and implicit geometric cues into multimodal large language ...
- Together, these complementary cues – explicit depth-based projection and implicit learned priors – yield compact yet spatially expressive representations that substantially improve navigation efficiency and performance.

## Abstract Cue
- Despite significant progress in Vision-Language Navigation (VLN), existing approaches still rely on dense RGB videos that produce excessive patch tokens and lack explicit spatial structure, resulting in substantial computational overhead and limited spatial reasoning.
