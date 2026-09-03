# Problem - Depth Anything V2

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2406.09414; PDF retrieval source: https://arxiv.org/pdf/2406.09414. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 4 (1 Introduction), p. 7 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction)): Consequently, despite the astonishing precision of Hypersim [58] or Virtual KITTI [9] (Figure 4b), we cannot expect models trained on them to generalize well in real-world scenes like "crowded people".

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** This work presents Depth Anything V2.
- **p. 1 / Abstract - extractive body cue:** Without pursuing fancy techniques, we aim to reveal crucial findings to pave the way towards building a powerful monocular depth estimation model.
- **p. 1 / Abstract - extractive body cue:** Notably, compared with V1 [89], this version produces much finer and more robust depth predictions through three key practices: 1) replacing all labeled real images ...
- **p. 1 / Abstract - extractive body cue:** Compared with the latest models [31] built on Stable Diffusion, our models are significantly more efficient (more than 10× faster) and more accurate.
- **p. 1 / Abstract - extractive body cue:** We offer models of different scales (ranging from 25M to 1.3B params) to support extensive scenarios.
- **p. 4 / 1 Introduction - extractive body cue:** Consequently, despite the astonishing precision of Hypersim [58] or Virtual KITTI [9] (Figure 4b), we cannot expect models trained on them to generalize well in ...
- **p. 7 / 1 Introduction - extractive body cue:** 6 A New Evaluation Benchmark: DA-2K 6.1 Limitations in Existing Benchmarks In Section 2, we demonstrated that commonly used real training sets have noisy depth ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Consequently, despite the astonishing precision of Hypersim [58] or Virtual KITTI [9] (Figure 4b), we cannot expect models trained on them to ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | This observation is indeed similar to SAM [33] that only releases its pseudo-labeled masks. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | observation, indeed, similar, SAM, only, releases, pseudo-labeled, masks, Precise, depth | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Community, Models, Depth, Anything, Ours, Marigold, Geowizard, DepthFM | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: observation, indeed, similar, SAM, only, releases, pseudo-labeled, masks, Precise, depth | p. 9 (Method), p. 2 (1 Introduction), p. 8 (Method) |
| Decision / output variable | geometry/map/query r; body terms: consists, three, steps, train, reliable, teacher, model, DINOv2-G | p. 6 (1 Introduction), p. 7 (1 Introduction), p. 4 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: MiDaS, proposes, gradient, matching, loss, Lgm, enhance, depth | p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions), p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions), p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions), p. 8 (Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 1 (Figure/Table caption), p. 16 (C.1 Per-scenario accuracy), p. 16 (C.1 Per-scenario accuracy) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 7 / 1 Introduction - extractive body cue:** 6 A New Evaluation Benchmark: DA-2K 6.1 Limitations in Existing Benchmarks In Section 2, we demonstrated that commonly used real training sets have noisy depth ...
- **p. 3 / 1 Introduction - extractive body cue:** However, we find current test sets [70] are too noisy to reflect the true strengths of MDE models.
- **p. 3 / 1 Introduction - extractive body cue:** Black regions are ignored during training. such a challenging goal, no fancy or sophisticated techniques need to be developed.
- **p. 4 / 1 Introduction - extractive body cue:** 3 Challenges in Using Synthetic Data If synthetic data are so advantageous, why are real data still dominating MDE?

## What the Paper Changes

PDF body contribution framing (p. 6 (1 Introduction), p. 7 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction)): It consists of three steps: • train a reliable teacher model based on DINOv2-G purely on high-quality synthetic images. • produce precise pseudo depth on large-scale unlabeled real images. • ...

- **p. 7 / 1 Introduction - extractive body cue:** To address this, we introduce a second pipeline, where we carefully analyze images and manually identify challenging pairs.
- **p. 4 / 1 Introduction - extractive body cue:** In the right side of Figure 4c, we show the fine-grained prediction of a MDE model trained on synthetic images.
- **p. 3 / 1 Introduction - extractive body cue:** Black regions are ignored during training. such a challenging goal, no fancy or sophisticated techniques need to be developed.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | Table 13: Comparison among various pre-trained encoders when purely trained on synthetic images. B.7 Benefit of gradient matching ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 6: Failure cases of the most capable DINOv2-G model when purely trained on synthetic images. Left: the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Table 2: Zero-shot relative depth estimation. Better: AbsRel ↓, δ1 ↑. Solely from the metrics, Depth Anything V2 ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Figure 9: Our proposed evaluation benchmark DA-2K. (a) The annotation pipeline for relative depth between two points. Points ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 9 (Method), p. 2 (1 Introduction), p. 8 (Method), p. 9 (Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 4 (1 Introduction), p. 7 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), interface p. 9 (Method), p. 2 (1 Introduction), p. 8 (Method), p. 9 (Method), objective p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions), p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
