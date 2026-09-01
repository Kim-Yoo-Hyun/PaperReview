# Problem - DiSCO-3D : Discovering and Segmenting Sub-Concepts from Open-vocabulary Queries in NeRF

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Statement and Overview)): As illustrated in Figure 1, DiSCO-3D not only addresses OV-SD but also generalizes to its edge cases: 3D OV-Seg (when queries target a single sub-concept) and 3D USS (when no ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** 3D semantic segmentation provides high-level scene understanding for applications in robotics, autonomous systems, etc.
- **p. 1 / Abstract - extractive PDF cue:** Traditional methods adapt exclusively to either task-specific goals (open-vocabulary segmentation) or scene content (unsupervised semantic segmentation).
- **p. 1 / Abstract - extractive PDF cue:** We propose DiSCO-3D, the first method addressing the broader problem of 3D Open-Vocabulary Sub-concepts Discovery, which aims to provide a 3D semantic segmentation that adapts ...
- **p. 1 / Abstract - extractive PDF cue:** We build DiSCO3D on Neural Fields representations, combining unsupervised segmentation with weak open-vocabulary guidance.
- **p. 1 / Abstract - extractive PDF cue:** Our evaluations demonstrate that DiSCO-3D achieves effective performance in Open-Vocabulary Sub-concepts Discovery and exhibits state-of-the-art results in the edge cases of both open-vocabulary and unsupervised ...
- **p. 2 / 1. Introduction - extractive PDF cue:** As illustrated in Figure 1, DiSCO-3D not only addresses OV-SD but also generalizes to its edge cases: 3D OV-Seg (when queries target a single sub-concept) ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We present DiSCO-3D, the first method designed to solve the 3D OV-SD problem, combining Unsupervised Semantic Segmentation with Open-Vocabulary Segmentation guidance to serve as a ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | As illustrated in Figure 1, DiSCO-3D not only addresses OV-SD but also generalizes to its edge cases: 3D OV-Seg (when queries target ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Regarding GrowSP, although it succeeds in performing accurate segmentation, the global performances are lower, probably due to the input data modalities, as ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Regarding, GrowSP, although, succeeds, performing, accurate, segmentation, global, performances, lower | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | DiSCO-3D, inputs, pairs, features, samples, projector, network, learnt | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Regarding, GrowSP, although, succeeds, performing, accurate, segmentation, global, performances, lower | p. 8 (4.3.2. Unsupervised Semantic Segmentation), p. 2 (1. Introduction), p. 3 (3.1. Problem Statement and Overview) |
| Decision / output variable | geometry/map/query r; body terms: Although, present, pre-trained, LeRF, input, DiSCO-3D, compatible, wide | p. 5 (3.5. Method extensions), p. 3 (3.1. Problem Statement and Overview), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: While, losses, Lproj, Lproto, remain, unchanged, loss, Lqi | p. 5 (3.5. Method extensions), p. 5 (3.5. Method extensions) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.5. Method extensions), p. 5 (3.5. Method extensions) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4.2.3. Ablations studies), p. 6 (4.1. Implementation and evaluation details), p. 7 (4.2.3. Ablations studies) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** We present DiSCO-3D, the first method designed to solve the 3D OV-SD problem, combining Unsupervised Semantic Segmentation with Open-Vocabulary Segmentation guidance to serve as a ...
- **p. 3 / 3.1. Problem Statement and Overview - extractive PDF cue:** Discovery problem, specialized to the case of Neural Field [25] representations.

## What the Paper Changes

PDF contribution framing (p. 5 (3.5. Method extensions), p. 3 (3.1. Problem Statement and Overview), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 8 (4.3.1. Open-Vocabulary Segmentation)): Although we present our method using a pre-trained LeRF as input, DiSCO-3D is compatible with a wide range of feature fields (and their combinations) as long as two conditions are ...

- **p. 3 / 3.1. Problem Statement and Overview - extractive PDF cue:** In the following, we present our method in three parts.
- **p. 2 / 1. Introduction - extractive PDF cue:** We present DiSCO-3D, the first method designed to solve the 3D OV-SD problem, combining Unsupervised Semantic Segmentation with Open-Vocabulary Segmentation guidance to serve as a ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We introduce 3D OV-SD, a new 3D semantic segmentation task providing adaptive segmentations based on scene context and user-defined queries.
- **p. 8 / 4.3.1. Open-Vocabulary Segmentation - extractive PDF cue:** We present quantitative outcomes in Table 3, first analyzing results for classes, followed by concepts.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Additional details on hyperparameters, evaluation protocols and baselines can be found in the supplementary materials, as well as ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The last column refers to the main experiment where the number of prototypes is fixed and does not ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 8 (4.3.2. Unsupervised Semantic Segmentation), p. 2 (1. Introduction), p. 3 (3.1. Problem Statement and Overview), p. 3 (3.2. Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Statement and Overview), interface p. 8 (4.3.2. Unsupervised Semantic Segmentation), p. 2 (1. Introduction), p. 3 (3.1. Problem Statement and Overview), p. 3 (3.2. Preliminaries), objective p. 5 (3.5. Method extensions), p. 5 (3.5. Method extensions).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
