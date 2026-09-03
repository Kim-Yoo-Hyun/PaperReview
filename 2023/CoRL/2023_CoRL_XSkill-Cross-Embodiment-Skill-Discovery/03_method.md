# Method - XSkill: Cross Embodiment Skill Discovery

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v229/xu23a.html; PDF retrieval source: https://arxiv.org/pdf/2307.09955. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3 Approach), p. 4 (3 Approach), p. 3 (3 Approach), p. 4 (3 Approach)): From this video prompt, the algorithm first identifies the order of skills used in the prompt and then composes the skills using the learned policy P(a/s, z).

## Method Body Digest

- **p. 3 / 3 Approach - extractive body cue:** From this video prompt, the algorithm first identifies the order of skills used in the prompt and then composes the skills using the learned policy ...
- **p. 4 / 3 Approach - extractive body cue:** Then, we extract the skill representation zij = ftemporal(vij) from each video clip with a temporal skill encoder consisting of a vision backbone and a ...
- **p. 3 / 3 Approach - extractive body cue:** In the Compose phase, the algorithm takes as input a single human prompt video τ h prompt for a new task that requires an unseen ...
- **p. 4 / 3 Approach - extractive body cue:** • Regularizing the training process using Sinkhorn-Knopp clustering [63, 1] within singleembodiment batches.
- **p. 4 / 3 Approach - extractive body cue:** Both ftemporal and fprototype are trained jointly to minimize the CorssEntropy loss between the predicted pij and target qij skill prototypes distributions: Lprototype =
- **p. 3 / 3 Approach - extractive body cue:** In the transfer phase, the algorithm uses the robot teleoperation dataset Dr to learn the skill-conditioned visuomotor policy P(a/s, z), where z ∈Z and s ...
- **p. 2 / 1 Introduction - extractive body cue:** 2) A skill-conditioned diffusion policy that translates the observed human demonstration into robot actions.
- **p. 2 / 1 Introduction - extractive body cue:** With the identified cross-embodiment skill prototypes, the robot can then learn a skill-conditioned visuomotor policy that transfers each identified skill to the robot's action space.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first ...
- **p. 1 / 1 Introduction - extractive body cue:** We refer to the task as "Cross-Embodiment Skill Discovery" and introduce our method 7th Conference on Robot Learning (CoRL 2023), Atlanta, USA.
- **p. 2 / 1 Introduction - extractive body cue:** To encourage across-embodiment alignment, we introduce a set of learnable skill prototypes through feature clustering.

## Source Evidence Cues

- **p. 3 / 3 Approach - extractive body cue:** From this video prompt, the algorithm first identifies the order of skills used in the prompt and then composes the skills using the learned policy ...
- **p. 4 / 3 Approach - extractive body cue:** Then, we extract the skill representation zij = ftemporal(vij) from each video clip with a temporal skill encoder consisting of a vision backbone and a ...
- **p. 3 / 3 Approach - extractive body cue:** In the Compose phase, the algorithm takes as input a single human prompt video τ h prompt for a new task that requires an unseen ...
- **p. 4 / 3 Approach - extractive body cue:** • Regularizing the training process using Sinkhorn-Knopp clustering [63, 1] within singleembodiment batches.
- **Detected method headings:** 3 Approach (p. 3); A.4.1 Sinkhorn-Knopp Algorithm (p. 16); A.4.4 Diffusion Policy (p. 18)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | From this video prompt, the algorithm first identifies the order of skills used in the prompt and then composes the skills using ... | p. 3 (3 Approach), p. 4 (3 Approach) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | Then, we extract the skill representation zij = ftemporal(vij) from each video clip with a temporal skill encoder consisting of a vision ... | p. 4 (3 Approach), p. 3 (3 Approach) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | In the Compose phase, the algorithm takes as input a single human prompt video τ h prompt for a new task that ... | p. 3 (3 Approach), p. 4 (3 Approach) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Approach - extractive body cue:** Both ftemporal and fprototype are trained jointly to minimize the CorssEntropy loss between the predicted pij and target qij skill prototypes distributions: Lprototype =
- **p. 4 / 3 Approach - extractive body cue:** • Regularizing the training process using Sinkhorn-Knopp clustering [63, 1] within singleembodiment batches.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 4 (3 Approach).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | transfer, phase, algorithm, uses, robot, teleoperation, dataset, learn, skill-conditioned, visuomotor, policy, where, includes, proprioception | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | transfer, phase, algorithm, uses, robot, teleoperation, dataset, learn, skill-conditioned, visuomotor | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | Together, cross-embodiment, dataset, simulation, real, world, hope, inspire, future, exploration | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | ftemporal, fprototype, trained, jointly, minimize, CorssEntropy, loss, between, predicted, target | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 Approach - extractive body cue:** In the transfer phase, the algorithm uses the robot teleoperation dataset Dr to learn the skill-conditioned visuomotor policy P(a/s, z), where z ∈Z and s ...
- **p. 3 / 3 Approach - extractive body cue:** From this video prompt, the algorithm first identifies the order of skills used in the prompt and then composes the skills using the learned policy ...
- **p. 2 / 1 Introduction - extractive body cue:** 2) A skill-conditioned diffusion policy that translates the observed human demonstration into robot actions.
- **p. 2 / 1 Introduction - extractive body cue:** With the identified cross-embodiment skill prototypes, the robot can then learn a skill-conditioned visuomotor policy that transfers each identified skill to the robot's action space.
- **p. 4 / 3 Approach - extractive body cue:** The target distribution qij is obtained from the other augmented version of the same video clip.
- **p. 4 / 3 Approach - extractive body cue:** The probability pij of skills being executed in the given video clip vij is predicted by applying the Softmax function.
- **p. 1 / 1 Introduction - extractive body cue:** 3) Compose, performing novel compositions of the learned skills to accomplish new tasks.
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value was not selected from the PDF body. | If the robot executes an undemonstrated sub-task, the episode ends. | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | The video clip length L and uniform sample frames M are set as 8 and 100 for both simulated and real-world kitchens. | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 Approach - extractive body cue:** • Regularizing the training process using Sinkhorn-Knopp clustering [63, 1] within singleembodiment batches.
- **p. 6 / 4 Evaluation - extractive body cue:** TCN: Same as the GCD Policy above but replacing the video encoder with pre-trained Time-Contrastive Network (TCN)[67]. • XSkill w.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** video, prompt, algorithm, first, identifies, order, skills, then, composes, learned, policy, extract, skill, representation, ftemporal, clip, temporal, encoder, consisting, vision.
- **Relevant PDF headings:** 3 Approach (p. 3); A.4.1 Sinkhorn-Knopp Algorithm (p. 16); A.4.4 Diffusion Policy (p. 18).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | During the inference, the robot must complete an unseen composition of subtasks after viewing a prompt video from the sphere agent demonstration. ... | p. 6 (4 Evaluation), p. 6 (4 Evaluation) |
| Policy fitting | 1 & 2) on unseen tasks with cross-embodiment prompts in simulated and real-world environments, which outperforms all baselines. | p. 7 (4 Evaluation), p. 6 (4 Evaluation) |
| Closed-loop rollout | [XSkill] achieves 70.2% and 60% success (Tab. | p. 7 (4 Evaluation), p. 7 (4 Evaluation) |

## Failure and Ablation Link

- **p. 6 / 4 Evaluation - extractive body cue:** The ablation study on K, time contrastive loss, and more implementation details can be found in the supplementary material.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is augmented ...
- **p. 6 / 4 Evaluation - extractive body cue:** NN-composition: XSkill removing skill alignment transformer.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is augmented ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Execution on a novel task and robustness to perturbation. (a) XSkill analyzes a human video of a novel task, identifying skills for each ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3 Approach), p. 4 (3 Approach), p. 3 (3 Approach), p. 4 (3 Approach), objective p. 4 (3 Approach), p. 4 (3 Approach), temporal p. 6 (4 Evaluation), p. 6 (4 Evaluation), p. 7 (4 Evaluation), p. 4 (3 Approach), p. 5 (B P), p. 8 (4 Subtasks Avg).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** In the transfer phase, the algorithm uses the robot teleoperation dataset Dr to learn the skill-conditioned visuomotor policy P(a/s, z), where z ∈Z and s includes both robot proprioception and ... (p. 3, 3 Approach).
- **Objective/update evidence:** Both ftemporal and fprototype are trained jointly to minimize the CorssEntropy loss between the predicted pij and target qij skill prototypes distributions: Lprototype = (p. 4, 3 Approach).
- **Temporal/runtime evidence:** If the robot executes an undemonstrated sub-task, the episode ends. (p. 6, 4 Evaluation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
