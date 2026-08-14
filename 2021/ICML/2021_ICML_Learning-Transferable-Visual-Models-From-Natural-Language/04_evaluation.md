# Evaluation

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2021 / ICML
- Category: Foundations: Vision and Language Models
- Tags: CLIP, Vision-Language Model, alignment
- Paper link: ./2021/ICML/2021_ICML_Learning-Transferable-Visual-Models-From-Natural-Language/paper.pdf
- Code/Project: https://github.com/openai/CLIP
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- COCO
- KITTI

## Metrics
- accuracy
- mAP

## Evaluation Protocol and Results
- State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories.
- We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch ...

## Baselines
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
