# Problem

- Year/Venue: 2026 / RA-L
- Category: Navigation and Embodied AI
- Tags: Robotics, Navigation
- Paper link: ./2026/RA-L/2026_RA-L_LAMP-Implicit-Language-Map-for-Robot-Navigation/paper.pdf
- Code/Project: https://lab-of-ai-and-robotics.github.io/LAMP/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, existing methods that explicitly store language vectors in grid or node-based maps struggle to scale to large environments due to excessive memory requirements and limited resolution for ...
- By combining this implicit representation with a sparse graph, LAMP supports efficient coarse path planning and then performs gradient-based optimization in the learned field to refine poses near ...
- Our experimental results, both in NVIDIA Isaac Sim and on a real multi-floor building, demonstrate that LAMP outperforms existing explicit methods in both memory efficiency and fine-grained goal-reaching ...

## 해결하려는 문제
- Our experimental results, both in NVIDIA Isaac Sim and on a real multi-floor building, demonstrate that LAMP outperforms existing explicit methods in both memory efficiency and fine-grained goal-reaching ...
- We introduce LAMP (Language Map), a novel neural language field-based navigation framework that learns a continuous, language-driven map and directly leverages it for fine-grained path generation.
- Unlike prior approaches, our method encodes language features as an implicit neural field rather than storing them explicitly at every location.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
