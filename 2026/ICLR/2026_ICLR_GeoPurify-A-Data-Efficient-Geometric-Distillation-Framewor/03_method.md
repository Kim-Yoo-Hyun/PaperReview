# Method

- Year/Venue: 2026 / ICLR Poster
- Category: 3D Semantic Understanding and Alignment
- Tags: semantic, alignment, 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_GeoPurify-A-Data-Efficient-Geometric-Distillation-Framewor/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- This result provides compelling evidence that our method learns a more fundamental and truly domain-agnostic understanding of 3D geometry.
- We analyze the impact of our core geometric purification module, the choice of 2D backbone, the contrastive sampling strategy, the number of pooling iterations (T ), and the ...
- Component Setting mIoU mAcc Geometric Purification w/o Purification (Aggregated 2D features) + GeoPurify (Ours) 50.2 55.1 68.1 72.5 2D Semantic Backbone LSeg LSeg + GeoPurify 48.6 51.2 61.6 ...

## 원리적 동기
- To move beyond these limitations, the field is shifting toward open-vocabulary 3D understanding, which enables models to identify objects using arbitrary descriptions rather than predefined labels.
- Existing approaches can be grouped into two categories: training-free and training-based.
- This result provides compelling evidence that our method learns a more fundamental and truly domain-agnostic understanding of 3D geometry.

## 핵심 방법론
- ScanNetV2 Matterport3D mIoU mAcc mIoU mAcc TextureNet Huang et al. (2019) ScanComplete (Dai et al., 2018) DCM-Net (Schult et al., 2020) SupCon (Zheng et al., 2021) MinkowskiNet (Choy ...
- Generalizability on Long-Tail Datasets.
- As shown in Table 2, GeoPurify establishes a new stateof-the-art on long-tail benchmarks like ScanNet200 and the challenging M160 split.
- This robust generalization arises from the synergy between our semantic and geometric modules.
