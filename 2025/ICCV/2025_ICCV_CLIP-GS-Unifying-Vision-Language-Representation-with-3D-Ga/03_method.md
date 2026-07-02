# Method

- Year/Venue: 2025 / ICCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Vision-Language Model, 3D Vision, Gaussian Splatting
- Paper link: ./2025/ICCV/2025_ICCV_CLIP-GS-Unifying-Vision-Language-Representation-with-3D-Ga/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce the GS Tokenizer to generate serialized gaussian tokens, which are then processed through transformer layers pre-initialized with weights from point cloud models, resulting in the 3DGS ...
- In this paper, we present CLIPGS, a novel multimodal representation learning framework grounded in 3DGS.
- CLIP-GS leverages contrastive loss between 3DGS and the visual-text embeddings of CLIP, and we introduce an image voting loss to guide the directionality and convergence of gradient optimization.

## 원리적 동기
- This limitation constrains the potential of point cloud-based 3D multimodal representation learning.
- Existing works in 3D representation learning have made remarkable progress, particularly through the development of transformer-based approaches , as well as mamba-based approaches .
- We introduce the GS Tokenizer to generate serialized gaussian tokens, which are then processed through transformer layers pre-initialized with weights from point cloud models, resulting in the 3DGS ...

## 핵심 방법론
- We use the Objaverse-GS for analysis.
- For the xyz-order, we used the x-axis order for visualization.
- 7, exploring the effectiveness of initializing transformer layers in CLIP-GS with either 2D pretraining models or point cloud pretraining models.
- We report the performance of training CLIPGS from the 2D pretraining model EVA-CLIP and the point cloud pretraining model Uni3D .
- We report the average accuracy (%) for 5-shot classification across 5, 10, 20, and 50 ways. * denotes Objacerse-LVIS shapes are used during training.
