# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_GS-LRM-Large-Reconstruction-Model-for-3D-Gaussian-Splattin/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.
- We propose GS-LRM, a scalable large reconstruction model that can predict high-quality 3D Gaussian primitives from 2-4 posed sparse images in ∼0.23 seconds on single A100 GPU.
- Our model features a very simple transformer-based architecture; we patchify input posed images, pass the concatenated multi-view image tokens through a sequence of transformer blocks, and decode final ...

## 원리적 동기
- Reconstructing a 3D scene from image captures is both a central problem and a long-standing challenge in computer vision.
- However, these models adopt triplane NeRF as the scene representation, which suffers from a limited triplane resolution and expensive volume rendering.
- In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.

## 핵심 방법론
- In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.
- 3.1 Transformer-based Model Architecture As shown in Fig.
- Following prior works , we use the Plücker ray coordinates of each image {Pi ∈ RH×W ×6 } computed from the camera parameters for pose conditioning.
- Multi-view image tokens are then concatenated and passed through a sequence of transformer blocks consisting of self-attention and MLP layers.
- 2, we train a transformer model to regress per-pixel 3D GS parameters from a set of images with known camera poses.
