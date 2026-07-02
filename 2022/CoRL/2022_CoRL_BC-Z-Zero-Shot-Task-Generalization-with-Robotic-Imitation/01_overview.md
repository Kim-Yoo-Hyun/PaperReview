# BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning

- Year/Venue: 2022 / CoRL
- Category: Foundations: Vision-Language-Action and Robotics
- Tags: Robotics, Imitation Learning, Vision-Language Action
- Paper link: ./2022/CoRL/2022_CoRL_BC-Z-Zero-Shot-Task-Generalization-with-Robotic-Imitation/paper.pdf
- Code/Project: https://sites.google.com/view/bc-z/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In this paper, we study the problem of enabling a robot to generalize zero-shot or few-shot to new vision-based manipulation tasks.
- We study this problem using the framework of imitation learning.
- The key challenge in this endeavour is generalization: the robot must handle new environments, recognize and manipulate objects it has not seen before, and understand the intent of ...

## Core Idea
- To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on different forms of ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments aim to evaluate BC-Z in large-scale imitation learning settings.
- Then, our experiments will aim to answer the following questions: (1) Can BC-Z enable zero-shot and few-shot generalization to new tasks from a command in the form of ...
- We present experiments aimed at these questions in this section.

## Limitation
- Our system does have a number of limitations.
- This suggests that an exciting direction for future work is to use our policies as a general-purpose initialization for finetuning of downstream tasks, where additional training, perhaps with ...
- A direction to address this limitation is to relabel the dataset with a variety of human-provided annotations , which could enable the system to handle more variability in ...

## Contribution
- To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on different forms of ...
- : In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning.
- We approach the challenge from an imitation learning perspective, aiming to study how scaling and broadening the data collected can facilitate such generalization.

## Abstract Cue
- : In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning.
