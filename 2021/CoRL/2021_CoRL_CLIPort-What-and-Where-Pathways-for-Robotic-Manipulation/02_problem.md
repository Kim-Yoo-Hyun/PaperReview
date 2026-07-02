# Problem

- Year/Venue: 2021 / CoRL
- Category: Foundations: Vision-Language-Action and Robotics
- Tags: Robotics, Vision-Language Action, CLIP, manipulation
- Paper link: ./2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/paper.pdf
- Code/Project: https://cliport.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To address this problem, we bake in a strong semantic prior while learning policies.
- A natural solution to both these problems is to condition policies with natural language.
- This allows us to formulate tabletop rearrangement as a series of language-conditioned affordance predictions, a predominantly vision-based inference problem, and thus benefit from the strengths of data-driven paradigms ...

## 해결하려는 문제
- Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts.
- To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation.
- Specifically, we present CLIP ORT, a language-conditioned imitationlearning agent that combines the broad semantic understanding (what) of CLIP with the spatial precision (where) of Transporter .

## 선행 연구 / 배경 단서
- To address this problem, we bake in a strong semantic prior while learning policies.
- A natural solution to both these problems is to condition policies with natural language.
- This allows us to formulate tabletop rearrangement as a series of language-conditioned affordance predictions, a predominantly vision-based inference problem, and thus benefit from the strengths of data-driven paradigms ...
