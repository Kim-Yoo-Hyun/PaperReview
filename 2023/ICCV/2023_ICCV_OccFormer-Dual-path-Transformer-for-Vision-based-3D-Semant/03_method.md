# Method

- Year/Venue: 2023 / ICCV
- Category: Foundations: 3D Semantic Occupancy
- Tags: 3D Vision, semantic, occupancy, Transformer
- Paper link: ./2023/ICCV/2023_ICCV_OccFormer-Dual-path-Transformer-for-Vision-based-3D-Semant/paper.pdf
- Code/Project: https://github.com/zhangyp15/OccFormer
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this issue, we propose the class-guided sampling method.
- More specifically, we first compute the class frequencies nc ∈ RNc from the training set, where Nc is the number of classes.
- Loss Functions Following Mask2Former , we compute the bipartite matching between the predicted and ground-truth segments, considering only the sampled positions.

## 원리적 동기
- Though LiDAR-based methods , with explicit depth measurements, have been dominating the leading performance on public datasets , vision-based approaches still offer advantages in terms of cost-effectiveness, stability, ...
- Experimental results demonstrate that OccFormer significantly outperforms existing methods for semantic scene completion on SemanticKITTI dataset and for LiDAR semantic segmentation on nuScenes dataset.
- To address this issue, we propose the class-guided sampling method.

## 핵심 방법론
- To address this issue, we propose the class-guided sampling method.
- More specifically, we first compute the class frequencies nc ∈ RNc from the training set, where Nc is the number of classes.
- Loss Functions Following Mask2Former , we compute the bipartite matching between the predicted and ground-truth segments, considering only the sampled positions.
- The final training loss is a simple summation: L = Lmask-cls + Ldepth .
- During training, each voxel is assigned a sampling weight according to its ground-truth class.
