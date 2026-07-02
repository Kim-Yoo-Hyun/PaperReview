# Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling

- Year/Venue: 2022 / CVPR
- Category: Foundations: 3D Representation Learning
- Tags: point cloud, 3D Vision
- Paper link: ./2022/CVPR/2022_CVPR_Point-BERT-Pre-training-3D-Point-Cloud-Transformers-with-M/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Tokenizer We present Point-BERT, a new paradigm for learning Transformers to generalize the concept of BERT to 3D point cloud.
- Inspired by BERT, we devise a Masked Point Modeling (MPM) task to pre-train point cloud Transformers.
- Specifically, we first divide a point cloud into several local point patches, and a point cloud Tokenizer with a discrete Variational AutoEncoder (dVAE) is designed to generate discrete ...

## Core Idea
- Equipped with our pretraining strategy, we show that a pure Transformer architecture attains 93.8% accuracy on ModelNet40 and 83.1% accuracy on the hardest setting of ScanObjectNN, surpassing carefully ...
- Tokenizer We present Point-BERT, a new paradigm for learning Transformers to generalize the concept of BERT to 3D point cloud.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that the proposed BERT-style pretraining strategy significantly improves the performance of standard point cloud Transformers.
- We also demonstrate that the representations learned by Point-BERT transfer well to new tasks and domains, where our models largely advance the state-of-the-art of few-shot point cloud classification ...
- Equipped with our pretraining strategy, we show that a pure Transformer architecture attains 93.8% accuracy on ModelNet40 and 83.1% accuracy on the hardest setting of ScanObjectNN, surpassing carefully ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate that the proposed BERT-style pretraining strategy significantly improves the performance of standard point cloud Transformers.
- Equipped with our pretraining strategy, we show that a pure Transformer architecture attains 93.8% accuracy on ModelNet40 and 83.1% accuracy on the hardest setting of ScanObjectNN, surpassing carefully ...
- Tokenizer We present Point-BERT, a new paradigm for learning Transformers to generalize the concept of BERT to 3D point cloud.

## Abstract Cue
- Tokenizer We present Point-BERT, a new paradigm for learning Transformers to generalize the concept of BERT to 3D point cloud.
