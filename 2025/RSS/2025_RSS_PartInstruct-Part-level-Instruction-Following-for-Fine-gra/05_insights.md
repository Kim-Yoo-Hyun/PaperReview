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

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 for the low-level action policy based on the task instruction and the current observation.를 3D Diffuser Actor (3D-DA) [18] tains a policy that is jointly conditioned on a tokenized 3D scene, proprioceptive feedback, and a natural-language instruction, It uses diffusion to generate 3D pose trajectories.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely difficult for state-of-the-art end-to-end vision-language policy learning ‘methods. ‘There are several ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, Benchmark, part-level grounding, 3D manipulation, language instruction, long-horizon`.
- **Reading predecessor in the generated track queue:** CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely difficult for state-of-the-art end-to-end vision-language policy learning ‘methods. ‘There are several ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts..
3. Compare against the body-reported baseline or a matched simpler baseline: 3) Demonstration Generation: Each demonstration is. a sequential execution of oracle high-level plans of base skills defined in Table X, To generate the trajectories in the demonstrations, we detect grasping point using ....
4. Report the body metric and its denominator/aggregation: Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error bars denote the standard errors calculated across all ....
5. Re-run the body-reported ablation/failure condition: Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (B. Bi-level Planning), p. 8 (B. Bi-level Planning), p. 8 (B. Bi-level Planning); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 6 (C. Dataset), p. 6 (C. Dataset); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Specifically, bi-level, planner mechanism이 3) Demonstration Generation: Each demonstration is. a sequential execution of oracle high-level plans of base skills ... 대비 Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group ...을 개선하고, Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
