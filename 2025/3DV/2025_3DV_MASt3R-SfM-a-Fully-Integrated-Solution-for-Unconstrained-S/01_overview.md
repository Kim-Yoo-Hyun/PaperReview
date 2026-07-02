# MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion

- Year/Venue: 2025 / 3DV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_MASt3R-SfM-a-Fully-Integrated-Solution-for-Unconstrained-S/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The presence of outliers, e.g. wrong pixel matches, poses additional challenges and compels existing methods to resort to hypothesis formulation and verification at multiple occasions in the pipeline, ...
- Since finding the global minimum in such a landscape is too challenging to be done directly, traditional SfM approaches such as COLMAP decomposes the problem as a series ...
- These changes must, however, be put into perspective, as they do not fundamentally challenge the overall structure of the traditional pipeline.

## Core Idea
- We note that 14 scenes of T&T are part of MegaDepth , which is used for training the MASt3R checkpoint we used.
- Our approach compares favorably to existing methods, particularly when the number of input images is low.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We show here a reconstruction from 6 views sharing the same optical center. tive function with many local minima .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In comparison, FlowMap and Ace-Zero independently propose a radically novel type of approach to solve SfM, which is based on simple first-order gradient descent of a global loss ...
- The presence of outliers, e.g. wrong pixel matches, poses additional challenges and compels existing methods to resort to hypothesis formulation and verification at multiple occasions in the pipeline, ...
- We show here a reconstruction from 6 views sharing the same optical center. tive function with many local minima .

## Abstract Cue
- Philippe Weinzaepfel3 Jerome Revaud3 Figure 1.
