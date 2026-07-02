# Method

- Year/Venue: 2023 / CVPR
- Category: Foundations: 3D Semantic Occupancy
- Tags: semantic, alignment, 3D Vision
- Paper link: ./2023/CVPR/2023_CVPR_VoxFormer-Sparse-Voxel-Transformer-for-Camera-based-3D-Sem/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To enable such capability in AI systems, we propose VoxFormer, a Transformerbased semantic scene completion framework that can output complete 3D volumetric semantics from only 2D images.
- We use 8 sampling points around each reference point for the cross-/self-attention head.
- An SSC solution has to simultaneously address two subtasks: scene reconstruction for visible areas and scene hallucination for Self-Attention Cross-Attention Output Input: 2D Images Query Proposals 3D Semantic ...

## 원리적 동기
- However, obtaining accurate and complete 3D information of the real world is difficult, since the task is challenged by the lack of sensing resolution and the incomplete observation ...
- Introduction Holistic 3D scene understanding is an important problem in autonomous vehicle (AV) perception.
- To enable such capability in AI systems, we propose VoxFormer, a Transformerbased semantic scene completion framework that can output complete 3D volumetric semantics from only 2D images.

## 핵심 방법론
- We use 8 sampling points around each reference point for the cross-/self-attention head.
- The numbers of deformable attention layers for cross-attention and self-attention are 3 and 2 respectively.
