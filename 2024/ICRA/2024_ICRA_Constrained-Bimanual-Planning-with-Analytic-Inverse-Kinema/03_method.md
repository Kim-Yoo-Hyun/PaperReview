# Method - Constrained Bimanual Planning with Analytic Inverse Kinematics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.08770; PDF retrieval source: https://arxiv.org/pdf/2309.08770. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY)): 2) Trajectory Optimization: Trajectory optimization in configuration space is already nonconvex, so implementing constraints (5b) and (5c) requires no algorithmic changes.

## Method Body Digest

- **p. 4 / III. METHODOLOGY - extractive PDF cue:** 2) Trajectory Optimization: Trajectory optimization in configuration space is already nonconvex, so implementing constraints (5b) and (5c) requires no algorithmic changes.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Although this constraint would be enforced by the later constraints, specifically handling this case first greatly improves the performance of the later counterexample searches.
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** Algorithm 1: Constrained IRIS (Single Iteration) Input: Bounding Box H0(A0, b0) Hyperellipsoid E(C, d) s.t. d ∈H0(A0, b0) Constraint Sets CS1, . . . , ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Parametrizing the Kinematically Constrained Space Now, we turn our attention to the bimanual case.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Finally, we explain the modifications needed to adapt existing planning algorithms to utilize this parametrization.
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** To also enforce H(A, b) ⊆QFREE, we search for configurations q such that the robot is in collision.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** We minimize the arc length in the parametrized space L(¯γ), as this objective provides a useful convex surrogate for the true (nonconvex) objective (5a).
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** (4d) (L denotes the arc length functional, but can be replaced with another cost.) The main challenge this formulation presents is the nonlinear equality constraint ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Then, we present our parametrization of the constraint manifold for bimanual planning, and discuss its relevant geometric and topological properties.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** If a robot must move an object that it is holding with both hands, we propose constructing a plan for one "controllable" arm, and then ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Finally, we present various experiments demonstrating the efficacy of these new techniques.

## Source Evidence Cues

- **p. 4 / III. METHODOLOGY - extractive PDF cue:** 2) Trajectory Optimization: Trajectory optimization in configuration space is already nonconvex, so implementing constraints (5b) and (5c) requires no algorithmic changes.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Although this constraint would be enforced by the later constraints, specifically handling this case first greatly improves the performance of the later counterexample searches.
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** Algorithm 1: Constrained IRIS (Single Iteration) Input: Bounding Box H0(A0, b0) Hyperellipsoid E(C, d) s.t. d ∈H0(A0, b0) Constraint Sets CS1, . . . , ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Parametrizing the Kinematically Constrained Space Now, we turn our attention to the bimanual case.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Finally, we explain the modifications needed to adapt existing planning algorithms to utilize this parametrization.
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** To also enforce H(A, b) ⊆QFREE, we search for configurations q such that the robot is in collision.
- **Detected method headings:** III. METHODOLOGY (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / error representation | motion·force 목표를 제어 error로 바꾼다 | joint/task state, reference, wrench | task frame, Jacobian, impedance, selection 또는 error coordinates를 구성 | desired task command | 2) Trajectory Optimization: Trajectory optimization in configuration space is already nonconvex, so implementing constraints (5b) and (5c) requires no algorithmic changes. | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Dynamics / constraint solve | 목표를 feasible actuator command로 바꾼다 | error, model, constraints | inverse dynamics, QP, MPC, operational mapping 또는 feedback law를 계산 | torque, force, velocity 또는 position command | Although this constraint would be enforced by the later constraints, specifically handling this case first greatly improves the performance of the later ... | p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY) |
| Feedback / actuation | 실제 state와 disturbance에 따라 command를 닫힌 loop로 보정한다 | sensor feedback과 nominal command | tracking correction, saturation, null-space, fallback 또는 replan을 수행 | next actuation과 response | Algorithm 1: Constrained IRIS (Single Iteration) Input: Bounding Box H0(A0, b0) Hyperellipsoid E(C, d) s.t. d ∈H0(A0, b0) Constraint Sets CS1, . ... | p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / III. METHODOLOGY - extractive PDF cue:** Algorithm 1: Constrained IRIS (Single Iteration) Input: Bounding Box H0(A0, b0) Hyperellipsoid E(C, d) s.t. d ∈H0(A0, b0) Constraint Sets CS1, . . . , ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** We minimize the arc length in the parametrized space L(¯γ), as this objective provides a useful convex surrogate for the true (nonconvex) objective (5a).
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** (4d) (L denotes the arc length functional, but can be replaced with another cost.) The main challenge this formulation presents is the nonlinear equality constraint ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** A configuration (θL, ψR) is valid if: ϕT (fL(θL)) ∈Wj,R (Respect reachability.) (3a) θmin ≤ξ(θL, ψR) ≤θmax (Respect joint limits.) (3b) We call the set ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** These three constraints will ensure H(A, b) ⊆QVALID.
- **Formal bridge:** q, q̇, x, wrench -> u/τ subject to dynamics and actuator/contact constraints -> tracking or interaction error -> stability, tracking and constraint satisfaction.
- **Equation/algorithm anchors:** p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Algorithm, Constrained, IRIS, Single, Iteration, Input, Bounding, Box, Hyperellipsoid, Constraint, Sets, CS1, CSk, Output | joint/task state, reference와 sensor feedback | body cue; exact tensor/frame verify |
| State/latent | Algorithm, Constrained, IRIS, Single, Iteration, Input, Bounding, Box, Hyperellipsoid, Constraint | state estimate, task-space error와 control decision | body cue; notation verify |
| Action/output | Then, present, parametrization, constraint, manifold, bimanual, planning, discuss, relevant, geometric | torque, force, velocity 또는 position command | body cue; unit/decoder verify |
| Objective/constraint | Algorithm, Constrained, IRIS, Single, Iteration, Input, Bounding, Box, Hyperellipsoid, Constraint | tracking or interaction error | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / III. METHODOLOGY - extractive PDF cue:** Algorithm 1: Constrained IRIS (Single Iteration) Input: Bounding Box H0(A0, b0) Hyperellipsoid E(C, d) s.t. d ∈H0(A0, b0) Constraint Sets CS1, . . . , ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** When a rigid object is held with both end effectors, a rigid transformation T ∈SE(3) between them becomes fixed; we let ϕT : XL →SE(3) ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** The connected components of the preimages of W-sheets are called Cbundles and are composed of regular points of C.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Enabling bimanual robots to execute coordinated actions with both arms is essential for achieving (super)human-like skill in automation and home contexts.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In many manipulation tasks, one gripper can be used to provide fixture to the manipuland, while the other performs the desired action [2]; such tasks ...
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** We introduce a bijective mapping between joint angles and end-effector pose for a single arm with analytic IK.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** As with sampling-based planning, collision avoidance (and other constraints applied to the full configuration space) must be enforced at a finer resolution.
- **Normalized interface:** observation=joint/task state, reference와 sensor feedback; state=state estimate, task-space error와 control decision; output/action=torque, force, velocity 또는 position command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instantaneous or receding-horizon reference tracking; exact prediction horizon은 exact value not recovered from the selected body cues. | In Section IV, we demonstrate that this theoretical limitation is not a major roadblock to our framework's efficacy. | episode/sequence/action-chunk boundary |
| Rate / latency | sensor/actuator control tick마다 feedback solve; numeric rate는 paper-specific. | Motion Planning with the Parametrization Constraint (5c) is a nonlinear inequality constraint, so feasible trajectories are constrained to lie in a positive ... | Hz/fps, inference time and control rate |
| Memory | 현재 joint/task state, reference, contact/wrench feedback; long history 여부 확인 필요. | not recovered | window and reset |
| Compute | dynamics/Jacobian evaluation, QP/MPC/inverse-dynamics solve와 actuator latency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. METHODOLOGY - extractive PDF cue:** 2) Trajectory Optimization: Trajectory optimization in configuration space is already nonconvex, so implementing constraints (5b) and (5c) requires no algorithmic changes.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Although this constraint would be enforced by the later constraints, specifically handling this case first greatly improves the performance of the later counterexample searches.
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** Algorithm 1: Constrained IRIS (Single Iteration) Input: Bounding Box H0(A0, b0) Hyperellipsoid E(C, d) s.t. d ∈H0(A0, b0) Constraint Sets CS1, . . . , ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Parametrizing the Kinematically Constrained Space Now, we turn our attention to the bimanual case.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** We now describe the constraint sets CS needed for Algorithm 1 to generate g-convex sets in QVALID ∩QFREE, and how to encode (6c).
- **p. 6 / IV. RESULTS - extractive PDF cue:** Overall, the PRM methods have the shortest online runtimes.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Trajectory, Optimization, configuration, space, already, nonconvex, implementing, constraints, requires, algorithmic, changes, Although, constraint, would, enforced, later, specifically, handling, case, first.
- **Relevant PDF headings:** III. METHODOLOGY (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / error representation | GCS can use such regions to plan motions for objects of different sizes; we include hardware demonstrations in our results video. | p. 6 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Dynamics / constraint solve | We do not compare to any GCS baseline without IK, as the constraint manifold is inherently nonconvex; IK-GCS is the first proposal ... | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Feedback / actuation | AtlasBiRRT runtimes were only averaged over successful runs (not including timeouts). | p. 5 (IV. RESULTS), p. 6 (IV. RESULTS) |

## Failure and Ablation Link

- **p. 5 / IV. RESULTS - extractive PDF cue:** We do not compare to any GCS baseline without IK, as the constraint manifold is inherently nonconvex; IK-GCS is the first proposal for extending GCS ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between the shelves, avoiding collisions and respecting the ...
- **p. 5 / IV. RESULTS - extractive PDF cue:** Paths marked with an asterisk were not collision-free.
- **p. 5 / IV. RESULTS - extractive PDF cue:** Plans from the trajectory optimization baseline also had slight collisions with obstacles.
- **p. 6 / IV. RESULTS - extractive PDF cue:** (c) A region that represents varying grasp distances, in addition to collision-free configurations in the shelf (not shown).
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4: Robot configurations sampled from various IRIS regions. average path length and planning time. We set a maximum planning time of 10 minutes for ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), objective p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), temporal p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
