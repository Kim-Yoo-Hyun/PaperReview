# Method

- Year/Venue: 2023 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, data generation, robot manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://mimicgen.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We introduce MimicGen, a system for automatically synthesizing large-scale, rich datasets from only a small number of human demonstrations by adapting them to new contexts.
- We use MimicGen to generate over 50K demonstrations across 18 tasks with diverse scene configurations, object instances, and robot arms from just ∼200 human demonstrations.
- 4.1 Parsing the Source Dataset into Object-Centric Segments Each task consists of a sequence of object-centric subtasks (Assumption 2, Sec.

## 원리적 동기
- However, this success does not come without costly and time-consuming human labor.
- However, the demonstrations can be extremely costly and time-consuming to collect.
- We introduce MimicGen, a system for automatically synthesizing large-scale, rich datasets from only a small number of human demonstrations by adapting them to new contexts.

## 핵심 방법론
- 4.1 Parsing the Source Dataset into Object-Centric Segments Each task consists of a sequence of object-centric subtasks (Assumption 2, Sec.
- 2 (right), this consists of three key steps for each subtask: (1) choosing a reference subtask segment in the source dataset, (2) transforming the subtask segment for the ...
