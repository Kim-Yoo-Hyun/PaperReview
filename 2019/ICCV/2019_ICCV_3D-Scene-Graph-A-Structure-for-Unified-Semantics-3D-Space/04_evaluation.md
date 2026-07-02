# Evaluation

- Year/Venue: 2019 / ICCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Scene Graph, semantic, geometry, Graph Reasoning
- Paper link: ./2019/ICCV/2019_ICCV_3D-Scene-Graph-A-Structure-for-Unified-Semantics-3D-Space/paper.pdf
- Code/Project: https://3dscenegraph.stanford.edu/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- COCO
- ScanNet
- Matterport3D

## Metrics
- accuracy
- AP
- mAP

## Evaluation Protocol and Results
- obj1 obj1 obj2 (0.8, 0.3, - 0.1) obj2 0.85 obj2 class: bed color: blue, brown material: wood, fabric area: 2.2 m2 shape: prism rectangular action affordance: sit on, ...
- Introduction B1 Where should semantic information be grounded and what structure should it have to be most useful and invariant?

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
