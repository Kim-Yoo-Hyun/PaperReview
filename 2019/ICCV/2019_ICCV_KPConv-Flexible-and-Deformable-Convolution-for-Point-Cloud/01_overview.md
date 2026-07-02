# KPConv: Flexible and Deformable Convolution for Point Clouds

- Year/Venue: 2019 / ICCV
- Category: Foundations: 3D Representation Learning
- Tags: point cloud, 3D Vision
- Paper link: ./2019/ICCV/2019_ICCV_KPConv-Flexible-and-Deformable-Convolution-for-Point-Cloud/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Such a point cloud is a sparse structure that has the property to be unordered, which makes it very different from a grid.

## Core Idea
- For this task, we use KP-FCNN architecture with the same parameters as in the classification task, adding the positions (x, y, z) as additional features to the constant ...
- We present Kernel Point Convolution1 (KPConv), a new design of point convolution, i.e. that operates on point clouds without any intermediate representation.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Whether they use deformable KPConv for complex tasks, or rigid KPconv for simpler tasks, our networks outperform state-of-the-art classification and segmentation approaches on several datasets.
- We also offer ablation studies and visualizations to provide understanding of what has been learned by KPConv and to validate the descriptive power of deformable KPConv.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Whether they use deformable KPConv for complex tasks, or rigid KPconv for simpler tasks, our networks outperform state-of-the-art classification and segmentation approaches on several datasets.
- We present Kernel Point Convolution1 (KPConv), a new design of point convolution, i.e. that operates on point clouds without any intermediate representation.
- We also offer ablation studies and visualizations to provide understanding of what has been learned by KPConv and to validate the descriptive power of deformable KPConv.

## Abstract Cue
- We present Kernel Point Convolution1 (KPConv), a new design of point convolution, i.e. that operates on point clouds without any intermediate representation.
