# Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation

- Year/Venue: 2025 / ICCV
- Category: Navigation and Embodied AI
- Tags: Navigation, grounding, exploration
- Paper link: ./2025/ICCV/2025_ICCV_Move-to-Understand-a-3D-Scene-Bridging-Visual-Grounding-an/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing 3D Vision-Language (3D-VL) models primarily focus on grounding objects in static observations from 3D reconstruction, such as meshes and point clouds, but lack the ability to actively ...
- To address this limitation, we introduce Move to Understand (MTU3D), a unified framework that integrates active perception with 3D vision-language learning, enabling embodied agents to effectively explore and ...

## Core Idea
- Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We propose a unified ...
- MTU3D In this section, we present the architecture of our model in Fig.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive evaluations across various embodied navigation and question-answering benchmarks show that MTU3D outperforms state-of-the-art reinforcement learning and modular navigation approaches by 14%, 23%, 9%, and 2% in success ...
- This is achieved by three key innovations: 1) Online query-based representation learning, enabling direct spatial memory construction from RGB-D frames, eliminating the need for explicit 3D reconstruction.
- The deployment on a real robot demonstrates MTU3D’s effectiveness in handling real-world data.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive evaluations across various embodied navigation and question-answering benchmarks show that MTU3D outperforms state-of-the-art reinforcement learning and modular navigation approaches by 14%, 23%, 9%, and 2% in success ...
- To address this limitation, we introduce Move to Understand (MTU3D), a unified framework that integrates active perception with 3D vision-language learning, enabling embodied agents to effectively explore and ...
- 3) End-to-end trajectory learning that combines Vision-Language-Exploration pre-training over a million diverse trajectories collected from both simulated and realworld RGB-D sequences.

## Abstract Cue
- ploring, which represents unexplored locations as frontier queries and jointly optimizes object grounding and frontier selection.
