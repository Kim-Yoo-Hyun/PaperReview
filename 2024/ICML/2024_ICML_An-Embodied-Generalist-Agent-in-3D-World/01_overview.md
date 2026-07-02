# An Embodied Generalist Agent in 3D World

- Year/Venue: 2024 / ICML
- Category: 3D Large Multimodal Models
- Tags: LLM, 3D Vision, Planning, Robotics
- Paper link: ./2024/ICML/2024_ICML_An-Embodied-Generalist-Agent-in-3D-World/paper.pdf
- Code/Project: https://embodied-generalist.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Nonetheless, existing generalist models primarily thrive within 2D domains, lacking comprehension of the 3D physical environment that envelops human-level intelligence.
- We argue these limitations significantly hinder current models from performing real-world tasks and approaching general intelligence.
- However, several significant challenges remain: (i) most of these models rely on 2D images yet exhibit a limited capacity for 3D input; (ii) these models rarely explore the ...

## Core Idea
- To this end, we introduce LEO, an embodied multimodal generalist agent that excels in perceiving, grounding, reasoning, planning, and acting in the 3D world.
- The keys to the success of this paradigm lie in large-scale internet-level datasets from numerous tasks and domains, as well as scalable Transformer architectures (Vaswani et al., 2017) ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Leveraging massive knowledge from large language models (LLMs), recent machine learning models show notable successes in generalpurpose task solving in diverse domains such as computer vision and robotics.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- The keys to the success of this paradigm lie in large-scale internet-level datasets from numerous tasks and domains, as well as scalable Transformer architectures (Vaswani et al., 2017) ...
- To this end, we introduce LEO, an embodied multimodal generalist agent that excels in perceiving, grounding, reasoning, planning, and acting in the 3D world.
- LEO is trained with a unified task interface, model architecture, and objective in two stages: (i) 3D vision-language (VL) alignment and (ii) 3D vision-language-action (VLA) instruction tuning.

## Abstract Cue
- Introduction Building one generalist model that can handle comprehensive tasks like humans has been a long-existing pursuit in artificial intelligence and neuroscience (Lake et al., 2015; 2017; Zhu et al., 2020; Mountcastle, 1979; Schmidhuber, 2018; Huang et al., 2022a).
