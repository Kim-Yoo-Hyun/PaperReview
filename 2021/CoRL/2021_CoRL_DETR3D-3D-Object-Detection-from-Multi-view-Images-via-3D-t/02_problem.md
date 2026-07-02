# Problem

- Year/Venue: 2021 / CoRL
- Category: Sensor Fusion, LiDAR, and Autonomous Driving
- Tags: 3D Vision, BEV, 3D detection, camera
- Paper link: ./2021/CoRL/2021_CoRL_DETR3D-3D-Object-Detection-from-Multi-view-Images-via-3D-t/paper.pdf
- Code/Project: https://github.com/WangYueFt/detr3d
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- 3D object detection from visual information is a long-standing challenge for low-cost autonomous driving systems.
- Our framework, termed DETR3D (Multi-View 3D Detection), addresses this problem in a top-down fashion.
- Different from existing works that combine object predictions from the different camera views in a final stage, our method fuses information from all the camera views in each ...

## 해결하려는 문제
- We achieve state-of-the-art performance on the nuScenes autonomous driving benchmark.
- In contrast to existing works, which estimate 3D bounding boxes directly from monocular images or use depth prediction networks to generate input for 3D object detection from 2D ...
- : We introduce a framework for multi-camera 3D object detection.

## 선행 연구 / 배경 단서
- 3D object detection from visual information is a long-standing challenge for low-cost autonomous driving systems.
- Different from existing works that combine object predictions from the different camera views in a final stage, our method fuses information from all the camera views in each ...
- It does not suffer from inaccurate depth predictions from a secondary network, and seamlessly uses information from multiple cameras by back-projecting 3D information onto all available frames. • ...
