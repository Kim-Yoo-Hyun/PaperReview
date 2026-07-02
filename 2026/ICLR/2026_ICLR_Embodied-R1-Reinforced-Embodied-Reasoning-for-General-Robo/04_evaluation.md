# Evaluation

- Year/Venue: 2026 / ICLR Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Paper link: ./2026/ICLR/2026_ICLR_Embodied-R1-Reinforced-Embodied-Reasoning-for-General-Robo/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Objaverse
- LIBERO
- BridgeData
- Open X-Embodiment

## Metrics
- accuracy
- mAP
- RMSE
- success rate
- collision

## Evaluation Protocol and Results
- It can be seen that Embodied-R1 achieves accurate visual trajectory prediction across various scenarios.
- Here, we provide an analysis of the failure modes for the results in Tab.
- For additional video materials, please see our project website: https://embodied-r1.github.io/ More Visualization of Real World Manipulation Process We showcase the process of EmbodiedR1 performing real-world tasks in Fig.
- To further evaluate its robustness, we visualize the process of Embodied-R1 performing Task 6 under different visual disturbances in Fig.
- F, we provide further experiments, including an analysis of integration with learning-based methods, an ablation study on the benefits of mixed training, and results using RGB-D inputs.
- 6 show that RL-based models consistently outperform their SFT counterparts, highlighting the crucial role of RL in OOD generalization.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
