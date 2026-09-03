# Method - PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p148.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p148.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (B. Bi-level Planning), p. 8 (B. Bi-level Planning), p. 8 (B. Bi-level Planning), p. 6 (A. End-to-End Policy Learning), p. 7 (1 Actions .ow-Level Action), p. 6 (A. End-to-End Policy Learning)): Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy.

## Method Body Digest

- **p. 7 / B. Bi-level Planning - extractive body cue:** Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy.
- **p. 8 / B. Bi-level Planning - extractive body cue:** Specifically, given an RGB image and language input, we first utilize a VLM, eg Florence-2 [34] to ground the language onto the tanget part, then ...
- **p. 8 / B. Bi-level Planning - extractive body cue:** Given this result, we then adopt DP3-5 as the low-level action policy and pair it with diferent high-level planners to create bi-level planning baselines.
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** At each time step, the model outputs an action vector that contains the translation and rotation of the robot end effector, along with ‘one dimension ...
- **p. 7 / 1 Actions .ow-Level Action - extractive body cue:** skill instruction, the low-level action policy then generates actions for achieving that subgoal
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** These key pose Wi then be executed using a motion planner,
- **p. 3 / C. Robot Planning with LLMs and VLMs - extractive body cue:** For instance, TaPA [44] and LLM-Planner [38] focus oon leveraging the contextual and generative capabilities. of LLMs to decompose high-level instructions into actionable sub-tasks, SayCan ...
- **p. 7 / 1 Actions .ow-Level Action - extractive body cue:** updates the skill instruction once every n steps, while the low-level action policy updates the action at every step.

## Design Rationale

- **p. 7 / B. Bi-level Planning - extractive body cue:** Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy.
- **p. 4 / A. Problem Setup - extractive body cue:** ‘To develop an embodied agent capable of executing tasks defined by g, we hypothesize that it would be beneficial to star, With a set of ...
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** Diffusion Policy (DP) [5] represents a visuomotor policy as a conditional denoising diffusion process in the action space, which allows it to effectively handle multimodal ...

## Source Evidence Cues

- **p. 7 / B. Bi-level Planning - extractive body cue:** Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy.
- **p. 8 / B. Bi-level Planning - extractive body cue:** Specifically, given an RGB image and language input, we first utilize a VLM, eg Florence-2 [34] to ground the language onto the tanget part, then ...
- **p. 8 / B. Bi-level Planning - extractive body cue:** Given this result, we then adopt DP3-5 as the low-level action policy and pair it with diferent high-level planners to create bi-level planning baselines.
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** At each time step, the model outputs an action vector that contains the translation and rotation of the robot end effector, along with ‘one dimension ...
- **p. 7 / 1 Actions .ow-Level Action - extractive body cue:** skill instruction, the low-level action policy then generates actions for achieving that subgoal
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** These key pose Wi then be executed using a motion planner,
- **p. 3 / C. Robot Planning with LLMs and VLMs - extractive body cue:** For instance, TaPA [44] and LLM-Planner [38] focus oon leveraging the contextual and generative capabilities. of LLMs to decompose high-level instructions into actionable sub-tasks, SayCan ...
- **Detected method headings:** A. End-to-End Policy Learning (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy. | p. 7 (B. Bi-level Planning), p. 8 (B. Bi-level Planning) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Specifically, given an RGB image and language input, we first utilize a VLM, eg Florence-2 [34] to ground the language onto the ... | p. 8 (B. Bi-level Planning), p. 8 (B. Bi-level Planning) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | Given this result, we then adopt DP3-5 as the low-level action policy and pair it with diferent high-level planners to create bi-level ... | p. 8 (B. Bi-level Planning), p. 6 (A. End-to-End Policy Learning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 1 Actions .ow-Level Action - extractive body cue:** updates the skill instruction once every n steps, while the low-level action policy updates the action at every step.
- **p. 7 / B. Bi-level Planning - extractive body cue:** See Appendix DB for the detailed prompt. sg, will be passed to the lowlevel action policy for execution and will be updated every rn step.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 7 (1 Actions .ow-Level Action), p. 7 (B. Bi-level Planning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | low-level, action, policy, task, instruction, current, observation, Diffuser, Actor, D-DA, tains, jointly, conditioned, tokenized | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | low-level, action, policy, task, instruction, current, observation, Diffuser, Actor, D-DA | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | Specifically, bi-level, planner, consists, modules, high-level, task, low-level, action, policy | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | updates, skill, instruction, once, every, steps, while, low-level, action, policy | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / 1 Actions .ow-Level Action - extractive body cue:** for the low-level action policy based on the task instruction and the current observation.
- **p. 6 / A. End-to-End Policy Learning - extractive body cue:** 3D Diffuser Actor (3D-DA) [18] tains a policy that is jointly conditioned on a tokenized 3D scene, proprioceptive feedback, and a natural-language instruction, It uses ...
- **p. 7 / 1 Actions .ow-Level Action - extractive body cue:** skill instruction, the low-level action policy then generates actions for achieving that subgoal
- **p. 8 / B. Bi-level Planning - extractive body cue:** However, in our tasks, the robot needs to interact with at most one part for the subgoal sg defined in each skill instruction, making it ...
- **p. 8 / B. Bi-level Planning - extractive body cue:** We can train the end-to-end policy learning models evaluated in Section IV-A on skill instructions to create low-level action policies,
- **p. 4 / A. Problem Setup - extractive body cue:** parameterized by (1) the object part it interacts with and the type of interaction (e.g, touching or grasping), (2) the degree of rotation required for ...
- **p. 3 / C. Robot Planning with LLMs and VLMs - extractive body cue:** For instance, TaPA [44] and LLM-Planner [38] focus oon leveraging the contextual and generative capabilities. of LLMs to decompose high-level instructions into actionable sub-tasks, SayCan ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | At each time step, the model outputs an action vector that contains the translation and rotation of the robot end effector, along ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Additionally, frameworks like DP (5] and DP3 [49] formulate visuomotor robot policies using Denoising Diffusion Probabilistic Models (DDPM), enabling these policies to ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 1 Actions .ow-Level Action - extractive body cue:** Specifically, We use a pre-trained TS language encoder to get the language ‘embedding [31].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, bi-level, planner, consists, modules, high-level, task, low-level, action, policy, given, RGB, image, language, input, first, utilize, VLM, Florence-2, ground.
- **Relevant PDF headings:** A. End-to-End Policy Learning (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts. | p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), p. 5 (C. Dataset) |
| Baseline harness | 3) Demonstration Generation: Each demonstration is. a sequential execution of oracle high-level plans of base skills defined in Table X, To generate ... | p. 6 (C. Dataset), p. 7 (Figure/Table caption) |
| Metric / failure reporting | Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning ... | p. 7 (Figure/Table caption), p. 6 (C. Dataset) |

## Failure and Ablation Link

- **p. 2 / A. Instruction Following Benchmarks for Table-Top Robot - extractive body cue:** Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts.
- **p. 6 / C. Dataset - extractive body cue:** This yields between 3 -8 natural-language variants per template, greatly increasing the language diversity Of the dataset.
- **p. 2 / A. Instruction Following Benchmarks for Table-Top Robot - extractive body cue:** For instance, CALVIN incorporates spatial semantics but lacks explicit partlevel semantics, treating components like a "door handle as standalone objects rather than parts of a ...
- **p. 9 / V. Discussion - extractive body cue:** Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely difficult for state-of-the-art end-to-end vision-language policy learning ‘methods. ‘There ...
- **p. 9 / V. Discussion - extractive body cue:** While they can follow simple part-based instructions such as "grasp" or "touch? instructions Tike "touch the left part" introduce fine-grained spatial reasoning that these models ...
- **p. 2 / A. Instruction Following Benchmarks for Table-Top Robot - extractive body cue:** For instance, CALVIN incorporates spatial semantics but lacks explicit partlevel semantics, treating components like a "door handle as standalone objects rather than parts of a ...
- **p. 10 / V. Discussion - extractive body cue:** However, VLM-based planners can still fail during task planning, particularly in tasks that require a long chain of, skill instructions (e.., tasks in Test 4).

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (B. Bi-level Planning), p. 8 (B. Bi-level Planning), p. 8 (B. Bi-level Planning), p. 6 (A. End-to-End Policy Learning), p. 7 (1 Actions .ow-Level Action), p. 6 (A. End-to-End Policy Learning), objective p. 7 (1 Actions .ow-Level Action), p. 7 (B. Bi-level Planning), temporal p. 6 (A. End-to-End Policy Learning), p. 3 (B. Vision-Language Policies for Robot Manipulation), p. 4 (A. Problem Setup), p. 5 (C. Dataset), p. 6 (C. Dataset), p. 8 (B. Bi-level Planning).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy. (p. 7, B. Bi-level Planning).
- **Objective/update evidence:** updates the skill instruction once every n steps, while the low-level action policy updates the action at every step. (p. 7, 1 Actions .ow-Level Action).
- **Temporal/runtime evidence:** Additionally, frameworks like DP (5] and DP3 [49] formulate visuomotor robot policies using Denoising Diffusion Probabilistic Models (DDPM), enabling these policies to capture multimodal action distributions and generate high-dimensiona ... (p. 3, B. Vision-Language Policies for Robot Manipulation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
