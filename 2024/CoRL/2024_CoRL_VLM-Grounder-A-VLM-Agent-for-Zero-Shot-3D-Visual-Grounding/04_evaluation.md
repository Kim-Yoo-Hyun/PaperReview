# Evaluation

- Year/Venue: 2024 / CoRL
- Category: 3D Vision-Language Grounding
- Tags: 3D visual grounding, VLM, zero-shot
- Paper link: ./2024/CoRL/2024_CoRL_VLM-Grounder-A-VLM-Agent-for-Zero-Shot-3D-Visual-Grounding/paper.pdf
- Code/Project: https://github.com/InternRobotics/VLM-Grounder
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- ScanRefer
- ReferIt3D
- Nr3D

## Metrics
- accuracy
- IoU
- mAP
- Chamfer

## Evaluation Protocol and Results
- We report the performance of the baselines from their original papers, and the results on the same 250 validation samples are provided in the supplementary material.
- For our experiments, we sample one frame from every 20 frames of the original ScanNet image sequences.
- The ScanRefer benchmark requires predicting the 3D bounding box of the target object from scene point clouds and queries.
- In contrast, the Nr3D benchmark provides ground truth bounding boxes (without class labels) for all objects, focusing on top-1 accuracy in selection.
- Experiments on ScanRefer and Nr3D datasets show VLM-Grounder outperforms previous zero-shot methods, achieving 51.6% Acc@0.25 on ScanRefer and 48.0% Acc on Nr3D, without relying on 3D geometry or ...
- We report the performance of the baselines from their original papers, and the results on the same 250 validation samples are provided in the supplementary material.

## Baselines
- We report the performance of the baselines from their original papers, and the results on the same 250 validation samples are provided in the supplementary material.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
