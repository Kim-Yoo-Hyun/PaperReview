# ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models

- Year/Venue: 2026 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Chain-of-Thought, Planning
- Paper link: ./2026/CVPR/2026_CVPR_ACoT-VLA-Action-Chain-of-Thought-for-Vision-Language-Actio/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Sub-tasks Vision-Language-Action models have emerged as essential generalist robot policies for diverse manipulation tasks, conventionally relying on directly translating multimodal inputs into actions via Vision-Language Model embeddings.
- Recent advancements have introduced explicit intermediary reasoning—such as sub-task prediction (language) or goal image synthesis (vision)—to guide action generation.
- However, these intermediate reasoning are often indirect and inherently limited in their capacity to convey the full, granular information required for precise action execution.

## Core Idea
- In this paper, we propose ACoT-VLA, a novel architecture that materializes the ACoT paradigm.
- We introduce Action Chain-of-Thought (ACoT), a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the final policy.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments in real-world and simulation environments demonstrate the superiority of our proposed method.
- Recent advancements seek to improve the mapping from the input space to the action space by introducing the intermediate reasoning step by language generation, leading to more generalized ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this paper, we propose ACoT-VLA, a novel architecture that materializes the ACoT paradigm.
- Extensive experiments in real-world and simulation environments demonstrate the superiority of our proposed method.
- We introduce Action Chain-of-Thought (ACoT), a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the final policy.

## Abstract Cue
- Sub-tasks Vision-Language-Action models have emerged as essential generalist robot policies for diverse manipulation tasks, conventionally relying on directly translating multimodal inputs into actions via Vision-Language Model embeddings.
