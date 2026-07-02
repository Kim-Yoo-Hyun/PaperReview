# SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space

- Year/Venue: 2025 / ICML Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Diffusion, Imitation Learning, equivariant
- Paper link: ./2025/ICML/2025_ICML_SE3-Equivariant-Diffusion-Policy-in-Spherical-Fourier-Spac/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Diffusion Policy may struggle to attain robust 3D generalization without training on a large amount of costly human demonstrations to exhaust the possible 3D arrangements of the scene.

## Core Idea
- We propose Spherical Diffusion Policy (SDP), a Fourier space SE(3) equivariant method that automatically adapts to changes in the scene.
- To address this issue, we propose Spherical Diffusion Policy (SDP), an SE(3) equivariant diffusion policy that adapts trajectories according to 3D transformations of the scene.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Lastly, we propose a spherical denoising temporal U-net that achieves spatiotemporal equivariance with computational efficiency.
- SDP demonstrates a large performance improvement over strong baselines in 20 simulation tasks and 5 physical robot tasks including single-arm and bi-manual embodiments.
- Such equivariance is achieved by embedding the states, actions, and the denoising process in spherical Fourier space.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address this issue, we propose Spherical Diffusion Policy (SDP), an SE(3) equivariant diffusion policy that adapts trajectories according to 3D transformations of the scene.
- We propose Spherical Diffusion Policy (SDP), a Fourier space SE(3) equivariant method that automatically adapts to changes in the scene.
- Lastly, we propose a spherical denoising temporal U-net that achieves spatiotemporal equivariance with computational efficiency.

## Abstract Cue
- Diffusion Policies are effective at learning closed-loop manipulation policies from human demonstrations but generalize poorly to novel arrangements of objects in 3D space, hurting real-world performance.
