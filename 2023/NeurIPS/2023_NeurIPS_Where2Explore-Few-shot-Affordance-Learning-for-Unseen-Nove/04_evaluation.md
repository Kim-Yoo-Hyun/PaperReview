# Evaluation

- Year/Venue: 2023 / NeurIPS
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, 3D Vision, active exploration, affordance, articulated objects, few-shot learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/where2explore/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- F-score
- success rate

## Evaluation Protocol and Results
- We conduct experiments under two different manipulation action types (pushing and pulling).
- For the training stage, to filter out randomness and prove the universal effectiveness of our framework, we conduct experiments using 4 different training category combinations, which are {cabinet, ...
- To demonstrate the ability of our framework to propose informative interactions for cross-category exploration efficiently.
- Finally, we test our fine-tuned model on unseen instances in novel categories to demonstrate that our model learns the general semantic and geometric information.
- Extensive experiments in simulated and real-world environments demonstrate our framework’s capacity for efficient few-shot exploration and generalization.
- We conduct experiments under two different manipulation action types (pushing and pulling).

## Baselines
- We set up three baselines for comparisons.
- For baselines, we train the models using all training objects in training categories, whereas we divide the training categories into two parts to train our framework, as mentioned ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
