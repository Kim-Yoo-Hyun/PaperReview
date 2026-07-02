# CLIPort: What and Where Pathways for Robotic Manipulation

- Year/Venue: 2021 / CoRL
- Category: Foundations: Vision-Language-Action and Robotics
- Tags: Robotics, Vision-Language Action, CLIP, manipulation
- Paper link: ./2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/paper.pdf
- Code/Project: https://cliport.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address this problem, we bake in a strong semantic prior while learning policies.
- A natural solution to both these problems is to condition policies with natural language.
- This allows us to formulate tabletop rearrangement as a series of language-conditioned affordance predictions, a predominantly vision-based inference problem, and thus benefit from the strengths of data-driven paradigms ...

## Core Idea
- To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation.
- Specifically, we present CLIP ORT, a language-conditioned imitationlearning agent that combines the broad semantic understanding (what) of CLIP with the spatial precision (where) of Transporter .

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts.
- We perform experiments both in simulation and hardware aimed at answering the following questions: 1) How effective is the language-conditioned two-stream architecture for fine-grained manipulation compared to one-stream ...
- All simulated experiments are based on a Universal Robot UR5e with a suction gripper.

## Limitation
- As such, it cannot handle complex partially-observable scenes, or output continuous control for multi-fingered hands, or predict task-completion (see Appendix I for an extended discussion).
- While CLIP ORT can solve a range of tabletop tasks, extending it to dexterous 6-DOF manipulation that goes beyond the two-step primitive remains a challenge.

## Contribution
- Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts.
- To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation.
- Specifically, we present CLIP ORT, a language-conditioned imitationlearning agent that combines the broad semantic understanding (what) of CLIP with the spatial precision (where) of Transporter .

## Abstract Cue
- : How can we imbue robots with the ability to manipulate objects precisely but also to reason about them in terms of abstract concepts?
