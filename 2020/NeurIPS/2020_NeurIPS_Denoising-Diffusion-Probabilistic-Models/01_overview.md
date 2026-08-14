# Denoising Diffusion Probabilistic Models

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2020 / NeurIPS
- Category: Foundations: Generative Models
- Tags: Diffusion, Generation
- Paper link: ./2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/paper.pdf
- Code/Project: https://github.com/hojonathanho/diffusion
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Deep generative models of all kinds have recently exhibited high quality samples in a wide variety of data modalities.
- Generative adversarial networks (GANs), autoregressive models, flows, and variational autoencoders (VAEs) have synthesized striking image and audio samples , and there have been remarkable advances in energy-based modeling ...
- This paper presents progress in diffusion probabilistic models .

## Core Idea
- We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- We present a more refined analysis of this phenomenon in the language of lossy compression, and we show that the sampling procedure of diffusion models is a type ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- With our FID score of 3.17, our unconditional model achieves better sample quality than most models in the literature, including class conditional models.
- On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17.
- We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin ...
- Our implementation is available at https://github.com/hojonathanho/diffusion.

## Abstract Cue
- We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
