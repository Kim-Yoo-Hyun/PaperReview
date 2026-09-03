# Method - SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/10610040/; PDF retrieval source: https://arxiv.org/pdf/2401.16013. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (4.5. Impedance Controller for Contact-Rich), p. 6 (4.5. Impedance Controller for Contact-Rich), p. 5 (4.5. Impedance Controller for Contact-Rich), p. 5 (4.5. Impedance Controller for Contact-Rich), p. 7 (4.6. Relative Observation and Action Frame), p. 7 (4.6. Relative Observation and Action Frame)): The output from the RL policy is tracked within a block of time by the downstream controller. this objective will then be converted into joint space torques by multiplying Jacobian ...

## Method Body Digest

- **p. 6 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** The output from the RL policy is tracked within a block of time by the downstream controller. this objective will then be converted into joint ...
- **p. 6 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** This might seem reasonable, but can be impractical in some scenarios: some objects such as the PCB board may require a very small interaction force, ...
- **p. 5 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** A typical setup for robotic RL employs a two-layered control hierarchy, where an RL policy produces setpoint actions at a much lower frequency than the ...
- **p. 5 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** A typical impedance control objective for this controller is 𝐹= 𝑘𝑝⋅𝑒+ 𝑘𝑑⋅̇ 𝑒+ 𝐹𝑓𝑓+ 𝐹𝑐𝑜𝑟, where 𝑒= 𝑝-𝑝𝑟𝑒𝑓, 𝑝is the measured pose, and 𝑝𝑟𝑒𝑓is the ...
- **p. 7 / 4.6. Relative Observation and Action Frame - extractive body cue:** The robot's proprioceptive information is expressed with respect to frame of the end-effector's initial pose; the action output from the policy (6D twist) is relative ...
- **p. 7 / 4.6. Relative Observation and Action Frame - extractive body cue:** Package Task Training time Success rate Demos Shaping?
- **p. 6 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** At the same time, we strictly enforce the reference constraint at the real-time level whenever in contact.
- **p. 6 / 4.6. Relative Observation and Action Frame - extractive body cue:** The target, for instance, the PCB insertion socket holes, is fixed relative to the robot base frame, and the reward can be specified using any ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** However, in the process of evaluating our framework, we also make a scientifically interesting empirical observation: when implemented properly in a carefully engineered software package, ...
- **p. 2 / 1. Introduction - extractive body cue:** SERL consists of the following components: (1) a high-quality RL implementation that is geared towards real-world robotic learning and supports image observations and demonstrations; (2) ...
- **p. 6 / 4.6. Relative Observation and Action Frame - extractive body cue:** To develop an agent capable of adapting to a dynamic target, we propose a training procedure that simulates a moving target without the need for ...

## Source Evidence Cues

- **p. 6 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** The output from the RL policy is tracked within a block of time by the downstream controller. this objective will then be converted into joint ...
- **p. 6 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** This might seem reasonable, but can be impractical in some scenarios: some objects such as the PCB board may require a very small interaction force, ...
- **p. 5 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** A typical setup for robotic RL employs a two-layered control hierarchy, where an RL policy produces setpoint actions at a much lower frequency than the ...
- **p. 5 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** A typical impedance control objective for this controller is 𝐹= 𝑘𝑝⋅𝑒+ 𝑘𝑑⋅̇ 𝑒+ 𝐹𝑓𝑓+ 𝐹𝑐𝑜𝑟, where 𝑒= 𝑝-𝑝𝑟𝑒𝑓, 𝑝is the measured pose, and 𝑝𝑟𝑒𝑓is the ...
- **p. 7 / 4.6. Relative Observation and Action Frame - extractive body cue:** The robot's proprioceptive information is expressed with respect to frame of the end-effector's initial pose; the action output from the policy (6D twist) is relative ...
- **p. 7 / 4.6. Relative Observation and Action Frame - extractive body cue:** Package Task Training time Success rate Demos Shaping?
- **Detected method headings:** 4.5. Impedance Controller for Contact-Rich (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | The output from the RL policy is tracked within a block of time by the downstream controller. this objective will then be ... | p. 6 (4.5. Impedance Controller for Contact-Rich), p. 6 (4.5. Impedance Controller for Contact-Rich) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | This might seem reasonable, but can be impractical in some scenarios: some objects such as the PCB board may require a very ... | p. 6 (4.5. Impedance Controller for Contact-Rich), p. 5 (4.5. Impedance Controller for Contact-Rich) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | A typical setup for robotic RL employs a two-layered control hierarchy, where an RL policy produces setpoint actions at a much lower ... | p. 5 (4.5. Impedance Controller for Contact-Rich), p. 5 (4.5. Impedance Controller for Contact-Rich) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** A typical impedance control objective for this controller is 𝐹= 𝑘𝑝⋅𝑒+ 𝑘𝑑⋅̇ 𝑒+ 𝐹𝑓𝑓+ 𝐹𝑐𝑜𝑟, where 𝑒= 𝑝-𝑝𝑟𝑒𝑓, 𝑝is the measured pose, and 𝑝𝑟𝑒𝑓is the ...
- **p. 6 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** At the same time, we strictly enforce the reference constraint at the real-time level whenever in contact.
- **p. 6 / 4.6. Relative Observation and Action Frame - extractive body cue:** The target, for instance, the PCB insertion socket holes, is fixed relative to the robot base frame, and the reward can be specified using any ...
- **p. 7 / 4.6. Relative Observation and Action Frame - extractive body cue:** The green box indicates a state where the robot receives a high reward for completing the task.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 5 (4.5. Impedance Controller for Contact-Rich), p. 6 (4.5. Impedance Controller for Contact-Rich), p. 6 (4.5. Impedance Controller for Contact-Rich).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Robotic, reinforcement, learning, tasks, defined, MDP, where, state, observation, image, combination, current, end-effector, position | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | Robotic, reinforcement, learning, tasks, defined, MDP, where, state, observation, image | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | However, process, evaluating, framework, make, scientifically, interesting, empirical, observation, when | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | typical, impedance, control, objective, controller, where, measured, pose, target, computed | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Preliminaries and Problem Statement - extractive body cue:** Robotic reinforcement learning tasks can be defined via an MDP = {, , 𝜌, , 𝑟, 𝛾}, where 𝐬∈is the state observation (e.g., an image ...
- **p. 7 / 4.6. Relative Observation and Action Frame - extractive body cue:** The robot's proprioceptive information is expressed with respect to frame of the end-effector's initial pose; the action output from the policy (6D twist) is relative ...
- **p. 6 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** One might wonder if we should directly clip the action output by the RL policy.
- **p. 6 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** The output from the RL policy is tracked within a block of time by the downstream controller. this objective will then be converted into joint ...
- **p. 2 / 1. Introduction - extractive body cue:** For each of these tasks, SERL is able to learn effectively within 15 - 60 min of training per policy (in terms of total wall-clock ...
- **p. 3 / 3. Preliminaries and Problem Statement - extractive body cue:** An optimal policy 𝜋is one that maximizes the cumulative expected value of the reward, i.e., 𝐸[∑∞ 𝑡=0 𝛾𝑡𝑟(𝐬𝑡, 𝐚𝑡)], where the expectation is taken with ...
- **p. 5 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** A typical setup for robotic RL employs a two-layered control hierarchy, where an RL policy produces setpoint actions at a much lower frequency than the ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value was not selected from the PDF body. | tion Frame Let the robot's base frame be {𝑠}; for the 𝑖-th episode of rolling out the policy, we denote {𝑏(𝑖) 𝑡} ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | This might seem reasonable, but can be impractical in some scenarios: some objects such as the PCB board may require a very ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | 4, where a high-level RL controller 𝜋(𝐚/𝐬) sends control targets at 10HZ for the low-level impedance controller to track at 1K HZ, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.5. Impedance Controller for Contact-Rich - extractive body cue:** This might seem reasonable, but can be impractical in some scenarios: some objects such as the PCB board may require a very small interaction force, ...
- **p. 7 / 4.6. Relative Observation and Action Frame - extractive body cue:** Package Task Training time Success rate Demos Shaping?
- **p. 8 / 5. Experiments - extractive body cue:** Comparison to prior systems: While it's difficult to directly compare our results to those of prior systems due to numerous differences in the setup, lack ...
- **p. 9 / 5. Experiments - extractive body cue:** SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Figure 8: Peg Insertion Task at University of Washington these prior works generally have either lower ...
- **p. 8 / 5. Experiments - extractive body cue:** SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Task # of Demos Image Input Random Reset Reward Specification Bin Size Training Time PCB Component ...
- **p. 7 / 4.6. Relative Observation and Action Frame - extractive body cue:** Package Task Training time Success rate Demos Shaping?

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** output, policy, tracked, within, block, time, downstream, controller, objective, will, then, converted, joint, space, torques, multiplying, Jacobian, transpose, offset, nullspace.
- **Relevant PDF headings:** 4.5. Impedance Controller for Contact-Rich (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Task # of Demos Image Input Random Reset Reward Specification Bin Size Training ... | p. 8 (5. Experiments), p. 7 (5. Experiments) |
| Policy fitting | For the cable routing task and PCB insertion task, our policies outperform BC baselines by a large margin, despite training with 5x ... | p. 8 (5. Experiments), p. 8 (5. Experiments) |
| Closed-loop rollout | The learned RL policies not only outperformed their BC counterparts by as much as 10x in terms of success rate but also ... | p. 8 (5. Experiments), p. 9 (5. Experiments) |

## Failure and Ablation Link

- **p. 8 / 5. Experiments - extractive body cue:** SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Task # of Demos Image Input Random Reset Reward Specification Bin Size Training Time PCB Component ...
- **p. 9 / 5. Experiments - extractive body cue:** Although the components of our system are all based on (recent) prior work, the stateof-the-art performance of this combination illustrates our main thesis: the details ...
- **p. 9 / 6. Discussion - extractive body cue:** Our framework does have a number of limitations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (4.5. Impedance Controller for Contact-Rich), p. 6 (4.5. Impedance Controller for Contact-Rich), p. 5 (4.5. Impedance Controller for Contact-Rich), p. 5 (4.5. Impedance Controller for Contact-Rich), p. 7 (4.6. Relative Observation and Action Frame), p. 7 (4.6. Relative Observation and Action Frame), objective p. 5 (4.5. Impedance Controller for Contact-Rich), p. 6 (4.5. Impedance Controller for Contact-Rich), p. 6 (4.6. Relative Observation and Action Frame), p. 7 (4.6. Relative Observation and Action Frame), temporal p. 9 (7.1. Details on Relative Observation and Ac), p. 6 (4.5. Impedance Controller for Contact-Rich), p. 8 (5. Experiments), p. 5 (4.5. Impedance Controller for Contact-Rich), p. 10 (7.1. Details on Relative Observation and Ac), p. 4 (4. Sample Efficient Robotic Reinforce).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Robotic reinforcement learning tasks can be defined via an MDP = {, , 𝜌, , 𝑟, 𝛾}, where 𝐬∈is the state observation (e.g., an image in combination with the current ... (p. 3, 3. Preliminaries and Problem Statement).
- **Objective/update evidence:** A typical impedance control objective for this controller is 𝐹= 𝑘𝑝⋅𝑒+ 𝑘𝑑⋅̇ 𝑒+ 𝐹𝑓𝑓+ 𝐹𝑐𝑜𝑟, where 𝑒= 𝑝-𝑝𝑟𝑒𝑓, 𝑝is the measured pose, and 𝑝𝑟𝑒𝑓is the target pose computed by the ... (p. 5, 4.5. Impedance Controller for Contact-Rich).
- **Temporal/runtime evidence:** tion Frame Let the robot's base frame be {𝑠}; for the 𝑖-th episode of rolling out the policy, we denote {𝑏(𝑖) 𝑡} as the endeffector frame expressed w.r.t. {𝑠} at ... (p. 9, 7.1. Details on Relative Observation and Ac).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
