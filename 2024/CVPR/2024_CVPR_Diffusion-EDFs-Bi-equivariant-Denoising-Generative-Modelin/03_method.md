# Method

- Year/Venue: 2024 / CVPR
- Category: Equivariance, Diffusion, and 3D Action
- Tags: equivariant, Diffusion, Robotics
- Paper link: ./2024/CVPR/2024_CVPR_Diffusion-EDFs-Bi-equivariant-Denoising-Generative-Modelin/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we present Diffuion-EDFs, a diffusionbased alternative to EDFs with a significantly reduced training time (×15 faster).
- This enables our method to be trained end-to-end from only 5∼10 human demonstrations without requiring any pre-training and object segmentation, yet are highly generalizable to out-of-distribution object configurations.
- In this paper, we present Diffusion-EDFs, a novel SE(3)-equivariant diffusion-based approach for visual robotic manipulation tasks.

## 원리적 동기
- Diffusion generative modeling has become a promising approach for learning robotic manipulation tasks from stochastic human demonstrations.
- In this paper, we present Diffusion-EDFs, a novel SE(3)-equivariant diffusion-based approach for visual robotic manipulation tasks.
- In this paper, we present Diffuion-EDFs, a diffusionbased alternative to EDFs with a significantly reduced training time (×15 faster).

## 핵심 방법론
- R-NDFs Default (Trained Setup) SE(3)-DiffusionFields Diffusion-EDFs (Ours) R-NDFs Previously Unseen Instances SE(3)-DiffusionFields Diffusion-EDFs (Ours) R-NDFs Previously Unseen Poses SE(3)-DiffusionFields SE(3)-DiffusionFields Diffusion-EDFs (Ours) § Models with segmented inputs are ...
- 5) Diffusion-EDFs infer the gripper pose to place the grasped object on the placement target.
- 2) Diffusion-EDFs infer the gripper pose to pick up the target object.
