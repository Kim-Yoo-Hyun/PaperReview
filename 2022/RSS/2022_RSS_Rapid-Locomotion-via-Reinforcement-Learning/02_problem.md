# Problem - Rapid Locomotion via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss18/p022.html; PDF retrieval source: https://arxiv.org/pdf/2205.02824. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Task difficulty is a function of both the system dynamics and the optimization algorithm, making manual curriculum design tedious and problem-dependent.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Agile maneuvers such as sprinting and high-speed turning in the wild are challenging for legged robots.
- **p. 1 / Abstract - extractive PDF cue:** We present an end-to-end learned controller that achieves record agility for the MIT Mini Cheetah, sustaining speeds up to 3.9 m/s.
- **p. 1 / Abstract - extractive PDF cue:** This system runs and turns fast on natural terrains like grass, ice, and gravel and responds robustly to disturbances.
- **p. 1 / Abstract - extractive PDF cue:** Our controller is a neural network trained in simulation via reinforcement learning and transferred to the real world.
- **p. 1 / Abstract - extractive PDF cue:** The two key components are (i) an adaptive curriculum on velocity commands and (ii) an online system identification strategy for sim-to-real transfer leveraged from prior ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Task difficulty is a function of both the system dynamics and the optimization algorithm, making manual curriculum design tedious and problem-dependent.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** However, increasing the range of commanded velocities to include high speeds results in training failure.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Task difficulty is a function of both the system dynamics and the optimization algorithm, making manual curriculum design tedious and problem-dependent. | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | Our goal is to learn a policy πθ(.) with parameters θ that takes as input sensory data and velocity commands and gives ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF |
| State / latent | goal, learn, policy, parameters, takes, input, sensory, data, velocity, commands | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | policy, tasked, follow, range, velocity, commands, generated, curriculum | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: goal, learn, policy, parameters, takes, input, sensory, data, velocity, commands | p. 2 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Decision / output variable | joint action/torque/footstep; body terms: algorithms, Equal, contribution, end-to-end, learned, controller, enables, MIT | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: policy, commonly, referred, teacher, trained, algorithm, maximize, expected | p. 3 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Success / guarantee | progress, balance and terrain robustness | p. 5 (Figure/Table caption), p. 5 (IV. RESULTS), p. 6 (IV. RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** However, increasing the range of commanded velocities to include high speeds results in training failure.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** How can we perform real-time control in complex environments where efficient reduced-order models may not exist or are currently unknown?
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** The problem is that trajectory optimization with a full model is not possible in real-time for a complex task such as fast running on natural ...

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION)): RL algorithms * Equal contribution.

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** 1: An end-to-end learned controller enables the MIT Mini Cheetah to execute: (a) fast sprinting at 3.9 m/s (top); (b) a rough terrain 10-meter sprint ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** The same policy can spin the robot at 5.7 rad/s on flat ground and also enables the robot to spin on the more challenging icy ...
- **p. 3 / III. METHOD - extractive PDF cue:** Teacher-student training enables the agent to specialize its behavior to the current dynamics dt, instead of learning a single behavior that works across different dt.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** We show that reinforcement learning can be used to learn locomotion controllers that simultaneously achieve linear and angular high-speed behaviors and operate on diverse natural ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Our system also does not use vision, so in general, it cannot perform tasks that require planning ahead ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We cannot use motion capture to record the robot's state outdoors as we do in the lab. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Response to Terrain Changes and Hardware Failures We tested our system in a diverse set of challenging real-world ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | While these results highlight the robustness of policies, we want to emphasize that we are not claiming that ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 2 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), objective p. 3 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
