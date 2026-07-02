# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, 3D reconstruction, geometry, semantic, alignment, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_Uni3R-Unified-3D-Reconstruction-and-Semantic-Understanding/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Our approach leverages a Cross-View Transformer to robustly integrate information across arbitrary multi-view inputs, which then regresses a set of 3D Gaussian primitives endowed with semantic feature fields.
- Implementation Details We use DINOv2 as the image encoder, with a patch size of 16, and set the CrossView Transformer layers as L = 24.
- In this paper, we introduce Uni3R, a novel feed-forward framework that jointly reconstructs a unified 3D scene representation enriched with open-vocabulary semantics, directly from unposed multiview images.

## 원리적 동기
- Reconstructing and semantically interpreting 3D scenes from sparse 2D views remains a fundamental challenge in computer vision.
- Conventional methods often decouple semantic understanding from reconstruction or necessitate costly per-scene optimization, thereby restricting their scalability and generalizability.
- Our approach leverages a Cross-View Transformer to robustly integrate information across arbitrary multi-view inputs, which then regresses a set of 3D Gaussian primitives endowed with semantic feature fields.

## 핵심 방법론
- Implementation Details We use DINOv2 as the image encoder, with a patch size of 16, and set the CrossView Transformer layers as L = 24.
- The final training objective is a weighted sum of the individual losses: \mathcal {L}_{\text {total}} = \mathcal {L}_{\text {rgb}} + \lambda _{\text {sem}}\mathcal {L}_{\text {sem}} + \lambda _{\text ...
- We initialize the encoder and decoder with the weights from the pretrained Comparison with Per-Scene Optimized Methods To evaluate efficiency and generalization, we compare Uni3R with the per-scene ...
- The loss is formulated as: VGGT , while the remaining intrinsic layer and Gaussian head are randomly initialized.
