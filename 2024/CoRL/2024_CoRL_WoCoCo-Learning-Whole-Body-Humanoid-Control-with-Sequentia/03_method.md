# Method

- Year/Venue: 2024 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, sequential contacts, Reinforcement Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://wococo-humanoid.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- To better facilitate exploration, we propose a task-agnostic curiosity reward term.
- In this work, we propose WoCoCo (Whole-Body Control with Sequential Contacts), a unified framework to learn whole-body humanoid control with sequential contacts by naturally decomposing the tasks into ...
- Sferrazza et al. trained policies for multiple dynamic manipulation tasks with a shared hierarchical RL architecture, yet they did not address sim-to-real concerns or propose unified contact-related rewards.

## 원리적 동기
- In WoCoCo, we reformulate the problem as the sequential fulfillment of multiple contact stages (detailed in Section 2), which also breaks down the exploration burden into separate stages.
- This then transforms each challenge to a question: Q1: How to reach desired contact states within each stage?
- To better facilitate exploration, we propose a task-agnostic curiosity reward term.

## 핵심 방법론
- To better facilitate exploration, we propose a task-agnostic curiosity reward term.
- Sferrazza et al. trained policies for multiple dynamic manipulation tasks with a shared hierarchical RL architecture, yet they did not address sim-to-real concerns or propose unified contact-related rewards.
