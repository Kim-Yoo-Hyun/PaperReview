# Problem - OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): Due to the aforementioned challenges with online methods, recent work has increasingly shifted toward offline approaches.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary 3D object detection for autonomous driving aims to detect novel objects beyond the predefined training label sets in point cloud scenes.
- **p. 1 / Abstract - extractive body cue:** Existing approaches achieve this by connecting traditional 3D object detectors with vision-language models (VLMs) to regress 3D bounding boxes for novel objects and perform open-vocabulary ...
- **p. 1 / Abstract - extractive body cue:** However, achieving robust cross-modal alignment remains a challenge due to semantic inconsistencies when generating corresponding 3D and 2D feature pairs.
- **p. 1 / Abstract - extractive body cue:** To overcome this challenge, we present OV-SCAN, an Open-Vocabulary 3D framework that enforces Semantically Consistent Alignment for Novel object discovery.
- **p. 1 / Abstract - extractive body cue:** OVSCAN employs two core strategies: discovering precise 3D annotations and filtering out low-quality or corrupted alignment pairs (arising from 3D annotation, occlusioninduced, or resolution-induced noise).
- **p. 1 / 1. Introduction - extractive body cue:** Due to the aforementioned challenges with online methods, recent work has increasingly shifted toward offline approaches.
- **p. 1 / 1. Introduction - extractive body cue:** OV-3D object detection faces two main challenges: (1) novel object discovery (NOD), which involves generating 3D labels for novel objects in order to train an ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Due to the aforementioned challenges with online methods, recent work has increasingly shifted toward offline approaches. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | In addition, the proposed H2SA head effectively aligns 3D-to-2D alignment pairs by introducing a two-stage alignment process. • We validate OV-SCAN on ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | addition, H2SA, head, effectively, aligns, D-to-2D, alignment, pairs, introducing, two-stage | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Traditional, LiDAR-based, object, detection, methods, designed, regress, features | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: addition, H2SA, head, effectively, aligns, D-to-2D, alignment, pairs, introducing, two-stage | p. 2 (1. Introduction), p. 3 (3.1. Notation and Preliminaries), p. 3 (3.1. Notation and Preliminaries) |
| Decision / output variable | geometry/map/query r; body terms: summarize, main, contributions, follows, present, OV-SCAN, OV-3D, object | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Semantically Consistent NOD (SC-NOD)) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: optimization, governed, cost, function, balances, multiple, objectives, continuous | p. 3 (3.1. Notation and Preliminaries), p. 4 (3.2. Semantically Consistent NOD (SC-NOD)), p. 4 (3.1. Notation and Preliminaries), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 6 (3.4. Training) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Notation and Preliminaries), p. 4 (3.2. Semantically Consistent NOD (SC-NOD)), p. 6 (3.4. Training) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 2 (Figure/Table caption), p. 7 (4.1. Experimental Setup), p. 7 (4.2. Main Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** OV-3D object detection faces two main challenges: (1) novel object discovery (NOD), which involves generating 3D labels for novel objects in order to train an ...
- **p. 2 / 1. Introduction - extractive body cue:** However, existing methods often overlook common autonomous driving scenarios where objects are partially occluded (Fig.
- **p. 2 / 1. Introduction - extractive body cue:** In such cases, the 2D features become ambiguous or lack sufficient representation, leading to confusion during cross-modal alignment.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Semantically Consistent NOD (SC-NOD)), p. 3 (3. Method), p. 3 (3.1. Notation and Preliminaries)): We summarize our main contributions as follows: • We present OV-SCAN, an OV-3D object detector benefiting from improved cross-modal alignment, see Fig.

- **p. 2 / 1. Introduction - extractive body cue:** More specifically, we introduce the Semantically-Consistent Novel-Object Discovery (SCNOD) module to handle the inherent challenges of noisy cross-modal alignment.
- **p. 4 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive body cue:** Our method relies on CLIP to classify the object into its corresponding novel class c.
- **p. 3 / 3. Method - extractive body cue:** In this section, we present the details of OV-SCAN.
- **p. 3 / 3.1. Notation and Preliminaries - extractive body cue:** Our method extends the traditional target pair of 3D bounding box and class label, into a triplet target denoted by !→= {(Bi, ci, A2D,i)}N i=1.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | The primary limitation of SC-NOD is its limited annotation recovery (Fig. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | These insights motivate future work exploring alternative methods less dependent on 2D proposals and anchor-free box-parameterization strategies. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 2. 3D Annotation Errors. Common 3D annotation errors during box parametrization, including but not limited to, poor ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 3. Sources of Semantic Discrepancies. (a) CLIP sim- ilarity scores for a truck reveal that occlusion cases ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 3 (3.1. Notation and Preliminaries), p. 3 (3.1. Notation and Preliminaries), p. 4 (3.1. Notation and Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 3 (3.1. Notation and Preliminaries), p. 3 (3.1. Notation and Preliminaries), p. 4 (3.1. Notation and Preliminaries), objective p. 3 (3.1. Notation and Preliminaries), p. 4 (3.2. Semantically Consistent NOD (SC-NOD)), p. 4 (3.1. Notation and Preliminaries), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 5 (3.2. Semantically Consistent NOD (SC-NOD)), p. 6 (3.4. Training).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
