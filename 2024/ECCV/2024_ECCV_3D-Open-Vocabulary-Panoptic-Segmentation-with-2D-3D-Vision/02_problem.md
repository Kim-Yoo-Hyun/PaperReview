# Problem

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision, semantic
- Paper link: ./2024/ECCV/2024_ECCV_3D-Open-Vocabulary-Panoptic-Segmentation-with-2D-3D-Vision/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Although prior 3D panoptic segmentation approaches have achieved great performance on closedset benchmarks, generalizing these approaches to unseen things and unseen stuff categories remains an open problem.

## 해결하려는 문제
- Our experiments on the nuScenes and SemanticKITTI datasets show that our method outperforms the strong baseline by a large margin.
- To further improve the classification performance on novel classes and leverage the CLIP model, we propose two novel loss functions: objectlevel distillation loss and voxel-level distillation loss.
- Although prior 3D panoptic segmentation approaches have achieved great performance on closedset benchmarks, generalizing these approaches to unseen things and unseen stuff categories remains an open problem.

## 선행 연구 / 배경 단서
- 3D panoptic segmentation is a crucial task in computer vision with many realworld applications, most notably in autonomous driving.
- It combines 3D semantic and instance segmentation to produce per-point predictions for two different types of objects: things (e.g., car) and stuff (e.g., road).
- To date, there has been significant progress in 3D panoptic segmentation .
