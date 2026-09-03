# Problem - ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.08830; PDF retrieval source: https://arxiv.org/pdf/1912.08830. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): However, these methods and datasets are restricted to 2D images, where object localization fails to capture the true 3D extent of an object (see Fig.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** In recent years, there has been tremendous progress in both semantic understanding and localization of objects in 2D images from natural language (also known as ...
- **p. 2 / 1 Introduction - extractive body cue:** Flickr30K Entities [47] have enabled the development of various methods for visual grounding in 2D [23, 22, 39].
- **p. 2 / 1 Introduction - extractive body cue:** However, these methods and datasets are restricted to 2D images, where object localization fails to capture the true 3D extent of an object (see Fig.
- **p. 2 / 1 Introduction - extractive body cue:** This is a limitation for applications ranging from assistive robots to AR/VR agents where understanding the global 3D context and the physical size is important, ...
- **p. 2 / 1 Introduction - extractive body cue:** [31] looked at coreference in 3D, but was limited to single-view RGB-D images.
- **p. 6 / 5 Method - extractive body cue:** Our architecture consists of two main modules: 1) detection & encoding; 2) fusion & localization (Fig.
- **p. 7 / 5 Method - extractive body cue:** 5.2 Network Architecture Our method takes as input the preprocessed point cloud P′ and the word embedding sequence W representing the input description and outputs ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these methods and datasets are restricted to 2D images, where object localization fails to capture the true 3D extent of an ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The detection & encoding module encodes the input point cloud and description, and outputs the object proposals and the language embedding, which ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | detection, encoding, module, encodes, input, point, cloud, description, outputs, object | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | ScanRefer, architecture, PointNet, backbone, takes, input, point, cloud | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: detection, encoding, module, encodes, input, point, cloud, description, outputs, object | p. 6 (5 Method), p. 7 (5 Method), p. 7 (5 Method) |
| Decision / output variable | geometry/map/query r; body terms: architecture, consists, main, modules, detection, encoding, fusion, localization | p. 6 (5 Method), p. 7 (5 Method), p. 8 (5 Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: then, cross-entropy, loss, localization, Lloc, language, object, classification | p. 7 (5 Method), p. 8 (5 Method), p. 8 (5 Method), p. 9 (5 Method), p. 9 (5 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (5 Method), p. 8 (5 Method), p. 9 (5 Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 10 (6 Experiments), p. 12 (Figure/Table caption), p. 10 (6 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** This is a limitation for applications ranging from assistive robots to AR/VR agents where understanding the global 3D context and the physical size is important, ...

## What the Paper Changes

PDF body contribution framing (p. 6 (5 Method), p. 7 (5 Method), p. 8 (5 Method), p. 8 (5 Method), p. 2 (1 Introduction)): Our architecture consists of two main modules: 1) detection & encoding; 2) fusion & localization (Fig.

- **p. 7 / 5 Method - extractive body cue:** 5.2 Network Architecture Our method takes as input the preprocessed point cloud P′ and the word embedding sequence W representing the input description and outputs ...
- **p. 8 / 5 Method - extractive body cue:** Conceptually, our localization pipeline consists of the following four stages: detection, encoding, fusion and localization.
- **p. 8 / 5 Method - extractive body cue:** Next, the proposal module takes in the point clusters and processes those clusters to predict the objectness mask Dobjn ∈RM×1 and the axis-aligned bounding boxes ...
- **p. 2 / 1 Introduction - extractive body cue:** Flickr30K Entities [47] have enabled the development of various methods for visual grounding in 2D [23, 22, 39].

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 13 | In contrast, even provided with a pool of ground truth proposals, OracleRefer sometimes still fails to predict correct ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | We show examples where our method produced good predictions (blue block) as well as failure cases (orange block). | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | Some failure cases of our method are displayed in the orange block in Fig. | reported limitation/failure wording; scope must be verified |
| body cue at p. 33 | Fig. 17: Additional qualitative analysis in the "unique" scenarios where there is only one object from a certain ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (5 Method), p. 7 (5 Method), p. 7 (5 Method), p. 8 (5 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 6 (5 Method), p. 7 (5 Method), p. 7 (5 Method), p. 8 (5 Method), objective p. 7 (5 Method), p. 8 (5 Method), p. 8 (5 Method), p. 9 (5 Method), p. 9 (5 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
