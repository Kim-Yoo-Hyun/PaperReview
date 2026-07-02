# Method

- Year/Venue: 2023 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: LLM, VLM, Planning, Robotics
- Paper link: ./2023/CoRL/2023_CoRL_VoxPoser-Composable-3D-Value-Maps-for-Robotic-Manipulation/paper.pdf
- Code/Project: https://voxposer.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present a largescale study of the proposed method in both simulated and real-robot environments, showcasing the ability to perform a large variety of everyday manipulation tasks specified ...

## 원리적 동기
- However, to enable physical interactions with the environment, existing approaches typically rely on a repertoire of pre-defined motion primitives (i.e., skills) that may be invoked by an LLM ...
- We look at the problem of grounding abstract language instructions (e.g., “set up the table”) in robot actions .
- We present a largescale study of the proposed method in both simulated and real-robot environments, showcasing the ability to perform a large variety of everyday manipulation tasks specified ...

## 핵심 방법론
- We first provide the formulation of VoxPoser as an optimization problem (Sec.
- Then we describe how VoxPoser can be used as a general zero-shot framework to map language instructions to 3D value maps (Sec.
- We subsequently demonstrate how trajectories can be synthesized in closed-loop for robotic manipulation (Sec.
- While zero-shot in nature, we demonstrate how VoxPoser can learn from online interactions to efficiently solve contact-rich tasks (Sec.
- 3.1 Problem Formulation Consider a manipulation problem given as a free-form language instruction L (e.g., “open the top drawer”).
