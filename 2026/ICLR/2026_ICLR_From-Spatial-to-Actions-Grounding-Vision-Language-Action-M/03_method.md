# Method

- Year/Venue: 2026 / ICLR Poster
- Category: 3D Vision-Language Grounding
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_From-Spatial-to-Actions-Grounding-Vision-Language-Action-M/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we introduce FALCON (From Spatial to Action), a novel paradigm that injects rich 3D spatial tokens into the action head.
- In contrast, our method exhibits strong robustness to scale variations, avoiding these issues and achieving the highest success rates in both scenarios.
- FALCON leverages spatial foundation models to deliver strong geometric priors from RGB alone, and includes an Embodied Spatial Model that can optionally fuse depth, or pose for higher ...

## 원리적 동기
- These designs enable FALCON to address limitations in spatial representation, modality transferability, and alignment.
- A BSTRACT Existing vision-language-action (VLA) models act in 3D real-world but are typically built on 2D encoders, leaving a spatial reasoning gap that limits generalization and adaptability.
- In this work, we introduce FALCON (From Spatial to Action), a novel paradigm that injects rich 3D spatial tokens into the action head.

## 핵심 방법론
- In contrast, our method exhibits strong robustness to scale variations, avoiding these issues and achieving the highest success rates in both scenarios.
- To combine the aligned spatial feature e tspl with the semantic action token t̂act , we further investigate three distinct fusion approaches: 1) Cross-Attention Fusion: The action token ...
- Multi-head attention enables adaptive feature recalibration based on cross-modal relevance.
- Len. ↑ Method Task Tasks Completed in a Row (%) 1 2 3 4 5 FALCONVLM-tokens Cross-Attention FiLM-Gated FALCON (ours) ABCD→D ABCD→D ABCD→D ABCD→D 92.9 93.7 93.8 94.0 ...
- KosmosVLA (w/ rgb-d) is a point cloud-based variant where the ESM is replaced by a lightweight point cloud encoder (Ze et al., 2025) while retaining other parts.
