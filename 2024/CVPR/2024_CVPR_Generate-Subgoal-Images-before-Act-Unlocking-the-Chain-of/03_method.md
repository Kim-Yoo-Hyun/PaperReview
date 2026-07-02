# Method

- Year/Venue: 2024 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Diffusion, VLA, Planning
- Paper link: ./2024/CVPR/2024_CVPR_Generate-Subgoal-Images-before-Act-Unlocking-the-Chain-of/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Inspired by the great success of diffusion model in image generation tasks, we propose a novel hierarchical framework named as CoTDiffusion that incorporates diffusion model as a high-level ...
- Additionally, we propose bi-directional generation and frame concat mechanism to further enhance the fidelity of generated subgoal images and the accuracy of instruction following.
- The coarse-to-fine semantic alignment training training allows developing spatial reasoning prior to synthesis.

## 원리적 동기
- Moreover, for long-horizon manipulation tasks, the deviation from general instruction tends to accumulate if lack of intermediate guidance from high-level subgoals.
- Inspired by the great success of diffusion model in image generation tasks, we propose a novel hierarchical framework named as CoTDiffusion that incorporates diffusion model as a high-level ...

## 핵심 방법론
- The coarse-to-fine semantic alignment training training allows developing spatial reasoning prior to synthesis.
- Additionally, ablating coarse pretraining and bi-directional generation degrades performance, validating their benefits.
- We attribute this to two potential reasons: First, accurate and grounded subgoal images generated in visual planners provide supplemental visual context, which can partly compensate for the insufficient ...
- With step-wise sub-prompts decomposed in advance, the performance of SuSIE gets largely raised but still underperforms CoTDiffusion, which has no need to explicitly decompose the general prompts and ...
- Rearrange Reasoning Constraints Overall Gato Flamingo VIMA 6.4 ± 1.3 17.5 ± 1.6 43.1 ± 3.3 2.5 ± 0.4 3.0 ± 0.5 38.2 ± 4.4 25.2 ± 3.1 ...
