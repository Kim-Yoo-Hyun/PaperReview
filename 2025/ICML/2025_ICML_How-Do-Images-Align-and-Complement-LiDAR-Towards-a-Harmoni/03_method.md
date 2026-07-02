# Method

- Year/Venue: 2025 / ICML Poster
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2025/ICML/2025_ICML_How-Do-Images-Align-and-Complement-LiDAR-Towards-a-Harmoni/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address these issues, we propose Image-Assists-LiDAR (IAL), a novel multimodal 3D panoptic segmentation framework.
- We present comprehensive comparison results for LiDAR panoptic segmentation performance on the nuScenes validation and test sets, as shown in Table 2 and Table 3.
- We use AdamW (Kingma & Ba, 2014) as the optimizer, with a default weight decay of 0.01.

## 원리적 동기
- Recently, a few studies have sought to overcome this challenge by integrating LiDAR inputs with camera images, leveraging the rich and dense texture information provided by the latter.
- However, LiDAR inherently faces limitations in detecting small or distant objects due to its radial emission pattern, which results in sparse returns along each laser ray (Li et ...
- To address these issues, we propose Image-Assists-LiDAR (IAL), a novel multimodal 3D panoptic segmentation framework.

## 핵심 방법론
- We present comprehensive comparison results for LiDAR panoptic segmentation performance on the nuScenes validation and test sets, as shown in Table 2 and Table 3.
- We use AdamW (Kingma & Ba, 2014) as the optimizer, with a default weight decay of 0.01.
- The LiDAR branch is built upon the architecture of P3former.
- The training spans 80 epochs for nuScenes and 36 epochs for SemanticKITTI.
