# Method

- Year/Venue: 2021 / CoRL
- Category: Sensor Fusion, LiDAR, and Autonomous Driving
- Tags: 3D Vision, BEV, 3D detection, camera
- Paper link: ./2021/CoRL/2021_CoRL_DETR3D-3D-Object-Detection-from-Multi-view-Images-via-3D-t/paper.pdf
- Code/Project: https://github.com/WangYueFt/detr3d
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- : We introduce a framework for multi-camera 3D object detection.
- Our method performs worse than FCOS3D in terms of mATE.
- Our method considers all cameras simultaneously, while FCOS3D predicts bounding boxes per camera individually.

## 원리적 동기
- 3D object detection from visual information is a long-standing challenge for low-cost autonomous driving systems.
- Our framework, termed DETR3D (Multi-View 3D Detection), addresses this problem in a top-down fashion.
- : We introduce a framework for multi-camera 3D object detection.

## 핵심 방법론
- Our method performs worse than FCOS3D in terms of mATE.
- Our method considers all cameras simultaneously, while FCOS3D predicts bounding boxes per camera individually.
- Hence, we implement a baseline ourselves to verify that our approach is more effective than explicit depth prediction.
- We use a pre-trained PackNet network to predict dense depth maps from all six cameras and then convert these depth maps into point clouds using the camera transformations.
- For evaluation, we use the nuScenes evalutation toolkit.
