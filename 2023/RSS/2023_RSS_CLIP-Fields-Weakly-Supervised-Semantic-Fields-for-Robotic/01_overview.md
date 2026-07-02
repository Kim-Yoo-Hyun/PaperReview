# CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory

- Year/Venue: 2023 / RSS
- Category: Open-Vocabulary 3D Mapping
- Tags: CLIP, Robotics, semantic, NeRF
- Paper link: ./2023/RSS/2023_RSS_CLIP-Fields-Weakly-Supervised-Semantic-Fields-for-Robotic/paper.pdf
- Code/Project: https://mahis.life/clip-fields/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, existing representations are coarse, often relying on a preset list of classes and capturing minimal semantics .

## Core Idea
- —We propose CLIP-Fields, an implicit scene model that can be used for a variety of tasks, such as segmentation, instance identification, semantic search over space, and view localization.
- As a solution, we propose CLIP-Fields, which builds an implicit spatial semantic memory using webscale pretrained models as weak supervision.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- When compared to baselines like Mask-RCNN, our method outperforms on few-shot instance identification or semantic segmentation on the HM3D dataset with only a fraction of the examples.
- Importantly, we show that this mapping can be trained with supervision coming only from webimage and web-text trained models such as CLIP, Detic, and Sentence-BERT; and thus uses ...
- Finally, we show that using CLIP-Fields as a scene memory, robots can perform semantic navigation in real-world environments.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- When compared to baselines like Mask-RCNN, our method outperforms on few-shot instance identification or semantic segmentation on the HM3D dataset with only a fraction of the examples.
- —We propose CLIP-Fields, an implicit scene model that can be used for a variety of tasks, such as segmentation, instance identification, semantic search over space, and view localization.
- As a solution, we propose CLIP-Fields, which builds an implicit spatial semantic memory using webscale pretrained models as weak supervision.

## Abstract Cue
- —We propose CLIP-Fields, an implicit scene model that can be used for a variety of tasks, such as segmentation, instance identification, semantic search over space, and view localization.
