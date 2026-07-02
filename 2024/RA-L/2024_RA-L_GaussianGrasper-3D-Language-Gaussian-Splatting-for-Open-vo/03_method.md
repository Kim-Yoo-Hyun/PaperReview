# Method

- Year/Venue: 2024 / RA-L
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2024/RA-L/2024_RA-L_GaussianGrasper-3D-Language-Gaussian-Splatting-for-Open-vo/paper.pdf
- Code/Project: https://github.com/MrSecant/GaussianGrasper
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Thus, we present the GaussianGrasper, which utilizes 3D Gaussian Splatting to explicitly represent the scene as a collection of Gaussian primitives.
- In particular, we propose an Efficient Feature Distillation (EFD) module that employs contrastive learning to efficiently and accurately distill language embeddings derived from foundational models.
- Furthermore, we propose a normal-guided grasp module to select the best grasp pose.

## 원리적 동기
- To tackle this challenge, some research efforts have been dedicated to the development of language-embedded implicit fields.
- NeRF) encounter limitations due to the necessity of processing a large number of input views for reconstruction, coupled with their inherent inefficiencies in inference.
- Thus, we present the GaussianGrasper, which utilizes 3D Gaussian Splatting to explicitly represent the scene as a collection of Gaussian primitives.

## 핵심 방법론
- Our method renders accurate depth and surface normal even in areas where the ground truth is invalid.
- In the localiza- depth of the silver eyeglass case in this view because of the tion task, following LERF, given a language instruction, if the specular reflection of ...
- We also directly distill in ’Wooden fork’ and the pot and turkey with similar semantic CLIP features into 3D Gaussian field, which takes over 70 GB features in ...
