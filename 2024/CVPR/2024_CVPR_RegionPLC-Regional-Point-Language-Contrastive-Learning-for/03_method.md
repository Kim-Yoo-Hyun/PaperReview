# Method

- Year/Venue: 2024 / CVPR
- Category: Open-Vocabulary 3D Mapping
- Tags: point-language, open-world, semantic
- Paper link: ./2024/CVPR/2024_CVPR_RegionPLC-Regional-Point-Language-Contrastive-Learning-for/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Furthermore, our method has the flexibility to be effortlessly integrated with language models to enable open-ended grounded 3D reasoning without extra task-specific training.
- We propose a lightweight and scalable Regional PointLanguage Contrastive learning framework, namely RegionPLC, for open-world 3D scene understanding, aiming to identify and recognize open-set objects and categories.
- In this regard, we propose a Supplementary-orientated Fusion (SFusion) strategy to integrate the most diverse semantic clues while filtering out potential conflicts from different caption sources.

## 원리적 동기
- Despite advancements, existing solutions still exhibit limitations.
- However, this task poses significant challenges due to the scarcity of dense 3D semantic annotations, which are difficult to gather and scale to a large vocabulary space.
- Furthermore, our method has the flexibility to be effortlessly integrated with language models to enable open-ended grounded 3D reasoning without extra task-specific training.

## 핵심 방법론
- In this regard, we propose a Supplementary-orientated Fusion (SFusion) strategy to integrate the most diverse semantic clues while filtering out potential conflicts from different caption sources.
- When training 3D models on data-level mixed 3Dlanguage pairs, they are learning from a more informative language description, but suffer from sub-optimal performance.
