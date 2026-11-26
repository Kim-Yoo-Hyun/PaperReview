# Language-driven Semantic Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2201.03546.
> PDF retrieval source: https://arxiv.org/pdf/2201.03546. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ICLR
- Authors: Boyi Li, Kilian Q. Weinberger, Serge Belongie, Vladlen Koltun, René Ranftl
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, semantic, open-vocabulary, alignment, segmentation
- Official paper: https://arxiv.org/abs/2201.03546
- Full-text retrieval: https://arxiv.org/pdf/2201.03546
- Code/Project: https://github.com/isl-org/lang-seg
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

LSeg는 영상의 각 위치에 대해 주어진 텍스트 레이블과의 대응을 계산해 의미 분할한다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We present LSeg, a novel model for language-driven semantic image segmentation.
- **p. 1 / ABSTRACT - extractive body cue:** LSeg uses a text encoder to compute embeddings of descriptive input labels (e.g., "grass" or "building") together with a transformer-based image encoder that computes dense ...
- **p. 1 / ABSTRACT - extractive body cue:** The image encoder is trained with a contrastive objective to align pixel embeddings to the text embedding of the corresponding semantic class.
- **p. 1 / ABSTRACT - extractive body cue:** The text embeddings provide a flexible label representation in which semantically similar labels map to similar regions in the embedding space (e.g., "cat" and "furry").
- **p. 1 / ABSTRACT - extractive body cue:** This allows LSeg to generalize to previously unseen categories at test time, without retraining or even requiring a single additional training sample.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The main reason for the restricted label sets in existing methods is the cost of annotating images to produce sufficient training data.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Since the text encoder is trained to embed closely related concepts near one another (for example, "dog" is closer to "pet" than to "vehicle"), we ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our approach enables the synthesis of zero-shot semantic segmentation models on the fly.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work, we present a simple approach to leveraging modern language models to increase the flexibility and generality of semantic segmentation models.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose to use state-of-the-art text encoders that have been co-trained on visual data, such as CLIP, to embed labels from the training set into ...
- **p. 1 / ABSTRACT - extractive body cue:** We present LSeg, a novel model for language-driven semantic image segmentation.
- **p. 5 / C Input Label Set - extractive body cue:** In contrast, our approach can dynamically handle label sets with varying length, content, and order.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Since the text encoder is trained to embed closely related concepts near one another (for example, "dog" is closer to "pet" than to "vehicle"), we ...
- **p. 4 / C Input Label Set - extractive body cue:** We use an additional post-processing module that spatially regularizes and upsamples the predictions to the original input resolution.
- **p. 1 / ABSTRACT - extractive body cue:** The image encoder is trained with a contrastive objective to align pixel embeddings to the text embedding of the corresponding semantic class.

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | RGB 이미지와 범주 텍스트 |
| 표현 | 픽셀과 텍스트의 공통 특징 공간 |
| 출력 | 픽셀별 의미 범주 |
| 평가 | 열린 어휘 이미지 의미 분할 |

[원문 3쪽](https://arxiv.org/pdf/2201.03546#page=3) · [원문 6쪽](https://arxiv.org/pdf/2201.03546#page=6)

## Main Claims and Actual Contribution

- 영상 특징을 텍스트 인코더의 레이블 표현과 정렬한다.
- 학습 시 고정된 클래스 밖의 텍스트 레이블로도 영역을 지정한다.

[저자 원문](https://arxiv.org/abs/2201.03546)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Embodiment/environment | However, due to a lack of a standardized protocol and sufficient datasets and baselines for the zero-shot setting, we compare LSeg to zero- and few-shot semantic segmentation models on few-shot benchmarks. | hardware/simulator version and reset protocol | p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Dataset/benchmark | It contains a significant number of unseen or unannotated objects in comparison to previous datasets such as PASCAL and COCO. | role, split, size and leakage | p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Metric | Note that few-shot methods have access to more information and are thus expected to yield higher accuracy. | definition, denominator, direction and uncertainty | p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Baseline/ablation | Our model (with the same ResNet101 backbone) outperforms the zero-shot baseline by a considerable margin across folds and datasets and is even competitive with several few-shot methods. | fair input/data/compute/action matching | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** We hope that these failure cases can inform future work, which could involve augmenting training with negative samples or building fine-grained language-driven semantic segmentation models ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** While LSeg in general achieves very promising results, we also observe some failure cases, as illustrated in Figure 6.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Example results. LSeg is able to handle unseen labels as well as label sets of arbitrary length and order. This enables flexible synthesis ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (C Input Label Set)이다.

## 검색 태그 근거

이미지의 각 픽셀 특징과 입력 범주 이름을 임베딩한 특징을 비교해 의미 분할한다. PASCAL-5i와 COCO-20i 등을 사용해 학습 시 보지 않은 범주를 평가했다. [원문 3쪽](https://arxiv.org/pdf/2201.03546#page=3) · [원문 6쪽](https://arxiv.org/pdf/2201.03546#page=6)
