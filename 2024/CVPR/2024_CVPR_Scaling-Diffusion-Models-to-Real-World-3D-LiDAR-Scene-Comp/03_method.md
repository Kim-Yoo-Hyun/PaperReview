# Method

- Year/Venue: 2024 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, Diffusion, Generation, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_Scaling-Diffusion-Models-to-Real-World-3D-LiDAR-Scene-Comp/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Together with our approach, we propose a regularization loss to stabilize the noise predicted during the denoising process.
- Given the promising results of recent diffusion models as generative models for images, we propose extending them to achieve scene completion from a single 3D LiDAR scan.
- Distinctly, we propose to directly operate on the points, reformulating the noising and denoising diffusion process such that it can efficiently work at scene scale.

## 원리적 동기
- Previous works used diffusion models over range images extracted from LiDAR data, directly applying image-based diffusion methods.
- Such systems rely on the data collected by the sensors installed on the vehicle to perceive the environment but fail to deduce areas only partially observable by the ...
- Together with our approach, we propose a regularization loss to stabilize the noise predicted during the denoising process.

## 핵심 방법론
- We compare our method with different scene completion methods, LMSCNet , PVD , Make It Dense (MID) , and LODE .
- The best performance of our method over the CD metric can be explained by the fact that our method operates directly on the points, which enables it to ...
- SDF-based methods inherits artifacts from the voxelization, while our method, especially after the refinement, can generate a scene closer to the expected, following closely the structural information from ...
- For all baselines, we used their official code and the provided weights also trained on SemanticKITTI.
- To maintain the same amount of points used during training, we again use the scan max range as 50 m and sample 18, 000 points with farthest point ...
