# Method - Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p118.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p118.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP)): The first action recommended by this policy is the next controller to execute on the robot.

## Method Body Digest

- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** The first action recommended by this policy is the next controller to execute on the robot.
- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** 3: while abs(b) /∈G do 4: if abs(b) /∈Bsparse then 5: args ←(b0, G, O, s) 6: s, ˆT , Bsparse ←Model-Learning(args) 7: ▷Solve the ...
- **p. 5 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** We introduce an extension to PDDL for specifying schemata for controllers with uncertain effects.
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** We use Bayes3D perception framework for probabilistic pose inference [29].
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** In our experiments we used objects with known mesh object models, but Bayes3D also supports fewshot online learning of object models.
- **p. 5 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** Additionally, planners can exploit the knowledge that after applying an operator from state ¯b, the only reachable new states are those which modify ¯b by ...
- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** In this paper, we focus on planning problems with objectives modeled as goals in belief space (e.g., the goal may be to believe that with ...
- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** In addition, the resulting plans may be overly optimistic because they are untethered from geometric and physical constraints.

## Design Rationale

- **p. 3 / III. BACKGROUND - extractive body cue:** To mitigate this, we introduce the concept of a belief-space controller, which takes the current belief as input and executes in closedloop fashion over extended ...
- **p. 5 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** We introduce an extension to PDDL for specifying schemata for controllers with uncertain effects.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach, TAMPURA, is to exploit a coarse model of each controller's preconditions and effects to rapidly solve deterministic, symbolic planning problems that guide the ...

## Source Evidence Cues

- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** The first action recommended by this policy is the next controller to execute on the robot.
- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** 3: while abs(b) /∈G do 4: if abs(b) /∈Bsparse then 5: args ←(b0, G, O, s) 6: s, ˆT , Bsparse ←Model-Learning(args) 7: ▷Solve the ...
- **p. 5 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** We introduce an extension to PDDL for specifying schemata for controllers with uncertain effects.
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** We use Bayes3D perception framework for probabilistic pose inference [29].
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** In our experiments we used objects with known mesh object models, but Bayes3D also supports fewshot online learning of object models.
- **p. 5 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** Additionally, planners can exploit the knowledge that after applying an operator from state ¯b, the only reachable new states are those which modify ¯b by ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / error representation | motion·force 목표를 제어 error로 바꾼다 | joint/task state, reference, wrench | task frame, Jacobian, impedance, selection 또는 error coordinates를 구성 | desired task command | The first action recommended by this policy is the next controller to execute on the robot. | p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP) |
| Dynamics / constraint solve | 목표를 feasible actuator command로 바꾼다 | error, model, constraints | inverse dynamics, QP, MPC, operational mapping 또는 feedback law를 계산 | torque, force, velocity 또는 position command | 3: while abs(b) /∈G do 4: if abs(b) /∈Bsparse then 5: args ←(b0, G, O, s) 6: s, ˆT , Bsparse ←Model-Learning(args) ... | p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP) |
| Feedback / actuation | 실제 state와 disturbance에 따라 command를 닫힌 loop로 보정한다 | sensor feedback과 nominal command | tracking correction, saturation, null-space, fallback 또는 replan을 수행 | next actuation과 response | We introduce an extension to PDDL for specifying schemata for controllers with uncertain effects. | p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** In this paper, we focus on planning problems with objectives modeled as goals in belief space (e.g., the goal may be to believe that with ...
- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** In addition, the resulting plans may be overly optimistic because they are untethered from geometric and physical constraints.
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** The updated probability P(t + ∆t, x, y, z) at time t + ∆t is given by P(t + ∆t, x, y, z) = P(t, ...
- **p. 5 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** The overall effect of this operator can be described as a probability distribution on the four possible joint outcomes.
- **p. 5 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** Following a controller execution, these effects evaluated on the updated belief belief using the symbol grounding functions in ΨB.
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** We update the occupancy belief probabilities over time as follows.
- **Formal bridge:** q, q̇, x, wrench -> u/τ subject to dynamics and actuator/contact constraints -> tracking or interaction error -> stability, tracking and constraint satisfaction.
- **Equation/algorithm anchors:** p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (VII. REAL-WORLD IMPLEMENTATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Belief-State, Controller, MDP, When, action, space, represents, primitive, controls, robot, joint, torques, end-effector, velocity | joint/task state, reference와 sensor feedback | body cue; exact tensor/frame verify |
| State/latent | Belief-State, Controller, MDP, When, action, space, represents, primitive, controls, robot | state estimate, task-space error와 control decision | body cue; notation verify |
| Action/output | mitigate, introduce, concept, belief-space, controller, takes, current, belief, input, executes | torque, force, velocity 또는 position command | body cue; unit/decoder verify |
| Objective/constraint | focus, planning, problems, objectives, modeled, goals, belief, space, goal, believe | tracking or interaction error | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. BACKGROUND - extractive body cue:** Belief-State Controller MDP When the action space A represents primitive controls to the robot such as joint torques or end-effector velocity commands, the time horizons ...
- **p. 3 / III. BACKGROUND - extractive body cue:** A POMDP is a tuple M = ⟨S, O, A, T , Z, r, b0, γ⟩.1 S, O, and A are the state, observation, and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Each of them contains a unique type of uncertainty including uncertainty in (a) classsification, (b) pose due to noisy sensors or (c) partial observability, (d) ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** If the robot believes it has full knowledge of the state and dynamics of the world, it may confidently take actions that have potentially catastrophic ...
- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** The first action recommended by this policy is the next controller to execute on the robot.
- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** It can be solved with a probabilistic planner such as LAO*, resulting in a risk and uncertainty aware policy in the abstract belief-state MDP.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The robot plans to take information gathering actions based on a posterior estimate of the banana's pose shown in blue.
- **Normalized interface:** observation=joint/task state, reference와 sensor feedback; state=state estimate, task-space error와 control decision; output/action=torque, force, velocity 또는 position command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instantaneous or receding-horizon reference tracking; exact prediction horizon은 exact value was not selected from the PDF body. | The updated probability P(t + ∆t, x, y, z) at time t + ∆t is given by P(t + ∆t, x, y, ... | episode/sequence/action-chunk boundary |
| Rate / latency | sensor/actuator control tick마다 feedback solve; numeric rate는 paper-specific. | TAMP, the key to tractable planning over long time horizons is to sequence short-horizon controllers, exploiting a description of the conditions in ... | Hz/fps, inference time and control rate |
| Memory | 현재 joint/task state, reference, contact/wrench feedback; long history 여부 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | dynamics/Jacobian evaluation, QP/MPC/inverse-dynamics solve와 actuator latency가 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** We use Bayes3D perception framework for probabilistic pose inference [29].
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** In our experiments we used objects with known mesh object models, but Bayes3D also supports fewshot online learning of object models.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, action, recommended, policy, next, controller, execute, robot, while, Bsparse, then, args, Model-Learning, Solve, MDP, over, LAO-Star, Get, introduce, extension.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / error representation | Searching for Objects in Clutter This task is the real-world counterpart to the PARTIAL OBSERVABILITY simulated experiment. | p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Dynamics / constraint solve | Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to ... | p. 7 (Figure/Table caption), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Feedback / actuation | Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to ... | p. 7 (Figure/Table caption), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |

## Failure and Ablation Link

- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** The robot's task is to move these cubes into the bowl without colliding with a human's hand moving around in the workspace.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 5: TAMPURA moving cubes into a bowl without hitting a human in the workspace. Top row: images of robot execution. Bottom row: the robot's ...
- **p. 9 / VIII. DISCUSSION - extractive body cue:** Despite these novelties, TAMPURA, and TAMP in general, have several limitations.
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** The primary failure modes were (1) failure in perception (due, we believe, to improperly calibrated hard-coded camera poses), and (2) issues with tension in the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Uncertainty and Risk Aware Task and Motion Planning. (a) The robot's continuous space of probabilistic beliefs about world state is partitioned into a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), objective p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 9 (VII. REAL-WORLD IMPLEMENTATION), temporal p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. RELATED WORK), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 2 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** If the robot believes it has full knowledge of the state and dynamics of the world, it may confidently take actions that have potentially catastrophic effects, and it will never ... (p. 1, I. INTRODUCTION).
- **Objective/update evidence:** In this paper, we focus on planning problems with objectives modeled as goals in belief space (e.g., the goal may be to believe that with high probability the world is ... (p. 4, IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP).
- **Temporal/runtime evidence:** We use Bayes3D perception framework for probabilistic pose inference [29]. (p. 9, VII. REAL-WORLD IMPLEMENTATION).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
