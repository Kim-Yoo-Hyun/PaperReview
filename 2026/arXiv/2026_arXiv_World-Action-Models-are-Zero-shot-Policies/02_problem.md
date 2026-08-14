# Problem

- Year/Venue: 2026 / arXiv
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, world model, zero-shot policy, action representation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Introduction Recent robotic foundation models, termed Vision-Language Action models (VLAs), extend pretrained VisionLanguage Models (VLMs) to predict motor actions (Bjorck et al., 2025; Black et al., 2024; Brohan ...
- Although VLM priors encode what to do at a semantic level, they lack representations of how actions should be executed with precise spatial awareness, aligned with geometry, dynamics, ...
- However, they fail at a task like “untie the shoelace” if that specific skill was not present in the robot training data.

## 해결하려는 문제
- This results in over 2× improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in realrobot experiments.
- We introduce DreamZero, a World Action Model (WAM) built upon a pretrained video diffusion backbone.
- Finally, we demonstrate two forms of cross-embodiment transfer: video-only demonstrations from other robots or humans yield a relative improvement of over 42% on unseen task performance with just ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
