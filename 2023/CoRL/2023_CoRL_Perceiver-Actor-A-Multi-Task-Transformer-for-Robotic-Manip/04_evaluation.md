# Evaluation

- Year/Venue: 2023 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Imitation Learning, 3D manipulation
- Paper link: ./2023/CoRL/2023_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/paper.pdf
- Code/Project: https://peract.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- RLBench

## Metrics
- mAP
- success rate
- collision

## Evaluation Protocol and Results
- C2FARM-BC is a 3D fully-convolutional network by James et al. that has achieved state-of-the-art results on RLBench tasks.
- In contrast, P ER ACT’s voxel-based formulation naturally allows for integrating multi-view observations, learning 6-DoF action representations, and data-augmentation in 3D, all of which are non-trivial to achieve ...
- 4.1 Simulation Setup We conduct our primary experiments in simulation for the sake of reproducibility and benchmarking.
- We perform experiments to answer the following questions: (1) How effective is P ER ACT compared to unstructured image-to-action frameworks and standard architectures like 3D ConvNets?
- C2FARM-BC is a 3D fully-convolutional network by James et al. that has achieved state-of-the-art results on RLBench tasks.
- Our results show that P ER ACT significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.

## Baselines
- We study the effectiveness of our problem formulation by benchmarking against two language-conditioned baselines: Image-BC and C2FARM-BC.
- We perform experiments to answer the following questions: (1) How effective is P ER ACT compared to unstructured image-to-action frameworks and standard architectures like 3D ConvNets?

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
