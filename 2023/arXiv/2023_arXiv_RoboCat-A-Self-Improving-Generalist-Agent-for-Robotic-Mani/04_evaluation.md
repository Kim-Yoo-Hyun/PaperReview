# Evaluation

- Year/Venue: 2023 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, generalist policy, cross-embodiment, self-improvement, robot manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://deepmind.google/discover/blog/robocat-a-self-improving-robotic-agent/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet

## Metrics
- accuracy
- success rate

## Evaluation Protocol and Results
- The evaluations and comparisons we present in this section investigate the following questions: 1.
- Can RoboCat learn from heterogeneous data and solve a large set of tasks, specified with visual goals and requiring dexterity on multiple physical and simulated embodiments? (Section 5.1)
- We also show how a trained model itself can be used to generate data for subsequent training iterations, thus providing a basic building block for an autonomous improvement ...
- With RoboCat, we demonstrate the ability to generalise to new tasks and robots, both zero-shot as well as through adaptation using only 100–1000 examples for the target task.

## Baselines
- The evaluations and comparisons we present in this section investigate the following questions: 1.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
