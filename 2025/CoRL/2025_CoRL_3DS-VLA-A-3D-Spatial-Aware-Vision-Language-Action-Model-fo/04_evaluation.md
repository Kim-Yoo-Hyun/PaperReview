# Evaluation

- Year/Venue: 2025 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, 3D Vision, Robotics
- Paper link: ./2025/CoRL/2025_CoRL_3DS-VLA-A-3D-Spatial-Aware-Vision-Language-Action-Model-fo/paper.pdf
- Code/Project: https://vis-www.cs.umass.edu/3ds-vla/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- RLBench

## Metrics
- accuracy
- mAP
- success rate

## Evaluation Protocol and Results
- 4.1 Training and Inference Following previous settings , we assume that the model should predict an action specified by a target end-effector pose and gripper state in the ...
- The keyframes represent important or bottleneck steps of the gripper during task execution, such as a pre-pick, grasp, or place pose.
- We simultaneously train on demonstrations from the single-arm simulator RLBench and the dual-arm simulator RLBench2 .
- The fine-tuning stage trains on 2,400 demonstrations and runs for 10 epochs, taking approximately 8 hours on an NVIDIA RTX A100 GPU, achieving a 5Hz inference speed (similar ...
- Experiments in simulation and real world demonstrate that 3DS-VLA outperforms previous state-of-the-art policies and showcase its generalizable capabilities across multi-task, multi-embodiment, and diverse environmental settings.

## Baselines
- The fine-tuning stage trains on 2,400 demonstrations and runs for 10 epochs, taking approximately 8 hours on an NVIDIA RTX A100 GPU, achieving a 5Hz inference speed (similar ...
- 4.1 Training and Inference Following previous settings , we assume that the model should predict an action specified by a target end-effector pose and gripper state in the ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
