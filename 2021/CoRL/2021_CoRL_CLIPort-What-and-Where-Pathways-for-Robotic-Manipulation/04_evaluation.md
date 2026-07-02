# Evaluation

- Year/Venue: 2021 / CoRL
- Category: Foundations: Vision-Language-Action and Robotics
- Tags: Robotics, Vision-Language Action, CLIP, manipulation
- Paper link: ./2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/paper.pdf
- Code/Project: https://cliport.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet

## Metrics
- accuracy
- mAP

## Evaluation Protocol and Results
- We perform experiments both in simulation and hardware aimed at answering the following questions: 1) How effective is the language-conditioned two-stream architecture for fine-grained manipulation compared to one-stream ...
- All simulated experiments are based on a Universal Robot UR5e with a suction gripper.
- The language instructions are constructed from templates for simulated experiments, and human-annotated for real-world experiments.
- We extend the Ravens benchmark set in PyBullet with 10 language-conditioned manipulation tasks.
- Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts.
- We perform experiments both in simulation and hardware aimed at answering the following questions: 1) How effective is the language-conditioned two-stream architecture for fine-grained manipulation compared to one-stream ...

## Baselines
- We perform experiments both in simulation and hardware aimed at answering the following questions: 1) How effective is the language-conditioned two-stream architecture for fine-grained manipulation compared to one-stream ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
