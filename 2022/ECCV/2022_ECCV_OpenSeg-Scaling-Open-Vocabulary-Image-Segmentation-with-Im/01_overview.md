# Scaling Open-Vocabulary Image Segmentation with Image-Level Labels

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2112.12143.
> PDF retrieval source: https://arxiv.org/pdf/2112.12143. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ECCV
- Authors: Golnaz Ghiasi, Xiuye Gu, Yin Cui, Tsung-Yi Lin
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, semantic, open-vocabulary, segmentation
- Official paper: https://arxiv.org/abs/2112.12143
- Full-text retrieval: https://arxiv.org/pdf/2112.12143
- Code/Project: https://github.com/tensorflow/tpu/tree/master/models/official/detection/projects/openseg
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf)

## Why This Paper Is Here

OpenSeg는 물체 영역을 제안하는 과정과 영역을 텍스트 어휘에 연결하는 과정을 나누어 개방 어휘 영상 분할을 학습한다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf#page=1) · [PDF 5쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf#page=5)

## Problem and Motivation

- **p. 2 / 1 Introduction - extractive body cue:** Image segmentation is an important step to organize an image into a small number of regions in order to understand "what" and "where" are in ...
- **p. 2 / 1 Introduction - extractive body cue:** Each region represents a semantically meaningful entity, which can be a thing (e.g., a chair) or stuff(e.g., floor).
- **p. 2 / 1 Introduction - extractive body cue:** Language is a natural interface to describe what is in an image.
- **p. 2 / 1 Introduction - extractive body cue:** However, semantic segmentation algorithms often only learn with closed-set categories, and thus are unable to recognize concepts outside labeled datasets.
- **p. 2 / 1 Introduction - extractive body cue:** The segmentation model takes text queries as inputs and produces segmented regions accordingly.
- **p. 3 / 1 Introduction - extractive body cue:** Scaling Open-Vocabulary Image Segmentation with Image-Level Labels 3 However, the issue with this approach is in the scalability of training data.
- **p. 3 / 1 Introduction - extractive body cue:** We show that the model can generalize well to other datasets, reaching superior performances compared with prior works on segmentation proposals [3,33].

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** We call our method OpenSeg, standing for open-vocabulary image segmentation.
- **p. 3 / 1 Introduction - extractive body cue:** To evaluate our method, we measure performances on holdout image segmentation datasets.
- **p. 6 / 3 Method - extractive body cue:** 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) [32] for multi-scale feature extraction and a cross-attention ...
- **p. 6 / 3 Method - extractive body cue:** We use a cross-attention module taking inputs as FP E s and a randomly initialized queries q0 ∈RN×D to generate mask queries q ∈RN×D.
- **p. 7 / 3 Method - extractive body cue:** We follow MuST [17] and first train a teacher model on a segmentation dataset with only the segmentation loss LS.
- **p. 8 / 3 Method - extractive body cue:** 3.4 Inference Up to this point, we learn a vision model that predicts segmentation masks s ∈RN×H×W and corresponding features z ∈RN×D.
- **p. 7 / 3 Method - extractive body cue:** Then we annotate a large image-text dataset with pseudo segmentation labels using the teacher model.
- **p. 8 / 3 Method - extractive body cue:** Given an evaluation segmentation dataset, we encode its categories using the text encoder.

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | RGB 영상과 범주 이름. 캡션은 훈련 감독 |
| 표현 | 영역 마스크와 영역별 특징 |
| 출력 | 영상의 의미 분할 마스크 |
| 평가 | 열린 어휘 영상 분할 |

[원문 4쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf#page=4) · [원문 8쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf#page=8)

## Main Claims and Actual Contribution

- 마스크 감독으로 영역을 제안하고 영역 특징과 영상 캡션 단어를 정렬해 영상 수준의 감독을 활용한다. [PDF 5쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf#page=5) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf#page=6) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf#page=7)
- 학습 때의 분할 범주를 넘어 새로운 데이터셋의 이름으로 분할을 평가하고 캡션과 영역별 정렬의 효과를 비교했다. [PDF 9쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf#page=9) · [PDF 10쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf#page=10) · [PDF 13쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf#page=13)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 11 (4 Experiments), p. 12 (4 Experiments) |
| Embodiment/environment | Training Datasets COCO: We use the panoptic segmentation [26] and caption [9] annotations in the 2017 splits which include 118k/5k train/val images. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | Evaluation Datasets PASCAL Context: PASCAL Context [35] includes per-pixel segmentation annotations of object and stuffon 5k/5k train/val images from various indoor and outdoor senses. | role, split, size and leakage | p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 12 (4 Experiments) |
| Metric | 4.2 Predicting Masks Across Datasets We train the segmentation proposal model on COCO and evaluate on COCO and PC-59 with recalls at IoU 50%, 70%, and 90% as metrics. | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Baseline/ablation | Then we discuss the experimental results with our open-vocabulary baselines and state-of-the-art open-vocabulary and zero-shot methods. | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 10 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 5 Conclusion - extractive body cue:** We hope to encourage future works to learn a generalist segmentation model that can transfer across datasets using language as the interface.
- **p. 14 / 4 Experiments - extractive body cue:** The small performance differences across different ways of text filtering show OpenSeg is robust to the noise in the input words to some degree.
- **p. 10 / 4 Experiments - extractive body cue:** Notably, OpenSeg is trained on COCO which does not include underwater scenes.
- **p. 11 / 4 Experiments - extractive body cue:** We find that predictions in the mIoU and Grounding mIoU settings can look quite differently and sometimes mIoU does not correctly reflect the prediction quality ...
- **p. 20 / Figure/Table caption - extractive body cue:** Table 7. OpenSeg is robust to the batch size. We present performance of OpenSeg trained on COCO+Loc. Narr. and different batch sizes. Numbers inside the ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (1 Introduction), p. 6 (3 Method), p. 7 (3 Method), p. 8 (3 Method)이다.

## 검색 태그 근거

영역 마스크를 만들고 해당 영역의 픽셀 특징을 캡션 속 단어와 대응시킨다. 학습용 캡션과 배포 시 질의 클래스 이름을 구분하며 평가 출력은 이미지의 분할 마스크다. [원문 4쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf#page=4) · [원문 8쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136960532.pdf#page=8)
