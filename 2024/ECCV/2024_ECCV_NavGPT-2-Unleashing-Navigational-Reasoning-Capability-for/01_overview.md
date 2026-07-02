# NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models

- Year/Venue: 2024 / ECCV
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Navigation
- Paper link: ./2024/ECCV/2024_ECCV_NavGPT-2-Unleashing-Navigational-Reasoning-Capability-for/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Motivating by the considerable advances in Large Language Models (LLMs), there is an emerging effort to utilize these models for instructional tasks within robotic navigation .
- This development highlights two core capacities of LLMs: Firstly, the ability to generalize commonsense knowledge reasoning and efficiently process free-form linguistic inputs, thanks to learning enormous amounts of ...
- Secondly, the interpretative of LLMs to provide navigational reasoning explicitly in a human interpretable way and the associated communicative potential during interaction with humans.

## Core Idea
- The architecture of NavGPT-2, as depicted in Figure 2, comprises two primary components: a Large Vision-Language Model (VLM) and a navigation policy network.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We demonstrate the data efficiency of the proposed methods and eliminate the gap between LM-based agents and state-of-the-art VLN specialists.
- All experiments are conducted on a single NVIDIA A100 GPU.
- We adopt a comprehensive set of navigation metrics to evaluate performance , including Trajectory Length (TL), which measures the average path length in meters; Navigation Error (NE), the ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We demonstrate the data efficiency of the proposed methods and eliminate the gap between LM-based agents and state-of-the-art VLN specialists.

## Abstract Cue
- Capitalizing on the remarkable advancements in Large Language Models (LLMs), there is a burgeoning initiative to harness LLMs for instruction following robotic navigation.
