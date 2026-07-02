# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, depth, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Dream-to-Recon-Monocular-3D-Reconstruction-with-Diffusion/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose to leverage pre-trained 2D diffusion models and depth prediction models to generate synthetic scene geometry from a single image.
- Scene Reconstruction We first test our method’s ability to generate accurate volumetric geometry from a single image in complex scenes.
- Because our approach uses an off-the-shelf depth predictor to synthesize geometry, we also train a second BTS baseline that uses depth prediction in addition to multi-view supervision.

## 원리적 동기
- While MDE is already useful for many applications, it has a severe limitation: Depth maps are only a 2D projection of the 3D scene, and do not capture ...
- This limitation makes pure MDE unsuitable for many 3D understanding tasks, e.g. planning the path of a vehicle into a parking spot that was only partially observed.
- We propose to leverage pre-trained 2D diffusion models and depth prediction models to generate synthetic scene geometry from a single image.

## 핵심 방법론
- Scene Reconstruction We first test our method’s ability to generate accurate volumetric geometry from a single image in complex scenes.
- Because our approach uses an off-the-shelf depth predictor to synthesize geometry, we also train a second BTS baseline that uses depth prediction in addition to multi-view supervision.
- In fact, inconsistent depth predictions with slightly varying scales may even harm BTS training.
- Both the synthesized scenes and the distilled model match or surpass baselines, despite not requiring multi-view training data.
