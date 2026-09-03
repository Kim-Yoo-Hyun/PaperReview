# Problem - Clio: Real-time Task-Driven Open-Set 3D Scene Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2404.13696; PDF retrieval source: https://arxiv.org/pdf/2404.13696. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION)): These approaches, however, leave to the user the difficult task of tuning suitable thresholds to control the number of segments that are extracted from the scene as well as the ...

## PDF Body Digest

- **p. 2 / Abstract - extractive body cue:** Modern tools for class-agnostic image segmentation (e.g., SegmentAnything) and open-set semantic understanding (e.g., CLIP) provide unprecedented opportunities for robot perception and mapping.
- **p. 2 / Abstract - extractive body cue:** While traditional closed-set metricsemantic maps were restricted to tens or hundreds of semantic classes, we can now build maps with a plethora of objects and ...
- **p. 2 / Abstract - extractive body cue:** This leaves us with a fundamental question: what is the right granularity for the objects (and, more generally, for the semantic concepts) the robot has ...
- **p. 2 / Abstract - extractive body cue:** While related work implicitly chooses a level of granularity by tuning thresholds for object detection, we argue that such a choice is intrinsically task-dependent.
- **p. 2 / Abstract - extractive body cue:** The first contribution of this paper is to propose a task-driven 3D scene understanding problem, where the robot is given a list of tasks in ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** These approaches, however, leave to the user the difficult task of tuning suitable thresholds to control the number of segments that are extracted from the ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** This problem can be naturally formulated using the classical Information Bottleneck (IB) [13] theory, which also provides algorithmic approaches for task-driven clustering.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | These approaches, however, leave to the user the difficult task of tuning suitable thresholds to control the number of segments that are ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Our key observation is that if the graph of primitives in input to the algorithm has multiple connected components (e.g., 3D object ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | observation, graph, primitives, input, algorithm, multiple, connected, components, object, segments | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | obtain, semantic, features, places, compute, CLIP, embedding, vector | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: observation, graph, primitives, input, algorithm, multiple, connected, components, object, segments | p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 3 (I. INTRODUCTION), p. 5 (IV. TASK-DRIVEN CLUSTERING) |
| Decision / output variable | path/waypoint/velocity; body terms: Clio, novel, building, task-driven, scene, graphs, real-time, embedded | p. 2 (I. INTRODUCTION), p. 2 (Abstract), p. 3 (I. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: suggested, iteration, compute, Xk-1, measure, fractional, loss, information | p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 5 (IV. TASK-DRIVEN CLUSTERING) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 5 (IV. TASK-DRIVEN CLUSTERING) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / I. INTRODUCTION - extractive body cue:** This problem can be naturally formulated using the classical Information Bottleneck (IB) [13] theory, which also provides algorithmic approaches for task-driven clustering.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In order to overcome these limitations, a new set of approaches [8, 9] has begun to leverage vision-language foundation models for open-set semantic understanding.
- **p. 3 / I. INTRODUCTION - extractive body cue:** Contrary to current approaches for open-set 3D scene graph construction (e.g., [9]) which are restricted to off-line operation when querying large vision-language models (VLMs) [15] ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (Abstract), p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (IV. TASK-DRIVEN CLUSTERING)): We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics.

- **p. 2 / Abstract - extractive body cue:** Our final contribution is an extensive experimental campaign showing that Clio not only allows real-time construction of compact open-set 3D scene graphs, but also improves ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our third contribution (Section V) is to include the proposed task-driven clustering algorithm into a real-time system, named Clio (Fig.
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our second contribution (Section IV) is to apply the Agglomerative IB algorithm from [14] to the problem of taskdriven 3D scene understanding.
- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Towards this goal, we propose an incremental version of the algorithm that can be executed online as the robot explores

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Despite the encouraging experimental results, our approach has multiple limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | First, while our method is zero-shot and is not bound to any particular foundation model, it does inherit ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Closed-Set Object Evaluation While Clio is designed for open-set detection, we include results on the closed-set Replica [17] ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 3 (I. INTRODUCTION), p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 2 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), interface p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 3 (I. INTRODUCTION), p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 2 (Abstract), objective p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 5 (IV. TASK-DRIVEN CLUSTERING).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** These approaches, however, leave to the user the difficult task of tuning suitable thresholds to control the number of segments that are extracted from the scene as well as the ... (p. 2, I. INTRODUCTION).
- **Formulation-changing contribution:** We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics. (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** Notably, Clio was only unable to select the correct target object in the scene graph once (i.e., the "Wrong Object" failure category). (p. 8, VI. EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
