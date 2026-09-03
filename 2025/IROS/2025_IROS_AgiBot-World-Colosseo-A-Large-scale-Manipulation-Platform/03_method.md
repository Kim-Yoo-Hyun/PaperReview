# Method - AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://opendrivelab.com/AgiBot-World/; PDF retrieval source: https://arxiv.org/pdf/2503.06669. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (2) Implementation Details), p. 7 (2) Implementation Details), p. 8 (2) Implementation Details), p. 8 (2) Implementation Details)): The inclusion of the latent planner yields an average improvement of 0.12 task completion score.

## Method Body Digest

- **p. 7 / 2) Implementation Details - extractive body cue:** The inclusion of the latent planner yields an average improvement of 0.12 task completion score.
- **p. 7 / 2) Implementation Details - extractive body cue:** We choose the open-source RDT [10] model to study how much the AgiBot World dataset can help policy learning.
- **p. 8 / 2) Implementation Details - extractive body cue:** How does data quality impact policy learning?
- **p. 8 / 2) Implementation Details - extractive body cue:** Specifically, we provide an ablation study by fine-tuning an RDT model using both verified (528 trajectories) and unverified (482 trajectories) data from the "Wipe Table" ...
- **p. 7 / 2) Implementation Details - extractive body cue:** For GO1, fine-tuning is conducted with a learning rate of 2e-5, a batch size of 768, and 30,000 optimization steps.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) We propose GO-1, a robot foundation policy using latent action representations to unlock web-scale pre-training on web data.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet for the open-set real-world setting, tasks spanning from fine-grained object interaction, mobile manipulation to collaborative tasks, remains a formidable challenge [5].

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) We propose GO-1, a robot foundation policy using latent action representations to unlock web-scale pre-training on web data.

## Source Evidence Cues

- **p. 7 / 2) Implementation Details - extractive body cue:** The inclusion of the latent planner yields an average improvement of 0.12 task completion score.
- **p. 7 / 2) Implementation Details - extractive body cue:** We choose the open-source RDT [10] model to study how much the AgiBot World dataset can help policy learning.
- **p. 8 / 2) Implementation Details - extractive body cue:** How does data quality impact policy learning?
- **p. 8 / 2) Implementation Details - extractive body cue:** Specifically, we provide an ablation study by fine-tuning an RDT model using both verified (528 trajectories) and unverified (482 trajectories) data from the "Wipe Table" ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | The inclusion of the latent planner yields an average improvement of 0.12 task completion score. | p. 7 (2) Implementation Details), p. 7 (2) Implementation Details) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | We choose the open-source RDT [10] model to study how much the AgiBot World dataset can help policy learning. | p. 7 (2) Implementation Details), p. 8 (2) Implementation Details) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | How does data quality impact policy learning? | p. 8 (2) Implementation Details), p. 8 (2) Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 2) Implementation Details - extractive body cue:** For GO1, fine-tuning is conducted with a learning rate of 2e-5, a batch size of 768, and 30,000 optimization steps.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Following, dataset, address, limitations, previous, robot, foundation, models, heavily, rely, indomain, datasets, present, Genie | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Following, dataset, address, limitations, previous, robot, foundation, models, heavily, rely | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | Following, dataset, address, limitations, previous, robot, foundation, models, heavily, rely | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | GO1, fine-tuning, conducted, learning, rate, batch, size, optimization, steps | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive body cue:** Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) We propose GO-1, a robot foundation policy using latent action representations to unlock web-scale pre-training on web data.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet for the open-set real-world setting, tasks spanning from fine-grained object interaction, mobile manipulation to collaborative tasks, remains a formidable challenge [5].
- **p. 7 / 2) Implementation Details - extractive body cue:** Is GO-1 a more capable generalist policy?
- **p. 7 / 2) Implementation Details - extractive body cue:** Does AgiBot World boost policy learning at scale?
- **p. 8 / 2) Implementation Details - extractive body cue:** How does data quality impact policy learning?
- **p. 1 / I. INTRODUCTION - extractive body cue:** While significant progress has been made in general-purpose foundational models for natural language processing [1] and computer vision [2], robotics lags behind due to the ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | The action expert decodes low-level action chunks, denoted by At = [at,at+1,...,at+H] with H = 30, using proprioceptive state pt over an ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | Each episode is meticulously designed, featuring multiple camera views, depth information, camera calibration, and language annotations for both the overall task and ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | The evaluation metric employs a normalized score, computed as the average across 10 rollouts per task, scenario, and method. | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 2) Implementation Details - extractive body cue:** Specifically, we provide an ablation study by fine-tuning an RDT model using both verified (528 trajectories) and unverified (482 trajectories) data from the "Wipe Table" ...
- **p. 7 / 2) Implementation Details - extractive body cue:** For GO1, fine-tuning is conducted with a learning rate of 2e-5, a batch size of 768, and 30,000 optimization steps.
- **p. 6 / 1) Evaluation Tasks - extractive body cue:** The evaluation metric employs a normalized score, computed as the average across 10 rollouts per task, scenario, and method.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** inclusion, latent, planner, yields, average, improvement, task, completion, score, choose, open-source, RDT, model, study, much, AgiBot, World, dataset, help, policy.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | Based on the hardware platform developed by us, AgiBot G1, we construct AgiBot Worldan open-source robot manipulation dataset collected by more than ... | p. 3 (Dataset), p. 5 (Dataset) |
| Balance-aware whole-body execution | Across all tasks and comparisons, GO-1 outperforms baselines by a large margin. | p. 7 (1) Evaluation Tasks), p. 7 (1) Evaluation Tasks) |
| Recovery / adaptation | Fig. 7: Further analysis on: a) how model performance scales with data size, and b) the impact of filtering undesir- able data ... | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / V. EXPERIMENT AND ANALYSIS - extractive body cue:** We evaluate the real-world performance of policies pretrained on different data sources including the AgiBot World dataset, demonstrating the effectiveness credited from the GO-1 model ...
- **p. 7 / 1) Evaluation Tasks - extractive body cue:** We evaluate GO-1 against previous generalist policy RDT-1B and our baseline without the latent planner, with all policies pre-trained on AgiBot World beta.
- **p. 8 / 2) Implementation Details - extractive body cue:** Specifically, we provide an ablation study by fine-tuning an RDT model using both verified (528 trajectories) and unverified (482 trajectories) data from the "Wipe Table" ...
- **p. 4 / Dataset - extractive body cue:** However, they are often able to recover from these errors and successfully complete the task without requiring a full reconfiguration of the setup.
- **p. 3 / Dataset - extractive body cue:** For instance, RDT [10] employs Diffusion Transformers, initially pre-trained on heterogeneous multirobot datasets and fine-tuned on over 6k dual-arm trajectories, showcasing the benefits of pre-training ...
- **p. 7 / 2) Implementation Details - extractive body cue:** For GO1, fine-tuning is conducted with a learning rate of 2e-5, a batch size of 768, and 30,000 optimization steps.
- **p. 3 / Dataset - extractive body cue:** Notably, to expand data applicability and potential, we include imperfect data (i.e., failure recovery data with annotated error states) and tasks with dexterous hands.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (2) Implementation Details), p. 7 (2) Implementation Details), p. 8 (2) Implementation Details), p. 8 (2) Implementation Details), objective p. 7 (2) Implementation Details), temporal p. 6 (Dataset), p. 2 (I. INTRODUCTION), p. 6 (1) Evaluation Tasks), p. 7 (2) Implementation Details), p. 7 (2) Implementation Details), p. 4 (Dataset).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** 2) We propose GO-1, a robot foundation policy using latent action representations to unlock web-scale pre-training on web data. (p. 2, I. INTRODUCTION).
- **Objective/update evidence:** For GO1, fine-tuning is conducted with a learning rate of 2e-5, a batch size of 768, and 30,000 optimization steps. (p. 7, 2) Implementation Details).
- **Temporal/runtime evidence:** We evaluate GO-1 on five tasks of varying complexity, categorized by their visual richness and task horizon. (p. 7, 2) Implementation Details).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
