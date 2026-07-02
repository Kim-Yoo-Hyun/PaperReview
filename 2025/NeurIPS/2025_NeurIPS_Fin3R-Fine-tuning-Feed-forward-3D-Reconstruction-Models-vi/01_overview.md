# Fin3R: Fine-tuning Feed-forward 3D Reconstruction Models via Monocular Knowledge Distillation

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, depth, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Fin3R-Fine-tuning-Feed-forward-3D-Reconstruction-Models-vi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing non-synthetic depth labels are noisy and predominantly biased toward indoor environments. (2) Long-sequence pointmap degradation: Inherent ambiguities in multi-view pointmap regression impede the network’s ability to capture ...
- Fine structures are frequently over-smoothed, object boundaries become blurred, and transparent or glossy surfaces are reconstructed with significant inaccuracies, yielding point clouds that lack crisp geometry.

## Core Idea
- To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift.
- We present Fin3R, a simple, effective, and general fine-tuning method for feedforward 3D reconstruction models.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The table shows that our integrated models consistently achieve lower relative depth error and higher δ1 scores.
- The fine-tuned models consistently deliver sharper boundaries, recover complex structures, and achieve higher geometric accuracy in both single- and multi-view settings, while adding only the tiny LoRA weights, ...
- After fine-tuning, our method improves the model’s ability to capture fine details and complex surfaces such as transparent ones.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We freeze the decoder, which handles view matching, and fine-tune only the image encoder—the component dedicated to feature extraction.
- We present Fin3R, a simple, effective, and general fine-tuning method for feedforward 3D reconstruction models.
- We validate our method on a wide range of models, including DUSt3R, MASt3R, CUT3R, and VGGT.

## Abstract Cue
- We present Fin3R, a simple, effective, and general fine-tuning method for feedforward 3D reconstruction models.
