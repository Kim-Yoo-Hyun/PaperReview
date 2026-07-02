# Method

- Year/Venue: 2025 / NeurIPS spotlight
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_OnlineSplatter-Pose-Free-Online-3D-Reconstruction-for-Free/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce OnlineSplatter, a novel online feed-forward framework generating highquality, object-centric 3D Gaussians directly from RGB frames without requiring camera pose, depth priors, or bundle optimization.
- To differentiate and contextualize these tokens, we introduce
- Our approach anchors reconstruction using the first frame and progressively refines the object representation through a dense Gaussian primitive field, maintaining constant computational cost regardless of video sequence ...

## 원리적 동기
- Motivated by these challenges, we propose OnlineSplatter, a feed-forward framework for online reconstruction of freely moving objects.
- Real-time 3D reconstruction of freely moving objects from monocular video remains a fundamental challenge in computer vision, with far-reaching implications for robotics, augmented reality, and interactive 3D applications ...
- We introduce OnlineSplatter, a novel online feed-forward framework generating highquality, object-centric 3D Gaussians directly from RGB frames without requiring camera pose, depth priors, or bundle optimization.

## 핵심 방법론
- To differentiate and contextualize these tokens, we introduce
- The goal of our method is to perform an online reconstruction of a freely moving rigid object using monocular RGB images without relying on known camera poses or ...
- While most reconstruction methods implicitly rely on static scenes and background surfaces for stability, our approach explicitly handles freely moving objects in isolation.
- The term "online" implies that our approach processes incoming data causally, updating the reconstructed object representation incrementally as new frames become available.
- We therefore introduce a learnable counterpart, EncoderI2 , which adopts the same architecture but is trained end-to-end within OnlineSplatter to capture complementary geometric cues.
