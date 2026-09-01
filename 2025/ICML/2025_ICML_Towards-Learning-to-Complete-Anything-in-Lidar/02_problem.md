# Problem - Towards Learning to Complete Anything in Lidar

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vWPzKn6usZ; PDF retrieval source: https://openreview.net/pdf/8fbe2a59d85d4f1be15c6351679cc46349d858df.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): However, prior work can only localize and complete around 1

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We propose CAL (Complete Anything in Lidar) for Lidar-based shape-completion in-the-wild.
- **p. 1 / Abstract - extractive PDF cue:** This is closely related to Lidar-based semantic/panoptic scene completion.
- **p. 1 / Abstract - extractive PDF cue:** However, contemporary methods can only complete and recognize objects from a closed vocabulary labeled in existing Lidar datasets.
- **p. 1 / Abstract - extractive PDF cue:** Different to that, our zero-shot approach leverages the temporal context from multi-modal sensor sequences to mine object shapes and semantic features of observed objects.
- **p. 1 / Abstract - extractive PDF cue:** These are then distilled into a Lidar-only instance-level completion and recognition model.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, prior work can only localize and complete around 1
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, we leverage image (Kirillov et al., 2023) and video (Ravi et al., 2024) segmentation foundation models to localize and track objects ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, prior work can only localize and complete around 1 | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | CAL takes a single input Lidar scan P, providing sparse and incomplete observations of scene geometry (Fig. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | CAL, takes, single, input, Lidar, scan, providing, sparse, incomplete, observations | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Given, Lidar, point, cloud, input, CAL, produces, object | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: CAL, takes, single, input, Lidar, scan, providing, sparse, incomplete, observations | p. 4 (3.2. Learning To Complete Objects), p. 3 (3. Method), p. 5 (3.2. Learning To Complete Objects) |
| Decision / output variable | geometry/map/query r; body terms: first, Zero-Shot, Lidar, Panoptic, Scene, Completion, demonstrate, recognize | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: During, training, iteration, generative, decoder, produces, coarse-to-fine, voxel | p. 5 (3.2. Learning To Complete Objects), p. 5 (3.2. Learning To Complete Objects) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.2. Learning To Complete Objects), p. 5 (3.2. Learning To Complete Objects) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 23 (Figure/Table caption), p. 6 (4.1. Experimental Setup), p. 7 (4.1. Experimental Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, we leverage image (Kirillov et al., 2023) and video (Ravi et al., 2024) segmentation foundation models to localize and track objects ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Mining shape priors from unlabeled data.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Method), p. 4 (3.2. Learning To Complete Objects), p. 5 (3.2. Learning To Complete Objects)): We propose the first method for Zero-Shot Lidar Panoptic Scene Completion.

- **p. 2 / 1. Introduction - extractive PDF cue:** 1, 2⃝) and demonstrate that our method can recognize and complete arbitrary objects not captured in canonical semantic vocabularies (Fig.
- **p. 4 / 3. Method - extractive PDF cue:** Our method takes a semantic vocabulary consisting of free-form semantic class descriptions only at test time.
- **p. 4 / 3.2. Learning To Complete Objects - extractive PDF cue:** The backbone consists of a sparse feature encoder (●) (Choy et al., 2019) followed by a dense 3D convolutional block (●).
- **p. 5 / 3.2. Learning To Complete Objects - extractive PDF cue:** We estimate scene-level occupancy using a multiscale sparse generative decoder that consists of decoder blocks D, two occupancy heads Bo and Bs, and a pseudo-semantic ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | We believe these are promising directions for future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Table 7. Number of CLIP prototypes. We evaluate SSC/PSC performance on SemanticKITTI when varying the number of CLIP ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We employ the LODE variant that does not use any semantic labels. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Fully supervised baselines have a clear advantage over CAL as they train on closed-set, noise-free annotations with full ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Learning To Complete Objects), p. 3 (3. Method), p. 5 (3.2. Learning To Complete Objects), p. 4 (3.1. Mining 3D Shape Priors From Unlabeled Data). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.2. Learning To Complete Objects), p. 3 (3. Method), p. 5 (3.2. Learning To Complete Objects), p. 4 (3.1. Mining 3D Shape Priors From Unlabeled Data), objective p. 5 (3.2. Learning To Complete Objects), p. 5 (3.2. Learning To Complete Objects).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
