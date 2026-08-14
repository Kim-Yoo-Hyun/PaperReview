# DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools

- Year/Venue: 2022 / ICLR
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, deformable object, tool use, differentiable physics, skill abstraction, Planning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://diffskill.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- 2.2 C OLLECTING D EMONSTRATION T RAJECTORIES WITH D IFFERENTIABLE P HYSICS Previous work has shown that differentiable physics solvers can acquire short-horizon skills for deformable object manipulation ...

## Core Idea
- Given an initial state s0 , a goal state sg and the transition dynamics p of a differentiable simulator, we use gradient-based trajectory optimization to solve for an ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Inspired by this work, we first collect demonstration trajectories of using each tool to achieve a short-term goal.
- An overview of our framework is shown in Figure 2.
- 2.2 C OLLECTING D EMONSTRATION T RAJECTORIES WITH D IFFERENTIABLE P HYSICS Previous work has shown that differentiable physics solvers can acquire short-horizon skills for deformable object manipulation ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Given an initial state s0 , a goal state sg and the transition dynamics p of a differentiable simulator, we use gradient-based trajectory optimization to solve for an ...
- 2.2 C OLLECTING D EMONSTRATION T RAJECTORIES WITH D IFFERENTIABLE P HYSICS Previous work has shown that differentiable physics solvers can acquire short-horizon skills for deformable object manipulation ...
- Inspired by this work, we first collect demonstration trajectories of using each tool to achieve a short-term goal.

## Abstract Cue
- primitive skills from this differentiable physics simulator; we then plan on top of these skills to solve long-horizon tasks.
