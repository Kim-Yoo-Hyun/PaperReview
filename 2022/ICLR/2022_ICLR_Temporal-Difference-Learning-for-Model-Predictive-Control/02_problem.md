# Problem - Temporal Difference Learning for Model Predictive Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.04955; PDF retrieval source: https://arxiv.org/pdf/2203.04955. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction)): To overcome these challenges, we make three key changes to model learning.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Data-driven model predictive control has two key advantages over model-free methods: a potential for improved sample efficiency through model learning, and better performance as computational ...
- **p. 1 / Abstract - extractive body cue:** However, it is both costly to plan over long horizons and challenging to obtain an accurate model of the environment.
- **p. 1 / Abstract - extractive body cue:** In this work, we combine the strengths of model-free and model-based methods.
- **p. 1 / Abstract - extractive body cue:** We use a learned task-oriented latent dynamics model for local trajectory optimization over a short horizon, and use a learned terminal value function to estimate ...
- **p. 1 / Abstract - extractive body cue:** Our method, TD-MPC, achieves superior sample efficiency and asymptotic performance over prior work on both state and image-based continuous control tasks from DMControl and MetaWorld.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these challenges, we make three key changes to model learning.
- **p. 2 / 1. Introduction - extractive body cue:** While prior work learns a model through state or video prediction, we argue that it is remarkably inefficient to model everything in the environment, including ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To overcome these challenges, we make three key changes to model learning. | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | (2015)) control for planning (denoted Πθ), learned models dθ, Rθ of the (latent) dynamics and reward signal, respectively, a terminal state-action value ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF body |
| State / latent | control, planning, denoted, learned, models, latent, dynamics, reward, signal, respectively | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | Instead, regularize, TOLD, latent, state, consistency, loss, Equation | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: control, planning, denoted, learned, models, latent, dynamics, reward, signal, respectively | p. 3 (3. TD-Learning for Model Predictive Control), p. 3 (3. TD-Learning for Model Predictive Control), p. 5 (4. Task-Oriented Latent Dynamics Model) |
| Decision / output variable | filtered/recovery action u_safe; body terms: Top, present, framework, MPC, task-oriented, latent, dynamics, model | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: During, training, minimize, temporally, weighted, objective, i-tL, where | p. 4 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 3 (3. TD-Learning for Model Predictive Control), p. 3 (3. TD-Learning for Model Predictive Control), p. 4 (4. Task-Oriented Latent Dynamics Model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. TD-Learning for Model Predictive Control), p. 4 (4. Task-Oriented Latent Dynamics Model), p. 3 (3. TD-Learning for Model Predictive Control) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 8 (5. Experiments), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** While prior work learns a model through state or video prediction, we argue that it is remarkably inefficient to model everything in the environment, including ...
- **p. 1 / 1. Introduction - extractive body cue:** Concretely, prior work on model-based methods can largely be subdivided into two directions, each exploiting key ad
- **p. 1 / 1. Introduction - extractive body cue:** Planning is a powerful approach to such sequential decision making problems, and has achieved tremendous success in application areas such as game-playing (Kaiser et al., ...

## What the Paper Changes

PDF body contribution framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. TD-Learning for Model Predictive Control)): (Top) We present a framework for MPC using a task-oriented latent dynamics model and value function learned jointly by temporal difference learning.

- **p. 1 / 1. Introduction - extractive body cue:** (Bottom) Episode return of our method, SAC, and MPC with a ground-truth simulator on challenging, highdimensional Humanoid and Dog tasks (Tassa et al., 2018).
- **p. 2 / 1. Introduction - extractive body cue:** Lastly, we propose a modality-agnostic prediction loss in latent space that enforces temporal consistency in the learned representation without explicit state or image prediction.
- **p. 2 / 1. Introduction - extractive body cue:** In particular, our method solves Humanoid and Dog locomotion tasks with up to 38-dimensional continuous action spaces in as little as 1M environment steps (see ...
- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** We summarize our framework in Figure 1 and Algorithm 1.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Due to dimensionality explosion under discretization, MuZero and EfficientZero cannot feasibly solve tasks with higher-dimensional action spaces, e.g., ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Mean of 5 runs. have access to the egocentric camera fails. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Performance of LOOP is similar to SAC, and MPC with a simulator (MPC:sim) performs well on locomotion tasks ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3. TD-Learning for Model Predictive Control), p. 3 (3. TD-Learning for Model Predictive Control), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 2 (2. Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 3 (3. TD-Learning for Model Predictive Control), p. 3 (3. TD-Learning for Model Predictive Control), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 2 (2. Preliminaries), objective p. 4 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 3 (3. TD-Learning for Model Predictive Control), p. 3 (3. TD-Learning for Model Predictive Control), p. 4 (4. Task-Oriented Latent Dynamics Model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
