# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision, semantic
- Paper link: ./2024/ECCV/2024_ECCV_3D-Open-Vocabulary-Panoptic-Segmentation-with-2D-3D-Vision/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To further improve the classification performance on novel classes and leverage the CLIP model, we propose two novel loss functions: objectlevel distillation loss and voxel-level distillation loss.
- Then we provide detailed descriptions of the model architecture as well as the proposed loss functions.
- In this paper, we propose the first method to tackle 3D open-vocabulary panoptic segmentation.

## 원리적 동기
- Although prior 3D panoptic segmentation approaches have achieved great performance on closedset benchmarks, generalizing these approaches to unseen things and unseen stuff categories remains an open problem.
- To further improve the classification performance on novel classes and leverage the CLIP model, we propose two novel loss functions: objectlevel distillation loss and voxel-level distillation loss.

## 핵심 방법론
- Then we provide detailed descriptions of the model architecture as well as the proposed loss functions.
- The overview of our method is presented in Fig.
- Following the settings of prior work , we assume the availability of the name of the novel categories during inference, but the novel categories are not present in ...
- 1, and the two proposed loss functions are illustrated in Fig.
