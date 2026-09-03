# Identity-aware Language Gaussian Splatting for Open-vocabulary 3D Semantic Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Gaussian Splatting, semantic
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To do this, most previous methods have utilized high-quality 3D point clouds [19, 25], however, it is quite difficult to acquire data, which reflects various realworld environments, with language annotations.를 문제로 두고, The main contribution of the proposed method can be summarized as follows: • We propose a novel framework that enforces language embeddings in the Gaussian field to be located closer in the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary 3D semantic segmentation has been actively studied by incorporating language features into 3D scene representations.
- **p. 1 / Abstract - extractive body cue:** Even though many methods have shown the notable improvement in this task, they still have difficulties to make language embeddings be consistent across different views.
- **p. 1 / Abstract - extractive body cue:** This inconsistency highly results in mis-labeling where different language embeddings are assigned to the same part of an object.
- **p. 1 / Abstract - extractive body cue:** To address this issue, we propose a simple yet powerful method that aligns language embeddings via the identity information.
- **p. 1 / Abstract - extractive body cue:** The key idea is to locate language embeddings for the same identity closely in the latent space while putting them apart otherwise.
- **p. 1 / 1. Introduction - extractive body cue:** To do this, most previous methods have utilized high-quality 3D point clouds [19, 25], however, it is quite difficult to acquire data, which reflects various ...
- **p. 1 / 1. Introduction - extractive body cue:** This limitation still makes the practical use of open-vocabulary 3D semantic segmentation challenging.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The main contribution of the proposed method can be summarized as follows: • We propose a novel framework that enforces language embeddings in the Gaussian ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose an identity-aware language Gaussian field to resolve the aforementioned problem in open-vocabulary 3D semantic segmentation.
- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive body cue:** To address this issue, we introduce an identity-aware semantic consistency learning scheme.
- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive body cue:** Specifically, we incorporate the identity information into our framework, inspired by the concept of the identity encoding for segmentation and editing in 3D scenes [31].
- **p. 4 / 3.3. Progressive Mask Expanding - extractive body cue:** To resolve this problem, we propose a progressive mask expanding scheme.
- **p. 5 / 3.4. Loss Function - extractive body cue:** For stable optimization, we do not apply Lcons during the first 15,000 iterations, allowing the model to focus on learning by Lclip.
- **p. 4 / 3.4. Loss Function - extractive body cue:** The color reconstruction loss consists of L1 and D-SSIM terms, which measure the similarity of colors and structures between the rendered image ˆI and the ...
- **p. 4 / 3.3. Progressive Mask Expanding - extractive body cue:** We then Novel view Identity-aware language 3D Gaussian field Seed segment Final segment Progressive mask expanding Highest cosine similarity Text query Gundam Language feature map ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This approach makes language embeddings be consistent for the same object, even in different views. • We propose a masking strategy that starts with the most relevant segment, determined by the highest ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 4 (3.2. Identity-aware Semantic Consistency Learning) |
| State/latent | makes, language, embeddings, consistent, same, object, even, different, views, masking, strategy, starts | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 1 (1. Introduction) |
| Output/action | By aligning language embeddings conditioned on the identity information, the proposed method yields the reliable segmentation result, which is well aligned with the input text query across different views as shown in ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | The loss term Lsame enforces the consistency by maximizing the cosine similarity between language embeddings of Gaussians having the same identity. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 3 (3.2. Identity-aware Semantic Consistency Learning), p. 4 (3.2. Identity-aware Semantic Consistency Learning) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** The main contribution of the proposed method can be summarized as follows: • We propose a novel framework that enforces language embeddings in the Gaussian ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose an identity-aware language Gaussian field to resolve the aforementioned problem in open-vocabulary 3D semantic segmentation.
- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive body cue:** To address this issue, we introduce an identity-aware semantic consistency learning scheme.
- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive body cue:** Specifically, we incorporate the identity information into our framework, inspired by the concept of the identity encoding for segmentation and editing in 3D scenes [31].
- **p. 4 / 3.3. Progressive Mask Expanding - extractive body cue:** To resolve this problem, we propose a progressive mask expanding scheme.
- **p. 5 / 4.3. Performance Evaluation - extractive body cue:** Specifically, the proposed method achieves 80.5 mIoU and 76.0 mBIoU on the LERF dataset, which outperforms the stateof-the-art methods by a considerable margin for all ...
- **p. 5 / 4.3. Performance Evaluation - extractive body cue:** As can be seen, the proposed method achieves 94.4 mIoU, which shows the superior performance compared to previous methods.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** As can be seen, the performance of open-vocabulary 3D semantic segmentation is considerably improved as each component is added to the baseline.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (4.3. Performance Evaluation), p. 5 (4.3. Performance Evaluation) |
| Embodiment/environment | The LERF dataset consists of 3D scenes in the wild, which are captured by using the Polycam application on the iPhone. | hardware/simulator version and reset protocol | p. 5 (4.2. Datasets and Evaluation Metrics), p. 5 (4.2. Datasets and Evaluation Metrics) |
| Dataset/benchmark | Performance comparisons of novel view rendering on the LERF [10] dataset (the best results are shown in bold). can see that the proposed method is able to render the target object without ... | role, split, size and leakage | p. 5 (4.2. Datasets and Evaluation Metrics), p. 5 (4.2. Datasets and Evaluation Metrics), p. 7 (4.3. Performance Evaluation), p. 6 (4.3. Performance Evaluation) |
| Metric | These metrics evaluate the accuracy of semantic segmentation masks corresponding to the input text queries. | definition, denominator, direction and uncertainty | p. 5 (4.2. Datasets and Evaluation Metrics), p. 5 (4.2. Datasets and Evaluation Metrics), p. 6 (4.3. Performance Evaluation) |
| Baseline/ablation | Performance comparisons of novel view rendering on the LERF [10] dataset (the best results are shown in bold). can see that the proposed method is able to render the target object without ... | fair input/data/compute/action matching | p. 7 (4.3. Performance Evaluation), p. 6 (4.3. Performance Evaluation), p. 5 (4.3. Performance Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.3. Performance Evaluation - extractive body cue:** Furthermore, we also evaluate the performance of the proposed method with photometric metrics, such as peak signal-to-noise ratio (PSNR), structural similarity index (SSIM) [27], and ...
- **p. 6 / 4.3. Performance Evaluation - extractive body cue:** In addition, previous methods often fail to extract boundaries accurately due to the use of fixed threshold values in generating semantic segmentation masks(see Fig.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To do this, most previous methods have utilized high-quality 3D point clouds [19, 25], however, it is quite difficult to acquire data, which reflects various realworld environments, with language annotations.를 문제로 두고, The main contribution of the proposed method can be summarized as follows: • We propose a novel framework that enforces language embeddings in the Gaussian field to be located closer in the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Loss Function), p. 4 (3.4. Loss Function), p. 4 (3.3. Progressive Mask Expanding) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
