# SSCNet: Semantic Scene Completion from a Single Depth Image

- Year/Venue: 2017 / CVPR
- Category: Foundations: 3D Semantic Occupancy
- Tags: 3D Vision, semantic, occupancy, geometry
- Paper link: ./2017/CVPR/2017_CVPR_SSCNet-Semantic-Scene-Completion-from-a-Single-Depth-Image/paper.pdf
- Code/Project: https://github.com/shurans/sscnet
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, we observe that these two problems are tightly intertwined.
- Therefore, the two problems of predicting voxel occupancy and identifying object semantics are strongly coupled.

## Core Idea
- The SUNCG test set consists of 500 depth images rendered from 184 scenes that are not in the training set.
- To leverage the coupled nature of these two tasks, we introduce the semantic scene completion network (SSCNet), an end-to-end 3D convolutional network that takes a single depth image ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments demonstrate that the joint model outperforms methods addressing each task in isolation and outperforms alternative approaches on the semantic scene completion task.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our experiments demonstrate that the joint model outperforms methods addressing each task in isolation and outperforms alternative approaches on the semantic scene completion task.
- To leverage the coupled nature of these two tasks, we introduce the semantic scene completion network (SSCNet), an end-to-end 3D convolutional network that takes a single depth image ...
- However, we observe that these two problems are tightly intertwined.

## Abstract Cue
- This paper focuses on semantic scene completion, a task for producing a complete 3D voxel representation of volumetric occupancy and semantic labels for a scene from a single-view depth map observation.
