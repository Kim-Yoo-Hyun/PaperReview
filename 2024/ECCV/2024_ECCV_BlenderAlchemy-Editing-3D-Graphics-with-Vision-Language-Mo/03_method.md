# Method - BlenderAlchemy: Editing 3D Graphics with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/12578_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/12578.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (3 Method), p. 8 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 6 (3 Method), p. 8 (3 Method)): BlenderAlchemy 7 To discover a good edit to p0, we introduce the procedure outlined in Algorithm 1, an iterative refinement loop that repeatedly uses a visual state evaluator V to ...

## Method Body Digest

- **p. 7 / 3 Method - extractive PDF cue:** BlenderAlchemy 7 To discover a good edit to p0, we introduce the procedure outlined in Algorithm 1, an iterative refinement loop that repeatedly uses a ...
- **p. 8 / 3 Method - extractive PDF cue:** Instead, we propose supplementing the text-to-program understanding of VLM's with the text-to-image understanding in state-of-the-art image generation models.
- **p. 5 / 3 Method - extractive PDF cue:** 3.1 Representation of the Blender Visual State The state of the initial Blender design environment can be decomposed into an "base" Blender state Sbase and ...
- **p. 7 / 3 Method - extractive PDF cue:** Inspired by works like [51], we propose a visual state evaluator V (S1, S2, I), which is tasked with returning whichever of the two visual ...
- **p. 6 / 3 Method - extractive PDF cue:** Then our goal is to discover some edited version of p0, called p1, such that F({p1}, Sbase) produces a visual state better aligned with some ...
- **p. 8 / 3 Method - extractive PDF cue:** In practice, such restrictions are softly enforced through incontext prompting of VLMs, and though their inputs encourage them to abide by these constraints, the model ...
- **p. 5 / 3 Method - extractive PDF cue:** This requires us to (1) decompose the input initial Blender input into a combination of programs and a "base" Blender state (Section 3.1) and (2) ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Given an input Blender state and a user intention specified using either language or reference images, BlenderAlchemy edits the Blender state to satisfy that intention ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** We show that our method can outperform prior works designed for similar problem settings, such as BlenderGPT [1].
- **p. 3 / 1 Introduction - extractive PDF cue:** We show that our method is capable of accomplishing graphical design tasks within Blender, guided by user intention in the form of text and images.
- **p. 7 / 3 Method - extractive PDF cue:** Inspired by works like [51], we propose a visual state evaluator V (S1, S2, I), which is tasked with returning whichever of the two visual ...

## Source Evidence Cues

- **p. 7 / 3 Method - extractive PDF cue:** BlenderAlchemy 7 To discover a good edit to p0, we introduce the procedure outlined in Algorithm 1, an iterative refinement loop that repeatedly uses a ...
- **p. 8 / 3 Method - extractive PDF cue:** Instead, we propose supplementing the text-to-program understanding of VLM's with the text-to-image understanding in state-of-the-art image generation models.
- **p. 5 / 3 Method - extractive PDF cue:** 3.1 Representation of the Blender Visual State The state of the initial Blender design environment can be decomposed into an "base" Blender state Sbase and ...
- **p. 7 / 3 Method - extractive PDF cue:** Inspired by works like [51], we propose a visual state evaluator V (S1, S2, I), which is tasked with returning whichever of the two visual ...
- **p. 6 / 3 Method - extractive PDF cue:** Then our goal is to discover some edited version of p0, called p1, such that F({p1}, Sbase) produces a visual state better aligned with some ...
- **p. 8 / 3 Method - extractive PDF cue:** In practice, such restrictions are softly enforced through incontext prompting of VLMs, and though their inputs encourage them to abide by these constraints, the model ...
- **p. 5 / 3 Method - extractive PDF cue:** This requires us to (1) decompose the input initial Blender input into a combination of programs and a "base" Blender state (Section 3.1) and (2) ...
- **Detected method headings:** 3 Method (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | BlenderAlchemy 7 To discover a good edit to p0, we introduce the procedure outlined in Algorithm 1, an iterative refinement loop that ... | p. 7 (3 Method), p. 8 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Instead, we propose supplementing the text-to-program understanding of VLM's with the text-to-image understanding in state-of-the-art image generation models. | p. 8 (3 Method), p. 5 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 3.1 Representation of the Blender Visual State The state of the initial Blender design environment can be decomposed into an "base" Blender ... | p. 5 (3 Method), p. 7 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / 3 Method - extractive PDF cue:** In practice, such restrictions are softly enforced through incontext prompting of VLMs, and though their inputs encourage them to abide by these constraints, the model ...
- **p. 7 / 3 Method - extractive PDF cue:** Inspired by works like [51], we propose a visual state evaluator V (S1, S2, I), which is tasked with returning whichever of the two visual ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 8 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, input, Blender, state, user, intention, specified, either, language, reference, images, BlenderAlchemy, edits, satisfy | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, input, Blender, state, user, intention, specified, either, language, reference | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | outperform, prior, works, designed, similar, problem, settings, BlenderGPT, capable, accomplishing | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | practice, restrictions, softly, enforced, through, incontext, prompting, VLMs, though, inputs | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** Given an input Blender state and a user intention specified using either language or reference images, BlenderAlchemy edits the Blender state to satisfy that intention ...
- **p. 5 / 3 Method - extractive PDF cue:** This requires us to (1) decompose the input initial Blender input into a combination of programs and a "base" Blender state (Section 3.1) and (2) ...
- **p. 5 / 3 Method - extractive PDF cue:** 3.1 Representation of the Blender Visual State The state of the initial Blender design environment can be decomposed into an "base" Blender state Sbase and ...
- **p. 7 / 3 Method - extractive PDF cue:** Extending Tree-of-Thoughts [57] to the visual domain, G(p, S, I, b, P) is a module tasked with generating b different variations of program p, conditioned ...
- **p. 8 / 3 Method - extractive PDF cue:** Instead, we propose supplementing the text-to-program understanding of VLM's with the text-to-image understanding in state-of-the-art image generation models.
- **p. 3 / 1 Introduction - extractive PDF cue:** 2: Iterative visual program editing employs a edit generator G and a state evaluator V in each iteration to explore and prune different potential program ...
- **p. 6 / 3 Method - extractive PDF cue:** Then our goal is to discover some edited version of p0, called p1, such that F({p1}, Sbase) produces a visual state better aligned with some ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Due to the VLM's lack of baked-in understanding of the visual consequences of various programs within Blender, a multi-hypothesis and multi-step approach ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To improve the stability of the edit discovery process, we add the visual state of the program being edited at every timestep ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 3 Method - extractive PDF cue:** In practice, such restrictions are softly enforced through incontext prompting of VLMs, and though their inputs encourage them to abide by these constraints, the model ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** BlenderAlchemy, discover, good, edit, introduce, procedure, outlined, Algorithm, iterative, refinement, loop, repeatedly, uses, visual, state, evaluator, select, among, hypotheses, generator.
- **Relevant PDF headings:** 3 Method (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We show qualitative examples of our system controlling geometry by programmatically 1) interpolating between preset blend shapes, 2) editing of geometry node ... | p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Semantic / temporal fusion | We collect 592 Mechanical Turk comparisons between BlenderAlchemy and the baselines from 24 Turkers on materials created using 32 different text prompts. | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Robot query / planning handoff | Table 1: CLIP scores of BlenderAlchemy vs. BlenderGPT for the text-based material editing task. We find that a version of our system ... | p. 11 (Figure/Table caption), p. 2 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / 4 Experiments - extractive PDF cue:** BlenderGPT reasons only about how to edit the program using the input text description, doing so in a single pass without state evaluation or multi-hypothesis ...
- **p. 11 / 4 Experiments - extractive PDF cue:** Our system is the same as for text-based material editing, but without the need for visual imagination.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Iterative visual program editing employs a edit generator G and a state evaluator V in each iteration to explore and prune different potential ...
- **p. 11 / 4 Experiments - extractive PDF cue:** We find that a version of our system that has no visual components (-Vision) still outperforms BlenderGPT.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Iterative visual program editing employs a edit generator G and a state evaluator V in each iteration to explore and prune different potential ...
- **p. 9 / 4 Experiments - extractive PDF cue:** For instance, observe that for the "digital camouflage" example, BlenderAlchemy is able to produce the "sharper angles" that the original description requests (See Figure 3) ...
- **p. 14 / 4 Experiments - extractive PDF cue:** We've demonstrated BlenderAlchemy on editing materials, geometry and lighting, and hope that future works will extend this to other workflows as well.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (3 Method), p. 8 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 6 (3 Method), p. 8 (3 Method), objective p. 8 (3 Method), p. 7 (3 Method), temporal p. 7 (3 Method), p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 8 (3 Method), p. 10 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
