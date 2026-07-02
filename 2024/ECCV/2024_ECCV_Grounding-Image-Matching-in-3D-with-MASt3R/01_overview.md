# Grounding Image Matching in 3D with MASt3R

- Year/Venue: 2024 / ECCV
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D geometry, matching, calibration
- Paper link: ./2024/ECCV/2024_ECCV_Grounding-Image-Matching-in-3D-with-MASt3R/paper.pdf
- Code/Project: https://github.com/naver/mast3r
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Yet despite matching being fundamentally a 3D problem, intrinsically linked to camera pose and scene geometry, it is typically treated as a 2D problem.

## Core Idea
- We introduced a fast reciprocal matcher and a coarse to fine approach for efficient processing, allowing users to balance between accuracy and speed.
- We introduce a fast reciprocal matching scheme that not only accelerates matching by orders of magnitude, but also comes with theoretical guarantees and, lastly, yields improved results.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments show that our approach, coined MASt3R, significantly outperforms the state of the art on multiple matching tasks.
- We introduce a fast reciprocal matching scheme that not only accelerates matching by orders of magnitude, but also comes with theoretical guarantees and, lastly, yields improved results.
- We aim here to improve the matching capabilities of such an approach while preserving its robustness.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments show that our approach, coined MASt3R, significantly outperforms the state of the art on multiple matching tasks.
- We introduce a fast reciprocal matching scheme that not only accelerates matching by orders of magnitude, but also comes with theoretical guarantees and, lastly, yields improved results.
- In this work, we take a different stance and propose to cast matching as a 3D task with DUSt3R, a recent and powerful 3D reconstruction framework based on ...

## Abstract Cue
- Image Matching is a core component of all best-performing algorithms and pipelines in 3D vision.
