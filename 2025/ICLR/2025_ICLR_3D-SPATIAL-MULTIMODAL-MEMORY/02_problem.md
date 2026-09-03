# Problem - 3D-SPATIAL MULTIMODAL MEMORY

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=XYdstv3ySl; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114814. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): We observe two key issues: First, due to the computational limitations, the feature vector dimensions in Gaussian primitives are significantly reduced compared to the original 2D feature maps (typically 16-64 ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** We present 3D Spatial MultiModal Memory (M3), a multimodal memory system designed to retain information about medium-sized static scenes through video sources for visual perception.
- **p. 1 / ABSTRACT - extractive body cue:** By integrating 3D Gaussian Splatting techniques with foundation models, M3 builds a multimodal memory capable of rendering feature representations across granularities, encompassing a wide range ...
- **p. 1 / ABSTRACT - extractive body cue:** In our exploration, we identify two key challenges in previous works on feature splatting: (1) computational constraints in storing high-dimensional features for each Gaussian primitive, ...
- **p. 1 / ABSTRACT - extractive body cue:** To address these challenges, we propose M3 with key components of principal scene components and Gaussian memory attention, enabling efficient training and inference.
- **p. 1 / ABSTRACT - extractive body cue:** To validate M3, we conduct comprehensive quantitative evaluations of feature similarity and downstream tasks, as well as qualitative visualizations to highlight the pixel trace of ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We observe two key issues: First, due to the computational limitations, the feature vector dimensions in Gaussian primitives are significantly reduced compared to the original ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, these models lack the capability to retain the semantic understanding of the scene like humans.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We observe two key issues: First, due to the computational limitations, the feature vector dimensions in Gaussian primitives are significantly reduced compared ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | We formally define the input of M3 as a video sequence with frames, where each frame corresponds to a view V∗. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | formally, define, input, video, sequence, frames, where, frame, corresponds, view | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | evaluate, employ, diverse, foundation, models, including, vision-language, LMM/LLMs | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: formally, define, input, video, sequence, frames, where, frame, corresponds, view | p. 4 (3 METHOD), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION) |
| Decision / output variable | geometry/map/query r; body terms: Specifically, store, original, high-dimensional, feature, maps, memory, bank | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: introduce, optimizable, attribute, queries, Gaussian, primitives, apply, Memory | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 METHOD) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, these models lack the capability to retain the semantic understanding of the scene like humans.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, for larger-scale environments, our understanding tends to remain more coarse and generalized.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 4 (3 METHOD)): Specifically, we propose to store the original high-dimensional 2D feature maps in a memory bank called principal scene components and use the low-dimensional principal queries from 3D Gaussians as indices.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these issues, we present MultiModal Memory (M3), a better integration of Gaussian splatting and multimodal foundation models that efficiently store expressive multimodal memory ...
- **p. 3 / 3 METHOD - extractive body cue:** A real-world visual perception scene (V) consists of both structure (S) and knowledge (I).
- **p. 4 / 3 METHOD - extractive body cue:** We introduce optimizable attribute queries (q) to Gaussian primitives, and apply a Gaussian Memory Attention (Agm) mechanism to produce the final rendered features ( ˆR), ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | SEEM and LLaMA3 features extraction failed on FSplat, which we assume was mainly due to the ground truth ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3 METHOD), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), interface p. 4 (3 METHOD), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
