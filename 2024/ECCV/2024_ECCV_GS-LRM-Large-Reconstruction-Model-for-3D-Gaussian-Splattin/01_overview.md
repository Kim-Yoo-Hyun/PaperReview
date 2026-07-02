# GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_GS-LRM-Large-Reconstruction-Model-for-3D-Gaussian-Splattin/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Reconstructing a 3D scene from image captures is both a central problem and a long-standing challenge in computer vision.
- However, these models adopt triplane NeRF as the scene representation, which suffers from a limited triplane resolution and expensive volume rendering.
- Recently, transformer-based 3D large reconstruction models (LRMs) have been proposed, learning general 3D reconstruction priors from vast collections of 3D objects and achieving sparse-view 3D reconstruction of unprecedented ...

## Core Idea
- In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.
- We propose GS-LRM, a scalable large reconstruction model that can predict high-quality 3D Gaussian primitives from 2-4 posed sparse images in ∼0.23 seconds on single A100 GPU.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In both scenarios, the models outperform state-of-the-art baselines by a wide margin.
- We refer the readers to our project page for video results and interactive visualizations.
- We also demonstrate applications of our model in downstream 3D generation tasks.

## Limitation
- We hope that our work can inspire more future work in the space of data-driven feed-forward 3D reconstruction.

## Contribution
- Our model features a very simple transformer-based architecture; we patchify input posed images, pass the concatenated multi-view image tokens through a sequence of transformer blocks, and decode final ...
- We propose GS-LRM, a scalable large reconstruction model that can predict high-quality 3D Gaussian primitives from 2-4 posed sparse images in ∼0.23 seconds on single A100 GPU.
- We show that our model can work on both object and scene captures by training it on Objaverse and RealEstate10K respectively.

## Abstract Cue
- We propose GS-LRM, a scalable large reconstruction model that can predict high-quality 3D Gaussian primitives from 2-4 posed sparse images in ∼0.23 seconds on single A100 GPU.
