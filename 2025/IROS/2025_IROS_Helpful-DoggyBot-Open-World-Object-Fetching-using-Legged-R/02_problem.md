# Problem - Helpful DoggyBot: Open-World Object Fetching using Legged Robots and Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.00231; PDF retrieval source: https://arxiv.org/pdf/2410.00231. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): In this paper, we present Helpful DoggyBot, a quadrupedal robot system that aims to overcome these limitations and enable helpful mobile manipulation skills that can understand human commands and generalize ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Learning-based methods have achieved strong performance for quadrupedal locomotion.
- **p. 1 / Abstract - extractive body cue:** However, several challenges prevent quadrupeds from learning helpful indoor skills that require interaction with environments and humans: lack of end-effectors for manipulation, limited semantic understanding ...
- **p. 1 / Abstract - extractive body cue:** We present a system for quadrupedal mobile manipulation in indoor environments.
- **p. 1 / Abstract - extractive body cue:** It uses a front-mounted gripper for object manipulation, a lowlevel controller trained in simulation using egocentric depth for agile skills like climbing and whole-body tilting, ...
- **p. 1 / Abstract - extractive body cue:** We evaluate our system in two unseen environments without any real-world data collection or training.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Several key challenges have hindered progress in this direction.
- **p. 2 / I. INTRODUCTION - extractive body cue:** On the semantic perception and control front for solving useful tasks, instead of relying on collecting human demonstrations that is time-consuming or simulation that has ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In this paper, we present Helpful DoggyBot, a quadrupedal robot system that aims to overcome these limitations and enable helpful mobile manipulation ... | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | The output of this estimator replaces the scandots input to the base policy learned in Phase 1. | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF body |
| State / latent | output, estimator, replaces, scandots, input, base, policy, learned, Phase, VLM | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | convert, angular, velocity, command, policy, input, calculates, difference | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: output, estimator, replaces, scandots, input, base, policy, learned, Phase, VLM | p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER) |
| Decision / output variable | joint action/torque/footstep; body terms: contributions, system, include, simple, effective, DoF, gripper, design | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: introduce, auxiliary, rewards, maintaining, balance, minimizing, energy, consumption | p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER) |
| Success / guarantee | progress, balance and terrain robustness | p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Several key challenges have hindered progress in this direction.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Notably, our system achieves this generalization without any real-world data collection or training, highlighting the potential of our approach for creating helpful quadrupedal assistants that ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** On the semantic perception and control front for solving useful tasks, instead of relying on collecting human demonstrations that is time-consuming or simulation that has ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 2 (I. INTRODUCTION)): The key contributions of our system include (1) a simple yet effective 1-DoF gripper design that enables object grasping for quadrupeds, (2) a general-purpose low-level controller trained in simulation that ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present Helpful DoggyBot, a quadrupedal robot system that aims to overcome these limitations and enable helpful mobile manipulation skills that can ...
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** Our online estimator architecture consists of a convolutional neural network (CNN) followed by a gated recurrent unit (GRU) to process the temporal sequence of depth ...
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** We introduce auxiliary rewards for maintaining balance, minimizing energy consumption, and smooth transitions between different locomotion modes (e.g., walking, climbing, and tilting).
- **p. 2 / I. INTRODUCTION - extractive body cue:** Notably, our system achieves this generalization without any real-world data collection or training, highlighting the potential of our approach for creating helpful quadrupedal assistants that ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | While our approach demonstrates progress, limitations include the gripper's restricted dexterity, reliance on ceiling-mounted cameras for navigation, and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Go2 default controller fails to climb up high obstacles like beds and sofas, whereas No Tracking only generates ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | This controller does not use exteroception. • Teleop: the commands are generated by an expert human operator through ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We find only small degradation in performance from the oracle policy using priviledged information in Phase 1. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), objective p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
