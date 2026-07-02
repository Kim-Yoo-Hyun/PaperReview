# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_GSV3D-Gaussian-Splatting-based-Geometric-Distillation-with/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose a method that leverages 2D diffusion models’ implicit 3D reasoning ability while ensuring 3D consistency via Gaussian-splattingbased geometric distillation.
- As a result, our approach simultaneously generates high-quality, multi-viewconsistent images and accurate 3D models, providing a 1.
- This limitation stems from the restricted diversity of the training data, which hinders the model’s ability to generalize well to unseen or complex scenarios.

## 원리적 동기
- However, existing methods have limitations: 3D diffusion models are limited by dataset scarcity and the absence of strong pretrained priors, while 2D diffusion-based approaches struggle with geometric consistency.
- This limitation restricts the generalization ability of these models and makes it difficult for them to capture complex details across var- ious object types.
- We propose a method that leverages 2D diffusion models’ implicit 3D reasoning ability while ensuring 3D consistency via Gaussian-splattingbased geometric distillation.

## 핵심 방법론
- This limitation stems from the restricted diversity of the training data, which hinders the model’s ability to generalize well to unseen or complex scenarios.
- GaussianAnything and TriplaneGaussians are 3D methods, while LGM, Zero123Plus, Era3D, and SV3D are 2D methods.
- GA and TGS are abbreviations for GaussianAnything and TriplaneGaussian, respectively.
