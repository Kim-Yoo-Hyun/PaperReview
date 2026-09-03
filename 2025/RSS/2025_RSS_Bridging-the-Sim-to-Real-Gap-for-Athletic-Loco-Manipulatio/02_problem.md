# Problem - Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p125.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p125.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (Body text (section not recovered)), p. 1 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 3 (A. Unsupervised Actuator Net)): However, training solely with task rewards introduces two major challenges: these rewards are prone (o exploitation (reward hacking), and the exploration process can lack sufficient direction.

## PDF Body Digest

- **p. 1 / Body text (section not recovered) - extractive body cue.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation
- **p. 1 / Body text (section not recovered) - extractive body cue:** Improbable Al Lab.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Achieving athletic loco-manipulation on robots requires moving beyond traditional tracking rewards-which simply guide the robot along a reference trajectory-to task rewards that drive truly dynamic, ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Commands such as "throw the ball as far as you can" or "lift the weight as quickly as possible" compel the robot to exhibit the ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** However, training solely with task rewards introduces two major challenges: these rewards are prone (o exploitation (reward hacking), and the exploration process can lack sufficient ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** However, these task rewards pose two major challenges: (i) they are prone 10 reward hacking, where the policy exploits imperfections in the simulation, and (i) ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, training solely with task rewards introduces two major challenges: these rewards are prone (o exploitation (reward hacking), and the exploration process ... | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Observation, Space, policy, consists, proprioceptive, readings, robot, onboard, sors, including | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | policy, track, reference, trajectories, provided, sequence, base, velocity | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: Observation, Space, policy, consists, proprioceptive, readings, robot, onboard, sors, including | p. 3 (B. Whole-body Controller Pre-training), p. 3 (B. Whole-body Controller Pre-training), p. 2 (1. Iyrropucrion) |
| Decision / output variable | joint action/torque/footstep; body terms: Rather, enforcing, strict, adherence, reference, trajectory, treating, hint | p. 2 (1. Iyrropucrion), p. 1 (Body text (section not recovered)), p. 2 (A. Unsupervised Actuator Net) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: tracking, term, rewards, minimizing, distance, between, four, points | p. 4 (B. Whole-body Controller Pre-training), p. 4 (B. Whole-body Controller Pre-training) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (A. Comparing System Identification Approaches), p. 3 (B. Whole-body Controller Pre-training), p. 5 (A. Comparing System Identification Approaches) |
| Success / guarantee | progress, balance and terrain robustness | p. 5 (A. Comparing System Identification Approaches), p. 5 (Figure/Table caption), p. 4 (B. Whole-body Controller Pre-training) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Iyrropucrion - extractive body cue:** However, these task rewards pose two major challenges: (i) they are prone 10 reward hacking, where the policy exploits imperfections in the simulation, and (i) ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Building on this enhanced simulation environment, we audress the challenge of guided exploration for athletic behaviors.
- **p. 2 / 1. Iyrropucrion - extractive body cue:** The real-to-sim calibration phase involves collecting data on the real robot and training a UAN to close the sim-to-real gap for non-ideal actuation mechanisms.
- **p. 3 / A. Unsupervised Actuator Net - extractive body cue:** Our training pipeline involves three steps: 1) Train a UAN to close the sim-to-real gap for actuators with complex transmission mechanisms by mapping a history ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Iyrropucrion), p. 1 (Body text (section not recovered)), p. 2 (A. Unsupervised Actuator Net), p. 3 (A. Unsupervised Actuator Net), p. 3 (B. Whole-body Controller Pre-training)): Rather than enforcing strict adherence to a reference trajectory, we propose treating it as a hint to guide exploration, In our approach, « WBC is frst pre-trained on random base ...

- **p. 1 / Body text (section not recovered) - extractive body cue:** First, we introduce the Un= supervised Actuator Net (UAN), which leverages real-world data {o bridge the sim-to-real gap for complex actuation mechanisms without requiring access ...
- **p. 2 / A. Unsupervised Actuator Net - extractive body cue:** Alternatively, we propose a method for matching the transition dynamics of the actuator such that
- **p. 3 / A. Unsupervised Actuator Net - extractive body cue:** Each training episode consists of a 20s rollout executing the torque sequence from the hardware data from 3, t0 8744.20 Through taining on rollouts, the ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected in the robot's ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | During development, the Unitree ZI Pro arm experienced structural failures at inks 2 and 4, with minor deformations ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Meanwhile, the Default, DR, and ROA policies produced unstable behaviors-the Default policy, for instance, strayed excessively and failed ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | ‘To avoid the reliance on high-quality pre-training, another possibility is to discard the explicit notion of reference trajectories ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | For this comparison, wwe train and test policies with a fixed-base arm, to avoid the risk of the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (B. Whole-body Controller Pre-training), p. 3 (B. Whole-body Controller Pre-training), p. 2 (1. Iyrropucrion), p. 4 (B. Whole-body Controller Pre-training). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Body text (section not recovered)), p. 1 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 3 (A. Unsupervised Actuator Net), interface p. 3 (B. Whole-body Controller Pre-training), p. 3 (B. Whole-body Controller Pre-training), p. 2 (1. Iyrropucrion), p. 4 (B. Whole-body Controller Pre-training), objective p. 4 (B. Whole-body Controller Pre-training), p. 4 (B. Whole-body Controller Pre-training).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
