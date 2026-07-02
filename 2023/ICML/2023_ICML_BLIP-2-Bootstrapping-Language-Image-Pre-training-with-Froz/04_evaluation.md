# Evaluation

- Year/Venue: 2023 / ICML
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, LLM, alignment
- Paper link: ./2023/ICML/2023_ICML_BLIP-2-Bootstrapping-Language-Image-Pre-training-with-Froz/paper.pdf
- Code/Project: https://github.com/salesforce/LAVIS
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- COCO

## Metrics
- BLEU

## Evaluation Protocol and Results
- BLIP-2 achieves state-of-the-art performance on various visionlanguage tasks, despite having significantly fewer trainable parameters than existing methods.
- For example, our model outperforms Flamingo80B by 8.7% on zero-shot VQAv2 with 54x fewer trainable parameters.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
