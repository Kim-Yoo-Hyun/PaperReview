# Evaluation

- Year/Venue: 2023 / NeurIPS
- Category: 3D Large Multimodal Models
- Tags: LLM, 3D Vision, Vision-Language
- Paper link: ./2023/NeurIPS/2023_NeurIPS_3D-LLM-Injecting-the-3D-World-into-Large-Language-Models/paper.pdf
- Code/Project: https://vis-www.cs.umass.edu/3dllm/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- Objaverse
- Habitat
- HM3D
- ScanRefer
- ScanQA

## Metrics
- BLEU
- mAP

## Evaluation Protocol and Results
- For example, for BLEU-1, our model outperforms the state-of-the-art ScanQA model by ∼9% for validation set and ∼7% for test set.
- Particularly, ScanQA is the state-of-the-art method on the benchmark that uses VoteNet to obtain object proposals, and then fuse them with language embeddings.
- These results show that by injecting 3D into LLMs, the models can generate answers that are much more similar to the ground-truth answers.
- Result Analysis We report our results on ScanQA validation set in Table 1, and results on test set in Table 2.
- Experiments on ScanQA show that our model outperforms state-of-the-art baselines by a large margin (e.g., the BLEU-1 score surpasses state-of-the-art score by 9%).
- Furthermore, experiments on our held-in datasets for 3D captioning, task composition, and 3D-assisted dialogue show that our model outperforms 2D VLMs.

## Baselines
- 5.1 Held-Out Evaluation We finetune our pretrained 3D-LLMs on the ScanQA dataset and compare with baseline models.
- For CIDER, we report a ∼5% gain compared to ScanQA, and much higher than other 3D-based baselines.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
