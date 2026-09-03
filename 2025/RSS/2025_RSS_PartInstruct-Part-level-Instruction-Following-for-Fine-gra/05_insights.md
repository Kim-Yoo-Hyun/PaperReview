# Insights — PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p148.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p148.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 7 / B. Bi-level Planning - extractive body cue:** Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy.
- **p. 4 / A. Problem Setup - extractive body cue:** ‘To develop an embodied agent capable of executing tasks defined by g, we hypothesize that it would be beneficial to star, With a set of ...
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** Diffusion Policy (DP) [5] represents a visuomotor policy as a conditional denoising diffusion process in the action space, which allows it to effectively handle multimodal ...
- **p. 8 / B. Bi-level Planning - extractive body cue:** Specifically, given an RGB image and language input, we first utilize a VLM, eg Florence-2 [34] to ground the language onto the tanget part, then ...
- **p. 8 / B. Bi-level Planning - extractive body cue:** Given this result, we then adopt DP3-5 as the low-level action policy and pair it with diferent high-level planners to create bi-level planning baselines.
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** At each time step, the model outputs an action vector that contains the translation and rotation of the robot end effector, along with ‘one dimension ...
- **p. 7 / 1 Actions .ow-Level Action - extractive body cue:** skill instruction, the low-level action policy then generates actions for achieving that subgoal
- **Contribution anchor:** p. 7 (B. Bi-level Planning), p. 4 (A. Problem Setup), p. 6 (A. End-to-End Policy Learning), p. 8 (B. Bi-level Planning), p. 8 (B. Bi-level Planning), p. 6 (A. End-to-End Policy Learning)

### Strongest assumption and failure boundary

- **p. 1 / Abstract - extractive body cue:** Kine-grained robot manipulation, such as lifting and rotating a bottle to display the label on the cap, requires robust reasoning about object parts and their ...
- **p. 1 / Abstract - extractive body cue:** Despite recent advances in training general-purpose robot manipulation policies guided by language instructions, there is a notable lack of large-scale datasets for fine-grained ‘manipulation tasks ...
- **p. 9 / V. Discussion - extractive body cue:** Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely difficult for state-of-the-art end-to-end vision-language policy learning ‘methods. ‘There ...
- **p. 9 / V. Discussion - extractive body cue:** While they can follow simple part-based instructions such as "grasp" or "touch? instructions Tike "touch the left part" introduce fine-grained spatial reasoning that these models ...
- **p. 2 / A. Instruction Following Benchmarks for Table-Top Robot - extractive body cue:** For instance, CALVIN incorporates spatial semantics but lacks explicit partlevel semantics, treating components like a "door handle as standalone objects rather than parts of a ...
- **p. 10 / V. Discussion - extractive body cue:** However, VLM-based planners can still fail during task planning, particularly in tasks that require a long chain of, skill instructions (e.., tasks in Test 4).
- **Boundary to test:** Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely difficult for state-of-the-art end-to-end vision-language policy learning ‘methods. ‘There are several ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy. | p. 7 (B. Bi-level Planning), p. 4 (A. Problem Setup) |
| Reported outcome | Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error bars denote the standard errors calculated across all ... | p. 7 (Figure/Table caption), p. 6 (C. Dataset) |
| Failure/limitation | Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely difficult for state-of-the-art end-to-end vision-language policy learning ‘methods. ‘There are several ... | p. 9 (V. Discussion), p. 9 (V. Discussion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** 3D Diffuser Actor (3D-DA) [18] tains a policy that is jointly conditioned on a tokenized 3D scene, proprioceptive feedback, and a natural-language instruction, It uses diffusion to generate 3D pose ... (p. 6, A. End-to-End Policy Learning).
- **Paper-specific mechanism:** In this work, we introduce Partinstruct, the first large-scale benchmark for both (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error bars denote the standard errors calculated ... (p. 7, Figure/Table caption); the relevant task/metric cue is Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts. (p. 2, A. Instruction Following Benchmarks for Table-Top Robot). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The Failure Cause was calculated by dividing the number of times a skill chain failed because of a specific skill or part by the total number of skill chain failures. (p. 21, C. Skill and Object Part Impact Study).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, Benchmark, part-level grounding, 3D manipulation, language instruction, long-horizon`.
- **Reading predecessor in the generated track queue:** CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely difficult for state-of-the-art end-to-end vision-language policy learning ‘methods. ‘There are several ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 3D Diffuser Actor (3D-DA) [18] tains a policy that is jointly conditioned on a tokenized 3D scene, proprioceptive feedback, and a natural-language instruction, It uses diffusion to generate 3D pose ... (p. 6, A. End-to-End Policy Learning); preserve the objective/update rule: updates the skill instruction once every n steps, while the low-level action policy updates the action at every step. (p. 7, 1 Actions .ow-Level Action).
2. Use the paper-reported task/data/environment cue: Each episode contains an observation set with different modslities, an expert action trajectory, a natural language description of the overall task, referred to as the task instruction Iga. as well ... (p. 5, C. Dataset).
3. Compare against the reported or matched baseline: Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts. (p. 2, A. Instruction Following Benchmarks for Table-Top Robot).
4. Report the body metric with its denominator and aggregation: Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts. (p. 2, A. Instruction Following Benchmarks for Table-Top Robot).
5. Re-run the reported ablation or stress/failure condition: Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts. (p. 2, A. Instruction Following Benchmarks for Table-Top Robot); if none is reported, design one around: The Failure Cause was calculated by dividing the number of times a skill chain failed because of a specific skill or part by the total number of skill chain failures. (p. 21, C. Skill and Object Part Impact Study).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 7 (B. Bi-level Planning), match the reported outcome at p. 7 (Figure/Table caption), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), and measure the boundary at p. 21 (C. Skill and Object Part Impact Study), p. 9 (V. Discussion).

## Falsifiable research question

Under the paper's stated interface (3D Diffuser Actor (3D-DA) [18] tains a policy that is jointly conditioned on a tokenized 3D scene, proprioceptive feedback, and a natural-language ...), does the paper-specific mechanism (In this work, we introduce Partinstruct, the first large-scale benchmark for both) retain the reported evaluation outcome (Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of ...) when tested against the paper's strongest explicit boundary (The Failure Cause was calculated by dividing the number of times a skill chain failed because of a ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this work, we introduce Partinstruct, the first large-scale benchmark for both (p. 1, Abstract).
- **Paper-supported outcome:** Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error bars denote the standard errors calculated ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** The Failure Cause was calculated by dividing the number of times a skill chain failed because of a specific skill or part by the total number of skill chain failures. (p. 21, C. Skill and Object Part Impact Study).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
