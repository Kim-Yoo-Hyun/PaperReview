# 3D Open-Vocabulary Panoptic Segmentation with 2D-3D Vision-Language Distillation

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision, semantic
- Paper link: ./2024/ECCV/2024_ECCV_3D-Open-Vocabulary-Panoptic-Segmentation-with-2D-3D-Vision/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Although prior 3D panoptic segmentation approaches have achieved great performance on closedset benchmarks, generalizing these approaches to unseen things and unseen stuff categories remains an open problem.

## Core Idea
- To further improve the classification performance on novel classes and leverage the CLIP model, we propose two novel loss functions: objectlevel distillation loss and voxel-level distillation loss.
- Then we provide detailed descriptions of the model architecture as well as the proposed loss functions.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- 4.3 Main Results Since there are no existing methods for the 3D open-vocabulary panoptic segmentation task, we mainly compare with three methods to demonstrate the capability of our ...
- Our experiments on the nuScenes and SemanticKITTI datasets show that our method outperforms the strong baseline by a large margin.
- Our method significantly outperforms 3D Open-Vocabulary Panoptic Segmentation 11 Table 1: Quantitative results of panoptic segmentation on nuScenes.

## Limitation
- We experimentally verified that simply extending the 2D open-vocabulary segmentation method into 3D does not yield good performance, and demonstrated that our proposed model design and loss functions ...

## Contribution
- Our experiments on the nuScenes and SemanticKITTI datasets show that our method outperforms the strong baseline by a large margin.
- To further improve the classification performance on novel classes and leverage the CLIP model, we propose two novel loss functions: objectlevel distillation loss and voxel-level distillation loss.
- Although prior 3D panoptic segmentation approaches have achieved great performance on closedset benchmarks, generalizing these approaches to unseen things and unseen stuff categories remains an open problem.

## Abstract Cue
- 3D panoptic segmentation is a challenging perception task, especially in autonomous driving.
