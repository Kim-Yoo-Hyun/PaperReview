# Problem - DreamWaQ: Learning Robust Quadrupedal Locomotion with Implicit Terrain Imagination via Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2301.10602; PDF retrieval source: https://arxiv.org/pdf/2301.10602. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): This dilemma is often called the representation learning bottleneck [25], which can hinder optimal policy learning.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Quadrupedal robots resemble the physical ability of legged animals to walk through unstructured terrains.
- **p. 1 / Abstract - extractive body cue:** However, designing a controller for quadrupedal robots poses a significant challenge due to their functional complexity and requires adaptation to various terrains.
- **p. 1 / Abstract - extractive body cue:** Recently, deep reinforcement learning, inspired by how legged animals learn to walk from their experiences, has been utilized to synthesize natural quadrupedal locomotion.
- **p. 1 / Abstract - extractive body cue:** However, state-of-the-art methods strongly depend on a complex and reliable sensing framework.
- **p. 1 / Abstract - extractive body cue:** Furthermore, prior works that rely only on proprioception have shown a limited demonstration for overcoming challenging terrains, especially for a long distance.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This dilemma is often called the representation learning bottleneck [25], which can hinder optimal policy learning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Unlike wheeled mobile robots, quadrupedal robots can traverse unstructured terrains but are relatively difficult to control.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This dilemma is often called the representation learning bottleneck [25], which can hinder optimal policy learning. | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | 1) Policy Network: The policy, πφ(at/ot, vt, zt) is a neural network parameterized by φ that infers an action at, given a ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Policy, Network, at/ot, neural, parameterized, infers, action, given, proprioceptive, observation | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | total, reward, policy, taking, action, state, given, riwi | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: Policy, Network, at/ot, neural, parameterized, infers, action, given, proprioceptive, observation | p. 2 (II. DREAMWAQ), p. 2 (II. DREAMWAQ), p. 3 (II. DREAMWAQ) |
| Decision / output variable | joint action/torque/footstep; body terms: framework, called, Dream, Walking, Quadrupedal, Robots, DreamWaQ, trains | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (II. DREAMWAQ) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: However, reward, minimizes, overall, power, without, considering, motor | p. 3 (II. DREAMWAQ), p. 3 (II. DREAMWAQ) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (II. DREAMWAQ), p. 2 (II. DREAMWAQ), p. 4 (II. DREAMWAQ) |
| Success / guarantee | progress, balance and terrain robustness | p. 4 (Figure/Table caption), p. 4 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Unlike wheeled mobile robots, quadrupedal robots can traverse unstructured terrains but are relatively difficult to control.

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (II. DREAMWAQ), p. 3 (II. DREAMWAQ), p. 1 (I. INTRODUCTION)): In this paper, we proposed a framework called Dream Walking for Quadrupedal Robots (DreamWaQ), that trains a robust locomotion policy for quadrupedal robots with ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work are threefold:
- **p. 2 / II. DREAMWAQ - extractive body cue:** The reward function consists of task rewards for tracking the
- **p. 3 / II. DREAMWAQ - extractive body cue:** Therefore, we introduced a power distribution reward to reduce motor overheating in the real world by penalizing motors' power with high variance over all motors ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** 20018216, "Development of Mobile Intelligence SW for Autonomous Navigation of Legged Robots in Dynamic and Atypical Environments for Real Application").

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | DreamWaQ's limitation lies in its adaptation mechanism, where it must first hit the obstacles with its legs. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | In severe cases, inaccurate estimation can lead to catastrophic failure. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | (a) Foot stumble Foot slip Normal walk Normal walk Normal walk Climb upstairs Go downstairs Irregular foothold Adaptation ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | 6 shows the robot's foot reflex when faced with foot stumbling and slipping. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (II. DREAMWAQ), p. 2 (II. DREAMWAQ), p. 3 (II. DREAMWAQ), p. 3 (II. DREAMWAQ). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 2 (II. DREAMWAQ), p. 2 (II. DREAMWAQ), p. 3 (II. DREAMWAQ), p. 3 (II. DREAMWAQ), objective p. 3 (II. DREAMWAQ), p. 3 (II. DREAMWAQ).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
