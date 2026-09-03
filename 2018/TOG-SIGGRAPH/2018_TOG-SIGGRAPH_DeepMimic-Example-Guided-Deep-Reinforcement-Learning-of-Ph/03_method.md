# Method - DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1804.02717; PDF retrieval source: https://arxiv.org/pdf/1804.02717. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (4 BACKGROUND), p. 4 (4 BACKGROUND), p. 4 (4 BACKGROUND), p. 3 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 5 (4 BACKGROUND)): Property Humanoid Atlas T-Rex Dragon Links 13 12 20 32 Total Mass (kg) 45 169.8 54.5 72.5 Height (m) 1.62 1.82 1.66 1.83 Degrees of Freedom 34 31 55 79 ...

## Method Body Digest

- **p. 6 / 4 BACKGROUND - extractive body cue:** Property Humanoid Atlas T-Rex Dragon Links 13 12 20 32 Total Mass (kg) 45 169.8 54.5 72.5 Height (m) 1.62 1.82 1.66 1.83 Degrees of ...
- **p. 4 / 4 BACKGROUND - extractive body cue:** The action distribution is modeled as a Gaussian, with a state dependent mean µ(s) specified by the network, and a fixed diagonal covariance matrix Σ ...
- **p. 4 / 4 BACKGROUND - extractive body cue:** The resulting features are then concatenated with the input state s and goal д, and processed by a similar fully-connected network as the one used ...
- **p. 3 / 4 BACKGROUND - extractive body cue:** A policy π(a/s) models the conditional distribution over action a ∈A given a state s ∈S.
- **p. 5 / 4 BACKGROUND - extractive body cue:** With this design, the policy must learn the motion in a sequential manner, by first learning the early phases of the motion, and then incrementally ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** Training proceeds episodically, where at the start of each episode, an initial state s0 is sampled uniformly from the reference motion (section 6.1), and rollouts ...
- **p. 8 / 4 BACKGROUND - extractive body cue:** The memory state h can be removed by training a recurrent policy, but our simple solution avoids the complexities of training recurrent networks while still ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** The policy is updated using gradients computed from the surrogate objective, with advantages At computed using GAE(λ) [Schulman et al.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Although our framework consists of individual components that have been known for some time, the particular combination of these components in the context of data-driven ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In our ablation studies, we identify two specific components of our method, reference state initialization and early termination, that are critical for achieving highly dynamic ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Our method handles keyframed motions, highly-dynamic actions such as motion-captured flips and spins, and retargeted motions.

## Source Evidence Cues

- **p. 6 / 4 BACKGROUND - extractive body cue:** Property Humanoid Atlas T-Rex Dragon Links 13 12 20 32 Total Mass (kg) 45 169.8 54.5 72.5 Height (m) 1.62 1.82 1.66 1.83 Degrees of ...
- **p. 4 / 4 BACKGROUND - extractive body cue:** The action distribution is modeled as a Gaussian, with a state dependent mean µ(s) specified by the network, and a fixed diagonal covariance matrix Σ ...
- **p. 4 / 4 BACKGROUND - extractive body cue:** The resulting features are then concatenated with the input state s and goal д, and processed by a similar fully-connected network as the one used ...
- **p. 3 / 4 BACKGROUND - extractive body cue:** A policy π(a/s) models the conditional distribution over action a ∈A given a state s ∈S.
- **p. 5 / 4 BACKGROUND - extractive body cue:** With this design, the policy must learn the motion in a sequential manner, by first learning the early phases of the motion, and then incrementally ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** Training proceeds episodically, where at the start of each episode, an initial state s0 is sampled uniformly from the reference motion (section 6.1), and rollouts ...
- **p. 8 / 4 BACKGROUND - extractive body cue:** The memory state h can be removed by training a recurrent policy, but our simple solution avoids the complexities of training recurrent networks while still ...
- **Detected method headings:** B OFF-POLICY LEARNING (p. 15); C PROXIMAL POLICY OPTIMIZATION (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | Property Humanoid Atlas T-Rex Dragon Links 13 12 20 32 Total Mass (kg) 45 169.8 54.5 72.5 Height (m) 1.62 1.82 1.66 ... | p. 6 (4 BACKGROUND), p. 4 (4 BACKGROUND) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | The action distribution is modeled as a Gaussian, with a state dependent mean µ(s) specified by the network, and a fixed diagonal ... | p. 4 (4 BACKGROUND), p. 4 (4 BACKGROUND) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | The resulting features are then concatenated with the input state s and goal д, and processed by a similar fully-connected network as ... | p. 4 (4 BACKGROUND), p. 3 (4 BACKGROUND) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4 BACKGROUND - extractive body cue:** The policy is updated using gradients computed from the surrogate objective, with advantages At computed using GAE(λ) [Schulman et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we take a simple approach to this problem by directly rewarding the learned controller for producing motions that resemble reference animation data, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We also demonstrate three methods for constructing controllers from multiple clips: training with a multi-clip reward based on a max operator; training a policy to ...
- **p. 3 / 4 BACKGROUND - extractive body cue:** Our tasks will be structured as standard reinforcement learning problems, where an agent interacts with an environment according to a policy in order to maximize ...
- **p. 6 / 4 BACKGROUND - extractive body cue:** Multi-Clip Reward: To utilize multiple reference motion clips during training, we define a composite imitation objective calculated simply as the max over the previously introduced ...
- **p. 4 / 4 BACKGROUND - extractive body cue:** The policy gradient can therefore be interpreted as increasing the likelihood of actions that lead to higher than expected returns, while decreasing the likelihood of ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 5 (4 BACKGROUND), p. 6 (4 BACKGROUND), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1 INTRODUCTION), p. 4 (4 BACKGROUND), p. 4 (4 BACKGROUND).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Network, policy, represented, neural, maps, given, state, goal, distribution, over, action, Training, proceeds, episodically | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Network, policy, represented, neural, maps, given, state, goal, distribution, over | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | Although, framework, consists, individual, components, have, been, known, some, time | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | policy, updated, gradients, computed, surrogate, objective, advantages, GAE, Schulman, take | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4 BACKGROUND - extractive body cue:** 5.2 Network Each policy π is represented by a neural network that maps a given state s and goal д to a distribution over action ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** Training proceeds episodically, where at the start of each episode, an initial state s0 is sampled uniformly from the reference motion (section 6.1), and rollouts ...
- **p. 3 / 4 BACKGROUND - extractive body cue:** For a parametric policy πθ (a/s), the goal of the agent is to learn the optimal parameters θ∗that maximizes its expected return J(θ) = Eτ ...
- **p. 4 / 4 BACKGROUND - extractive body cue:** The resulting features are concatenated with the input state s and goal д and processed by by two fully-connected layer with 1024 and 512 units.
- **p. 8 / 4 BACKGROUND - extractive body cue:** The target direction is provided as the input goal дt = d∗ t to the policy.
- **p. 3 / 4 BACKGROUND - extractive body cue:** At each control timestep, the agent observes the current state st and samples an action at from π.
- **p. 5 / 4 BACKGROUND - extractive body cue:** The policy only receives reward retrospectively, once it has visited a state.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Training proceeds episodically, where at the start of each episode, an initial state s0 is sampled uniformly from the reference motion (section ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | We demonstrate that a single model-free framework is capable of a wider range of motion skills (from walks to highly dynamic kicks ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4 BACKGROUND - extractive body cue:** Property Humanoid Atlas T-Rex Dragon Links 13 12 20 32 Total Mass (kg) 45 169.8 54.5 72.5 Height (m) 1.62 1.82 1.66 1.83 Degrees of ...
- **p. 5 / 4 BACKGROUND - extractive body cue:** Training proceeds episodically, where at the start of each episode, an initial state s0 is sampled uniformly from the reference motion (section 6.1), and rollouts ...
- **p. 8 / 4 BACKGROUND - extractive body cue:** The memory state h can be removed by training a recurrent policy, but our simple solution avoids the complexities of training recurrent networks while still ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Property, Humanoid, Atlas, T-Rex, Dragon, Links, Total, Mass, Height, Degrees, Freedom, State, Features, Action, Parameters, Without, early, termination, data, collected.
- **Relevant PDF headings:** B OFF-POLICY LEARNING (p. 15); C PROXIMAL POLICY OPTIMIZATION (p. 15).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | Each environment is denoted by "Character: Skill - Task". | p. 10 (10 RESULTS), p. 10 (10 RESULTS) |
| Balance-aware whole-body execution | To investigate the extent to which the motions are adapted for a particular task, we compared the performance of policies trained to ... | p. 11 (10 RESULTS), p. 12 (10 RESULTS) |
| Recovery / adaptation | The performance achieved by the Atlas policies are comparable to those achieved by the humanoid. | p. 12 (10 RESULTS), p. 11 (10 RESULTS) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Performance statistics of imitating various skills. All skills are performed by the humanoid unless stated otherwise. Policies are trained only to imitate a ...
- **p. 10 / 10 RESULTS - extractive body cue:** The task is left unspecified for policies that are trained solely to imitate a reference motion without additional task objectives.
- **p. 11 / 10 RESULTS - extractive body cue:** Training without a reference motion produces policies that develop awkward, but functional, strategies for satisfying the task objectives.
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 8. Policy trained for the throw task without a reference motion. Instead of throwing the ball, the character learns to run towards the target.
- **p. 12 / 10 RESULTS - extractive body cue:** Learning curves for policies trained with and without reference state initialization (RSI) and early termination (ET).
- **p. 12 / 10 RESULTS - extractive body cue:** To retarget the motion clips, we simply copied the local joint rotations from the humanoid to the Atlas, without any further modification.
- **p. 12 / 10 RESULTS - extractive body cue:** When the character falls, the composite policy activates the appropriate getup policy without requiring any manual scripting, as shown in the supplemental video.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (4 BACKGROUND), p. 4 (4 BACKGROUND), p. 4 (4 BACKGROUND), p. 3 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 5 (4 BACKGROUND), objective p. 5 (4 BACKGROUND), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (4 BACKGROUND), p. 6 (4 BACKGROUND), p. 4 (4 BACKGROUND), temporal p. 5 (4 BACKGROUND), p. 2 (2 RELATED WORK), p. 3 (4 BACKGROUND), p. 4 (4 BACKGROUND), p. 5 (4 BACKGROUND), p. 6 (4 BACKGROUND).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Training proceeds episodically, where at the start of each episode, an initial state s0 is sampled uniformly from the reference motion (section 6.1), and rollouts are generated by sampling actions ... (p. 5, 4 BACKGROUND).
- **Objective/update evidence:** The policy is updated using gradients computed from the surrogate objective, with advantages At computed using GAE(λ) [Schulman et al. (p. 5, 4 BACKGROUND).
- **Temporal/runtime evidence:** Each episode is simulated to a fixed time horizon or until a termination condition has been triggered (section 6.2). (p. 5, 4 BACKGROUND).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
