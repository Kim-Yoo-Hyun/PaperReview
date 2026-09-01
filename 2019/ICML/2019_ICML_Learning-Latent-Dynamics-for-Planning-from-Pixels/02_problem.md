# Problem - Learning Latent Dynamics for Planning from Pixels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1811.04551; PDF retrieval source: https://arxiv.org/pdf/1811.04551. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Planning has been very successful for control tasks with known environment dynamics.
- **p. 1 / Abstract - extractive body cue:** To leverage planning in unknown environments, the agent needs to learn the dynamics from interactions with the world.
- **p. 1 / Abstract - extractive body cue:** However, learning dynamics models that are accurate enough for planning has been a long-standing challenge, especially in image-based domains.
- **p. 1 / Abstract - extractive body cue:** We propose the Deep Planning Network (PlaNet), a purely model-based agent that learns the environment dynamics from images and chooses actions through fast online planning ...
- **p. 1 / Abstract - extractive body cue:** To achieve high performance, the dynamics model must accurately predict the rewards ahead for multiple time steps.
- **p. 1 / 1. Introduction - extractive body cue:** Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the training distribution.
- **p. 1 / 1. Introduction - extractive body cue:** PlaNet solves continuous control tasks from pixels that are more difficult than those previously solved by planning with learned models.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Key difficulties include model inaccuracies, accumulating errors of multi-step predictions, failure to capture multiple possible futures, and overconfident predictions outside of the ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | We define a discrete time step t, hidden states st, image observations ot, continuous action vectors at, and scalar rewards rt, that ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF |
| State / latent | define, discrete, time, step, hidden, states, image, observations, continuous, action | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | Problem, setup, Since, individual, image, observations, generally, reveal | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: define, discrete, time, step, hidden, states, image, observations, continuous, action | p. 2 (2. Latent Space Planning), p. 3 (3. Recurrent State Space Model), p. 2 (2. Latent Space Planning) |
| Decision / output variable | filtered/recovery action u_safe; body terms: Deep, Planning, Network, PlaNet, model-based, agent, learns, environment | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (2. Latent Space Planning) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: CEM, populationbased, optimization, algorithm, infers, distribution, over, action | p. 2 (2 Initialize model parameters θ randomly), p. 4 (3. Recurrent State Space Model), p. 2 (2. Latent Space Planning), p. 3 (2 Initialize model parameters θ randomly), p. 3 (3. Recurrent State Space Model), p. 4 (3. Recurrent State Space Model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (2 Initialize model parameters θ randomly), p. 3 (3. Recurrent State Space Model), p. 4 (3. Recurrent State Space Model) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 6 (5. Experiments), p. 7 (Figure/Table caption), p. 19 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** PlaNet solves continuous control tasks from pixels that are more difficult than those previously solved by planning with learned models.
- **p. 2 / 1. Introduction - extractive body cue:** (f) The walker task requires balance and predicting difficult interactions with the ground when the robot is lying down. its latent space.
- **p. 2 / 1. Introduction - extractive body cue:** Our experiments indicate having both components to be crucial for high planning performance. • Latent overshooting We generalize the standard variational bound to include multi-step ...

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (2. Latent Space Planning), p. 3 (2 Initialize model parameters θ randomly)): In this paper, we propose the Deep Planning Network (PlaNet), a model-based agent that learns the environment dynamics from pixels and chooses actions through online planning in a compact latent ...

- **p. 1 / 1. Introduction - extractive body cue:** Key contributions of this work are summarized as follows: • Planning in latent spaces We solve a variety of tasks from the DeepMind control suite, ...
- **p. 2 / 2. Latent Space Planning - extractive body cue:** In this section, we introduce notation for the environment and describe the general implementation of our model-based agent.
- **p. 3 / 2 Initialize model parameters θ randomly - extractive body cue:** Because the reward is modeled as a function of the latent state, the planner can operate purely in latent space without generating images, which allows ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Directions for future work include learning temporal abstraction instead of using a fixed action repeat, possibly through hierarchical ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The cartpole swingup task requires a long planning horizon and to memorize the cart when it is out ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The noise might also add a safety margin to the planning objective that results in more robust action ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Figure 4: Comparison of PlaNet to model-free algorithms and other model designs. Plots show test performance over the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (2. Latent Space Planning), p. 3 (3. Recurrent State Space Model), p. 2 (2. Latent Space Planning), p. 3 (2 Initialize model parameters θ randomly). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (2. Latent Space Planning), p. 3 (3. Recurrent State Space Model), p. 2 (2. Latent Space Planning), p. 3 (2 Initialize model parameters θ randomly), objective p. 2 (2 Initialize model parameters θ randomly), p. 4 (3. Recurrent State Space Model), p. 2 (2. Latent Space Planning), p. 3 (2 Initialize model parameters θ randomly), p. 3 (3. Recurrent State Space Model), p. 4 (3. Recurrent State Space Model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
