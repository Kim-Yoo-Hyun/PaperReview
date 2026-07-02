# Method

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision, equivariant
- Paper link: ./2025/NeurIPS/2025_NeurIPS_3D-Equivariant-Visuomotor-Policy-Learning-via-Spherical-Pr/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- The observation x ∈ X consists of two parts, an eye-in-hand RGB image I, that captures visual information, and proprioceptive data, P ∈ R7 , including the end-effector’s ...
- In the following subsections, we first describe our observation encoder, which extracts SO(3)-equivariant features from 2D images, and then our equivariant diffusion module.
- The observation encoder uses spherical projection to map image-extracted features onto a hemisphere and applies spherical convolutions to ensure SO(3)-equivariance, producing the conditioning vector for the diffusion process.

## 원리적 동기
- When used with RGB data, current equivariant policies are unable to fully leverage the SO(3) structure present in the problem and underperform the point cloud version significantly .
- This paper addresses this challenge by introducing a novel diffusion policy framework that incorporates SO(3)-equivariance into eye-in-hand visuomotor learning.
- The observation x ∈ X consists of two parts, an eye-in-hand RGB image I, that captures visual information, and proprioceptive data, P ∈ R7 , including the end-effector’s ...

## 핵심 방법론
- The observation x ∈ X consists of two parts, an eye-in-hand RGB image I, that captures visual information, and proprioceptive data, P ∈ R7 , including the end-effector’s ...
- In the following subsections, we first describe our observation encoder, which extracts SO(3)-equivariant features from 2D images, and then our equivariant diffusion module.
- The observation encoder uses spherical projection to map image-extracted features onto a hemisphere and applies spherical convolutions to ensure SO(3)-equivariance, producing the conditioning vector for the diffusion process.
- The diffusion module is designed as an SO(3)equivariant function of the conditioning vectors and noisy inputs.
- Image Encoder Our image encoder is detailed in Figure 2a.
