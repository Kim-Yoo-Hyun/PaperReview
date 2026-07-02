# Digging Into Self-Supervised Monocular Depth Estimation

- Year/Venue: 2019 / ICCV
- Category: Foundations: Monocular Geometry
- Tags: 3D Vision, monocular depth, self-supervised, geometry
- Paper link: ./2019/ICCV/2019_ICCV_Digging-Into-Self-Supervised-Monocular-Depth-Estimation/paper.pdf
- Code/Project: https://github.com/nianticlabs/monodepth2
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, collecting large and varied training datasets with accurate ground truth depth for supervised learning is itself a formidable challenge.
- To overcome this limitation, self-supervised learning has emerged as a promising alternative for training models to perform monocular depth estimation.
- Generating high quality depth-from-color is attractive because it could inexpensively complement LIDAR sensors used in self-driving cars, and enable new single-photo applications such as image-editing and AR-compositing.

## Core Idea
- In particular, we propose (i) a minimum reprojection loss, designed to robustly handle occlusions, (ii) a full-resolution multi-scale sampling method that reduces visual artifacts, and (iii) an auto-masking ...
- Research on self-supervised monocular training usually explores increasingly complex architectures, loss functions, and image formation models, all of which have recently helped to close the gap with fully-supervised ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We demonstrate the effectiveness of each component in isolation, and show high quality, state-of-the-art results on the KITTI benchmark.
- In this paper, we propose a set of improvements, which together result in both quantitatively and qualitatively improved depth maps compared to competing self-supervised methods.
- We show that a surprisingly simple model, and associated design choices, lead to superior predictions.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We demonstrate the effectiveness of each component in isolation, and show high quality, state-of-the-art results on the KITTI benchmark.
- Research on self-supervised monocular training usually explores increasingly complex architectures, loss functions, and image formation models, all of which have recently helped to close the gap with fully-supervised ...
- In particular, we propose (i) a minimum reprojection loss, designed to robustly handle occlusions, (ii) a full-resolution multi-scale sampling method that reduces visual artifacts, and (iii) an auto-masking ...

## Abstract Cue
- Per-pixel ground-truth depth data is challenging to acquire at scale.
