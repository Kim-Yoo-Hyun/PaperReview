# Problem

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Diffusion
- Paper link: ./2025/ICCV/2025_ICCV_On-Device-Diffusion-Transformer-Policy-for-Efficient-Robot/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We first conduct an extensive computational analysis on existing Diffusion Policy architectures, identifying the denoising network as the primary contributor to latency.
- However, this endeavor presents multifaceted challenges: 1) Diffusion Policies require multiple denoising steps, which slows down the generation process; 2) the standard architectures involve billions of parameters, leading ...
- To address these challenges, recent work by DeeR-VLA introduces a multi-exit architecture built on the Roboflamingo framework , enabling dynamic termination of the computation process to accelerate action ...

## 해결하려는 문제
- Extensive real-world experiments also show the proposed LightDP can achieve performance comparable to state-ofthe-art Diffusion Policies.
- We first conduct an extensive computational analysis on existing Diffusion Policy architectures, identifying the denoising network as the primary contributor to latency.
- However, this endeavor presents multifaceted challenges: 1) Diffusion Policies require multiple denoising steps, which slows down the generation process; 2) the standard architectures involve billions of parameters, leading ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
