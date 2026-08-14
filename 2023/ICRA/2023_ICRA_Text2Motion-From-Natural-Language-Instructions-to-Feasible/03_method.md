# Method

- Year/Venue: 2023 / ICRA
- Category: Planning and Long-Horizon Reasoning
- Tags: Robotics, LLM planning, task and motion planning, feasibility, skill chaining
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/text-to-motion/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We propose Text2Motion, a language-based planning framework enabling robots to solve sequential manipulation tasks that require long-horizon reasoning.

## 원리적 동기
- We evaluate our method on a suite of problems that require long-horizon reasoning, interpretation of abstract goals, and handling of partial affordance perception.
- Our experiments show that Text2Motion can solve these challenging problems with a success rate of 82%, while prior state-of-the-art language-based planning methods only achieve 13%.
- We propose Text2Motion, a language-based planning framework enabling robots to solve sequential manipulation tasks that require long-horizon reasoning.

## 핵심 방법론
- The core idea of this paper is to ensure the geometric feasibility of an LLM task plan—and thereby its correctness—by predicting the success probability (Eq.
- 3) of learned skills that are sequenced according to the task plan.
- In the following sections, we outline two strategies for planning with LLMs and learned skills: a shooting-based planner and a search-based planner.
- We then introduce the full planning algorithm, Text2Motion, which synergistically integrates the strengths of both strategies.
- These strategies represent different ways of maximizing the overall planning objective in Eq.
