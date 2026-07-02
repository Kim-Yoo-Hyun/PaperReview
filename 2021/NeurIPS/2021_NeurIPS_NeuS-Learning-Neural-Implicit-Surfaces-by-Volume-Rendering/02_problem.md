# Problem

- Year/Venue: 2021 / NeurIPS
- Category: Foundations: 3D Scene Representations
- Tags: 3D Vision, NeRF, surface reconstruction, geometry
- Paper link: ./2021/NeurIPS/2021_NeurIPS_NeuS-Learning-Neural-Implicit-Surfaces-by-Volume-Rendering/paper.pdf
- Code/Project: https://lingjie0206.github.io/papers/NeuS/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Reconstructing surfaces from multi-view images is a fundamental problem in computer vision and computer graphics.
- The cause of this limitation is that the surface rendering method used in IDR only considers a single surface intersection point for each ray.
- 3D reconstruction with neural implicit representations has recently become a highly promising alternative to classical reconstruction approaches due to its high reconstruction quality and its potential to reconstruct ...

## 해결하려는 문제
- Experiments on the DTU dataset and the BlendedMVS dataset show that NeuS outperforms the state-of-the-arts in high-quality surface reconstruction, especially for objects and scenes with complex structures and ...
- In NeuS, we propose to represent a surface as the zero-level set of a signed distance function (SDF) and develop a new volume rendering method to train a ...
- We present a novel neural surface reconstruction method, called NeuS, for reconstructing objects and scenes with high fidelity from 2D image inputs.

## 선행 연구 / 배경 단서
- Reconstructing surfaces from multi-view images is a fundamental problem in computer vision and computer graphics.
- The cause of this limitation is that the surface rendering method used in IDR only considers a single surface intersection point for each ray.
- 3D reconstruction with neural implicit representations has recently become a highly promising alternative to classical reconstruction approaches due to its high reconstruction quality and its potential to reconstruct ...
