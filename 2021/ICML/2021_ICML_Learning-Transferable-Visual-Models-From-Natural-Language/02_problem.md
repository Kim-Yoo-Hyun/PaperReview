# Problem

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2021 / ICML
- Category: Foundations: Vision and Language Models
- Tags: CLIP, Vision-Language Model, alignment
- Paper link: ./2021/ICML/2021_ICML_Learning-Transferable-Visual-Models-From-Natural-Language/paper.pdf
- Code/Project: https://github.com/openai/CLIP
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and ...

## 해결하려는 문제
- We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch ...
- For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on.
- After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks.

## 선행 연구 / 배경 단서
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.
