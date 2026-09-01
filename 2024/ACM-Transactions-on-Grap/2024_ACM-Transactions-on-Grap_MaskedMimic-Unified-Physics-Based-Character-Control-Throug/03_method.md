# Method - MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/par/maskedmimic/; PDF retrieval source: https://research.nvidia.com/labs/par/maskedmimic/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (3. Inference), p. 4 (3 PRELIMINARIES), p. 8 (3. Inference), p. 8 (3. Inference), p. 5 (3. Inference), p. 6 (3. Inference)): The decoder D(𝑎𝑡/𝑠𝑡,𝑧𝑡) is then conditioned on a latent sampled from the encoder's distribution, and produces an action for the simulated character.

## Method Body Digest

- **p. 7 / 3. Inference - extractive body cue:** The decoder D(𝑎𝑡/𝑠𝑡,𝑧𝑡) is then conditioned on a latent sampled from the encoder's distribution, and produces an action for the simulated character.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** To train a versatile controller that can be directed using partial goals, we propose a simple training scheme that trains the controller on randomly masked ...
- **p. 8 / 3. Inference - extractive body cue:** The encoder and decoder are modeled as fully-connected networks, and observe a flattened concatenation of the input features.
- **p. 8 / 3. Inference - extractive body cue:** Encoder Prior Decoder Flatten Flatten Encode Tokens Transformer Fully-connected Fully-connected token masks (b) Detailed view: During training, features are extracted and masked from ground-truth motion ...
- **p. 5 / 3. Inference - extractive body cue:** Since the motion dataset only consist of kinematic motion clips, the primary purpose of 𝜋FC is to estimate the actions (motor actuations) required to control ...
- **p. 6 / 3. Inference - extractive body cue:** Training scene (screenshot): The top region consists of standard flat terrain, enabling the controller to reproduce the original motions in a setting that best represents ...
- **p. 7 / 3. Inference - extractive body cue:** MaskedMimic consists of 3 components: a learnable prior 𝜌, an encoder E, and a decoder D.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** The agent's objective is to learn a policy that maximizes the discounted cumulative reward: 𝐽= E𝑝(𝜏/𝜋) " 𝑇 ∑︁ 𝑡=0 𝛾𝑡𝑟𝑡 # , (1) where ...

## Design Rationale

- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Our framework consists of two stages.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Training on masked motion sequences enables the model to generalize to novel combinations of objectives.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose a framework that trains a versatile control model by leveraging the rich multi-modal information within existing motion capture datasets, such as kinematic trajectories, ...

## Source Evidence Cues

- **p. 7 / 3. Inference - extractive body cue:** The decoder D(𝑎𝑡/𝑠𝑡,𝑧𝑡) is then conditioned on a latent sampled from the encoder's distribution, and produces an action for the simulated character.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** To train a versatile controller that can be directed using partial goals, we propose a simple training scheme that trains the controller on randomly masked ...
- **p. 8 / 3. Inference - extractive body cue:** The encoder and decoder are modeled as fully-connected networks, and observe a flattened concatenation of the input features.
- **p. 8 / 3. Inference - extractive body cue:** Encoder Prior Decoder Flatten Flatten Encode Tokens Transformer Fully-connected Fully-connected token masks (b) Detailed view: During training, features are extracted and masked from ground-truth motion ...
- **p. 5 / 3. Inference - extractive body cue:** Since the motion dataset only consist of kinematic motion clips, the primary purpose of 𝜋FC is to estimate the actions (motor actuations) required to control ...
- **p. 6 / 3. Inference - extractive body cue:** Training scene (screenshot): The top region consists of standard flat terrain, enabling the controller to reproduce the original motions in a setting that best represents ...
- **p. 7 / 3. Inference - extractive body cue:** MaskedMimic consists of 3 components: a learnable prior 𝜌, an encoder E, and a decoder D.
- **Detected method headings:** 1. Fully Constrained Controller (p. 5); 2. Masked Mimic (Partially Constrained Controller) (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | The decoder D(𝑎𝑡/𝑠𝑡,𝑧𝑡) is then conditioned on a latent sampled from the encoder's distribution, and produces an action for the simulated character. | p. 7 (3. Inference), p. 4 (3 PRELIMINARIES) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | To train a versatile controller that can be directed using partial goals, we propose a simple training scheme that trains the controller ... | p. 4 (3 PRELIMINARIES), p. 8 (3. Inference) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | The encoder and decoder are modeled as fully-connected networks, and observe a flattened concatenation of the input features. | p. 8 (3. Inference), p. 8 (3. Inference) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 PRELIMINARIES - extractive body cue:** The agent's objective is to learn a policy that maximizes the discounted cumulative reward: 𝐽= E𝑝(𝜏/𝜋) " 𝑇 ∑︁ 𝑡=0 𝛾𝑡𝑟𝑡 # , (1) where ...
- **p. 7 / 3. Inference - extractive body cue:** All component are trained using an objective that maximizes the log-likelihood of actions predicted by 𝜋FC and minimizes the KL divergence between the encoder and ...
- **p. 5 / 3. Inference - extractive body cue:** The training objective is formulated as a motion-tracking reward and optimized using reinforcement learning [Mnih et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Intuitive partial constraints replace complex, error-prone reward functions, simplifying the design process (Figure 2).
- **p. 6 / 3. Inference - extractive body cue:** 5.3 Reward Function The reward 𝑟𝑡encourages the character to track a reference motion by minimizing the difference between the state of the simulated character and ...
- **p. 7 / 3. Inference - extractive body cue:** 6.1 Partial Goals The objective of 𝜋PC is to produce motions that conform to constraints specified by partial goals, akin to the task of motion ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 7 (3. Inference), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 5 (3. Inference).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | denotes, distribution, states, goals, observed, under, student, policy, Character, Observations, step, observes, current, humanoid | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | denotes, distribution, states, goals, observed, under, student, policy, Character, Observations | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | framework, consists, stages, Training, masked, motion, sequences, enables, model, generalize | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | agent, objective, learn, policy, maximizes, discounted, cumulative, reward, where, likelihood | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 PRELIMINARIES - extractive body cue:** (2) 𝑝(𝑠,𝑔/𝜋) denotes the distribution of states and goals observed under the student policy.
- **p. 5 / 3. Inference - extractive body cue:** Character Observations: At each step, 𝜋FC observes the current humanoid state 𝑠𝑡, consisting of the 3D body pose and velocity, canonicalized with respect to the ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** The agent then samples an action 𝑎𝑡from the policy 𝑎𝑡∼𝜋(𝑎𝑡/𝑠𝑡,𝑔𝑡).
- **p. 5 / 3. Inference - extractive body cue:** The objective is to predict the next actions based on the current character state, surrounding terrain, and a sequence of future target poses.
- **p. 8 / 3. Inference - extractive body cue:** To ensure the model supports high-level goals, such as textcommands and interaction with a target object, all future poses can be masked out.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** These partial descriptions can include target keyframes, target joint positions/rotations, text instructions, object interactions, or any combination thereof.
- **p. 6 / 3. Inference - extractive body cue:** 6 • Tessler, C. et al by the success of transformers in natural language processing, we tokenize each of the inputs and design 𝜋FC as ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | This path specifies target positions for the head (including height) at each timestep. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | To successfully follow a given target trajectory, consisting of a sequence of waypoint positions, we first compute the target rotation at each ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 PRELIMINARIES - extractive body cue:** To train a versatile controller that can be directed using partial goals, we propose a simple training scheme that trains the controller on randomly masked ...
- **p. 8 / 3. Inference - extractive body cue:** Encoder Prior Decoder Flatten Flatten Encode Tokens Transformer Fully-connected Fully-connected token masks (b) Detailed view: During training, features are extracted and masked from ground-truth motion ...
- **p. 5 / 3. Inference - extractive body cue:** Since the motion dataset only consist of kinematic motion clips, the primary purpose of 𝜋FC is to estimate the actions (motor actuations) required to control ...
- **p. 6 / 3. Inference - extractive body cue:** Training scene (screenshot): The top region consists of standard flat terrain, enabling the controller to reproduce the original motions in a setting that best represents ...
- **p. 7 / 3. Inference - extractive body cue:** The encoder is used solely for training, and is not utilized at runtime.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** decoder, then, conditioned, latent, sampled, encoder, distribution, produces, action, simulated, character, train, versatile, controller, directed, partial, goals, simple, training, scheme.
- **Relevant PDF headings:** 1. Fully Constrained Controller (p. 5); 2. Masked Mimic (Partially Constrained Controller) (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | To evaluate the effectiveness of our framework, we construct a benchmark consisting of common tasks introduced by prior systems. | p. 9 (7.2 Evaluation), p. 10 (7.2 Evaluation) |
| Balance-aware whole-body execution | This test establishes the baseline capability for motion generation, both in terms of success rates and tracking quality, and allows comparison to ... | p. 10 (7.2 Evaluation), p. 10 (7.2 Evaluation) |
| Recovery / adaptation | While MaskedMimic demonstrates high success rates in generating diverse motions, there are three notable areas for improvement in terms of motion quality. | p. 15 (8 RESULTS), p. 11 (8 RESULTS) |

## Failure and Ablation Link

- **p. 14 / Figure/Table caption - extractive body cue:** Table 6. Objects + ablation: We evaluate MaskedMimic and conduct an ablation on various design decisions. Experiments are conducted on the sitting task with a ...
- **p. 11 / 8 RESULTS - extractive body cue:** The superior performance of our model suggests that, in the context of full-body tracking, a welldesigned unified network can effectively capture the diversity of motions ...
- **p. 10 / 7.2 Evaluation - extractive body cue:** This form of goal-engineering (akin to prompt-engineering for language models) enables MaskedMimic to perform a range of new tasks, without additional task-specific training.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. The MaskedMimic framework: The first phase produces a fully- constrained controller 𝜋FC. This full-body tracker is trained using reinforce- ment learning to imitate ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Training scene (screenshot): The top region consists of standard flat terrain, enabling the controller to reproduce the original motions in a setting that ...
- **p. 12 / 8 RESULTS - extractive body cue:** By conditioning MaskedMimic on different goals at each stage of the task, the controller can be directed to perform a wide range of tasks without ...
- **p. 12 / 8 RESULTS - extractive body cue:** Full-body VR Success MPJPE Success MPOJPE FC Train 98% 51.5 Test 98.2% 51 MaskedMimic Train 94.7% 61.3 94.4% 62.7 Test 95.4% 62.9 93.6% 69.4 In ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (3. Inference), p. 4 (3 PRELIMINARIES), p. 8 (3. Inference), p. 8 (3. Inference), p. 5 (3. Inference), p. 6 (3. Inference), objective p. 4 (3 PRELIMINARIES), p. 7 (3. Inference), p. 5 (3. Inference), p. 2 (1 INTRODUCTION), p. 6 (3. Inference), p. 7 (3. Inference), temporal p. 10 (7.2 Evaluation), p. 12 (8 RESULTS), p. 9 (7.2 Evaluation), p. 10 (7.2 Evaluation), p. 5 (3. Inference), p. 5 (3. Inference).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
