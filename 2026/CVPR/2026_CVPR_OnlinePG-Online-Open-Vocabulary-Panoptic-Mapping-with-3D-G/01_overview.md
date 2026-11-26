# OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Hongjia Zhai, Qi Zhang, Xiaokun Pan, Xiyu Zhang, Yitong Dong, Huaqi Zhang, Dan Xu, Guofeng Zhang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, semantic mapping, open-vocabulary, 3D segmentation
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf)

## Why This Paper Is Here

OnlinePG는 RGB-D 시퀀스로부터 기하·의미·인스턴스를 온라인으로 누적해 자연어로 질의할 수 있는 가우시안 지도를 만든다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary scene understanding with online panoptic mapping is essential for embodied applications to perceive and interact with environments.
- **p. 1 / Abstract - extractive body cue:** However, existing methods are predominantly offline or lack instance-level understanding, limiting their applicability to real-world robotic tasks.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose OnlinePG, a novel and effective system that integrates geometric reconstruction and open-vocabulary perception using 3D Gaussian Splatting in an online ...
- **p. 1 / Abstract - extractive body cue:** Technically, to achieve online panoptic mapping, we employ an efficient local-to-global paradigm with a sliding window.
- **p. 1 / Abstract - extractive body cue:** To build local consistency map, we construct a 3D segment clustering graph that jointly leverages geometric and semantic cues, fusing inconsistent segments within sliding window ...
- **p. 1 / 1. Introduction - extractive body cue:** However, these approaches are predominantly offline and lack support for online instance-level panoptic perception, hindering their applications in embodied tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Current online open-vocabulary scene understanding approaches [42, 52] cannot distinguish individual 3D instances based on text queries, while offline instanceaware approaches [19, 39, 50, 58] ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Overall, the technical contributions of our approach are summarized as follows: • We propose an online open-vocabulary panoptic mapping framework that unifies geometric reconstruction and ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we present OnlinePG, an efficient online open-vocabulary panoptic mapping system based on 3D Gaussian Splatting that integrates geometric reconstruction with semantic understanding.
- **p. 3 / 3. Method - extractive body cue:** To mitigate the inconsistencies of 2D segmentation results, we propose an effective segment clustering algorithm that synergistically leverages geometric and semantic cues to obtain consistent ...
- **p. 3 / 3.2. Local Consistent Map Construction - extractive body cue:** For i-th keyframe inside the sliding window W, we use LSeg [17] and EntitySeg [21] to extract its 2D feature map fi ∈RH×W ×Df and ...
- **p. 4 / 3.2. Local Consistent Map Construction - extractive body cue:** The semantic cue is then computed as the cosine similarity between language features: X(Si, Sj) = zi · zj/(//zi// · //zj//).
- **p. 4 / 3.2. Local Consistent Map Construction - extractive body cue:** Through this multi-cue graph clustering algorithm, we obtain geometrically and semantically consistent 3D Gaussian instances I from the local sliding window.
- **p. 5 / 3.3. Local-to-Global Map Fusion - extractive body cue:** For each voxel v occupied by a clustered instance I, we update the global feature grid Ft g and confidence grid Ct g using weighted ...
- **p. 5 / 3.3. Local-to-Global Map Fusion - extractive body cue:** construct a forward correspondence score matrix Ml→g ∈ Rnl×ng: Ml→g = zl · zg //zl// · //zg// + /Il ∩Ig/ Cont.(Il, Ig), (10) where nl ...

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | RGB-D 스트림과 텍스트 조회 |
| 표현 | 지역 관측을 정합한 가우시안 인스턴스 지도 |
| 출력 | 온라인 파놉틱 지도와 조회 영역 |
| 평가 | ScanNetV2·Replica 열린 어휘 분할 |

[원문 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf#page=3) · [원문 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf#page=7)

## Main Claims and Actual Contribution

- 슬라이딩 윈도 안의 분할을 기하·의미 그래프로 모으고 양방향 이분 매칭으로 지역 인스턴스를 전역 지도에 연결한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf#page=5)
- 격자에 합친 시각언어 특징으로 개방 어휘 의미와 인스턴스를 평가하고 온라인 지도 작성의 처리 시간을 비교했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.3. Ablation Studies), p. 6 (4.2. Main Experiments) |
| Embodiment/environment | Following [50, 58], we take the commonly-used 8 scenes {room0-2,office0-4} for Replica dataset. | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings) |
| Dataset/benchmark | For Scene0645 in the ScanNetV2 dataset, our method takes an average of 410 ms to perform rendering optimization for 5 keyframes with 20 iterations, 350 ms for clustering the 12 keyframes in ... | role, split, size and leakage | p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings), p. 7 (4.2. Main Experiments), p. 6 (4.1. Experimental Settings) |
| Metric | 2, we show the performance of different matching strategies for fusing local map from the sliding window into global map. #1 represents using the basic nearest neighbor matching algorithm based on the ... | definition, denominator, direction and uncertainty | p. 8 (4.3. Ablation Studies), p. 5 (4.1. Experimental Settings), p. 8 (4.3. Ablation Studies) |
| Baseline/ablation | Figure 3. Qualitative 3D Semantic Segmentation Comparison of ScanNetV2 Dataset. Our approach outperforms recent online ap- proaches, O2V-Mapping [42] and OnlineAnySeg [41], by a large margin. Compared with the offline SOTA PanoGS ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 7 (4.2. Main Experiments), p. 7 (4.2. Main Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Limitations: (1) Our method currently cannot reconstruct dynamic objects.
- **p. 8 / 5. Conclusion - extractive body cue:** Our future work will explore feed-forward approaches [20, 46, 47] that eliminate these requirements for fully pose-free and depth-free openvocabulary reconstruction.
- **p. 5 / 4.1. Experimental Settings - extractive body cue:** Since the baselines [31, 33, 50] marked with ∗ cannot obtain 3D panoptic results, we use the performance reported in [58], which uses a supervised ...
- **p. 7 / 4.2. Main Experiments - extractive body cue:** While OnlineAnySeg can handle simple queries (e.g., "television"), it fails on some fine-grained and multi-instance queries (e.g., "pillow", "toilet paper", "bag") due to inaccurate 3D ...
- **p. 7 / 4.2. Main Experiments - extractive body cue:** Since some offline baselines (LangSplat [33], OpenGaussian [50], OpenScene [31]) marked with ∗cannot inherently output 3D instances, PanoGS [58] provides supervised instance annotations [44] for ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of OnlinePG, which integrates geometric reconstruction and open-vocabulary panoptic perception built upon 3D Gaussian Splatting. Given the posed video stream and 2D ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Local Consistent Map Construction), p. 3 (3. Method)이다.

## 검색 태그 근거

RGB-D 스트림의 깊이로 가우시안을 초기화하고, 슬라이딩 윈도에서 만든 인스턴스 지도를 전역 지도와 대응시킨다. 텍스트가 지정하는 범주와 개별 물체 영역을 질의한다. [원문 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf#page=3) · [원문 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf#page=7)
