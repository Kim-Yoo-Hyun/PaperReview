# Self-Supervised Pretraining of 3D Features on any Point-Cloud

- Year/Venue: 2021 / ICCV
- Category: Foundations: 3D Representation Learning
- Tags: 3D Vision, point cloud, representation, self-supervised
- Paper link: ./2021/ICCV/2021_ICCV_Self-Supervised-Pretraining-of-3D-Features-on-any-Point-Cl/paper.pdf
- Code/Project: https://github.com/facebookresearch/DepthContrast
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- A primary reason is the lack of large annotated datasets because 3D data is both difficult to acquire and time consuming to label.
- Pretraining on depth maps faces several challenges: first, the absence of any supervision at scale requires
- Thus, 3D data acquisition and annotation both require significantly more effort than images or videos, and there is no existing weak supervision, like image tags, to shortcut the ...

## Core Idea
- We use our data augmentation described in § 3.4 and use the training objectives from § 3.
- We present a simple self-supervised pretraining method that can work with any 3D data — single or multiview, indoor or outdoor, acquired by varied sensors, without 3D registration.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We evaluate our models on 9 benchmarks for object detection, semantic segmentation, and object classification, where they achieve stateof-the-art results and can outperform supervised pretraining.
- Our pretraining which uses unlabeled single-view 3D data, outperforms training from scratch, and achieves the same detection performance with about half the detection labels. points that need to ...
- We pretrain standard point cloud and voxel based model architectures, and show that joint pretraining further improves performance.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We evaluate our models on 9 benchmarks for object detection, semantic segmentation, and object classification, where they achieve stateof-the-art results and can outperform supervised pretraining.
- We pretrain standard point cloud and voxel based model architectures, and show that joint pretraining further improves performance.
- Our pretraining which uses unlabeled single-view 3D data, outperforms training from scratch, and achieves the same detection performance with about half the detection labels. points that need to ...

## Abstract Cue
- Same perf. ~2x fewer labels Pretraining on large labeled datasets is a prerequisite to achieve good performance in many computer vision tasks like 2D object recognition, video classification etc.
