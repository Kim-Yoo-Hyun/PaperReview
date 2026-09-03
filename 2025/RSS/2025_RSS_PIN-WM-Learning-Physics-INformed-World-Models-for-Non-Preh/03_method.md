# Method - PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p153.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p153.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (B. Physics-INformed World Model), p. 3 (B. World Models for Policy Learning), p. 5 (B. Physics-INformed World Model), p. 2 (B. World Models for Policy Learning), p. 2 (B. World Models for Policy Learning), p. 6 (B. Physics-INformed World Model)): We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under global constraints, Here, we use LCP to first ...

## Method Body Digest

- **p. 5 / B. Physics-INformed World Model - extractive body cue:** We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under global constraints, Here, ...
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** DINOWM [84] leverages spatial patch features pre-trained with DINOv2 to learn a world model and achieve task-agnostic behavior planning by treating goal features as prediction ...
- **p. 5 / B. Physics-INformed World Model - extractive body cue:** The transformed observations = {Z(,e¢°)} 4 are then obtained in simulation with Equation 5, where x - G(X+++-1) At+s-1, 8) is the updated state when ...
- **p. 2 / B. World Models for Policy Learning - extractive body cue:** (26) propose Dreamer, a world model that learns compact latent representation of the environment dynamics.
- **p. 2 / B. World Models for Policy Learning - extractive body cue:** World models [25], which learn the environment dynamics in a data-driven manner, provide interactive environments for effective policy training [26, 28].
- **p. 6 / B. Physics-INformed World Model - extractive body cue:** Since we use a velocity-based LCP, the end-effector translation d can be converted into velocity €° - d/H. where 11 is the action time horizon, ...
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** In contrast, PIN-WM enables end-to-end identification of 3D rigid-body dynamics from visual observations using few-shot, task-agnostic interaction data, which facilitates the training of vision-based manipulation ...
- **p. 6 / B. Physics-INformed World Model - extractive body cue:** Where £ is the gravity wrench, Xe, Ao, Ay.y are constraint impulse magnitudes, B is a binary matrix making the equation linearly independent at multiple ...

## Design Rationale

- **p. 2 / 2 Wuhan Universi - extractive body cue:** We introduce PIN-WM, a Physies-INformed World Mode! that allows end-to-end identification of a 3D rigid body ‘dynamical system from visual observations.
- **p. 2 / 2 Wuhan Universi - extractive body cue:** + We conduct real robot implementation to demonstrate that our approach enables learning control policies with minimal task-agnostic interaction data and attains high performance Real2Sim2Real ...
- **p. 3 / C. Domain Randomization - extractive body cue:** We provide an overview of our framework in Figure 2

## Source Evidence Cues

- **p. 5 / B. Physics-INformed World Model - extractive body cue:** We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under global constraints, Here, ...
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** DINOWM [84] leverages spatial patch features pre-trained with DINOv2 to learn a world model and achieve task-agnostic behavior planning by treating goal features as prediction ...
- **p. 5 / B. Physics-INformed World Model - extractive body cue:** The transformed observations = {Z(,e¢°)} 4 are then obtained in simulation with Equation 5, where x - G(X+++-1) At+s-1, 8) is the updated state when ...
- **p. 2 / B. World Models for Policy Learning - extractive body cue:** (26) propose Dreamer, a world model that learns compact latent representation of the environment dynamics.
- **p. 2 / B. World Models for Policy Learning - extractive body cue:** World models [25], which learn the environment dynamics in a data-driven manner, provide interactive environments for effective policy training [26, 28].
- **p. 6 / B. Physics-INformed World Model - extractive body cue:** Since we use a velocity-based LCP, the end-effector translation d can be converted into velocity €° - d/H. where 11 is the action time horizon, ...
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** In contrast, PIN-WM enables end-to-end identification of 3D rigid-body dynamics from visual observations using few-shot, task-agnostic interaction data, which facilitates the training of vision-based manipulation ...
- **Detected method headings:** B. World Models for Policy Learning (p. 2); B. Physics-INformed World Model (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under ... | p. 5 (B. Physics-INformed World Model), p. 3 (B. World Models for Policy Learning) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | DINOWM [84] leverages spatial patch features pre-trained with DINOv2 to learn a world model and achieve task-agnostic behavior planning by treating goal ... | p. 3 (B. World Models for Policy Learning), p. 5 (B. Physics-INformed World Model) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | The transformed observations = {Z(,e¢°)} 4 are then obtained in simulation with Equation 5, where x - G(X+++-1) At+s-1, 8) is the ... | p. 5 (B. Physics-INformed World Model), p. 2 (B. World Models for Policy Learning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / B. Physics-INformed World Model - extractive body cue:** The transformed observations = {Z(,e¢°)} 4 are then obtained in simulation with Equation 5, where x - G(X+++-1) At+s-1, 8) is the updated state when ...
- **p. 5 / B. Physics-INformed World Model - extractive body cue:** We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under global constraints, Here, ...
- **p. 6 / B. Physics-INformed World Model - extractive body cue:** Where £ is the gravity wrench, Xe, Ao, Ay.y are constraint impulse magnitudes, B is a binary matrix making the equation linearly independent at multiple ...
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** Despite those advances, only few studies {53, 5, 67] incorporate physical property estimation into world models for nonprehensile manipulation, relying on gradient-free optimization ‘or simplified ...
- **p. 6 / B. Physics-INformed World Model - extractive body cue:** We propagate recursive derivatives of Equation 11 across H/h simulation time steps and optimize 8.
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** DINOWM [84] leverages spatial patch features pre-trained with DINOv2 to learn a world model and achieve task-agnostic behavior planning by treating goal features as prediction ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 5 (B. Physics-INformed World Model), p. 6 (B. Physics-INformed World Model), p. 5 (B. Physics-INformed World Model), p. 3 (B. World Models for Policy Learning), p. 3 (B. World Models for Policy Learning), p. 4 (B. Physics-INformed World Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Adopting, differentiable, physics, simulation, PIN-WM, learned, few-shot, task-agnostic, physical, interaction, trajectories, observational, loss, induced | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | Adopting, differentiable, physics, simulation, PIN-WM, learned, few-shot, task-agnostic, physical, interaction | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | introduce, PIN-WM, Physies-INformed, World, Mode, allows, end-to-end, identification, rigid, body | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | transformed, observations, then, obtained, simulation, Equation, where, updated, state, when | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** Adopting differentiable physics simulation, PIN-WM can be learned with few-shot and task-agnostic physical interaction trajectories. ‘observational loss induced ‘aussian Splatting without needing state estimation.
- **p. 5 / B. Physics-INformed World Model - extractive body cue:** The transformed observations = {Z(,e¢°)} 4 are then obtained in simulation with Equation 5, where x - G(X+++-1) At+s-1, 8) is the updated state when ...
- **p. 14 / A. Implementation Details for Baselines - extractive body cue:** A history of recent states and actions is used as input for the "Domain Rand + Z" (denoted as DR) baseline [60].
- **p. 1 / Abstract - extractive body cue:** To achieve robust policy learning and generalization, we opt to learn a world model of the 3D rigid body dynamics involved in nonprehensile manipulations and ...
- **p. 4 / 20 Gaussian Slats - extractive body cue:** where g, parameterized by 8, predicts the next state x from ‘current state x; and action a;, and Z, parameterized by 4, generates the image ...
- **p. 5 / B. Physics-INformed World Model - extractive body cue:** next object pose x1 based on current state x+ and action ay.
- **p. 6 / B. Physics-INformed World Model - extractive body cue:** Moreover, in robot manipulation, the action time horizon 11 is usually inequivalent to simulation step size h, while the latter is set small ‘enough to ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | Where t denotes the time step and w represents the learnable parameters. | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | We propagate recursive derivatives of Equation 11 across H/h simulation time steps and optimize 8. | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / B. Physics-INformed World Model - extractive body cue:** We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under global constraints, Here, ...
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** DINOWM [84] leverages spatial patch features pre-trained with DINOv2 to learn a world model and achieve task-agnostic behavior planning by treating goal features as prediction ...
- **p. 2 / B. World Models for Policy Learning - extractive body cue:** World models [25], which learn the environment dynamics in a data-driven manner, provide interactive environments for effective policy training [26, 28].
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** In contrast, PIN-WM enables end-to-end identification of 3D rigid-body dynamics from visual observations using few-shot, task-agnostic interaction data, which facilitates the training of vision-based manipulation ...
- **p. 14 / A. Implementation Details for Baselines - extractive body cue:** All RL-based policies are trained using PPO [66], with the same model architecture, reward function, hyperparameters, and stopping criterion based on the success rate.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** formulate, system, identification, process, velocity-based, Linear, Complementarity, Problem, LCP, solves, equations, motion, under, global, constraints, Here, first, estimate, then, further.
- **Relevant PDF headings:** B. World Models for Policy Learning (p. 2); B. Physics-INformed World Model (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | Experiment setup: n simulation, we collect a single task-agnostc trajectory thatthe target object is pushed forward along a straight line by the ... | p. 7 (A. Evaluations in Simulation), p. 8 (B. Evaluations in Real-World) |
| Filtering / recovery | Note that all physics-based methods being compared are trained with the same task-agnostic trajectories as PIN-WM, for fair comparison. | p. 7 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation) |
| Monitoring / re-entry | All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain ... | p. 7 (A. Evaluations in Simulation), p. 8 (A. Evaluations in Simulation) |

## Failure and Ablation Link

- **p. 7 / A. Evaluations in Simulation - extractive body cue:** All policies are trained until no significant success rate performance can be gained and are then deployed directly to the target domain for evaluation, We ...
- **p. 7 / A. Evaluations in Simulation - extractive body cue:** We set a variant with fixed, random physics and rendering parameters where no system identification or randomization is involved, denoted as Random.
- **p. 8 / A. Evaluations in Simulation - extractive body cue:** Without PADC, our method still outperforms others, although with a performance decrease.
- **p. 14 / A. Implementation Details for Baselines - extractive body cue:** Diffusion Policy is trained with successful trajectories collected from ‘expert policies trained in the environment with GT physical parameters, without any randomization,
- **p. 7 / A. Evaluations in Simulation - extractive body cue:** Since neither of the two methods learns rendering parameters and their trained policies cannot work without aligned visual input, we add our rendering function Z ...
- **p. 8 / A. Evaluations in Simulation - extractive body cue:** The purely data-driven world model Dreamer V2 [27], albeit having access to more task-agnostic data, fails to accurately approximate the dynamics of the target domain, ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 10: Push cube object on a slippery plane.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (B. Physics-INformed World Model), p. 3 (B. World Models for Policy Learning), p. 5 (B. Physics-INformed World Model), p. 2 (B. World Models for Policy Learning), p. 2 (B. World Models for Policy Learning), p. 6 (B. Physics-INformed World Model), objective p. 5 (B. Physics-INformed World Model), p. 5 (B. Physics-INformed World Model), p. 6 (B. Physics-INformed World Model), p. 3 (B. World Models for Policy Learning), p. 6 (B. Physics-INformed World Model), p. 3 (B. World Models for Policy Learning), temporal p. 3 (C. Domain Randomization), p. 6 (B. Physics-INformed World Model), p. 6 (IV. RESULTS AND EVALUATIONS), p. 7 (A. Evaluations in Simulation), p. 7 (A. Evaluations in Simulation), p. 8 (B. Evaluations in Real-World).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** In contrast, PIN-WM enables end-to-end identification of 3D rigid-body dynamics from visual observations using few-shot, task-agnostic interaction data, which facilitates the training of vision-based manipulation policies with RL. (p. 3, B. World Models for Policy Learning).
- **Objective/update evidence:** We formulate this system identification process as a velocity-based Linear Complementarity Problem (LCP) [16, 68] which solves the equations of motion under global constraints, Here, we use LCP to first ... (p. 5, B. Physics-INformed World Model).
- **Temporal/runtime evidence:** ‘We evaluate our method on rigid body motion control. ‘The robot's objective is to perform a sequence of non-prehensile actions to move an object into a target pose. (p. 6, IV. RESULTS AND EVALUATIONS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
