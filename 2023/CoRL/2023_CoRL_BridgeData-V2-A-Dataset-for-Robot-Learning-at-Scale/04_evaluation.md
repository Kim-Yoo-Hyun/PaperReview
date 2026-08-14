# Evaluation

- Year/Venue: 2023 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Dataset, Imitation Learning, robot manipulation, data scaling, generalization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://rail-berkeley.github.io/bridgedata/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- BridgeData

## Metrics
- success rate

## Evaluation Protocol and Results
- The goal of our experiments is to evaluate the utility of our dataset for testing a variety of multi-task offline learning methods.
- Our experiments are designed to answer the following questions: 1.
- We first evaluated the methods in Section 4 on tasks that are seen in the training data (see Table 2).
- In our experiments, we train 6 state-of-the-art imitation learning and offline reinforcement learning methods on our dataset, and find that they succeed on a suite of tasks requiring ...
- We also demonstrate that the performance of these methods improves with more data and higher capacity models, and that training on a greater variety of skills leads to ...

## Baselines
- Most apparently, RT-1 is significantly better than our LCBC baseline, likely due to a combination of design decisions such as larger images, action discretization, and observation histories.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
