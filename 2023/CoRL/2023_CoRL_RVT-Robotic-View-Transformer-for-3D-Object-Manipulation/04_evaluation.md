# Evaluation

- Year/Venue: 2023 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D manipulation, Transformer
- Paper link: ./2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/paper.pdf
- Code/Project: https://robotic-view-transformer.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- RLBench

## Metrics
- accuracy
- success rate
- collision

## Evaluation Protocol and Results
- To achieve the target gripper pose, we generate joint space actions by using the same sampling-based motion planner as in .
- We compare with two variants with CNN and ViT vision encoders respectively. (2) C2F-ARM-BC is a behavior cloning agent that converts the RGB-D images into multi-resolution voxels and ...
- 4.1 Simulation Experiments Simulation Setup.
- To achieve the target gripper pose, we generate joint space actions by using the same sampling-based motion planner as in .
- It also trains 36X faster than PerAct for achieving the same performance and achieves 2.3X the inference speed of PerAct.

## Baselines
- We compare against the following three baselines: (1) Image-BC is an image-toaction behavior cloning agent that predicts action based on the image observations from the sensor camera views.
- We compare with two variants with CNN and ViT vision encoders respectively. (2) C2F-ARM-BC is a behavior cloning agent that converts the RGB-D images into multi-resolution voxels and ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
