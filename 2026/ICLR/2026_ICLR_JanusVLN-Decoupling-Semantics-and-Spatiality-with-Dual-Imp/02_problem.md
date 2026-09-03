# Problem - JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=RnuB0Nlbd5; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/248109. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): Inspired by human cognitive science, this framework simultaneously captures visual semantics and spatial geometry to overcome the inherent limitations of existing navigation LLM. • We unlock the potential of spatial ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Vision-and-Language Navigation (VLN) requires an embodied agent to navigate through unseen environments, guided by natural language instructions and a continuous video stream.
- **p. 1 / ABSTRACT - extractive body cue:** Recent advances in VLN have been driven by the powerful semantic understanding of Multimodal Large Language Models (MLLMs).
- **p. 1 / ABSTRACT - extractive body cue:** However, these methods typically rely on explicit semantic memory, such as building textual cognitive maps or storing historical visual frames.
- **p. 1 / ABSTRACT - extractive body cue:** This type of method suffers from spatial information loss, computational redundancy, and memory bloat, which impede efficient navigation.
- **p. 1 / ABSTRACT - extractive body cue:** Inspired by the implicit scene representation in human navigation, analogous to the left brain's semantic understanding and the right brain's spatial cognition, we propose JanusVLN, ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Inspired by human cognitive science, this framework simultaneously captures visual semantics and spatial geometry to overcome the inherent limitations of existing navigation LLM. • We ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This makes it exceedingly difficult for the model to extract critical information from a vast, cluttered, and fragmented memory, thereby leading to severe inefficiency.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Inspired by human cognitive science, this framework simultaneously captures visual semantics and spatial geometry to overcome the inherent limitations of existing navigation ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Vision-and-Language Navigation (VLN) is a foundational task in embodied AI, requiring an agent to navigate through unseen environments guided by visual inputs ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Vision-and-Language, Navigation, VLN, foundational, task, embodied, requiring, agent, navigate, through | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | process, iterates, until, agent, executes, Stop, action, target | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Vision-and-Language, Navigation, VLN, foundational, task, embodied, requiring, agent, navigate, through | p. 1 (1 INTRODUCTION), p. 4 (3 METHOD), p. 4 (3 METHOD) |
| Decision / output variable | path/waypoint/velocity; body terms: summary, contributions, follows, introduce, novel, dual, implicit, memory | p. 3 (1 INTRODUCTION), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: DUAL, IMPLICIT, MEMORY, limitations, traditional, explicit, semantic, including | p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** This makes it exceedingly difficult for the model to extract critical information from a vast, cluttered, and fragmented memory, thereby leading to severe inefficiency.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Navigation is an inherently 3D physical interaction, yet the visual encoders of existing VLA models almost exclusively inherit the CLIP paradigm pre-trained on 2D image-text ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Unlike the visual encoders of general MLLMs, which are predominantly trained on 2D image-text data, this spatial geometry model is typically trained on pixel-3D point ...

## What the Paper Changes

PDF body contribution framing (p. 3 (1 INTRODUCTION), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD)): In summary, our contributions are as follows: • We introduce a novel dual implicit memory paradigm for VLN.

- **p. 4 / 3 METHOD - extractive body cue:** To address these challenges, we introduce the VGGT as a spatial geometry encoder and propose a novel dual implicit memory paradigm for VLN research in ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we introduce JanusVLN, a dual implicit memory framework for VLN that features both spatialgeometric and visual-semantic memory in Figure 1.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by the human brain's hemispheric specialization for navigation, where the left hemisphere handles semantic understanding and the right manages 3D spatial cognition to form ...
- **p. 6 / 3 METHOD - extractive body cue:** Building upon the dual implicit memory paradigm, we propose JanusVLN in Figure 2, enhances the spatial understanding capabilities without requiring costly 3D data (e.g., depth).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 21 | Figure 9: Visualization and presentation of the types of failure cases. on relatively simple instructions (1-150 words). However, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 20 | Figure 8: Performance on various instruction lengths/complexity. larger-scale external datasets, akin to the approaches of StreamVLN and NaVILA, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Finally, when we omit the preservation of the initial window's KV, a slight performance degradation is observed, indicating ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1 INTRODUCTION), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 1 (1 INTRODUCTION), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), objective p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
