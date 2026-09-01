# Method - Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p135.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p135.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 6 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY)): Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object pose and extrinsic contacts; ii) a passive compliance ...

## Method Body Digest

- **p. 3 / IV. METHODOLOGY - extractive body cue:** Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object pose and extrinsic ...
- **p. 3 / IV. METHODOLOGY - extractive body cue:** The main contributions of our work are in components (iii) and (iv) where we augment the model in (ii) with contact-aware constraints for object poses ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** Extrinsic Contact Trajectory Optimization The goal of the controller is to generate a trajectory of endeffector and grasped object poses that results in the desired ...
- **p. 6 / IV. METHODOLOGY - extractive body cue:** We use the log-barrier function to enforce this constraint.
- **p. 4 / IV. METHODOLOGY - extractive body cue:** Tactile Elasticity Model The goal of the tactile elasticity module is to model the force-deformation relationship of the Soft Bubbles tactile sensor for a grasped ...
- **p. 4 / IV. METHODOLOGY - extractive body cue:** Extrinsic Contact Model The goal of the extrinsic contact model is to model the dynamics of the extrinsic object in contact with the grasped object ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** In general, the trajectory optimization problem is nonconvex since the force balance on the extrinsic and grasped object in (P1) depends on Jacobians and gravitational ...
- **p. 6 / IV. METHODOLOGY - extractive body cue:** The resultant cost function is defined as follows: L = Lcone + Lsmooth + Lcontact force + Lpenetration where: • Cone Loss (Lcone): Incentivizes the ...

## Design Rationale

- **p. 5 / IV. METHODOLOGY - extractive body cue:** The key contribution of our method is to formulate the contact trajectory optimization precisely to address these requirements while also being amenable to gradient-based optimization ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** An integral part of our method is the use of tactile sensors.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method is able to produce a variety of "manipulation skills" and is amenable to gradient-based optimization by exploiting differentiability within contact modes (e.g., specifications ...

## Source Evidence Cues

- **p. 3 / IV. METHODOLOGY - extractive body cue:** Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object pose and extrinsic ...
- **p. 3 / IV. METHODOLOGY - extractive body cue:** The main contributions of our work are in components (iii) and (iv) where we augment the model in (ii) with contact-aware constraints for object poses ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** Extrinsic Contact Trajectory Optimization The goal of the controller is to generate a trajectory of endeffector and grasped object poses that results in the desired ...
- **p. 6 / IV. METHODOLOGY - extractive body cue:** We use the log-barrier function to enforce this constraint.
- **p. 4 / IV. METHODOLOGY - extractive body cue:** Tactile Elasticity Model The goal of the tactile elasticity module is to model the force-deformation relationship of the Soft Bubbles tactile sensor for a grasped ...
- **p. 4 / IV. METHODOLOGY - extractive body cue:** Extrinsic Contact Model The goal of the extrinsic contact model is to model the dynamics of the extrinsic object in contact with the grasped object ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** In general, the trajectory optimization problem is nonconvex since the force balance on the extrinsic and grasped object in (P1) depends on Jacobians and gravitational ...
- **Detected method headings:** IV. METHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object ... | p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | The main contributions of our work are in components (iii) and (iv) where we augment the model in (ii) with contact-aware constraints ... | p. 3 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | Extrinsic Contact Trajectory Optimization The goal of the controller is to generate a trajectory of endeffector and grasped object poses that results ... | p. 5 (IV. METHODOLOGY), p. 6 (IV. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / IV. METHODOLOGY - extractive body cue:** The resultant cost function is defined as follows: L = Lcone + Lsmooth + Lcontact force + Lpenetration where: • Cone Loss (Lcone): Incentivizes the ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** 4) Given the object and robot poses, the external wrench, and the contact forces compute the loss function L and backpropagate the gradients through the ...
- **p. 6 / IV. METHODOLOGY - extractive body cue:** constraints and replace them with a cost term that pushes these contact forces to the contact cone.
- **p. 5 / IV. METHODOLOGY - extractive body cue:** Moreover, since the Jacobian formation is differentiable, inspired by OptNet [38], we can propagate the gradients through the QP and employ gradient-based optimization to iteratively ...
- **p. 3 / IV. METHODOLOGY - extractive body cue:** We constraint the object pose to be in SE(2), i.e. in the task plane.
- **p. 3 / IV. METHODOLOGY - extractive body cue:** The main contributions of our work are in components (iii) and (iv) where we augment the model in (ii) with contact-aware constraints for object poses ...
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 5 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 6 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | composed, core, components, stateestimation, pipeline, feedback, tactile, sensor, estimate, object, pose, extrinsic, contacts, passive | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | composed, core, components, stateestimation, pipeline, feedback, tactile, sensor, estimate, object | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | contribution, formulate, contact, trajectory, optimization, precisely, address, requirements, while, being | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | resultant, cost, function, defined, follows, Lcone, Lsmooth, Lcontact, force, Lpenetration | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / IV. METHODOLOGY - extractive body cue:** Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object pose and extrinsic ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Here, we use high-resolution and highly deformable tactile sensors (Soft Bubbles [2]) because they: i) allow for state-estimation that provides key feedback for controls that ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This is because robots of the future will likely extensively use tactile sensors as they provide a means for feedback directly from the physical interaction ...
- **p. 3 / IV. METHODOLOGY - extractive body cue:** There are two methods to recover this wrench that are interchangeable: 1) Use a wrist-mounted force-torque sensor to directly measure the wrench or 2) Use ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** 2) Given the grasped object state xgo and the robot state xee use the tactile compliance model to compute the external wrench applied to the ...
- **p. 4 / IV. METHODOLOGY - extractive body cue:** Tactile Elasticity Model The goal of the tactile elasticity module is to model the force-deformation relationship of the Soft Bubbles tactile sensor for a grasped ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** Extrinsic Contact Trajectory Optimization The goal of the controller is to generate a trajectory of endeffector and grasped object poses that results in the desired ...
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | For each method, we perform 5 offline trajectory optimizations with a horizon of 40 steps. | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | [30] presents a hierarchical planning framework for planning through rigid body motions and complex contact sequences based on Monte Carlo tree search. | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not recovered | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | For each method, we perform 5 offline trajectory optimizations with a horizon of 40 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / IV. METHODOLOGY - extractive body cue:** The main contributions of our work are in components (iii) and (iv) where we augment the model in (ii) with contact-aware constraints for object poses ...
- **p. 6 / IV. METHODOLOGY - extractive body cue:** We use the log-barrier function to enforce this constraint.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** composed, core, components, stateestimation, pipeline, feedback, tactile, sensor, estimate, object, pose, extrinsic, contacts, passive, compliance, model, maps, changes, grasped, forces.
- **Relevant PDF headings:** IV. METHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | This expansion would significantly broaden the applicability of our method to real-world manipulation tasks involving intricate object shapes and diverse robot motions. | p. 10 (V. EXPERIMENTS AND RESULTS), p. 10 (V. EXPERIMENTS AND RESULTS) |
| Contact / dynamics inference | To ensure a fair comparison with the baseline methods, we evaluate two different versions of each: one with 100 QP queries and ... | p. 9 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS) |
| Force-aware action correction | While the current model yields satisfactory results, exploring higher-dimensional models with improved accuracy could further enhance performance. | p. 10 (V. EXPERIMENTS AND RESULTS), p. 7 (V. EXPERIMENTS AND RESULTS) |

## Failure and Ablation Link

- **p. 8 / V. EXPERIMENTS AND RESULTS - extractive body cue:** We report the mean absolute error for each of the wrench and pose components.
- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques.
- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** DISCUSSION, LIMITATIONS, AND FUTURE WORK In this paper, we proposed an approach to extrinsic object manipulation leveraging tactile sensor compliance, tactile sensor measurements, and contact ...
- **p. 6 / V. EXPERIMENTS AND RESULTS - extractive body cue:** In this instance, the contacts between the object and the environment must be sticking, i.e. fc,i ∈int Fc,i. • Grasped Object Pivoting: The goal is ...
- **p. 7 / V. EXPERIMENTS AND RESULTS - extractive body cue:** We display the sticking contact points in red and the slipping contacts in green.
- **p. 8 / V. EXPERIMENTS AND RESULTS - extractive body cue:** The desired contact mode is sticking contact between the grasped and extrinsic objects contacts, while the contact between the extrinsic object and the environment must ...
- **p. 9 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Additionally, we observed instances of slippage between the sensor and the grasped object, which violates the assumption of sticking contact between them.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 6 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), objective p. 6 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 6 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), temporal p. 9 (V. EXPERIMENTS AND RESULTS), p. 2 (II. RELATED WORK), p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
