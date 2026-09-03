# Method - OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2509.26633; PDF retrieval source: https://arxiv.org/pdf/2509.26633. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 1 (I. INTRODUCTION)): To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, ...

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This challenge is further amplified on humanoids, whose high-dimensional action spaces and complex dynamics make learning natural, expressive behaviors from scratch both difficult and inefficient.
- **p. 1 / Abstract - extractive body cue:** By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OMNIRETARGET generates kinematically feasible trajectories.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While deep reinforcement learning (RL) has shown remarkable success in robot control, efficient exploration is highly sensitive to reward engineering [3].
- **p. 1 / Body text (section not recovered) - extractive body cue:** Thanks to the high-quality interaction-preserving motion retargeting, these policies are trained and deployed in a minimal and unified way: it involves only 5 rewards, 4 ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, imitating human motions offers a powerful alternative for learning whole-body control, especially for complex scene interactions.

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and ...
- **p. 1 / Abstract - extractive body cue:** Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations.

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This challenge is further amplified on humanoids, whose high-dimensional action spaces and complex dynamics make learning natural, expressive behaviors from scratch both difficult and inefficient.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the ... | p. 1 (Abstract), p. 1 (I. INTRODUCTION) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | This challenge is further amplified on humanoids, whose high-dimensional action spaces and complex dynamics make learning natural, expressive behaviors from scratch both ... | p. 1 (I. INTRODUCTION) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | To address this, we introduce OMNIRETARGET, an interactionpreserving data generation engine based on an interaction mesh that explicitly models and preserves the ... | p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OMNIRETARGET generates kinematically feasible trajectories.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While deep reinforcement learning (RL) has shown remarkable success in robot control, efficient exploration is highly sensitive to reward engineering [3].
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 1 (Abstract), p. 1 (Abstract).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Thanks, high-quality, interaction-preserving, motion, retargeting, policies, trained, deployed, minimal, unified, involves, only, rewards, robot | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Thanks, high-quality, interaction-preserving, motion, retargeting, policies, trained, deployed, minimal, unified | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | address, introduce, OMNIRETARGET, interactionpreserving, data, generation, engine, interaction, mesh, explicitly | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | minimizing, Laplacian, deformation, between, human, robot, meshes, while, enforcing, kinematic | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Body text (section not recovered) - extractive body cue:** Thanks to the high-quality interaction-preserving motion retargeting, these policies are trained and deployed in a minimal and unified way: it involves only 5 rewards, 4 ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, imitating human motions offers a powerful alternative for learning whole-body control, especially for complex scene interactions.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | 1: OMNIRETARGET enables reinforcement learning policies to learn complex, long-horizon loco-manipulation skills in challenging environments that transfer zero-shot from simulation to a ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | Such high-quality data enables proprioceptive RL policies to successfully execute longhorizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** All code, retargeted datasets, and trained policies will be publicly released.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, introduce, OMNIRETARGET, interactionpreserving, data, generation, engine, interaction, mesh, explicitly, models, preserves, crucial, spatial, contact, relationships, between, agent, terrain, manipulated.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | The quest to enable humanoid robots to perform complex whole-body scene- and object-interaction tasks has long been constrained by a fundamental data ... | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Balance-aware whole-body execution | Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, ... | p. 7 (Figure/Table caption), p. 1 (Abstract) |
| Recovery / adaptation | Fig. 7: Artifacts resulting from the retargeting baselines. trained on our augmented data instead yield reliable success (see video for comparison). Admittedly, ... | p. 7 (Figure/Table caption), p. 12 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: OMNIRETARGET overview. Human demonstrations are retargeted to the robot via interaction-mesh-based constrained optimization. Each spatial and shape augmentation is solved as a new ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 10: Histograms from the downstream RL evaluation showing the failure patterns for the baselines in different tasks. VideoMimic, which fails systematically due to poor ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Cross-embodiment robot-object-terrain interaction. Drake [52], which correctly handles the differential geometry of rotations on the S3 manifold [53]. Our interaction-mesh-based kinematic pipeline is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Additional hardware results showing diverse, agile and human-like behaviors. • Observation noise: ±0.05 for orientation in Rot6D, ±0.5 m/s and ±0.2 rad/s for ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 1 (I. INTRODUCTION), objective p. 1 (Abstract), p. 1 (I. INTRODUCTION), temporal p. 1 (Body text (section not recovered)), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
