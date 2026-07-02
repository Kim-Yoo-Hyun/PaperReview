# pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction

- Year/Venue: 2024 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_pixelSplat-3D-Gaussian-Splats-from-Image-Pairs-for-Scalabl/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Introduction We investigate the problem of generalizable novel view synthesis from sparse image observations.
- To overcome local minima inherent to sparse and locally supported representations, we predict a dense probability distribution over 3D and sample Gaussian means from that probability distribution.

## Core Idea
- We present pixelSplat, which brings the benefits of a primitive-based 3D representation—fast and memoryefficient rendering as well a Ours No Epipolar Encoder No Depth Encoding No Probabilistic Sampling ...
- We introduce pixelSplat, a feed-forward model that learns to reconstruct 3D radiance fields parameterized by 3D Gaussian primitives from pairs of images.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We benchmark our method on wide-baseline novel view synthesis on the real-world RealEstate10k and ACID datasets, where we outperform state-of-the-art light field transformers and accelerate rendering by 2.5 ...
- Meanwhile, recent work on single-scene novel view synthesis has shown that it is possible to use 3D Gaussian primitives to enable real-time rendering with little memory cost via ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We benchmark our method on wide-baseline novel view synthesis on the real-world RealEstate10k and ACID datasets, where we outperform state-of-the-art light field transformers and accelerate rendering by 2.5 ...
- We introduce pixelSplat, a feed-forward model that learns to reconstruct 3D radiance fields parameterized by 3D Gaussian primitives from pairs of images.
- This has motivated light-field transformers , where a ray is rendered by embedding it into a query token and a color is obtained via cross-attention over image tokens.

## Abstract Cue
- We introduce pixelSplat, a feed-forward model that learns to reconstruct 3D radiance fields parameterized by 3D Gaussian primitives from pairs of images.
