# Problem - Rh-3DGS: Robust Open-Vocabulary Scene Understanding via Riemannian Huber Distillation and Manifold-Aware Sampling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=bjtuHOb3vN; PDF retrieval source: https://openreview.net/pdf/8310d4c5a6346eaadb420914138e1711121a0ff8.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction)): (a) RGB(View-1) + zoom-in box (b) Baseline mask (View-1) (c) Baseline multi-view inconsistency (View-1 vs View-2) Problem: Boundary ambiguity & view inconsistency (d) VCD (f) LIC (h) Our multi-view stable(View-1 ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary 3D scene understanding answers free-form text queries over reconstructed scenes.
- **p. 1 / Abstract - extractive body cue:** However, lifting dense 2D foundationmodel embeddings into 3D Gaussian Splatting (3DGS) is still challenging.
- **p. 1 / Abstract - extractive body cue:** Existing 3DGS-based methods often average normalized embeddings in Euclidean space.
- **p. 1 / Abstract - extractive body cue:** This ignores their hyperspherical geometry and can cause feature collapse.
- **p. 1 / Abstract - extractive body cue:** They also distill supervision from all views equally, which amplifies occlusion noise and mixed-depth artifacts.
- **p. 1 / 1. Introduction - extractive body cue:** (a) RGB(View-1) + zoom-in box (b) Baseline mask (View-1) (c) Baseline multi-view inconsistency (View-1 vs View-2) Problem: Boundary ambiguity & view inconsistency (d) VCD (f) ...
- **p. 4 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive body cue:** We propose Visibility-Calibrated Distillation (VCD).

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | (a) RGB(View-1) + zoom-in box (b) Baseline mask (View-1) (c) Baseline multi-view inconsistency (View-1 vs View-2) Problem: Boundary ambiguity & view inconsistency ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Rh-3DGS 𝒊 radius 𝜸 same semantic (in 𝓝) excluded 𝑳𝑳𝑰𝑪 Local consistency Build 𝓝𝒓𝒔𝒆𝒎(𝒊) 𝒙𝒊, sem(𝒊) 𝒇𝒊 LIC semantic radius graph Posed ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Rh-3DGS, radius, same, semantic, excluded, Local, consistency, Build, LIC, graph | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | outputs, per-pixel, weight, reweights, semantic, supervision, compute, expected | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Rh-3DGS, radius, same, semantic, excluded, Local, consistency, Build, LIC, graph | p. 4 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.3. Visibility-Calibrated Distillation (VCD)) |
| Decision / output variable | geometry/map/query r; body terms: Visibility-Calibrated, Distillation, VCD, Visibility-Weighted, echet, Mean, VFM, Low | p. 4 (4.3. Visibility-Calibrated Distillation (VCD)), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 4 (4.3. Visibility-Calibrated Distillation (VCD)) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: optimize, model, end-to-end, Lrgb, LVFM, LLIC, where, photometric | p. 4 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.3. Visibility-Calibrated Distillation (VCD)), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 5 (4.3. Visibility-Calibrated Distillation (VCD)) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (4.1. Problem Formulation and Notation), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), p. 9 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** (a) RGB(View-1) + zoom-in box (b) Baseline mask (View-1) (c) Baseline multi-view inconsistency (View-1 vs View-2) Problem: Boundary ambiguity & view inconsistency (d) VCD (f) ...

## What the Paper Changes

PDF body contribution framing (p. 4 (4.3. Visibility-Calibrated Distillation (VCD)), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 4 (4.3. Visibility-Calibrated Distillation (VCD))): We propose Visibility-Calibrated Distillation (VCD).

- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive body cue:** We propose Visibility-Weighted Fr´echet Mean (VFM).
- **p. 4 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive body cue:** Low accumulated opacity often indicates weak or unstable contributions.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | Figure 2. Overview of Rh-3DGS. Given posed RGB images, a frozen teacher (e.g., SAM/CLIP) provides per-pixel semantic embeddings. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Future work will extend to dynamic scenes, multi-teacher distillation, and more efficient implementations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | 9, activating LIC from the beginning is less effective because pseudoinstances are unstable in the early stage. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We present Rh-3DGS for robust open-vocabulary 3D semantics in 3D Gaussian Splatting. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.3. Visibility-Calibrated Distillation (VCD)), p. 3 (4.1. Problem Formulation and Notation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), interface p. 4 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.3. Visibility-Calibrated Distillation (VCD)), p. 3 (4.1. Problem Formulation and Notation), objective p. 4 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.3. Visibility-Calibrated Distillation (VCD)), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 5 (4.3. Visibility-Calibrated Distillation (VCD)).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
