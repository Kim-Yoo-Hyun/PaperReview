# Problem

- Year/Venue: 2026 / ICLR Poster
- Category: 3D Semantic Understanding and Alignment
- Tags: semantic, alignment, 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_GeoPurify-A-Data-Efficient-Geometric-Distillation-Framewor/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To move beyond these limitations, the field is shifting toward open-vocabulary 3D understanding, which enables models to identify objects using arbitrary descriptions rather than predefined labels.
- Existing approaches can be grouped into two categories: training-free and training-based.
- This approach fails to scale to the diverse and complex real-world objects and is further constrained by the prohibitive cost of manual 3D annotation, a notoriously laborious process ...

## 해결하려는 문제
- A baseline that directly aggregates 2D features from the X-Decoder backbone without any geometric refinement achieves 50.2 mIoU.
- This result provides compelling evidence that our method learns a more fundamental and truly domain-agnostic understanding of 3D geometry.
- We analyze the impact of our core geometric purification module, the choice of 2D backbone, the contrastive sampling strategy, the number of pooling iterations (T ), and the ...

## 선행 연구 / 배경 단서
- This approach fails to scale to the diverse and complex real-world objects and is further constrained by the prohibitive cost of manual 3D annotation, a notoriously laborious process ...
- Existing approaches can be grouped into two categories: training-free and training-based.
- To move beyond these limitations, the field is shifting toward open-vocabulary 3D understanding, which enables models to identify objects using arbitrary descriptions rather than predefined labels.
