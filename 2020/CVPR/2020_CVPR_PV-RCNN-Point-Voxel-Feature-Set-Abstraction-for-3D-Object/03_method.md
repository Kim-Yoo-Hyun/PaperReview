# Method

- Year/Venue: 2020 / CVPR
- Category: Foundations: 3D Detection and BEV Perception
- Tags: point cloud, 3D Vision
- Paper link: ./2020/CVPR/2020_CVPR_PV-RCNN-Point-Voxel-Feature-Set-Abstraction-for-3D-Object/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Grid Point Keypoint z y We present a novel and high-performance 3D object detection framework, named PointVoxel-RCNN (PV-RCNN), for accurate 3D object detection from point clouds.
- We adopt the official released evaluation tools for evaluating our method, where the mean average precision (mAP) and the mean average precision weighted by heading (mAPH) are used ...
- 15th, 2019, our method currently ranks 1st on the car 3D detection leaderboard among all methods including both the RGB+LiDAR methods and LiDAR-only methods, and ranks 1st on ...

## 원리적 동기
- Most existing 3D detection methods could be classified into two categories in terms of point cloud representations, i.e., the grid-based methods and the point-based methods.
- Grid Point Keypoint z y We present a novel and high-performance 3D object detection framework, named PointVoxel-RCNN (PV-RCNN), for accurate 3D object detection from point clouds.

## 핵심 방법론
- We adopt the official released evaluation tools for evaluating our method, where the mean average precision (mAP) and the mean average precision weighted by heading (mAPH) are used ...
- 15th, 2019, our method currently ranks 1st on the car 3D detection leaderboard among all methods including both the RGB+LiDAR methods and LiDAR-only methods, and ranks 1st on ...
- Recall of different proposal generation networks on the car class at moderate difficulty level of the KITTI val split set. mentation to randomly “paste” some new ground-truth objects ...
- 3D Detection on the Waymo Open Dataset RPN with 3D Keypoints RoI-grid Voxel CNN Encoding Pooling RPN Baseline X Pool from Encoder X X PV-RCNN X X X ...
