# Problem

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_GS-LRM-Large-Reconstruction-Model-for-3D-Gaussian-Splattin/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Reconstructing a 3D scene from image captures is both a central problem and a long-standing challenge in computer vision.
- However, these models adopt triplane NeRF as the scene representation, which suffers from a limited triplane resolution and expensive volume rendering.
- Recently, transformer-based 3D large reconstruction models (LRMs) have been proposed, learning general 3D reconstruction priors from vast collections of 3D objects and achieving sparse-view 3D reconstruction of unprecedented ...

## 해결하려는 문제
- Our model features a very simple transformer-based architecture; we patchify input posed images, pass the concatenated multi-view image tokens through a sequence of transformer blocks, and decode final ...
- We propose GS-LRM, a scalable large reconstruction model that can predict high-quality 3D Gaussian primitives from 2-4 posed sparse images in ∼0.23 seconds on single A100 GPU.
- We show that our model can work on both object and scene captures by training it on Objaverse and RealEstate10K respectively.

## 선행 연구 / 배경 단서
- Reconstructing a 3D scene from image captures is both a central problem and a long-standing challenge in computer vision.
- Recently, transformer-based 3D large reconstruction models (LRMs) have been proposed, learning general 3D reconstruction priors from vast collections of 3D objects and achieving sparse-view 3D reconstruction of unprecedented ...
- However, these models adopt triplane NeRF as the scene representation, which suffers from a limited triplane resolution and expensive volume rendering.
