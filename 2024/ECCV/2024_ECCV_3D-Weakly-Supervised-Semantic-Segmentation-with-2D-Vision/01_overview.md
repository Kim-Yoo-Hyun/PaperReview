# 3D Weakly Supervised Semantic Segmentation with 2D Vision-Language Guidance

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9223_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: Xiaoxu Xu, Yitian Yuan, Jinlong Li, Qiudan Zhang, Zequn Jie, Lin Ma, Hao Tang, Nicu Sebe, Xu Wang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision, semantic
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9223_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf)

## Why This Paper Is Here

3DSS-VLG는 점별 정답 라벨을 구하는 부담을 줄이기 위해 2D 시각·언어 모델과 장면 단위 범주 라벨로 3D 의미 분할을 학습한다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf#page=1) · [PDF 4쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf#page=4)

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** 3D point cloud semantic segmentation [13, 16, 27-29, 43] can provide valuable geometric and semantic data about the 3D environment and has gained considerable attention ...
- **p. 2 / X. Xu et al - extractive body cue:** Therefore, how to design a network that achieves good performance despite the lack of 2D anno
- **p. 2 / X. Xu et al - extractive body cue:** Given the simple GAP connectivity structure, these methods can easily identify the importance of each point by projecting back the output classification weight onto the ...
- **p. 3 / X. Xu et al - extractive body cue:** 3DSS with 2D Vision-Language Guidance 3 tations still remains a big challenge.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Specifically, our method exploits the superior generalization ability of the 2D visionlanguage models and proposes the Embeddings Soft-Guidance Stage to utilize it to implicitly align ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Moreover, with extensive quantitative and qualitative experiments, we present that our 3DSS-VLG is able not only to achieve the state-ofthe-art performance on both S3DIS and ...

## Core Idea

- **p. 4 / X. Xu et al - extractive body cue:** In summary, the main contributions of this paper are as follows: - We propose a weakly supervised method 3DSS-VLG for 3D WSSS, which takes 2D ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Moreover, we introduce the Embeddings Specialization Stage to purify the feature representation with the help of a given scene-level label, specifying a better feature supervised ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Specifically, our method exploits the superior generalization ability of the 2D visionlanguage models and proposes the Embeddings Soft-Guidance Stage to utilize it to implicitly align ...
- **p. 3 / X. Xu et al - extractive body cue:** Therefore, we propose to alleviate this problem by three stages.
- **p. 3 / X. Xu et al - extractive body cue:** 3 (a), we propose the Embeddings Specialization Stage, which transfers the 2D-projected embeddings with an adapter module to obtain adapted 3D embeddings, and the
- **p. 2 / X. Xu et al - extractive body cue:** Point clouds are first processed by several Multi-Layer Perception (MLP) layers and thus get a point cloud feature map, and then this point cloud feature ...
- **p. 8 / X. Xu et al - extractive body cue:** Finally, we use the pseudo labels Y to supervise the model, and the green dashed lines denote back-propagation of the loss La.
- **p. 3 / X. Xu et al - extractive body cue:** We first process these multi-view images using the image encoder of the pretrained off-the-shelf 2D OVSS model such as Openseg [12] to get the 2D ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Moreover, we propose Embeddings Specialization Stage to make the embedding space to be more robust based on the pseudo label filtering with indoor point cloud scene knowledge. - Extensive experiments on the ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (X. Xu et al), p. 3 (X. Xu et al) |
| State/latent | Moreover, Embeddings, Specialization, Stage, make, embedding, space, more, robust, pseudo, label, filtering | geometry, map, object/relationship state | p. 4 (X. Xu et al), p. 3 (X. Xu et al), p. 6 (X. Xu et al) |
| Output/action | Specifically, for the input 3D point cloud, the dataset also provides a set of multi-view images corresponding to it. | point map, pose, scene graph, affordance 또는 query result | p. 3 (X. Xu et al), p. 6 (X. Xu et al), p. 6 (X. Xu et al) |
| Objective/outcome | The red dashed lines denote back-propagation of the loss Ls. a classification cross-entropy loss La is introduced to supervise the procedure. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 8 (X. Xu et al), p. 8 (X. Xu et al) |

## Main Claims and Actual Contribution

- 동결한 영상 모델의 특징을 점군에 역투영해 텍스트 표현과 정렬하고 해당 장면에 존재하는 범주 정보로 감독 신호를 정제한다. [PDF 5쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf#page=5) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf#page=6) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf#page=7)
- S3DIS와 ScanNet에서 약지도 분할을 비교하고 영상 특징과 텍스트 범주를 이용하는 각 학습 단계의 영향을 평가했다. [PDF 10쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf#page=10) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf#page=11) · [PDF 13쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf#page=13)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 12 (Figure/Table caption) |
| Embodiment/environment | We adopt the default train-val split setting, where there are 1201 training scenes and 312 validation scenes. | hardware/simulator version and reset protocol | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | We adopt the default train-val split setting, where there are 1201 training scenes and 312 validation scenes. | role, split, size and leakage | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Metric | We reduce the learning rate by a multiplying factor of 0.7 every 20 epochs for a total of 80 epochs. | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 9 (4 Experiments), p. 6 (Figure/Table caption) |
| Baseline/ablation | The competing methods are then presented and compared. | fair input/data/compute/action matching | p. 9 (4 Experiments), p. 14 (Figure/Table caption), p. 9 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 13 / 5 Conclusion - extractive body cue:** In this paper, we propose 3DSS-VLG to address the shortage of point-level annotations.
- **p. 13 / 5 Conclusion - extractive body cue:** Specifically, our 3DSS-VLG exploits the superior ability of current vision-language models on aligning the semantics between texts and 2D images, as well as the naturally ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (X. Xu et al), p. 3 (X. Xu et al), p. 1 (Body text (section not recovered))이다.
