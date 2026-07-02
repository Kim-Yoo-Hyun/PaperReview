# SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration

- Year/Venue: 2025 / NeurIPS Poster
- Category: Navigation and Embodied AI
- Tags: Robotics, Navigation, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_SimWorld-Robotics-Synthesizing-Photorealistic-and-Dynamic/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, to address the critical challenges faced by real-world robotics in urban environments, they lack the necessary realism, customizability, scalability, and versatility.
- Compared to indoor scenarios, robotics in outdoor environments, in particular, large urban environments, introduces additional challenges, such as (1) 3D perception, spatial reasoning and grounding in large environments; ...
- Unlike existing benchmarks, these two new benchmarks comprehensively evaluate a wide range of critical robot capacities in realistic scenarios, including (1) multimodal instructions grounding, (2) 3D spatial reasoning ...

## Core Idea
- In this work, we present SimWorldRobotics (SWR), a simulation platform for embodied AI in large-scale, photorealistic urban environments.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- After ﬁne-tuning, QwenVL2.5-7B shows substantial improvements across all metrics and is the only model to achieve a non-zero full task success rate.
- In our experiment, the reasoning models show improved depth estimation and destination alignment, which further demonstrates the importance of visual and spatial reasoning in our benchmark.
- As shown in Table 2, among zero-shot ReAct models, Gemini 2.5 Flash achieves the highest progress score.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our experimental results demonstrate that stateof-the-art models, including vision-language models (VLMs), struggle with our tasks, lacking robust perception, reasoning, and planning abilities necessary for urban environments.
- Unlike existing benchmarks, these two new benchmarks comprehensively evaluate a wide range of critical robot capacities in realistic scenarios, including (1) multimodal instructions grounding, (2) 3D spatial reasoning ...
- In this work, we present SimWorldRobotics (SWR), a simulation platform for embodied AI in large-scale, photorealistic urban environments.

## Abstract Cue
- Recent advances in foundation models have shown promising results in developing generalist robotics that can perform diverse tasks in open-ended scenarios given multimodal inputs.
