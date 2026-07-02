# Method

- Year/Venue: 2021 / NeurIPS
- Category: Foundations: 3D Scene Representations
- Tags: 3D Vision, NeRF, surface reconstruction, geometry
- Paper link: ./2021/NeurIPS/2021_NeurIPS_NeuS-Learning-Neural-Implicit-Surfaces-by-Volume-Rendering/paper.pdf
- Code/Project: https://lingjie0206.github.io/papers/NeuS/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In NeuS, we propose to represent a surface as the zero-level set of a signed distance function (SDF) and develop a new volume rendering method to train a ...
- We present a novel neural surface reconstruction method, called NeuS, for reconstructing objects and scenes with high fidelity from 2D image inputs.
- In order to learn the weights of the neural network, we developed a novel volume rendering method to render images from the implicit SDF and minimize the difference ...

## 원리적 동기
- Reconstructing surfaces from multi-view images is a fundamental problem in computer vision and computer graphics.
- The cause of this limitation is that the surface rendering method used in IDR only considers a single surface intersection point for each ray.
- In NeuS, we propose to represent a surface as the zero-level set of a signed distance function (SDF) and develop a new volume rendering method to train a ...

## 핵심 방법론
- In order to learn the weights of the neural network, we developed a novel volume rendering method to render images from the implicit SDF and minimize the difference ...
- The surface S of the object is represented by the zero-level set of its SDF, that is, S = x ∈ R3 |f (x) = 0 . (1) ...
