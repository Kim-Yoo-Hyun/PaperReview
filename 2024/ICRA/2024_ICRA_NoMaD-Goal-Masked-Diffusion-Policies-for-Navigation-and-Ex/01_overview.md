# NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration

- Year/Venue: 2024 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Navigation, diffusion policy, exploration
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://general-navigation-models.github.io/nomad/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- In this work, we study a particularly important instance of this problem in the domain of robotic navigation, where the user might specify a destination visually (i.e., via ...
- We show that this unified policy results in better overall performance when navigating to visually indicated goals in novel environments, as compared to approaches that use subgoal proposals ...

## Core Idea
- We instantiate our method by using a large-scale Transformerbased policy trained on data from multiple ground robots, with a diffusion model decoder to flexibly handle both goalconditioned and ...
- Random Subgoals: A variation of the above ViNT system which replaces subgoal diffusion with randomly sampling the training data for a candidate subgoal, which is passed to the ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments, conducted on a real-world mobile robot platform, show effective navigation in unseen environments in comparison with five alternative methods, and demonstrate significant improvements in performance and ...
- We show that this unified policy results in better overall performance when navigating to visually indicated goals in novel environments, as compared to approaches that use subgoal proposals ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We instantiate our method by using a large-scale Transformerbased policy trained on data from multiple ground robots, with a diffusion model decoder to flexibly handle both goalconditioned and ...
- Our experiments, conducted on a real-world mobile robot platform, show effective navigation in unseen environments in comparison with five alternative methods, and demonstrate significant improvements in performance and ...
- We show that this unified policy results in better overall performance when navigating to visually indicated goals in novel environments, as compared to approaches that use subgoal proposals ...

## Abstract Cue
- — Robotic learning for navigation in unfamiliar environments needs to provide policies for both task-oriented navigation (i.e., reaching a goal that the robot has located), and task-agnostic exploration (i.e., searching for a goal in a novel setting).
