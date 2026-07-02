# Problem

- Year/Venue: 2021 / CVPR
- Category: Foundations: 3D Detection and BEV Perception
- Tags: point cloud, 3D Vision
- Paper link: ./2021/CVPR/2021_CVPR_CenterPoint-Center-based-3D-Object-Detection-and-Tracking/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Compared to the wellstudied 2D detection problem, 3D detection on point-clouds offers a series of interesting challenges: First, point-clouds are sparse, and most regions of 3D space are ...
- This representation mimics the well-studied image-based 2D bounding-box detection but comes with additional challenges.
- Objects in a 3D world do not follow any particular orientation, and box-based detectors have difficulties enumerating all orientations or fitting an axis-aligned bounding box to rotated objects.

## 해결하려는 문제
- CenterPoint achieved state-of-theart performance on the nuScenes benchmark for both 3D detection and tracking, with 65.5 NDS and 63.8 AMOTA for a single model.
- Introduction Figure 1: We present a center-based framework to represent, detect and track objects.
- Compared to the wellstudied 2D detection problem, 3D detection on point-clouds offers a series of interesting challenges: First, point-clouds are sparse, and most regions of 3D space are ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
