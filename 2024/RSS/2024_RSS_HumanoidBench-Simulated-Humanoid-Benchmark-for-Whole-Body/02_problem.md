# Problem - HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p061.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p061.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (I. INTRODUCTION)): However, all these works focus fon demonstrating their approaches on specific humanoid tasks and lack a diversity of tasks.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Humanoid robots hold great promise in assisting ‘humans in diverse environments and tasks, due to their flexibility and adaptability leveraging human-like morphology.
- **p. 1 / Abstract - extractive body cue:** However, research in humanoid robots is often bottlenecked by the costly and fragile hardware setups.
- **p. 1 / Abstract - extractive body cue:** To aecelerate algorithmic research in humanoid robots, we present a high-dimensional, simulated robot learning henchmark, HumanoidBench, featuring a humanoid robot equipped with dexterous hands and ...
- **p. 1 / Abstract - extractive body cue:** With HumanoidBench, we provide the robotics community with a platform to identify the challenges arising when solving diverse tasks with humanoid robots, facilitating prompt verification ...
- **p. 1 / Abstract - extractive body cue:** The open-source code is available at ‘hupst//humanold-bench.github.io.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, all these works focus fon demonstrating their approaches on specific humanoid tasks and lack a diversity of tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, most of these benchmarks use a singlearm manipulation setup with either a parallel gripper or a dexterous hand [9, 49], limiting the types of ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, all these works focus fon demonstrating their approaches on specific humanoid tasks and lack a diversity of tasks. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | + Proprioceptive robot state (i, joint angles and velocities) and task-relevant environment observations (ie, object, poses and velocities) | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | Proprioceptive, robot, state, joint, angles, velocities, task-relevant, environment, observations, object | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | present, extensive, benchmarking, state-of-the-art, reinforcement, leaning, algorithms, require | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: Proprioceptive, robot, state, joint, angles, velocities, task-relevant, environment, observations, object | p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Decision / output variable | method trajectory/action; body terms: accelerate, progress, research, humanoid, robots, present, first-of-its-kind, robot | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: represent, standard, deviation, Returns, computed, summing, rewards, timesteps | p. 2 (I. INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 5 (IV. HuMANOIDBENcH) |
| Success / guarantee | comparable score and protocol validity | p. 8 (B. Results), p. 9 (B. Results), p. 7 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, most of these benchmarks use a singlearm manipulation setup with either a parallel gripper or a dexterous hand [9, 49], limiting the types of ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our simulated humanoid benchmark demonstrates a variety of challenges in addressing learning for autonomous humanoid robots, such as the intricate control of robots with, complex ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Although other sensory inputs are available from the environment, to investigate challenges in whole-body control of humanoid robots, we first focus on the state-based environment ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** We devise 15 benchmarking whole-body manipulation tasks that cover a wide variety of interactions and difficulties.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (I. INTRODUCTION)): To accelerate the progress of research for humanoid robots, We present the first-of-its-kind humanoid robot benchmark, HumanoidBench, with a diverse set of locomotion and manipulation tasks.

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present extensive benchmarking results of the state-of-the-art reinforcement leaning (RL) algorithms, which do not require extensive domain knowledge, and a hierarchical ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 4, 42, 29, 17, 30, 48] In the context of humanoids, we propose an HRL paradigm
- **p. 3 / I. INTRODUCTION - extractive body cue:** While this is not currently a realistic model, we anticipate the trend in the industry towards developing slimmer, human-like hhands (e-g., Tesla Optimus, Figure 01) ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** Torque-based control is also supported but we found that position control is generally more stable and allows for lower control frequency than torque control.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Fig. 10: Failure Scenarios. This figure presents a selection of common failures that occur while training our benchmark ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | For low-level reaching policy training, we employ a simplified Hi model that only considers collisions between feet and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Remarkably, this class of algorithms requires limited domain expertise and does not necessarily rely fon expert demonstrations, which ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (I. INTRODUCTION), interface p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (Abstract), objective p. 2 (I. INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
