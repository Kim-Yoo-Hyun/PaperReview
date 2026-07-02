# Evaluation

- Year/Venue: 2023 / NeurIPS
- Category: Open-Vocabulary 3D Mapping
- Tags: open-vocabulary, 3D segmentation, CLIP
- Paper link: ./2023/NeurIPS/2023_NeurIPS_OpenMask3D-Open-Vocabulary-3D-Instance-Segmentation/paper.pdf
- Code/Project: https://openmask3d.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- ScanNet200
- Replica
- LERF

## Metrics
- accuracy
- AP

## Evaluation Protocol and Results
- 4.1 Quantitative results: closed-vocabulary 3D instance segmentation evaluation We evaluate our approach on the closed-vocabulary 3D instance segmentation task.
- We report our ScanNet200 results on the validation set consisting of 312 scenes, and evaluate for the 3D instance segmentation task using the closed vocabulary of 200 categories ...
- In this section, we present quantitative and qualitative results from our method OpenMask3D.
- 4.2, we share qualitative results for open-vocabulary 3D instance segmentation, demonstrating potential applications.
- Experiments and ablation studies on ScanNet200 and Replica show that OpenMask3D outperforms other open-vocabulary methods, especially on the long-tail distribution.
- 4.1 Quantitative results: closed-vocabulary 3D instance segmentation evaluation We evaluate our approach on the closed-vocabulary 3D instance segmentation task.

## Baselines
- In Sec 4.1, we quantitatively evaluate our method, and compare OpenMask3D with supervised 3D instance segmentation approaches as well as existing open-vocabulary 3D scene understanding models we adapted ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
