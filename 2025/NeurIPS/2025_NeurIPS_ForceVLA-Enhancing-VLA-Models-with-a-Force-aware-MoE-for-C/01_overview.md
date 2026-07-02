# ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Robotics
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ForceVLA-Enhancing-VLA-Models-with-a-Force-aware-MoE-for-C/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address these limitations, we introduce ForceVLA, a novel framework that augments VLA models with a force-aware Mixture-of-Experts (MoE) module, enabling effective reasoning and context-sensitive, force-informed action generation ...
- Existing VLA models rely heavily on visual and linguistic cues, often overlooking force sensing, a modality critical for precise physical interaction.
- Current methods lack mechanisms to perceive and adapt to these dynamic variations, limiting their ability to reason over time about physical interactions.

## Core Idea
- Key to our approach is a force-aware Mixture-of-Experts-based fusion module, which enables dynamic processing and deep integration of force, visual, and language features during action generation, significantly enhancing ...
- To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Incorporating external force feedback improves performance for π0 -base model, while our method achieves the highest average success rate, demonstrating robust performance under complex interaction dynamics. “Wipe Board-1” ...
- As demonstrated in FigTable 1: Performance of cucumber peeling. ure 5, ForceVLA achieves an average success rate of 60.5% across all five tasks, significantly outAvg.
- 5.1 Experimental Setups To evaluate the effectiveness of ForceVLA, we conducted experiments on five diverse contact-rich manipulation tasks: Bottle Pumping, Plug Insertion, USB Drive Insertion, Whiteboard Wiping, and ...

## Limitation
- Each sequence illustrates how ForceVLA adapts its actions in response to contact dynamics, retrying or adjusting pose when failures occur, ultimately achieving successful task completion. challenging tasks show ...
- We recognize that large-scale training with simulated data represents a promising avenue for expanding the range of tasks our model can address and view this as an important ...

## Contribution
- To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems.
- Our approach highlights the importance of multimodal integration for dexterous manipulation and sets a new benchmark for physically intelligent robotic control.
- ForceVLA improves average task success by 23.2% over strong π0 -based baselines, achieving up to 80% success in tasks such as plug insertion.

## Abstract Cue
- Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations.
