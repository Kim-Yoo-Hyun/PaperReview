# Problem - Learning Vision-Based Bipedal Locomotion for Challenging Terrain

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.14594; PDF retrieval source: https://arxiv.org/pdf/2309.14594. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Robustly achieving such an integration of vision and locomotion remains an open problem for bipedal robots.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Reinforcement learning (RL) for bipedal locomotion has recently demonstrated robust gaits over moderate terrains using only proprioceptive sensing.
- **p. 1 / Abstract - extractive body cue:** However, such blind controllers will fail in environments where robots must anticipate and adapt to local terrain, which requires visual perception.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a fully-learned system that allows bipedal robots to react to local terrain while maintaining commanded travel speed and direction.
- **p. 1 / Abstract - extractive body cue:** Our approach first trains a controller in simulation using a heightmap expressed in the robot's local frame.
- **p. 1 / Abstract - extractive body cue:** Next, data is collected in simulation to train a heightmap predictor, whose input is the history of depth images and robot states.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Robustly achieving such an integration of vision and locomotion remains an open problem for bipedal robots.
- **p. 1 / I. INTRODUCTION - extractive body cue:** For this purpose, bipedal robots have the potential to match human locomotion capabilities, but currently are far inferior.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Robustly achieving such an integration of vision and locomotion remains an open problem for bipedal robots. | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | The input to the vision-based modulator includes all of the available observations, including the heightmap, in addition to the action produced by ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF body |
| State / latent | input, vision-based, modulator, includes, available, observations, including, heightmap, addition, action | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | Below, describe, observation, space, action, architecture, policy, training | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: input, vision-based, modulator, includes, available, observations, including, heightmap, addition, action | p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 1 (I. INTRODUCTION), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |
| Decision / output variable | joint action/torque/footstep; body terms: relative, encoding, means, heights, vary, robot, moves, down | p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: However, nature, term, only, acts, soft, constraint, robot | p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |
| Success / guarantee | progress, balance and terrain robustness | p. 5 (VI. SIMULATION RESULTS), p. 6 (Figure/Table caption), p. 5 (VI. SIMULATION RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** For this purpose, bipedal robots have the potential to match human locomotion capabilities, but currently are far inferior.

## What the Paper Changes

PDF body contribution framing (p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY)): The relative encoding means that the heights vary as the robot moves up and down during its gait, but enables us to avoid using global mapping and odometry estimation techniques, ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** The key contribution of our work is the sim-to-real pipeline and the system integration for these components, which allows the overall locomotion controller to transfer ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The proposed approach enables bipedal robot Cassie traversing over challenging terrains, including random high blocks, stairs, 0.5m step up (∼60% leg length), with speed up ...
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** 3: Policy consists of a blind policy and a vision-based modulator. cos (2π(ϕt + γi t)).
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** This allows the policy to gain some experience on easier terrains, which is useful early in learning, but focuses most of the learning effort on ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with different heightmap ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | These random foot collisions with the terrain could lead to failures. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Indeed, Terminations due to foot collision indicates that collisions account for most failure cases overall. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In Termination due to foot collision, compared to LSTM, other models fails with higher chances from unfavorable foot ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 1 (I. INTRODUCTION), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 1 (I. INTRODUCTION), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), objective p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
