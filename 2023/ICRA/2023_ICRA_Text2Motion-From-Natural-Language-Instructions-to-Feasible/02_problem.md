# Problem

- Year/Venue: 2023 / ICRA
- Category: Planning and Long-Horizon Reasoning
- Tags: Robotics, LLM planning, task and motion planning, feasibility, skill chaining
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/text-to-motion/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- We evaluate our method on a suite of problems that require long-horizon reasoning, interpretation of abstract goals, and handling of partial affordance perception.
- Our experiments show that Text2Motion can solve these challenging problems with a success rate of 82%, while prior state-of-the-art language-based planning methods only achieve 13%.
- We propose Text2Motion, a language-based planning framework enabling robots to solve sequential manipulation tasks that require long-horizon reasoning.

## 해결하려는 문제
- Our experiments show that Text2Motion can solve these challenging problems with a success rate of 82%, while prior state-of-the-art language-based planning methods only achieve 13%.
- We evaluate our method on a suite of problems that require long-horizon reasoning, interpretation of abstract goals, and handling of partial affordance perception.
- We propose Text2Motion, a language-based planning framework enabling robots to solve sequential manipulation tasks that require long-horizon reasoning.

## 선행 연구 / 배경 단서
- The emergence of Large Language Models (LLMs) as a task-agnostic reasoning module presents a promising pathway to general robot planning capabilities.
- Several recent works [3– 6] capitalize on their ability to perform task planning for robot systems without needing to manually specify symbolic planning domains.
- Nevertheless, these prior approaches adopt myopic or open-loop execution strategies, trusting LLMs to produce correct plans without verifying them on the symbolic or geometric level.
