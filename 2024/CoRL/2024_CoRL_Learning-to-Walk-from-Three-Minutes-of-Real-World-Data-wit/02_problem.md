# Problem - Learning to Walk from Three Minutes of Real-World Data with Semi-structured Dynamics Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=evCXwlCMIi; PDF retrieval source: https://arxiv.org/pdf/2410.09163. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 6 (1 Introduction), p. 7 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): However, in practice, the black-box neural network models favored in the ∗These authors contributed equally.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Traditionally, model-based reinforcement learning (MBRL) methods exploit neural networks as flexible function approximators to represent a priori unknown environment dynamics.
- **p. 1 / Abstract - extractive PDF cue:** However, training data are typically scarce in practice, and these black-box models often fail to generalize.
- **p. 1 / Abstract - extractive PDF cue:** Modeling architectures that leverage known physics can substantially reduce the complexity of system-identification, but break down in the face of complex phenomena such as contact.
- **p. 1 / Abstract - extractive PDF cue:** We introduce a novel framework for learning semi-structured dynamics models for contact-rich systems which seamlessly integrates structured first principles modeling techniques with black-box auto-regressive models.
- **p. 1 / Abstract - extractive PDF cue:** Specifically, we develop an ensemble of probabilistic models to estimate external forces, conditioned on historical observations and actions, and integrate these predictions using known Lagrangian ...
- **p. 1 / 1 Introduction - extractive PDF cue:** However, in practice, the black-box neural network models favored in the ∗These authors contributed equally.
- **p. 6 / 1 Introduction - extractive PDF cue:** Predictions from semi-structured dynamics models demonstrate greater accuracy and improved generalization beyond training data compared to black-box models.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, in practice, the black-box neural network models favored in the ∗These authors contributed equally. | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | Algorithm 1 Auto-Regressive State Predictions 1: Inputs hallucination buffer Dmodel, models {ˆpi ψi}, policy πθ, start state s0, start history h0 2: ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF |
| State / latent | Algorithm, Auto-Regressive, State, Predictions, Inputs, hallucination, buffer, Dmodel, models, policy | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | optimize, neural, network, policy, conditioned, previous, observations, outputs | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: Algorithm, Auto-Regressive, State, Predictions, Inputs, hallucination, buffer, Dmodel, models, policy | p. 5 (1 Introduction), p. 14 (A.3 Control Architecture), p. 3 (1 Introduction) |
| Decision / output variable | joint action/torque/footstep; body terms: when, combined, accuracy, predictions, over, long-horizons, Section, provides | p. 6 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: Reward, Term, Expression, Weight, Maximize, forward, velocity, Limit | p. 13 (A.2 Reward Function and Termination Condition), p. 14 (A.2 Reward Function and Termination Condition), p. 13 (A.1 Observation and Action Spaces) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 13 (A.2 Reward Function and Termination Condition), p. 13 (A Implementation Details), p. 14 (A.2 Reward Function and Termination Condition) |
| Success / guarantee | progress, balance and terrain robustness | p. 16 (Figure/Table caption), p. 18 (Figure/Table caption), p. 7 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 6 / 1 Introduction - extractive PDF cue:** Predictions from semi-structured dynamics models demonstrate greater accuracy and improved generalization beyond training data compared to black-box models.
- **p. 7 / 1 Introduction - extractive PDF cue:** To assess generalization (Hypothesis 3), we train our semi-structured models and the black-box models from scratch over 3 minutes of saved simulated data using 1- ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Effective robotic agents must leverage complex interactions between the robot and its environment, which are difficult to model using first principles.
- **p. 2 / 1 Introduction - extractive PDF cue:** Currently, both paradigms are too inefficient and unreliable to make learning new behaviors in the real world practical for many applications.

## What the Paper Changes

PDF contribution framing (p. 6 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 7 (1 Introduction)): This, when combined with the accuracy of our predictions over long-horizons (Section 4.2) provides insight into why our approach enables such effective policy optimization [38].

- **p. 3 / 1 Introduction - extractive PDF cue:** The space of observations Ωconsists of the states that can be measured, and the observation distribution O(·/st, at, et) provides (noisy) estimates of the states ...
- **p. 4 / 1 Introduction - extractive PDF cue:** 3 Semi-structured Reinforcement Learning A high-level overview of our method is presented in Fig.
- **p. 5 / 1 Introduction - extractive PDF cue:** 3.4 Policy Optimization Finally, we introduce the Semi-Structured Reinforcement Learning (SSRL) in Algorithm 2.
- **p. 7 / 1 Introduction - extractive PDF cue:** Right-Prediction error for 20-step synthetic rollouts in an unseen environment showcases our method's superior ability to generalize.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | However there are several key limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | 6 Limitations This paper presents a novel framework for model-based reinforcement learning, which leverages physics-informed, semi-structured dynamics models ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | The termination flag dt stops the accumulation of reward after the quadruped falls and is defined by: dt ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | Figure 8: Our approach is robust to errors in a priori knowledge of the robot's inertial properties. B.4 ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (1 Introduction), p. 14 (A.3 Control Architecture), p. 3 (1 Introduction), p. 4 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 6 (1 Introduction), p. 7 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), interface p. 5 (1 Introduction), p. 14 (A.3 Control Architecture), p. 3 (1 Introduction), p. 4 (1 Introduction), objective p. 13 (A.2 Reward Function and Termination Condition), p. 14 (A.2 Reward Function and Termination Condition), p. 13 (A.1 Observation and Action Spaces).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
