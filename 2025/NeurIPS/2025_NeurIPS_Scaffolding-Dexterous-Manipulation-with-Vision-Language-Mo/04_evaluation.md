# Evaluation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Scaffolding-Dexterous-Manipulation-with-Vision-Language-Mo/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ManiSkill

## Metrics
- accuracy
- success rate

## Evaluation Protocol and Results
- Thus, we mainly focus our experiments on comparison with a variety of oracles and ablations: • Iterative Keypoint Rewards (IKER): We implement Iterative Keypoint Rewards , in which ...
- We run 20 trials for each configuration for a total of 2000 evaluation episodes and average results across three seeds.
- We conduct a comprehensive suite of experiments to assess the effectiveness, generality, and robustness of our method across a diverse range of dexterous manipulation tasks.
- 2) How much can iterative refinement improve performance?
- Thus, we mainly focus our experiments on comparison with a variety of oracles and ablations: • Iterative Keypoint Rewards (IKER): We implement Iterative Keypoint Rewards , in which ...
- We run 20 trials for each configuration for a total of 2000 evaluation episodes and average results across three seeds.

## Baselines
- Methods Given the novelty of our problem setting, there are few applicable baselines which are also language-conditioned, Semantic Understanding demonstration-free, and do not require ground-truth state estiMove Apple ...
- Articulated Object Manipulation • Pre-recorded Trajectories: This method reuses pre-recorded Open Drawer Open Fridge trajectories from the training set at test-time, eliminating adaptability to new scenarios. • Oracle ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
