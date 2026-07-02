# Method

- Year/Venue: 2025 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, grounding, LVLM
- Paper link: ./2025/CVPR/2025_CVPR_ReasonGrounder-LVLM-Guided-Hierarchical-Feature-Splatting/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we propose ReasonGrounder, an LVLM-guided framework that uses hierarchical 3D feature Gaussian fields for adaptive grouping based on physical scale, enabling open-vocabulary 3D grounding and ...
- We use LLaVA 1.5 as the LVLM in our ReasonGrounder.
- To extract language features from each image, we use the OpenCLIP ViT-B/16 model.

## 원리적 동기
- Open-vocabulary 3D visual grounding and reasoning aim to localize objects in a scene based on implicit language descriptions, even when they are occluded.
- This ability is crucial for tasks such as vision-language navigation and autonomous robotics.
- In this work, we propose ReasonGrounder, an LVLM-guided framework that uses hierarchical 3D feature Gaussian fields for adaptive grouping based on physical scale, enabling open-vocabulary 3D grounding and ...

## 핵심 방법론
- We use LLaVA 1.5 as the LVLM in our ReasonGrounder.
- To extract language features from each image, we use the OpenCLIP ViT-B/16 model.
- We then train the hierarchical feature Gaussian field by fixing all other parameters of the 3D Gaussians.
- Each scene is first trained using 3D Gaussian Splatting for 30,000 iterations with default parameters from .
