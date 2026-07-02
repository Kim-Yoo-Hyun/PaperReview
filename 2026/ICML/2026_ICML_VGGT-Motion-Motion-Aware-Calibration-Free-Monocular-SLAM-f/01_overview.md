# VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency

- Year/Venue: 2026 / ICML spotlight
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, depth, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_VGGT-Motion-Motion-Aware-Calibration-Free-Monocular-SLAM-f/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Motion-agnostic partitioning breaks contextual coherence and causes zero-motion drift, while conventional geometric alignment is computationally expensive.
- By exploiting context-balanced anchors, it achieves search-free, pixel-wise dense alignment and efficient loop closure without costly feature matching.

## Core Idea
- To address these issues, we propose VGGT-Motion, a calibration-free SLAM system for efficient and robust global consistency over kilometer-scale trajectories.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments show that VGGT-Motion markedly improves trajectory accuracy and efficiency, achieving state-of-the-art performance in zero-shot, long-range calibrationfree monocular SLAM.
- By exploiting context-balanced anchors, it achieves search-free, pixel-wise dense alignment and efficient loop closure without costly feature matching.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments show that VGGT-Motion markedly improves trajectory accuracy and efficiency, achieving state-of-the-art performance in zero-shot, long-range calibrationfree monocular SLAM.
- To address these issues, we propose VGGT-Motion, a calibration-free SLAM system for efficient and robust global consistency over kilometer-scale trajectories.
- By exploiting context-balanced anchors, it achieves search-free, pixel-wise dense alignment and efficient loop closure without costly feature matching.

## Abstract Cue
- Despite recent progress in calibration-free monocular SLAM via 3D vision foundation models, scale drift remains severe on long sequences.
