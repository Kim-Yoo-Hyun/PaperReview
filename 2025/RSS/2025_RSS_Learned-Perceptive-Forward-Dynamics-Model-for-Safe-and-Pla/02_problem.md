# Problem - Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p001.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p001.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Inrropucrion), p. 2 (1. Inrropucrion), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (B. Planning), p. 3 (A. Dynamics Modeling)): However, open challenges remain to incorporate 3) perception to target rough environments and the transfer from simulation to the real system.

## PDF Body Digest

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Learned Perceptive Forward Dynamics Model for Safe
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 1: Demonstration of the proposed perceptive Forward Dynamics Model for robust navigation in complex environments.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The model, trained with real-world and simulation data, predicts the robots future states given a sequence of velocity actions.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** It takes as input the surrounding geometry in the form of a height scan, along with past states and proprioceptive measurements.
- **p. 2 / 1. Inrropucrion - extractive body cue:** However, open challenges remain to incorporate 3) perception to target rough environments and the transfer from simulation to the real system.
- **p. 2 / 1. Inrropucrion - extractive body cue:** However, training neural networks to represent robot dynamics often requires substantial amounts of state-action trajectories, motivating the use of synthetic data to mitigate the challenges ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, open challenges remain to incorporate 3) perception to target rough environments and the transfer from simulation to the real system. | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | We define ihe state ¥ to be the tuple (p,r), where p © SE2 is the robot's pose and r < {0,1} ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF body |
| State / latent | define, state, tuple, where, SE2, robot, pose, failure, risk, trajectory | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | Given, current, observation, sequence, actions, esn-1, predict, future | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: define, state, tuple, where, SE2, robot, pose, failure, risk, trajectory | p. 3 (A. Dynamics Modeling), p. 2 (A. Dynamics Modeling), p. 3 (A. Dynamics Modeling) |
| Decision / output variable | joint action/torque/footstep; body terms: overcome, issues, novel, learned, perceptive, addresses, domain, discrepancies | p. 1 (Body text (section boundary not confidently recovered)), p. 3 (B. Planning), p. 5 (B. Model Architecture) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: Consequently, objective, dynamics, model, becomes, minimizing, combined, loss | p. 4 (A. Dynamics Modeling), p. 5 (B. Model Architecture), p. 4 (B. Planning), p. 5 (B. Model Architecture), p. 3 (B. Model Predictive Path Integral Control), p. 3 (B. Model Predictive Path Integral Control) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (B. Model Predictive Path Integral Control), p. 5 (B. Model Architecture), p. 4 (B. Planning) |
| Success / guarantee | progress, balance and terrain robustness | p. 10 (C. Platform-aware Predictions), p. 7 (A. FDM Percepriveness), p. 8 (B. Baseline Comparison) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Inrropucrion - extractive body cue:** However, training neural networks to represent robot dynamics often requires substantial amounts of state-action trajectories, motivating the use of synthetic data to mitigate the challenges ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The FDM is trained on multiple years of simulated navigation experience, including high-risk ‘maneuvers, and real-world interactions to incorporate the full system dynamics beyond rigid ...
- **p. 3 / B. Planning - extractive body cue:** While unsupervised approaches rely on simplified dynamics and require manual ccost-map tuning, RL-based planners learn platform-aware behaviors through experience but face sim-to-real transfer challenges due ...
- **p. 3 / A. Dynamics Modeling - extractive body cue:** We define ihe state ¥ to be the tuple (p,r), where p © SE2 is the robot's pose and r < {0,1} is the failure ...

## What the Paper Changes

PDF body contribution framing (p. 1 (Body text (section boundary not confidently recovered)), p. 3 (B. Planning), p. 5 (B. Model Architecture), p. 2 (1. Inrropucrion), p. 2 (1. Inrropucrion)): To overcome these issues, we propose a novel learned perceptive

- **p. 3 / B. Planning - extractive body cue:** Our method addresses domain discrepancies by incorporating real-world data into the ‘dynamics model while maintaining platform awareness through earning from past experiences.
- **p. 5 / B. Model Architecture - extractive body cue:** The Forward Dynamics Model loss £ consists of supervised terms for network outputs.
- **p. 2 / 1. Inrropucrion - extractive body cue:** The main contributions of this work are as follows:
- **p. 2 / 1. Inrropucrion - extractive body cue:** by reducing the need for extensive parameter tuning and providing a flexible solution for non-task-specific planning. ‘This enables zero-shot adaptation to new environments without requiring ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Moreover, demonstrates the most precise failure estimation, although it is less likely to detect all collisions compared to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In the planar environment, robot failures are rare (0.042%), likely caused by simulation instabilities that the model cannot ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | The proposed FDM accurately predicts failures due to collisions and ealy path terminations caused by unlzaversable stars and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (A. Dynamics Modeling), p. 2 (A. Dynamics Modeling), p. 3 (A. Dynamics Modeling), p. 5 (B. Model Architecture). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Inrropucrion), p. 2 (1. Inrropucrion), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (B. Planning), p. 3 (A. Dynamics Modeling), interface p. 3 (A. Dynamics Modeling), p. 2 (A. Dynamics Modeling), p. 3 (A. Dynamics Modeling), p. 5 (B. Model Architecture), objective p. 4 (A. Dynamics Modeling), p. 5 (B. Model Architecture), p. 4 (B. Planning), p. 5 (B. Model Architecture), p. 3 (B. Model Predictive Path Integral Control), p. 3 (B. Model Predictive Path Integral Control).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, open challenges remain to incorporate 3) perception to target rough environments and the transfer from simulation to the real system. (p. 2, 1. Inrropucrion).
- **Formulation-changing contribution:** To overcome these issues, we propose a novel learned perceptive (p. 1, Body text (section boundary not confidently recovered)).
- **Assumption/failure evidence:** Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data lacks demonstrations. of collisions due to the risk of hardware damage, leaving ... (p. 10, C. Platform-aware Predictions).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
