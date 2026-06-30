# Evaluation

## Dataset
- SA-V: 50.9K videos, 642.6K masklets, 35.5M masks.
- SA-V split: val 155 videos / 293 masklets, test 150 videos / 278 masklets.
- Training mix includes SA-V, SA-1B, VOS datasets, and internal licensed video data.
- Zero-shot video datasets include DAVIS, YouTube-VOS, MOSE, LVOS/LVOSv2 and additional video segmentation benchmarks.
- Image segmentation evaluation uses 37 zero-shot datasets, including the 23 Segment Anything benchmark datasets.

## Benchmark
- Promptable video segmentation: simulated interactive prompting over multiple frames.
- Semi-supervised VOS: prompt only on the first frame with clicks, boxes, or ground-truth mask.
- Image Segment Anything task: 1-click and 5-click segmentation.
- Dataset/data-engine ablations: performance change from VOS + SA-1B, Phase 1/2/3, and automatic masklets.

## Metrics
- Video: J&F accuracy, and J metric for datasets whose protocol requires it.
- Image: mIoU for 1-click and 5-click settings.
- Speed: FPS on a single A100 GPU.
- Data quality: mask alignment / IoU-based checks in data engine analysis.

## Splits
- SA-V train/val/test split is based on video authors and geographic locations to reduce overlap.
- SA-V val/test emphasize challenging targets with fast motion, occlusion, disappearance, and reappearance.
- Zero-shot datasets are held out from training according to the paper's benchmark protocol.

## Baselines
- SAM.
- SAM + XMem++.
- SAM + Cutie.
- Prior VOS / interactive video segmentation methods under comparable prompt settings.

## Main Results
- SA-V is reported as 53x larger in masks than prior VOS datasets when automatic masklets are included.
- In promptable video segmentation, SAM 2 achieves better accuracy with more than 3x fewer interactions than strong SAM+tracker baselines.
- In semi-supervised VOS across 17 datasets, SAM 2 outperforms SAM+XMem++ and SAM+Cutie across 1-click, 3-click, 5-click, box, and mask prompts.
- In image segmentation, SAM 2 improves over SAM on the 23-dataset SA benchmark and is reported as about 6x faster.

## Reproducibility Notes
- Code/Project: https://github.com/facebookresearch/sam2
- Project page: https://ai.meta.com/research/sam2/
- Dataset page is linked from the project and Meta page.
- Model checkpoints, training code, dataset, and demo are publicly released, but full reproduction still requires substantial compute and careful data handling.
