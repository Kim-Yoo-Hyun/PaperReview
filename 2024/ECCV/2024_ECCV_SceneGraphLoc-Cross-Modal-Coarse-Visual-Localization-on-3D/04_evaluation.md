# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Vision, Graph Reasoning
- Paper link: ./2024/ECCV/2024_ECCV_SceneGraphLoc-Cross-Modal-Coarse-Visual-Localization-on-3D/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- 3RScan

## Metrics
- accuracy
- mAP

## Evaluation Protocol and Results
- For comparison with state-of-the-art visual localization methods requiring large image databases, we included CVNet and AnyLoc .
- With images, SceneGraphLoc achieves performance close to that of state-of-the-art techniques depending on large image databases, while requiring three orders-of-magnitude less storage and operating orders-of-magnitude faster.
- For comparison with state-of-the-art visual localization methods requiring large image databases, we included CVNet and AnyLoc .

## Baselines
- No existing methods directly tackle our task, but several recent advancements provide relevant baselines.
- We also explored open-vocabulary object-retrieval-based baselines using OpenMask3D and OpenSeg , with OpenMask3D assigning CLIP descriptors to 3D object instances from multiple observing images, and OpenSeg extracting pixel-level ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
