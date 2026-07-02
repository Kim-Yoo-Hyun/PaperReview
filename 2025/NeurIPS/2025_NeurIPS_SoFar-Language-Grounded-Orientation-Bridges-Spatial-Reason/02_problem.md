# Problem

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_SoFar-Language-Grounded-Orientation-Bridges-Spatial-Reason/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, translating a specific language description into a desired orientation is challenging for existing VLMs.
- While prior works emphasize position relationship, orientation understanding is equally critical for defining the full 6-DoF of object pose or end-effector poses .
- These annotations are from Objaverse and generated automatically by prompting GPT-4o with rich semantic queries covering both intra-object spatial reasoning and inter-object manipulation contexts—eliminating the need for costly ...

## 해결하려는 문제
- Extensive experiments demonstrated the effectiveness and generalization of our S O FAR, e.g., zero-shot 48.7% successful rate on Open6DOR and zero-shot 74.9% successful rate on SIMPLER-Env.
- In this paper, we introduce the concept of semantic orientation, which defines object orientations using natural language in a reference-frame-free manner (e.g., the “plug-in” direction of a USB ...

## 선행 연구 / 배경 단서
- Our method significantly outperforms state-of-the-art VLMs and VLA models—even those trained on expensive robot trajectories—across both simulated and real-world tasks.
- However, translating a specific language description into a desired orientation is challenging for existing VLMs.
- While prior works emphasize position relationship, orientation understanding is equally critical for defining the full 6-DoF of object pose or end-effector poses .
