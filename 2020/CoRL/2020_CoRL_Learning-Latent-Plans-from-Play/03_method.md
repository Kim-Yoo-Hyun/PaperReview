# Method - Learning Latent Plans from Play

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/lynch20a.html; PDF retrieval source: https://arxiv.org/pdf/1903.01973. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 12 (A.2 Architecture Details), p. 12 (A.2 Architecture Details), p. 17 (A.4.3 Coverage Analysis of Interaction Space), p. 15 (A.3.4 Training Data), p. 15 (A.3.4 Training Data), p. 16 (A.4.3 Coverage Analysis of Interaction Space)): Action space Our 8-DOF agent's action space state consists of: 3 cartesian coordinates for the position of its end effector, 3 Euler angles representing its end effector orientation, and 2 ...

## Method Body Digest

- **p. 12 / A.2 Architecture Details - extractive body cue:** Action space Our 8-DOF agent's action space state consists of: 3 cartesian coordinates for the position of its end effector, 3 Euler angles representing its ...
- **p. 12 / A.2 Architecture Details - extractive body cue:** 9 we show the layers with their sizes and depths of different sub-networks used in the model: the vision network, plan recognition network, plan proposal ...
- **p. 17 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** Our state models were trained on a smaller dataset, up to 180 minutes of play (see Fig 8). "Random": we collected a random exploration dataset ...
- **p. 15 / A.3.4 Training Data - extractive body cue:** We model an 8-dof continuous action space representing agent end effector position, rotation, and gripper control.
- **p. 15 / A.3.4 Training Data - extractive body cue:** Tasks are specified to goal-conditioned models by resetting the environment to the initial state of the demonstration, and feeding in the final state as the ...
- **p. 16 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** 2d, we quantitatively measure the coverage of interaction space for different methods.
- **p. 16 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** To compute regions of interaction space, we quantized the 11 dimensions of action space corresponding to object interactions: the 3 position and 3 euler angle ...
- **p. 15 / A.3.4 Training Data - extractive body cue:** An updated version of the Mujoco HAPTIX system is used to collect teleoperation demonstration data [39].

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose an alternative means of obtaining task-agnostic control-self-supervising on top of unlabeled teleoperated play data: continuous logs of low-level observations and ...
- **p. 3 / 1 Introduction - extractive body cue:** 3, we propose two self-supervised methods for learning task-agnostic control from play: Play-GCBC and Play-LMP.
- **p. 12 / A.2 Architecture Details - extractive body cue:** Action space Our 8-DOF agent's action space state consists of: 3 cartesian coordinates for the position of its end effector, 3 Euler angles representing its ...

## Source Evidence Cues

- **p. 12 / A.2 Architecture Details - extractive body cue:** Action space Our 8-DOF agent's action space state consists of: 3 cartesian coordinates for the position of its end effector, 3 Euler angles representing its ...
- **p. 12 / A.2 Architecture Details - extractive body cue:** 9 we show the layers with their sizes and depths of different sub-networks used in the model: the vision network, plan recognition network, plan proposal ...
- **p. 17 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** Our state models were trained on a smaller dataset, up to 180 minutes of play (see Fig 8). "Random": we collected a random exploration dataset ...
- **p. 15 / A.3.4 Training Data - extractive body cue:** We model an 8-dof continuous action space representing agent end effector position, rotation, and gripper control.
- **p. 15 / A.3.4 Training Data - extractive body cue:** Tasks are specified to goal-conditioned models by resetting the environment to the initial state of the demonstration, and feeding in the final state as the ...
- **p. 16 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** 2d, we quantitatively measure the coverage of interaction space for different methods.
- **p. 16 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** To compute regions of interaction space, we quantized the 11 dimensions of action space corresponding to object interactions: the 3 position and 3 euler angle ...
- **Detected method headings:** A.2 Architecture Details (p. 12)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | Action space Our 8-DOF agent's action space state consists of: 3 cartesian coordinates for the position of its end effector, 3 Euler ... | p. 12 (A.2 Architecture Details), p. 12 (A.2 Architecture Details) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | 9 we show the layers with their sizes and depths of different sub-networks used in the model: the vision network, plan recognition ... | p. 12 (A.2 Architecture Details), p. 17 (A.4.3 Coverage Analysis of Interaction Space) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | Our state models were trained on a smaller dataset, up to 180 minutes of play (see Fig 8). "Random": we collected a ... | p. 17 (A.4.3 Coverage Analysis of Interaction Space), p. 15 (A.3.4 Training Data) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 15 / A.3.4 Training Data - extractive body cue:** An updated version of the Mujoco HAPTIX system is used to collect teleoperation demonstration data [39].
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 15 (A.3.4 Training Data).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Algorithm, Training, Play-LMP, Input, Play, data, Randomly, initialize, model, parameters, LMP, while, done, Sample | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | Algorithm, Training, Play-LMP, Input, Play, data, Randomly, initialize, model, parameters | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | alternative, means, obtaining, task-agnostic, control-self-supervising, unlabeled, teleoperated, play, data, continuous | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | updated, version, Mujoco, HAPTIX, system, collect, teleoperation, demonstration, data | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 12 / A.1 Theoretical Motivation - extractive body cue:** Algorithm 2 Training Play-LMP 1: Input: Play data D : {(s1, a1), · · · , (sT , aT )} 2: Randomly initialize model parameters ...
- **p. 2 / 1 Introduction - extractive body cue:** (a) Training: 1) sample a random window of experience from a memory of play data; 2) train to recognize and organize a repertoire of behaviors ...
- **p. 12 / A.2 Architecture Details - extractive body cue:** Goals In the image experiments, only the output of the visual embedder is treated as goal state, i.e. not the proprioceptive state.
- **p. 2 / 1 Introduction - extractive body cue:** (b) Inference: the policy is conditioned on the current state, the goal state (specified by the user) and a latent plan which is sampled once ...
- **p. 11 / A.1 Theoretical Motivation - extractive body cue:** The learned conditional prior becomes a "plan proposal" network mapping from current and goal state to a distribution over high level latent plans connecting them. ...
- **p. 11 / A.1 Theoretical Motivation - extractive body cue:** [34]): log pθ(x/c) ≥-KL  qφ(z/x, c) // pθ(z/c)  + Eqφ(z/x,c) [log pθ(x/z, c)] (6) We note that this model implies a formal conditional generative ...
- **p. 17 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** Our state models were trained on a smaller dataset, up to 180 minutes of play (see Fig 8). "Random": we collected a random exploration dataset ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value was not selected from the PDF body. | We allow the agent to "replan" by inferring and sampling new latent plans every κ timesteps (matching the average planning horizon it ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | We compute the action reconstruction cost as follows: For each timestep t in the input sequence τ, we feed in st ← ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | Shaded regions indicate 95% confidence intervals over 20 rollouts. | hardware, batch and throughput |

## Training vs Inference

- **p. 17 / A.4.3 Coverage Analysis of Interaction Space - extractive body cue:** Our state models were trained on a smaller dataset, up to 180 minutes of play (see Fig 8). "Random": we collected a random exploration dataset ...
- **p. 7 / 4 Experiments - extractive body cue:** Success is reported with confidence intervals over 3 seeded training runs for pixel experiments.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Action, space, DOF, agent, state, consists, cartesian, coordinates, position, effector, Euler, angles, representing, orientation, gripper, layers, sizes, depths, different, sub-networks.
- **Relevant PDF headings:** A.2 Architecture Details (p. 12).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | To compare our play-supervised models to a conventional scenario, we collect a training set of 100 expert demonstrations per task in the ... | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Policy fitting | (a) Play-LMP consistently outperforms the baselines, whether trained on groundtruth states or directly on pixels. | p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Closed-loop rollout | 3) Does decoupling latent plan inference and plan decoding into independent problems, as is done in Play-LMP, improve performance over goal-conditioned Behavioral ... | p. 7 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive body cue:** These data ablation numbers were obtained from models trained on ground truth state observations.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 14: Naturally emerging retrying behavior: example run of Play-LMP policy on "close sliding" task (sliding door left to right). The policy is aiming the ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 13: Naturally emerging retrying behavior: example run of Play-LMP policy on "grasp upright" task (grasping an object in upright position). The agent fails initially, ...
- **p. 17 / A.5 Limitations - extractive body cue:** The question of out-of-distribution generalization-say, playing in the living room and generalizing to the kitchen-is left to future work.
- **p. 8 / 4 Experiments - extractive body cue:** Emergent Retrying: We find qualitative evidence that play-supervised models, unlike models trained solely on expert demonstrations, make multiple attempts to retry the task after initial ...
- **p. 8 / 5 Conclusion - extractive body cue:** Future work includes exploring whether generalization is possible to novel objects or novel environments, as well as exploring the effects of imbalance in play data ...
- **p. 17 / A.5 Limitations - extractive body cue:** We hope to explore this in future work.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 12 (A.2 Architecture Details), p. 12 (A.2 Architecture Details), p. 17 (A.4.3 Coverage Analysis of Interaction Space), p. 15 (A.3.4 Training Data), p. 15 (A.3.4 Training Data), p. 16 (A.4.3 Coverage Analysis of Interaction Space), objective p. 15 (A.3.4 Training Data), temporal p. 6 (2 Related Work), p. 6 (2 Related Work), p. 8 (4 Experiments), p. 5 (2 Related Work), p. 5 (2 Related Work), p. 11 (A.1 Theoretical Motivation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Algorithm 2 Training Play-LMP 1: Input: Play data D : {(s1, a1), · · · , (sT , aT )} 2: Randomly initialize model parameters θ = {θV , θCG, ... (p. 12, A.1 Theoretical Motivation).
- **Objective/update evidence:** An updated version of the Mujoco HAPTIX system is used to collect teleoperation demonstration data [39]. (p. 15, A.3.4 Training Data).
- **Temporal/runtime evidence:** We can sidestep this issue by turning to stochastic gradient variational Bayes (SGVB) (Kingma and Welling [33]) framework, which optimizes a surrogate objective function: the variational lower bound of the ... (p. 11, A.1 Theoretical Motivation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
