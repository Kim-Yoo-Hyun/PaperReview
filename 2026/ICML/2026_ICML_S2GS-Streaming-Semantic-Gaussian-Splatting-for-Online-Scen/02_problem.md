# Problem - S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=CbWCaD8tRC; PDF retrieval source: https://openreview.net/pdf/fec4864d5571755c82ad1d076f9a8e3e4ca69cf8.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): However, most existing approaches remain limited to streaming modeling of geometry and appearance, lacking semantic scene understanding and instance-level, decomposable representations, and thus falling short for downstream applications ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Existing offline feed-forward methods for joint scene understanding and reconstruction on long image streams often repeatedly perform global computation over an ever-growing set of past ...
- **p. 1 / Abstract - extractive body cue:** We propose Streaming Semantic Gaussian Splatting (S2GS), a strictly causal, incremental 3D Gaussian semantic field framework: it does not leverage future frames and continuously updates ...
- **p. 1 / Abstract - extractive body cue:** S2GS adopts a geometry-semantic decoupled dual-backbone design: the geometry branch performs causal modeling to drive incremental Gaussian updates, while the semantic branch leverages a 2D ...
- **p. 1 / Abstract - extractive body cue:** Experiments show that S2GS matches or outperforms strong offline baselines on joint reconstruction-and-understanding benchmarks, while significantly improving longhorizon scalability: it processes 1,000+ frames with much ...
- **p. 1 / 1. Introduction - extractive body cue:** Recently, feed-forward methods (Xu et al., 2025; Sun et al., 2025; Tian et al., 2025) built upon 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) ...
- **p. 1 / 1. Introduction - extractive body cue:** However, most existing approaches remain limited to streaming modeling of geometry and appearance, lacking semantic scene understanding and instance-level, decomposable representations, and thus falling short ...
- **p. 1 / 1. Introduction - extractive body cue:** As shown in Figure 1, even on an H200 GPU equipped with 140 GB of VRAM, SIU3R (Xu et al., 2025) still encounters an out-ofmemory ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, most existing approaches remain limited to streaming modeling of geometry and appearance, lacking semantic scene understanding and instance-level, decomposable representations, and ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | This naturally imposes a causal constraint on online joint reconstruction and understanding: at each time step, the model can only rely on ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | naturally, imposes, causal, constraint, online, joint, reconstruction, understanding, time, step | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | provide, semantic, teacher, signal, apply, predicted, mask, input | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: naturally, imposes, causal, constraint, online, joint, reconstruction, understanding, time, step | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Language-driven Open-vocabulary Segmentation) |
| Decision / output variable | geometry/map/query r; body terms: S2GS, strictly, causal, reprocessing-free, framework, online, joint, reconstruction | p. 2 (1. Introduction), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Under, causal, constraint, Transformer, aggregates, information, form, geometry | p. 3 (3.2. Causal Transformer for 3D Gaussian Regression), p. 3 (3.2. Causal Transformer for 3D Gaussian Regression), p. 4 (3.3. Online Instance Tracking and Semantic), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 4 (3.2. Causal Transformer for 3D Gaussian Regression), p. 5 (3.4. Language-driven Open-vocabulary Segmentation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 4 (3.2. Causal Transformer for 3D Gaussian Regression) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (4.1. Experimental Setup), p. 6 (82.49 Method), p. 8 (4.3. Ablation Studies) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** As shown in Figure 1, even on an H200 GPU equipped with 140 GB of VRAM, SIU3R (Xu et al., 2025) still encounters an out-ofmemory ...
- **p. 2 / 1. Introduction - extractive body cue:** S2GS addresses two core challenges in strictly causal online joint modeling: (i) maintaining stable geometry without future-view corrections, and (ii) preserving temporally consistent instance identities ...
- **p. 2 / 1. Introduction - extractive body cue:** Under this constraint, how to incorporate stable and temporally consistent semantic understanding while preserving the scalability of streaming inference remains an open problem.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 2 (1. Introduction), p. 3 (3.2. Causal Transformer for 3D Gaussian Regression), p. 4 (3.2. Causal Transformer for 3D Gaussian Regression)): We propose S2GS, a strictly causal and reprocessing-free framework for online joint 3D reconstruction and scene understanding, which incrementally maintains scene geometry, appearance, and an instance-level semantic field.

- **p. 5 / 3.4. Language-driven Open-vocabulary Segmentation - extractive body cue:** To bridge this gap, we introduce a lightweight Query Semantic Projector gθ(·) that maps each per-frame query embedding to the 2D foundation vision model (Tschannen ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: 1.
- **p. 3 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** (1) This design allows parallel processing of training clips while remaining equivalent to an autoregressive causal model.
- **p. 4 / 3.2. Causal Transformer for 3D Gaussian Regression - extractive body cue:** Semantic confidence is lifted to the 3D Gaussian field and decoded via splatting, enabling unified novel view synthesis, semantic segmentation, instance segmentation, and panoptic segmentation ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | As shown in Table 2, under the extremely sparse 2-view setting, S2GS does not achieve the best PSNR/SSIM. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | This is expected, since offline baselines can exploit non-causal cross-view aggregation over the full input set to better ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Nevertheless, under the same training configuration, S2GS achieves better reconstruction and semantic performance on both datasets, demonstrating stronger ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 2 (1. Introduction), objective p. 3 (3.2. Causal Transformer for 3D Gaussian Regression), p. 3 (3.2. Causal Transformer for 3D Gaussian Regression), p. 4 (3.3. Online Instance Tracking and Semantic), p. 5 (3.4. Language-driven Open-vocabulary Segmentation), p. 4 (3.2. Causal Transformer for 3D Gaussian Regression), p. 5 (3.4. Language-driven Open-vocabulary Segmentation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
