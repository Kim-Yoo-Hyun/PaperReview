# Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment

- Year/Venue: 2025 / ICML poster
- Category: 3D Equivariance, Calibration, and Registration
- Tags: semantic, alignment, Diffusion, Generation, equivariant, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_Scalable-Non-Equivariant-3D-Molecule-Generation-via-Rotati/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Different from data with grid-like structures (e.g., images and text sequences), 3D molecules pose unique challenges to generative modeling due to the Euclidean symmetry group of R3 , ...

## Core Idea
- In this paper, we propose an approach that relaxes such equivariance constraints.
- Specifically, our approach learns a sample-dependent SO(3) transformation for each molecule to construct an aligned latent space.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- It yields sample quality comparable to state-of-the-art equivariant diffusion models and offers improved training and sampling efficiency.
- Experimental results demonstrate that our approach performs significantly better than previously reported nonequivariant models.
- Equivariant diffusion models have achieved impressive performance in 3D molecule generation.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- It yields sample quality comparable to state-of-the-art equivariant diffusion models and offers improved training and sampling efficiency.
- Experimental results demonstrate that our approach performs significantly better than previously reported nonequivariant models.
- However, specialized equivariant architectures limit the scalability and efficiency of diffusion models.

## Abstract Cue
- language (von Rütte et al., 2025), molecules (Hoogeboom et al., 2022), proteins (Yim et al., 2023).
