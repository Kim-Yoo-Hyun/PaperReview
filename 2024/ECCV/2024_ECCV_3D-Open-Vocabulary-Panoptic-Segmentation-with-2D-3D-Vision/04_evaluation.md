# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision, semantic
- Paper link: ./2024/ECCV/2024_ECCV_3D-Open-Vocabulary-Panoptic-Segmentation-with-2D-3D-Vision/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- SemanticKITTI
- nuScenes
- Waymo

## Metrics
- mIoU
- IoU

## Evaluation Protocol and Results
- 4.3 Main Results Since there are no existing methods for the 3D open-vocabulary panoptic segmentation task, we mainly compare with three methods to demonstrate the capability of our ...
- Our method significantly outperforms 3D Open-Vocabulary Panoptic Segmentation 11 Table 1: Quantitative results of panoptic segmentation on nuScenes.
- 4.1 Experimental Setting 9 Following the state-of-the-art closed-set 3D panoptic segmentation work , we conduct experiments and ablation studies on the nuScenes and SemanticKITTI datasets. nuScenes.
- We show that this is due to lack of supervision of the whole scene as P3Former achieves similar performance when only trained on base categories.
- 4.3 Main Results Since there are no existing methods for the 3D open-vocabulary panoptic segmentation task, we mainly compare with three methods to demonstrate the capability of our ...
- Our experiments on the nuScenes and SemanticKITTI datasets show that our method outperforms the strong baseline by a large margin.

## Baselines
- 4.3 Main Results Since there are no existing methods for the 3D open-vocabulary panoptic segmentation task, we mainly compare with three methods to demonstrate the capability of our ...
- In summary, this baseline provides a comparison against our proposed method without the multimodal feature fusion module, the unified segmentation head, and the distillation losses.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
