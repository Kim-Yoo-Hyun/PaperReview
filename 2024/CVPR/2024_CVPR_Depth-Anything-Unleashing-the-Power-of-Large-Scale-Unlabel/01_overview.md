# Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data

- Year/Venue: 2024 / CVPR
- Category: Foundations: Monocular Geometry
- Tags: depth, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_Depth-Anything-Unleashing-the-Power-of-Large-Scale-Unlabel/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Monocular Depth Estimation (MDE), which is a fundamental problem with broad applications in robotics , autonomous driving , virtual reality , etc., also requires a foundation model to ...

## Core Idea
- This allows our method to enjoy both the semantic-aware representation from DINOv2 and the part-level discriminative representation from depth supervision.
- Following MiDaS , we use the DPT decoder for

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our better depth model also results in a better depth-conditioned ControlNet.
- We evaluate its zero-shot capabilities extensively, including six public datasets and randomly captured photos.
- It demonstrates impressive generalization ability (Figure 1).

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- These successes primarily rely on large-scale training data that can effectively cover the data distribution.
- MiDaS made a pioneering study along this direction by training an MDE model on a collection of mixed labeled datasets.
- Second, an auxiliary supervision is developed to enforce the model to inherit rich semantic priors from pre-trained encoders.

## Abstract Cue
- This work presents Depth Anything1 , a highly practical solution for robust monocular depth estimation.
