# Method - BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p068.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p068.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (A. Locomotion on Sparse Footholds), p. 2 (1. INrRopucTION), p. 1 (Abstract), p. 1 (Abstract), p. 3 (A. Foothold Reward), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL)): Recent studies have explored combining RL. with modelbased controllers, such as using RL to generate trajectories that are then tracked by model-based controllers [15, 61, 55]e or employing RL policies ...

## Method Body Digest

- **p. 2 / A. Locomotion on Sparse Footholds - extractive PDF cue:** Recent studies have explored combining RL. with modelbased controllers, such as using RL to generate trajectories that are then tracked by model-based controllers [15, 61, ...
- **p. 2 / 1. INrRopucTION - extractive PDF cue:** We begin by defining a samplingbased foothold reward, designed to evaluate the foot placement ‘of a polygonal foot model. ‘To address the challenge of sparse ...
- **p. 1 / Abstract - extractive PDF cue:** dynamics by training the humanoid on flat terr providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on the actual task ...
- **p. 1 / Abstract - extractive PDF cue:** To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds.
- **p. 3 / A. Foothold Reward - extractive PDF cue:** To accommodate the polygonal foot model of the humanoid robot, we introduce a sampling-based foothold reward that evaluates foot placement on sparse footholds.This evaluation
- **p. 4 / C. Learning Terrain-Aware Locomotion via Two-Stage RL - extractive PDF cue:** To expose the robot to real terrain dynamics, we use the foothold reward (introduced in Section I-A).
- **p. 3 / B. Reinforcement Learning in Locomotion Control - extractive PDF cue:** This work aims to develop an terrain-aware humanoid locomotion policy, where controllers are trained via reinforcement learning (RL).
- **p. 3 / B. Reinforcement Learning in Locomotion Control - extractive PDF cue:** The primary objective is to optimize the policy x(as / s+) to maximize the discounted cumulative rewards:

## Design Rationale

- **p. 1 / Abstract - extractive PDF cue:** To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds.
- **p. 2 / 1. INrRopucTION - extractive PDF cue:** In this work, we introduce BEAMDOJO, a novel reinforcement learning-based framework for controlling humanoid robots traversing risky terrains with sparse footholds.
- **p. 2 / 1. INrRopucTION - extractive PDF cue:** + We propose BEAMDOIO, a two-stage RL framework that combines a newly designed foothold reward for the polygonal foot model and a double critic, enabling ...

## Source Evidence Cues

- **p. 2 / A. Locomotion on Sparse Footholds - extractive PDF cue:** Recent studies have explored combining RL. with modelbased controllers, such as using RL to generate trajectories that are then tracked by model-based controllers [15, 61, ...
- **p. 2 / 1. INrRopucTION - extractive PDF cue:** We begin by defining a samplingbased foothold reward, designed to evaluate the foot placement ‘of a polygonal foot model. ‘To address the challenge of sparse ...
- **p. 1 / Abstract - extractive PDF cue:** dynamics by training the humanoid on flat terr providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on the actual task ...
- **p. 1 / Abstract - extractive PDF cue:** To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds.
- **p. 3 / A. Foothold Reward - extractive PDF cue:** To accommodate the polygonal foot model of the humanoid robot, we introduce a sampling-based foothold reward that evaluates foot placement on sparse footholds.This evaluation
- **p. 4 / C. Learning Terrain-Aware Locomotion via Two-Stage RL - extractive PDF cue:** To expose the robot to real terrain dynamics, we use the foothold reward (introduced in Section I-A).
- **p. 3 / B. Reinforcement Learning in Locomotion Control - extractive PDF cue:** This work aims to develop an terrain-aware humanoid locomotion policy, where controllers are trained via reinforcement learning (RL).
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | Recent studies have explored combining RL. with modelbased controllers, such as using RL to generate trajectories that are then tracked by model-based ... | p. 2 (A. Locomotion on Sparse Footholds), p. 2 (1. INrRopucTION) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | We begin by defining a samplingbased foothold reward, designed to evaluate the foot placement ‘of a polygonal foot model. ‘To address the ... | p. 2 (1. INrRopucTION), p. 1 (Abstract) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | dynamics by training the humanoid on flat terr providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on ... | p. 1 (Abstract), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / B. Reinforcement Learning in Locomotion Control - extractive PDF cue:** The primary objective is to optimize the policy x(as / s+) to maximize the discounted cumulative rewards:
- **p. 3 / B. Double Critic for Sparse Reward Learning - extractive PDF cue:** Specifically, each value network V, is updated independently for its corresponding reward group , with temporal difference loss (TD-1os8):
- **p. 4 / B. Double Critic for Sparse Reward Learning - extractive PDF cue:** This overall advantage is then used to update the policy: f nin (a(O)Ae ‘clip(a4(8),1- 1 +o4e)). o where a,(8) is the probability ratio, and ¢ ...
- **p. 5 / C. Learning Terrain-Aware Locomotion via Two-Stage RL - extractive PDF cue:** ‘To maintain a smooth gait and accurate foot placements, we ‘continue leveraging the double-critic framework to optimize both locomotion rewards and the foothold reward rasta ...
- **p. 1 / Abstract - extractive PDF cue:** E approaches often struggle on such complex terrains due to sparse foothold rewards and inefficient learning processes.
- **p. 1 / Abstract - extractive PDF cue:** BEAMDOJO begins by introducing a sampling-based foothold reward tailored for polygonal feet, along with a double critic to balancing the learning process between dense locomotion ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 3 (B. Double Critic for Sparse Reward Learning), p. 2 (1. INrRopucTION), p. 2 (1. INrRopucTION), p. 3 (B. Reinforcement Learning in Locomotion Control), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Observation, Space, Action, policy, observations, denoted, consist, four, components, commands, specify, desired, velocity, represented | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Observation, Space, Action, policy, observations, denoted, consist, four, components, commands | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | address, challenges, introduce, BEAMDOJO, reinforcement, learning, framework, designed, enabling, agile | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | primary, objective, optimize, policy, maximize, discounted, cumulative, rewards, Specifically, value | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / C. Learning Terrain-Aware Locomotion via Two-Stage RL - extractive PDF cue:** 1) Observation Space and Action Space: ‘The policy observations, denoted a8 o,, consist of four components: 0 = [61 0f°"*, of", a ® ‘The commands ...
- **p. 4 / C. Learning Terrain-Aware Locomotion via Two-Stage RL - extractive PDF cue:** We let the humanoid robot traverse the terrain F, receiving proprioceptive observations, while providing perceptual feedback in the form of the elevation map of terrain ...
- **p. 1 / Abstract - extractive PDF cue:** dynamics by training the humanoid on flat terr providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on the actual task ...
- **p. 2 / 1. INrRopucTION - extractive PDF cue:** First, the reward signal for evaluating foot placement is sparse, typically provided only after completing a full sub-process (eg. lifting and landing a foot), which ...
- **p. 3 / B. Reinforcement Learning in Locomotion Control - extractive PDF cue:** The RL problem is formulated as a Markov Decision Process (MDP) M = (S,A,T,O,r,7). where S and A denote the state and action spaces, respectively.
- **p. 4 / B. Double Critic for Sparse Reward Learning - extractive PDF cue:** and the foothold reward are decoupled respectively, with the former obtained from flat terrain and the latter from task terain, The double critic modile separately ...
- **p. 5 / C. Learning Terrain-Aware Locomotion via Two-Stage RL - extractive PDF cue:** The action of lst timestep a¢-1 € Ris also included to provide temporal context. ‘The action a, € R'? represents the target joint positions for ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | + Vertical Measurement: Random vertical offsets are applied to the heights for an episode, along with uniformly sampled vertical noise added to ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | ‘+ Stepping Beams: ‘This terrain consists of a sequence ‘of beams to step on, randomly distributed along the longitudinal direction, with two ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive PDF cue:** dynamics by training the humanoid on flat terr providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on the actual task ...
- **p. 3 / B. Reinforcement Learning in Locomotion Control - extractive PDF cue:** This work aims to develop an terrain-aware humanoid locomotion policy, where controllers are trained via reinforcement learning (RL).
- **p. 2 / 1. INrRopucTION - extractive PDF cue:** BEAMDOJO further incorporates a two-stage approach to encourage fully trial-and-error exploration, In the first stage, terrain dynamics constraints are relaxed, allowing the humanoid robot to ...
- **p. 7 / B. Simulation Experiments - extractive PDF cue:** e123 5 7 0 ‘Training Steps (&) "= Naive + Ours wio Sot Dyn + Ours wio Double Critic ->- Ours

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Recent, studies, have, explored, combining, modelbased, controllers, generate, trajectories, then, tracked, model-based, employing, policies, track, generated, planners, begin, defining, samplingbased.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | 1) Hardware Setup: We use Unitree G1 humanoid robot for our experiments in this work. | p. 6 (evaluation), p. 7 (A. Experimental Setup) |
| Balance-aware whole-body execution | This requires a distinct gait compared to regular Jocomotion tasks. | p. 5 (evaluation), p. 6 (A. Experimental Setup) |
| Recovery / adaptation | 1) Quantitative results: We report the success rate (Race) and traverse rate (R,9y) for four terrains at medium and hard difficulty levels ... | p. 7 (B. Simulation Experiments), p. 7 (A. Experimental Setup) |

## Failure and Ablation Link

- **p. 8 / B. Simulation Experiments - extractive PDF cue:** Gait Regularization: The combination of small-scale gait regularization rewards with sparse foothold reward can hinder gait performance, as shown in Table Ill, where the naive ...
- **p. 6 / A. Experimental Setup - extractive PDF cue:** BL 3) Ours w/o Soft Dyn: This is an ablation which removing the first stage of training with soft terrain dynamics, constraints
- **p. 5 / evaluation - extractive PDF cue:** This terrain is challenging for the robot as it must learn to keep its feet together on the beams without colliding with each other, while ...
- **p. 6 / A. Experimental Setup - extractive PDF cue:** BL 4) Ours w/o Double Critie: This is an ablation which uses a single critic to handle both locomotion rewards and foothold reward, instead of ...
- **p. 7 / B. Simulation Experiments - extractive PDF cue:** 2) Detailed Ablation Analysis: We conduct additional ablation studies by comparing BEAMDO4O with BL.
- **p. 7 / B. Simulation Experiments - extractive PDF cue:** single-stage approaches and ablation designs, achieving, high success rates and low foothold errors across all ‘challenging terrains.
- **p. 8 / B. Simulation Experiments - extractive PDF cue:** In contrast, ‘our method and the ablation with double critic demonstrates superior motion smoothness and improved feet clearance.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (A. Locomotion on Sparse Footholds), p. 2 (1. INrRopucTION), p. 1 (Abstract), p. 1 (Abstract), p. 3 (A. Foothold Reward), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), objective p. 3 (B. Reinforcement Learning in Locomotion Control), p. 3 (B. Double Critic for Sparse Reward Learning), p. 4 (B. Double Critic for Sparse Reward Learning), p. 5 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 1 (Abstract), p. 1 (Abstract), temporal p. 6 (evaluation), p. 5 (evaluation), p. 6 (evaluation), p. 5 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 2 (1. INrRopucTION), p. 7 (B. Simulation Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
