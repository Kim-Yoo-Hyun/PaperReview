# Point Transformer

- Year/Venue: 2021 / ICCV
- Category: Foundations: 3D Representation Learning
- Tags: point cloud, 3D Vision
- Paper link: ./2021/ICCV/2021_ICCV_Point-Transformer/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- part segmentation tic ion an ntat semgme se arXiv:2012.09164v2 [cs.CV] 26 Sep 2021 Hengshuang Zhao1,2 Li Jiang3 Jiaya Jia3 Philip Torr1 Vladlen Koltun4 University of Oxford 2 The ...
- The Point Transformer can serve as the backbone for various 3D point cloud understanding tasks such as object classification, object part segmentation, and semantic scene segmentation. analysis .
- The transformer family of models is particularly appropriate for point cloud processing because the self-attention operator, which is at the core of transformer networks, is in essence a ...

## Core Idea
- It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.
- We use the sampled point sets produced by Qi et al. for a fair comparison with prior work.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- These networks can serve as general backbones for 3D scene understanding. • We report extensive experiments over multiple dom
- We show that Point Transformers are remarkably effective in 3D deep learning tasks, both at the level of detailed object analysis and large-scale parsing of massive scenes.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- The transformer family of models is particularly appropriate for point cloud processing because the self-attention operator, which is at the core of transformer networks, is in essence a ...
- We show that Point Transformers are remarkably effective in 3D deep learning tasks, both at the level of detailed object analysis and large-scale parsing of massive scenes.
- We flesh out this intuition and develop a self-attention layer for 3D point cloud processing.

## Abstract Cue
- part segmentation tic ion an ntat semgme se arXiv:2012.09164v2 [cs.CV] 26 Sep 2021 Hengshuang Zhao1,2 Li Jiang3 Jiaya Jia3 Philip Torr1 Vladlen Koltun4 University of Oxford 2 The University of Hong Kong The Chinese University of Hong Kong 4 Intel Labs Point Transformer Figure 1.
