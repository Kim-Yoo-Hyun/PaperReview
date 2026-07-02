# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, Diffusion, semantic
- Paper link: ./2024/ECCV/2024_ECCV_Open-Vocabulary-3D-Semantic-Segmentation-with-Text-to-Imag/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- ScanNet200
- Matterport3D
- Replica
- Nr3D

## Metrics
- mIoU
- mAP

## Evaluation Protocol and Results
- We conduct a series of experiments to demonstrate the effectiveness of Diff2Scene on a variety of zero-shot 3D scene understanding benchmarks.
- We train our 3D branch using the images in the training splits and report the results on test split.
- Finally, we qualitatively demonstrate the strong ability of the proposed model for open-vocabulary 3D segmentation and grounding complicated compositional text queries.
- We first evaluate the proposed model on zero-shot open-vocabulary semantic segmentation tasks following the evaluation protocol of .
- We show that it outperforms competitive baselines and achieves significant improvements over state-of-the-art methods.
- In particular, Diff2Scene improves the state-of-the-art method on ScanNet200 by 12%.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
