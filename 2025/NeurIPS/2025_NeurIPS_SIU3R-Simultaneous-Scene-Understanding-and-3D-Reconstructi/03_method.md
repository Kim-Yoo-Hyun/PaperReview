# Method

- Year/Venue: 2025 / NeurIPS spotlight
- Category: 3D Semantic Understanding and Alignment
- Tags: 3D reconstruction, semantic, alignment, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_SIU3R-Simultaneous-Scene-Understanding-and-3D-Reconstructi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for decoding pixel-aligned 2D ...
- In particular, to promote understanding from reconstruction, we propose Multi-View Mask Aggregation module, which utilizes 3D geometric clues in G to aggregate semantic information from all views to ...
- In light of this, we propose SIU3R, the first alignment-free framework for generalizable simultaneous understanding and 3D reconstruction from unposed images.

## 원리적 동기
- 2) Information loss in feature compression: To efficiently embed 2D features into 3D representations and save the memory cost during feature rasterization, existing methods usually need to compress ...
- To address the challenges outlined above, we propose SIU3R, a novel generalizable framework achieving SI MULTANEOUS U NDERSTANDING and 3D R ECONSTRUCTION beyond feature alignment (Fig.1 b).
- Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for decoding pixel-aligned 2D ...

## 핵심 방법론
- Our method consists of Image and Text Encoders for extracting multi-view and text features, Gaussian Decoder for decoding pixel-aligned 3D Gaussians, Unified Query Decoder for decoding pixel-aligned 2D ...
- In particular, to promote understanding from reconstruction, we propose Multi-View Mask Aggregation module, which utilizes 3D geometric clues in G to aggregate semantic information from all views to ...
- We design our Image Encoder following ’s architecture as a Vision Transformer (ViT) enhanced with an adapter module.
- Moreover, to improve reconstruction by understanding, we introduce Mask-Guided Geometry Refinement module that leverages 2D masks to enforce intrainstance depth continuity for refining reconstructed 3D geometry.
- We also introduce the following loss in training to enable matching supervision: Nt Ltext = 1 X t CrossEntropy(Softmax(Attn(ftext , Q) · qn ), δngt ), Nt t=1 ...
