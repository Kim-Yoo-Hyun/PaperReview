# Method

- Year/Venue: 2018 / CVPR
- Category: Foundations: 3D Detection and BEV Perception
- Tags: 3D Vision, LiDAR, 3D detection, sensor fusion
- Paper link: ./2018/CVPR/2018_CVPR_VoxelNet-End-to-End-Learning-for-Point-Cloud-Based-3D-Obje/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present several 3D detection examples in Figure 6.
- Our approach can operate directly on sparse 3D points and capture 3D shape information effectively.
- To analyze the importance of end-to-end learning, we implement a strong baseline that is derived from the VoxelNet architecture but uses hand-crafted features instead of the proposed feature ...

## 원리적 동기
- Accurate detection of objects in 3D point clouds is a central problem in many applications, such as autonomous navigation, housekeeping robots, and augmented/virtual reality.
- To interface a highly sparse LiDAR point cloud with a region proposal network (RPN), most existing efforts have focused on hand-crafted feature representations, for example, a bird’s eye ...
- We present several 3D detection examples in Figure 6.

## 핵심 방법론
- We present several 3D detection examples in Figure 6.
- Our approach can operate directly on sparse 3D points and capture 3D shape information effectively.
- To analyze the importance of end-to-end learning, we implement a strong baseline that is derived from the VoxelNet architecture but uses hand-crafted features instead of the proposed feature ...
- In this paper, we remove the bottleneck of manual feature engineering and propose VoxelNet, a novel end-to-end trainable deep architecture for point cloud based 3D detection.
- We train the HC-baseline using the same training procedure and data augmentation described in Section 3.
