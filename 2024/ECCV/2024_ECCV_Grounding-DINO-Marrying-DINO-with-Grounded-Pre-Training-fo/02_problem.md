# Problem

- Year/Venue: 2024 / ECCV
- Category: Foundations: Vision Foundation Models
- Tags: Vision Foundation Model, grounding, open-vocabulary
- Paper link: ./2024/ECCV/2024_ECCV_Grounding-DINO-Marrying-DINO-with-Grounded-Pre-Training-fo/paper.pdf
- Code/Project: https://github.com/IDEA-Research/GroundingDINO
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Most existing open-set detectors are developed by extending closed-set detectors to open-set scenarios with language information.

## 해결하려는 문제
- In this paper, we develop an open-set object detector, called Grounding DINO, by marrying Transformer-based detector DINO with grounded pre-training, which can detect arbitrary objects with human inputs ...
- Grounding DINO achieves a 52.5 AP on the COCO zeroshot1 detection benchmark.
- Liu et al. including object detection data, grounding data, and caption data, and evaluate the model on both open-set object detection and referring object detection benchmarks.

## 선행 연구 / 배경 단서
- Most existing open-set detectors are developed by extending closed-set detectors to open-set scenarios with language information.
- Open-Set Detector To help a model Text Encoder align cross-modality information some work Backbone Neck Head tried to fuse features before the final loss Closed-Set Detector stage.
