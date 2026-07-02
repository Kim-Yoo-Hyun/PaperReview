# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Vision, Graph Reasoning
- Paper link: ./2024/ECCV/2024_ECCV_Heterogeneous-Graph-Learning-for-Scene-Graph-Prediction-in/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 3RScan

## Metrics
- accuracy

## Evaluation Protocol and Results
- 4.1 Experimental Settings 3DSSG Dataset The 3DSSG dataset is an extension of 3RScan , providing annotations for 3D semantic scene graphs within the 3RScan dataset.
- It includes 1,482 3D reconstructed models of 478 indoor environments.
- The 1,482 scene graphs have a total of 48k object nodes and 544k edges.
- For a fair comparison, we split the 1,482 scenes into 3852 sub-scenes for the training set and 548 for the test set in the same way as KISGP ...
- Extensive experiments show that our method achieves comparable or superior performance to existing methods on 3DSSG dataset.

## Baselines
- For a fair comparison, we split the 1,482 scenes into 3852 sub-scenes for the training set and 548 for the test set in the same way as KISGP ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
