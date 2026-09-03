# Problem - SATA: Safe and Adaptive Torque-Based Locomotion Policies Inspired by Animal Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p124.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p124.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (1. Iyrropuction), p. 2 (1. Iyrropuction), p. 2 (1. Iyrropuction), p. 4 (A. Biomechanical Modet)): However, challenges such as a highly nonlinear state ‘space and inefficient exploration during training have hindered their broader adoption, To address these limit

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Despite recent advances in learning-based con~ trollers for legged robots, deployments in human-centrie env ronments remain limited by safety concerns.
- **p. 1 / Abstract - extractive body cue:** Most of these approaches use position-based control, where policies output target joint angles that must be processed hy a low-level controller (e.g PD or impedance ...
- **p. 1 / Abstract - extractive body cue:** Although impressive results have been achieved in controlled real-world scenarios, these methods often struggle with compliance and adaptability when encountering environments or disturbances ‘unseen during ...
- **p. 1 / Abstract - extractive body cue:** Inspired by how animals achieve smooth and adaptive movements by controlling muscle extension and contraction, torque-based policies offer a promising alternative by enabling precise and ...
- **p. 1 / Abstract - extractive body cue:** In Principle, this approach facilitates more effective interactions
- **p. 1 / Abstract - extractive body cue:** However, challenges such as a highly nonlinear state ‘space and inefficient exploration during training have hindered their broader adoption, To address these limit
- **p. 1 / 1. Iyrropuction - extractive body cue:** However, this simplicity limits the policy's capacity to explore fine-grained and dynamic behaviors, thereby reducing its adaptability and generalization to unseen challenges in real-world environments.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, challenges such as a highly nonlinear state ‘space and inefficient exploration during training have hindered their broader adoption, To address these ... | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | Learning-based controllers typically use position-based action spaces, where the policy directly outputs position com- ‘mands for the actuators. ‘These commands are subsequently ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Learning-based, controllers, typically, position-based, action, spaces, where, policy, directly, outputs | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | successfully, trained, torque, policy, incorporating, additional, reward, terms | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: Learning-based, controllers, typically, position-based, action, spaces, where, policy, directly, outputs | p. 2 (1. Iyrropuction), p. 4 (A. Biomechanical Modet), p. 2 (1. Iyrropuction) |
| Decision / output variable | joint action/torque/footstep; body terms: Stable, Efficient, Torque-Based, Learning, novel, framework, loco-, motion | p. 2 (1. Iyrropuction), p. 5 (IV. GROWTH-BASED TRAINING), p. 2 (1. Iyrropuction) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: Similarly, allows, robot, adapt, reward, priorities, align, specific | p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Implementation of the Growth Mechanism) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (A. Implementation of the Growth Mechanism), p. 5 (IV. GROWTH-BASED TRAINING), p. 5 (IV. GROWTH-BASED TRAINING) |
| Success / guarantee | progress, balance and terrain robustness | p. 7 (A. Simulation Experiments), p. 7 (A. Simulation Experiments), p. 5 (A. Implementation of the Growth Mechanism) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Iyrropuction - extractive body cue:** However, this simplicity limits the policy's capacity to explore fine-grained and dynamic behaviors, thereby reducing its adaptability and generalization to unseen challenges in real-world environments.
- **p. 2 / 1. Iyrropuction - extractive body cue:** Moreover, reliance on exteroception Introduces additional challenges, such as the sim-to-real gap, ‘where sensor noise, latency, and real-world variations degrade performance.
- **p. 2 / 1. Iyrropuction - extractive body cue:** By addressing the inherent challenges in torque-based poliy learning. our approach not only provides a robust and efficient solution for torque-based control but also demonstrates ...
- **p. 4 / A. Biomechanical Modet - extractive body cue:** Compared to directly using the neural network's output as joint torques, our approach aims to reduce exploration difficulty during training and improve motion continuity.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Iyrropuction), p. 5 (IV. GROWTH-BASED TRAINING), p. 2 (1. Iyrropuction), p. 1 (1. Iyrropuction), p. 3 (1. Iyrropuction)): + Stable and Efficient Torque-Based Learning: We propose «novel framework for learning torque-based loco- ‘motion policies with a growth mechanism that gradually. unlocks torque limits, control frequency, and reward terms, ...

- **p. 5 / IV. GROWTH-BASED TRAINING - extractive body cue:** Due to the highly nonlinear nature of the torque space, training a torque-based policy poses greater challenges than a position-based one, especially during early-stage exploration. ...
- **p. 2 / 1. Iyrropuction - extractive body cue:** By directly controlling actuation in torque space, this approach enables finer interaction with the environment, leading to more dynamic and robust locomotion, Moreover. torque control ...
- **p. 1 / 1. Iyrropuction - extractive body cue:** 1 of animals in nature, we propose a framework that addresses the challenges ‘of torque-based lecomosion learning achieving 2roshot sim-o-real tanser slong with exceptional compliance ...
- **p. 3 / 1. Iyrropuction - extractive body cue:** ‘To achieve robust and adaptive locomotion contro! in legged robots, we propose a bio-inspired neural architecture that em

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | [Locomotion on wet slippery surfaces, showing both sucess (a) and failure (b), Even when the foot ofthe robot ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | In contrast, Figure 11b shows a failure case, where the robot is given an abrupt command on the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | 2) Robustness to Single-Leg Failure: In this experiment, we simulate the failure of a single leg by abruptly ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This dynamic redistribution of effort ensures continuous and stable locomotion even under single leg failures. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Iyrropuction), p. 4 (A. Biomechanical Modet), p. 2 (1. Iyrropuction), p. 3 (1. Iyrropuction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Abstract), p. 1 (1. Iyrropuction), p. 2 (1. Iyrropuction), p. 2 (1. Iyrropuction), p. 4 (A. Biomechanical Modet), interface p. 2 (1. Iyrropuction), p. 4 (A. Biomechanical Modet), p. 2 (1. Iyrropuction), p. 3 (1. Iyrropuction), objective p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Implementation of the Growth Mechanism).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
