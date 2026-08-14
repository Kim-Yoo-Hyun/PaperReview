# Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, mobile manipulation, bimanual manipulation, teleoperation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://mobile-aloha.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Using data collected with Mobile ALOHA, we then perform supervised behavior cloning and find that co-training with existing static ALOHA datasets boosts performance on mobile manipulation tasks.
- We first present Mobile ALOHA, a low-cost and whole-body teleoperation system for data collection.

## Core Idea
- In this work, we develop a system for imitating mobile manipulation tasks that are bimanual and require whole-body control.
- Using data collected with Mobile ALOHA, we then perform supervised behavior cloning and find that co-training with existing static ALOHA datasets boosts performance on mobile manipulation tasks.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- To further improve the imitation learning performance, we are inspired by the recent success of pre-training and co-training on diverse robot datasets, while noticing that there are few ...
- This observation is also consistent across different class of state-of-the-art imitation learning methods, including ACT and Diffusion
- However, most results focus on table-top manipulation, lacking the mobility and dexterity necessary for generally useful tasks.

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- To further improve the imitation learning performance, we are inspired by the recent success of pre-training and co-training on diverse robot datasets, while noticing that there are few ...
- This observation is also consistent across different class of state-of-the-art imitation learning methods, including ACT and Diffusion
- Using data collected with Mobile ALOHA, we then perform supervised behavior cloning and find that co-training with existing static ALOHA datasets boosts performance on mobile manipulation tasks.

## Abstract Cue
- Imitation learning from human demonstrations has shown impressive performance in robotics.
