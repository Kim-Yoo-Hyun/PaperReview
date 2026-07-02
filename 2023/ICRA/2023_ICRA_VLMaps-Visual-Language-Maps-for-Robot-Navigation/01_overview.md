# VLMaps: Visual-Language Maps for Robot Navigation

- Year/Venue: 2023 / ICRA
- Category: Navigation and Embodied AI
- Tags: Vision-Language Navigation, semantic map, Robotics
- Paper link: ./2023/ICRA/2023_ICRA_VLMaps-Visual-Language-Maps-for-Robot-Navigation/paper.pdf
- Code/Project: https://vlmaps.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address this problem, we propose VLMaps, a spatial map representation that directly fuses pretrained visual-language features with a 3D reconstruction of the physical world.
- Specifically, when combined with large language models (LLMs), VLMaps can be used to (i) translate natural language commands into a sequence of open-vocabulary navigation goals (which, beyond prior ...
- While this is useful for matching images to natural language descriptions of object goals, it remains disjoint from the process of mapping the environment, so that it lacks ...

## Core Idea
- To address this problem, we propose VLMaps, a spatial map representation that directly fuses pretrained visual-language features with a 3D reconstruction of the physical world.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments carried out in simulated and real-world environments show that VLMaps enable navigation according to more complex language instructions than existing methods.
- Meanwhile, recent works show that visual-language models (VLMs) , pretrained on Internet-scale data (e.g., image captions) can be used out-of-the-box to ground language to the visual observations of ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address this problem, we propose VLMaps, a spatial map representation that directly fuses pretrained visual-language features with a 3D reconstruction of the physical world.
- Extensive experiments carried out in simulated and real-world environments show that VLMaps enable navigation according to more complex language instructions than existing methods.
- Meanwhile, recent works show that visual-language models (VLMs) , pretrained on Internet-scale data (e.g., image captions) can be used out-of-the-box to ground language to the visual observations of ...

## Abstract Cue
- — Grounding language to the visual observations of a navigating agent can be performed using off-the-shelf visuallanguage models pretrained on Internet-scale data (e.g., image captions).
