# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Vision-Language Grounding
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_VGMamba-Attribute-to-Location-Clue-Reasoning-for-Quantity/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Particularly, we propose a VGMamba network that consists of an SVD-based attribute mamba, location mamba, and multi-modal fusion mamba.
- Training Objectives Building on previous work , the loss of VGMamba consists of the 3D Visual Grounding loss Lref , text-object contrastive loss Lcon , and object detection ...
- In the experiment, our method is veriﬁed on four datasets.

## 원리적 동기
- Most existing methods often follow a two-stage process, i.e., ﬁrst detecting proposal objects and identifying the right objects based on the relevance to the given query.
- Recent studies have attempted to address this challenge by incorporating both object attributes (e.g., color, shape, texture) and spatial relationships (e.g., relative positions) to improve grounding accuracy.
- Particularly, we propose a VGMamba network that consists of an SVD-based attribute mamba, location mamba, and multi-modal fusion mamba.

## 핵심 방법론
- Training Objectives Building on previous work , the loss of VGMamba consists of the 3D Visual Grounding loss Lref , text-object contrastive loss Lcon , and object detection ...
- Nr3D (Natural Reference in 3D) consists of 41,503 human-annotated referring expressions across 707 indoor scenes, where each description uniquely identiﬁes a target object among distractors.
- Implementation Details The experimental setting for the multi-object dataset is similar to that for the single-object dataset, with a few differences: during training, we treat all predicted bounding ...
