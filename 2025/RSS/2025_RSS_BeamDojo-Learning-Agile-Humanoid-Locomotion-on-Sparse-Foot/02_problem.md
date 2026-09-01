# Problem - BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p068.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p068.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. INrRopucTION), p. 1 (Abstract), p. 2 (1. INrRopucTION), p. 2 (1. INrRopucTION), p. 3 (B. Reinforcement Learning in Locomotion Control)): However, these methods encounter great challenges when applied to humanoid robots, primarily due to a key difference

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Traversing risky terrains with sparse footholds poses f significant challenge for humanoid robot iri foot placements and stable locomotion.
- **p. 1 / Abstract - extractive PDF cue:** E approaches often struggle on such complex terrains due to sparse foothold rewards and inefficient learning processes.
- **p. 1 / Abstract - extractive PDF cue:** To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds.
- **p. 1 / Abstract - extractive PDF cue:** BEAMDOJO begins by introducing a sampling-based foothold reward tailored for polygonal feet, along with a double critic to balancing the learning process between dense locomotion ...
- **p. 1 / Abstract - extractive PDF cue:** To encourage sufficient trial-and-error exploration, BEAMDOJO incorporates a two-stage RL approach: the first stage relaxes
- **p. 1 / 1. INrRopucTION - extractive PDF cue:** However, these methods encounter great challenges when applied to humanoid robots, primarily due to a key difference
- **p. 2 / 1. INrRopucTION - extractive PDF cue:** Enabling agile movement on risky terrains for humanoid robots presents several challenges.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these methods encounter great challenges when applied to humanoid robots, primarily due to a key difference | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | 1) Observation Space and Action Space: ‘The policy observations, denoted a8 o,, consist of four components: 0 = [61 0f°"*, of", a ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | Observation, Space, Action, policy, observations, denoted, consist, four, components, commands | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | dynamics, training, humanoid, flat, terr, providing, task-terrain, perceptive | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Observation, Space, Action, policy, observations, denoted, consist, four, components, commands | p. 5 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 1 (Abstract) |
| Decision / output variable | joint/whole-body action; body terms: address, challenges, introduce, BEAMDOJO, reinforcement, learning, framework, designed | p. 1 (Abstract), p. 2 (1. INrRopucTION), p. 2 (1. INrRopucTION) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: primary, objective, optimize, policy, maximize, discounted, cumulative, rewards | p. 3 (B. Double Critic for Sparse Reward Learning), p. 2 (1. INrRopucTION), p. 2 (1. INrRopucTION), p. 3 (B. Reinforcement Learning in Locomotion Control), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 1 (Abstract), p. 1 (Abstract) |
| Success / guarantee | motion/task success and recovery | p. 7 (B. Simulation Experiments), p. 7 (A. Experimental Setup), p. 10 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive PDF cue:** Traversing risky terrains with sparse footholds poses f significant challenge for humanoid robot iri foot placements and stable locomotion.
- **p. 2 / 1. INrRopucTION - extractive PDF cue:** Enabling agile movement on risky terrains for humanoid robots presents several challenges.
- **p. 2 / 1. INrRopucTION - extractive PDF cue:** Additionally, obtaining reliable percep tual information is challenging due to sensory limitations and environmental noise [66]
- **p. 3 / B. Reinforcement Learning in Locomotion Control - extractive PDF cue:** In contrast, this work introduces a novel two-stage training approach specitically aimed at improving sample efficiency, particularly addressing. the challenge of early termination when walking ...

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 2 (1. INrRopucTION), p. 2 (1. INrRopucTION), p. 3 (A. Foothold Reward), p. 1 (Front matter)): To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds.

- **p. 2 / 1. INrRopucTION - extractive PDF cue:** In this work, we introduce BEAMDOJO, a novel reinforcement learning-based framework for controlling humanoid robots traversing risky terrains with sparse footholds.
- **p. 2 / 1. INrRopucTION - extractive PDF cue:** + We propose BEAMDOIO, a two-stage RL framework that combines a newly designed foothold reward for the polygonal foot model and a double critic, enabling ...
- **p. 3 / A. Foothold Reward - extractive PDF cue:** To accommodate the polygonal foot model of the humanoid robot, we introduce a sampling-based foothold reward that evaluates foot placement on sparse footholds.This evaluation
- **p. 1 / Front matter - extractive PDF cue:** 1: Our proposed framework, BEAMDOJO, enables agile and robust humanoid locomotion across challenging sparse foothold.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | 5) Failure Cases: ‘To investigate the framework's perfor- ‘mance limitations, we evaluate its performance across varying. stone sizes ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Meanwhile, the double-critic setup separates the foothold reward from the locomotion rewards, ensuring that its updates remain unaffected ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Fig. 11: Failure Case Analysis. We evaluate the success rate on varying (a) stove sizes, and (b) step ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | before falling to the total terrain length (8 m). | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 1 (Abstract), p. 2 (1. INrRopucTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. INrRopucTION), p. 1 (Abstract), p. 2 (1. INrRopucTION), p. 2 (1. INrRopucTION), p. 3 (B. Reinforcement Learning in Locomotion Control), interface p. 5 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 1 (Abstract), p. 2 (1. INrRopucTION), objective p. 3 (B. Double Critic for Sparse Reward Learning), p. 2 (1. INrRopucTION), p. 2 (1. INrRopucTION), p. 3 (B. Reinforcement Learning in Locomotion Control), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
