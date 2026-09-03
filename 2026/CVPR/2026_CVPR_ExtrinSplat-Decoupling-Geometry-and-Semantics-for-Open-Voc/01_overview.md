# ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, semantic, alignment, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Open-vocabulary 3D scene understanding enables the parsing of 3D scenes with arbitrary natural language queries, moving beyond the limitations of predefined categories to offer enhanced generalization and richer semantics for applicatio ...를 문제로 두고, Our contributions are summarized as follows: • We propose ExtrinSplat, a new framework realizing the extrinsic paradigm, which efficiently decouples 3D geometry and semantics through object grouping and lightweight textual indices. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Lifting 2D open-vocabulary understanding into 3D Gaussian Splatting (3DGS) scenes is a critical challenge.
- **p. 1 / Abstract - extractive body cue:** Mainstream methods, built on an embedding paradigm, suffer from three key flaws: (i) geometry-semantic inconsistency, where points, rather than objects, serve as the semantic basis, ...
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we introduce ExtrinSplat, a framework built on the extrinsic paradigm that decouples geometry from semantics.
- **p. 1 / Abstract - extractive body cue:** Instead of embedding features, ExtrinSplat clusters Gaussians into multi-granularity, overlapping 3D object groups.
- **p. 1 / 1. Introduction - extractive body cue:** Open-vocabulary 3D scene understanding enables the parsing of 3D scenes with arbitrary natural language queries, moving beyond the limitations of predefined categories to offer enhanced ...
- **p. 1 / 1. Introduction - extractive body cue:** The primary challenge in this domain lies in finding an efficient and effective 3D scene representation.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose the extrinsic paradigm, a distinct, decoupled and layered architecture.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We propose ExtrinSplat, a new framework realizing the extrinsic paradigm, which efficiently decouples 3D geometry and semantics through ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose the extrinsic paradigm, a distinct, decoupled and layered architecture.
- **p. 3 / 3.1. Overall Architecture - extractive body cue:** Our method takes an optimized 3DGS scene representation and its corresponding image sequence as input.
- **p. 3 / 3.1. Overall Architecture - extractive body cue:** We present ExtrinSplat, a training-free framework that realizes the extrinsic paradigm by decoupling 3D geometry from semantics, as shown in Fig.
- **p. 5 / 3.3. Object-level Grouping - extractive body cue:** (b) Our method (via semantic distillation): We leverage DAM2SAM to track a single instance.
- **p. 4 / 3.3. Object-level Grouping - extractive body cue:** Specifically, for each group, we first identify the object's high-confidence core via mask back-projection, then refine its boundaries by identifying and excluding ambiguous points with ...
- **p. 3 / 3.1. Overall Architecture - extractive body cue:** Then, the instance feature extraction stage (§3.4) uses a VLM to generate textual hypotheses for each object group.
- **p. 7 / 2) Baselines. We compare our method with several recent - extractive body cue:** Method Ramen Teatime Figurines Waldo Mean 2D Methods LEGaussians 46.0 60.3 40.8 39.4 46.6 LangSplat 51.2 65.1 44.7 44.5 51.4 Feature-3DGS 43.7 58.8 40.5 39.6 ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our method takes an optimized 3DGS scene representation and its corresponding image sequence as input. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Overall Architecture), p. 5 (3.3. Object-level Grouping) |
| State/latent | takes, optimized, DGS, scene, representation, corresponding, image, sequence, input, Mainstream, direct, extraction | geometry, map, object/relationship state | p. 3 (3.1. Overall Architecture), p. 5 (3.3. Object-level Grouping), p. 3 (3.1. Overall Architecture) |
| Output/action | (a) Mainstream method (via direct extraction): All object masks, typically generated by SAM, are used to directly extract CLIP image features. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.3. Object-level Grouping), p. 3 (3.1. Overall Architecture), p. 4 (3.2. Data Preparation) |
| Objective/outcome | This design minimizes the requirements for perfect input data (see Appendix for details). | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2. Data Preparation), p. 5 (3.4. Instance Feature Extraction), p. 6 (2) Baselines. We compare our method with several recent) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We propose ExtrinSplat, a new framework realizing the extrinsic paradigm, which efficiently decouples 3D geometry and semantics through ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose the extrinsic paradigm, a distinct, decoupled and layered architecture.
- **p. 3 / 3.1. Overall Architecture - extractive body cue:** Our method takes an optimized 3DGS scene representation and its corresponding image sequence as input.
- **p. 3 / 3.1. Overall Architecture - extractive body cue:** We present ExtrinSplat, a training-free framework that realizes the extrinsic paradigm by decoupling 3D geometry from semantics, as shown in Fig.
- **p. 5 / 3.3. Object-level Grouping - extractive body cue:** (b) Our method (via semantic distillation): We leverage DAM2SAM to track a single instance.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative results of our 3D object segmentation on the ScanNet dataset. OpenGaussian and InstanceGaussian rely on matching CLIP features extracted from 2D images. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. This caption compares computational resources for the LERF figurines scene, including per-scene optimization time, peak VRAM use, and storage for CLIP features. By ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. mIoU results for open-vocabulary object selection in 3D space on the LERF dataset. Bold/Underline indicates the best/second-best performance per category.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Embodiment/environment | Given a text query as input, the task is to produce multi-view renderings of the semantically corresponding 3D instance(s). | hardware/simulator version and reset protocol | p. 5 (4.1. Open-Vocabulary Object Selection in 3D Space) |
| Dataset/benchmark | Given a text query as input, the task is to produce multi-view renderings of the semantically corresponding 3D instance(s). | role, split, size and leakage | p. 5 (4.1. Open-Vocabulary Object Selection in 3D Space) |
| Metric | Figure 1. Overview of our method. (a) Multi-view 2D segmentation masks are first extracted from the input scene. (b) Based on these masks, our method lifts the objects into 3D point groups ... | definition, denominator, direction and uncertainty | p. 3 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Baseline/ablation | Table 5. Ablation on feature extraction. We compare VLM-based text distillation against CLIP image baselines. Case Feature Source View Aggregation mIoU↑ #1 Image | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion and Limitation - extractive body cue:** Despite its strong performance, our method has certain limitations: 1) The accuracy of our object-level grouping can be compromised by substantially inaccurate initial segmentation masks ...
- **p. 8 / 5. Conclusion and Limitation - extractive body cue:** Addressing these issues remains a promising direction for future work.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results on object selection from the LERF dataset. OpenGaussian fails to separate nearby objects or maintain sharp boundaries, while Dr.Splat struggles to ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Open-vocabulary 3D scene understanding enables the parsing of 3D scenes with arbitrary natural language queries, moving beyond the limitations of predefined categories to offer enhanced generalization and richer semantics for applicatio ...를 문제로 두고, Our contributions are summarized as follows: • We propose ExtrinSplat, a new framework realizing the extrinsic paradigm, which efficiently decouples 3D geometry and semantics through object grouping and lightweight textual indices. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.3. Object-level Grouping), p. 3 (3.1. Overall Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
