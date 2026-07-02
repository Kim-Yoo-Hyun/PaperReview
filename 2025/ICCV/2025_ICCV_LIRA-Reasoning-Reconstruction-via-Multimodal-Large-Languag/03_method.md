# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, Vision-Language
- Paper link: ./2025/ICCV/2025_ICCV_LIRA-Reasoning-Reconstruction-via-Multimodal-Large-Languag/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To handle this task, we propose LIRA: Language Instructed Reconstruction Assistant.
- Since the evaluation system for this task is not well established, we propose a benchmark ReasonRecon comprising the largest collection of scene-instruction data samples involving implicit reasoning.
- In LIRA, to achieve higher instance fusion quality, we propose TIFF, a Text-enhanced Instance Fusion module operating within Fragment bounding volume, which is learning-based and fuses multiple keyframes ...

## 원리적 동기
- Existing language instruction-guided online 3D reconstruction systems mainly rely on explicit instructions or queryable maps, showing inadequate capability to handle implicit and complex instructions.
- Experiments demonstrate that LIRA outperforms existing methods in the reasoning reconstruction task and is capable of running in real time.
- To handle this task, we propose LIRA: Language Instructed Reconstruction Assistant.

## 핵심 방법론
- We use 3 transformer blocks with a feature dimension of 128 in the instance fusion module.
- Unless otherwise speciﬁed, in the 2D reasoning segmentation module, we use LLaVA-7B as the base VLM, and adopt SAM with ViT-H backbone as the segmentation foundation model.
- Then, we use the cluster centers as prompts and apply SAM to generate the corresponding segmentation mask.
- The training set and test set are divided into 8 : 2.
- Loss functions and more implementation details are described in the supplementary material.
