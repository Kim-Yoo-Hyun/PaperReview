# Evaluation

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Spatial-Understanding-from-Videos-Structured-Prompts-Meet/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- 3RScan
- Objaverse
- HM3D
- SQA3D
- ScanQA

## Metrics
- BLEU
- accuracy
- mAP

## Evaluation Protocol and Results
- Across all models, a consistent trend emerges: the +Des variant outperforms others, followed by 7
- The experimental settings (including benchmarks, baselines, etc.) and more experimental results can be found in the Appendix A and B.
- Extensive experiments across multiple benchmarks demonstrate the individual and combined effectiveness of our prompting and fine-tuning strategies, and yield insights that may inspire future research on visual-spatial understanding.
- Across all models, a consistent trend emerges: the +Des variant outperforms others, followed by 7

## Baselines
- The experimental settings (including benchmarks, baselines, etc.) and more experimental results can be found in the Appendix A and B.
- 5.1 Performace Comparison We investigated the following five key questions to assess our approach: Q1: Which scene representation format is most interpretable by VLMs?

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
