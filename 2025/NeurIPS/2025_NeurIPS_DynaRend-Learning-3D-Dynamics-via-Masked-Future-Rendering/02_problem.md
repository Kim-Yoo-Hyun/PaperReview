# Problem

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_DynaRend-Learning-3D-Dynamics-via-Masked-Future-Rendering/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Despite the promise of end-to-end approaches for generalizable robotic control, the lack of abundant, diverse and high-quality robot data remains a key bottleneck.
- To address this, we leverage pretrained visual-conditioned generative models to augment target views by synthesizing novel views from existing views, reducing reliance on dense camera setups and enhancing ...
- However, these approaches mainly model dynamics in 2D and lack explicit awareness of the underlying 3D scene structure.

## 해결하려는 문제
- We evaluate DynaRend on two challenging benchmarks, RLBench and Colosseum, as well as in real-world robotic experiments, demonstrating substantial improvements in policy success rate, generalization to environmental perturbations, ...
- Learning generalizable robotic manipulation policies remains a key challenge due to the scarcity of diverse real-world training data.
- In this paper, we present DynaRend, a representation learning framework that learns 3D-aware and dynamics-informed triplane features via masked reconstruction and future prediction using differentiable volumetric rendering.

## 선행 연구 / 배경 단서
- Our contribution can be summarized as follows: • We propose DynaRend, a novel representation learning framework that learns generalizable triplane features via masked future rendering for robotic manipulation. ...
- Despite the promise of end-to-end approaches for generalizable robotic control, the lack of abundant, diverse and high-quality robot data remains a key bottleneck.
- To address this, we leverage pretrained visual-conditioned generative models to augment target views by synthesizing novel views from existing views, reducing reliance on dense camera setups and enhancing ...
