# Problem - OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): However, these approaches are predominantly offline and lack support for online instance-level panoptic perception, hindering their applications in embodied tasks.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary scene understanding with online panoptic mapping is essential for embodied applications to perceive and interact with environments.
- **p. 1 / Abstract - extractive body cue:** However, existing methods are predominantly offline or lack instance-level understanding, limiting their applicability to real-world robotic tasks.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose OnlinePG, a novel and effective system that integrates geometric reconstruction and open-vocabulary perception using 3D Gaussian Splatting in an online ...
- **p. 1 / Abstract - extractive body cue:** Technically, to achieve online panoptic mapping, we employ an efficient local-to-global paradigm with a sliding window.
- **p. 1 / Abstract - extractive body cue:** To build local consistency map, we construct a 3D segment clustering graph that jointly leverages geometric and semantic cues, fusing inconsistent segments within sliding window ...
- **p. 1 / 1. Introduction - extractive body cue:** However, these approaches are predominantly offline and lack support for online instance-level panoptic perception, hindering their applications in embodied tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Current online open-vocabulary scene understanding approaches [42, 52] cannot distinguish individual 3D instances based on text queries, while offline instanceaware approaches [19, 39, 50, 58] ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these approaches are predominantly offline and lack support for online instance-level panoptic perception, hindering their applications in embodied tasks. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | For each voxel v occupied by instance Ii, we assign the local instance label and weight grids: T t l (v) = ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | voxel, occupied, instance, assign, local, label, weight, grids, IDi, where | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Therefore, maintain, sliding, window, over, input, stream, perform | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: voxel, occupied, instance, assign, local, label, weight, grids, IDi, where | p. 4 (3.2. Local Consistent Map Construction), p. 1 (1. Introduction), p. 3 (3.2. Local Consistent Map Construction) |
| Decision / output variable | path/waypoint/velocity; body terms: Overall, technical, contributions, summarized, follows, online, open-vocabulary, panoptic | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Following, previous, works, adopt, loss, terms, appearance, geometry | p. 5 (3.3. Local-to-Global Map Fusion), p. 3 (3.1. Scene Representation), p. 4 (3.2. Local Consistent Map Construction), p. 5 (3.3. Local-to-Global Map Fusion) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Local Consistent Map Construction), p. 4 (3.2. Local Consistent Map Construction), p. 5 (3.3. Local-to-Global Map Fusion) |
| Success / guarantee | goal reach with collision-free execution | p. 8 (4.3. Ablation Studies), p. 5 (4.1. Experimental Settings), p. 8 (4.3. Ablation Studies) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Current online open-vocabulary scene understanding approaches [42, 52] cannot distinguish individual 3D instances based on text queries, while offline instanceaware approaches [19, 39, 50, 58] ...
- **p. 1 / 1. Introduction - extractive body cue:** Despite previous approaches that combine VLMs with 3DGS having yielded satisfactory performance, two critical limitations remain: 1) offline reconstruction and perception settings.
- **p. 2 / 1. Introduction - extractive body cue:** Addressing these challenges is crucial for enabling real-time, open-vocabulary panoptic mapping and understanding in embodied applications.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method)): Overall, the technical contributions of our approach are summarized as follows: • We propose an online open-vocabulary panoptic mapping framework that unifies geometric reconstruction and semantic understanding in a local-to-global ...

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we present OnlinePG, an efficient online open-vocabulary panoptic mapping system based on 3D Gaussian Splatting that integrates geometric reconstruction with semantic understanding.
- **p. 3 / 3. Method - extractive body cue:** To mitigate the inconsistencies of 2D segmentation results, we propose an effective segment clustering algorithm that synergistically leverages geometric and semantic cues to obtain consistent ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Limitations: (1) Our method currently cannot reconstruct dynamic objects. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Our future work will explore feed-forward approaches [20, 46, 47] that eliminate these requirements for fully pose-free and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Since the baselines [31, 33, 50] marked with ∗ cannot obtain 3D panoptic results, we use the performance ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | While OnlineAnySeg can handle simple queries (e.g., "television"), it fails on some fine-grained and multi-instance queries (e.g., "pillow", ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3.2. Local Consistent Map Construction), p. 1 (1. Introduction), p. 3 (3.2. Local Consistent Map Construction), p. 4 (3.2. Local Consistent Map Construction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.2. Local Consistent Map Construction), p. 1 (1. Introduction), p. 3 (3.2. Local Consistent Map Construction), p. 4 (3.2. Local Consistent Map Construction), objective p. 5 (3.3. Local-to-Global Map Fusion), p. 3 (3.1. Scene Representation), p. 4 (3.2. Local Consistent Map Construction), p. 5 (3.3. Local-to-Global Map Fusion).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
