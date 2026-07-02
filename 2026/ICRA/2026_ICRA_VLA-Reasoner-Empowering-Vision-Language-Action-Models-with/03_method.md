# Method

- Year/Venue: 2026 / ICRA
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Reinforcement Learning
- Paper link: ./2026/ICRA/2026_ICRA_VLA-Reasoner-Empowering-Vision-Language-Action-Models-with/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this problem, we propose a plug-in framework named VLA-Reasoner that effectively empowers off-the-shelf VLAs with the capability of foreseeing future states via test-time scaling.
- This raises a core question: “Can VLAs explore the longhorizon future influence of actions at test time, and decide the optimal action?” To this end, we propose a ...
- Meanwhile, we introduce a confidence sampling mechanism based on Kernel Density Estimation (KDE), to enable efficient exploration in MCTS without redundant VLA queries.

## 원리적 동기
- To address this problem, we propose a plug-in framework named VLA-Reasoner that effectively empowers off-the-shelf VLAs with the capability of foreseeing future states via test-time scaling.
- However, existing VLAs are limited to predicting short-sighted next-action, which struggle with long-horizon trajectory tasks due to incremental deviations.
- To address this problem, we propose a plug-in framework named VLA-Reasoner that effectively empowers off-the-shelf VLAs with the capability of foreseeing future states via test-time scaling.

## 핵심 방법론
- We design and test 5 real-world tasks via deploying our method on two cutting-edge VLAs: an open-sourced popular model OpenVLA-7B , and an advanced commercial model π0 − ...
- The training phases use the same datasets, and we collect 10 failure cases for each task to supplement the training of the world model.
