# Problem

- Year/Venue: 2020 / ECCV
- Category: Foundations: 3D Detection and BEV Perception
- Tags: 3D Vision, BEV, sensor fusion, camera
- Paper link: ./2020/ECCV/2020_ECCV_Lift-Splat-Shoot-Encoding-Images-from-Arbitrary-Camera-Rig/paper.pdf
- Code/Project: https://github.com/nv-tlabs/lift-splat-shoot
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- For instance, for the problem of 3D object detection from n cameras, one can apply a single-image detector to all input images individually, then rotate and translate each ...
- On standard bird’seye-view tasks such as object segmentation and map segmentation, our model outperforms all baselines and prior work.
- In pursuit of the goal of learning dense representations for motion planning, we show that the representations inferred by our model enable interpretable end-to-end motion planning by “shooting” ...

## 해결하려는 문제
- We propose a new end-to-end architecture that directly extracts a bird’s-eye-view representation of a scene given image data from an arbitrary number of cameras.
- We benchmark our approach against models that use oracle depth from lidar.
- The core idea behind our approach is to “lift” each image individually into a frustum of features for each camera, then “splat” all frustums into a rasterized bird’s-eyeview ...

## 선행 연구 / 배경 단서
- For instance, for the problem of 3D object detection from n cameras, one can apply a single-image detector to all input images individually, then rotate and translate each ...
- We propose a model named “Lift-Splat” that preserves the 3 symmetries identified above by design while also being end-to-end differentiable.
- In Section 3.3, we propose a method for “shooting” proposal trajectories into this reference plane for interpretable end-to-end motion planning.
