# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_MVSplat-Efficient-3D-Gaussian-Splatting-from-Sparse-Multi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- For better efficiency, we use Swin Transformer’s local window attention in our Transformer architecture.
- Then, we use a multi-view Transformer with selfand cross-attention layers to exchange information between different views.
- In this paper, we present MVSplat, a Gaussian-based feed-forward model for novel view synthesis.

## 원리적 동기
- However, reconstructing a 3D scene from a single image is inherently ill-posed and ambiguous, posing a significant challenge when applied to a more general and larger scene, which ...
- We consider the problem of 3D scene reconstruction and novel view synthesis from very sparse (i.e., as few as two) images in just one forward pass of a ...
- For better efficiency, we use Swin Transformer’s local window attention in our Transformer architecture.

## 핵심 방법론
- For better efficiency, we use Swin Transformer’s local window attention in our Transformer architecture.
- Then, we use a multi-view Transformer with selfand cross-attention layers to exchange information between different views.
- In this paper, we present MVSplat, a Gaussian-based feed-forward model for novel view synthesis.
- Unlike pixelSplat that predicts probabilistic depth, we develop an efficient and high-performance multi-view depth estimation model that enables unprojecting predicted depth maps as the Gaussian centers, in parallel ...
- To construct the cost volumes, we first extract multi-view image features with a CNN and Transformer architecture .
