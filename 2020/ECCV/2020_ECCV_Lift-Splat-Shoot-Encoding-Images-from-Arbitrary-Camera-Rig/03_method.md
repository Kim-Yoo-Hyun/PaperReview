# Method

- Year/Venue: 2020 / ECCV
- Category: Foundations: 3D Detection and BEV Perception
- Tags: 3D Vision, BEV, sensor fusion, camera
- Paper link: ./2020/ECCV/2020_ECCV_Lift-Splat-Shoot-Encoding-Images-from-Arbitrary-Camera-Rig/paper.pdf
- Code/Project: https://github.com/nv-tlabs/lift-splat-shoot
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this section, we present our approach for learning bird’s-eye-view representations of scenes from image data captured by an arbitrary camera rig.
- We propose a new end-to-end architecture that directly extracts a bird’s-eye-view representation of a scene given image data from an arbitrary number of cameras.
- The core idea behind our approach is to “lift” each image individually into a frustum of features for each camera, then “splat” all frustums into a rasterized bird’s-eyeview ...

## 원리적 동기
- For instance, for the problem of 3D object detection from n cameras, one can apply a single-image detector to all input images individually, then rotate and translate each ...
- On standard bird’seye-view tasks such as object segmentation and map segmentation, our model outperforms all baselines and prior work.
- In this section, we present our approach for learning bird’s-eye-view representations of scenes from image data captured by an arbitrary camera rig.

## 핵심 방법론
- In this section, we present our approach for learning bird’s-eye-view representations of scenes from image data captured by an arbitrary camera rig.
