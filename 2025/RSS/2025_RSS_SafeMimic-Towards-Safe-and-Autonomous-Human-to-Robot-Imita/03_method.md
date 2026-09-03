# Method - SafeMimic: Towards Safe and Autonomous Human-to-Robot Imitation for Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p128.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p128.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (C. Learning from Previous Successful Exploration), p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 6 (C. Learning from Previous Successful Exploration), p. 1 (Abstract), p. 5 (C. Learning from Previous Successful Exploration), p. 4 (B. Safe and Autonomous Real-World Adaptation)): The architecture for the action prediction policy network is composed by a PointNet [66] encoder for the visual information, and a SentenceTransformer [67] for the task description, combined with an ...

## Method Body Digest

- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** The architecture for the action prediction policy network is composed by a PointNet [66] encoder for the visual information, and a SentenceTransformer [67] for the ...
- **p. 4 / B. Safe and Autonomous Real-World Adaptation - extractive body cue:** The state representation consists of simulated pointclouds and robot proprioceptive information (for details of the network architecture, see Appendix A).
- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning (1L) baselines based ...
- **p. 1 / Abstract - extractive body cue:** Then, it adapts the behavior to the robot's own morphology by sampling candidate actions around the human ones, and verifying them for safety before execution ...
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** To that end, we then train an action prediction policy network that maps point clouds, P" and language description of the task, {to actions, e.g. ...
- **p. 4 / B. Safe and Autonomous Real-World Adaptation - extractive body cue:** Given this function, the robot's objective is to find a policy that maps states to the actions that maximize the task reward while remaining safe, ...
- **p. 2 / I. INrRopucTION - extractive body cue:** Other works have explored human video modeling as a pretraining objective [19, 20].
- **p. 2 / I. INrRopucTION - extractive body cue:** Learning from Human Video directly has received increasing attention as strategy to learn manipulation skills Some works have explored leveraging large collections of human activity ...

## Design Rationale

- **p. 2 / I. INrRopucTION - extractive body cue:** environments with different human teachers, and observe experimentally that our framework enables the robot to suc cessfully acquire the desired behaviors safely and more efficiently ...
- **p. 1 / Abstract - extractive body cue:** Our experiments show that our method allows robots to safely fand efficiently learn multistep mobile manipulation behaviors from a single human demonstration, from different users, ...
- **p. 2 / I. INrRopucTION - extractive body cue:** In summary, SAFEMIMIC introduces several novel contributions:

## Source Evidence Cues

- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** The architecture for the action prediction policy network is composed by a PointNet [66] encoder for the visual information, and a SentenceTransformer [67] for the ...
- **p. 4 / B. Safe and Autonomous Real-World Adaptation - extractive body cue:** The state representation consists of simulated pointclouds and robot proprioceptive information (for details of the network architecture, see Appendix A).
- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning (1L) baselines based ...
- **p. 1 / Abstract - extractive body cue:** Then, it adapts the behavior to the robot's own morphology by sampling candidate actions around the human ones, and verifying them for safety before execution ...
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** To that end, we then train an action prediction policy network that maps point clouds, P" and language description of the task, {to actions, e.g. ...
- **p. 4 / B. Safe and Autonomous Real-World Adaptation - extractive body cue:** Given this function, the robot's objective is to find a policy that maps states to the actions that maximize the task reward while remaining safe, ...
- **p. 2 / I. INrRopucTION - extractive body cue:** Other works have explored human video modeling as a pretraining objective [19, 20].
- **Detected method headings:** A. Model Details (p. 13)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | The architecture for the action prediction policy network is composed by a PointNet [66] encoder for the visual information, and a SentenceTransformer ... | p. 5 (C. Learning from Previous Successful Exploration), p. 4 (B. Safe and Autonomous Real-World Adaptation) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | The state representation consists of simulated pointclouds and robot proprioceptive information (for details of the network architecture, see Appendix A). | p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 6 (C. Learning from Previous Successful Exploration) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning ... | p. 6 (C. Learning from Previous Successful Exploration), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / B. Safe and Autonomous Real-World Adaptation - extractive body cue:** Given this function, the robot's objective is to find a policy that maps states to the actions that maximize the task reward while remaining safe, ...
- **p. 2 / I. INrRopucTION - extractive body cue:** Learning from Human Video directly has received increasing attention as strategy to learn manipulation skills Some works have explored leveraging large collections of human activity ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, to mitigate the dependency on costly human ‘monitoring, this learning process should be performed in a sale 1d autonomous manner.
- **p. 1 / I. INrRopucTION - extractive body cue:** This would bypass the need for costly teleoperated data collection (1, 2, 3}, which is significantly complex and time-consuming for multi-step tasks and those combining ...
- **p. 2 / I. INrRopucTION - extractive body cue:** as collisions, excessive forces, or grasp losses and, as we
- **p. 3 / I. INrRopucTION - extractive body cue:** In the real-world, such constraints are difficult to acquire in novel environments, much less in the presence of human teachers.
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 2 (I. INrRopucTION), p. 2 (I. INrRopucTION), p. 3 (I. INrRopucTION), p. 3 (I. INrRopucTION), p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 4 (B. Safe and Autonomous Real-World Adaptation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | evaluate, data, generated, train, safety, Qfunctions, would, suffice, training, task, policies, include, Imitation, Learning | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | evaluate, data, generated, train, safety, Qfunctions, would, suffice, training, task | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | environments, different, human, teachers, observe, experimentally, framework, enables, robot, cessfully | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | Given, function, robot, objective, find, policy, maps, states, actions, maximize | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning (1L) baselines based ...
- **p. 4 / B. Safe and Autonomous Real-World Adaptation - extractive body cue:** Given this function, the robot's objective is to find a policy that maps states to the actions that maximize the task reward while remaining safe, ...
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** To that end, we then train an action prediction policy network that maps point clouds, P" and language description of the task, {to actions, e.g. ...
- **p. 2 / I. INrRopucTION - extractive body cue:** Most closely related t0 SAFEMIMIC, several works imitate human actions directly by tracking the human pose and extracting actions using pose tracking before finetuning with ...
- **p. 2 / I. INrRopucTION - extractive body cue:** These works address the requirement of autonomy, but generally sidestep the question of safety - ‘critical challenge when learning mobile manipulation in the real world, ...
- **p. 4 / B. Safe and Autonomous Real-World Adaptation - extractive body cue:** We adopt the standard MDP formalism and represent each segment by the tuple M = (S,A, R,T,7). where S is the state space, A is ...
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** The architecture for the action prediction policy network is composed by a PointNet [66] encoder for the visual information, and a SentenceTransformer [67] for the ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value was not selected from the PDF body. | Then, it adapts the behavior to the robot's own morphology by sampling candidate actions around the human ones, and verifying them for ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value was not selected from the PDF body. | However, these techniques are restricted to short horizon skills and require tedious human supervision, tasked with ensuring that the robot exploration is ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value was not selected from the PDF body. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile was not selected from the PDF body. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** The architecture for the action prediction policy network is composed by a PointNet [66] encoder for the visual information, and a SentenceTransformer [67] for the ...
- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning (1L) baselines based ...
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** To that end, we then train an action prediction policy network that maps point clouds, P" and language description of the task, {to actions, e.g. ...
- **p. 2 / I. INrRopucTION - extractive body cue:** Other works have explored human video modeling as a pretraining objective [19, 20].
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** The architecture for the action prediction policy network is composed by a PointNet [66] encoder for the visual information, and a SentenceTransformer [67] for the ...
- **p. 3 / I. INrRopucTION - extractive body cue:** Constrained RL methods (48, 49, 50, 51] similarly allow for policy learning while obeying constraints, though typically require closed-form constraints available at runtime.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** architecture, action, prediction, policy, network, composed, PointNet, encoder, visual, information, SentenceTransformer, task, description, combined, MLP, head, trained, geometric, augmentations, rotations.
- **Relevant PDF headings:** A. Model Details (p. 13).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning ... | p. 6 (C. Learning from Previous Successful Exploration), p. 8 (C. Learning from Previous Successful Exploration) |
| Base-arm task decision | Note as well hat some lines overlap at the Same ly outperforms all baselines and achieves upto 100% sucess ia exploratory adaptation, ... | p. 6 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration) |
| Execution / correction | We observe that SAFEMIMIC achieves a minimum of 40% final suc- ‘cess rate over the seven tasks, significantly outperforming all baselines. | p. 7 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration) |

## Failure and Ablation Link

- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** This baseline is SAFEMIMIC without the use of SQFs.
- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** We compare SAFEMIMC's tsk performance 10 five baselines: direct exccution without safety Q-unctions (SQFs), which equires human supervsia, dict execution with SQFs, exploration without SQF, ...
- **p. 7 / C. Learning from Previous Successful Exploration - extractive body cue:** Exploration alone (Explozat Lon without SO®) similarly results in 14.2% unsafe actions, demonstrating the critical need for safety during exploration
- **p. 7 / C. Learning from Previous Successful Exploration - extractive body cue:** The Direct Execution (without safety Q-functions) gen erates 13.4% unsafe actions and incurs safety violations in nearly every task, commonly colliding during both navigation and ...
- **p. 8 / C. Learning from Previous Successful Exploration - extractive body cue:** explored hy" SAFEMIMIC with (cgh0) and without policy memory lef, Successful attempts from an ial exploration are recorded and use to tain the policy memory.
- **p. 8 / V. LIMITATIONS AND FUTURE WORK - extractive body cue:** Scaling to other types of safety violations or task failures presents an opportunity for future work.
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** We evaluate SaFEMIMIC in 7 challenging multi-step mobile ‘manipulation tasks demonstrated by humans. ‘The tasks all consist of multiple stages and require navigation, rigid-body pick-and-place, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (C. Learning from Previous Successful Exploration), p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 6 (C. Learning from Previous Successful Exploration), p. 1 (Abstract), p. 5 (C. Learning from Previous Successful Exploration), p. 4 (B. Safe and Autonomous Real-World Adaptation), objective p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 2 (I. INrRopucTION), p. 1 (Abstract), p. 1 (I. INrRopucTION), p. 2 (I. INrRopucTION), p. 3 (I. INrRopucTION), temporal p. 1 (Abstract), p. 1 (I. INrRopucTION), p. 2 (I. INrRopucTION), p. 2 (I. INrRopucTION), p. 4 (I. INrRopucTION), p. 4 (B. Safe and Autonomous Real-World Adaptation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The architecture for the action prediction policy network is composed by a PointNet [66] encoder for the visual information, and a SentenceTransformer [67] for the task description, combined with an ... (p. 5, C. Learning from Previous Successful Exploration).
- **Objective/update evidence:** Given this function, the robot's objective is to find a policy that maps states to the actions that maximize the task reward while remaining safe, given formally by: (p. 4, B. Safe and Autonomous Real-World Adaptation).
- **Temporal/runtime evidence:** However, these techniques are restricted to short horizon skills and require tedious human supervision, tasked with ensuring that the robot exploration is safe, resetting the task constantly and detecting success, ... (p. 1, I. INrRopucTION).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
