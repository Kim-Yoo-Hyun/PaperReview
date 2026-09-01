# Problem - ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.11575; PDF retrieval source: https://arxiv.org/pdf/2602.11575. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Such limitations make it difficult to learn safe navigation in the presence of dynamic obstacles and to render photorealistic human appearances within reconstructed real-world environments.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Visual navigation models often struggle in realworld dynamic environments due to limited robustness to the sim-to-real gap and the difficulty of training policies tailored to ...
- **p. 1 / Abstract - extractive PDF cue:** Although real-to-sim navigation simulation using 3D Gaussian Splatting (GS) can mitigate these challenges, prior GS-based works have considered only static scenes or non-photorealistic human obstacles ...
- **p. 1 / Abstract - extractive PDF cue:** To address these issues, we propose ReaDy-Go, a novel real-to-sim simulation pipeline that synthesizes photorealistic dynamic scenarios in target environments by augmenting a reconstructed static ...
- **p. 1 / Abstract - extractive PDF cue:** The pipeline provides three key contributions: (1) a dynamic GS simulator that integrates static scene GS with a human animation module, enabling the insertion of ...
- **p. 1 / Abstract - extractive PDF cue:** ReaDy-Go outperforms baselines across target environments in both simulation and real-world experiments, demonstrating improved navigation performance even after sim-to-real transfer and in the presence of ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Such limitations make it difficult to learn safe navigation in the presence of dynamic obstacles and to render photorealistic human appearances within reconstructed real-world environments.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, the resulting sim-toreal distribution gap significantly degrades performance during deployment.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Such limitations make it difficult to learn safe navigation in the presence of dynamic obstacles and to render photorealistic human appearances within ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | By leveraging the simulator and planners, the pipeline collects RGB observations, actions, and relative goal positions as training samples for a navigation ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | leveraging, simulator, planners, pipeline, collects, RGB, observations, actions, relative, goal | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | RGB-only, navigation, models, typically, learn, nonlinear, visuomotor, policies | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: leveraging, simulator, planners, pipeline, collects, RGB, observations, actions, relative, goal | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: framework, consists, three, components, dynamic, simulator, integrates, static | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Specifically, employed, PGSR, scene, reconstruction, achieves, high-quality, surface | p. 3 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHOD) |
| Success / guarantee | goal reach with collision-free execution | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, the resulting sim-toreal distribution gap significantly degrades performance during deployment.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Motivated by these limitations, we propose ReaDy-Go, a photorealistic Real-to-Sim Dynamic 3D Gaussian Splatting Simulation pipeline for environment-specific RGB-only visual navigation with moving obstacles (Fig.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Furthermore, it shows generalization potential via zeroshot sim-to-real deployment in an unseen environment.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD)): The framework consists of three key components: (1) a dynamic GS simulator that integrates a static scene GS, an animatable human GS obstacle, and a human motion generation module, enabling ...

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** By reconstructing environments from RGB videos, GS enables high-fidelity rendering at fast frame rates, novel view synthesis, and simulation with an explicit 3D scene representation.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Our contributions are threefold. • Dynamic GS Simulator: We develop a photorealistic realto-sim dynamic 3D Gaussian Splatting simulator with human GS obstacles.
- **p. 3 / III. METHOD - extractive PDF cue:** GS is a representation that enables 3D geometry reconstruction, high-fidelity novel view synthesis, and fast training and rendering by fitting positions, rotations, scales, opacities, and ...
- **p. 3 / III. METHOD - extractive PDF cue:** The pipeline consists of three main components: (1) a real-to-sim dynamic 3D Gaussian Splatting (GS) simulator, (2) dynamic navigation dataset generation using the simulator and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | ReaDy-Go yields fewer failures than the baselines, especially in failure modes related to dynamic obstacle avoidance, including Dynamic ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Second, while ReaDy-Go and Vid2Sim showed similar numbers of failures in cases unrelated to dynamic obstacle interactions, ReaDy-Go ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Fig. 3: Visualization of the robot expert planner. (a) The robot follows a collision-free path (red) from start ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | The robot should reach the goal without collisions within the scenario time limit. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 4 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), objective p. 3 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
