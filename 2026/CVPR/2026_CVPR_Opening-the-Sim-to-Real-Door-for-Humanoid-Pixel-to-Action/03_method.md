# Method - Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (1. Introduction), p. 3 (1. Introduction), p. 6 (2.4. Massive-Scale Simulation Randomization), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 5 (2.3. RL Finetuning for Partial Observability), p. 4 (2.3. RL Finetuning for Partial Observability)): To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure RGB perception. • We introduce ...

## Method Body Digest

- **p. 3 / 1. Introduction - extractive PDF cue:** To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure ...
- **p. 3 / 1. Introduction - extractive PDF cue:** To improve training efficiency, we introduce an exploration scheme that resets environments from late-stage snapshots, leveraging the recoverability of the simulator.
- **p. 6 / 2.4. Massive-Scale Simulation Randomization - extractive PDF cue:** To balance rendering quality and performance while training an RL policy in parallel, we use the RTX Real-Time renderer in performance mode, with post-processing effects ...
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive PDF cue:** To address this, we introduce a staged reset law α = (α1, . . . , αK), K X y=1 αy = 1, (1) which ...
- **p. 5 / 2.3. RL Finetuning for Partial Observability - extractive PDF cue:** It is worth mentioning that during fine-tuning, we use mainly a binary task success signal, plus simple shaping reward terms such as joint velocity, joint ...
- **p. 4 / 2.3. RL Finetuning for Partial Observability - extractive PDF cue:** Standard behavioral cloning loss alone may not yield optimal performance when the student observation space omits key features due to occlusion.
- **p. 1 / Abstract - extractive PDF cue:** Our approach introduces a staged-reset exploration strategy that stabilizes long-horizon privileged-policy training, and a GRPO-based fine-tuning procedure designed to mitigate partial observability and improve closed-loop ...
- **p. 4 / 2.1. Visual RL and Teacher-Student Distillation - extractive PDF cue:** We train the teacher policy using standard proximal policy optimization (PPO) [35], with the exact reward shaping recipe available in Appendix ??.

## Design Rationale

- **p. 3 / 1. Introduction - extractive PDF cue:** To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure ...
- **p. 3 / 1. Introduction - extractive PDF cue:** To address the first challenge, we introduce a novel, scalable teacher-student-bootstrap learning pipeline.
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive PDF cue:** Here, we present the design of a robust teacher training pipeline for whole-body loco-manipulation tasks.

## Source Evidence Cues

- **p. 3 / 1. Introduction - extractive PDF cue:** To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure ...
- **p. 3 / 1. Introduction - extractive PDF cue:** To improve training efficiency, we introduce an exploration scheme that resets environments from late-stage snapshots, leveraging the recoverability of the simulator.
- **p. 6 / 2.4. Massive-Scale Simulation Randomization - extractive PDF cue:** To balance rendering quality and performance while training an RL policy in parallel, we use the RTX Real-Time renderer in performance mode, with post-processing effects ...
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive PDF cue:** To address this, we introduce a staged reset law α = (α1, . . . , αK), K X y=1 αy = 1, (1) which ...
- **p. 5 / 2.3. RL Finetuning for Partial Observability - extractive PDF cue:** It is worth mentioning that during fine-tuning, we use mainly a binary task success signal, plus simple shaping reward terms such as joint velocity, joint ...
- **p. 4 / 2.3. RL Finetuning for Partial Observability - extractive PDF cue:** Standard behavioral cloning loss alone may not yield optimal performance when the student observation space omits key features due to occlusion.
- **p. 1 / Abstract - extractive PDF cue:** Our approach introduces a staged-reset exploration strategy that stabilizes long-horizon privileged-policy training, and a GRPO-based fine-tuning procedure designed to mitigate partial observability and improve closed-loop ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated ... | p. 3 (1. Introduction), p. 3 (1. Introduction) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | To improve training efficiency, we introduce an exploration scheme that resets environments from late-stage snapshots, leveraging the recoverability of the simulator. | p. 3 (1. Introduction), p. 6 (2.4. Massive-Scale Simulation Randomization) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | To balance rendering quality and performance while training an RL policy in parallel, we use the RTX Real-Time renderer in performance mode, ... | p. 6 (2.4. Massive-Scale Simulation Randomization), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 2.1. Visual RL and Teacher-Student Distillation - extractive PDF cue:** We train the teacher policy using standard proximal policy optimization (PPO) [35], with the exact reward shaping recipe available in Appendix ??.
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive PDF cue:** This shows that the staged-reset scheme reweighs the occupancy measure towards later-stage regions, increasing the frequency and effective magnitude of gradient updates for those states.
- **p. 5 / 2.3. RL Finetuning for Partial Observability - extractive PDF cue:** It is worth mentioning that during fine-tuning, we use mainly a binary task success signal, plus simple shaping reward terms such as joint velocity, joint ...
- **p. 3 / 1. Introduction - extractive PDF cue:** First, a teacher with privileged states (e.g., door pose and articulation state) is trained via reinforcement learning (RL) with stage-conditioned rewards.
- **p. 3 / 1. Introduction - extractive PDF cue:** Phase 1 Teacher RL Phase 2 Student Distillation Phase 3 Student Bootstrapping Isaac Lab Environment Privileged Observation Teacher Policy PPO Student Policy DAgger Student Policy ...
- **p. 5 / 2.3. RL Finetuning for Partial Observability - extractive PDF cue:** We define normalized group-relative advantages ˆAi = Ri -mean(R) std(R) , (4) and update πS using the clipped PPO surrogate: LGRPO(θ) = E i,t h ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 4 (2.3. RL Finetuning for Partial Observability), p. 5 (2.3. RL Finetuning for Partial Observability).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | While, student, policy, access, non-privileged, proprioception, information, joint, angles, velocities, root, angular, perception, task | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | While, student, policy, access, non-privileged, proprioception, information, joint, angles, velocities | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | summarize, main, contributions, present, first, end-to-end, humanoid, sim-to-real, policy, capable | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | train, teacher, policy, standard, proximal, optimization, PPO, exact, reward, shaping | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 2.1. Visual RL and Teacher-Student Distillation - extractive PDF cue:** While the student policy has access to non-privileged proprioception information, such as joint angles q, joint velocities ˙q, and root angular velocities ˙ω ∈R3, its ...
- **p. 3 / 2.1. Visual RL and Teacher-Student Distillation - extractive PDF cue:** In humanoid wholebody control literature, the policy is responsible for outputting target joint positions, which, in the case of a Unitree G1 robot, includes 29 ...
- **p. 3 / 2.1. Visual RL and Teacher-Student Distillation - extractive PDF cue:** Consider a partially observable Markov decision process (POMDP) P = (S, A, O, T, R, O, γ, ρ0), where S is the state space, A ...
- **p. 4 / 2.3. RL Finetuning for Partial Observability - extractive PDF cue:** In teacher-student policy distillation, a student policy πS(a/o) receives only partial observations ot ∈O, while the teacher policy πT (a/s) has access to privileged observations.
- **p. 5 / 2.3. RL Finetuning for Partial Observability - extractive PDF cue:** It is worth mentioning that during fine-tuning, we use mainly a binary task success signal, plus simple shaping reward terms such as joint velocity, joint ...
- **p. 1 / Abstract - extractive PDF cue:** Building on these advances, we develop a teacher-student-bootstrap learning framework for visionbased humanoid loco-manipulation, using articulatedobject interaction as a representative high-difficulty benchmark.
- **p. 1 / 1. Introduction - extractive PDF cue:** Seemingly simple household interactions, such as pulling a drawer, twisting a knob, or unlatching a gate, all require precise perception-action This CVPR paper is the ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Success rate and completion time are evaluated at when the robot traverses through the door and reaches a point 1 m beyond ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | (pull lever): requiring skillful manipulation in constrained space and long-horizon behavior. • Push-bar handle, opening into the direction of travel (push bar): ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | The policy also needs to be inferenced consistently at 50 Hz, which requires efficient neural network architectures. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 1. Introduction - extractive PDF cue:** To summarize, the main contributions of our work are: • We present the first end-to-end humanoid sim-to-real policy capable of diverse articulated loco-manipulation from pure ...
- **p. 3 / 1. Introduction - extractive PDF cue:** To improve training efficiency, we introduce an exploration scheme that resets environments from late-stage snapshots, leveraging the recoverability of the simulator.
- **p. 6 / 2.4. Massive-Scale Simulation Randomization - extractive PDF cue:** To balance rendering quality and performance while training an RL policy in parallel, we use the RTX Real-Time renderer in performance mode, with post-processing effects ...
- **p. 4 / 2.2. Multi-Stage Whole-Body Loco-Manipulation - extractive PDF cue:** To address this, we introduce a staged reset law α = (α1, . . . , αK), K X y=1 αy = 1, (1) which ...
- **p. 5 / 2.3. RL Finetuning for Partial Observability - extractive PDF cue:** It is worth mentioning that during fine-tuning, we use mainly a binary task success signal, plus simple shaping reward terms such as joint velocity, joint ...
- **p. 1 / Abstract - extractive PDF cue:** Our approach introduces a staged-reset exploration strategy that stabilizes long-horizon privileged-policy training, and a GRPO-based fine-tuning procedure designed to mitigate partial observability and improve closed-loop ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** summarize, main, contributions, present, first, end-to-end, humanoid, sim-to-real, policy, capable, diverse, articulated, loco-manipulation, pure, RGB, perception, introduce, teacher-student-bootstrap, pipeline, whole-body.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | Real-world visuals are unseen during training. | p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 6 (3. Experiment) |
| Balance-aware whole-body execution | In this section, we will establish real-world comparison with human baselines. | p. 6 (3. Experiment), p. 6 (3.1. Surpassing Human-Teleop Baseline) |
| Recovery / adaptation | Figure 7. Training progress of student policy bootstrapping with improvements in task success rate. The dashed lines are teacher policy success rates. ... | p. 7 (Figure/Table caption), p. 7 (3.2. Effect of Photorealistic Visual Randomization) |

## Failure and Ablation Link

- **p. 7 / 3.4. Effect of Staged Reset Exploration - extractive PDF cue:** Finally, we run ablation study to investigate the effect of staged reset exploration on the stability of teacher training.
- **p. 7 / 3.2. Effect of Photorealistic Visual Randomization - extractive PDF cue:** We design an ablation study on the visual diversity during training, starting with no visual randomization, where objects are coated in a default gray reflective ...
- **p. 6 / 3. Experiment - extractive PDF cue:** We will also investigate the effect of varies components in our pipeline, including visual randomization, staged reset, and fine-tuning.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Procedurally generated doors used to train DoorMan, covering panel designs, latching mechanisms, lighting, materials, etc. Each parallelized environment is trained on a unique ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 8. Teacher training progress with different reset buffer sizes of 0, 10 and 100. reset buffer, as the policy finds it difficult to enter ...
- **p. 7 / 3.4. Effect of Staged Reset Exploration - extractive PDF cue:** The exploration fails when not using the 6648
- **p. 8 / 5. Conclusion - extractive PDF cue:** Trained entirely in photorealistic simulation, the resulting policy achieves robust zero-shot performance on articulated-object interaction tasks, including diverse door configurations, and exceeds human teleoperation baselines ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (1. Introduction), p. 3 (1. Introduction), p. 6 (2.4. Massive-Scale Simulation Randomization), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 5 (2.3. RL Finetuning for Partial Observability), p. 4 (2.3. RL Finetuning for Partial Observability), objective p. 4 (2.1. Visual RL and Teacher-Student Distillation), p. 4 (2.2. Multi-Stage Whole-Body Loco-Manipulation), p. 5 (2.3. RL Finetuning for Partial Observability), p. 3 (1. Introduction), p. 3 (1. Introduction), p. 5 (2.3. RL Finetuning for Partial Observability), temporal p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 6 (3.1. Surpassing Human-Teleop Baseline), p. 7 (3.2. Effect of Photorealistic Visual Randomization), p. 1 (Abstract), p. 1 (Abstract), p. 3 (2.1. Visual RL and Teacher-Student Distillation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
