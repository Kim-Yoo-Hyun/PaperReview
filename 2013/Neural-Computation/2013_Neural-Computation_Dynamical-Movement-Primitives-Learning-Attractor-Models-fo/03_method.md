# Method - Dynamical Movement Primitives: Learning Attractor Models for Motor Behaviors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (47 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://is.mpg.de/ics/publications/ijspeert_nc_2013; PDF retrieval source: https://www.pure.ed.ac.uk/ws/portalfiles/portal/7874487/NECO_a_00393.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 6 (2 A Learnable Nonlinear Attractor Systems)): Thus, as a novel component, we introduce a replacement of time by means of the following first-order linear dynamics in x τ ˙x = -αxx, (2.2) where αx is a ...

## Method Body Digest

- **p. 6 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** Thus, as a novel component, we introduce a replacement of time by means of the following first-order linear dynamics in x τ ˙x = -αxx, ...
- **p. 4 / 1 Introduction - extractive PDF cue:** The following sections first introduce our modeling approach (see section 1), then, examine its theoretical properties (see section 2), and finally explore our approach in ...
- **p. 3 / 1 Introduction - extractive PDF cue:** In order to allow investigations of such second objectives, a dynamical systems model has to be found first.
- **p. 4 / 1 Introduction - extractive PDF cue:** We evaluate our approach in the domain of motor control for robotics, where desired kinematic motor behaviors will be coded in attractor landscapes and then ...
- **p. 3 / 1 Introduction - extractive PDF cue:** In this letter, we propose a generic modeling approach to generate multidimensional systems of weakly nonlinear differential equations to 1With low-dimensional, we refer to systems ...
- **p. 6 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** Since the forcing term is chosen to be nonlinear in the state of the differential equations and since it transforms the simple dynamics of the ...
- **p. 5 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** As one of the simplest possible systems, we chose a damped spring model,4 τ ¨y = αz(βz(g -y) -˙y) + f, which, throughout this letter, ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Such behaviors are goal oriented; the focus is less on emergent coordination phenomena and more on achieving a task objective.

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** In this letter, we propose a generic modeling approach to generate multidimensional systems of weakly nonlinear differential equations to 1With low-dimensional, we refer to systems ...
- **p. 4 / 1 Introduction - extractive PDF cue:** The essence of our methodology is to transform well-understood simple attractor systems with the help of a learnable forcing function term into a desired attractor ...
- **p. 6 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** Thus, as a novel component, we introduce a replacement of time by means of the following first-order linear dynamics in x τ ˙x = -αxx, ...

## Source Evidence Cues

- **p. 6 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** Thus, as a novel component, we introduce a replacement of time by means of the following first-order linear dynamics in x τ ˙x = -αxx, ...
- **p. 4 / 1 Introduction - extractive PDF cue:** The following sections first introduce our modeling approach (see section 1), then, examine its theoretical properties (see section 2), and finally explore our approach in ...
- **p. 3 / 1 Introduction - extractive PDF cue:** In order to allow investigations of such second objectives, a dynamical systems model has to be found first.
- **p. 4 / 1 Introduction - extractive PDF cue:** We evaluate our approach in the domain of motor control for robotics, where desired kinematic motor behaviors will be coded in attractor landscapes and then ...
- **p. 3 / 1 Introduction - extractive PDF cue:** In this letter, we propose a generic modeling approach to generate multidimensional systems of weakly nonlinear differential equations to 1With low-dimensional, we refer to systems ...
- **p. 6 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** Since the forcing term is chosen to be nonlinear in the state of the differential equations and since it transforms the simple dynamics of the ...
- **p. 5 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** As one of the simplest possible systems, we chose a damped spring model,4 τ ¨y = αz(βz(g -y) -˙y) + f, which, throughout this letter, ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / error representation | motion·force 목표를 제어 error로 바꾼다 | joint/task state, reference, wrench | task frame, Jacobian, impedance, selection 또는 error coordinates를 구성 | desired task command | Thus, as a novel component, we introduce a replacement of time by means of the following first-order linear dynamics in x τ ... | p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 4 (1 Introduction) |
| Dynamics / constraint solve | 목표를 feasible actuator command로 바꾼다 | error, model, constraints | inverse dynamics, QP, MPC, operational mapping 또는 feedback law를 계산 | torque, force, velocity 또는 position command | The following sections first introduce our modeling approach (see section 1), then, examine its theoretical properties (see section 2), and finally explore ... | p. 4 (1 Introduction), p. 3 (1 Introduction) |
| Feedback / actuation | 실제 state와 disturbance에 따라 command를 닫힌 loop로 보정한다 | sensor feedback과 nominal command | tracking correction, saturation, null-space, fallback 또는 replan을 수행 | next actuation과 response | In order to allow investigations of such second objectives, a dynamical systems model has to be found first. | p. 3 (1 Introduction), p. 4 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 1 Introduction - extractive PDF cue:** In order to allow investigations of such second objectives, a dynamical systems model has to be found first.
- **p. 3 / 1 Introduction - extractive PDF cue:** Such behaviors are goal oriented; the focus is less on emergent coordination phenomena and more on achieving a task objective.
- **p. 4 / 1 Introduction - extractive PDF cue:** Stability of the model equations can be guaranteed.
- **p. 4 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** Before developing our model equations, it will be useful to clarify the specific goals pursued with this model: 1.
- **p. 5 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** This notation should not be confused with discrete dynamical systems, which denotes difference equations-those that are time discretized.
- **p. 5 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** If the forcing term f = 0, these equations represent a globally stable second-order linear system with (z, y) = (0, g) as a unique ...
- **Formal bridge:** q, q̇, x, wrench -> u/τ subject to dynamics and actuator/contact constraints -> tracking or interaction error -> stability, tracking and constraint satisfaction.
- **Equation/algorithm anchors:** p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (2 A Learnable Nonlinear Attractor Systems), p. 5 (2 A Learnable Nonlinear Attractor Systems), p. 5 (2 A Learnable Nonlinear Attractor Systems).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Since, forcing, term, chosen, nonlinear, state, differential, equations, transforms, simple, dynamics, unforced, systems, desired | joint/task state, reference와 sensor feedback | body cue; exact tensor/frame verify |
| State/latent | Since, forcing, term, chosen, nonlinear, state, differential, equations, transforms, simple | state estimate, task-space error와 control decision | body cue; notation verify |
| Action/output | letter, generic, modeling, generate, multidimensional, systems, weakly, nonlinear, differential, equations | torque, force, velocity 또는 position command | body cue; unit/decoder verify |
| Objective/constraint | order, allow, investigations, second, objectives, dynamical, systems, model, found, first | tracking or interaction error | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** Since the forcing term is chosen to be nonlinear in the state of the differential equations and since it transforms the simple dynamics of the ...
- **p. 6 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** Starting from some arbitrarily chosen initial state x0, such as x0 = 1, the state x converges monotonically to zero. x can thus be conceived ...
- **p. 8 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** To start the time evolution of the equations, the goal is set to g = 1, and the canonical system state is initialized to x ...
- **p. 8 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** As shown in the vector field plots of Figure 2, at every moment of time (represented by the phase variable x), there is an attractor ...
- **p. 5 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** The system needs to be able to incorporate coupling terms, for example, as typically used in synchronization studies or phase resetting studies and as needed ...
- **p. 7 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** Given that equation 2.2 is a linear differential equation, there exists a simple exponential function that relates time and the state x of this equation.
- **p. 7 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** With equation 2.2, we can reformulate our forcing term to become f (x) = N i=1 i(x)wi N i=1 i(x) x(g -y0) (2.3) with N ...
- **Normalized interface:** observation=joint/task state, reference와 sensor feedback; state=state estimate, task-space error와 control decision; output/action=torque, force, velocity 또는 position command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instantaneous or receding-horizon reference tracking; exact prediction horizon은 exact value not recovered from the selected body cues. | We will discuss imitation learning of discrete and rhythmic movement, online modulation with the help of coupling terms, synchronization and entrainment phenomena, ... | episode/sequence/action-chunk boundary |
| Rate / latency | sensor/actuator control tick마다 feedback solve; numeric rate는 paper-specific. | Those online modulations are among the most important properties offered by a dynamical systems approach, and these properties cannot easily be replicated ... | Hz/fps, inference time and control rate |
| Memory | 현재 joint/task state, reference, contact/wrench feedback; long history 여부 확인 필요. | not recovered | window and reset |
| Compute | dynamics/Jacobian evaluation, QP/MPC/inverse-dynamics solve와 actuator latency가 결정한다. | Afterward, we had the external metronome pace increase frequency slowly to 0.5 Hz to demonstrate the continuous adaptation ability of the oscillator. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 1 Introduction - extractive PDF cue:** In this letter, we propose a generic modeling approach to generate multidimensional systems of weakly nonlinear differential equations to 1With low-dimensional, we refer to systems ...
- **p. 6 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** Since the forcing term is chosen to be nonlinear in the state of the differential equations and since it transforms the simple dynamics of the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Thus, novel, component, introduce, replacement, time, means, following, first-order, linear, dynamics, where, constant, sections, first, modeling, section, then, examine, theoretical.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / error representation | In the next sections, we present and review several experimental evaluations of applying our approach to learning attractor systems in the domain ... | p. 22 (3 Evaluations), p. 22 (3 Evaluations) |
| Dynamics / constraint solve | The design parameters of the rhythmic system are g, the baseline of the oscillation; τ, the period divided by 2π; and r, ... | p. 23 (3 Evaluations), p. 33 (Figure/Table caption) |
| Feedback / actuation | Within two beats (the time needed to extract the frequency from the acoustic signal), perfect synchronization and phase locking is achieved with ... | p. 29 (3 Evaluations), p. 30 (3 Evaluations) |

## Failure and Ablation Link

- **p. 24 / 3 Evaluations - extractive PDF cue:** Those online modulations are among the most important properties offered by a dynamical systems approach, and these properties cannot easily be replicated without the attractor ...
- **p. 26 / 3 Evaluations - extractive PDF cue:** By modulating the canonical system, one can influence the temporal evolution of our dynamical systems without affecting
- **p. 29 / 3 Evaluations - extractive PDF cue:** Without coupling terms, the dynamical system would just continue its time evolution, regardless of what happens to the point mass.
- **p. 30 / 3 Evaluations - extractive PDF cue:** Without the coupling terms, y would already have evolved all the way to the goal position, and the error between ya and y would have ...
- **p. 30 / 3 Evaluations - extractive PDF cue:** Essentially the perturbation simply delays the time evolution of the dynamical system without any large motor commands leading to possible harm. system, that is, both ...
- **p. 24 / 3 Evaluations - extractive PDF cue:** Those online modulations are among the most important properties offered by a dynamical systems approach, and these properties cannot easily be replicated without the attractor ...
- **p. 26 / 3 Evaluations - extractive PDF cue:** Trajectories starting at points where the direct line to the goal does not intersect with the obstacle are only minimally curved around the obstacle, while ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 6 (2 A Learnable Nonlinear Attractor Systems), objective p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (2 A Learnable Nonlinear Attractor Systems), p. 5 (2 A Learnable Nonlinear Attractor Systems), p. 5 (2 A Learnable Nonlinear Attractor Systems), temporal p. 22 (3 Evaluations), p. 24 (3 Evaluations), p. 29 (3 Evaluations), p. 29 (3 Evaluations), p. 8 (2 A Learnable Nonlinear Attractor Systems), p. 16 (2.1.3 Stability Properties. Stability of our dynamical systems equations).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
