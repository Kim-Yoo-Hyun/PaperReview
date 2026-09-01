# Problem - BlenderAlchemy: Editing 3D Graphics with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/12578_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/12578.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction)): However, for all of the work mentioned so far, their fundamentally image-based or latent-based representations make the output materials difficult to edit in existing 3D graphics pipelines.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** To produce the compelling graphics content we see in movies or video games, 3D artists usually need to spend hours in software like Blender to ...
- **p. 1 / 1 Introduction - extractive PDF cue:** These operations require the artist to create a mental picture of the target, experiment with different parameters, and visually examine whether their edits get closer ...
- **p. 1 / 1 Introduction - extractive PDF cue:** One can imagine automating these processes by converting language or visual descriptions of user intent into edits that achieve a design goal.
- **p. 1 / 1 Introduction - extractive PDF cue:** Such a system can improve the productivity of millions of 3D designers and impact various industries that depend on 3D graphic design.
- **p. 1 / 1 Introduction - extractive PDF cue:** Graphic design is very challenging because even a small design goal requires performing a variety of different tasks.
- **p. 4 / 1 Introduction - extractive PDF cue:** However, for all of the work mentioned so far, their fundamentally image-based or latent-based representations make the output materials difficult to edit in existing 3D ...
- **p. 2 / 1 Introduction - extractive PDF cue:** While LLMs have excellent abilities to understand user intentions and suggest sequences of actions to satisfy them, applying LLMs to graphical design remains challenging largely ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, for all of the work mentioned so far, their fundamentally image-based or latent-based representations make the output materials difficult to edit ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Given an input Blender state and a user intention specified using either language or reference images, BlenderAlchemy edits the Blender state to ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Given, input, Blender, state, user, intention, specified, either, language, reference | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Representation, Blender, Visual, State, initial, design, environment, decomposed | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Given, input, Blender, state, user, intention, specified, either, language, reference | p. 2 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method) |
| Decision / output variable | geometry/map/query r; body terms: outperform, prior, works, designed, similar, problem, settings, BlenderGPT | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 7 (3 Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: practice, restrictions, softly, enforced, through, incontext, prompting, VLMs | p. 8 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 8 (3 Method), p. 7 (3 Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (4 Experiments), p. 10 (Figure/Table caption), p. 11 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** While LLMs have excellent abilities to understand user intentions and suggest sequences of actions to satisfy them, applying LLMs to graphical design remains challenging largely ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Naively applying VLMs to this editing setting gives rise to many failure cases, possibly due to the fact that out-of-the-box VLMs have a poor understanding ...
- **p. 4 / 1 Introduction - extractive PDF cue:** Their application to visual problem settings, however, has mostly been limited due to the nonexistent visual perception capabilities of the LLMs [11, 15, 48, 50, ...
- **p. 3 / 1 Introduction - extractive PDF cue:** We show that our method can outperform prior works designed for similar problem settings, such as BlenderGPT [1].

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method)): We show that our method can outperform prior works designed for similar problem settings, such as BlenderGPT [1].

- **p. 3 / 1 Introduction - extractive PDF cue:** We show that our method is capable of accomplishing graphical design tasks within Blender, guided by user intention in the form of text and images.
- **p. 7 / 3 Method - extractive PDF cue:** Inspired by works like [51], we propose a visual state evaluator V (S1, S2, I), which is tasked with returning whichever of the two visual ...
- **p. 7 / 3 Method - extractive PDF cue:** BlenderAlchemy 7 To discover a good edit to p0, we introduce the procedure outlined in Algorithm 1, an iterative refinement loop that repeatedly uses a ...
- **p. 8 / 3 Method - extractive PDF cue:** Instead, we propose supplementing the text-to-program understanding of VLM's with the text-to-image understanding in state-of-the-art image generation models.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Fig. 2: Iterative visual program editing employs a edit generator G and a state evaluator V in each ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | For instance, observe that for the "digital camouflage" example, BlenderAlchemy is able to produce the "sharper angles" that ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | We've demonstrated BlenderAlchemy on editing materials, geometry and lighting, and hope that future works will extend this to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method), p. 7 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), interface p. 2 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method), p. 7 (3 Method), objective p. 8 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
