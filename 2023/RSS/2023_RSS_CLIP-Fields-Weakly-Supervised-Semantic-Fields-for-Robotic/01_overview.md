# CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2210.05663.
> PDF retrieval source: https://arxiv.org/pdf/2210.05663. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / RSS
- Authors: Nur Muhammad (Mahi) Shafiullah, Chris Paxton, Lerrel Pinto, Soumith Chintala, Arthur Szlam
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: CLIP, Robotics, semantic, NeRF
- Official paper: https://arxiv.org/abs/2210.05663
- Venue verification: https://www.roboticsproceedings.org/rss19/p074.html
- DOI: https://doi.org/10.15607/RSS.2023.XIX.074
- Full-text retrieval: https://arxiv.org/pdf/2210.05663
- Code/Project: https://mahis.life/clip-fields/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

CLIP-Fields는 3차원 좌표에서 시각·언어 특징을 조회하는 장면 기억을 학습해 로봇이 자연어로 지정한 장소나 물체를 찾게 한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss19/p074.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We propose CLIP-Fields, an implicit scene model that can be used for a variety of tasks, such as segmentation, instance identification, semantic search over space, ...
- **p. 1 / Abstract - extractive body cue:** CLIP-Fields learns a mapping from spatial locations to semantic embedding vectors.
- **p. 1 / Abstract - extractive body cue:** Importantly, we show that this mapping can be trained with supervision coming only from webimage and web-text trained models such as CLIP, Detic, and Sentence-BERT; ...
- **p. 1 / Abstract - extractive body cue:** When compared to baselines like Mask-RCNN, our method outperforms on few-shot instance identification or semantic segmentation on the HM3D dataset with only a fraction of ...
- **p. 1 / Abstract - extractive body cue:** Finally, we show that using CLIP-Fields as a scene memory, robots can perform semantic navigation in real-world environments.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, existing representations are coarse, often relying on a preset list of classes and capturing minimal semantics [2, 11].
- **p. 1 / I. INTRODUCTION - extractive body cue:** Concurrently, web-scale weakly-supervised vision-language models like CLIP [22] have shown that the ability to capture powerful semantic abstractions from individual 2D images.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** As a solution, we propose CLIP-Fields, which builds an implicit spatial semantic memory using webscale pretrained models as weak supervision.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we introduce a method for building weakly supervised semantic neural fields, called CLIP-Fields, which combines the advantages of both of these lines ...
- **p. 4 / IV. APPROACH - extractive body cue:** We use a Multi-resolution Hash Encoder [20] to learn a low level spatial representation mapping R3 →Rd, which is then mapped to higher dimensions and ...
- **p. 5 / IV. APPROACH - extractive body cue:** semantic label, f = heads ◦g is the associated semantic encoding function, F is a pre-trained semantic language encoder, c is the confidence associated with ...
- **p. 4 / IV. APPROACH - extractive body cue:** We use the following training objectives: Semantic Label Embedding: This objective trains the function encoding the semantic information of a 3D point as a n-dimensional ...
- **p. 5 / IV. APPROACH - extractive body cue:** In this paper's experiments, we use the CLIP ViT-B/32 model embeddings, giving the visual features 512 dimensions.
- **p. 3 / IV. APPROACH - extractive body cue:** When no human annotations are available, we use web-image trained object detection models on our RGB images.
- **p. 3 / IV. APPROACH - extractive body cue:** To train our model, we first preprocess this set of RGB-D frames into a scene dataset (Fig.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Concurrently, web-scale weakly-supervised vision-language models like CLIP [22] have shown that the ability to capture powerful semantic abstractions from individual 2D images. | camera/depth stream, pose, map와 language goal | p. 1 (I. INTRODUCTION), p. 3 (IV. APPROACH) |
| State/latent | Concurrently, web-scale, weakly-supervised, vision-language, models, like, CLIP, have, ability, capture, powerful, semantic | robot pose, free-space/semantic map와 local goal | p. 1 (I. INTRODUCTION), p. 3 (IV. APPROACH), p. 4 (IV. APPROACH) |
| Output/action | For ease of decoding, we constrain the output spaces of f, h to match the embedding space of pre-trained language and vision-language models, respectively. | collision-free trajectory 또는 velocity command | p. 3 (IV. APPROACH), p. 4 (IV. APPROACH), p. 4 (IV. APPROACH) |
| Objective/outcome | While training the contrastive loss objective, we also take into consideration the associated label weights. | goal reach, safety, localization error와 replanning latency | p. 4 (IV. APPROACH), p. 5 (IV. APPROACH), p. 5 (IV. APPROACH) |

## Main Claims and Actual Contribution

- RGB-D 관측을 공간에 투영하고 Detic, CLIP, Sentence-BERT의 출력을 약한 감독으로 사용해 장면별 수작업 주석 없이 좌표별 표현을 학습했다. [PDF 3쪽](https://www.roboticsproceedings.org/rss19/p074.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss19/p074.pdf#page=4)
- HM3D의 물체 인스턴스 식별과 의미 분할을 평가하고, 실제 실내에서는 질의와 유사한 공간 위치를 이동 목표로 사용했다. [PDF 6쪽](https://www.roboticsproceedings.org/rss19/p074.pdf#page=6) · [PDF 7쪽](https://www.roboticsproceedings.org/rss19/p074.pdf#page=7) · [PDF 8쪽](https://www.roboticsproceedings.org/rss19/p074.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION) |
| Embodiment/environment | Our visual segmentation experiments are performed on a subset of Habitat-Matterport 3D Semantic (HM3D semantics) [35] dataset, while our robot experiments were performed on a Hello Robot Stretch using Hector SLAM [15]. | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION) |
| Dataset/benchmark | 2) Data collection and training: We ran our robot experiment in two different scenes, one in the lab kitchen, and another in the lab library (Figure 9). | role, split, size and leakage | p. 5 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 8 (V. EXPERIMENTAL EVALUATION) |
| Metric | 7: Mean average accuracy on the semantic segmentation task on the HM3D Semantic dataset with label noise simulating errors in base labelling models. | definition, denominator, direction and uncertainty | p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTAL EVALUATION) |
| Baseline/ablation | In Figure 5, we see once again that CLIP-Fields outperforms the RGB-based models significantly, to the point where even with three labelled views, CLIP-Fields has a higher AP than any of the ... | fair input/data/compute/action matching | p. 6 (V. EXPERIMENTAL EVALUATION), p. 5 (V. EXPERIMENTAL EVALUATION), p. 5 (V. EXPERIMENTAL EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VI. CONCLUSIONS AND FUTURE WORK - extractive body cue:** In future work, we hope to explore models that share parameters across scenes, and can handle dynamic scenes and objects.
- **p. 5 / V. EXPERIMENTAL EVALUATION - extractive body cue:** Detic is absent from the first two evaluations since it is a detection model and thus cannot be fine-tuned on segmentation labels.
- **p. 8 / V. EXPERIMENTAL EVALUATION - extractive body cue:** However, if an object was misidentified during data preparation, CLIP-Fields fails to correctly identify it as well.
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 4) CLIP-Fields's robustness to label errors: In real-world applications, CLIP-Fields relies on labels given by large
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 7: Mean average accuracy on the semantic segmentation task on the HM3D Semantic dataset with label noise simulating errors in base labelling models.
- **p. 7 / V. EXPERIMENTAL EVALUATION - extractive body cue:** In this section, we examine the robustness of CLIP-Fields to such label errors.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 4 (IV. APPROACH), p. 5 (IV. APPROACH)이다.
