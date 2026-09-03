# Method - Optimization-Based Locomotion Planning, Estimation, and Control Design for the Atlas Humanoid Robot

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.research.ed.ac.uk/en/publications/optimization-based-locomotion-planning-estimation-and-controldesi/; PDF retrieval source: https://www.cs.cmu.edu/~cga/z/Kuindersma_AURO_2016.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.1.1 Convex decomposition), p. 8 (3.2 Dynamic motion planning), p. 11 (4.4 Additional costs and constraints), p. 8 (3.2 Dynamic motion planning), p. 10 (4 Controller design), p. 3 (3.1 Footstep planning as a mixed-integer convex)): We use the polytope representation in our planner, since it is always of larger volume than the (inscribed) ellipsoid and can be represented as a set of linear constraints.

## Method Body Digest

- **p. 5 / 3.1.1 Convex decomposition - extractive body cue:** We use the polytope representation in our planner, since it is always of larger volume than the (inscribed) ellipsoid and can be represented as a ...
- **p. 8 / 3.2 Dynamic motion planning - extractive body cue:** As will be discussed below, we use a redundant multiple-force description of the total wrench acting on a rigid body because it permits the use ...
- **p. 11 / 4.4 Additional costs and constraints - extractive body cue:** For this we used a simple logic to determine what contact force variables should be included in the 123
- **p. 8 / 3.2 Dynamic motion planning - extractive body cue:** By simultaneously optimizing the states and inputs along the trajectory, transcription methods avoid numerical issues that can be present in shooting methods (in which small ...
- **p. 10 / 4 Controller design - extractive body cue:** In the following sections, we write the problem in a general form first, then describe particular implementations used in conjunction with the planners described previously.
- **p. 3 / 3.1 Footstep planning as a mixed-integer convex - extractive body cue:** If the objective function and constraints are convex, then such an optimization can be solved extremely efficiently (Boyd and Vandenberghe 2004).
- **p. 3 / 3 Motion planning - extractive body cue:** Then we solve an optimization problem that assigns contacts to these regions in a way that minimizes cost while respecting kinematic and dynamic constraints.
- **p. 6 / 3.1.3 Determining the number of footsteps - extractive body cue:** Adding a negative cost on each ρ j to the objective in our optimization allows us to reward the planner for taking fewer footsteps without ...

## Design Rationale

- **p. 4 / 3.1 Footstep planning as a mixed-integer convex - extractive body cue:** Unfortunately, the set of safe terrain is unlikely to be convex or even connected: in an environment as simple as a staircase, the safe terrain ...
- **p. 1 / 1 Introduction - extractive body cue:** In this paper we describe our approach to addressing these problems with Atlas.
- **p. 1 / 1 Introduction - extractive body cue:** Our approach to walking combines an efficient footstep planner with a simple dynamic model of the robot to efficiently compute desired walking trajectories.

## Source Evidence Cues

- **p. 5 / 3.1.1 Convex decomposition - extractive body cue:** We use the polytope representation in our planner, since it is always of larger volume than the (inscribed) ellipsoid and can be represented as a ...
- **p. 8 / 3.2 Dynamic motion planning - extractive body cue:** As will be discussed below, we use a redundant multiple-force description of the total wrench acting on a rigid body because it permits the use ...
- **p. 11 / 4.4 Additional costs and constraints - extractive body cue:** For this we used a simple logic to determine what contact force variables should be included in the 123
- **p. 8 / 3.2 Dynamic motion planning - extractive body cue:** By simultaneously optimizing the states and inputs along the trajectory, transcription methods avoid numerical issues that can be present in shooting methods (in which small ...
- **p. 10 / 4 Controller design - extractive body cue:** In the following sections, we write the problem in a general form first, then describe particular implementations used in conjunction with the planners described previously.
- **p. 3 / 3.1 Footstep planning as a mixed-integer convex - extractive body cue:** If the objective function and constraints are convex, then such an optimization can be solved extremely efficiently (Boyd and Vandenberghe 2004).
- **p. 3 / 3 Motion planning - extractive body cue:** Then we solve an optimization problem that assigns contacts to these regions in a way that minimizes cost while respecting kinematic and dynamic constraints.
- **Detected method headings:** 4 Controller design (p. 9); 5.1 Requirements and approach (p. 14); 5.4 Process model (p. 15); 5.5 Measurement model (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | We use the polytope representation in our planner, since it is always of larger volume than the (inscribed) ellipsoid and can be ... | p. 5 (3.1.1 Convex decomposition), p. 8 (3.2 Dynamic motion planning) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | As will be discussed below, we use a redundant multiple-force description of the total wrench acting on a rigid body because it ... | p. 8 (3.2 Dynamic motion planning), p. 11 (4.4 Additional costs and constraints) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | For this we used a simple logic to determine what contact force variables should be included in the 123 | p. 11 (4.4 Additional costs and constraints), p. 8 (3.2 Dynamic motion planning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3 Motion planning - extractive body cue:** Then we solve an optimization problem that assigns contacts to these regions in a way that minimizes cost while respecting kinematic and dynamic constraints.
- **p. 6 / 3.1.3 Determining the number of footsteps - extractive body cue:** Adding a negative cost on each ρ j to the objective in our optimization allows us to reward the planner for taking fewer footsteps without ...
- **p. 10 / 4.1 General formulation - extractive body cue:** Next we define a quadratic cost function, g(x(t), u(t), t) = ¯xT (t)Q¯x(t) + ¯uT (t)R¯u(t), (15) and solve the constrained minimization problem, minimize u(t)
- **p. 10 / 4.1 General formulation - extractive body cue:** (16) By the Hamilton-Jacobi-Bellman (HJB) equation (Bertsekas 1995), we know that the optimal controller satisfies ¯u∗(t) = arg min ¯u ℓ(¯x, ¯u, t), (17) ℓ(¯x, ...
- **p. 13 / 4.5 Efficient QP solver - extractive body cue:** (2008) consider the MPC problems where the cost function and dynamic constraints are the same at each time step; i.e., the QPs solved at iteration ...
- **p. 3 / 3.1 Footstep planning as a mixed-integer convex - extractive body cue:** If the objective function and constraints are convex, then such an optimization can be solved extremely efficiently (Boyd and Vandenberghe 2004).
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 3 (3.1 Footstep planning as a mixed-integer convex), p. 7 (3.1.3 Determining the number of footsteps), p. 8 (3.2 Dynamic motion planning), p. 9 (3.2 Dynamic motion planning), p. 12 (4.4 Additional costs and constraints), p. 10 (4.1 General formulation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Note, inputs, computed, solving, general, equal, thresholding, output, closed-form, LQR, policy, Given, current, robot | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Note, inputs, computed, solving, general, equal, thresholding, output, closed-form, LQR | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | Unfortunately, safe, terrain, unlikely, convex, even, connected, environment, simple, staircase | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | Then, solve, optimization, problem, assigns, contacts, regions, minimizes, cost, while | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 10 / 4.1 General formulation - extractive body cue:** Note that inputs computed by solving this QP are, in general, not equal to those computed by thresholding the output of the closed-form LQR policy.
- **p. 11 / 4.4 Additional costs and constraints - extractive body cue:** Given the current robot state, q, v, we can compute the equations of motion, H(q)˙v + C(q, v) = Bτ + JT λ, (25) H ...
- **p. 14 / 5.1 Requirements and approach - extractive body cue:** LQR solutions can be recomputed online (typically in a separate thread) using the current state of the robot to reduce the systems sensitivity to deviations ...
- **p. 2 / 1 Introduction - extractive body cue:** Inputs to the controller are computed by a low-drift state estimator that fuses kinematic, inertial, and LIDAR information (Sect.
- **p. 2 / 1 Introduction - extractive body cue:** We describe an efficient active-set algorithm capable of finding solutions in less than 1 millisecond for Atlas (68 states and 28 inputs).
- **p. 8 / 3.2 Dynamic motion planning - extractive body cue:** Transcription methods, on the other hand, include a finite set of states along the trajectory as decision variables and incorporate the dynamics of the system ...
- **p. 8 / 3.2 Dynamic motion planning - extractive body cue:** By simultaneously optimizing the states and inputs along the trajectory, transcription methods avoid numerical issues that can be present in shooting methods (in which small ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | However, because of the inaccuracy in joint sensing and because the robot's foot does not always remain motionless after initial contact, we ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | An estimate w ˆpb [k] of the position of the floating base at time step k can be computed using the current ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | However, because of the inaccuracy in joint sensing and because the robot's foot does not always remain motionless after initial contact, we ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.1.1 Convex decomposition - extractive body cue:** We use the polytope representation in our planner, since it is always of larger volume than the (inscribed) ellipsoid and can be represented as a ...
- **p. 8 / 3.2 Dynamic motion planning - extractive body cue:** As will be discussed below, we use a redundant multiple-force description of the total wrench acting on a rigid body because it permits the use ...
- **p. 3 / 3.1 Footstep planning as a mixed-integer convex - extractive body cue:** If the objective function and constraints are convex, then such an optimization can be solved extremely efficiently (Boyd and Vandenberghe 2004).
- **p. 3 / 3 Motion planning - extractive body cue:** Then we solve an optimization problem that assigns contacts to these regions in a way that minimizes cost while respecting kinematic and dynamic constraints.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** polytope, representation, planner, since, always, larger, volume, inscribed, ellipsoid, represented, linear, constraints, will, discussed, below, redundant, multiple-force, description, total, wrench.
- **Relevant PDF headings:** 4 Controller design (p. 9); 5.1 Requirements and approach (p. 14); 5.4 Process model (p. 15); 5.5 Measurement model (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | We describe several experiments performed on the robot and in simulation. | p. 19 (6 Experiments), p. 19 (6.1 State estimation evaluation) |
| Balance-aware whole-body execution | no linked comparison cue | 본문 anchor 없음 |
| Recovery / adaptation | To characterize the state estimator we evaluate its performance in a variety of experiments. | p. 19 (6.1 State estimation evaluation), p. 19 (6.1 State estimation evaluation) |

## Failure and Ablation Link

- **p. 20 / 6.3 Closed-loop walking with LIDAR feedback - extractive body cue:** The robot's trailing foot eventually collided with the front of the step resulting in a fall.
- **p. 20 / 6.3 Closed-loop walking with LIDAR feedback - extractive body cue:** This scenario requires great precision, if the state estimator drifts by even a few centimeters, the robot will hit a step edge and fall.
- **p. 22 / 6.4.1 Running - extractive body cue:** 13), require at least 3cm of clearance between links to avoid self-collisions, and constrain the gaze of the robot's head cameras to be no more ...
- **p. 19 / 6.1 State estimation evaluation - extractive body cue:** In the manipulation experiment, the LIDAR contribution actually degrades performance slightly due to occlusions caused by arm motions.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.1.1 Convex decomposition), p. 8 (3.2 Dynamic motion planning), p. 11 (4.4 Additional costs and constraints), p. 8 (3.2 Dynamic motion planning), p. 10 (4 Controller design), p. 3 (3.1 Footstep planning as a mixed-integer convex), objective p. 3 (3 Motion planning), p. 6 (3.1.3 Determining the number of footsteps), p. 10 (4.1 General formulation), p. 10 (4.1 General formulation), p. 13 (4.5 Efficient QP solver), p. 3 (3.1 Footstep planning as a mixed-integer convex), temporal p. 17 (5.5.1 Leg kinematics), p. 17 (5.5.1 Leg kinematics), p. 11 (4.2 COM and COP stabilization), p. 13 (4.5 Efficient QP solver), p. 13 (4.5 Efficient QP solver), p. 1 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
