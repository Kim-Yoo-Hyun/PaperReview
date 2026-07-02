# Method

- Year/Venue: 2025 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_Taming-Video-Diffusion-Prior-with-Scene-Grounding-Guidance/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose using video diffusion models that provide plausible interpretations for regions that are outside the field of view and occluded.
- To tackle these issues, we propose to use a reconstruction by generation pipeline that leverages learned priors from video diffusion models to provide plausible interpretations for regions outside ...
- To resolve inconsistencies within generated sequences, we introduce a novel scene-grounding guidance that controls the diffusion model to generate consistent sequences without any fine-tuning.

## 원리적 동기
- Despite recent successes in novel view synthesis using 3D Gaussian Splatting (3DGS), modeling scenes with sparse inputs remains a challenge.
- Despite recent advances in scene representations based on 3DGS, modeling scenes with sparse inputs remains a significant challenge.
- We propose using video diffusion models that provide plausible interpretations for regions that are outside the field of view and occluded.

## 핵심 방법론
- We propose using video diffusion models that provide plausible interpretations for regions that are outside the field of view and occluded.
- To resolve inconsistencies within generated sequences, we introduce a novel scene-grounding guidance that controls the diffusion model to generate consistent sequences without any fine-tuning.
- Additionally, we propose a trajectory initialization strategy to enhance holistic modeling and develop a scheme for optimizing 3DGS with generated sequences.
- 5, our method effectively addresses the extrapolation issue (e.g., the ceiling in the fourth row) and mitigates needle-like artifacts observed in the rendered images of DNGaussian and FSGS ...
- Our method not only effectively addresses extrapolation and occlusion (red boxes), improving the overall quality (blue boxes), but also predicts more plausible geometry.
