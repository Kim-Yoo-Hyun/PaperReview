# Problem - Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Bl2VfU9NhF; PDF retrieval source: https://arxiv.org/pdf/2505.24198. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): The nature of ground contacts makes it more susceptible to the sim-to-real gap, demanding greater robustness against noise and disturbances.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Can your humanoid walk up and hand you a full cup of beer-without spilling a drop?
- **p. 1 / Abstract - extractive body cue:** While humanoids are increasingly featured in flashy demos-dancing, delivering packages, traversing rough terrain-fine-grained control during locomotion remains a significant challenge.
- **p. 1 / Abstract - extractive body cue:** In particular, stabilizing a filled end-effector (EE) while walking is far from solved, due to a fundamental mismatch in task characteristics: locomotion demands slow-timescale, robust ...
- **p. 1 / Abstract - extractive body cue:** To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with ...
- **p. 1 / Abstract - extractive body cue:** This temporal and objective separation mitigates policy interference and enables coordinated whole-body behavior.
- **p. 2 / 1 Introduction - extractive body cue:** The nature of ground contacts makes it more susceptible to the sim-to-real gap, demanding greater robustness against noise and disturbances.
- **p. 2 / 1 Introduction - extractive body cue:** To bridge the gap, we propose SoFTA-a Slow-Fast Two-Agent reinforcement learning (RL) framework that decouples the action and value spaces of the upper and lower ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The nature of ground contacts makes it more susceptible to the sim-to-real gap, demanding greater robustness against noise and disturbances. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | The actor relies solely on onboard-accessible inputs-proprioception, command signals, and recent actions-excluding global position data, thus removing dependence on odometry or external ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | actor, relies, solely, onboard-accessible, inputs-proprioception, command, signals, recent, actions-excluding, global | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | include, general, PPO, settings, action, different, body, modules | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: actor, relies, solely, onboard-accessible, inputs-proprioception, command, signals, recent, actions-excluding, global | p. 15 (A.1 Training Details), p. 15 (A.1 Training Details), p. 17 (A.1 Training Details) |
| Decision / output variable | joint/whole-body action; body terms: contributions, introduce, SoFTA, novel, slow-fast, two-agent, framework, decouples | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 16 (A.1 Training Details) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: Notice, termination, shared, reward, component, introduce, several, penalties | p. 17 (A.1 Training Details), p. 16 (A.1 Training Details) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 16 (A.1 Training Details), p. 17 (A.1 Training Details), p. 17 (A.1 Training Details) |
| Success / guarantee | motion/task success and recovery | p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 16 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** To bridge the gap, we propose SoFTA-a Slow-Fast Two-Agent reinforcement learning (RL) framework that decouples the action and value spaces of the upper and lower ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 16 (A.1 Training Details), p. 16 (A.1 Training Details)): Our key contributions are: • We introduce SoFTA, a novel slow-fast two-agent RL framework that decouples control for locomotion and EE stabilization in both temporal and task objective space, enabling ...

- **p. 2 / 1 Introduction - extractive body cue:** To bridge the gap, we propose SoFTA-a Slow-Fast Two-Agent reinforcement learning (RL) framework that decouples the action and value spaces of the upper and lower ...
- **p. 16 / A.1 Training Details - extractive body cue:** After obtaining a stable policy, we introduce push disturbances to further improve robustness under external disturbance.
- **p. 16 / A.1 Training Details - extractive body cue:** Notice that the termination is a shared reward component Also, we introduce several penalties and energy regularization in order to achieve robust sim-to-real performance like ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Figure 7: Max Acc under Different Control Frequencies in Simulation and Real World: Higher values reflect reduced stability. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 6 Limitation Despite its strong performance, SoFTA still faces several limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | First, while it significantly reduces EE acceleration, the achieved stability still falls short of human-level performance. | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | We observe that increasing the upper-body control frequency reduces recovery time (defined as the time when the error ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 15 (A.1 Training Details), p. 15 (A.1 Training Details), p. 17 (A.1 Training Details), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 15 (A.1 Training Details), p. 15 (A.1 Training Details), p. 17 (A.1 Training Details), p. 2 (1 Introduction), objective p. 17 (A.1 Training Details), p. 16 (A.1 Training Details).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
