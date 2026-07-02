# Dynamic Graph CNN for Learning on Point Clouds

- Year/Venue: 2019 / TOG
- Category: Foundations: 3D Representation Learning
- Tags: point cloud, 3D Vision
- Paper link: ./2019/TOG/2019_TOG_Dynamic-Graph-CNN-for-Learning-on-Point-Clouds/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Traditional methods for solving these problems employ handcrafted features to capture geometric properties of point clouds [Lu et al.
- This independence, however, neglects the geometric relationships among points, presenting a fundamental limitation that cannot capture local features.
- This approach, however, usually introduces quantization artifacts and excessive memory usage, making it difficult to go to capture high-resolution or fine-grained features.

## Core Idea
- To address these drawbacks, we propose a novel simple operation, called EdgeConv, which captures local geometric structure while maintaining permutation invariance.
- We summarize the key contributions of our work as follows: • We present a novel operation for learning from point clouds, EdgeConv, to better capture local geometric features ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster.
- Our model achieves the best results on this dataset.
- An advanced version including dynamical graph recomputation achieves the best results on this dataset.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Abstract Cue
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
