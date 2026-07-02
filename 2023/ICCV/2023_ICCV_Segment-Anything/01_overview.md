# Segment Anything

- Year/Venue: 2023 / ICCV
- Category: Foundations: Vision Foundation Models
- Tags: segmentation, foundation model, prompting
- Paper link: ./2023/ICCV/2023_ICCV_Segment-Anything/paper.pdf
- Code/Project: https://github.com/facebookresearch/segment-anything
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- With this model, we aim to solve a range of downstream segmentation problems on new data distributions using prompt engineering.
- While much progress has been made on vision and language encoders, computer vision includes a wide range of problems beyond this scope, and for many of these, abundant ...

## Core Idea
- To develop them, we address the following questions about image segmentation: We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation.
- While much progress has been made on vision and language encoders, computer vision includes a wide range of problems beyond this scope, and for many of these, abundant ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We evaluate its capabilities on numerous tasks and find that its zero-shot performance is impressive – often competitive with or even superior to prior fully supervised results.
- Empirical trends show this behavior improving with model scale, dataset size, and total training compute .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- While much progress has been made on vision and language encoders, computer vision includes a wide range of problems beyond this scope, and for many of these, abundant ...
- Empirical trends show this behavior improving with model scale, dataset size, and total training compute .
- To develop them, we address the following questions about image segmentation: We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation.

## Abstract Cue
- matching in some cases) fine-tuned models .
