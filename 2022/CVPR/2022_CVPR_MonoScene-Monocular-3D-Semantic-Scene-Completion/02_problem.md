# Problem - MonoScene: Monocular 3D Semantic Scene Completion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.00726; PDF retrieval source: https://arxiv.org/pdf/2112.00726. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): The SSC literature mainly relies on cross-entropy loss which considers each voxel independently, lacking context awareness.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** MonoScene proposes a 3D Semantic Scene Completion (SSC) framework, where the dense geometry and semantics of a scene are inferred from a single monocular RGB ...
- **p. 1 / Abstract - extractive PDF cue:** Different from the SSC literature, relying on 2.5 or 3D input, we solve the complex problem of 2D to 3D scene reconstruction while jointly inferring ...
- **p. 1 / Abstract - extractive PDF cue:** Our framework relies on successive 2D and 3D UNets, bridged by a novel 2D3D features projection inspired by optics, and introduces a 3D context relation ...
- **p. 1 / Abstract - extractive PDF cue:** Along with architectural contributions, we introduce novel global scene and local frustums losses.
- **p. 1 / Abstract - extractive PDF cue:** Experiments show we outperform the literature on all metrics and datasets while hallucinating plausible scenery even beyond the camera field of view.
- **p. 1 / 1. Introduction - extractive PDF cue:** The SSC literature mainly relies on cross-entropy loss which considers each voxel independently, lacking context awareness.
- **p. 1 / 1. Introduction - extractive PDF cue:** Our framework infers dense semantic scenes, hallucinating scenery outside the field of view of the image (dark voxels, right). and outdoor scenes.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The SSC literature mainly relies on cross-entropy loss which considers each voxel independently, lacking context awareness. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The output map F3D is used as 3D UNet input. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | output, F3D, UNet, input, been, almost, exclusively, addressed, inputs, point | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | UNet, bases, pre-trained, EfficientNetB7, taking, input, image, xrgb | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: output, F3D, UNet, input, been, almost, exclusively, addressed, inputs, point | p. 3 (3.1. Features Line of Sight Projection (FLoSP)), p. 2 (3. Method), p. 2 (3. Method) |
| Decision / output variable | geometry/map/query r; body terms: framework, infers, dense, semantic, scenes, hallucinating, scenery, outside | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (3. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: more, generality, loss, Lscal, maximizes, above, class-wise, metrics | p. 2 (3. Method), p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)), p. 4 (3.3. Losses), p. 4 (3.3. Losses) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (3. Method), p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.2.1 Evaluation), p. 5 (4.2.1 Evaluation), p. 5 (4. Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** 3.1). • A 3D Context Relation Prior (3D CRP, Sec.

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)), p. 3 (3.2. 3D Context Relation Prior (3D CRP))): Our framework infers dense semantic scenes, hallucinating scenery outside the field of view of the image (dark voxels, right). and outdoor scenes.

- **p. 1 / 1. Introduction - extractive PDF cue:** Here, we present MonoScene which - unlike the literature - relies on a single RGB image to infer the dense 3D voxelized semantic scene working ...
- **p. 2 / 3. Method - extractive PDF cue:** To guide the SSC training, we introduce new complementary losses.
- **p. 3 / 3.2. 3D Context Relation Prior (3D CRP) - extractive PDF cue:** As voxels relations are greedy with N 2 relations for N voxels, we present the lighter supervoxel↔voxel relations.
- **p. 3 / 3.2. 3D Context Relation Prior (3D CRP) - extractive PDF cue:** Here, we propose a 3D Context Relation Prior (3D CRP) layer, inserted at the 3D UNet bottleneck, which learns n-way voxel↔voxel semantic scene-wise relation maps.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Compared to the Whole Scene, the in-FOV performance is higher since it considers visible surfaces, whereas the out-FOV ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Due to the single viewpoint, occlusion artefacts such as distortions are visible along the line of sight in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 2. MonoScene framework. We infer 3D SSC from a single RGB image, leveraging 2D and 3D UNets, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 6. Frustum Proportion Loss. Considering an image di- vided into same-size 2D patches (here, 2×2), each corresponds ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.1. Features Line of Sight Projection (FLoSP)), p. 2 (3. Method), p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 3 (3.1. Features Line of Sight Projection (FLoSP)), p. 2 (3. Method), p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)), objective p. 2 (3. Method), p. 2 (3. Method), p. 3 (3.2. 3D Context Relation Prior (3D CRP)), p. 4 (3.3. Losses), p. 4 (3.3. Losses).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
