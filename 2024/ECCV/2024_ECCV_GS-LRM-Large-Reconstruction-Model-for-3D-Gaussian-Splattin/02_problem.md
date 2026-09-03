# Problem - GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3212_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): Reconstructing a 3D scene from image captures is both a central problem and a long-standing challenge in computer vision.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** Reconstructing a 3D scene from image captures is both a central problem and a long-standing challenge in computer vision.
- **p. 1 / 1 Introduction - extractive body cue:** Traditionally, high-quality 3D reconstruction relies on complex photogrammetry systems [23, 48,50] and requires a dense set of multi-view images.
- **p. 1 / 1 Introduction - extractive body cue:** Recent advancements in neural representations and differentiable rendering [9, 30, 40, 41] have shown superior reconstruction and rendering quality, by optimizing renderings on a per-scene ...
- **p. 1 / 1 Introduction - extractive body cue:** However, these methods are slow and still require a large number of input views.
- **p. 1 / 1 Introduction - extractive body cue:** Recently, transformer-based 3D large reconstruction models (LRMs) have been proposed, learning general 3D reconstruction priors from vast collections of 3D objects and achieving sparse-view 3D ...
- **p. 1 / 1 Introduction - extractive body cue:** This leads to challenges in training and rendering speeds, preserving fine details, and scaling to large scenes beyond object-centric inputs. *
- **p. 4 / 3 Method - extractive body cue:** In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Reconstructing a 3D scene from image captures is both a central problem and a long-standing challenge in computer vision. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Unlike previous LRMs that require careful designs of additional (triplane) NeRF tokens for reconstruction, we align input (2D images) and output (3D ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Unlike, previous, LRMs, require, careful, designs, additional, triplane, NeRF, tokens | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | tokenize, posed, input, images, patchify, operator, Prompt, plush | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Unlike, previous, LRMs, require, careful, designs, additional, triplane, NeRF, tokens | p. 2 (1 Introduction), p. 6 (3 Method), p. 4 (3 Method) |
| Decision / output variable | geometry/map/query r; body terms: section, present, technical, details, including, architecture, transformer-based, model | p. 4 (3 Method), p. 2 (1 Introduction), p. 5 (3 Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Loss, Functions, During, training, render, images, supervision, views | p. 6 (3 Method), p. 6 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 Method), p. 6 (3 Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** This leads to challenges in training and rendering speeds, preserving fine details, and scaling to large scenes beyond object-centric inputs. *

## What the Paper Changes

PDF body contribution framing (p. 4 (3 Method), p. 2 (1 Introduction), p. 5 (3 Method), p. 2 (1 Introduction), p. 6 (3 Method)): In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose GS-LRM, a novel transformer-based large reconstruction model that predicts 3D Gaussian primitives [30] from sparse input images, enabling fast and ...
- **p. 5 / 3 Method - extractive body cue:** 2) and consists of Pre-LayerNorm [3], multi-head Self-Attention [60] and MLP.
- **p. 2 / 1 Introduction - extractive body cue:** The core of our approach is a simple and scalable transformer-based network architecture that predicts per-pixel Gaussians.
- **p. 6 / 3 Method - extractive body cue:** This property allows us to better handle high-frequency details in the inputs and large-scale scene captures.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 13 | 4.6 Limitations Although our method shows high-quality reconstruction results from posed sparse images, there are still a few ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | We hope that our work can inspire more future work in the space of data-driven feed-forward 3D reconstruction. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The Triplane-LRM cannot reconstruct high-frequency details (top left and top right) and thin structures (bottom left) well. | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Please refer to our project page for the video and interactive rendering results. the view frustum, which means ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 6 (3 Method), p. 4 (3 Method), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 2 (1 Introduction), p. 6 (3 Method), p. 4 (3 Method), p. 2 (1 Introduction), objective p. 6 (3 Method), p. 6 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
