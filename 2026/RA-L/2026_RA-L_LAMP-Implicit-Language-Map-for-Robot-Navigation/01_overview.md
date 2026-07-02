# LAMP: Implicit Language Map for Robot Navigation

- Year/Venue: 2026 / RA-L
- Category: Navigation and Embodied AI
- Tags: Robotics, Navigation
- Paper link: ./2026/RA-L/2026_RA-L_LAMP-Implicit-Language-Map-for-Robot-Navigation/paper.pdf
- Code/Project: https://lab-of-ai-and-robotics.github.io/LAMP/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, existing methods that explicitly store language vectors in grid or node-based maps struggle to scale to large environments due to excessive memory requirements and limited resolution for ...
- By combining this implicit representation with a sparse graph, LAMP supports efficient coarse path planning and then performs gradient-based optimization in the learned field to refine poses near ...
- Our experimental results, both in NVIDIA Isaac Sim and on a real multi-floor building, demonstrate that LAMP outperforms existing explicit methods in both memory efficiency and fine-grained goal-reaching ...

## Core Idea
- We introduce LAMP (Language Map), a novel neural language field-based navigation framework that learns a continuous, language-driven map and directly leverages it for fine-grained path generation.
- Unlike prior approaches, our method encodes language features as an implicit neural field rather than storing them explicitly at every location.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experimental results, both in NVIDIA Isaac Sim and on a real multi-floor building, demonstrate that LAMP outperforms existing explicit methods in both memory efficiency and fine-grained goal-reaching ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our experimental results, both in NVIDIA Isaac Sim and on a real multi-floor building, demonstrate that LAMP outperforms existing explicit methods in both memory efficiency and fine-grained goal-reaching ...
- We introduce LAMP (Language Map), a novel neural language field-based navigation framework that learns a continuous, language-driven map and directly leverages it for fine-grained path generation.
- Unlike prior approaches, our method encodes language features as an implicit neural field rather than storing them explicitly at every location.

## Abstract Cue
- —Recent advances in vision-language models have made zero-shot navigation feasible, enabling robots to interpret and follow natural language instructions without requiring labeling.
