# Text2Motion: From Natural Language Instructions to Feasible Plans

- Year/Venue: 2023 / ICRA
- Category: Planning and Long-Horizon Reasoning
- Tags: Robotics, LLM planning, task and motion planning, feasibility, skill chaining
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/text-to-motion/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- We evaluate our method on a suite of problems that require long-horizon reasoning, interpretation of abstract goals, and handling of partial affordance perception.
- Our experiments show that Text2Motion can solve these challenging problems with a success rate of 82%, while prior state-of-the-art language-based planning methods only achieve 13%.
- We propose Text2Motion, a language-based planning framework enabling robots to solve sequential manipulation tasks that require long-horizon reasoning.

## Core Idea
- We propose Text2Motion, a language-based planning framework enabling robots to solve sequential manipulation tasks that require long-horizon reasoning.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments show that Text2Motion can solve these challenging problems with a success rate of 82%, while prior state-of-the-art language-based planning methods only achieve 13%.
- We conduct experiments to test four hypotheses: H1 Geometric feasibility planning is a necessary ingredient when using LLMs and robot skills to solve manipulation tasks with geometric dependencies ...
- Qualitative results are made available at sites.google.com/stanford.edu/text2motion.

## Limitation
- Future Work: We outline several avenues for future work based on these observations.
- Text2Motion represents a hybrid planning formalism that optimistically queries an LLM for long-horizon plans and falls back to a reliable search strategy should optimistic planning fail.
- First, there remains an opportunity to increase the plan-time efficiency of our method, for instance, by warm starting geometric feasibility planning with solutions cached in earlier planning iterations ...

## Contribution
- Our experiments show that Text2Motion can solve these challenging problems with a success rate of 82%, while prior state-of-the-art language-based planning methods only achieve 13%.
- We evaluate our method on a suite of problems that require long-horizon reasoning, interpretation of abstract goals, and handling of partial affordance perception.
- We propose Text2Motion, a language-based planning framework enabling robots to solve sequential manipulation tasks that require long-horizon reasoning.

## Abstract Cue
- We propose Text2Motion, a language-based planning framework enabling robots to solve sequential manipulation tasks that require long-horizon reasoning.
