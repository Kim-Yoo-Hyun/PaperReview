# Uni3R: Unified 3D Reconstruction and Semantic Understanding via Generalizable Gaussian Splatting from Unposed Multi-View Images

- Year/Venue: 2026 / CVPR
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, 3D reconstruction, geometry, semantic, alignment, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_Uni3R-Unified-3D-Reconstruction-and-Semantic-Understanding/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Reconstructing and semantically interpreting 3D scenes from sparse 2D views remains a fundamental challenge in computer vision.
- Conventional methods often decouple semantic understanding from reconstruction or necessitate costly per-scene optimization, thereby restricting their scalability and generalizability.
- Introduction The ability to perceive and interpret the 3D world from sparse images is a cornerstone of computer vision, holding profound implications for robotics, autonomous driving, and augmented ...

## Core Idea
- Our approach leverages a Cross-View Transformer to robustly integrate information across arbitrary multi-view inputs, which then regresses a set of 3D Gaussian primitives endowed with semantic feature fields.
- Implementation Details We use DINOv2 as the image encoder, with a patch size of 16, and set the CrossView Transformer layers as L = 24.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that Uni3R sets a new state of the art across multiple benchmarks, including indomain datasets such as RE10K and ScanNet, as well as the out-of-domain ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our approach leverages a Cross-View Transformer to robustly integrate information across arbitrary multi-view inputs, which then regresses a set of 3D Gaussian primitives endowed with semantic feature fields.
- Extensive experiments demonstrate that Uni3R sets a new state of the art across multiple benchmarks, including indomain datasets such as RE10K and ScanNet, as well as the out-of-domain ...
- In this paper, we introduce Uni3R, a novel feed-forward framework that jointly reconstructs a unified 3D scene representation enriched with open-vocabulary semantics, directly from unposed multiview images.

## Abstract Cue
- Reconstructing and semantically interpreting 3D scenes from sparse 2D views remains a fundamental challenge in computer vision.
