# LERF: Language Embedded Radiance Fields

- Year/Venue: 2023 / ICCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: NeRF, Vision-Language, grounding
- Paper link: ./2023/ICCV/2023_ICCV_LERF-Language-Embedded-Radiance-Fields/paper.pdf
- Code/Project: https://www.lerf.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- queries like “Electricity”, visual properties like “Yellow”, long-tail objects such as “Waldo”, and even reading text like “Boops” on the mug.
- For each prompt, an RGB image and relevancy map are rendered focusing on the location with maximum relevancy activation.
- Abstract ended language queries in 3D.

## Core Idea
- In this work we propose Language Embedded Radiance Fields (LERFs), a method for grounding language embeddings from off-the-shelf models like CLIP into NeRF, which enable these types of ...
- LERF learns a dense, multiscale language field inside NeRF by volume rendering CLIP embeddings along training rays, supervising these embeddings across training views to provide multi-view consistency and ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- queries like “Electricity”, visual properties like “Yellow”, long-tail objects such as “Waldo”, and even reading text like “Boops” on the mug.
- For each prompt, an RGB image and relevancy map are rendered focusing on the location with maximum relevancy activation.
- Abstract ended language queries in 3D.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work we propose Language Embedded Radiance Fields (LERFs), a method for grounding language embeddings from off-the-shelf models like CLIP into NeRF, which enable these types of ...
- LERF learns a dense, multiscale language field inside NeRF by volume rendering CLIP embeddings along training rays, supervising these embeddings across training views to provide multi-view consistency and ...

## Abstract Cue
- queries like “Electricity”, visual properties like “Yellow”, long-tail objects such as “Waldo”, and even reading text like “Boops” on the mug.
