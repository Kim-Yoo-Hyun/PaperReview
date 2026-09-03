# Problem - Details Matter for Indoor Open-vocabulary 3D Instance Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): However, ours has unique features to improve the limitations of existing works.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Unlike closed-vocabulary 3D instance segmentation that is often trained end-to-end, open-vocabulary 3D instance segmentation (OV-3DIS) often leverages vision-language models (VLMs) to generate 3D instance proposals ...
- **p. 1 / Abstract - extractive body cue:** While various concepts have been proposed from existing research, we observe that these individual concepts are not mutually exclusive but complementary.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a new state-of-the-art solution for OV-3DIS by carefully designing a recipe to combine the concepts together and refining them to ...
- **p. 1 / Abstract - extractive body cue:** Our solution follows the two-stage scheme: 3D proposal generation and instance classification.
- **p. 1 / Abstract - extractive body cue:** We employ robust 3D tracking-based proposal aggregation to generate 3D proposals and remove overlapped or partial proposals by iterative merging/removal.
- **p. 2 / 1. Introduction - extractive body cue:** However, ours has unique features to improve the limitations of existing works.
- **p. 1 / 1. Introduction - extractive body cue:** This paper carefully combines the concepts and refines each step to address key challenges, achieving state-of-theart (SoTA) performance in existing benchmarks.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, ours has unique features to improve the limitations of existing works. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Given a 3D proposal and the visual encoder from Alpha-CLIP, we project the proposal onto all 2D images and select a subset ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Given, proposal, visual, encoder, Alpha-CLIP, project, onto, images, select, subset | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | conduct, frame-wise, sIOU, comparisons, between, observation, tracked, instance | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Given, proposal, visual, encoder, Alpha-CLIP, project, onto, images, select, subset | p. 5 (3.2. Open-Vocabulary Instance Classification), p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation) |
| Decision / output variable | geometry/map/query r; body terms: contributions, summarized, follows, carefully, combine, existing, concepts, refine | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: ratio, construct, inclusion, cost, matrix, Cincl, full, since | p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** This paper carefully combines the concepts and refines each step to address key challenges, achieving state-of-theart (SoTA) performance in existing benchmarks.
- **p. 1 / 1. Introduction - extractive body cue:** While we adopt this general paradigm, we refine each stage to effectively handle missing details in the existing literature.
- **p. 2 / 1. Introduction - extractive body cue:** Following existing works [39, 60, 63], we use 3D superpoints [13] as a basic unit of point cloud operations.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.1. Image-based Proposal Generation), p. 3 (3.1. Image-based Proposal Generation)): Our contributions are summarized as follows: • We carefully combine the existing concepts and refine 3D proposal generation by removing overlaps in 2D predictions and applying robust 3D tracking for ...

- **p. 1 / 1. Introduction - extractive body cue:** Examples of open-vocabulary predictions from our method in the ScanNet200 dataset [7].
- **p. 1 / 1. Introduction - extractive body cue:** Our method effectively retrieves instances based on functional descriptions (e.g., drink water, heat mac & cheese) and object attributes (e.g., red chair). dicted proposals into ...
- **p. 4 / 3.1. Image-based Proposal Generation - extractive body cue:** With refinement, irrelevant 3D superpoints are removed, and our method successfully removes 3D superpoints that do not belong to the object, resulting in geometrically consistent ...
- **p. 3 / 3.1. Image-based Proposal Generation - extractive body cue:** Leveraging VFMs [28, 35, 43], image-based proposals provide a complementary approach for detecting novel classes not covered during the training of the 3D instance segmentation ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Improving such limitations remains our future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 6. Failure cases of using CLIP for instance classification. CLIP fails when the shape of the object ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Also, we found that our method fails to improve performance on small objects (e.g., ScanNet++ in the supplementary) ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | However, it lags behind OpenYOLO3D [2] in terms of mAP, which does not use CLIP for instance classification. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3.2. Open-Vocabulary Instance Classification), p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation), p. 5 (3.2. Open-Vocabulary Instance Classification). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 5 (3.2. Open-Vocabulary Instance Classification), p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation), p. 5 (3.2. Open-Vocabulary Instance Classification), objective p. 4 (3.1. Image-based Proposal Generation), p. 4 (3.1. Image-based Proposal Generation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
