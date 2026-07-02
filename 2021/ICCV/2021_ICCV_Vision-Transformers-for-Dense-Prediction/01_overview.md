# Vision Transformers for Dense Prediction

- Year/Venue: 2021 / ICCV
- Category: Foundations: Monocular Geometry
- Tags: 3D Vision, monocular depth, Vision Transformer, geometry
- Paper link: ./2021/ICCV/2021_ICCV_Vision-Transformers-for-Dense-Prediction/paper.pdf
- Code/Project: https://github.com/isl-org/DPT
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Introduction Virtually all existing architectures for dense prediction are based on convolutional networks .

## Core Idea
- We introduce dense vision transformers, an architecture that leverages vision transformers in place of convolutional networks as a backbone for dense prediction tasks.
- Our experiments show that this architecture yields substantial improvements on dense prediction tasks, especially when a large amount of training data is available.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments show that this architecture yields substantial improvements on dense prediction tasks, especially when a large amount of training data is available.
- For monocular depth estimation, we observe an improvement of up to 28% in relative performance when compared to a state-of-theart fully-convolutional network.
- We further show that the architecture can be fine-tuned on smaller datasets such as NYUv2, KITTI, and Pascal Context where it also sets the new state of the ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our experiments show that this architecture yields substantial improvements on dense prediction tasks, especially when a large amount of training data is available.
- We introduce dense vision transformers, an architecture that leverages vision transformers in place of convolutional networks as a backbone for dense prediction tasks.
- The design of dense prediction architectures commonly follows a pattern that logically separates the network into an encoder and a decoder.

## Abstract Cue
- We introduce dense vision transformers, an architecture that leverages vision transformers in place of convolutional networks as a backbone for dense prediction tasks.
