# Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers

- Year/Venue: 2024 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_Triplane-Meets-Gaussian-Splatting-Fast-and-Generalizable-S/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, the inherent ambiguity and lack of information in single images pose a substantial challenge in accurately recovering the complete, ∗ Intern at VAST high-quality shape and texture ...
- This design choice addresses the challenges associated with directly regressing explicit 3D Gaussian attributes characterized by their non-structural nature.
- Introduction Digitizing 3D objects from single 2D images represents a crucial and longstanding challenge in both computer vision and graphics, with wide applications in augmented reality (AR) and ...

## Core Idea
- Our method utilizes two transformerbased networks, namely a point decoder and a triplane decoder, to reconstruct 3D objects using a hybrid TriplaneGaussian intermediate representation.
- In this paper, we introduce a novel approach for single-view reconstruction that efficiently generates a 3D model from a single image via feedforward inference.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The evaluations conducted on both synthetic datasets and real-world images demonstrate that our method not only achieves higher quality but also ensures a faster runtime in comparison to ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our method utilizes two transformerbased networks, namely a point decoder and a triplane decoder, to reconstruct 3D objects using a hybrid TriplaneGaussian intermediate representation.
- The evaluations conducted on both synthetic datasets and real-world images demonstrate that our method not only achieves higher quality but also ensures a faster runtime in comparison to ...
- Both decoders are built upon a scalable, transformer-based architecture and have been efficiently trained on large-scale 3D datasets.

## Abstract Cue
- Recent advancements in 3D reconstruction from single images have been driven by the evolution of generative models.
