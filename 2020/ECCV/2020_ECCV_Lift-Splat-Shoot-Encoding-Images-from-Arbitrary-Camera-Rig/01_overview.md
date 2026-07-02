# Lift, Splat, Shoot: Encoding Images from Arbitrary Camera Rigs by Implicitly Unprojecting to 3D

- Year/Venue: 2020 / ECCV
- Category: Foundations: 3D Detection and BEV Perception
- Tags: 3D Vision, BEV, sensor fusion, camera
- Paper link: ./2020/ECCV/2020_ECCV_Lift-Splat-Shoot-Encoding-Images-from-Arbitrary-Camera-Rig/paper.pdf
- Code/Project: https://github.com/nv-tlabs/lift-splat-shoot
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- For instance, for the problem of 3D object detection from n cameras, one can apply a single-image detector to all input images individually, then rotate and translate each ...
- On standard bird’seye-view tasks such as object segmentation and map segmentation, our model outperforms all baselines and prior work.
- In pursuit of the goal of learning dense representations for motion planning, we show that the representations inferred by our model enable interpretable end-to-end motion planning by “shooting” ...

## Core Idea
- In this section, we present our approach for learning bird’s-eye-view representations of scenes from image data captured by an arbitrary camera rig.
- We propose a new end-to-end architecture that directly extracts a bird’s-eye-view representation of a scene given image data from an arbitrary number of cameras.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- On standard bird’seye-view tasks such as object segmentation and map segmentation, our model outperforms all baselines and prior work.
- In pursuit of the goal of learning dense representations for motion planning, we show that the representations inferred by our model enable interpretable end-to-end motion planning by “shooting” ...
- We benchmark our approach against models that use oracle depth from lidar.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose a new end-to-end architecture that directly extracts a bird’s-eye-view representation of a scene given image data from an arbitrary number of cameras.
- We benchmark our approach against models that use oracle depth from lidar.
- The core idea behind our approach is to “lift” each image individually into a frustum of features for each camera, then “splat” all frustums into a rasterized bird’s-eyeview ...

## Abstract Cue
- The goal of perception for autonomous vehicles is to extract semantic representations from multiple sensors and fuse these representations into a single “bird’s-eye-view” coordinate frame for consumption by motion planning.
