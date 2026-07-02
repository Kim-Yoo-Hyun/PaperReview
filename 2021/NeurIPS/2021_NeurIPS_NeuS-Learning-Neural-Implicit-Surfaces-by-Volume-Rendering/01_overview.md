# NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction

- Year/Venue: 2021 / NeurIPS
- Category: Foundations: 3D Scene Representations
- Tags: 3D Vision, NeRF, surface reconstruction, geometry
- Paper link: ./2021/NeurIPS/2021_NeurIPS_NeuS-Learning-Neural-Implicit-Surfaces-by-Volume-Rendering/paper.pdf
- Code/Project: https://lingjie0206.github.io/papers/NeuS/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Reconstructing surfaces from multi-view images is a fundamental problem in computer vision and computer graphics.
- The cause of this limitation is that the surface rendering method used in IDR only considers a single surface intersection point for each ray.
- 3D reconstruction with neural implicit representations has recently become a highly promising alternative to classical reconstruction approaches due to its high reconstruction quality and its potential to reconstruct ...

## Core Idea
- In NeuS, we propose to represent a surface as the zero-level set of a signed distance function (SDF) and develop a new volume rendering method to train a ...
- We present a novel neural surface reconstruction method, called NeuS, for reconstructing objects and scenes with high fidelity from 2D image inputs.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on the DTU dataset and the BlendedMVS dataset show that NeuS outperforms the state-of-the-arts in high-quality surface reconstruction, especially for objects and scenes with complex structures and ...
- The results show that our approach outperforms the baseline methods on the DTU dataset in both settings – w/ and w/o mask in terms of the Chamfer distance.
- COLMAP results are achieved by trim=0.

## Limitation
- One limitation of our method is that although our method does not heavily rely on correspondence matching of texture features, the performance would still degrade for textureless objects ...

## Contribution
- Experiments on the DTU dataset and the BlendedMVS dataset show that NeuS outperforms the state-of-the-arts in high-quality surface reconstruction, especially for objects and scenes with complex structures and ...
- In NeuS, we propose to represent a surface as the zero-level set of a signed distance function (SDF) and develop a new volume rendering method to train a ...
- We present a novel neural surface reconstruction method, called NeuS, for reconstructing objects and scenes with high fidelity from 2D image inputs.

## Abstract Cue
- We present a novel neural surface reconstruction method, called NeuS, for reconstructing objects and scenes with high fidelity from 2D image inputs.
