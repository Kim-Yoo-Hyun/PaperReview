# Problem - DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/LRA.2020.2977257; PDF retrieval source: https://doi.org/10.1109/LRA.2020.2977257. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): [12], [13], [14], [15], the main bottleneck for wide adoption of touch sensing in robotic manipulation is the lack of sensors that fulfill at the same time all the requirements ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Despite decades of research, general purpose inhand manipulation remains one of the unsolved challenges of robotics.
- **p. 1 / Abstract - extractive body cue:** One of the contributing factors that limit current robotic manipulation systems is the difficulty of precisely sensing contact forces - sensing and reasoning about contact ...
- **p. 1 / Abstract - extractive body cue:** As a step towards enabling better robotic manipulation, we introduce DIGIT, an inexpensive, compact, and high-resolution tactile sensor geared towards in-hand manipulation.
- **p. 1 / Abstract - extractive body cue:** DIGIT improves upon past vision-based tactile sensors by miniaturizing the form factor to be mountable on multi-fingered hands, and by providing several design improvements that ...
- **p. 1 / Abstract - extractive body cue:** We demonstrate the capabilities of the DIGIT sensor by training deep neural network model-based controllers to manipulate glass marbles in-hand with a multi-finger robotic hand.
- **p. 1 / I. INTRODUCTION - extractive body cue:** [12], [13], [14], [15], the main bottleneck for wide adoption of touch sensing in robotic manipulation is the lack of sensors that fulfill at the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** One contributing factor is the difficulty of precisely estimating contact forces.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | [12], [13], [14], [15], the main bottleneck for wide adoption of touch sensing in robotic manipulation is the lack of sensors that ... | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | Second, we demonstrate the sensor by learning to manipulate small objects with a multi-finger hand from raw tactile inputs. | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF |
| State / latent | Second, demonstrate, sensor, learning, manipulate, small, objects, multi-finger, hand, tactile | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | reason, conjunction, release, design, sensor, digit, ACCEPTED, JANUARY | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: Second, demonstrate, sensor, learning, manipulate, small, objects, multi-finger, hand, tactile | p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION) |
| Decision / output variable | contact-aware action/force; body terms: better, fulfill, requirements, present, design, novel, tactile, sensor | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | contact prediction/control error; cue terms: provide, robotic, community, access, reliable, low-cost, tactile, sensors | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Success / guarantee | slip/contact success and safe interaction | p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** One contributing factor is the difficulty of precisely estimating contact forces.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): To better fulfill these requirements, in this paper, we present the design of a novel tactile sensor.

- **p. 1 / I. INTRODUCTION - extractive body cue:** First, we present the design and manufacturing process of DIGIT, and analyze the properties of the resulting sensor.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To scale up tactile-MPC, we propose new approaches for dynamics model learning and task specification that dramatically reduce the computational cost.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | This is a very challenging task because it requires controlling the slipping and rolling dynamics of the marble ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | 3) and the robustness of the gel (Section III-D), we now evaluate the DIGIT in the complex in-hand ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | (Bottom) Due to control noise, potential planning inaccuracies and the challenging nature of this task, the hand tends ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
