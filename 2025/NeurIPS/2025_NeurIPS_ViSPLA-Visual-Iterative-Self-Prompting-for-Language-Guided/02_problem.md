# Problem

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ViSPLA-Visual-Iterative-Self-Prompting-for-Language-Guided/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- This approach addresses several critical challenges in the field: (1) Existing single-pass inference methods lack the ability to iteratively refine predictions, often leading to suboptimal segmentation, especially on ...
- Formally, we can represent the affordance detection problem as a mapping function fθ : (P) 7→ A, where P ∈ RN ×3 denotes a point cloud with N ...
- Language-guided affordance prediction offers a mathematically elegant solution to this complex problem.

## 해결하려는 문제
- Extensive experiments demonstrate that ViSPLA achieves state-of-the-art results on both seen and unseen objects on two benchmark datasets.
- In this work, we introduce ViSPLA, a novel iterative selfprompting framework that leverages the intrinsic geometry of predicted masks for continual refinement.
- To further enhance precision and coherence, we introduce Implicit Neural Affordance Fields, which define continuous probabilistic regions over the 3D surface without additional supervision.

## 선행 연구 / 배경 단서
- This approach addresses several critical challenges in the field: (1) Existing single-pass inference methods lack the ability to iteratively refine predictions, often leading to suboptimal segmentation, especially on ...
- Formally, we can represent the affordance detection problem as a mapping function fθ : (P) 7→ A, where P ∈ RN ×3 denotes a point cloud with N ...
- Language-guided affordance prediction offers a mathematically elegant solution to this complex problem.
