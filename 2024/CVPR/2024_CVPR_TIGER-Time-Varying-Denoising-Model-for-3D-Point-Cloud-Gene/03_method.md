# Method

- Year/Venue: 2024 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_TIGER-Time-Varying-Denoising-Model-for-3D-Point-Cloud-Gene/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose to merge these two properties across different timesteps in the diffusion process. plore and develop efficient and effective model architectures for 3D point cloud generation.
- In light of this observation, we propose a time-varying twostream denoising model combined with convolution layers and transformer blocks.
- The training set consists of 2, 832, 4, 612, and 2, 458 shapes, while the evaluation set is composed of 405, 662, and 352 shapes for airplanes, chairs, ...

## 원리적 동기
- Existing point cloud generative models are built on a range of frameworks, including generative adversarial networks (GANs) , variational autoenco
- However, compared to 2D images, the cost and complexity of acquiring 3D point clouds make it crucial to ex- Figure 1.
- We propose to merge these two properties across different timesteps in the diffusion process. plore and develop efficient and effective model architectures for 3D point cloud generation.

## 핵심 방법론
- The training set consists of 2, 832, 4, 612, and 2, 458 shapes, while the evaluation set is composed of 405, 662, and 352 shapes for airplanes, chairs, ...
- Following the baselines PVD and LION , we use 1-NN (1-nearest neighbor) accuracy as our evaluation metric.
- Generative Model r-GAN l-GAN(CD) l-GAN(EMD) PointFlow DPF-Net ShapeGF SoftFlow SetVAE DPM PVD TIGER LION TIGER GAN GAN GAN Normalizing Flow Normalizing Flow GAN Normalizing Flow VAE Diffusion Diffusion ...
- The overview of our decoder is shown in Fig.
