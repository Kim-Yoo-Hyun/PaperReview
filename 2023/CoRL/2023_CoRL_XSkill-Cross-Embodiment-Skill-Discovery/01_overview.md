# XSkill: Cross Embodiment Skill Discovery

- Year/Venue: 2023 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, cross-embodiment, skill discovery, human video, Imitation Learning, Diffusion
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://xskill.cs.columbia.edu/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Meanwhile, our approach differs from existing work on single-embodiment skill discovery , which solely relies on on-robot demonstration data.
- By learning cross-embodiment skill prototypes, our framework can use direct human demonstration, which is more cost-effective and scalable, even for non-expert demonstrators.
- With the proposed skill alignment transformer, the algorithm can robustly align skills in the human video to the robot visual observation, despite the embodiment difference and unexpected execution ...

## Core Idea
- The XSkill framework consists of three phases: Discover §3.1, Transfer §3.2, and Compose §3.3 that uses three different data sources.
- To ensure that the skill representation focuses on underlying skills rather than embodiment and is aligned across embodiments, XSkill employs a combination of data sampling and entropy regularization ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments in simulation and real-world environments show that the discovered skill prototypes facilitate both skill transfer and composition for unseen tasks, resulting in a more general and ...
- The benchmark, code, and qualitative results are on project website.
- During the inference, the robot must complete an unseen composition of subtasks after viewing a prompt video from the sphere agent demonstration. • Realworld Kitchen: is a new ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our experiments in simulation and real-world environments show that the discovered skill prototypes facilitate both skill transfer and composition for unseen tasks, resulting in a more general and ...
- The benchmark, code, and qualitative results are on project website.
- To bridge this embodiment gap, this paper introduces XSkill, an imitation learning framework that 1) discovers a cross-embodiment representation called skill prototypes purely from unlabeled human and robot ...

## Abstract Cue
- : Human demonstration videos are a widely available data source for robot learning and an intuitive user interface for expressing desired behavior.
