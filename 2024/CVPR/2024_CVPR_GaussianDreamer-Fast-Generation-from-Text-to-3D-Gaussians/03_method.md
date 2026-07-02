# Method

- Year/Venue: 2024 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_GaussianDreamer-Fast-Generation-from-Text-to-3D-Gaussians/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Conclusion We propose a fast text-to-3D method GaussianDreamer by bridging the abilities of 3D and 2D diffusion models via the Gaussian splatting representation.
- Visualization Results In this section, we present the results of initializing the 3D Gaussians with two different 3D diffusion models: text-to3D and text-to-motion diffusion models.
- The 3D diffusion models used in our method are Shap-E and MDM , and we load the Shap-E model finetuned on Objaverse in Cap3D .

## 원리적 동기
- 3D diffusion models have good 3D consistency, but their quality and generalization are limited as trainable 3D data is expensive and hard to obtain.
- Introduction 3D asset generation has been an expensive and professional work in conventional pipelines.
- Conclusion We propose a fast text-to-3D method GaussianDreamer by bridging the abilities of 3D and 2D diffusion models via the Gaussian splatting representation.

## 핵심 방법론
- Conclusion We propose a fast text-to-3D method GaussianDreamer by bridging the abilities of 3D and 2D diffusion models via the Gaussian splatting representation.
- Visualization Results In this section, we present the results of initializing the 3D Gaussians with two different 3D diffusion models: text-to3D and text-to-motion diffusion models.
- The 3D diffusion models used in our method are Shap-E and MDM , and we load the Shap-E model finetuned on Objaverse in Cap3D .
- In the third row, the generation result of Shap-E is far different from the given text prompt while our method makes the 3D assets closer to the prompt ...
- Our approach utilizes 3D diffusion model priors, which greatly alleviates the issue of multi-face problems.
