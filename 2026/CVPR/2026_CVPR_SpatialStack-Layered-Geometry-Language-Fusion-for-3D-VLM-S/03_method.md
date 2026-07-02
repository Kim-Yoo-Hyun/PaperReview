# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Large Multimodal Models
- Tags: geometry, VLM, spatial reasoning
- Paper link: ./2026/CVPR/2026_CVPR_SpatialStack-Layered-Geometry-Language-Fusion-for-3D-VLM-S/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To overcome this, we propose SpatialStack, a general hierarchical fusion framework that progressively aligns vision, geometry, and language representations across the model hierarchy.
- We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for robust 3D spatial reasoning.
- While recent efforts have introduced multi-view geometry transformers into VLMs, they typically fuse only the deep-layer features from vision and geometry encoders, discarding rich hierarchical signals and creating ...

## 원리적 동기
- This limitation arises from their inability to capture fine-grained 3D geometry and spatial relationships.
- While recent efforts have introduced multi-view geometry transformers into VLMs, they typically fuse only the deep-layer features from vision and geometry encoders, discarding rich hierarchical signals and creating ...
- To overcome this, we propose SpatialStack, a general hierarchical fusion framework that progressively aligns vision, geometry, and language representations across the model hierarchy.

## 핵심 방법론
- We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for robust 3D spatial reasoning.
- By progressively aligning multi-level geometric features with the LLM decoder, SpatialStack preserves both local precision and high-level relational semantics.
