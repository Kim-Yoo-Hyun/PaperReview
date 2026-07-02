# Method

- Year/Venue: 2025 / 3DV
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_SMORE-Simultaneous-Map-and-Object-REconstruction/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Beyond pursuing dynamic reconstruction as a goal in and of itself, we propose that such a system can be used to auto-label partially annotated sequences and produce ground ...
- We present a method for dynamic surface reconstruction of large-scale urban scenes from LiDAR.
- We developed an optimization framework for understanding this problem and provided a simple yet effective solution based on decomposing the problem into well-studied sub-components.

## 원리적 동기
- Beyond pursuing dynamic reconstruction as a goal in and of itself, we propose that such a system can be used to auto-label partially annotated sequences and produce ground ...
- To achieve this, we take inspiration from recent novel view synthesis methods and frame the reconstruction problem as a global optimization over neural surfaces, ego poses, and object ...
- Beyond pursuing dynamic reconstruction as a goal in and of itself, we propose that such a system can be used to auto-label partially annotated sequences and produce ground ...

## 핵심 방법론
- We developed an optimization framework for understanding this problem and provided a simple yet effective solution based on decomposing the problem into well-studied sub-components.
- We compare our method to linearly interpolating the poses as is commonly done to create scene-flow labels . aggregation errors, leading to poor surface reconstructions.
- Pose accuracy evaluation on nuScenes (using NuScene’s default ATE metric), measured by comparing the bounding box locations predicted by our method to held-out ground truth labels provided at ...
- Ego-pose evaluation by fitting a SOTA NeRF method to: the poses provided by nuScenes, those from a LiDAR odometry method, and the ones produced by our method.
- We hope that this method will not only be useful for creating training and evaluation data for other perception tasks but will also promote active research in this ...
