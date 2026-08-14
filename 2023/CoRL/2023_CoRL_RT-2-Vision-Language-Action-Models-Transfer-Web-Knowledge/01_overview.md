# RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2023 / CoRL
- Category: VLA and Generalist Robot Policies
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/paper.pdf
- Code/Project: https://robotics-transformer2.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- visual concepts from web scale data and low level robot actions during fine-tuning, instead of just robot actions.
- During co-fine-tuning we balance the ratios of robot and web data in each training batch by increasing the sampling weight on the robot dataset.
- One important distinction between RT-2 and standard VLMs is that RT-2 is required to output valid action tokens for execution on the real robot.

## Core Idea
- We develop a protocol that allows us to run RT-2 models on robots by deploying them in a multi-TPU cloud service and querying this service over the network.
- During co-fine-tuning we balance the ratios of robot and web data in each training batch by increasing the sampling weight on the robot dataset.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- With this solution, we can achieve a suitable frequency of control and also serve multiple robots using the same cloud service.
- Experiments Our experiments focus on real-world generalization and emergent capabilities of RT-2 and aim to answer the following questions: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control ...
- The largest model we evaluated, the 55B parameter RT-2-PaLI-X-55B model, can run at a frequency of 1-3 Hz.

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- We evaluate our approach and several baselines with about 6,000 evaluation trajectories in a varie
- We develop a protocol that allows us to run RT-2 models on robots by deploying them in a multi-TPU cloud service and querying this service over the network.
- During co-fine-tuning we balance the ratios of robot and web data in each training batch by increasing the sampling weight on the robot dataset.

## Abstract Cue
- visual concepts from web scale data and low level robot actions during fine-tuning, instead of just robot actions.
