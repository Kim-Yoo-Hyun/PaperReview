# Problem - Blind Bipedal Stair Traversal via Sim-to-Real Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss17/p061.html; PDF retrieval source: https://www.roboticsproceedings.org/rss17/p061.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): On stair-like environments, this is especially apparent due to the difficulty of recovery from missteps with only two legs.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Accurate and precise terrain estimation is a difficult problem for robot locomotion in real-world environments.
- **p. 1 / Abstract - extractive body cue:** Thus, it is useful to have systems that do not depend on accurate estimation to the point of fragility.
- **p. 1 / Abstract - extractive body cue:** In this paper, we explore the limits of such an approach by investigating the problem of traversing stair-like terrain without any external perception or terrain ...
- **p. 1 / Abstract - extractive body cue:** For such blind bipedal platforms, the problem appears difficult (even for humans) due to the surprise elevation changes.
- **p. 1 / Abstract - extractive body cue:** Our main contribution is to show that sim-to-real reinforcement learning (RL) can achieve robust locomotion over stair-like terrain on the bipedal robot Cassie using only ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** On stair-like environments, this is especially apparent due to the difficulty of recovery from missteps with only two legs.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Further, integrating a state-ofthe-art computer vision system into a high-speed controller is technically difficult, especially on a computationally limited platform like a mobile robot.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | On stair-like environments, this is especially apparent due to the difficulty of recovery from missteps with only two legs. | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | State Space The state st that is input to the control policy at each time step includes three main components. | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF body |
| State / latent | State, Space, input, control, policy, time, step, includes, three, main | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | While, component, included, control, policy, action, does, appear | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: State, Space, input, control, policy, time, step, includes, three, main | p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION) |
| Decision / output variable | joint action/torque/footstep; body terms: present, training, pipeline, produces, policies, capable, blindly, ascending | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: optimization, objective, considered, learn, policy, through, interaction, environment | p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION) |
| Success / guarantee | progress, balance and terrain robustness | p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 4 (IV. RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Further, integrating a state-ofthe-art computer vision system into a high-speed controller is technically difficult, especially on a computationally limited platform like a mobile robot.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, the limits of this approach are unclear and prior work has not been demonstrated on the scale and variety of disturbances involved in stair-like ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we show that robust proprioceptive bipedal control for complex stair-like terrain can be learned via an existing RL framework with surprisingly little ...

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION)): We present a training pipeline which produces policies capable of blindly ascending and descending stairs in the real world.

- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we show that robust proprioceptive bipedal control for complex stair-like terrain can be learned via an existing RL framework with surprisingly little ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These policies learn proprioceptive reflexes to reject significant disturbances in ground height, resulting in highly robust behavior to many realworld environments. start location or the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Learning on this distribution allows for blind locomotion up and down unknown stairs as well as handling more general stair-like terrain characteristics, e.g. logs, curbs, ...
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Intuitively, this allows the controller to choose an appropriate stepping frequency for a particular gait, command, and terrain.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | In future work, it will be interesting to investigate how vision can be most effectively used to improve ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Fig. 1: In this work, we investigate the limits of blind bipedal locomo- tion. We present a training ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | In this work, we have motivated the desirability of a highly robust but blind walking controller, and demonstrated ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), objective p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
