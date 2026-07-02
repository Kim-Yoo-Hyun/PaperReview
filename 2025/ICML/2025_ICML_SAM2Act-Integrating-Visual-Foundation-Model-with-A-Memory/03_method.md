# Method

- Year/Venue: 2025 / ICML Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Imitation Learning
- Paper link: ./2025/ICML/2025_ICML_SAM2Act-Integrating-Visual-Foundation-Model-with-A-Memory/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Building on this foundation, we propose SAM2Act+, a memory-based architecture inspired by SAM2, which incorporates a memory bank, an encoder, and an attention mechanism to enhance spatial memory.
- To bridge this gap, we introduce SAM2Act, a multi-view robotic transformerbased policy that leverages multi-resolution upsampling with visual representations from largescale foundation model.
- To address the need for evaluating memory-dependent tasks, we introduce MemoryBench, a novel benchmark designed to assess spatial memory and action recall in robotic manipulation.

## 원리적 동기
- While significant progress has been made in robotic manipulation, existing approaches often fall short in generalization to complex environmental variations and addressing memorydependent tasks.
- Significant progress has been made in robotic manipulation through prior work.
- Building on this foundation, we propose SAM2Act+, a memory-based architecture inspired by SAM2, which incorporates a memory bank, an encoder, and an attention mechanism to enhance spatial memory.

## 핵심 방법론
- We use the software stack as in (Grotz et al., 2024).
- RVT-2 is a multi-view robotics transformer that leverages a coarse-to-fine approach on the constructed point cloud to predict the next best action heatmap.
