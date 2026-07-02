# Point-MAE: Masked Autoencoders for Point Cloud Self-supervised Learning

- Year/Venue: 2022 / ECCV
- Category: Foundations: 3D Representation Learning
- Tags: point cloud, 3D Vision
- Paper link: ./2022/ECCV/2022_ECCV_Point-MAE-Masked-Autoencoders-for-Point-Cloud-Self-supervi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Inspired by this, we propose a neat scheme of masked autoencoders for point cloud self-supervised learning, addressing the challenges posed by point cloud’s properties, including leakage of location ...

## Core Idea
- Inspired by this, we propose a neat scheme of masked autoencoders for point cloud self-supervised learning, addressing the challenges posed by point cloud’s properties, including leakage of location ...
- We show with our scheme, a simple architecture entirely based on standard Transformers can surpass dedicated Transformer models from supervised learning.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Specifically, our pre-trained models achieve 85.18% accuracy on ScanObjectNN and 94.04% accuracy on ModelNet40, outperforming all the other self-supervised learning methods.
- On the hardest variant PB-T50-RS, our model achieves 85.18% accuracy, outperforming Point-BERT by 2.11%.
- Specifically, our approach with standard Transformers backbone surpasses IAE that uses a more powerful DGCNN as the backbone (As shown in Table 2, when training from scratch, DGCNN ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments show that our approach is efficient during pre-training and generalizes well on various downstream tasks.
- Inspired by this, we propose a neat scheme of masked autoencoders for point cloud self-supervised learning, addressing the challenges posed by point cloud’s properties, including leakage of location ...
- We show with our scheme, a simple architecture entirely based on standard Transformers can surpass dedicated Transformer models from supervised learning.

## Abstract Cue
- As a promising scheme of self-supervised learning, masked autoencoding has significantly advanced natural language processing and computer vision.
