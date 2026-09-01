# Problem - SparseGS: Sparse View Synthesis using 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=O9GMl5UJbe&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): The challenge of learning 3D representations from 2D images has been a longstanding area of interest, but achieving a balance between efficiency and fidelity remains a persistent challenge.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** 3D Gaussian Splatting (3DGS) has recently enabled real-time rendering of unbounded 3D scenes for novel view synthesis.
- **p. 1 / Abstract - extractive PDF cue:** However, this technique requires dense training views to accurately reconstruct 3D geometry.
- **p. 1 / Abstract - extractive PDF cue:** A limited number of input views will significantly degrade reconstruction quality, resulting in artifacts such as "floaters" and "background collapse" at unseen viewpoints.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we introduce SparseGS, an efficient training pipeline designed to address the limitations of 3DGS in scenarios with sparse training views.
- **p. 1 / Abstract - extractive PDF cue:** SparseGS incorporates depth priors, novel depth rendering techniques, and a pruning heuristic to mitigate floater artifacts, alongside an Unseen Viewpoint Regularization module to alleviate background ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The challenge of learning 3D representations from 2D images has been a longstanding area of interest, but achieving a balance between efficiency and fidelity remains ...
- **p. 1 / 1. Introduction - extractive PDF cue:** These issues are further exacerbated when the training set lacks substantial scene coverage, such as in multi-view unbounded scenes [2] (referred as 360-degree scenes in ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The challenge of learning 3D representations from 2D images has been a longstanding area of interest, but achieving a balance between efficiency ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Combined, our pipeline achieves state-of-the-art (SOTA) performance in sparse-input novel view synthesis (NVS) problems, not only on forward-facing datasets but also on ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Combined, pipeline, achieves, state-of-the-art, SOTA, performance, sparse-input, novel, view, synthesis | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | However, DGS, still, suffers, artifacts, caused, inherent, ambiguity | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Combined, pipeline, achieves, state-of-the-art, SOTA, performance, sparse-input, novel, view, synthesis | p. 2 (1. Introduction), p. 6 (3.3. Unseen Viewpoints Regularization (UVR)), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: consists, three, components, designed, function, cohesively, improve, view | p. 3 (3. Methods), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Because, softmax, depth, loss, soft, constraint, there, exist | p. 6 (3.4. Advanced Floater Pruning), p. 4 (3.1. Mode-selection & Softmax-scaling Depth Ren), p. 3 (3. Methods), p. 3 (3. Methods), p. 4 (3.1. Mode-selection & Softmax-scaling Depth Ren), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Methods), p. 4 (3.1. Mode-selection & Softmax-scaling Depth Ren), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 3 (Figure/Table caption), p. 7 (4.2. Comparison), p. 7 (4.2. Comparison) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** These issues are further exacerbated when the training set lacks substantial scene coverage, such as in multi-view unbounded scenes [2] (referred as 360-degree scenes in ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Combined, our pipeline achieves state-of-the-art (SOTA) performance in sparse-input novel view synthesis (NVS) problems, not only on forward-facing datasets but also on 360-degree unbounded scenes, ...
- **p. 2 / 1. Introduction - extractive PDF cue:** resolve the problem of floaters, particularly in unbounded scenes.

## What the Paper Changes

PDF contribution framing (p. 3 (3. Methods), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)), p. 6 (3.4. Advanced Floater Pruning)): Our method consists of three key components designed to function cohesively to improve view consistency and depth accuracy in novel view synthesis: a depth correlation loss, an Unseen Viewpoint Regularization ...

- **p. 2 / 1. Introduction - extractive PDF cue:** Next, we introduce a module designed to tackle background collapse by leveraging a 2D generative diffusion prior [16, 26] and depth warping [22, 44].
- **p. 2 / 1. Introduction - extractive PDF cue:** We propose a novel framework, SparseGS, for training coherent and robust 3D Gaussian representations from limited inputs, outperforming SOTA methods in sparse view synthesis.
- **p. 5 / 3.3. Unseen Viewpoints Regularization (UVR) - extractive PDF cue:** In this section, we propose two regularization methods to improve reconstruction from novel viewpoints: 1).
- **p. 6 / 3.4. Advanced Floater Pruning - extractive PDF cue:** Therefore, we propose a novel pruning operator to remove the Gaussians at false modes at the end of training.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | This limitation actually prompted the introduction of positional encoding [20, 37]. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In contrast, FSGS excels in preserving fine details due to its densification technique but fails to reconstruct background ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In regions with little coverage by input views, we leverage Score Distillation Sampling (SDS) and Depth Warping to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. The quality of 3DGS [12] degrades as the number of input views decreases, particularly in unbounded ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 6 (3.3. Unseen Viewpoints Regularization (UVR)), p. 1 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 6 (3.3. Unseen Viewpoints Regularization (UVR)), p. 1 (1. Introduction), p. 2 (1. Introduction), objective p. 6 (3.4. Advanced Floater Pruning), p. 4 (3.1. Mode-selection & Softmax-scaling Depth Ren), p. 3 (3. Methods), p. 3 (3. Methods), p. 4 (3.1. Mode-selection & Softmax-scaling Depth Ren), p. 5 (3.3. Unseen Viewpoints Regularization (UVR)).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
