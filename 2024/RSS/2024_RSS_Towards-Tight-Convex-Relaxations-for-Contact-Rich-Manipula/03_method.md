# Method - Towards Tight Convex Relaxations for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p132.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p132.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (IV. HIGH-LEVEL APPROACH), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (IV. HIGH-LEVEL APPROACH)): A feasible path p through G then has the interpretation as a continuous trajectory from the initial state to the target state, that consists of distinct trajectory segments for each ...

## Method Body Digest

- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** A feasible path p through G then has the interpretation as a continuous trajectory from the initial state to the target state, that consists of ...
- **p. 3 / IV. HIGH-LEVEL APPROACH - extractive body cue:** The first step in formulating our motion planning method is to consider the dynamics and kinematics in a fixed contact mode.
- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** Specifically, for each edge e = (u, v) ∈E we enforce that the last state in the trajectory in vertex u is equal to the ...
- **p. 6 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** Hence, for the non-contact modes we do not model the slider velocity or contact forces, and given a feasible initial slider pose that satisfies (16), ...
- **p. 6 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** The cost takes the following form: N-1 X k=0 L(xk, xk+1) + E(xk, xk+1, uk) + kfh∥fk∥2 2 + N X k=0 ψ(xk) (17) where ...
- **p. 3 / IV. HIGH-LEVEL APPROACH - extractive body cue:** More specifically, quadratic equality constraints arise from considering elements of SO(2), rotations of velocities and forces to the world frame, and the contact torque as ...
- **p. 4 / V. BACKGROUND AND OPTIMIZATION TOOLS - extractive body cue:** A nonconvex QCQP in homogeneous form is the optimization program minimize x⊺Q0x (3a) subject to x⊺Qix ≥0, ∀i = 1, . . . , l ...
- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** In principle, this does not include all the tightening constraints (4d) and yields a potentially weaker convex relaxation, but in practice, we find that the ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method approximates these bilinearities using a tight Semidefinite Programming (SDP) relaxation for each contact mode.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As a first application for evaluating our method, this work explores the task of planar pushing, first studied by Mason in [2].
- **p. 2 / I. INTRODUCTION - extractive body cue:** of planar pushing, the technique we introduce generalizes naturally to more complex multi-contact problems.

## Source Evidence Cues

- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** A feasible path p through G then has the interpretation as a continuous trajectory from the initial state to the target state, that consists of ...
- **p. 3 / IV. HIGH-LEVEL APPROACH - extractive body cue:** The first step in formulating our motion planning method is to consider the dynamics and kinematics in a fixed contact mode.
- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** Specifically, for each edge e = (u, v) ∈E we enforce that the last state in the trajectory in vertex u is equal to the ...
- **p. 6 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** Hence, for the non-contact modes we do not model the slider velocity or contact forces, and given a feasible initial slider pose that satisfies (16), ...
- **p. 6 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** The cost takes the following form: N-1 X k=0 L(xk, xk+1) + E(xk, xk+1, uk) + kfh∥fk∥2 2 + N X k=0 ψ(xk) (17) where ...
- **p. 3 / IV. HIGH-LEVEL APPROACH - extractive body cue:** More specifically, quadratic equality constraints arise from considering elements of SO(2), rotations of velocities and forces to the world frame, and the contact torque as ...
- **p. 4 / V. BACKGROUND AND OPTIMIZATION TOOLS - extractive body cue:** A nonconvex QCQP in homogeneous form is the optimization program minimize x⊺Q0x (3a) subject to x⊺Qix ≥0, ∀i = 1, . . . , l ...
- **Detected method headings:** IV. HIGH-LEVEL APPROACH (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | A feasible path p through G then has the interpretation as a continuous trajectory from the initial state to the target state, ... | p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (IV. HIGH-LEVEL APPROACH) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | The first step in formulating our motion planning method is to consider the dynamics and kinematics in a fixed contact mode. | p. 3 (IV. HIGH-LEVEL APPROACH), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | Specifically, for each edge e = (u, v) ∈E we enforce that the last state in the trajectory in vertex u is ... | p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** In principle, this does not include all the tightening constraints (4d) and yields a potentially weaker convex relaxation, but in practice, we find that the ...
- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** In contrast, in this work we are able to obtain tight relaxations using only quadratic constraints, avoiding the significant computational cost of using higher-order relaxations.
- **p. 4 / V. BACKGROUND AND OPTIMIZATION TOOLS - extractive body cue:** A nonconvex QCQP in homogeneous form is the optimization program minimize x⊺Q0x (3a) subject to x⊺Qix ≥0, ∀i = 1, . . . , l ...
- **p. 3 / V. BACKGROUND AND OPTIMIZATION TOOLS - extractive body cue:** Additionally, each vertex v is associated with a vertex cost lv(xv), a nonnegative convex function of the point xv ∈Xv.
- **p. 3 / V. BACKGROUND AND OPTIMIZATION TOOLS - extractive body cue:** Finally, the edges of the graph are associated to convex constraints of the form (xu, xv) ∈Xe which couple the vertices in an edge e.
- **p. 4 / V. BACKGROUND AND OPTIMIZATION TOOLS - extractive body cue:** Moreover, if X∗is a rank-one minimizer of (4), then x∗satisfying X∗= x∗(x∗)⊺is the global optimum of (3).
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 3 (IV. HIGH-LEVEL APPROACH), p. 5 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | represent, trajectory, segment, within, mode, slider-pusher, system, discrete, knot, points, state, input, uN-1, point | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | represent, trajectory, segment, within, mode, slider-pusher, system, discrete, knot, points | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | approximates, bilinearities, tight, Semidefinite, Programming, SDP, relaxation, contact, mode, first | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | principle, does, include, tightening, constraints, yields, potentially, weaker, convex, relaxation | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** We represent a trajectory segment within each mode for the slider-pusher system by N discrete knot points for the state and N -1 knot points ...
- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** The point xv ∈Xv now corresponds to a trajectory of length N of states and inputs for the sliderpusher system in mode Ci.
- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** We enforce continuity between the state trajectories on a path in the graph.
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We assume isotropic Coulomb friction, i.e., that the coefficient of friction is constant, and the friction force at every contact point must have a constant ...
- **p. 3 / IV. HIGH-LEVEL APPROACH - extractive body cue:** More specifically, quadratic equality constraints arise from considering elements of SO(2), rotations of velocities and forces to the world frame, and the contact torque as ...
- **p. 6 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** Hence, for the non-contact modes we do not model the slider velocity or contact forces, and given a feasible initial slider pose that satisfies (16), ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Planar pushing has applications that span from warehouse automation to service robotics, and although it is among the simplest examples of non-prehensile manipulation, current state-of-the-art ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | The dynamics are then xk+1 = xk + hg(xk, uk) for k = 0, . . . , N -1 with the ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | For both slider geometries, we achieve a success rate of 100%, that is, the rounding step is able to retrieve a feasible ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** Hence, for the non-contact modes we do not model the slider velocity or contact forces, and given a feasible initial slider pose that satisfies (16), ...
- **p. 3 / IV. HIGH-LEVEL APPROACH - extractive body cue:** More specifically, quadratic equality constraints arise from considering elements of SO(2), rotations of velocities and forces to the world frame, and the contact torque as ...
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** This method encodes contact modes implicitly using complementarity constraints that are relaxed and solves the problem as a sequence of NLPs with increasingly strict complementarity ...
- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** Since the denominator is always positive, this function is a maximum over convex functions and is thus readily encoded through NF Rotated Second-Order Cone (RSOC) ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** feasible, path, through, then, interpretation, continuous, trajectory, initial, state, target, consists, distinct, segments, mode, represented, vertices, within, determined, points, first.
- **Relevant PDF headings:** IV. HIGH-LEVEL APPROACH (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | Execution on real hardware Finally, we demonstrate the feasibility of the obtained motion plans on a Kuka LBR iiwa 7 R800 7-DOF ... | p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |
| Grasp / trajectory generation | Comparison with contact-implicit trajectory optimization To compare our method with a state-of-the-art baseline for contact-rich planning, we select a direct, contact-implicit trajectory ... | p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS) |
| Contact execution / correction | For both slider geometries, we achieve a success rate of 100%, that is, the rounding step is able to retrieve a feasible ... | p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** This highlights a key advantage of our approach: by reasoning on a global level, our method (empirically) always finds a solution, without relying on an ...
- **p. 10 / IX. CONCLUSION AND FUTURE WORK - extractive body cue:** Future work will explore the ability of these reduction methods to accelerate the planning.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: a) An example of a configuration-space partitioning Q1, . . . , Q4 and the linear approximations ϕ1, . . . , ϕ4 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Our method is able to generate close-to globally optimal plans for pushing tasks with collision-free motion planning between contact modes. Here, two different ...
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** Our method also guarantees that the trajectory stays collision-free between contacts, while the baseline can be seen to clip the corners of the slider.
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** This limitation is not surprising, as the baseline is a local method that relies heavily on its initial guess.
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (IV. HIGH-LEVEL APPROACH), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (IV. HIGH-LEVEL APPROACH), objective p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 4 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 3 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 3 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 4 (V. BACKGROUND AND OPTIMIZATION TOOLS), temporal p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 3 (III. PROBLEM STATEMENT), p. 10 (IX. CONCLUSION AND FUTURE WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
