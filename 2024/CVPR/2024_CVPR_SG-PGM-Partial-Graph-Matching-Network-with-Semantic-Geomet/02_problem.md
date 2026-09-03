# Problem - SG-PGM: Partial Graph Matching Network with Semantic Geometric Fusion for 3D Scene Graph Alignment and Its Downstream Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Xie_SG-PGM_Partial_Graph_Matching_Network_with_Semantic_Geometric_Fusion_for_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Xie_SG-PGM_Partial_Graph_Matching_Network_with_Semantic_Geometric_Fusion_for_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): SGAligner [34] is the first work specifically focusing on this problem.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Scene graphs have been recently introduced into 3D spatial understanding as a comprehensive representation of the scene.
- **p. 1 / Abstract - extractive body cue:** The alignment between 3D scene graphs is the first step of many downstream tasks such as scene graph aided point cloud registration, mosaicking, overlap checking, ...
- **p. 1 / Abstract - extractive body cue:** In this work, we treat 3D scene graph alignment as a partial graph-matching problem and propose to solve it with a graph neural network.
- **p. 1 / Abstract - extractive body cue:** We reuse the geometric features learned by a point cloud registration method and associate the clustered point-level geometric features with the node-level semantic feature via ...
- **p. 1 / Abstract - extractive body cue:** Partial matching is enabled by using a learnable method to select the top-k similar node pairs.
- **p. 1 / 1. Introduction - extractive body cue:** SGAligner [34] is the first work specifically focusing on this problem.
- **p. 1 / 1. Introduction - extractive body cue:** One of the main problems of the aforementioned applications is searching for the partial alignment of two or more 3D scene graphs.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | SGAligner [34] is the first work specifically focusing on this problem. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | In this work, Sarkar et al. proposed a neural network that learns a joint multi-modal embedding encoded with semantic, geometric, and structural ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Sarkar, neural, network, learns, joint, multi-modal, embedding, encoded, semantic, geometric | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Thus, scene, graph, encoder, outputs, multi-layers, node, embedding | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Sarkar, neural, network, learns, joint, multi-modal, embedding, encoded, semantic, geometric | p. 1 (1. Introduction), p. 3 (3.1. Scene Graph Matching Network), p. 4 (3.1. Scene Graph Matching Network) |
| Decision / output variable | path/waypoint/velocity; body terms: consists, finite, object, nodes, adjacency, matrix, node, feature | p. 3 (3.1. Scene Graph Matching Network), p. 4 (3.2. Point to Scene Graph Feature Fusion), p. 4 (3.3. Super-point Matching Rescoring) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: follow, further, relax, constraint, Quadratic, Assignment, Problem, Linear | p. 3 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network), p. 5 (3.4. Loss Functions), p. 5 (3.4. Loss Functions), p. 4 (3.2. Point to Scene Graph Feature Fusion), p. 4 (3.2. Point to Scene Graph Feature Fusion) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Loss Functions), p. 5 (3.4. Loss Functions), p. 4 (3.1. Scene Graph Matching Network) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 7 (4.2. Point Cloud Registration and Mosaicking), p. 6 (4.1. Scene Graph Alignment and Overlap Checking) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** One of the main problems of the aforementioned applications is searching for the partial alignment of two or more 3D scene graphs.
- **p. 2 / 1. Introduction - extractive body cue:** Addressing the aforementioned aspects, we first define the 3D scene graph alignment as a partial graph matching problem.
- **p. 2 / 1. Introduction - extractive body cue:** Moreover, we design a Superpoint Matching Rescoring method using the predicted scene graph node alignment as the semantic level prior to guiding the point correspondence ...

## What the Paper Changes

PDF body contribution framing (p. 3 (3.1. Scene Graph Matching Network), p. 4 (3.2. Point to Scene Graph Feature Fusion), p. 4 (3.3. Super-point Matching Rescoring), p. 5 (3.3. Super-point Matching Rescoring), p. 5 (3.3. Super-point Matching Rescoring)): It consists of a finite set of object nodes V = {v1, v2, ..., vM}, an adjacency matrix A ∈{0, 1}M×M, a node feature matrix X ∈RM×· and a edge ...

- **p. 4 / 3.2. Point to Scene Graph Feature Fusion - extractive body cue:** In that case, the subgraph that only consists of these nodes is automorphism.
- **p. 4 / 3.3. Super-point Matching Rescoring - extractive body cue:** We propose the Super-point Matching Rescoring method that uses the semantic similarity learned by our scene graph 28404
- **p. 5 / 3.3. Super-point Matching Rescoring - extractive body cue:** Therefore, our method can be easily adapted to most feature-based registration methods, bot point-level matching [13] and super-point matching [16, 31, 50].
- **p. 5 / 3.3. Super-point Matching Rescoring - extractive body cue:** Because our rescoring method does not introduce any learnable parameters, we do not need to train our method with the point cloud registration method jointly.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Moreover, our scene graph alignment method remains decoupled from registration and robust to scene dynamics and noises. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | For future work, we would like to explore the approach for using semantic priors from scene graph alignment ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We trained SGAligner with random T and Gaussian noise as augmentation (SGA*). | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | This demonstrates that fusing graphs and geometric features with our method is robust against rotation. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1. Introduction), p. 3 (3.1. Scene Graph Matching Network), p. 4 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 1 (1. Introduction), p. 3 (3.1. Scene Graph Matching Network), p. 4 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network), objective p. 3 (3.1. Scene Graph Matching Network), p. 3 (3.1. Scene Graph Matching Network), p. 5 (3.4. Loss Functions), p. 5 (3.4. Loss Functions), p. 4 (3.2. Point to Scene Graph Feature Fusion), p. 4 (3.2. Point to Scene Graph Feature Fusion).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
