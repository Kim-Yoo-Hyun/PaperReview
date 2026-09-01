# Problem - NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.07896; PDF retrieval source: https://arxiv.org/pdf/2310.07896. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES)): Prior works have often addressed this challenge by training a separate high-level policy or goal proposal system that generates suitable exploratory tasks, for example using high-level planning [1], hierarchical reinforcement ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Robotic learning for navigation in unfamiliar environments needs to provide policies for both task-oriented navigation (i.e., reaching a goal that the robot has located), and ...
- **p. 1 / Abstract - extractive PDF cue:** Typically, these roles are handled by separate models, for example by using subgoal proposals, planning, or separate navigation strategies.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we describe how we can train a single unified diffusion policy to handle both goal-directed navigation and goal-agnostic exploration, with the latter ...
- **p. 1 / Abstract - extractive PDF cue:** We show that this unified policy results in better overall performance when navigating to visually indicated goals in novel environments, as compared to approaches that ...
- **p. 1 / Abstract - extractive PDF cue:** We instantiate our method by using a large-scale Transformerbased policy trained on data from multiple ground robots, with a diffusion model decoder to flexibly handle ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Prior works have often addressed this challenge by training a separate high-level policy or goal proposal system that generates suitable exploratory tasks, for example using ...
- **p. 2 / III. PRELIMINARIES - extractive PDF cue:** While ViNT shows state-of-the-art performance in goal-conditioned navigation, it cannot perform undirected exploration and requires an external subgoal proposal mechanism.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Prior works have often addressed this challenge by training a separate high-level policy or goal proposal system that generates suitable exploratory tasks, ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Our objective is to design a control policy π for visual navigation that takes the robot's current and past RGB observations as ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | objective, design, control, policy, visual, navigation, takes, robot, current, past | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | ViNT, uses, EfficientNet-B0, encoder, process, observation, image, independently | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: objective, design, control, policy, visual, navigation, takes, robot, current, past | p. 2 (III. PRELIMINARIES), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES) |
| Decision / output variable | path/waypoint/velocity; body terms: present, design, policy, combining, Transformer, backbone, encoding, highdimensional | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. METHOD) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: predicted, noise, compared, actual, through, mean, squared, error | p. 4 (IV. METHOD), p. 4 (IV. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD) |
| Success / guarantee | goal reach with collision-free execution | p. 4 (V. EVALUATION), p. 6 (V. EVALUATION), p. 6 (V. EVALUATION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / III. PRELIMINARIES - extractive PDF cue:** While ViNT shows state-of-the-art performance in goal-conditioned navigation, it cannot perform undirected exploration and requires an external subgoal proposal mechanism.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In this work, we study a particularly important instance of this problem in the domain of robotic navigation, where the user might specify a destination ...
- **p. 2 / III. PRELIMINARIES - extractive PDF cue:** Our objective is to design a control policy π for visual navigation that takes the robot's current and past RGB observations as input ot := ...

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 3 (IV. METHOD)): In this paper, we present a design for such a policy by combining a Transformer backbone for encoding the highdimensional stream of visual observations with diffusion models for modeling a ...

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** The main contribution of our work is Navigation with Goal Masked Diffusion, or NoMaD, a novel architecture for robotic navigation in previously unseen environments arXiv:2310.07896v1 ...
- **p. 4 / IV. METHOD - extractive PDF cue:** The noise prediction network, ϵθ, consists of a 1D conditional U-Net [29, 31] with 15 convolutional layers.
- **p. 4 / IV. METHOD - extractive PDF cue:** Note that we model the conditional (and not joint) action distribution, excluding ct from the output of the denoising process, which enables real-time control and ...
- **p. 3 / IV. METHOD - extractive PDF cue:** Training a shared policy across both behaviors allows the model to learn a more expressive prior over actions at, which can be used for both ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | While our experiments provide a proof of concept that unified policies can provide more effective navigation in new ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Exploration with topological maps: While goalconditioned policies can exhibit useful affordances and collision-avoidance behavior, they may be insufficient ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | We report the mean success rate for each baseline, as well as the mean number of collisions per ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Fig. 3: Visualizing the task-agnostic (yellow) and goal-directed pathways for two goal images (green, blue) learned by NoMaD. ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (III. PRELIMINARIES), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 3 (IV. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), interface p. 2 (III. PRELIMINARIES), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 3 (IV. METHOD), objective p. 4 (IV. METHOD), p. 4 (IV. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
