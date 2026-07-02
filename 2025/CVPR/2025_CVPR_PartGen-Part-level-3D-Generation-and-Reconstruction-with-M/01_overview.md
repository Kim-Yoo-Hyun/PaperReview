# PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models

- Year/Venue: 2025 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_PartGen-Part-level-3D-Generation-and-Reconstruction-with-M/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Introduction view-consistent coloring problem, fine-tuning a multi-view image generator to produce several color-coded segmentation maps of the given 3D object.
- Text- or image-to-3D generators and 3D scanners can now produce 3D assets with high-quality shapes and textures, but as single, fused entities lacking meaningful structure.

## Core Idea
- Our method leverages a multi-view diffusion model to extract plausible and view-consistent part segmentations from multiple views of a Work completed during Minghao Chen’s internship at Meta.
- To bridge this gap, we introduce PartGen, a novel approach for generating, from text, images, or unstructured 3D objects, 3D objects composed of meaningful parts.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We also demonstrate that PartGen can be easily ex
- In practice, we show that this approach better captures the artists’ intent compared to fine-tuning a model like SAM or SAM2 for the same task.
- We show that PartGen can be applied to different input modalities: starting from text, an image, or a real-world 3D scan, PartGen can generate 3D assets with meaningful ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our method leverages a multi-view diffusion model to extract plausible and view-consistent part segmentations from multiple views of a Work completed during Minghao Chen’s internship at Meta.
- To bridge this gap, we introduce PartGen, a novel approach for generating, from text, images, or unstructured 3D objects, 3D objects composed of meaningful parts.
- We assess our method empirically on a large collection of 3D assets produced by 3D artists or scanned, both quantitatively and qualitatively.

## Abstract Cue
- Text- or image-to-3D generators and 3D scanners can now produce 3D assets with high-quality shapes and textures, but as single, fused entities lacking meaningful structure.
