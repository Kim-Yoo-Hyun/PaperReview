# Holodeck: Language Guided Generation of 3D Embodied AI Environments

- Year/Venue: 2024 / CVPR
- Category: Navigation and Embodied AI
- Tags: Generation, 3D scene, Embodied AI
- Paper link: ./2024/CVPR/2024_CVPR_Holodeck-Language-Guided-Generation-of-3D-Embodied-AI-Envi/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address the challenge of positioning objects correctly, we prompt GPT-4 to generate spatial relational constraints between objects and then optimize the layout to satisfy those constraints.
- To mitigate this limitation, we present H OLODECK, a system that generates 3D environments to match a user-supplied prompt fully automatedly.
- To move beyond these limitations, recent works adapt 2D foundational models to generate 3D scenes from text .

## Core Idea
- We present humans with four shuffled top-down images from each layout strategy and ask them to rank the four layouts considering out-of-boundary, object collision, reachable space, and layout ...
- To mitigate this limitation, we present H OLODECK, a system that generates 3D environments to match a user-supplied prompt fully automatedly.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We also demonstrate an exciting application of H OLODECK in Embodied AI, training agents to navigate in novel scenes like music rooms and daycares without human-constructed data, which ...
- Our large-scale human evaluation shows that annotators prefer H OLODECK over manually designed procedural baselines in residential scenes and that H OLODECK can produce high-quality outputs for diverse ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To mitigate this limitation, we present H OLODECK, a system that generates 3D environments to match a user-supplied prompt fully automatedly.
- We also demonstrate an exciting application of H OLODECK in Embodied AI, training agents to navigate in novel scenes like music rooms and daycares without human-constructed data, which ...
- Introduction The predominant approach in training embodied agents involves learning in simulators .

## Abstract Cue
- 3D simulated environments play a critical role in Embodied AI, but their creation requires expertise and extensive manual effort, restricting their diversity and scope.
