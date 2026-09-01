# Problem - ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p066.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p066.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 4 (B. Phase-based Motion Tracking Policy Training), p. 4 (B. Phase-based Motion Tracking Policy Training), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract)): However, a successful backflip requires ‘mastering the landing first-if the policy cannot land correctly,

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Humanoid robots hold the potential fr leled versatility for performing. hn
- **p. 1 / Abstract - extractive body cue:** mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP
- **p. 1 / Abstract - extractive body cue:** red to tackle the dynamics ‘whole-body skis.
- **p. 1 / Abstract - extractive body cue:** between first stage, we prestrain motion trac such as using relargeted human motion data.
- **p. 1 / Abstract - extractive body cue:** In the second stage, we (DR) methods, often rely on labor-intensive parameter tuning deploy the in the real world and collect real-world data
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** However, a successful backflip requires ‘mastering the landing first-if the policy cannot land correctly,
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** Crucially, because the actor does not depend on position-based motion targets, ‘our approach eliminates the need for odometry during real world deployment-overcoming a well-documented challenge ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, a successful backflip requires ‘mastering the landing first-if the policy cannot land correctly, | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | As illustrated in Figure 2 (b), the delta action model is defined as Ady = (se, 44)» where the policy 77> leams ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | illustrated, Figure, delta, action, model, defined, Ady, where, policy, leams | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | However, directly, deploying, policy, real, hardware, degraded, performance | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: illustrated, Figure, delta, action, model, defined, Ady, where, policy, leams | p. 5 (B. Training Delta Action Model), p. 2 (Abstract), p. 2 (Abstract) |
| Decision / output variable | joint/whole-body action; body terms: mnparal-, result, overly, conservative, policies, sacrifice, yaper, present | p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: consider, RL-free, methods, fixed-point, iteration, gradient-based, optimization, Fixed | p. 10 (B. Different Usage of Delta Action Model), p. 10 (B. Different Usage of Delta Action Model), p. 11 (B. Different Usage of Delta Action Model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (B. Phase-based Motion Tracking Policy Training), p. 3 (B. Phase-based Motion Tracking Policy Training), p. 3 (B. Phase-based Motion Tracking Policy Training) |
| Success / guarantee | motion/task success and recovery | p. 3 (3) Extensive experiments in both simulation and real-world), p. 3 (3) Extensive experiments in both simulation and real-world), p. 1 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** Crucially, because the actor does not depend on position-based motion targets, ‘our approach eliminates the need for odometry during real world deployment-overcoming a well-documented challenge ...
- **p. 2 / Abstract - extractive body cue:** the sim-to-teal gap, especially when real-world dynamics fall outside the modeled distribution.
- **p. 2 / Abstract - extractive body cue:** However, most prior work [46, 74, 47, 73, 107, 19, 95, 50] has primarily focused ‘on locomotion, treating the legs as a means of mobility.
- **p. 3 / Abstract - extractive body cue:** This model effectively serves as a residual correction term for the dynamics gap.

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 4 (B. Phase-based Motion Tracking Policy Training), p. 5 (C. Fine-tuning Motion Tracking Policy under New Dynamics)): mnparal- or result in overly conservative policies that sacrifice a yaper, we present ASAP

- **p. 2 / Abstract - extractive body cue:** To this end, we propose ASAP, a two-stage framework that aligns the dynamics mismatch between simulation and realworld physics, enabling agile humanoid whole-body skills ASAP ...
- **p. 3 / Abstract - extractive body cue:** 1) We introduce ASAP, a framework that bridges the simto-real gap by leveraging a delta action model trained via reinforcement learning (RL) with real-world data
- **p. 4 / B. Phase-based Motion Tracking Policy Training - extractive body cue:** To mitigate this issue, we introduce a termination curriculum that progressively refines the motion error tolerance throughout training, guiding the policy toward improved tracking performance, ...
- **p. 5 / C. Fine-tuning Motion Tracking Policy under New Dynamics - extractive body cue:** In this section, we present extensive experimental results oon three policy transfers: IsaaeGym [58] to IsaacSim [63], IsaaeGym to Genesis [6], and IsiaeGym to real-world ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 11 | Such structured discrepancies cannot be effectively captured by merely adding uniform action noise. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | + Hardware Constraints: Agile whole-body motions exert significant stress on robots, leading to motor overheating, and hardware failure ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | While ASAP demonstrates promising results in bridging the sim-to-real gap for agile humanoid control, our framework has several ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | However, the performance of the action noise approach (MPJPE of 150) does not match the precision achieved by ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (B. Training Delta Action Model), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 4 (B. Phase-based Motion Tracking Policy Training), p. 4 (B. Phase-based Motion Tracking Policy Training), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), interface p. 5 (B. Training Delta Action Model), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), objective p. 10 (B. Different Usage of Delta Action Model), p. 10 (B. Different Usage of Delta Action Model), p. 11 (B. Different Usage of Delta Action Model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
