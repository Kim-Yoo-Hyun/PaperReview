# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, semantic
- Paper link: ./2024/ECCV/2024_ECCV_Dense-Multimodal-Alignment-for-Open-Vocabulary-3D-Scene-Un/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- ScanNet200
- Matterport3D
- nuScenes

## Metrics
- accuracy
- mIoU
- mAP

## Evaluation Protocol and Results
- Our DMA(OpenSeg) using only 3D model for prediction outperforms OpenScene(OpenSeg)-2D3D by 5.4% mIoU at a significantly lower latency, wherein the mIoU (F) and mIoU (B) are improved by ...
- When using text supervision only, our method outperforms the text-supervised approach RegionPLC by 9.5%, and even surpasses OpenScene(OpenSeg)-2D3D by 2.6% in terms of mIoU.
- We conduct comparisons with state-of-the-art methods on each of these datasets.
- Comparison with State-of-the-Arts We compare the proposed DMA with fully-/weakly-supervised and zero-shot methods .
- Our DMA(OpenSeg) using only 3D model for prediction outperforms OpenScene(OpenSeg)-2D3D by 5.4% mIoU at a significantly lower latency, wherein the mIoU (F) and mIoU (B) are improved by ...
- Extensive experiments show that our DMA method produces highly competitive open-vocabulary segmentation performance on various indoor and outdoor tasks.

## Baselines
- Comparison with State-of-the-Arts We compare the proposed DMA with fully-/weakly-supervised and zero-shot methods .
- This indicates that, compared to previous methods that generate image- and region-level captions, our method establishes dense and precise correspondences between text and 3D points by taking 2D ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
