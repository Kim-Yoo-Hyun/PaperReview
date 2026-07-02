# GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation

- Year/Venue: 2026 / ICLR Poster
- Category: 3D Semantic Understanding and Alignment
- Tags: semantic, alignment, 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_GeoPurify-A-Data-Efficient-Geometric-Distillation-Framewor/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To move beyond these limitations, the field is shifting toward open-vocabulary 3D understanding, which enables models to identify objects using arbitrary descriptions rather than predefined labels.
- Existing approaches can be grouped into two categories: training-free and training-based.
- This approach fails to scale to the diverse and complex real-world objects and is further constrained by the prohibitive cost of manual 3D annotation, a notoriously laborious process ...

## Core Idea
- This result provides compelling evidence that our method learns a more fundamental and truly domain-agnostic understanding of 3D geometry.
- We analyze the impact of our core geometric purification module, the choice of 2D backbone, the contrastive sampling strategy, the number of pooling iterations (T ), and the ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- A baseline that directly aggregates 2D features from the X-Decoder backbone without any geometric refinement achieves 50.2 mIoU.
- The results, summarized in Table 4, systematically deconstruct our model to validate its core design principles.
- Models are trained on the source dataset and evaluated directly on the target without fine-tuning.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- A baseline that directly aggregates 2D features from the X-Decoder backbone without any geometric refinement achieves 50.2 mIoU.
- This result provides compelling evidence that our method learns a more fundamental and truly domain-agnostic understanding of 3D geometry.
- We analyze the impact of our core geometric purification module, the choice of 2D backbone, the contrastive sampling strategy, the number of pooling iterations (T ), and the ...

## Abstract Cue
- This purely structural knowledge is highly transferable, acting as a robust regularizer even when the semantic context changes entirely.
