# Problem

- Year/Venue: 2020 / NeurIPS
- Category: Foundations: Diffusion and Generative Models
- Tags: Diffusion, generation
- Paper link: ./2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/paper.pdf
- Code/Project: https://github.com/hojonathanho/diffusion
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Deep generative models of all kinds have recently exhibited high quality samples in a wide variety of data modalities.
- Generative adversarial networks (GANs), autoregressive models, flows, and variational autoencoders (VAEs) have synthesized striking image and audio samples , and there have been remarkable advances in energy-based modeling ...
- This paper presents progress in diffusion probabilistic models .

## 해결하려는 문제
- We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin ...
- Our implementation is available at https://github.com/hojonathanho/diffusion.

## 선행 연구 / 배경 단서
- We present a more refined analysis of this phenomenon in the language of lossy compression, and we show that the sampling procedure of diffusion models is a type ...
- When the diffusion consists of small amounts of Gaussian noise, it is sufficient to set the sampling chain transitions to conditional Gaussians too, allowing for a particularly simple ...
- In addition, we show that a certain parameterization of diffusion models reveals an equivalence with denoising score matching over multiple noise levels during training and with annealed Langevin ...
