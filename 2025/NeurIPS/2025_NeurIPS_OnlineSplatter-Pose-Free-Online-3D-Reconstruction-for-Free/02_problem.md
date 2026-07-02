# Problem

- Year/Venue: 2025 / NeurIPS spotlight
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_OnlineSplatter-Pose-Free-Online-3D-Reconstruction-for-Free/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Motivated by these challenges, we propose OnlineSplatter, a feed-forward framework for online reconstruction of freely moving objects.
- Real-time 3D reconstruction of freely moving objects from monocular video remains a fundamental challenge in computer vision, with far-reaching implications for robotics, augmented reality, and interactive 3D applications ...
- The challenge is especially acute in an online setting, where systems must update their understanding of objects as every new frame arrives, a capability essential for autonomous robots ...

## 해결하려는 문제
- Our approach anchors reconstruction using the first frame and progressively refines the object representation through a dense Gaussian primitive field, maintaining constant computational cost regardless of video sequence ...
- We introduce OnlineSplatter, a novel online feed-forward framework generating highquality, object-centric 3D Gaussians directly from RGB frames without requiring camera pose, depth priors, or bundle optimization.
- Evaluations on real-world datasets demonstrate that OnlineSplatter significantly outperforms state-of-the-art pose-free reconstruction baselines, consistently improving with more observations while maintaining constant memory and runtime.

## 선행 연구 / 배경 단서
- Motivated by these challenges, we propose OnlineSplatter, a feed-forward framework for online reconstruction of freely moving objects.
- Real-time 3D reconstruction of freely moving objects from monocular video remains a fundamental challenge in computer vision, with far-reaching implications for robotics, augmented reality, and interactive 3D applications ...
- The challenge is especially acute in an online setting, where systems must update their understanding of objects as every new frame arrives, a capability essential for autonomous robots ...
