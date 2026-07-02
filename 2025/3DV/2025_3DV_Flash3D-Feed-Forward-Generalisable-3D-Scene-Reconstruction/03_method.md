# Method

- Year/Venue: 2025 / 3DV
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_Flash3D-Feed-Forward-Generalisable-3D-Scene-Reconstruction/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose Flash3D, a method for scene reconstruction and novel view synthesis from a single image which is both very generalisable and efficient.
- This suggests that prior works do not generalise as well as our method.
- Second, we compare our method on KITTI in Tab.

## 원리적 동기
- Introduction We consider the problem of reconstructing photorealistic 3D scenes from a single image in just one forward pass of a network.
- This problem is closely related to monocular depth estimation , which is a mature area.
- We propose Flash3D, a method for scene reconstruction and novel view synthesis from a single image which is both very generalisable and efficient.

## 핵심 방법론
- This suggests that prior works do not generalise as well as our method.
- Second, we compare our method on KITTI in Tab.
- 1, we observe that our method performs significantly better on this transfer experiment, despite the domain gap being relatively small.
- Given that UniDepth remains frozen during training, we can expedite the training by pre-extracting depth maps for the entire dataset.
- The training is remarkably efficient, completed in one day on a single A6000 GPU.
