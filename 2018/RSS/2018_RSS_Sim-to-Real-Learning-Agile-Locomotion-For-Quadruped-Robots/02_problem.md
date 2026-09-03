# Problem - Sim-to-Real: Learning Agile Locomotion For Quadruped Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsproceedings.org/rss14/p10.html; PDF retrieval source: https://arxiv.org/pdf/1804.10332. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Overcoming the reality gap is challenging.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Designing agile locomotion for quadruped robots often requires extensive expertise and tedious manual tuning.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present a system to automate this process by leveraging deep reinforcement learning techniques.
- **p. 1 / Abstract - extractive body cue:** Our system can learn quadruped locomotion from scratch using simple reward signals.
- **p. 1 / Abstract - extractive body cue:** In addition, users can provide an open loop reference to guide the learning process when more control over the learned gait is needed.
- **p. 1 / Abstract - extractive body cue:** The control policies are learned in a physics simulator and then deployed on real robots.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Overcoming the reality gap is challenging.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Even worse, this gap is greatly amplified in locomotion tasks.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Overcoming the reality gap is challenging. | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | If we want a policy that is learned from scratch, we can set ¯a(t) = 0 and give the feedback component π(o) ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF body |
| State / latent | want, policy, learned, scratch, give, feedback, component, wide, output, range | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | More, importantly, compact, observation, space, helps, transfer, policy | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: want, policy, learned, scratch, give, feedback, component, wide, output, range | p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS) |
| Decision / output variable | joint action/torque/footstep; body terms: main, contributions, complete, learning, system, agile, locomotion, present | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: Reinforcement, learning, optimizes, policy, maximizes, expected, return, accumulated | p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS) |
| Success / guarantee | progress, balance and terrain robustness | p. 8 (Figure/Table caption), p. 6 (VI. EVALUATION AND DISCUSSION), p. 7 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Even worse, this gap is greatly amplified in locomotion tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) We show that the reality gap can be narrowed by a variety of approaches and conduct comprehensive evaluations on their effectiveness.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS)): The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion.

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a complete learning system for agile locomotion, in which control policies are learned in simulation and deployed on real robots.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that with deep RL, highly agile locomotion gaits can emerge automatically.
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** For this reason, we decouple the locomotion controller into two parts, an open loop component that allows a user to provide reference trajectories and a ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | However, when the policies were deployed on the robot, we had mixed results due to the reality gap: ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Note that while this open loop controller expresses the user's preference of the locomotion style, by itself, it ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Fig. 1: The simulated and the real Minitaurs learned to gallop using deep reinforcement learning. to locomotion tasks ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | This points us to two interesting avenues for future work. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), objective p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, when the policies were deployed on the robot, we had mixed results due to the reality gap: Some policies can transfer while others cannot. (p. 6, VI. EVALUATION AND DISCUSSION).
- **Formulation-changing contribution:** The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion. (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** However, the binary outcome of success or failure does not capture the key characteristics of locomotion, such as running speed and energy consumption. (p. 7, B. Narrowing the Reality Gap).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
