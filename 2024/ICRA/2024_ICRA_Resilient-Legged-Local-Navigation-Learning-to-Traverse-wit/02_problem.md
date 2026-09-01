# Problem - Resilient Legged Local Navigation: Learning to Traverse with Compromised Perception End-to-End

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.03581; PDF retrieval source: https://arxiv.org/pdf/2310.03581. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However, such manually-designed rules cannot scale well to diverse situations.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Autonomous robots must navigate reliably in unknown environments even under compromised exteroceptive perception, or perception failures.
- **p. 1 / Abstract - extractive PDF cue:** Such failures often occur when harsh environments lead to degraded sensing, or when the perception algorithm misinterprets the scene due to limited generalization.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we model perception failures as invisible obstacles and pits, and train a reinforcement learning (RL) based local navigation policy to guide our ...
- **p. 1 / Abstract - extractive PDF cue:** Unlike previous works relying on heuristics and anomaly detection to update navigational information, we train our navigation policy to reconstruct the environment information in the ...
- **p. 1 / Abstract - extractive PDF cue:** To this end, we incorporate both proprioception and exteroception into our policy inputs, thereby enabling the policy to sense collisions on different body parts and ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, such manually-designed rules cannot scale well to diverse situations.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Generally, given an accurate map, it is not difficult for existing navigation planners to guide the robot towards the local goal safely.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, such manually-designed rules cannot scale well to diverse situations. | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF |
| State / latent | Actor, Critic, Low-Level, Exteroception, Proprioception, Previous, Action, Position, Command, Heading | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | Given, preestablished, low-level, locomotion, policy, train, navigation, generates | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: Actor, Critic, Low-Level, Exteroception, Proprioception, Previous, Action, Position, Command, Heading | p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), p. 2 (III. METHOD) |
| Decision / output variable | joint action/torque/footstep; body terms: incorporate, locomotion-level, observations, navigation, contrasting, existing, methods, typically | p. 1 (I. INTRODUCTION), p. 2 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: Overview, objective, guide, robot, local, target, within, given | p. 2 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Success / guarantee | progress, balance and terrain robustness | p. 5 (V. RESULTS AND ANALYSES), p. 5 (V. RESULTS AND ANALYSES), p. 4 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Generally, given an accurate map, it is not difficult for existing navigation planners to guide the robot towards the local goal safely.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** The learned navigation policy generates velocity commands to a pre-existing low-level locomotion policy, and takes low-level observations as part of its inputs.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 2 (III. METHOD), p. 1 (I. INTRODUCTION)): In this work, we propose to incorporate locomotion-level observations into navigation, contrasting existing methods that typically decouple navigation from locomotion.

- **p. 2 / III. METHOD - extractive PDF cue:** Overview The objective of our method is to guide the robot to a local target within the given time.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** All these cases lead to invisible obstacles and pits for the navigation module, which we call perception failures. † Equal Contribution, listed randomly 1 Robotic ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Despite our policy's generalization to different collision geometries, we find it cannot handle out-of-distribution mapping noises. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | These results indicate that the navigation policy cannot learn to react to perception failures without being exposed to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Fig. 2. Besides reaching the target in time, the robot should also reduce base collisions and avoid falls. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Hence, it is of great interest if we can train a policy to actively explore these areas and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), p. 2 (III. METHOD), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), p. 2 (III. METHOD), p. 1 (I. INTRODUCTION), objective p. 2 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
