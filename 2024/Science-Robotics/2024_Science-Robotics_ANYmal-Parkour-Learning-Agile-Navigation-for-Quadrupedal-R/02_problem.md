# Problem - ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.14874; PDF retrieval source: https://arxiv.org/pdf/2306.14874. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION)): The complexity of the task exacerbates many of the challenges commonly faced by mobile robots: • The locomotion controller cannot rely on a stable and periodic gait but must use ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Performing agile navigation with four-legged robots is a challenging task due to the highly dynamic motions, contacts with various parts of the robot, and the ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a fully-learned approach to train such robots and conquer scenarios that are reminiscent of parkour challenges.
- **p. 1 / Abstract - extractive body cue:** The method involves training advanced locomotion skills for several types of obstacles, such as walking, jumping, climbing, and crouching, and then using a high-level policy ...
- **p. 1 / Abstract - extractive body cue:** Thanks to our hierarchical formulation, the navigation policy is aware of the capabilities of each skill, and it will adapt its behavior depending on the ...
- **p. 1 / Abstract - extractive body cue:** Additionally, a perception module is trained to reconstruct obstacles from highly occluded and noisy sensory data and endows the pipeline with scene understanding.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The complexity of the task exacerbates many of the challenges commonly faced by mobile robots: • The locomotion controller cannot rely on a stable and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Method overview This work aims to solve the above-mentioned challenges and proposes a method to perform agile navigation with a quadrupedal robot in parkour-like settings ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The complexity of the task exacerbates many of the challenges commonly faced by mobile robots: • The locomotion controller cannot rely on ... | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | As input, the policies receive the current proprioceptive state, a local map of the surrounding terrain, an intermediate command, and output position ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF |
| State / latent | input, policies, receive, current, proprioceptive, state, local, surrounding, terrain, intermediate | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | navigation, locomotion, modules, output, make, path, planning, policy | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: input, policies, receive, current, proprioceptive, state, local, surrounding, terrain, intermediate | p. 14 (IV. MATERIALS AND METHODS), p. 5 (3) We develop a neural terrain reconstruction method that), p. 12 (IV. MATERIALS AND METHODS) |
| Decision / output variable | joint action/torque/footstep; body terms: Despite, promising, close, similarity, requires, human-designed, path, skill | p. 5 (3) We develop a neural terrain reconstruction method that), p. 5 (3) We develop a neural terrain reconstruction method that), p. 3 (I. INTRODUCTION) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: occupancy, output, trained, binary, cross-entropy, loss, while, centroids | p. 14 (IV. MATERIALS AND METHODS), p. 14 (IV. MATERIALS AND METHODS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 14 (IV. MATERIALS AND METHODS), p. 4 (3) We develop a neural terrain reconstruction method that), p. 12 (IV. MATERIALS AND METHODS) |
| Success / guarantee | progress, balance and terrain robustness | p. 8 (Figure/Table caption), p. 5 (II. RESULTS), p. 5 (II. RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Method overview This work aims to solve the above-mentioned challenges and proposes a method to perform agile navigation with a quadrupedal robot in parkour-like settings ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** The robot can cross difficult terrains with speeds of up to 2 m/s and make the right navigation decisions to reach the target in time.
- **p. 3 / I. INTRODUCTION - extractive body cue:** Contributions In our experimental validation, we demonstrate the system's ability to solve the problem autonomously, resulting in behaviors not shown before with such platforms.

## What the Paper Changes

PDF contribution framing (p. 5 (3) We develop a neural terrain reconstruction method that), p. 5 (3) We develop a neural terrain reconstruction method that), p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Despite the promising results and the close similarity to our method, this work requires human-designed path and skill selection and is limited to a single pre-mapped environment with a motion ...

- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** To the best of our knowledge, we propose the first system that can perform agile navigation with a quadrupedal robot in such challenging scenarios without ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** We can summarize our contributions as follows:
- **p. 3 / I. INTRODUCTION - extractive body cue:** Contributions In our experimental validation, we demonstrate the system's ability to solve the problem autonomously, resulting in behaviors not shown before with such platforms.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This discipline requires years of practice to develop the necessary competencies, intuitions, and reflexes and is considered particularly dangerous.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 12 | Finally, since the navigation module must make a series of correct decisions to reach the goal with many ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | We develop a specific curriculum to overcome this limitation. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | 3 (A2)), which is necessary for the leg to reach the other side of the gap and catch ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | At this location, it has to perform precise foothold placement to pass the last step and prepare for ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 14 (IV. MATERIALS AND METHODS), p. 5 (3) We develop a neural terrain reconstruction method that), p. 12 (IV. MATERIALS AND METHODS), p. 12 (IV. MATERIALS AND METHODS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), interface p. 14 (IV. MATERIALS AND METHODS), p. 5 (3) We develop a neural terrain reconstruction method that), p. 12 (IV. MATERIALS AND METHODS), p. 12 (IV. MATERIALS AND METHODS), objective p. 14 (IV. MATERIALS AND METHODS), p. 14 (IV. MATERIALS AND METHODS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
