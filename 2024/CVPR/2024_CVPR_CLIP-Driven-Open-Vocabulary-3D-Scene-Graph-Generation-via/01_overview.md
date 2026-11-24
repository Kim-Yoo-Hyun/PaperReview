# CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Lianggangxu Chen, Xuejiao Wang, Jiale Lu, Shaohui Lin, Changbo Wang, Gaoqi He
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Scene Graph, CLIP, Graph Reasoning
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf)

## Why This Paper Is Here

CCL-3DSGG는 점군 장면 그래프의 물체와 관계를 이미지·텍스트 특징에 정렬해 학습 시 보지 못한 범주를 인식한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Scene Graph Generation (3DSGG) aims to classify objects and their predicates within 3D point cloud scenes.
- **p. 1 / Abstract - extractive body cue:** However, current 3DSGG methods struggle with two main challenges.
- **p. 1 / Abstract - extractive body cue:** 1) The dependency on labor-intensive groundtruth annotations.
- **p. 1 / Abstract - extractive body cue:** 2) Closed-set classes training hampers the recognition of novel objects and predicates.
- **p. 1 / Abstract - extractive body cue:** Addressing these issues, our idea is to extract cross-modality features by CLIP from text and image data naturally related to 3D point clouds.
- **p. 3 / 1) Visual con - extractive body cue:** they are constrained by large language models (LLM) and lack the capacity for scene understanding.
- **p. 1 / 1. Introduction - extractive body cue:** Existing 3DSGG models are mainly working in two directions to improve the accuracy.

## Core Idea

- **p. 2 / 1) Visual contextual - extractive body cue:** The primary contributions are summarized as: • We propose the new and practical tasks of OV 3DSGG.
- **p. 1 / Abstract - extractive body cue:** Specifically, we propose a novel Cross-Modality Contrastive Learning 3DSGG (CCL-3DSGG) method.
- **p. 3 / 3. Methods - extractive body cue:** Our framework is depicted in Figure 2.
- **p. 3 / 3.1. Cross-modality Features Extraction - extractive body cue:** To enhance the discriminative power of text features and ensure precise cross-modality feature alignment, we propose segmenting text based on grammatical analysis [43, 50].
- **p. 4 / 3.2. Cross-Modality Contrastive Losses - extractive body cue:** The purpose of cross-modality contrastive losses is to align image and text to 3DSG, which consists of Multi-view Image-3DSG Contrastive (I3D) Loss and Text3DSG Contrastive ...
- **p. 4 / 3.1. Cross-modality Features Extraction - extractive body cue:** Drawing from the VL-SAT method described in [48], we use a pretrained CLIP vision encoder Iθ to produce features for multi-view images.
- **p. 4 / 3.1. Cross-modality Features Extraction - extractive body cue:** There is a wooden rectangle table behind of the beige armchair. %%% 3DSG Feature Extractor I3D Loss √ Positive term × Negative term T3D Loss ...
- **p. 3 / 3.1. Cross-modality Features Extraction - extractive body cue:** After generating these negative samples, we use Tθ to denote the text feature extractor from CLIP and extract the text feature FT ∈Rw×512.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our approach begins with the extraction of cross-modality features from text T , image I, and 3D point clouds P (Section 3.1). | camera/depth stream, pose, map와 language goal | p. 3 (3. Methods), p. 4 (3.1. Cross-modality Features Extraction) |
| State/latent | begins, extraction, cross-modality, features, text, image, point, clouds, Section, CCL-3DSGG, architecture, inputting | robot pose, free-space/semantic map와 local goal | p. 3 (3. Methods), p. 4 (3.1. Cross-modality Features Extraction), p. 5 (3.2. Cross-Modality Contrastive Losses) |
| Output/action | The CCL-3DSGG architecture begins with inputting image-text pairs and unlabeled 3D point clouds, aiming to train the 3DSG feature extractor Pθ. | collision-free trajectory 또는 velocity command | p. 4 (3.1. Cross-modality Features Extraction), p. 5 (3.2. Cross-Modality Contrastive Losses), p. 3 (3.1. Cross-modality Features Extraction) |
| Objective/outcome | 2) Contrastive loss optimization based methods refine representations by augmenting similarity for positive samples and diminishing it for negative ones [7, 18, 35]. | goal reach, safety, localization error와 replanning latency | p. 3 (1) Prompt learning based methods adjust to downstream), p. 3 (3. Methods), p. 4 (3.1. Cross-modality Features Extraction) |

## Main Claims and Actual Contribution

- 서술의 단어와 시점별 영상에서 대조 대상을 구성해 3차원 장면 그래프 특징을 CLIP의 표현에 정렬한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf#page=5)
- 그래프 특징과 텍스트 프롬프트의 유사도로 새 물체와 술어를 예측하고 개방 어휘 조건의 성능을 비교했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.3. Comparisons with SOTA Methods on Close-Set), p. 6 (4.3. Comparisons with SOTA Methods on Close-Set) |
| Embodiment/environment | The training set of 3DSSG [47] contains 3582 scenes, while the testing set comprises 548 scenes. | hardware/simulator version and reset protocol | p. 5 (4.1. Task Description), p. 5 (4.1. Task Description) |
| Dataset/benchmark | Head-tail and Unseen Triple with Supervised: As evidenced in Table 2, our approach achieves SOTA performance when benchmarked against SGFN and VL-SAT for the infrequent predicate classes and unseen triplets. | role, split, size and leakage | p. 5 (4.1. Task Description), p. 5 (4.1. Task Description), p. 6 (4.3. Comparisons with SOTA Methods on Close-Set), p. 6 (4.2. Implementation Details) |
| Metric | These findings underscore the efficacy of our pretraining strategy, leveraging naturally occurring free-form captions and images. | definition, denominator, direction and uncertainty | p. 7 (4.4. Predicting Novel Classes), p. 6 (Figure/Table caption), p. 7 (4.4. Predicting Novel Classes) |
| Baseline/ablation | Comparisons with state-of-the-arts on the 3DSSG dataset. | fair input/data/compute/action matching | p. 6 (4.2. Implementation Details), p. 7 (4.4. Predicting Novel Classes), p. 7 (4.4. Predicting Novel Classes) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Limitations: There are several limitations of our work and still much to do to realize the full potential of the proposed approach.
- **p. 7 / 4.3. Comparisons with SOTA Methods on Close-Set - extractive body cue:** For better viewing, we only show failure cases.
- **p. 8 / 5. Conclusion - extractive body cue:** In future work, it will be interesting to design experiments to quantify the success of open vocabulary queries for 3DSGG where ground truth is not ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. (a) Difference in training: Previous 3DSGG models trained on closed-set classes by fully supervised [12, 48, 61]. Our method trains a 3DSG feature ...
- **p. 6 / 4.3. Comparisons with SOTA Methods on Close-Set - extractive body cue:** These results substantiate that our model furnishes more robust 3DSG feature representations, enhancing its generalization Table 3.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** Meanwhile, both unseen and seen triplets from the validation set are used to evaluate the robustness of our trained 3DSG feature extractor.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (Abstract), p. 3 (1) Visual con), p. 1 (1. Introduction), p. 2 (1) Visual con), p. 2 (1) Visual contextual), p. 4 (3.1. Cross-modality Features Extraction)이다.
