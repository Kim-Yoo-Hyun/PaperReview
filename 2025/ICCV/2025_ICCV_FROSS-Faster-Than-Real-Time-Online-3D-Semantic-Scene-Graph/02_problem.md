# Problem - FROSS: Faster-Than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Problem Definition)): Real-world applications, however, present open-world challenges where environments often exceed known spatial boundaries and contain previously unseen spaces [27].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** The ability to abstract complex 3D environments into simplified and structured representations is crucial across various domains.
- **p. 1 / Abstract - extractive PDF cue:** 3D semantic scene graphs (SSGs) achieve this by representing objects as nodes and their interrelationships as edges, facilitating high-level scene understanding.
- **p. 1 / Abstract - extractive PDF cue:** Existing methods for 3D SSG generation, however, face significant challenges, including high computational demands and non-incremental processing that hinder their suitability for real-time open-world applications.
- **p. 1 / Abstract - extractive PDF cue:** To address this issue, we propose FROSS (Faster-thanReal-Time Online 3D Semantic Scene Graph Generation), an innovative approach for online and faster-than-realtime 3D SSG generation that ...
- **p. 1 / Abstract - extractive PDF cue:** This framework eliminates the dependency on precise and computationallyintensive point cloud processing.
- **p. 1 / 1. Introduction - extractive PDF cue:** Real-world applications, however, present open-world challenges where environments often exceed known spatial boundaries and contain previously unseen spaces [27].
- **p. 2 / 1. Introduction - extractive PDF cue:** These challenges, therefore, provide promising avenues for further innovative research contributions.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Real-world applications, however, present open-world challenges where environments often exceed known spatial boundaries and contain previously unseen spaces [27]. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Merging (Section 3.4) CNN Backbone & Encoder Self-Attention Layer 0 Self-Attention Layer 1 Self-Attention Layer N Hidden Layers Self-Attention Features RT-DETR Detected ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | Merging, Section, CNN, Backbone, Encoder, Self-Attention, Layer, Hidden, Layers, Features | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | observation, motivates, alternative, online, real-time, SSG, generation, inferring | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Merging, Section, CNN, Backbone, Encoder, Self-Attention, Layer, Hidden, Layers, Features | p. 4 (3.3. Lifting 2D SG to 3D), p. 3 (3.2. Overview of Framework), p. 2 (1. Introduction) |
| Decision / output variable | path/waypoint/velocity; body terms: main, contributions, summarized, follows, introduce, FROSS, innovative, methodology | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Given, sequence, input, images, primary, objective, construct, SSG | p. 3 (3.1. Problem Definition), p. 4 (3.3. Lifting 2D SG to 3D), p. 4 (3.3. Lifting 2D SG to 3D), p. 5 (3.4. Merging 3D SSGs), p. 3 (3.1. Problem Definition) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Merging 3D SSGs), p. 3 (3.1. Problem Definition), p. 7 (4.2. Implementation Details) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (4.3. Quantitative Results), p. 7 (4.3. Quantitative Results), p. 5 (4.1.1. Datasets) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** These challenges, therefore, provide promising avenues for further innovative research contributions.
- **p. 2 / 1. Introduction - extractive PDF cue:** Given these limitations, the aim of this study is to develop a method for faster-than-real-time online SSG generation.
- **p. 1 / 1. Introduction - extractive PDF cue:** 3D seChair Cabinet TV TV Above Under Chair Cabinet Near TV Chair Cabinet Merge Input Image Sequence 3D Semantic Scene Graph Lift Objects to 3D ...
- **p. 3 / 3.1. Problem Definition - extractive PDF cue:** The primary problem concerned in this study is the online generation of 3D SSGs for environments where the complete scene structure remains unknown a priori.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Definition), p. 1 (1. Introduction)): The main contributions of the paper can be summarized as follows: • We introduce FROSS, an innovative methodology for online real-time generation of 3D SSGs.

- **p. 1 / 1. Introduction - extractive PDF cue:** We introduce FROSS, an online real-time 3D semantic scene graph generation method that leverages and integrates 2D scene graphs.
- **p. 2 / 1. Introduction - extractive PDF cue:** FROSS demonstrates superior performance and significantly faster processing speeds compared to existing baseline methods. • We propose a new merging algorithm based on Gaussian distributions ...
- **p. 3 / 3.1. Problem Definition - extractive PDF cue:** The graph G consists of a set of nodes V and their corresponding directed edges E.
- **p. 1 / 1. Introduction - extractive PDF cue:** FROSS represents objects as 3D Gaussian distributions and operates without requiring 3D reconstruction. mantic scene graphs (SSGs) [31] extend this representation with an emphasis on ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | However, its merging mechanism fails to suppress duplicate detections, which hinders relationship aggregation and leads to significantly lower ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This substantiates the advantages of lifting scene graphs from 2D images over direct point cloud reasoning [31, 34, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.3. Lifting 2D SG to 3D), p. 3 (3.2. Overview of Framework), p. 2 (1. Introduction), p. 3 (3.1. Problem Definition). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Problem Definition), interface p. 4 (3.3. Lifting 2D SG to 3D), p. 3 (3.2. Overview of Framework), p. 2 (1. Introduction), p. 3 (3.1. Problem Definition), objective p. 3 (3.1. Problem Definition), p. 4 (3.3. Lifting 2D SG to 3D), p. 4 (3.3. Lifting 2D SG to 3D), p. 5 (3.4. Merging 3D SSGs), p. 3 (3.1. Problem Definition).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
