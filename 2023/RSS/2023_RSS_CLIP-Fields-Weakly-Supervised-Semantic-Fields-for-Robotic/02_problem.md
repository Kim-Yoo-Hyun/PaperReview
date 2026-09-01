# Problem - CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2210.05663; PDF retrieval source: https://arxiv.org/pdf/2210.05663. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): However, existing representations are coarse, often relying on a preset list of classes and capturing minimal semantics [2, 11].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We propose CLIP-Fields, an implicit scene model that can be used for a variety of tasks, such as segmentation, instance identification, semantic search over space, ...
- **p. 1 / Abstract - extractive PDF cue:** CLIP-Fields learns a mapping from spatial locations to semantic embedding vectors.
- **p. 1 / Abstract - extractive PDF cue:** Importantly, we show that this mapping can be trained with supervision coming only from webimage and web-text trained models such as CLIP, Detic, and Sentence-BERT; ...
- **p. 1 / Abstract - extractive PDF cue:** When compared to baselines like Mask-RCNN, our method outperforms on few-shot instance identification or semantic segmentation on the HM3D dataset with only a fraction of ...
- **p. 1 / Abstract - extractive PDF cue:** Finally, we show that using CLIP-Fields as a scene memory, robots can perform semantic navigation in real-world environments.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, existing representations are coarse, often relying on a preset list of classes and capturing minimal semantics [2, 11].
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Concurrently, web-scale weakly-supervised vision-language models like CLIP [22] have shown that the ability to capture powerful semantic abstractions from individual 2D images.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, existing representations are coarse, often relying on a preset list of classes and capturing minimal semantics [2, 11]. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Concurrently, web-scale weakly-supervised vision-language models like CLIP [22] have shown that the ability to capture powerful semantic abstractions from individual 2D images. | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | Concurrently, web-scale, weakly-supervised, vision-language, models, like, CLIP, have, ability, capture | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | objective-specific, heads, simple, two-layer, MLPs, ReLU, nonlinearities, dimensional | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Concurrently, web-scale, weakly-supervised, vision-language, models, like, CLIP, have, ability, capture | p. 1 (I. INTRODUCTION), p. 3 (IV. APPROACH), p. 4 (IV. APPROACH) |
| Decision / output variable | path/waypoint/velocity; body terms: solution, CLIP-Fields, builds, implicit, spatial, semantic, memory, webscale | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: While, training, contrastive, loss, objective, take, consideration, associated | p. 4 (IV. APPROACH), p. 5 (IV. APPROACH), p. 5 (IV. APPROACH), p. 4 (IV. APPROACH) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (IV. APPROACH), p. 4 (IV. APPROACH), p. 3 (IV. APPROACH) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTAL EVALUATION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Concurrently, web-scale weakly-supervised vision-language models like CLIP [22] have shown that the ability to capture powerful semantic abstractions from individual 2D images.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): As a solution, we propose CLIP-Fields, which builds an implicit spatial semantic memory using webscale pretrained models as weak supervision.

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In this work, we introduce a method for building weakly supervised semantic neural fields, called CLIP-Fields, which combines the advantages of both of these lines ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | In future work, we hope to explore models that share parameters across scenes, and can handle dynamic scenes ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Detic is absent from the first two evaluations since it is a detection model and thus cannot be ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | However, if an object was misidentified during data preparation, CLIP-Fields fails to correctly identify it as well. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | 4) CLIP-Fields's robustness to label errors: In real-world applications, CLIP-Fields relies on labels given by large | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (I. INTRODUCTION), p. 3 (IV. APPROACH), p. 4 (IV. APPROACH), p. 4 (IV. APPROACH). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 3 (IV. APPROACH), p. 4 (IV. APPROACH), p. 4 (IV. APPROACH), objective p. 4 (IV. APPROACH), p. 5 (IV. APPROACH), p. 5 (IV. APPROACH), p. 4 (IV. APPROACH).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
