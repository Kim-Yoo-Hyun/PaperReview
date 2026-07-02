# Problem

- Year/Venue: 2023 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: LLM, VLM, Planning, Robotics
- Paper link: ./2023/CoRL/2023_CoRL_VoxPoser-Composable-3D-Value-Maps-for-Robotic-Manipulation/paper.pdf
- Code/Project: https://voxposer.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, to enable physical interactions with the environment, existing approaches typically rely on a repertoire of pre-defined motion primitives (i.e., skills) that may be invoked by an LLM ...
- We look at the problem of grounding abstract language instructions (e.g., “set up the table”) in robot actions .
- In addressing this challenge, we first note that it is impractical for LLMs to directly output control actions in text, which are typically driven by high-frequency control signals ...

## 해결하려는 문제
- We present a largescale study of the proposed method in both simulated and real-robot environments, showcasing the ability to perform a large variety of everyday manipulation tasks specified ...
- We achieve this by first observing that LLMs excel at inferring affordances and constraints given a free-form language instruction.
- We further demonstrate how the proposed framework can benefit from online experiences by efficiently learning a dynamics model for scenes that involve contact-rich interactions.

## 선행 연구 / 배경 단서
- However, to enable physical interactions with the environment, existing approaches typically rely on a repertoire of pre-defined motion primitives (i.e., skills) that may be invoked by an LLM ...
- We look at the problem of grounding abstract language instructions (e.g., “set up the table”) in robot actions .
- In addressing this challenge, we first note that it is impractical for LLMs to directly output control actions in text, which are typically driven by high-frequency control signals ...
