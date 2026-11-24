# Detecting Twenty-thousand Classes using Image-level Supervision

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2201.02605.
> PDF retrieval source: https://arxiv.org/pdf/2201.02605. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ECCV
- Authors: Xingyi Zhou, Rohit Girdhar, Armand Joulin, Philipp Krähenbühl, Ishan Misra
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, open-vocabulary, detection, semantic
- Official paper: https://arxiv.org/abs/2201.02605
- Full-text retrieval: https://arxiv.org/pdf/2201.02605
- Code/Project: https://github.com/facebookresearch/Detic
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136690344.pdf)

## Why This Paper Is Here

Detic은 상자 주석이 있는 검출 자료와 영상 전체의 범주만 아는 자료를 함께 사용해 검출기의 분류 어휘를 확장한다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136690344.pdf#page=1) · [PDF 5쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136690344.pdf#page=5)

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Object detection consists of two sub-problems - finding the object (localization) and naming it (classification).
- **p. 1 / 1 Introduction - extractive body cue:** Traditional methods tightly couple these two subproblems and thus rely on box labels for all classes.
- **p. 1 / 1 Introduction - extractive body cue:** Despite many data collection efforts, detection datasets [18, 28, 34, 49] are much smaller in overall size and vocabularies than classification datasets [10].
- **p. 1 / 1 Introduction - extractive body cue:** For example, the recent LVIS detection dataset [18] has 1000+ classes with 120K images; OpenImages [28] has 500 classes in 1.8M images.
- **p. 1 / 1 Introduction - extractive body cue:** Moreover, not all classes contain sufficient annotations to train a robust detector (see Figure 1 Top).
- **p. 5 / 3 Preliminaries - extractive body cue:** In our experiments, the proposal network and the bounding box regressors are not the current performance bottleneck, as modern detectors use an over-sufficient number of ...
- **p. 1 / 1 Introduction - extractive body cue:** We observe that the localization and classification sub-problems can be decoupled.

## Core Idea

- **p. 2 / X. Zhou et al - extractive body cue:** This also enables our method to learn detectors for new classes which would have been impossible to predict and assign.
- **p. 1 / 1 Introduction - extractive body cue:** Object detection consists of two sub-problems - finding the object (localization) and naming it (classification).
- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we propose Detector with image classes (Detic) that uses image-level supervision in addition to detection supervision.
- **p. 2 / X. Zhou et al - extractive body cue:** Experiments on the open-vocabulary LVIS [17, 18] and the open-vocabulary COCO [2] benchmarks show that our method can significantly improve over a strong box-supervised baseline, ...
- **p. 3 / X. Zhou et al - extractive body cue:** Our contributions are summarized below: - We identify issues and propose a simpler alternative to existing weaklysupervised detection techniques in the open-vocabulary setting. - Our ...
- **p. 2 / X. Zhou et al - extractive body cue:** We propose a simple classification loss that applies the image-level supervision to the proposal with the largest size, and do not supervise other outputs for ...
- **p. 5 / 3 Preliminaries - extractive body cue:** We use the region proposal network to extract N object features {(b, f, o)j}N j=1.
- **p. 6 / X. Zhou et al - extractive body cue:** We then apply the classification loss to its RoI features f ′ for all classes c ∈{ck}K k=1: Limage-box = BCE(Wf ′, c) where BCE(s, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We propose a simple classification loss that applies the image-level supervision to the proposal with the largest size, and do not supervise other outputs for imagelabeled data. | camera/depth stream, pose, map와 language goal | p. 2 (X. Zhou et al), p. 5 (3 Preliminaries) |
| State/latent | simple, classification, loss, applies, image-level, supervision, proposal, largest, size, supervise, other, outputs | robot pose, free-space/semantic map와 local goal | p. 2 (X. Zhou et al), p. 5 (3 Preliminaries), p. 4 (3 Preliminaries) |
| Output/action | The second stage takes the object feature and outputs a classification score and a refined box location for each object, sj = Wfj, ˆbj = Bfj + bj, where W ∈R/Cdet/×D and ... | collision-free trajectory 또는 velocity command | p. 5 (3 Preliminaries), p. 4 (3 Preliminaries), p. 5 (3 Preliminaries) |
| Objective/outcome | Equalization losses [55, 56] and SeeSaw loss [64] reweights the per-class loss by balancing the gradients [55] or number of samples [64]. | goal reach, safety, localization error와 replanning latency | p. 4 (X. Zhou et al), p. 6 (X. Zhou et al), p. 6 (X. Zhou et al) |

## Main Claims and Actual Contribution

- 영상 수준 라벨의 분류 손실을 가장 큰 제안 영역에 적용해 상자 주석이 없는 범주의 분류기를 학습한다. [PDF 5쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136690344.pdf#page=5) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136690344.pdf#page=6)
- ImageNet 계열의 영상 수준 감독을 추가한 뒤 LVIS 등에서 새로운 범주 검출과 다른 자료로의 전이를 평가했다. [PDF 9쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136690344.pdf#page=9) · [PDF 10쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136690344.pdf#page=10) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136690344.pdf#page=11)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 13 (Figure/Table caption), p. 26 (Figure/Table caption) |
| Embodiment/environment | We evaluate Detic on the large-vocabulary object detection dataset LVIS [18]. | hardware/simulator version and reset protocol | p. 7 (5 Experiments), p. 7 (5 Experiments) |
| Dataset/benchmark | We evaluate Detic on the large-vocabulary object detection dataset LVIS [18]. | role, split, size and leakage | p. 7 (5 Experiments), p. 7 (5 Experiments) |
| Metric | Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, 45] use image-level labels by assigning them to ... | definition, denominator, direction and uncertainty | p. 3 (Figure/Table caption), p. 5 (Figure/Table caption), p. 11 (Figure/Table caption) |
| Baseline/ablation | Table 11: Ablations of the resolution change. We report mask mAP on the open- vocabulary LVIS following the setting of Table 1. Top: ImageNet as the image-labeled data. Bottom: CC as the ... | fair input/data/compute/action matching | p. 22 (Figure/Table caption), p. 11 (Figure/Table caption), p. 3 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, 45] ...
- **p. 13 / X. Zhou et al - extractive body cue:** By default, a trained classifier cannot recognize novel classes.
- **p. 14 / X. Zhou et al - extractive body cue:** 6 Limitations and Conclusions We present Detic which is a simple way to use image supervision in largevocabulary object detection.
- **p. 14 / X. Zhou et al - extractive body cue:** We leave incorporating such information for future work.
- **p. 12 / X. Zhou et al - extractive body cue:** Compared to the Box-Supervised baseline (trained on LVIS-all), Detic leverages image-level supervision to train robust detectors.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 5 (3 Preliminaries), p. 1 (1 Introduction), p. 4 (3 Preliminaries), p. 2 (X. Zhou et al)이다.
