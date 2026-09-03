# Method - SPIN: Simultaneous Perception, Interaction and Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (2. Method), p. 4 (2. Method), p. 3 (2. Method), p. 4 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth), p. 5 (2.2. Phase 2 - From Scandots to Depth)): This is followed by a phase-2 supervised training where this behavior is distilled into a student network that operates with ego-centric depth images (2) Decoupled Visuomotor Optimization (DVO) decouples the ...

## Method Body Digest

- **p. 3 / 2. Method - extractive body cue:** This is followed by a phase-2 supervised training where this behavior is distilled into a student network that operates with ego-centric depth images (2) Decoupled ...
- **p. 4 / 2. Method - extractive body cue:** Since the scandots are permutation invariant, we pass them through a trainable point-net architecture P to obtain compressed latent zt = P(˜st) that we pass ...
- **p. 3 / 2. Method - extractive body cue:** We propose two methods: (1) Coupled Visuomotor Optimization (CVO) learns robot and camera actions at the same time.
- **p. 4 / 2. Method - extractive body cue:** In particular, the policy gets proprioception xt and only visible scandots ˜st = F(st, xt) as observation and has to predict both the camera and ...
- **p. 5 / 2.2. Phase 2 - From Scandots to Depth - extractive body cue:** This latent is passed to a student policy π′ to predict the actions [˜arobot, ˜acam].
- **p. 5 / 2.2. Phase 2 - From Scandots to Depth - extractive body cue:** This is supervised using L2 loss from the phase 1 actions.
- **p. 4 / 2. Method - extractive body cue:** Rewards: For the navigation task, we use distance to goal reward ∥gt∥along with a forward progress reward / (vt)g / where (vt)g is velocity along ...
- **p. 4 / 2. Method - extractive body cue:** This is followed by a lift reward if a successful grasp is detected (based on whether contact forces cross a threshold). r_\ t ext r ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We find that our method outperforms classical methods and baselines which do not use active vision.
- **p. 3 / 2. Method - extractive body cue:** We propose two methods: (1) Coupled Visuomotor Optimization (CVO) learns robot and camera actions at the same time.
- **p. 4 / 2. Method - extractive body cue:** We present two approaches to tackle this problem.

## Source Evidence Cues

- **p. 3 / 2. Method - extractive body cue:** This is followed by a phase-2 supervised training where this behavior is distilled into a student network that operates with ego-centric depth images (2) Decoupled ...
- **p. 4 / 2. Method - extractive body cue:** Since the scandots are permutation invariant, we pass them through a trainable point-net architecture P to obtain compressed latent zt = P(˜st) that we pass ...
- **p. 3 / 2. Method - extractive body cue:** We propose two methods: (1) Coupled Visuomotor Optimization (CVO) learns robot and camera actions at the same time.
- **p. 4 / 2. Method - extractive body cue:** In particular, the policy gets proprioception xt and only visible scandots ˜st = F(st, xt) as observation and has to predict both the camera and ...
- **p. 5 / 2.2. Phase 2 - From Scandots to Depth - extractive body cue:** This latent is passed to a student policy π′ to predict the actions [˜arobot, ˜acam].
- **p. 5 / 2.2. Phase 2 - From Scandots to Depth - extractive body cue:** This is supervised using L2 loss from the phase 1 actions.
- **Detected method headings:** 2. Method (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | This is followed by a phase-2 supervised training where this behavior is distilled into a student network that operates with ego-centric depth ... | p. 3 (2. Method), p. 4 (2. Method) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | Since the scandots are permutation invariant, we pass them through a trainable point-net architecture P to obtain compressed latent zt = P(˜st) ... | p. 4 (2. Method), p. 3 (2. Method) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | We propose two methods: (1) Coupled Visuomotor Optimization (CVO) learns robot and camera actions at the same time. | p. 3 (2. Method), p. 4 (2. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 2. Method - extractive body cue:** Rewards: For the navigation task, we use distance to goal reward ∥gt∥along with a forward progress reward / (vt)g / where (vt)g is velocity along ...
- **p. 4 / 2. Method - extractive body cue:** This is followed by a lift reward if a successful grasp is detected (based on whether contact forces cross a threshold). r_\ t ext r ...
- **p. 5 / 2.2. Phase 2 - From Scandots to Depth - extractive body cue:** This is supervised using L2 loss from the phase 1 actions.
- **p. 3 / 2. Method - extractive body cue:** We propose two methods: (1) Coupled Visuomotor Optimization (CVO) learns robot and camera actions at the same time.
- **p. 3 / 2. Method - extractive body cue:** This is followed by a phase-2 supervised training where this behavior is distilled into a student network that operates with ego-centric depth images (2) Decoupled ...
- **p. 5 / 2.2. Phase 2 - From Scandots to Depth - extractive body cue:** For the navigation policy we optimize \ min _{C_\t ext rm {nav}, \pi '_ \te x trm {nav }} \left \/ \pi '_\textrm {nav}(C_\textrm {nav}(\mathbf ...
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 5 (2.2. Phase 2 - From Scandots to Depth), p. 4 (2. Method), p. 4 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | particular, policy, gets, proprioception, only, visible, scandots, observation, predict, camera, robot, actions, trained, phase | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | particular, policy, gets, proprioception, only, visible, scandots, observation, predict, camera | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | find, outperforms, classical, methods, baselines, active, vision, Coupled, Visuomotor, Optimization | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | Rewards, navigation, task, distance, goal, reward, along, forward, progress, where | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 2. Method - extractive body cue:** In particular, the policy gets proprioception xt and only visible scandots ˜st = F(st, xt) as observation and has to predict both the camera and ...
- **p. 4 / 2. Method - extractive body cue:** This policy is trained via RL to predict the robot actions from phase 1 policy arobot.
- **p. 5 / 2.2. Phase 2 - From Scandots to Depth - extractive body cue:** This latent is passed to a student policy π′ to predict the actions [˜arobot, ˜acam].
- **p. 2 / 1. Introduction - extractive body cue:** We train our approach via reinforcement learning (RL), and to get around the computational bottleneck of rendering depth images, we use a teacher-student training framework ...
- **p. 3 / 2. Method - extractive body cue:** 2.1.1 Pick Policy This accesses proprioception xt consisting of robot joint angles and velocities qt, ˙qt, base linear and angular velocity vt, ωt.
- **p. 3 / 2. Method - extractive body cue:** This is followed by a phase-2 supervised training where this behavior is distilled into a student network that operates with ego-centric depth images (2) Decoupled ...
- **p. 5 / 2.2. Phase 2 - From Scandots to Depth - extractive body cue:** Similarly, for the pick policy we estimate current object position ot from depth \ min _{C_ \tex trm {pick}, \pi '_\ tex trm {pick}} \ ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value was not selected from the PDF body. | For instance, if the camera swivels around the observations at the next timestep may look completely different. | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value was not selected from the PDF body. | We train a single model that not only outputs low-level controls for the robot body and arm but also predicts where should ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value was not selected from the PDF body. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile was not selected from the PDF body. | We train using IsaacGymEnvs [26] using 8192 environments which takes 6 hours of training for phase 1 and 10 hours of training ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 2. Method - extractive body cue:** This is followed by a phase-2 supervised training where this behavior is distilled into a student network that operates with ego-centric depth images (2) Decoupled ...
- **p. 4 / 2. Method - extractive body cue:** Since the scandots are permutation invariant, we pass them through a trainable point-net architecture P to obtain compressed latent zt = P(˜st) that we pass ...
- **p. 5 / 3. Experimental Setup - extractive body cue:** We train using IsaacGymEnvs [26] using 8192 environments which takes 6 hours of training for phase 1 and 10 hours of training time for phase ...
- **p. 3 / 2. Method - extractive body cue:** In the first one, we learn mobile manipulation behaviors via RL using a cheapto-compute variant of depth and in phase 2 we train a CNN ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** followed, phase-2, supervised, training, where, behavior, distilled, student, network, operates, ego-centric, depth, images, Decoupled, Visuomotor, Optimization, DVO, decouples, action, perception.
- **Relevant PDF headings:** 2. Method (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | While simulation benchmarks are useful for fair comparison with baselines as well as reproducibility, real-world experimenting is essential for determining the efficacy ... | p. 5 (4. Results and Analysis), p. 7 (4.3. Simulation results) |
| Base-arm task decision | We report the success rate of our method compared with the baseline. | p. 8 (4.3. Simulation results), p. 5 (4. Results and Analysis) |
| Execution / correction | Ours achieves ≈ 68% higher success rate than the FixCam baseline with the 18139 | p. 7 (4.3. Simulation results), p. 7 (4.3. Simulation results) |

## Failure and Ablation Link

- **p. 5 / 3. Experimental Setup - extractive body cue:** This is used to test whether reactive navigation is superior to planning. • NoPointNet: Instead of passing object scandots through a permutation-invariant PointNet architecture, we ...
- **p. 7 / 4.3. Simulation results - extractive body cue:** Our method achieves ≈33% higher success rate than the NoPointNet baseline since permutation invariant scandots latent makes the optimization problem easier and also generalizes better ...
- **p. 8 / 4.3. Simulation results - extractive body cue:** Finally, we compare between the decoupled (DVO) and coupled (CVO) variants of our method and find that they achieve similar performance.
- **p. 8 / 4.3. Simulation results - extractive body cue:** The classical performs reasonably in static environments, it quickly breaks with dynamic obstacles like humans walking around, whereas our method shows more robust reactivity to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. We illustrate one scenario of the simulation benchmark here with many obstacles in a narrow passage. The agent learns to develop whole-body coordination ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. We illustrate one scenario of the simulation benchmark here with many obstacles in a narrow passage. The agent learns to develop whole-body coordination ...
- **p. 5 / 4. Results and Analysis - extractive body cue:** What are the limitations of the latter?

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (2. Method), p. 4 (2. Method), p. 3 (2. Method), p. 4 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth), p. 5 (2.2. Phase 2 - From Scandots to Depth), objective p. 4 (2. Method), p. 4 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth), p. 3 (2. Method), p. 3 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth), temporal p. 4 (2. Method), p. 2 (1. Introduction), p. 2 (2. Method), p. 4 (2. Method), p. 5 (2. Method), p. 5 (3. Experimental Setup).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Since the scandots are permutation invariant, we pass them through a trainable point-net architecture P to obtain compressed latent zt = P(˜st) that we pass to the policy [\math bf ... (p. 4, 2. Method).
- **Objective/update evidence:** We propose two methods: (1) Coupled Visuomotor Optimization (CVO) learns robot and camera actions at the same time. (p. 3, 2. Method).
- **Temporal/runtime evidence:** Note that this entire process is very different from the classical approach, where perception, planning, and obstacle avoidance are separate processes executed separately and in sequence. (p. 2, 2. Method).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
