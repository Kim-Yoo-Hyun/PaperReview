# Evaluation

- Year/Venue: 2022 / ICML
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, alignment, generation
- Paper link: ./2022/ICML/2022_ICML_BLIP-Bootstrapping-Language-Image-Pre-training-for-Unified/paper.pdf
- Code/Project: https://github.com/salesforce/BLIP
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- COCO

## Metrics
- BLEU
- accuracy

## Evaluation Protocol and Results
- We achieve state-of-the-art results on a wide range of vision-language tasks, such as image-text retrieval (+2.7% in average recall@1), image captioning (+2.8% in CIDEr), and VQA (+1.6% in ...
- Furthermore, performance improvement has been largely achieved by scaling up the dataset with noisy image-text pairs collected from the web, which is a suboptimal source of supervision.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
