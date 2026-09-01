# Problem - ConceptFusion: Open-set Multimodal 3D Mapping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2302.07241; PDF retrieval source: https://arxiv.org/pdf/2302.07241. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): In this work, we bridge the gap between the rich open-set capabilities enabled by large foundation models and the semantic reasoning abilities expected of futuristic 3D mapping systems.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Building 3D maps of the environment is central to robot navigation, planning, and interaction with objects in a scene.
- **p. 1 / Abstract - extractive body cue:** Most existing approaches that integrate semantic concepts with 3D maps largely remain confined to the closed-set setting: they can only reason about a finite set ...
- **p. 1 / Abstract - extractive body cue:** Further, these maps can only be queried using class labels, or in more recent work, using text prompts.
- **p. 1 / Abstract - extractive body cue:** We address both these issues with ConceptFusion, a scene representation that is: (i) fundamentally open-set, enabling reasoning beyond a closed set of concepts (ii) inherently ...
- **p. 1 / Abstract - extractive body cue:** ConceptFusion leverages the open-set capabilities of today's foundation models that have been pretrained on internet-scale data to reason about concepts across modalities such as natural ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we bridge the gap between the rich open-set capabilities enabled by large foundation models and the semantic reasoning abilities expected of futuristic ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This major limitation exists because most foundation models consume images (e.g., CLIP [6], ALIGN [9], AudioCLIP [8]) and produce only a single vector encoding of ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In this work, we bridge the gap between the rich open-set capabilities enabled by large foundation models and the semantic reasoning abilities ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | The open-set multimodal 3D mapping problem: Given a sequence of image (and depth) observations of an environment | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | open-set, multimodal, mapping, problem, Given, sequence, image, depth, observations, environment | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Given, input, image, uses, foundation, model, feature, extractor | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: open-set, multimodal, mapping, problem, Given, sequence, image, depth, observations, environment | p. 3 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH) |
| Decision / output variable | path/waypoint/velocity; body terms: mitigate, introduce, novel, mechanism, construct, pixel-aligned, features, combine | p. 4 (IV. THE ConceptFusion APPROACH), p. 2 (I. INTRODUCTION), p. 4 (IV. THE ConceptFusion APPROACH) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: centroid, point, returned, query, term, refrigerator, television, blue | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (IV. THE ConceptFusion APPROACH), p. 10 (VI. OUTLOOK), p. 6 (IV. THE ConceptFusion APPROACH) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** This major limitation exists because most foundation models consume images (e.g., CLIP [6], ALIGN [9], AudioCLIP [8]) and produce only a single vector encoding of ...

## What the Paper Changes

PDF contribution framing (p. 4 (IV. THE ConceptFusion APPROACH), p. 2 (I. INTRODUCTION), p. 4 (IV. THE ConceptFusion APPROACH), p. 2 (I. INTRODUCTION), p. 5 (IV. THE ConceptFusion APPROACH)): To mitigate this, we introduce a novel mechanism to construct pixel-aligned features that combine global (image-level) context encapsulated in models like CLIP, with local (region-level) information.

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our key contributions are the following: • An approach to open-set multimodal 3D mapping that constructs map representations queryable by text, image, audio, and click ...
- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** Given an input image X ∈R3×H×W , our method uses a foundation model F as a feature extractor to produce three types of embeddings, which ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Crucially, we show that this approach is conceptually simple, principled, and effective even in the zero-shot setting (requiring no additional training or finetuning of foundation ...
- **p. 5 / IV. THE ConceptFusion APPROACH - extractive body cue:** To the right, we show sample reconstructions and semantic annotations over two sub-sequences.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | The GenericLLM-Agent fails to achieve the specified task since it does not have an explicit 3D map representation, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Limitations: The key limitations of our method are threefold. | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Third, we anticipate ConceptFusion to inherit the limitations and biases of foundation models [5, 75], warranting further investigations ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | As investigated in [82, 83, 73], CLIP does not inherently capture spatial relationships or compositions. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
