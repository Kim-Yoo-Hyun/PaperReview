# OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_OWMM-Agent-Open-World-Mobile-Manipulation-With-Multi-modal/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- More specifically, we formulate the high-level OWMM task for the internal VLM model as a multi-turn, multi-image, and multi-modal reasoning problem.
- To address the problem of domain adaptation, we further introduce an agentic data synthesis pipeline tailored for OWMM, to generate large-scale and instruction-driven episodes that teach the VLM ...
- Based on the aforementioned observations, we propose a novel VLM agent framework, OWMM-Agent, to address these challenges and leverage the power of VLMs for OWMM task.

## Core Idea
- To address this complexity, we propose a novel multi-modal agent architecture that maintains multi-view scene frames and agent states for decision-making and controls the robot by function calling.
- Additionally, we propose the “dead loop" metric to quantify the number of cyclic stagnations occurring during test episodes.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Through experiments, we demonstrate that our model achieves SOTA performance compared to other foundation models including GPT-4o and strong zero-shot generalization in real world.
- The OWMM-VLM-38B model achieves the best performance across all metrics, demonstrating its superior ability to integrate scene understanding, decision-making, and action generation. *: Since PIVOT and RoboPoint are ...
- Our model excels in decision-making, achieving state-of-the-art results in image retrieval and affordance grounding.

## Limitation
- Future work will focus on addressing limitations like pre-mapping reliance and enhancing cross-embodiment adaptability for more complex manipulation tasks.
- Episodic evaluations in simulated environments further confirmed the OWMM-Agent’s superior success rates and robustness against common failure modes like dead loops, while real-world tests on a Fetch robot ...
- Please also refer to the appendix for discussions about the potential impact of this research in Appendix A and extended discussions on limitations in Appendix B.

## Contribution
- To address this complexity, we propose a novel multi-modal agent architecture that maintains multi-view scene frames and agent states for decision-making and controls the robot by function calling.
- Through experiments, we demonstrate that our model achieves SOTA performance compared to other foundation models including GPT-4o and strong zero-shot generalization in real world.
- A second challenge is the hallucination from domain shift.

## Abstract Cue
- The rapid progress of navigation, manipulation, and vision models has made mobile manipulators capable in many specialized tasks.
