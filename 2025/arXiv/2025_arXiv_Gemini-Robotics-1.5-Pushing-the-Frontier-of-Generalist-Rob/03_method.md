# Method - Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (62 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2510.03342; PDF retrieval source: https://arxiv.org/pdf/2510.03342. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (2.1. Model & Architecture), p. 3 (2.1. Model & Architecture), p. 10 (4. Gemini Robotics-ER 1.5 is a generalist embodied reasoning model), p. 13 (4.2. Frontier capabilities for Embodied Reasoning), p. 4 (2.1. Model & Architecture), p. 12 (4.1. Generality)): We use GR-ER 1.5 as the orchestrator. • Action model: The action model translates instructions issued by the orchestrator into lowlevel robot actions.

## Method Body Digest

- **p. 3 / 2.1. Model & Architecture - extractive body cue:** We use GR-ER 1.5 as the orchestrator. • Action model: The action model translates instructions issued by the orchestrator into lowlevel robot actions.
- **p. 3 / 2.1. Model & Architecture - extractive body cue:** The full agentic system consists of an orchestrator and an action model that are implemented by the VLM and the VLA, respectively: • Orchestrator: The ...
- **p. 10 / 4. Gemini Robotics-ER 1.5 is a generalist embodied reasoning model - extractive body cue:** We introduce Gemini Robotics-ER 1.5 (GR-ER 1.5), our most advanced multimodal thinking model for state-of-the-art embodied reasoning based on Gemini.
- **p. 13 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** By extending this ability to predict a set of points, a model can generate more complex outputs like motion trajectories and paths, providing precise action ...
- **p. 4 / 2.1. Model & Architecture - extractive body cue:** In Gemini Robotics 1.5, we also introduce a new model architecture and training recipe for the VLA.
- **p. 12 / 4.1. Generality - extractive body cue:** Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer Progress Understanding Segmentation Masks Pointing Trajectory Prediction Object ...
- **p. 15 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** We find that models often require long inference time making real-time usage challenging, since stale success predictions quickly become irrelevant during dynamic robot interactions.
- **p. 3 / 2.1. Model & Architecture - extractive body cue:** It has additionally been optimized for complex embodied reasoning problems such as task planning, reasoning for spatial expertise, and task progress estimation.

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** This multi-embodiment pre-training allows GR 1.5 to control multiple robots, including the ALOHA, Bi-arm Franka, and Apollo humanoid robots, without any robot-specific post-training, and it ...
- **p. 2 / 1. Introduction - extractive body cue:** ER thinking traces Gemini Robotics 1.5 Gemini Robotics-ER 1.5 Actions Text Figure 1 / The Gemini Robotics 1.5 family of models consists of Gemini Robotics ...
- **p. 3 / 2.1. Model & Architecture - extractive body cue:** The full agentic system consists of an orchestrator and an action model that are implemented by the VLM and the VLA, respectively: • Orchestrator: The ...

## Source Evidence Cues

- **p. 3 / 2.1. Model & Architecture - extractive body cue:** We use GR-ER 1.5 as the orchestrator. • Action model: The action model translates instructions issued by the orchestrator into lowlevel robot actions.
- **p. 3 / 2.1. Model & Architecture - extractive body cue:** The full agentic system consists of an orchestrator and an action model that are implemented by the VLM and the VLA, respectively: • Orchestrator: The ...
- **p. 10 / 4. Gemini Robotics-ER 1.5 is a generalist embodied reasoning model - extractive body cue:** We introduce Gemini Robotics-ER 1.5 (GR-ER 1.5), our most advanced multimodal thinking model for state-of-the-art embodied reasoning based on Gemini.
- **p. 13 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** By extending this ability to predict a set of points, a model can generate more complex outputs like motion trajectories and paths, providing precise action ...
- **p. 4 / 2.1. Model & Architecture - extractive body cue:** In Gemini Robotics 1.5, we also introduce a new model architecture and training recipe for the VLA.
- **p. 12 / 4.1. Generality - extractive body cue:** Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer Progress Understanding Segmentation Masks Pointing Trajectory Prediction Object ...
- **p. 15 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** We find that models often require long inference time making real-time usage challenging, since stale success predictions quickly become irrelevant during dynamic robot interactions.
- **Detected method headings:** 2. Method Overview (p. 3); 2.1. Model & Architecture (p. 3); 4. Gemini Robotics-ER 1.5 is a generalist embodied reasoning model (p. 10)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | We use GR-ER 1.5 as the orchestrator. • Action model: The action model translates instructions issued by the orchestrator into lowlevel robot ... | p. 3 (2.1. Model & Architecture), p. 3 (2.1. Model & Architecture) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | The full agentic system consists of an orchestrator and an action model that are implemented by the VLM and the VLA, respectively: ... | p. 3 (2.1. Model & Architecture), p. 10 (4. Gemini Robotics-ER 1.5 is a generalist embodied reasoning model) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | We introduce Gemini Robotics-ER 1.5 (GR-ER 1.5), our most advanced multimodal thinking model for state-of-the-art embodied reasoning based on Gemini. | p. 10 (4. Gemini Robotics-ER 1.5 is a generalist embodied reasoning model), p. 13 (4.2. Frontier capabilities for Embodied Reasoning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2.1. Model & Architecture - extractive body cue:** It has additionally been optimized for complex embodied reasoning problems such as task planning, reasoning for spatial expertise, and task progress estimation.
- **p. 10 / 3.3. Thinking Helps Acting - extractive body cue:** 7, the robot automatically switches its objective from "pick up the yellow tennis ball" to "put the yellow tennis ball in the white bag" once ...
- **p. 13 / 4.1. Generality - extractive body cue:** The model can follow complex pointing prompts that require reasoning about physical, spatial, and semantic constraints: It can localize precise parts of objects, such as ...
- **p. 14 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** It particularly excels at complex pointing tasks that require reasoning about physical, spatial, and semantic constraints including safety.
- **p. 5 / 3. Gemini Robotics 1.5 is a general multi-embodiment Vision-Language-Action - extractive body cue:** We generally report mean and standard error of the mean of progress score (definitions in Appendix B.2 - Appendix B.4), as it provides a continuous ...
- **p. 9 / 3.3. Thinking Helps Acting - extractive body cue:** 6 demonstrates that enabling the thinking mode yields a sizable improvement in the progress score for these tasks.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 10 (3.3. Thinking Helps Acting), p. 13 (4.1. Generality), p. 14 (4.2. Frontier capabilities for Embodied Reasoning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | allows, model, convert, visual, observations, language-based, thoughts, simplify, complex, instructions, detect, task, success, failure | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | allows, model, convert, visual, observations, language-based, thoughts, simplify, complex, instructions | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | multi-embodiment, pre-training, allows, control, multiple, robots, including, ALOHA, Bi-arm, Franka | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | additionally, been, optimized, complex, embodied, reasoning, problems, task, planning, spatial | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** This allows the model to convert visual observations into language-based thoughts, simplify complex instructions, detect task success or failure, propose recovery behaviors, and make the ...
- **p. 2 / 1. Introduction - extractive body cue:** execution code_blocks Search search Function calling data_object Proprioception precision_manufacturing Images image Text instruction short_text Inputs Speech mic Images photo_library Text chat ALOHA 2 Bi-arm Franka ...
- **p. 3 / 2.1. Model & Architecture - extractive body cue:** The full agentic system consists of an orchestrator and an action model that are implemented by the VLM and the VLA, respectively: • Orchestrator: The ...
- **p. 3 / 2.1. Model & Architecture - extractive body cue:** The action model then decomposes each such instruction into shorter segments that correspond to a few seconds of robot movement each (e.g., "pick up the ...
- **p. 9 / 3.3. Thinking Helps Acting - extractive body cue:** This performance gain stems from the model's ability to decompose the difficult cross-modal translation, which involves mapping high-level, multi-step language instructions to lowlevel robot actions, ...
- **p. 5 / 3. Gemini Robotics 1.5 is a general multi-embodiment Vision-Language-Action - extractive body cue:** Gemini Robotics 1.5 can generalize to new environments and tasks To understand GR 1.5's generalization performance on short-horizon tasks, we use the same methodology as ...
- **p. 15 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** For the offline evaluations, we leverage various types of videos of real-world interaction, which cover a mix of embodiments, camera viewpoints, and input formats.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | First, the model generates a language-based thinking trace by converting the complex task into a sequence of specific, short-horizon steps (e.g., transforming ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | For the real-time evaluations, we sample recorded real-world robot rollouts from Section 5, and run the model at 5Hz and simulate inference ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | For the real-time evaluations, we sample recorded real-world robot rollouts from Section 5, and run the model at 5Hz and simulate inference ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 2.1. Model & Architecture - extractive body cue:** In Gemini Robotics 1.5, we also introduce a new model architecture and training recipe for the VLA.
- **p. 15 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** We find that models often require long inference time making real-time usage challenging, since stale success predictions quickly become irrelevant during dynamic robot interactions.
- **p. 11 / 4. Gemini Robotics-ER 1.5 is a generalist embodied reasoning model - extractive body cue:** Able to scale embodied reasoning performance via inference time compute.
- **p. 14 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** Real-time SD considers model inference latency when computing prediction accuracy, while offline success detection assumes unlimited inference time for each prediction.
- **p. 15 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** In the offline setting, we allow models unlimited inference time for success detection.
- **p. 15 / 4.2. Frontier capabilities for Embodied Reasoning - extractive body cue:** We find that models often require long inference time making real-time usage challenging, since stale success predictions quickly become irrelevant during dynamic robot interactions.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** GR-ER, orchestrator, Action, model, translates, instructions, issued, lowlevel, robot, actions, full, agentic, system, consists, implemented, VLM, VLA, respectively, processes, user.
- **Relevant PDF headings:** 2. Method Overview (p. 3); 2.1. Model & Architecture (p. 3); 4. Gemini Robotics-ER 1.5 is a generalist embodied reasoning model (p. 10).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | Over 90% of the evaluation episodes during the development of Gemini Robotics 1.5 were conducted in simulation. | p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation) |
| Balance-aware whole-body execution | For all comparisons reported in this report, we perform A/B/n testing on real robots. | p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation) |
| Recovery / adaptation | To improve research iteration speed, we have developed methods for evaluation without real robots in the loop. | p. 4 (2.3. Evaluation), p. 4 (2.3. Evaluation) |

## Failure and Ablation Link

- **p. 4 / 2.3. Evaluation - extractive body cue:** To improve research iteration speed, we have developed methods for evaluation without real robots in the loop.
- **p. 22 / 7. Discussion - extractive body cue:** Its performance on tasks like visual and spatial thinking, task planning, progress estimation, and success detection is critical for robust, real-world robotic applications.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (2.1. Model & Architecture), p. 3 (2.1. Model & Architecture), p. 10 (4. Gemini Robotics-ER 1.5 is a generalist embodied reasoning model), p. 13 (4.2. Frontier capabilities for Embodied Reasoning), p. 4 (2.1. Model & Architecture), p. 12 (4.1. Generality), objective p. 3 (2.1. Model & Architecture), p. 10 (3.3. Thinking Helps Acting), p. 13 (4.1. Generality), p. 14 (4.2. Frontier capabilities for Embodied Reasoning), p. 5 (3. Gemini Robotics 1.5 is a general multi-embodiment Vision-Language-Action), p. 9 (3.3. Thinking Helps Acting), temporal p. 9 (3.3. Thinking Helps Acting), p. 15 (4.2. Frontier capabilities for Embodied Reasoning), p. 2 (1. Introduction), p. 3 (2.1. Model & Architecture), p. 3 (2.1. Model & Architecture), p. 4 (2.3. Evaluation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (62 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The full agentic system consists of an orchestrator and an action model that are implemented by the VLM and the VLA, respectively: • Orchestrator: The orchestrator processes user input and ... (p. 3, 2.1. Model & Architecture).
- **Objective/update evidence:** It has additionally been optimized for complex embodied reasoning problems such as task planning, reasoning for spatial expertise, and task progress estimation. (p. 3, 2.1. Model & Architecture).
- **Temporal/runtime evidence:** First, the model generates a language-based thinking trace by converting the complex task into a sequence of specific, short-horizon steps (e.g., transforming the goal of "sorting clothes" into a thought ... (p. 9, 3.3. Thinking Helps Acting).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
