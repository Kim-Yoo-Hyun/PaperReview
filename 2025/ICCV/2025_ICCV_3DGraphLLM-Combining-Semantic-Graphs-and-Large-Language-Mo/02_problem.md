# Problem - 3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction)): However, existing methods [7, 8, 22, 24] that use learnable 3D scene representations for vision-language tasks typically rely only on spatial coordinates and fail to incorporate semantic relationships between objects ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** A 3D scene graph represents a compact scene model by capturing both the objects present and the semantic relationships between them, making it a promising ...
- **p. 1 / Abstract - extractive body cue:** To effectively interact with users, an embodied intelligent agent should be able to answer a wide range of natural language queries about the surrounding 3D ...
- **p. 1 / Abstract - extractive body cue:** Large Language Models (LLMs) are beneficial solutions for user-robot interaction due to their natural language understanding and reasoning abilities.
- **p. 1 / Abstract - extractive body cue:** Recent methods for learning scene representations have shown that adapting these representations to the 3D world can significantly improve the quality of LLM responses.
- **p. 1 / Abstract - extractive body cue:** However, existing methods typically rely only on geometric information, such as object coordinates, and overlook the rich semantic relationships between objects.
- **p. 2 / 1. Introduction - extractive body cue:** However, existing methods [7, 8, 22, 24] that use learnable 3D scene representations for vision-language tasks typically rely only on spatial coordinates and fail to ...
- **p. 1 / 1. Introduction - extractive body cue:** A common setup of this problem assumes access to a 3D reconstruction of the scene, such as a point cloud, mesh, or NeRF.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, existing methods [7, 8, 22, 24] that use learnable 3D scene representations for vision-language tasks typically rely only on spatial coordinates ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Our approach uses a set of point clouds of scene objects as input. | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | uses, point, clouds, scene, objects, input, obtained, either, ground-truth, annotations | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | One, advantages, only, requires, point, cloud, coordinates, input | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: uses, point, clouds, scene, objects, input, obtained, either, ground-truth, annotations | p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. Model Architecture) |
| Decision / output variable | path/waypoint/velocity; body terms: summarize, contributions, follows, introduce, DGraphLLM, first, creating, learnable | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Model Architecture) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: During, training, optimize, trainable, parameters, language, model, projection | p. 5 (3.3. Training Strategy) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3. Training Strategy), p. 5 (3.3. Training Strategy), p. 4 (3.1. Model Architecture) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.2. Ablation Studies) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** A common setup of this problem assumes access to a 3D reconstruction of the scene, such as a point cloud, mesh, or NeRF.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Model Architecture), p. 3 (3. Method), p. 4 (3.1. Model Architecture)): To summarize, our contributions are as follows: • We introduce 3DGraphLLM, the first method for creating a learnable 3D scene graph representation specifically designed for LLMs.

- **p. 2 / 1. Introduction - extractive body cue:** It enables semantic relationships between objects in a scene to be mapped directly into the LLM's token embedding space. • We propose an algorithm that ...
- **p. 3 / 3.1. Model Architecture - extractive body cue:** Thus, the set V of vertices of the graph consists of n point clouds {Pi}n i=1, where Pi ∈Rmi×6.
- **p. 3 / 3. Method - extractive body cue:** A scene graph consists of nodes representing the objects and edges corresponding to semantic relationships between them.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** We introduce trainable layers to map the extracted graph node and edge features into the token embedding space of a pre-trained LLM.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | A limitation of the method is a significant increase in resource consumption with an increase in the edge ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Our approach falls into the category of "LLM-based models" that consider different tasks as different user queries to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Another important aspect for further work is the creation of methods for generating semantic relations between objects that ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | It is worth noting that the n-gram-based evaluation metrics used in scene captioning and question answering benchmarks are ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. Model Architecture), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. Model Architecture), p. 1 (1. Introduction), objective p. 5 (3.3. Training Strategy).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
