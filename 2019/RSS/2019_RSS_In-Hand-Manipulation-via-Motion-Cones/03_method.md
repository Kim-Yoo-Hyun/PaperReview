# Method - In-Hand Manipulation via Motion Cones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1810.00219; PDF retrieval source: https://arxiv.org/pdf/1810.00219. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA)): Algorithm 1 : In-Hand Manipulation Planner input : qinit, qgoal output : tree T T ←initialize tree(qinit) generate motionCones(T , qinit) while qgoal /∈T or cost(qgoal) > cost threshold do ...

## Method Body Digest

- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** Algorithm 1 : In-Hand Manipulation Planner input : qinit, qgoal output : tree T T ←initialize tree(qinit) generate motionCones(T , qinit) while qgoal /∈T or ...
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** We assume the following physical properties of the system: · Object geometry and mass. · Initial and goal pose of an object in a grasp, ...
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** In [3], we present a planning framework where at the highlevel, a T-RRT∗-based architecture samples different object poses in the grasp [4, 16].
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** The planner initiates a tree T with qinit and generates motion cones at qinit.
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** We define the configuration cost as the distance from the goal.
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** For selective exploration, the TRRT* framework relies on a transition test that filters the sampled configurations to prefer exploration in low configuration-cost regions.
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** We set the cost of a push 0.1 if the parent node uses the same pusher as the child and 1 otherwise.
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** While the desired object pose is not reached within some cost threshold, a random configuration qrand is sampled.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We propose a polyhedral approximation to the motion cone for efficient computation. • Experimental validation of the stick/slip condition of motion cones in a prehensile ...
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** In [3], we present a planning framework where at the highlevel, a T-RRT∗-based architecture samples different object poses in the grasp [4, 16].

## Source Evidence Cues

- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** Algorithm 1 : In-Hand Manipulation Planner input : qinit, qgoal output : tree T T ←initialize tree(qinit) generate motionCones(T , qinit) while qgoal /∈T or ...
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** We assume the following physical properties of the system: · Object geometry and mass. · Initial and goal pose of an object in a grasp, ...
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** In [3], we present a planning framework where at the highlevel, a T-RRT∗-based architecture samples different object poses in the grasp [4, 16].
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** The planner initiates a tree T with qinit and generates motion cones at qinit.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | Algorithm 1 : In-Hand Manipulation Planner input : qinit, qgoal output : tree T T ←initialize tree(qinit) generate motionCones(T , qinit) while ... | p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | We assume the following physical properties of the system: · Object geometry and mass. · Initial and goal pose of an object ... | p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | In [3], we present a planning framework where at the highlevel, a T-RRT∗-based architecture samples different object poses in the grasp [4, ... | p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** We define the configuration cost as the distance from the goal.
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** For selective exploration, the TRRT* framework relies on a transition test that filters the sampled configurations to prefer exploration in low configuration-cost regions.
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** We set the cost of a push 0.1 if the parent node uses the same pusher as the child and 1 otherwise.
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** While the desired object pose is not reached within some cost threshold, a random configuration qrand is sampled.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Algorithm, In-Hand, Manipulation, Planner, input, qinit, qgoal, output, tree, initialize, generate, motionCones, while, cost | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | Algorithm, In-Hand, Manipulation, Planner, input, qinit, qgoal, output, tree, initialize | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | present, three, main, contributions, Mechanics, motion, cones, planar, tasks, gravity | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | define, configuration, cost, distance, goal, selective, exploration, TRRT, framework, relies | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** Algorithm 1 : In-Hand Manipulation Planner input : qinit, qgoal output : tree T T ←initialize tree(qinit) generate motionCones(T , qinit) while qgoal /∈T or ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In general planar tasks, external forces other than the pusher force (e.g., gravity) can alter the dynamics of contact interactions between the pusher, object, and ...
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** We assume the following physical properties of the system: · Object geometry and mass. · Initial and goal pose of an object in a grasp, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** A motion cone is the set of feasible motions that a rigid body can follow under the action of a frictional push.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The generalization of motion cones to interactions with gravity opens a door for efficient and robust planning of inhand manipulations that respect and exploit the ...
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** Let qinit and qgoal be an initial and desired pose of the object in the gripper frame respectively.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In Section V we discuss the computational aspects in the calculation and approximation of motion cones for pushing an object gripped with a finite force.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | In simulation, the direction of gravity remains constant in the pusher frame, because in reality, the pushers are fixed features. | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | [18] showed that for a similar setting, if the object is pushed horizontally in the grasp it slides down as it moves ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | The planning times in Table II are the median times over 10 trials. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Algorithm, In-Hand, Manipulation, Planner, input, qinit, qgoal, output, tree, initialize, generate, motionCones, while, cost, threshold, qrand, sample, random, configuration, qparent.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | 9: Simulation and experimental run for a pushing strategy to regrasp the aluminum object with low friction pushers. | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Grasp / trajectory generation | While there are no comparable available algorithms that can solve the type of regrasps we are interested in, we provide comparisons with ... | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Contact execution / correction | Similar to [3], our planner finds a strategy to achieve the regrasp using only one pusher. | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |

## Failure and Ablation Link

- **p. 8 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** When we replace the pushers with high-friction pushers (pushers with rubber coating), the planner detects that the desired object twist lies inside the motion cone ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, the unit grasp wrench can be scaled such that ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8: 2000 random prehensile pushes in the configuration shown in Fig. 7 are characterized by the slip observed at the pusher contact. The motion ...
- **p. 7 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** These include sampling with rejection by a feasibility check for stable pushing [3], and a complementarity formulation (MNCP) that allows both sticking and slipping at ...
- **p. 8 / VIII. DISCUSSION - extractive body cue:** We believe that the extension and application of motion cones to more general settings provides new opportunities for fast and robust manipulation through contact.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), objective p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), temporal p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
