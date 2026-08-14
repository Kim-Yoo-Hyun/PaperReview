# Method

- Year/Venue: 2026 / arXiv
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, world model, zero-shot policy, action representation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We introduce DreamZero, a World Action Model (WAM) built upon a pretrained video diffusion backbone.
- We explore few-shot embodiment adaptation by post-training on 30 minutes of new embodiment play data and evaluating on pick-and-place variants requiring strong language following.
- However, they fail at a task like “untie the shoelace” if that specific skill was not present in the robot training data.

## 원리적 동기
- Introduction Recent robotic foundation models, termed Vision-Language Action models (VLAs), extend pretrained VisionLanguage Models (VLMs) to predict motor actions (Bjorck et al., 2025; Black et al., 2024; Brohan ...
- Although VLM priors encode what to do at a semantic level, they lack representations of how actions should be executed with precise spatial awareness, aligned with geometry, dynamics, ...
- We introduce DreamZero, a World Action Model (WAM) built upon a pretrained video diffusion backbone.

## 핵심 방법론
- We explore few-shot embodiment adaptation by post-training on 30 minutes of new embodiment play data and evaluating on pick-and-place variants requiring strong language following.
