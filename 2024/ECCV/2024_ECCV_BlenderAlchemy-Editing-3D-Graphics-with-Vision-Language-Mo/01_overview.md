# BlenderAlchemy: Editing 3D Graphics with Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/12578_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/12578.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision, Graph Reasoning
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/12578_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/12578.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, for all of the work mentioned so far, their fundamentally image-based or latent-based representations make the output materials difficult to edit in existing 3D graphics pipelines.를 문제로 두고, We show that our method can outperform prior works designed for similar problem settings, such as BlenderGPT [1].를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** To produce the compelling graphics content we see in movies or video games, 3D artists usually need to spend hours in software like Blender to ...
- **p. 1 / 1 Introduction - extractive body cue:** These operations require the artist to create a mental picture of the target, experiment with different parameters, and visually examine whether their edits get closer ...
- **p. 1 / 1 Introduction - extractive body cue:** One can imagine automating these processes by converting language or visual descriptions of user intent into edits that achieve a design goal.
- **p. 1 / 1 Introduction - extractive body cue:** Such a system can improve the productivity of millions of 3D designers and impact various industries that depend on 3D graphic design.
- **p. 1 / 1 Introduction - extractive body cue:** Graphic design is very challenging because even a small design goal requires performing a variety of different tasks.
- **p. 4 / 1 Introduction - extractive body cue:** However, for all of the work mentioned so far, their fundamentally image-based or latent-based representations make the output materials difficult to edit in existing 3D ...
- **p. 2 / 1 Introduction - extractive body cue:** While LLMs have excellent abilities to understand user intentions and suggest sequences of actions to satisfy them, applying LLMs to graphical design remains challenging largely ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** We show that our method can outperform prior works designed for similar problem settings, such as BlenderGPT [1].
- **p. 3 / 1 Introduction - extractive body cue:** We show that our method is capable of accomplishing graphical design tasks within Blender, guided by user intention in the form of text and images.
- **p. 7 / 3 Method - extractive body cue:** Inspired by works like [51], we propose a visual state evaluator V (S1, S2, I), which is tasked with returning whichever of the two visual ...
- **p. 7 / 3 Method - extractive body cue:** BlenderAlchemy 7 To discover a good edit to p0, we introduce the procedure outlined in Algorithm 1, an iterative refinement loop that repeatedly uses a ...
- **p. 8 / 3 Method - extractive body cue:** Instead, we propose supplementing the text-to-program understanding of VLM's with the text-to-image understanding in state-of-the-art image generation models.
- **p. 5 / 3 Method - extractive body cue:** 3.1 Representation of the Blender Visual State The state of the initial Blender design environment can be decomposed into an "base" Blender state Sbase and ...
- **p. 6 / 3 Method - extractive body cue:** Then our goal is to discover some edited version of p0, called p1, such that F({p1}, Sbase) produces a visual state better aligned with some ...
- **p. 8 / 3 Method - extractive body cue:** In practice, such restrictions are softly enforced through incontext prompting of VLMs, and though their inputs encourage them to abide by these constraints, the model ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given an input Blender state and a user intention specified using either language or reference images, BlenderAlchemy edits the Blender state to satisfy that intention by iteratively refining a Blender python program ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 5 (3 Method) |
| State/latent | Given, input, Blender, state, user, intention, specified, either, language, reference, images, BlenderAlchemy | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method) |
| Output/action | This requires us to (1) decompose the input initial Blender input into a combination of programs and a "base" Blender state (Section 3.1) and (2) develop a procedure to edit each program ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (3 Method), p. 5 (3 Method), p. 7 (3 Method) |
| Objective/outcome | In practice, such restrictions are softly enforced through incontext prompting of VLMs, and though their inputs encourage them to abide by these constraints, the model can still produce more drastic "tweak" edits ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 8 (3 Method), p. 7 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** We show that our method can outperform prior works designed for similar problem settings, such as BlenderGPT [1].
- **p. 3 / 1 Introduction - extractive body cue:** We show that our method is capable of accomplishing graphical design tasks within Blender, guided by user intention in the form of text and images.
- **p. 7 / 3 Method - extractive body cue:** Inspired by works like [51], we propose a visual state evaluator V (S1, S2, I), which is tasked with returning whichever of the two visual ...
- **p. 7 / 3 Method - extractive body cue:** BlenderAlchemy 7 To discover a good edit to p0, we introduce the procedure outlined in Algorithm 1, an iterative refinement loop that repeatedly uses a ...
- **p. 8 / 3 Method - extractive body cue:** Instead, we propose supplementing the text-to-program understanding of VLM's with the text-to-image understanding in state-of-the-art image generation models.
- **p. 11 / Figure/Table caption - extractive body cue:** Table 1: CLIP scores of BlenderAlchemy vs. BlenderGPT for the text-based material editing task. We find that a version of our system that has no ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of BlenderAlchemy. Given an input Blender state and a user intention specified using either language or reference images, BlenderAlchemy edits the Blender ...
- **p. 9 / 4 Experiments - extractive body cue:** To match the number of edit generator queries we make, we run their method a maximum of 32 times, using the first successful example as ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 11 (Figure/Table caption), p. 2 (Figure/Table caption) |
| Embodiment/environment | We show qualitative examples of our system controlling geometry by programmatically 1) interpolating between preset blend shapes, 2) editing of geometry node graphs, and 3) the precise placement of objects within scenes. | hardware/simulator version and reset protocol | p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Dataset/benchmark | 4.3 Lighting Setup Editing We show that BlenderAlchemy can be used to adjust the lighting of scenes according to language instructions as well. | role, split, size and leakage | p. 12 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments), p. 14 (4 Experiments) |
| Metric | 4.1 Procedural Material Editing Procedural material editing has characteristics that make it difficult for the same reason as a lot of other visual program settings: (1) small edit distances of programs may ... | definition, denominator, direction and uncertainty | p. 8 (4 Experiments), p. 10 (Figure/Table caption), p. 11 (Figure/Table caption) |
| Baseline/ablation | We collect 592 Mechanical Turk comparisons between BlenderAlchemy and the baselines from 24 Turkers on materials created using 32 different text prompts. | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Iterative visual program editing employs a edit generator G and a state evaluator V in each iteration to explore and prune different potential ...
- **p. 9 / 4 Experiments - extractive body cue:** For instance, observe that for the "digital camouflage" example, BlenderAlchemy is able to produce the "sharper angles" that the original description requests (See Figure 3) ...
- **p. 14 / 4 Experiments - extractive body cue:** We've demonstrated BlenderAlchemy on editing materials, geometry and lighting, and hope that future works will extend this to other workflows as well.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, for all of the work mentioned so far, their fundamentally image-based or latent-based representations make the output materials difficult to edit in existing 3D graphics pipelines.를 문제로 두고, We show that our method can outperform prior works designed for similar problem settings, such as BlenderGPT [1].를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 7 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
