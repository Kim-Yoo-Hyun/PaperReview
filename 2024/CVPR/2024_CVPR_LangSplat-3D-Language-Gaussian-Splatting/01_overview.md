# LangSplat: 3D Language Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Qin_LangSplat_3D_Language_Gaussian_Splatting_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Qin_LangSplat_3D_Language_Gaussian_Splatting_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Minghan Qin, Wanhua Li, Jiawei Zhou, Haoqian Wang, Hanspeter Pfister
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, Vision-Language, grounding, open-vocabulary
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Qin_LangSplat_3D_Language_Gaussian_Splatting_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Qin_LangSplat_3D_Language_Gaussian_Splatting_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

LangSplat은 3D 가우시안에 언어 특징을 담아 자연어로 장면 속 영역을 검색한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humans live in a 3D world and commonly use natural language to interact with a 3D scene.
- **p. 1 / Abstract - extractive body cue:** Modeling a 3D language field to support open-ended language queries in 3D has gained increasing attention recently.
- **p. 1 / Abstract - extractive body cue:** This paper introduces LangSplat, which constructs a 3D language field that enables precise and efficient open-vocabulary querying within 3D spaces.
- **p. 1 / Abstract - extractive body cue:** Unlike existing methods that ground CLIP language embeddings in a NeRF model, LangSplat advances the field by utilizing a collection of 3D Gaussians, each encoding ...
- **p. 1 / Abstract - extractive body cue:** By employing a tile-based splatting technique for rendering language features, we circumvent the costly rendering process inherent in NeRF.
- **p. 2 / 1. Introduction - extractive body cue:** However, these methods [18, 24] suffer from significant limitations in both speed and accuracy, severely constraining their practical applicability.
- **p. 2 / 1. Introduction - extractive body cue:** These inaccurate CLIP features lead to the trained 3D language field lacking clear boundaries and containing a significant amount of noise.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** A scenespecific autoencoder is further introduced to alleviate the memory cost issue imposed by explicit modeling. • We propose to learn the hierarchical semantics defined ...
- **p. 2 / 1. Introduction - extractive body cue:** We summarize the contributions of this paper as follows: • We propose the LangSplat, which is the first 3D Gaussian Splatting-based method for 3D language ...
- **p. 4 / 3.3. 3D Gaussian Splatting for Language Fields - extractive body cue:** To address this issue, we present the first 3D Gaussian Splatting-based method for 3D language field modeling.
- **p. 4 / 3.2. Learning Hierarchical Semantics with SAM - extractive body cue:** In this paper, we propose leveraging SAM to obtain precise object masks, which are then used to acquire pixel-aligned features.
- **p. 5 / 3.3. 3D Gaussian Splatting for Language Fields - extractive body cue:** To reduce memory cost and improve efficiency, we introduce a scenewise language autoencoder.
- **p. 5 / 3.3. 3D Gaussian Splatting for Language Fields - extractive body cue:** (4) to render the language embeddings from 3D to 2D, and then we use the trained scene-specific decoder Ψ to recover the CLIP image embeddings ...
- **p. 5 / 3.3. 3D Gaussian Splatting for Language Fields - extractive body cue:** Specifically, we use the collections of CLIP features of SAM segmented masks {Ll t/l ∈{s, p, w}, 1 ≤t ≤T} to train a lightweight autoencoder.
- **p. 3 / 3. Proposed Approach - extractive body cue:** In this section, we first revisit the challenges of modeling 3D language fields and then elaborate on how our proposed LangSplat addresses these issues.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We take a set of calibrated images {It/t = 1, 2, ...T} as input and train a 3D language field Φ with these images. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Revisiting the Challenges of Language Fields), p. 2 (1. Introduction) |
| State/latent | take, calibrated, images, It/t, input, train, language, field, scenespecific, autoencoder, further, introduced | geometry, map, object/relationship state | p. 3 (3.1. Revisiting the Challenges of Language Fields), p. 2 (1. Introduction), p. 3 (3.1. Revisiting the Challenges of Language Fields) |
| Output/action | A scenespecific autoencoder is further introduced to alleviate the memory cost issue imposed by explicit modeling. • We propose to learn the hierarchical semantics defined by SAM to address the point ambiguity ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 3 (3.1. Revisiting the Challenges of Language Fields), p. 4 (3.1. Revisiting the Challenges of Language Fields) |
| Objective/outcome | We optimized the language embeddings with the objective: \ma t h cal {L}_{ l a ng} = \sum _ { l \i n \{s,p,w\}} \sum _{t=1}^{T} d_{lang}( \bm {F}_t^l(v), \bm {H}_t^l(v)), \label ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.3. 3D Gaussian Splatting for Language Fields), p. 5 (3.3. 3D Gaussian Splatting for Language Fields), p. 4 (3.3. 3D Gaussian Splatting for Language Fields) |

## Main Claims and Actual Contribution

- 가우시안에 CLIP 특징을 학습시키고 SAM이 구분한 영역을 이용해 여러 수준의 의미를 표현한다.
- 텍스트 질의에 해당하는 위치·영역과 언어 특징 렌더링의 효율을 평가한다.

[원문 초록](https://openaccess.thecvf.com/content/CVPR2024/html/Qin_LangSplat_3D_Language_Gaussian_Splatting_CVPR_2024_paper.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2. Results on the LERF dataset), p. 7 (4.3. Results on the 3D-OVS dataset) |
| Embodiment/environment | The LERF dataset [18] is captured using the iPhone App Polycam, which consists of complex in-the-wild scenes. | hardware/simulator version and reset protocol | p. 6 (4.1. Settings), p. 6 (4.1. Settings) |
| Dataset/benchmark | Ablations result on the bench scene of the 3D-OVS dataset. | role, split, size and leakage | p. 6 (4.1. Settings), p. 6 (4.1. Settings), p. 7 (4.2. Results on the LERF dataset), p. 8 (4.3. Results on the 3D-OVS dataset) |
| Metric | We report the average IoU scores (%). iterations. | definition, denominator, direction and uncertainty | p. 6 (4.1. Settings), p. 6 (4.1. Settings), p. 7 (4.2. Results on the LERF dataset) |
| Baseline/ablation | We observe that our method achieves an overall accuracy of 84.3%, significantly outperforming LERF. | fair input/data/compute/action matching | p. 6 (4.2. Results on the LERF dataset), p. 6 (4.2. Results on the LERF dataset), p. 7 (4.3. Results on the 3D-OVS dataset) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The framework of our LangSplat. Our LangSplat leverages SAM to learn hierarchical semantics to address the point ambiguity issue. Then segment masks are ...
- **p. 8 / 4.3. Results on the 3D-OVS dataset - extractive body cue:** As LERF suffers from the patchy issue and learns over-smoothed features, it fails to find accurate object boundaries.
- **p. 6 / 4.2. Results on the LERF dataset - extractive body cue:** We see that the LERF learned features fail to generate clear boundaries between objects while our method gives precise object shapes solely using CLIP features.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 5 (3.3. 3D Gaussian Splatting for Language Fields), p. 4 (3.2. Learning Hierarchical Semantics with SAM), p. 3 (3. Proposed Approach)이다.

## 검색 태그 근거

포즈가 알려진 다중 뷰 RGB의 SAM 마스크와 CLIP 특징을 가우시안에 기록한다. 텍스트 질의에 해당하는 영역을 렌더링해 여러 크기의 참조 물체를 평가했다. [원문 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Qin_LangSplat_3D_Language_Gaussian_Splatting_CVPR_2024_paper.pdf#page=4) · [원문 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Qin_LangSplat_3D_Language_Gaussian_Splatting_CVPR_2024_paper.pdf#page=7)
