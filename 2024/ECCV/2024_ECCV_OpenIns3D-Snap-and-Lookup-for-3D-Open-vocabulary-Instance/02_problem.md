# Problem - OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7914_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07914.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)): However, unlike 2D data that can be easily collected from the internet, constructing a large-scale 3D-text dataset poses a challenge.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** 3D scene understanding plays a critical role in various domains, such as autonomous driving, robotic sensing, AR/VR, and manufacturing, among others. ⋆Corresponding author.
- **p. 2 / 1 Introduction - extractive body cue:** Class Lookup Tables SNAP MASK LOOKUP 3d Point Cloud Synthetic Scene-level Images 3D Open vocabulary Instance Segmentation Mask2Pixel Guidance Class-agnostic Mask Proposals 2D openworld detector ...
- **p. 2 / 1 Introduction - extractive body cue:** OVOD ScanNetV2 OVIS-8/4 S3DIS OVIS SPTLS3D Indoor Outdoor (b) Results Comparison OV-Rec ScanNetV2 OVIS-6/6 S3DIS Fig.
- **p. 2 / 1 Introduction - extractive body cue:** 2: High-level Illustrations of OpenIns3D and Quantitative Results.
- **p. 2 / 1 Introduction - extractive body cue:** (a) OpenIns3D follows the "Mask-Snap-Lookup" steps for open-vocabulary scene understanding.
- **p. 2 / 1 Introduction - extractive body cue:** However, unlike 2D data that can be easily collected from the internet, constructing a large-scale 3D-text dataset poses a challenge.
- **p. 2 / 1 Introduction - extractive body cue:** This limitation impacts its performance in dynamic and everchanging contexts.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, unlike 2D data that can be easily collected from the internet, constructing a large-scale 3D-text dataset poses a challenge. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | This approach achieves state-of-the-art results across a range of benchmarks and possesses the ability to comprehend highly complex input queries. - The ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | achieves, state-of-the-art, across, range, benchmarks, possesses, ability, comprehend, highly, complex | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Mask, module, learns, class-agnostic, proposals, point, clouds, Snap | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: achieves, state-of-the-art, across, range, benchmarks, possesses, ability, comprehend, highly, complex | p. 4 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)) |
| Decision / output variable | geometry/map/query r; body terms: introduce, OpenIns3D, framework, designed, effectively, perform, open-vocabulary, scene | p. 3 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: images, specifically, designed, encompass, part, relevant, masks, aiming | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 12 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** This limitation impacts its performance in dynamic and everchanging contexts.
- **p. 3 / 1 Introduction - extractive body cue:** Lastly, the 3D mask proposals are refined by removing masks lacking class assignments after both global and local Lookup.
- **p. 3 / 1 Introduction - extractive body cue:** OpenIns3D even outperforms OpenMask3D [30], a concurrent work that heavily utilizes 2D images, for instance, segmentation on the challenging Replica [28] dataset.

## What the Paper Changes

PDF body contribution framing (p. 3 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): To this end, we introduce OpenIns3D, a framework designed to effectively perform 3D open-vocabulary scene understanding tasks without relying on 2D aligned images.

- **p. 4 / 1 Introduction - extractive body cue:** In summary, our contributions are: - OpenIns3D employs a distinct pipeline that operates without the need for well-aligned images.
- **p. 2 / 1 Introduction - extractive body cue:** While the development of 3D closed-set understanding is relatively mature, scene understanding in an open-vocabulary setting is still in its infancy.
- **p. 2 / 1 Introduction - extractive body cue:** We believe that developing a 3D open-vocabulary framework without relying on well-aligned 2D images is meaningful, as this will simplify deployment pre
- **p. 3 / 1 Introduction - extractive body cue:** The design of OpenIns3D also allows 2D detectors to be changed without the need for retraining.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 12 | Table 6: 3D instance segmentation results on the ScanNet200 validation set. OpenIns3D demonstrates robust performance when compared to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | It also shows certain limitations on small objects that are not well-reconstructed in 3D scenes. | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | For 3D instance segmentation, compared to works in the PLA family [9,10,34] and the latest work Open3DIS [22], ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 4 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
