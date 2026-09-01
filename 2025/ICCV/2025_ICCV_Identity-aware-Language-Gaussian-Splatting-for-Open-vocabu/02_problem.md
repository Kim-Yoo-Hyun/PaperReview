# Problem - Identity-aware Language Gaussian Splatting for Open-vocabulary 3D Semantic Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): To do this, most previous methods have utilized high-quality 3D point clouds [19, 25], however, it is quite difficult to acquire data, which reflects various realworld environments, with language annotations.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Open-vocabulary 3D semantic segmentation has been actively studied by incorporating language features into 3D scene representations.
- **p. 1 / Abstract - extractive PDF cue:** Even though many methods have shown the notable improvement in this task, they still have difficulties to make language embeddings be consistent across different views.
- **p. 1 / Abstract - extractive PDF cue:** This inconsistency highly results in mis-labeling where different language embeddings are assigned to the same part of an object.
- **p. 1 / Abstract - extractive PDF cue:** To address this issue, we propose a simple yet powerful method that aligns language embeddings via the identity information.
- **p. 1 / Abstract - extractive PDF cue:** The key idea is to locate language embeddings for the same identity closely in the latent space while putting them apart otherwise.
- **p. 1 / 1. Introduction - extractive PDF cue:** To do this, most previous methods have utilized high-quality 3D point clouds [19, 25], however, it is quite difficult to acquire data, which reflects various ...
- **p. 1 / 1. Introduction - extractive PDF cue:** This limitation still makes the practical use of open-vocabulary 3D semantic segmentation challenging.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To do this, most previous methods have utilized high-quality 3D point clouds [19, 25], however, it is quite difficult to acquire data, ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | This approach makes language embeddings be consistent for the same object, even in different views. • We propose a masking strategy that ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | makes, language, embeddings, consistent, same, object, even, different, views, masking | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | cosine, similarity, between, text, embedding, input, query, language | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: makes, language, embeddings, consistent, same, object, even, different, views, masking | p. 2 (1. Introduction), p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: main, contribution, summarized, follows, novel, framework, enforces, language | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Identity-aware Semantic Consistency Learning) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: loss, term, Lsame, enforces, consistency, maximizing, cosine, similarity | p. 3 (3.2. Identity-aware Semantic Consistency Learning), p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 5 (3.4. Loss Function), p. 5 (3.4. Loss Function) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Loss Function), p. 5 (3.4. Loss Function), p. 3 (3.1. Preliminaries) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (4.2. Datasets and Evaluation Metrics), p. 5 (4.2. Datasets and Evaluation Metrics), p. 6 (4.3. Performance Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** This limitation still makes the practical use of open-vocabulary 3D semantic segmentation challenging.
- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we propose an identity-aware language Gaussian field to resolve the aforementioned problem in open-vocabulary 3D semantic segmentation.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Identity-aware Semantic Consistency Learning), p. 3 (3.2. Identity-aware Semantic Consistency Learning), p. 4 (3.3. Progressive Mask Expanding)): The main contribution of the proposed method can be summarized as follows: • We propose a novel framework that enforces language embeddings in the Gaussian field to be located closer ...

- **p. 2 / 1. Introduction - extractive PDF cue:** In this paper, we propose an identity-aware language Gaussian field to resolve the aforementioned problem in open-vocabulary 3D semantic segmentation.
- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** To address this issue, we introduce an identity-aware semantic consistency learning scheme.
- **p. 3 / 3.2. Identity-aware Semantic Consistency Learning - extractive PDF cue:** Specifically, we incorporate the identity information into our framework, inspired by the concept of the identity encoding for segmentation and editing in 3D scenes [31].
- **p. 4 / 3.3. Progressive Mask Expanding - extractive PDF cue:** To resolve this problem, we propose a progressive mask expanding scheme.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Furthermore, we also evaluate the performance of the proposed method with photometric metrics, such as peak signal-to-noise ratio ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In addition, previous methods often fail to extract boundaries accurately due to the use of fixed threshold values ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 1 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 1 (1. Introduction), p. 2 (1. Introduction), objective p. 3 (3.2. Identity-aware Semantic Consistency Learning), p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 4 (3.2. Identity-aware Semantic Consistency Learning), p. 5 (3.4. Loss Function), p. 5 (3.4. Loss Function).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
