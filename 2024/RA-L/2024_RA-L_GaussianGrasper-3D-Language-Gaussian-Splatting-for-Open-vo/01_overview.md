# GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping

- Year/Venue: 2024 / RA-L
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2024/RA-L/2024_RA-L_GaussianGrasper-3D-Language-Gaussian-Splatting-for-Open-vo/paper.pdf
- Code/Project: https://github.com/MrSecant/GaussianGrasper
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To tackle this challenge, some research efforts have been dedicated to the development of language-embedded implicit fields.
- NeRF) encounter limitations due to the necessity of processing a large number of input views for reconstruction, coupled with their inherent inefficiencies in inference.

## Core Idea
- Thus, we present the GaussianGrasper, which utilizes 3D Gaussian Splatting to explicitly represent the scene as a collection of Gaussian primitives.
- In particular, we propose an Efficient Feature Distillation (EFD) module that employs contrastive learning to efficiently and accurately distill language embeddings derived from foundational models.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Through comprehensive real-world experiments, we demonstrate that GaussianGrasper enables robots to accurately query and grasp objects with language instructions, providing a new solution for language-guided manipulation tasks.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Thus, we present the GaussianGrasper, which utilizes 3D Gaussian Splatting to explicitly represent the scene as a collection of Gaussian primitives.
- Through comprehensive real-world experiments, we demonstrate that GaussianGrasper enables robots to accurately query and grasp objects with language instructions, providing a new solution for language-guided manipulation tasks.
- With the reconstructed geometry of the Gaussian field, our method enables the pre-trained grasping model to generate collision-free grasp pose candidates.

## Abstract Cue
- —Constructing a 3D scene capable of accommodating open-ended language queries, is a pivotal pursuit, particularly within the domain of robotics.
