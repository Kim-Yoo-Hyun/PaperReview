# Method - Learning Humanoid Standing-up Control across Diverse Postures

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p064.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p064.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details)): Our PPO implementation follows the framework outlined in [39]. ‘The actor network consists of 4 3-layer MLP with hidden dimensions [512, 256, 128], while each critic network is a 2-layer ...

## Method Body Digest

- **p. 12 / B. More Implementation Details - extractive PDF cue:** Our PPO implementation follows the framework outlined in [39]. ‘The actor network consists of 4 3-layer MLP with hidden dimensions [512, 256, 128], while each ...
- **p. 13 / B. More Implementation Details - extractive PDF cue:** postures, PD controllers, observation and action spaces.
- **p. 12 / B. More Implementation Details - extractive PDF cue:** The lower bounds for the vertical force and action bound are ON and 0.25, respectively.
- **p. 13 / B. More Implementation Details - extractive PDF cue:** We make the following adjustment to work the algorithm: scale of pulling force, height for curriculum, height for stage
- **p. 13 / B. More Implementation Details - extractive PDF cue:** We make the following adjustment to work the algorithm: more strict constraints on hip joint deviation rewards, weights for reward groups, and additional thigh orientation ...
- **p. 12 / B. More Implementation Details - extractive PDF cue:** The mul critic architecture is based on previous work [33]. where each advantage function is independently calculated and normalized within its corresponding reward group.
- **p. 12 / B. More Implementation Details - extractive PDF cue:** We present the complete set of ward functions and their detailed descriptions in Tulble V1 Several regularization reward terms are adapted from prior work [21, ...
- **p. 13 / B. More Implementation Details - extractive PDF cue:** Reward functions within the same group are independently normalized, Whose assovited advantaged functions are eaimated via disinet criti.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To enable postureadaptive motion beyond the ground, we introduce multiple terrains for training and a vertical pull force during the initial stages to facilitate exploration, ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** We overview the real-world performance of our controllers in Fg. / and summarize our core contributions as follows:
- **p. 12 / B. More Implementation Details - extractive PDF cue:** Our PPO implementation follows the framework outlined in [39]. ‘The actor network consists of 4 3-layer MLP with hidden dimensions [512, 256, 128], while each ...

## Source Evidence Cues

- **p. 12 / B. More Implementation Details - extractive PDF cue:** Our PPO implementation follows the framework outlined in [39]. ‘The actor network consists of 4 3-layer MLP with hidden dimensions [512, 256, 128], while each ...
- **p. 13 / B. More Implementation Details - extractive PDF cue:** postures, PD controllers, observation and action spaces.
- **p. 12 / B. More Implementation Details - extractive PDF cue:** The lower bounds for the vertical force and action bound are ON and 0.25, respectively.
- **p. 13 / B. More Implementation Details - extractive PDF cue:** We make the following adjustment to work the algorithm: scale of pulling force, height for curriculum, height for stage
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | Our PPO implementation follows the framework outlined in [39]. ‘The actor network consists of 4 3-layer MLP with hidden dimensions [512, 256, ... | p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | postures, PD controllers, observation and action spaces. | p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | The lower bounds for the vertical force and action bound are ON and 0.25, respectively. | p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 13 / B. More Implementation Details - extractive PDF cue:** We make the following adjustment to work the algorithm: more strict constraints on hip joint deviation rewards, weights for reward groups, and additional thigh orientation ...
- **p. 12 / B. More Implementation Details - extractive PDF cue:** The mul critic architecture is based on previous work [33]. where each advantage function is independently calculated and normalized within its corresponding reward group.
- **p. 12 / B. More Implementation Details - extractive PDF cue:** We present the complete set of ward functions and their detailed descriptions in Tulble V1 Several regularization reward terms are adapted from prior work [21, ...
- **p. 13 / B. More Implementation Details - extractive PDF cue:** Reward functions within the same group are independently normalized, Whose assovited advantaged functions are eaimated via disinet criti.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 13 (B. More Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | postures, controllers, observation, action, spaces, lower, bounds, vertical, force, bound, respectively, Curriculum, Setup, adjustment | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | postures, controllers, observation, action, spaces, lower, bounds, vertical, force, bound | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | enable, postureadaptive, motion, beyond, ground, introduce, multiple, terrains, training, vertical | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | make, following, adjustment, algorithm, more, strict, constraints, joint, deviation, rewards | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 13 / B. More Implementation Details - extractive PDF cue:** postures, PD controllers, observation and action spaces.
- **p. 12 / B. More Implementation Details - extractive PDF cue:** The lower bounds for the vertical force and action bound are ON and 0.25, respectively.
- **p. 12 / B. More Implementation Details - extractive PDF cue:** Curriculum Setup. ‘The curriculum adjustment condition is consistent for both the vertical force and action bound: the head height /jeaa must reach a target height ...
- **p. 13 / B. More Implementation Details - extractive PDF cue:** Observation noises are without curriculum, set as below:
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** + Real-world posture-adaptive motions are well achieved through our proposed RL-based method, without relying on predefined trajectories or sim-to-real adaptation techniques.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Reinforcement learning (RL) offers an alternative effective framework for humanoid locomotion and whole-body control [36, 13, 4 54], benefiting from minimal modeling assumptions.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Each episode has a rollout length of 500 steps. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | Lastly, HOSTHistory modifies the history length of states while keeping other implementations unchanged, | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | Lastly, HOSTHistory modifies the history length of states while keeping other implementations unchanged, | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | Each episode has a rollout length of 500 steps. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** PPO, implementation, follows, framework, outlined, actor, network, consists, layer, MLP, hidden, dimensions, while, critic, postures, controllers, observation, action, spaces, lower.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | this conclusion, with our approach achieving a 100% success rate and high motion smoothness across all scenes.' Generalization to outdoor environments (Viz. | p. 8 (A. Main Results), p. 9 (B. Sim-to-real Analysis) |
| Balance-aware whole-body execution | HOST with short history length underperforms in contact-rich scenarios, such as the Wall terrain, In contrast, a longer history length improves performance, ... | p. 6 (B. Main Results), p. 8 (A. Main Results) |
| Recovery / adaptation | key design choices is summarized as follows: Multiple critics are crucial for learning motor skills Using the same reward functions, the performance ... | p. 6 (B. Main Results), p. 6 (B. Main Results) |

## Failure and Ablation Link

- **p. 8 / B. Sim-to-real Analysis - extractive PDF cue:** ‘We select the successful episode to compute smocthaess to reflect the effect of L2C2 regularization tier.
- **p. 8 / B. Sim-to-real Analysis - extractive PDF cue:** In this analysis, we investigate the effect of various domain randomization terms on the sim-to-real gap, as shown in Fig.
- **p. 6 / B. Main Results - extractive PDF cue:** While the robot can learn to stand up without action bounds (HOST-w/o-Bound), its movements are excessively violent, as indicated by three performance metrics.
- **p. 6 / B. Main Results - extractive PDF cue:** Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as the other terrains require exploration from a ...
- **p. 12 / B. More Implementation Details - extractive PDF cue:** are handcrafted without collision models.
- **p. 12 / B. More Implementation Details - extractive PDF cue:** HOST-Bound0.25 uses a fixed action bound of $ ~ 0.25 without a curriculum, HOST-wip-r*"* eliminates all style-telated reward functions.
- **p. 13 / B. More Implementation Details - extractive PDF cue:** Observation noises are without curriculum, set as below:

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details), objective p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details), temporal p. 5 (C. Force Curriculum as Exploration Strategy), p. 12 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 3 (C. Learning Quadrupedal Robot Standing-up Control), p. 3 (C. Learning Quadrupedal Robot Standing-up Control), p. 5 (C. Force Curriculum as Exploration Strategy).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
