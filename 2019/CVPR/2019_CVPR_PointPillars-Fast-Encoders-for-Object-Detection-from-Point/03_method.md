# Method

- Year/Venue: 2019 / CVPR
- Category: Foundations: 3D Detection and BEV Perception
- Tags: 3D Vision, LiDAR, 3D detection, BEV
- Paper link: ./2019/CVPR/2019_CVPR_PointPillars-Fast-Encoders-for-Object-Detection-from-Point/paper.pdf
- Code/Project: https://github.com/nutonomy/second.pytorch
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Performance (AP) arXiv:1812.05784v2 [cs.LG] 7 May 2019 {alex, sourabh, holger, lubing, jiong.yang, oscar}@nutonomy.com Cyclist PP F A S V Runtime (Hz) Figure 1.
- Bird’s eye view performance vs speed for our proposed PointPillars, PP method on the KITTI test set.
- Lidar-only methods drawn as blue circles; lidar & vision methods drawn as red squares.

## 원리적 동기
- Introduction Deploying autonomous vehicles (AVs) in urban environments poses a difficult technological challenge.
- This overhead perspective offers several advantages such as lack of scale ambiguity and the near lack of occlusion.
- Performance (AP) arXiv:1812.05784v2 [cs.LG] 7 May 2019 {alex, sourabh, holger, lubing, jiong.yang, oscar}@nutonomy.com Cyclist PP F A S V Runtime (Hz) Figure 1.

## 핵심 방법론
- Modality MV3D Cont-Fuse Roarnet AVOD-FPN F-PointNet HDNET PIXOR++ VoxelNet SECOND PointPillars Lidar & Img.
- Lidar & Map Lidar Lidar Lidar Lidar Method Modality MV3D Cont-Fuse Roarnet AVOD-FPN F-PointNet VoxelNet SECOND PointPillars Lidar & Img.
- Lidar Lidar Lidar Speed mAP Car Pedestrian (Hz) Mod.
- Hard 2.8 N/A 86.02 76.90 68.49 N/A N/A N/A 16.7 N/A 88.81 85.83 77.33 N/A N/A N/A
