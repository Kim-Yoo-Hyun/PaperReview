# Deep Closest Point: Learning Representations for Point Cloud Registration

- Year/Venue: 2019 / ICCV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: 3D Vision, registration, point cloud, alignment
- Paper link: ./2019/ICCV/2019_ICCV_Deep-Closest-Point-Learning-Representations-for-Point-Clou/paper.pdf
- Code/Project: https://github.com/WangYueFt/dcp
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Point cloud registration is a key problem for computer vision applied to robotics, medical imaging, and other applications.
- This problem involves finding a rigid transformation from one point cloud into another so that they align.
- Many modeling and computational challenges hamper the design of a stable and efficient registration method.

## Core Idea
- To address local optima and other difficulties in the ICP pipeline, we propose a learning-based method, titled Deep Closest Point (DCP), inspired by recent techniques in computer vision ...
- Our model consists of three parts: a point cloud embedding network, an attention-based module combined with a pointer generation layer, to approximate combinatorial matching, and a differentiable singular ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Beyond providing a state-of-the-art registration technique, we evaluate the suitability of our learned features transferred to unseen objects.
- However, only our method achieve satisfying alignment for objects with sharp features and large transformation.
- We train our model end-to-end on the ModelNet40 dataset and show in several settings that it performs better than ICP, its variants (e.g., Go-ICP, FGR), and the recently-proposed ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our model consists of three parts: a point cloud embedding network, an attention-based module combined with a pointer generation layer, to approximate combinatorial matching, and a differentiable singular ...
- However, only our method achieve satisfying alignment for objects with sharp features and large transformation.
- To address local optima and other difficulties in the ICP pipeline, we propose a learning-based method, titled Deep Closest Point (DCP), inspired by recent techniques in computer vision ...

## Abstract Cue
- Point cloud registration is a key problem for computer vision applied to robotics, medical imaging, and other applications.
