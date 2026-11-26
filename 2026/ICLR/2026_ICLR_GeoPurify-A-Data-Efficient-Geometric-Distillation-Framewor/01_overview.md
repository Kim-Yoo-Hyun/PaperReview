# GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/039bc8e424e1fc196b4203555b54ebc4-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/248164. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Weijia Dou, Xu Zhang, Yi Bin, Jian Liu, Bo Peng, Guoqing Wang, Yang Yang, Heng Tao Shen
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: semantic, representation alignment, 3D segmentation, 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/039bc8e424e1fc196b4203555b54ebc4-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/039bc8e424e1fc196b4203555b54ebc4-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

GeoPurify는 2차원 시각언어 특징을 3차원으로 옮길 때 생기는 잡음을 3차원 자기지도 모델의 기하 정보로 줄인다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/039bc8e424e1fc196b4203555b54ebc4-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Recent attempts to transfer features from 2D Vision-Language Models (VLMs) to 3D semantic segmentation expose a persistent trade-off.
- **p. 1 / ABSTRACT - extractive body cue:** Directly projecting 2D features into 3D yields noisy and fragmented predictions, whereas enforcing geometric coherence necessitates costly training pipelines and large-scale, annotated 3D data.
- **p. 1 / ABSTRACT - extractive body cue:** We argue that this limitation stems from the dominant segmentationand-matching paradigm, which fails to reconcile 2D semantics with 3D geometric structure.
- **p. 1 / ABSTRACT - extractive body cue:** The geometric cues are not eliminated during the 2D-to-3D transfer but remain latent within the noisy and view-aggregated features.
- **p. 1 / ABSTRACT - extractive body cue:** To exploit this property, we propose GeoPurify that applies a small Student Affinity Network to purify 2D VLM-generated 3D point features using geometric priors distilled ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, this often results in severe geometric inconsistencies, since 2D models lack awareness of 3D spatial structure.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This approach fails to scale to the diverse and complex real-world objects and is further constrained by the prohibitive cost of manual 3D annotation, a ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are: • We introduce GeoPurify, a data-efficient framework built on the hypothesis that beyond their semantic richness, VLM-projected features also embed ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Motivated by this hypothesis, we present GeoPurify, a data-efficient framework designed to recover latent geometric structure from noisy semantic features and produce robust 3D representations.
- **p. 3 / 3 METHODOLOGY - extractive body cue:** To address this, we introduce a 3D student affinity network ϕS that learns geometric affinities from the point cloud using a self-supervised 3D geometric model ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** 3.3 GEOMETRIC CONTRASTIVE DISTILLATION To rectify the geometric inconsistencies within the initial semantic features Fsem, we introduce a contrastive purification module trained via knowledge distillation.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To move beyond these limitations, the field is shifting toward open-vocabulary 3D understanding, which enables models to identify objects using arbitrary descriptions rather than predefined ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** 3.1 OVERALL ARCHITECTURE As illustrated in Figure 2, our proposed GeoPurify first leverages a frozen Vision-Language Model (Ψ2D) to transfer and merge multi-view RGB images ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** The pre-trained student network then applies a geometry-aware pooling, using its learned affinities to refine the initial features.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** We then curate a set of hard negatives comprising two distinct types: macronegatives, which are the points globally most dissimilar to pa in the feature ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3.1 OVERALL ARCHITECTURE As illustrated in Figure 2, our proposed GeoPurify first leverages a frozen Vision-Language Model (Ψ2D) to transfer and merge multi-view RGB images into an initial 3D feature map Fsem ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY) |
| State/latent | OVERALL, ARCHITECTURE, illustrated, Figure, GeoPurify, first, leverages, frozen, Vision-Language, Model, transfer, merge | geometry, map, object/relationship state | p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 1 (1 INTRODUCTION) |
| Output/action | 3.2 SEMANTIC INITIALIZATION FROM A GENERALIST VLM To obtain 3D representations enriched with semantic priors, we project RGB inputs into the 3D point space (constructed by aggregating multi-view projections, without necessitating extern ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3 METHODOLOGY), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Objective/outcome | The student network, ϕS, which maps the point cloud P to a set of geometric embeddings Ggeo ∈RN×Dgeo, is then optimized to organize its embedding space according to this distilled affinity information ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |

## Main Claims and Actual Contribution

- 작은 학생 네트워크가 점들 사이의 기하적 유사성을 증류하고 추론 시 이 유사성으로 이웃 특징을 집계한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/039bc8e424e1fc196b4203555b54ebc4-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/039bc8e424e1fc196b4203555b54ebc4-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/039bc8e424e1fc196b4203555b54ebc4-Paper-Conference.pdf#page=5)
- 실내 열린 어휘 분할과 긴 꼬리 범주 평가에서 훈련 자료량과 모듈 구성에 따른 성능을 비교했다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/039bc8e424e1fc196b4203555b54ebc4-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/039bc8e424e1fc196b4203555b54ebc4-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/039bc8e424e1fc196b4203555b54ebc4-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/039bc8e424e1fc196b4203555b54ebc4-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 14 (A.1 NETWORK ARCHITECTURES), p. 8 (4 EXPERIMENTS) |
| Embodiment/environment | For all experiments, we adhere to the official training, validation, and testing splits for the ScanNetV2 and Matterport3D datasets to ensure fair comparison with prior work. | hardware/simulator version and reset protocol | p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION), p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION) |
| Dataset/benchmark | As shown in Table 2, GeoPurify establishes a new stateof-the-art on long-tail benchmarks like ScanNet200 and the challenging M160 split. | role, split, size and leakage | p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION), p. 15 (A.2 DATASET DETAILS AND SUBSET SELECTION), p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Metric | Finally, from each resulting cluster, we select the single most exemplary scene by ranking them with a composite score, S = Hc,norm + γ · Nc,norm, (6) which jointly rewards normalized complexity ... | definition, denominator, direction and uncertainty | p. 6 (4 EXPERIMENTS), p. 21 (Figure/Table caption), p. 6 (4 EXPERIMENTS) |
| Baseline/ablation | Our data-efficient GeoPurify is compared against other zero-shot baselines. | fair input/data/compute/action matching | p. 8 (4 EXPERIMENTS), p. 20 (Figure/Table caption), p. 9 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 21 / Figure/Table caption - extractive body cue:** Figure 6: Illustration of typical failure modes. From left to right: challenges with the presence of over-smoothing artifacts at object boundaries, and inherited semantic errors ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** First, we filter for quality, culling any scene that falls below the median value for both richness (Nc) and complexity (Hc).
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Without them, the model learns the global scene layout but fails to disentangle co-located surfaces.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: The Fundamental Disconnect: Semantic Richness vs. Geometric Coherence. Left: Original RGB 3D scene. Middle: Features distilled from 2D VLMs (Zou et al., 2023) ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We attribute this robustness to our decoupled design.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** This robust generalization arises from the synergy between our semantic and geometric modules.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We evaluate zero-shot cross-dataset generalization to test the robustness of our learned geometric prior.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHODOLOGY)이다.
