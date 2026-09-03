# Problem - SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminary of LMMs)): However, a significant gap remains: previous works [2, 14, 16] have primarily focused on 3D distance relationships, overlooking the crucial role of 3D object orientation.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Humans naturally understand 3D spatial relationships, enabling complex reasoning like predicting collisions of vehicles from different directions.
- **p. 1 / Abstract - extractive body cue:** Current large multimodal models (LMMs), however, lack of this capability of 3D spatial reasoning.
- **p. 1 / Abstract - extractive body cue:** This limitation stems from the scarcity of 3D training data and the bias in current model designs toward 2D data.
- **p. 1 / Abstract - extractive body cue:** In this paper, we systematically study the impact of 3D-informed data, architecture, and training setups, introducing SpatialLLM, a large multi-modal model with advanced 3D spatial ...
- **p. 1 / Abstract - extractive body cue:** To address data limitations, we develop two types of 3D-informed training datasets: (1) 3D-informed probing data focused on object's 3D location and orientation, and (2) ...
- **p. 1 / 1. Introduction - extractive body cue:** However, a significant gap remains: previous works [2, 14, 16] have primarily focused on 3D distance relationships, overlooking the crucial role of 3D object orientation.
- **p. 1 / 1. Introduction - extractive body cue:** Collecting a small set of high-quality 3D-aware data to tackle the first challenge is feasible, albeit labor-intensive, using readily available tools.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, a significant gap remains: previous works [2, 14, 16] have primarily focused on 3D distance relationships, overlooking the crucial role of ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Existing pretraining and visual instruction tuning data for LMMs [41, 58] focused on detailed descriptions and conversations about scenes, appearances, and actions, ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Existing, pretraining, visual, instruction, tuning, data, LMMs, focused, detailed, descriptions | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | compound, design, simultaneously, considers, D-informed, data, architecture, training | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Existing, pretraining, visual, instruction, tuning, data, LMMs, focused, detailed, descriptions | p. 4 (3.2.1. Challenges of 3D spatial reasoning), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3. Compound 3D-Informed Design) |
| Decision / output variable | geometry/map/query r; body terms: Second, novel, compound, D-informed, design, introduces, improvements, across | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methods) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: stage, focuses, developing, foundational, visual, representations, often, reconstructionbased | p. 3 (3.1. Preliminary of LMMs), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3.1. Design space) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3.1. Design space), p. 8 (Model), p. 8 (Model) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 4 (3.2.2. SpatialVQA for Evaluation), p. 4 (3.2.2. SpatialVQA for Evaluation), p. 7 (4.2. Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Collecting a small set of high-quality 3D-aware data to tackle the first challenge is feasible, albeit labor-intensive, using readily available tools.
- **p. 2 / 1. Introduction - extractive body cue:** This limitation suggests that a more holistic approach is necessary.
- **p. 2 / 1. Introduction - extractive body cue:** Addressing this gap, we aim to incorporate 3D orientation relationships-converted from ImageNet3D [17]-into our data engine, making us the first to enable complex spatial reasoning ...
- **p. 3 / 3.1. Preliminary of LMMs - extractive body cue:** Prior works [39, 41, 46, 58] repurpose VQA benchmarks [22, 32] into instruction-tuning datasets.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methods), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3.1. Design space)): Second, we propose a novel compound 3D-informed design that introduces improvements across multiple dimensions, leading to our proposed SpatialLLM model.

- **p. 2 / 1. Introduction - extractive body cue:** Third, we present the first comprehensive search over the LMM design space for spatial reasoning tasks and propose a roadmap towards developing state-of-the-art models in ...
- **p. 3 / 3. Methods - extractive body cue:** We present the task of reasoning 3D spatial relationships and explain the challenges LMMs face when answering these questions in Sec.
- **p. 3 / 3.1. Preliminary of LMMs - extractive body cue:** A standard LMM [39, 41] consists of a visual encoder to process the image, a multimodal connector to transform the visual feature to visual token, ...
- **p. 5 / 3.3.1. Design space - extractive body cue:** 3.2.1, we propose new training setups that aim to improve 3D awareness and advance the 3D spatial reasoning capabilities.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | Our SpatialVQA distinguishes itself from all previous spatial reasoning benchmarks in the sense that all questions require different ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Interestingly, although SpatialVLM [14] (implemented in SpaceLLaVA [2]) outperforms other open-source models in overall performance, it falls short ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We will consider models with additional inputs in future work. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3.2.1. Challenges of 3D spatial reasoning), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3. Compound 3D-Informed Design), p. 6 (3.3.1. Design space). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminary of LMMs), interface p. 4 (3.2.1. Challenges of 3D spatial reasoning), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3. Compound 3D-Informed Design), p. 6 (3.3.1. Design space), objective p. 3 (3.1. Preliminary of LMMs), p. 3 (3.1. Preliminary of LMMs), p. 5 (3.3.1. Design space).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
