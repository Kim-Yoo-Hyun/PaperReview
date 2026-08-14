# Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics

- Year/Venue: 2017 / RSS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, grasping, synthetic data, analytic grasp metric
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://berkeleyautomation.github.io/dex-net/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- —To reduce data collection time for deep learning of robust robotic grasp plans, we explore training from a synthetic dataset of 6.7 million point clouds, grasps, and analytic ...
- We use the resulting dataset, DexNet 2.0, to train a Grasp Quality Convolutional Neural Network (GQ-CNN) model that rapidly predicts the probability of success of grasps from depth ...
- Experiments with over 1,000 trials on an ABB YuMi comparing grasp planning methods on singulated objects suggest that a GQ-CNN trained with only synthetic data from Dex-Net 2.0 ...

## Core Idea
- We use the resulting dataset, DexNet 2.0, to train a Grasp Quality Convolutional Neural Network (GQ-CNN) model that rapidly predicts the probability of success of grasps from depth ...
- —To reduce data collection time for deep learning of robust robotic grasp plans, we explore training from a synthetic dataset of 6.7 million point clouds, grasps, and analytic ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The Dex-Net 2.0 grasp planner also has the highest success rate on a dataset of 10 novel rigid objects and achieves 99% precision (one false positive out of ...
- Recent results suggest that deep neural networks trained on large datasets of human grasp labels or physical grasp outcomes can be used to plan grasps that are successful ...
- Experiments with over 1,000 trials on an ABB YuMi comparing grasp planning methods on singulated objects suggest that a GQ-CNN trained with only synthetic data from Dex-Net 2.0 ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We use the resulting dataset, DexNet 2.0, to train a Grasp Quality Convolutional Neural Network (GQ-CNN) model that rapidly predicts the probability of success of grasps from depth ...
- —To reduce data collection time for deep learning of robust robotic grasp plans, we explore training from a synthetic dataset of 6.7 million point clouds, grasps, and analytic ...
- 1: Dex-Net 2.0 Architecture. (Center)

## Abstract Cue
- —To reduce data collection time for deep learning of robust robotic grasp plans, we explore training from a synthetic dataset of 6.7 million point clouds, grasps, and analytic grasp metrics generated from thousands of 3D models from Dex-Net 1.0 in randomized poses on a table.
